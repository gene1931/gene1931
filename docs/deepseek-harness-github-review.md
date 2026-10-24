# DeepSeek Harness — GitHub Review (doc notes)

Source: https://deepseek-harness.github.io/deepseek-harness/en/guide/github-review (fetched 2026-10-24)

**What it is**: an opt-in overlay for `dsh web` that adds a signed GitHub webhook
endpoint. When a PR in the configured repo flips from **draft → ready for review**,
a rule creates a titled root *Session* under the repo's Web Workspace and starts a
**read-only** review prompt automatically.

## Prerequisites
- Local checkout DSH can register as a Web Workspace
- `DSH_GITHUB_WEBHOOK_SECRET` credential reference (high-entropy GitHub webhook secret)
- TLS reverse proxy / tunnel exposing one public URL to the loopback listener
- GitHub webhook subscription: **Pull requests** event, content type `application/json`

## Key facts
- Defaults: Workspace = launch dir; listener = `127.0.0.1:3081` (override via
  `DSH_GITHUB_REVIEW_WORKSPACE` / `DSH_GITHUB_WEBHOOK_PORT`)
- Two **experimental** packages required, installed into the **web profile**:
  `dsh plugin --profile web add @deepseek-ai/dsh-webhook @deepseek-ai/dsh-webhook-github`
  (profiles do NOT install peers — the webhook runtime must be explicit)
- Launch: `dsh web --patch "$DSH_HOME:-~/.dsh/profiles/web/node_modules/@deepseek-ai/dsh-webhook-github/examples/github-review/cordis.yml"`
- Example must load from the profile install dir (rule module resolves
  profile-installed peers); copy both example files to
  `~/.dsh/profiles/web/github-review/` to customize, then `--patch` the copy
- Example source: `packages/experimental/webhook-github/examples/github-review/`
- Main Web UI + `/api` stay on :3080; overlay mounts a **second, isolated**
  WebServer where only `POST /github` exists (everything else 404s)
- Caddy snippet exposes only that route: `path /github` → reverse_proxy
  127.0.0.1:3081, else `respond 404`
- GitHub webhook config: Payload URL `https://hooks.example.com/github`,
  secret = DSH_GITHUB_WEBHOOK_SECRET value, event = Pull requests

## Rule behavior
- Accepts only: source `primary-github`, repo `deepseek-ai/deepseek-harness`,
  event `pull_request`, action `ready_for_review`
- Passes exact head SHA + selected PR fields to the review prompt, labeled
  **untrusted metadata**; forbids file/branch/PR/GitHub mutation
- Session request: `standard` agent preset, `read-only` permission preset
- `workspacePath` canonicalized via `WorkspaceRegistry.create()` — first
  matching delivery creates the Web Workspace, later deliveries reuse it
- **HTTP 202 ≠ rule matched**: only "signature + JSON accepted, rule calls
  scheduled in memory" — not a session-creation confirmation

## Programmatic extensions
- `run()` is ordinary trusted JS — can query an internal policy service
  (e.g., only auto-review when `automaticReview === true`) and return `null`
  to skip
- Can map repositories → different local workspace paths (repo-based routing)

## Delivery semantics (important)
- Webhook runtime stores **no** delivery/execution state → repeated delivery
  re-runs the rule and **may create another Session**; a crash loses rule calls
  not yet admitted to a prompt
- After prompt admission, the ordinary Session log/persistence/Workspace/Agent
  lifecycle owns the work
- The webhook secret authenticates **inbound** GitHub data only — it grants no
  outbound GitHub access to rules/Agents; configure that authority separately