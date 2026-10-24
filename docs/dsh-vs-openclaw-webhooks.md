# DSH GitHub-review vs OpenClaw — architecture comparison

Comparison written 2026-10-24 after reading both systems' docs. Companion file:
`docs/deepseek-harness-github-review.md` (the DSH doc notes). <!-- project: path:/home/mail2/.openclaw/workspace -->

## TL;DR
Both are "signed HTTP ingress → filtered by rules → spawn a scoped agent session."
Same security philosophy (untrusted external payloads, least-privilege agents,
HTTP-response ≠ execution outcome). DSH's is purpose-built for one flow (PR
draft→ready → read-only review session with SHA pinned). OpenClaw's
`hooks.*` ingress is generic (any sender → any agent), more elaborate on
session/admission mechanics, and pairs with `gh-issues` + `sessions_spawn`
skills to reproduce the entire DSH feature on this Gateway today.

## Side by side

| Dimension | DeepSeek Harness (`dsh-webhook-github`) | OpenClaw (`hooks.*` + skills) |
|---|---|---|
| Ingress auth | GitHub webhook **HMAC secret** (verifies GitHub as sender) | **Bearer token** (`hooks.token`; header only, `?token=` rejected); throttles 429 after 20 bad attempts/60s; loopback not exempt |
| Sender identity | HMAC proves GitHub, `source: primary-github` rule-gated | Token proves possession, NOT sender identity — docs say treat payload as untrusted |
| Endpoint shape | Dedicated second WebServer in isolated realm; only `POST /github`; all else 404 | One `/hooks` base + `/wake`, `/agent`, `/<name>` mapped endpoints; mappings first-match-wins |
| Payload filtering | Hardcoded rule: repo `deepseek-ai/deepseek-harness`, event `pull_request`, action `ready_for_review` only | `mappings[]` (ordered, first match wins) + `presets` (e.g. `gmail`); arbitrary conditions on payload fields |
| Agent scoping | Session pinned: `standard` agent preset + `read-only` permission preset; SHA-pinned review, mutation forbidden | Per-agent tool/workspace policy instead of a preset; `allowedAgentIds` allowlist; hook token grants ingress only |
| Session targeting | WorkspaceRegistry: first delivery creates repo Web Workspace, later reuse | `sessionKey` policy: `defaultSessionKey`, `allowRequestSessionKey` (default OFF), `allowedSessionKeyPrefixes`; `sessionMode` isolated/persistent |
| Response semantics | **202** = signature+JSON accepted, rule scheduled — explicitly ≠ rule matched/Session created | **200 `{ok, runId}`/`eventOutcome: queued\|coalesced`** = admission — "HTTP success does not prove a model result or channel delivery"; `waitForCompletion: true` upgrades to bounded terminal facts |
| Replay/dup handling | None stored — repeated webhook = repeated review sessions; crash loses un-admitted calls | **`idempotencyKey`** (header or payload) reconciles retries; 15s admission deadline then 503; fan-out continues in background |
| Automation of the flow | Built-in: draft→ready triggers review automatically | Reproduce via automations/cron watchers + `gh-issues` skill; GitHub-triggered means adding an automation that polls or exposing a hook for GitHub actions |
| Outbound authority | Webhook secret grants nothing outbound — configure separately | Same spirit: hook token grants ingress; agent's GitHub ability comes from its own tools/credentials policy |

## The identical security spine (both docs independently)
1. External payloads are untrusted data, never instructions.
2. Admission ≠ execution: HTTP success is deliberately weaker than agent outcome.
3. The listening secret grants nothing beyond ingress; agent capabilities are scoped separately.
4. Sessions/agents are workspace-scoped and permission-limited before any prompt runs.

## Reproducing DSH's PR-review flow on OpenClaw (what's missing today)
1. **Trigger**: GitHub can't HMAC-sign to hooks? It can via webhook to a
   mapping that checks `X-Hub-Signature-256`? — Not built-in: mappings match
   JSON payload fields, not headers. Options: GitHub Actions webhook to
   `/hooks/agent` with the Bearer token (simplest, GitHub-side secret optional),
   or a tiny relay validating HMAC then POSTing `/agent`.
2. **Review session**: `sessions_spawn(mode=run, context="isolated",
   runtime="subagent")` with a read-only-ish review brief — same SHA-pinning and
   mutation-forbidden instruction DSH hardcodes.
3. **Reporting**: hook payload `deliver: true` + `channel/to` posts the review
   back to chat when done.
4. Result: same feature set as DSH's overlay — draft→ready events from GitHub
   Actions, isolated review session, chat-delivered verdict — plus
   idempotency, which DSH explicitly lacks.

## Notable doc wording worth keeping
- OpenClaw: "Hook tokens grant ingress access, not an authenticated sender
  identity; treat payload content as untrusted data and restrict the target
  agent's tools and workspace separately."
- DSH: "The webhook secret authenticates inbound GitHub data only. It grants
  neither rule code nor the created Agent outbound GitHub access."
- Same conclusion, opposite emphasis — keep both.