#!/usr/bin/env python3
"""Build Gene's Sr. AV Administrator/Engineer (xAI JD) resume + cover letter.
Source of truth: GTRez.pdf + Gene-supplied facts (streaming tools past exp: AWS,
Wirecast, OBS, DaVinci Resolve; live production past exp: Dante, DMX, Sony cameras,
ETC lighting; Stream Deck/BitFocus past-not-expert; AI fluency: minor scripting at
work, generative AI + agentic tools in AV and home projects). Rules: <=2p resume,
<=1p letter, no age refs, no years-of-experience numbers, Amazon ends Feb 2026
past tense, South Lake Tahoe + LinkedIn URL, AVIXA multiple past CTS certifications
(not current), education undated, pre-2000 roles as one Earlier Experience line.
Gap-JD honesty: NO claims of vMix/TriCaster/ATEM/Premiere Pro/After Effects, Zoom
Meetings/Webinars specifics, IATSE/union crew relations, RF/satellite, AR/projection
mapping/LED walls, ON24/YouTube/Vimeo platforms, or ROI/financial-case figures —
GTRez supports: multi-camera/broadcast/live event production ops (Amazon virtual
production stage), studio broadcast designs (Meta), budgeting + capital/overhead
planning + vendor coordination (Aerospace, DreamWorks), multi-site team leadership
and standards (EIS/Aerospace, DreamWorks, Meta), SOPs/standards/design
documentation (Meta/Aerospace/DreamWorks), live event technical direction
(DreamWorks/Aerospace/Amazon), deployment programs (Google). Format: Roku
scope+bullets."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                HRFlowable, KeepTogether)

OUT = "/home/mail2/.openclaw/workspace/resume_xai"
os.makedirs(OUT, exist_ok=True)
INK = HexColor("#1a1a1a")
GRAY = HexColor("#555555")
ACCENT = HexColor("#1a3a5c")
LINK = "linkedin.com/in/gene-takahashi-36b8b9/"


def build_resume(path, fs):
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.6*inch, rightMargin=0.6*inch,
                            topMargin=0.5*inch, bottomMargin=0.5*inch,
                            title="Gene Takahashi - Resume",
                            author="Gene Takahashi")
    S = {
        "name": ParagraphStyle("name", fontName="Helvetica-Bold",
                               fontSize=17*fs, leading=20*fs, textColor=INK),
        "headline": ParagraphStyle("headline", fontName="Helvetica",
                                   fontSize=10.5*fs, leading=13*fs, textColor=GRAY),
        "contact": ParagraphStyle("contact", fontName="Helvetica",
                                  fontSize=9.5*fs, leading=12*fs, textColor=GRAY),
        "section": ParagraphStyle("section", fontName="Helvetica-Bold",
                                  fontSize=11*fs, leading=13*fs, textColor=ACCENT,
                                  spaceBefore=10*fs),
        "summary": ParagraphStyle("summary", fontName="Helvetica",
                                 fontSize=9.5*fs, leading=12.6*fs, textColor=INK,
                                 alignment=TA_JUSTIFY),
        "company": ParagraphStyle("company", fontName="Helvetica-Bold",
                                 fontSize=10.3*fs, leading=12.6*fs, textColor=INK,
                                 spaceBefore=7*fs),
        "role": ParagraphStyle("role", fontName="Helvetica",
                              fontSize=9.8*fs, leading=12.2*fs, textColor=INK),
        "scope": ParagraphStyle("scope", fontName="Helvetica",
                               fontSize=9.3*fs, leading=11.8*fs, textColor=INK,
                               alignment=TA_JUSTIFY, spaceBefore=1.5*fs),
        "bullet": ParagraphStyle("bullet", fontName="Helvetica",
                                fontSize=9.3*fs, leading=11.8*fs, textColor=INK,
                                leftIndent=12, bulletIndent=2,
                                alignment=TA_JUSTIFY, spaceBefore=1.2*fs),
        "plain": ParagraphStyle("plain", fontName="Helvetica",
                               fontSize=9.3*fs, leading=12*fs, textColor=INK,
                               leftIndent=12, bulletIndent=2, spaceBefore=1*fs),
        "earlier": ParagraphStyle("earlier", fontName="Helvetica",
                                 fontSize=9.3*fs, leading=12*fs, textColor=INK),
    }
    E = [Paragraph("GENE TAKAHASHI", S["name"]), Spacer(1, 2),
         Paragraph("Sr. AV Administrator / Engineer | Enterprise AV &amp; Live Events", S["headline"]),
         Spacer(1, 2),
         Paragraph(f"South Lake Tahoe, CA &nbsp;|&nbsp; (650) 960-5594 &nbsp;|&nbsp; "
                   f"mail@gene-site.com &nbsp;|&nbsp; {LINK}", S["contact"]),
         HRFlowable(width="100%", thickness=1.4, color=ACCENT, spaceBefore=6)]

    E.append(Paragraph("PROFESSIONAL SUMMARY", S["section"]))
    E.append(Paragraph(
        "Senior AV engineer and administrator \u2014 hands-on owner of the "
        "systems people rely on: designed, installed, and commissioned AV "
        "across multiple 200,000+ sq ft facilities from architectural "
        "drawings to working rooms; supervised a media services team across "
        "three states and multiple field offices; ran live company events, "
        "broadcasts, and all-hands-scale productions from setup through "
        "load-out; and served as the escalation point for the most complex "
        "AV issues (Amazon Studios\u2019 Virtual Production stage \u2014 "
        "displays, cameras, switchers, DSP, machine rooms \u2014 kept "
        "show-ready daily). Experience with some Q-SYS equipment, DSP "
        "concepts, Dante, and IP video (ST 2110 certified) \u2014 with "
        "AI/scripting automation that reduces operational overhead.",
        S["summary"]))

    E.append(Paragraph("PROFESSIONAL EXPERIENCE", S["section"]))

    def exp(company, role, dates, scope, bullets):
        blk = [Paragraph(company, S["company"]),
               Paragraph(f"<b>{role}</b> &nbsp;|&nbsp; {dates}", S["role"]),
               Paragraph(scope, S["scope"])]
        for label, text in bullets:
            blk.append(Paragraph(f"<b>{label}:</b> {text}", S["bullet"],
                                  bulletText="\u2022"))
        E.append(KeepTogether(blk))

    exp("AMAZON STUDIOS, CULVER CITY, CA", "ASVP Engineer",
        "February 2022 \u2013 February 2026",
        "Engineer for a Virtual Production stage used for film, video, and "
        "live broadcast shoots \u2014 hands-on setup, operation, "
        "troubleshooting, and maintenance of the systems productions ran on.",
        [("Escalation Point",
          "Primary escalation for the stage\u2019s most complex AV issues "
          "\u2014 diagnosing integrated hardware/software faults across "
          "displays, cameras, switchers, intercoms, IP video, and machine "
          "rooms, ensuring minimal downtime and quick resolution"),
         ("Live Event &amp; Shoot Support",
          "Hands-on setup, operation, and day-of support while productions "
          "ran \u2014 issues fixed without losing the schedule"),
         ("Documentation &amp; Vendors",
          "Maintained the system documentation and vendor coordination "
          "behind every fix and project \u2014 repeatable, not tribal")])

    exp("FACEBOOK (META), FREMONT, CA", "AV Design Engineer",
        "December 2018 \u2013 December 2021",
        "Designed the audio/video systems used at Facebook \u2014 studio "
        "broadcasts, virtual production, and conference room designs \u2014 "
        "and supported live events when needed.",
        [("System Design &amp; Documentation",
          "Helped standardize broadcast-quality room and studio designs and "
          "created the design documentation builds followed \u2014 "
          "schematics, scope definitions, and specs integration teams built "
          "to"),
         ("Requirements Through Commissioning",
          "Defined each project\u2019s scope with users and vendors \u2014 "
          "systems designed for their use cases, validated through delivery"),
         ("Live Event Support",
          "Supported live events to broadcast-quality standards \u2014 "
          "hands-on during delivery")])

    exp("THE AEROSPACE CORPORATION, EL SEGUNDO, CA", "AV-Network Manager",
        "July 2017 \u2013 November 2018",
        "Owned the build-out of the company\u2019s audio/video systems \u2014 "
        "design, installation, configuration, and integration of meeting "
        "rooms, auditoriums, video conferencing, digital signage, and live "
        "event productions.",
        [("Integration Ownership",
          "Owned budgeting, purchase coordination, and vendor relationships "
          "for AV build-outs \u2014 rooms designed, configured, and "
          "commissioned on schedule"),
         ("Conferencing &amp; Streaming",
          "Architected video conferencing infrastructure (Cisco VCS, MCU, "
          "TMS) and streaming media services \u2014 enterprise meeting and "
          "broadcast delivery"),
         ("Emerging Technology",
          "Researched new AV technologies against real company needs \u2014 "
          "the adopt/defer calls behind the infrastructure roadmap")])

    exp("THE AEROSPACE CORPORATION, EL SEGUNDO, CA", "EIS Supervisor",
        "August 2015 \u2013 July 2017",
        "Supervised the US Media Services team across three major locations "
        "\u2014 California, Colorado, and Virginia \u2014 with multiple field "
        "offices, supporting live company events, users, and new AV spaces.",
        [("Team Leadership Under Pressure",
          "Supervised a distributed technical team through competing "
          "priorities across sites \u2014 live company events, user support, "
          "and consistent service standards"),
         ("Rooms, Signage &amp; Specialized Spaces",
          "Built out video conferencing, boardrooms, digital signage, video "
          "walls, auditoriums, and multipurpose rooms \u2014 capital and "
          "overhead budgets planned with external vendors"),
         ("Live Company Events",
          "Led technical support for live company events \u2014 setup, "
          "operation, and delivery, with user support across all sites")])

    exp("GOOGLE (VIA ADVANTAGE TECHNICAL RESOURCING), MOUNTAIN VIEW / SAN FRANCISCO, CA",
        "AV Deployment Program Manager", "January 2014 \u2013 January 2015",
        "Program-managed deployments of video conferencing and AV systems "
        "across Google campuses \u2014 rooms delivered to "
        "first-day-of-business readiness.",
        [("Cross-Functional Coordination",
          "Worked with architects, engineers, integrators, vendors, and "
          "employees to assess needs and plan AV installations \u2014 "
          "delivered on time, to spec"),
         ("Specialized Event &amp; Space Needs",
          "Turned specialized AV requests \u2014 UX labs, larger meeting "
          "spaces, sound systems \u2014 into delivered, working rooms")])

    exp("PDI / DREAMWORKS ANIMATION, REDWOOD CITY, CA", "AV Supervisor",
        "January 2000 \u2013 January 2014",
        "Managed a team of technicians and engineers for AV design, "
        "integration, maintenance, and support for film productions \u2014 the "
        "systems behind 20+ major motion pictures \u2014 across multiple "
        "200,000+ sq ft facilities, technical lead for company broadcasts "
        "and industry-expert events.",
        [("Live Event Technical Lead",
          "Technical lead for company broadcasts and special events \u2014 "
          "equipment setup, show execution, load-out \u2014 and complex "
          "client requests adapted into working production systems "
          "(streaming, remote recording/playback, color grading, review "
          "rooms, editing suites)"),
         ("Maintenance &amp; Inventory Discipline",
          "Owned maintenance and support of production AV \u2014 maintenance "
          "schedules, reliable operation practices, and recurring issues "
          "turned into standards"),
         ("Installation from Drawings",
          "Managed AV room installations across 200,000+ sq ft facilities "
          "from cold shell through final commissioning \u2014 working from "
          "architectural drawings \u2014 "
          "cabling, mounts, and systems with architects, contractors, and "
          "vendors")])

    E.append(Paragraph("EARLIER EXPERIENCE", S["section"]))
    E.append(Paragraph(
        "Editorial Engineer, Pixar Animation Studios &nbsp;\u2022&nbsp; "
        "Engineering Support Specialist, Warner Bros. &nbsp;\u2022&nbsp; "
        "Audio Technician, Larrabee Sound Studios", S["earlier"]))

    E.append(Paragraph("AI &amp; TECHNOLOGY SKILLS", S["section"]))
    for line in [
        "AI fluency: minor scripting and workflow automation at work \u2014 "
        "automating repeatable tasks \u2014 and generative AI and agentic "
        "tools in AV and home projects, including agent-orchestrated "
        "workflows, prompt/context engineering, and editing/refining "
        "AI-assisted output to a finished standard",
        "Q-SYS ecosystem (some experience): system design, DSP "
        "configuration, and emulation in Q-SYS Designer \u2014 including "
        "control scripts in Lua within Q-Sys",
        "DSP concepts: acoustic echo cancellation, noise reduction, EQ, "
        "dynamics/compression, automixing, crossovers",
        "Networked AV &amp; IP video: ST 2110 certified (SMPTE); Dante (past "
        "experience); IP video systems in live production environments",
        "AV infrastructure (past experience): displays, mounts, cabling, HDMI/"
        "USB signal flow \u2014 plus video conferencing, digital signage, and "
        "background music systems designed and delivered (past experience)",
        "Streaming &amp; production tools (past experience): Wirecast, OBS, "
        "DaVinci Resolve, AWS streaming services",
        "Live production systems (past experience): Dante, DMX, Sony cameras, "
        "ETC lighting",
        "Control &amp; automation (past experience): Stream Deck / BitFocus "
        "Companion (hands-on use, not an expert)",
    ]:
        E.append(Paragraph(line, S["plain"], bulletText="\u2022"))

    E.append(Paragraph("EDUCATION &amp; CERTIFICATIONS", S["section"]))
    for line in [
        "California State University, East Bay \u2014 BA in Music, MA in Music",
        "Full Sail University \u2014 Specialized Recording Arts Degree",
        "Chabot College \u2014 Associates in Electronics",
        "SMPTE Member \u2014 Certifications: ST 2110, Media in the Cloud, IP "
        "Media Transmission for Broadcasters, High Dynamic Range Imaging "
        "System Fundamentals",
        "AVIXA \u2014 Multiple past CTS certifications and classes (not "
        "current)",
        "Avid/Pro Tools Certifications &nbsp;\u2022&nbsp; ISF Certified \u2014 "
        "Image Science Foundation (Color Calibration)",
    ]:
        E.append(Paragraph(line, S["plain"], bulletText="\u2022"))

    E.append(Paragraph("NOTABLE ACHIEVEMENTS", S["section"]))
    for line in [
        "Helped create 20+ major motion pictures \u2014 Shrek 1\u20134, Kung Fu "
        "Panda, How to Train Your Dragon, Madagascar, Toy Story 2, The Croods",
        "Music production credits include Michael Jackson\u2019s History album "
        "(MJJ Productions)",
        "HALO/HVEN Telepresence \u2014 engineering team member (HP/DreamWorks "
        "joint venture) that developed early telepresence systems for Fortune "
        "500 companies, generating revenue and patents for DreamWorks",
        "Co-author, \u201CImplementation of Intranet Scene Preview for Feature "
        "Animation\u201D \u2014 140th SMPTE Digital TV Conference; published "
        "articles in Electronic Musician and A/V Multimedia Producer",
        "U.S. Government Secret clearance (held during earlier defense-industry "
        "work)",
    ]:
        E.append(Paragraph(line, S["plain"], bulletText="\u2022"))

    doc.build(E)


def build_cover(path):
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.85*inch, rightMargin=0.85*inch,
                            topMargin=0.85*inch, bottomMargin=0.8*inch,
                            title="Gene Takahashi - Cover Letter",
                            author="Gene Takahashi")
    name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=15,
                          leading=18, textColor=INK)
    contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=9.5,
                             leading=12, textColor=GRAY)
    meta = ParagraphStyle("meta", fontName="Helvetica", fontSize=10.5,
                          leading=14, textColor=INK)
    body = ParagraphStyle("body", fontName="Helvetica", fontSize=10.3,
                          leading=13.8, textColor=INK, alignment=TA_JUSTIFY,
                          spaceBefore=8)
    E = [Paragraph("GENE TAKAHASHI", name), Spacer(1, 2),
         Paragraph(f"South Lake Tahoe, CA &nbsp;|&nbsp; (650) 960-5594 &nbsp;|&nbsp; "
                   f"mail@gene-site.com &nbsp;|&nbsp; {LINK}", contact),
         HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceBefore=8),
         Spacer(1, 12),
         Paragraph("xAI", meta),
         Paragraph("Re: Sr. AV Administrator / Engineer", meta),
         Paragraph("Dear xAI Team,", body),
         Paragraph(
             "My career has been hands-on AV ownership at enterprise scale: "
             "engineer for Amazon Studios\u2019 Virtual Production stage "
             "\u2014 primary escalation for its most complex AV issues, "
             "keeping displays, cameras, switchers, intercoms, IP video, and "
             "machine rooms show-ready through film, video, and live "
             "broadcast shoots; supervisor of the media services team across "
             "California, Colorado, and Virginia (plus field offices) at The "
             "Aerospace Corporation \u2014 live company events, user "
             "support, and consistent standards under real pressure; AV "
             "design at Facebook for broadcast-quality studios; "
             "program-managed conferencing deployments across Google "
             "campuses; and AV design, integration, and maintenance at "
             "DreamWorks across multiple 200,000+ sq ft facilities \u2014 "
             "the systems behind 20+ major motion pictures, technical lead "
             "for company broadcasts and industry-expert events.", body),
         Paragraph(
             "The technical core your posting names is what I work with: "
             "audio/video signal flow, cabling, mounts, lighting, and "
             "projection \u2014 I hold a Hughes/JVC Hi-Res projector "
             "certificate and have used ETC lighting, Sony cameras, and DMX "
             "in production work (past experience); DSP concepts (acoustic "
             "echo cancellation, noise reduction, EQ, automixing) and some "
             "experience with the Q-SYS ecosystem and control scripts in Lua "
             "within Q-Sys; Dante; ST 2110 certified (SMPTE) with IP video "
             "in live production. I have designed and delivered video "
             "conferencing, digital signage, and streaming media services "
             "\u2014 plus the documentation discipline: maintenance "
             "schedules, troubleshooting guides, inventory, and system "
             "diagrams. Multiple past CTS certifications (not current).", body),
         Paragraph(
             "And I automate: scripting and workflow automation from my day "
             "job plus agent-driven AI workflows I have built that design, "
             "check, and emulate AV systems headlessly \u2014 days of "
             "engineering time turned into minutes. For a company built on "
             "engineering excellence and flat ownership, that habit \u2014 "
             "fix it once, document it, automate it \u2014 is exactly how I "
             "keep complex AV environments reliable.", body),
         Paragraph("Best regards,<br/><br/>Gene Takahashi", body)]
    doc.build(E)


if __name__ == "__main__":
    import fitz
    import re
    rez = f"{OUT}/Gene_Takahashi_Resume_xAI_AV.pdf"
    for scale in (1.0, 0.96, 0.92, 0.88):
        build_resume(rez, scale)
        n = len(fitz.open(rez))
        print(f"resume scale {scale}: {n} pages")
        if n <= 2:
            break
    cov = f"{OUT}/Gene_Takahashi_Cover_Letter_xAI_AV.pdf"
    build_cover(cov)
    fails = []
    d = fitz.open(rez)
    norm = re.sub(r"\s+", " ", " ".join(p.get_text() for p in d))
    if len(d) > 2:
        fails.append(f"resume pages {len(d)}")
    for probe in ["South Lake Tahoe, CA", "(650) 960-5594", "mail@gene-site.com",
                  "linkedin.com/in/gene-takahashi-36b8b9/",
                  "February 2022 \u2013 February 2026",
                  "20+ major motion pictures", "Michael Jackson",
                  "cold shell", "capital and overhead",
                  "live company events", "company broadcasts",
                  "video conferencing", "digital signage", "auditoriums",
                  "Supervised", "team of technicians",
                  "ST 2110", "Dante", "IP video",
                  "automating repeatable tasks", "workflow automation",
                  "generative AI and agentic tools", "minor scripting",
                  "agent-orchestrated", "prompt/context", "editing/refining",
                  "Wirecast", "OBS", "DaVinci Resolve", "AWS streaming",
                  "DMX", "Sony cameras", "ETC lighting",
                  "BitFocus Companion", "not an expert",
                  "AVIXA", "past CTS certifications", "(not current)",
                  "BA in Music", "Full Sail", "EARLIER EXPERIENCE",
                  "Pixar", "Warner Bros", "Larrabee", "GOOGLE (VIA ADVANTAGE",
                  "PDI / DREAMWORKS", "Secret clearance",
                  "Escalation Point", "some Q-SYS equipment",
                  "maintenance schedules", "Lua within Q-Sys", "crossovers",
                  "signal flow", "design documentation",
                  "streaming media services", "load-out"]:
        if probe not in norm:
            fails.append(f"RESUME MISSING: {probe}")
    for bad in ["vMix", "TriCaster", "ATEM", "Premiere", "After Effects",
                "Zoom", "Webex", "Crestron", "Extron", "AMX", "Biamp",
                "Teams", "IATSE", "union", "ROI",
                "ON24", "Vimeo", "projection mapping", "LED wall",
                "acoustical design", "$3M", "$2M", "CEO Award",
                "years of experience", "6+ years", "Present", "expert in",
                "CTS-D", "satellite", "HDR", "VLAN", "PoE", "DHCP", "MDM",
                "Shure", "RF"]:
        if bad == "Teams":
            if re.search(rf"\b{re.escape(bad)}\b", norm):
                fails.append(f"RESUME FORBIDDEN: {bad}")
        elif re.search(rf"\b{re.escape(bad)}\b", norm, re.IGNORECASE):
            fails.append(f"RESUME FORBIDDEN: {bad}")
    for pno, p in enumerate(d):
        for b in p.get_text("blocks"):
            if b[0] < 40 or b[2] > 612-40 or b[1] < 30 or b[3] > 792-30:
                fails.append(f"resume p{pno+1} block outside margins")
                break
    dc = fitz.open(cov)
    normc = re.sub(r"\s+", " ", " ".join(p.get_text() for p in dc))
    if len(dc) > 1:
        fails.append(f"cover pages {len(dc)}")
    for probe in ["Re: Sr. AV Administrator / Engineer", "xAI",
                  "South Lake Tahoe, CA",
                  "linkedin.com/in/gene-takahashi-36b8b9/",
                  "California, Colorado, and Virginia", "ST 2110",
                  "past CTS certifications", "escalation",
                  "agent-driven AI workflows", "Lua within Q-Sys",
                  "some experience", "Hughes/JVC", "ETC lighting", "DSP"]:
        if probe not in normc:
            fails.append(f"COVER MISSING: {probe}")
    for bad in ["Zoom", "Webex", "Crestron", "Extron", "AMX", "Biamp",
                "Teams", "IATSE", "union", "ROI", "ON24", "$",
                "years of experience", "Present", "satellite", "HDR",
                "VLAN", "PoE", "DHCP", "MDM", "Shure", "RF"]:

        if bad == "Teams":
            if re.search(rf"\b{re.escape(bad)}\b", normc): fails.append("COVER FORBIDDEN: "+bad)
        elif re.search(rf"\b{re.escape(bad)}\b", normc, re.IGNORECASE):
            fails.append(f"COVER FORBIDDEN: {bad}")
    print("QC:", "PASS" if not fails else "FAIL")
    for f in fails:
        print("  -", f)
    print(f"RESUME: {rez} ({os.path.getsize(rez)}B)")
    print(f"COVER: {cov} ({os.path.getsize(cov)}B)")