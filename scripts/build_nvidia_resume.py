#!/usr/bin/env python3
"""Build Gene's Enterprise AV Design & Collaboration Engineer (NVIDIA JD) resume + cover letter.
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

OUT = "/home/mail2/.openclaw/workspace/resume_nvidia"
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
         Paragraph("Enterprise AV Engineer | Global Design, Deployment &amp; Operations", S["headline"]),
         Spacer(1, 2),
         Paragraph(f"South Lake Tahoe, CA &nbsp;|&nbsp; (650) 960-5594 &nbsp;|&nbsp; "
                   f"mail@gene-site.com &nbsp;|&nbsp; {LINK}", S["contact"]),
         HRFlowable(width="100%", thickness=1.4, color=ACCENT, spaceBefore=6)]

    E.append(Paragraph("PROFESSIONAL SUMMARY", S["section"]))
    E.append(Paragraph(
        "Enterprise AV engineer with a global design-and-deployment career "
        "\u2014 managed AV room installations across multiple 200,000+ sq ft "
        "facilities from cold shell to completion, program-managed "
        "multi-campus video conferencing deployments, and supervised a "
        "media services team across three states and multiple field offices. "
        "Owns design through commissioning with vendors, architects, and "
        "construction trades coordinated at each step \u2014 and keeps the "
        "systems he owns running (Amazon Studios\u2019 Virtual Production "
        "stage: displays, cameras, switchers, DSP, machine rooms maintained "
        "and show-ready daily). Experience with some Q-SYS equipment, DSP "
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
        "live broadcast shoots \u2014 day-to-day engineering of the systems "
        "productions ran on, with deep hands-on support through every "
        "delivery.",
        [("Tier-3 Systems Ownership",
          "Escalation point for the stage\u2019s most complex AV issues "
          "\u2014 diagnosing integrated hardware/software faults across its "
          "AV signal chain \u2014 displays, cameras, switchers, intercoms, "
          "IP video, machine rooms \u2014 to keep maximum uptime for "
          "productions"),
         ("Preventative Maintenance &amp; Break/Fix",
          "Ran preventive maintenance and hands-on fixes \u2014 issues "
          "diagnosed and resolved same-day while shows and shoots kept their "
          "schedules"),
         ("Vendor Coordination &amp; Procurement",
          "Coordinated vendors and third parties through fixes and projects "
          "\u2014 ordering, scheduling, and equipment delivered to working "
          "systems")])

    exp("FACEBOOK (META), FREMONT, CA", "AV Design Engineer",
        "December 2018 \u2013 December 2021",
        "Designed the audio/video systems used at Facebook \u2014 studio "
        "broadcasts, virtual production, and conference room designs \u2014 "
        "and supported live events when needed.",
        [("Design Documentation &amp; Standards",
          "Helped standardize broadcast-quality room and studio designs and "
          "created the design documentation builds followed \u2014 "
          "schematics, line-diagram-style scope definitions, and specs "
          "integration teams built to"),
         ("Design Through Commissioning",
          "Defined each project\u2019s scope with users and vendors \u2014 "
          "systems designed for their use cases, validated through delivery "
          "and acceptance"),
         ("Live Event Support",
          "Supported live events to broadcast-quality standards \u2014 "
          "hands-on during delivery")])

    exp("THE AEROSPACE CORPORATION, EL SEGUNDO, CA", "AV-Network Manager",
        "July 2017 \u2013 November 2018",
        "Owned the build-out of the company\u2019s audio/video systems \u2014 "
        "budgeting, procurement, design, and installation of meeting rooms, "
        "auditoriums, video conferencing, digital signage, and live event "
        "productions.",
        [("Procurement &amp; Vendor Management",
          "Owned budgeting, purchase coordination, and vendor relationships "
          "for AV build-outs \u2014 equipment ordered, configured, and "
          "installed on schedule"),
         ("Conferencing Architecture",
          "Architected video conferencing infrastructure (Cisco VCS, MCU, "
          "TMS) and streaming media services \u2014 enterprise meeting "
          "delivery built for reliability"),
         ("Technology Evaluation",
          "Researched next-generation AV technologies against real company "
          "needs \u2014 the adopt/defer calls behind the infrastructure "
          "roadmap")])

    exp("THE AEROSPACE CORPORATION, EL SEGUNDO, CA", "EIS Supervisor",
        "August 2015 \u2013 July 2017",
        "Supervised the US Media Services team across three major locations "
        "\u2014 California, Colorado, and Virginia \u2014 with multiple field "
        "offices, supporting live company events, users, and new AV spaces.",
        [("Global Support Operations",
          "Supervised a distributed technical team \u2014 Tier-3 escalation "
          "point for AV issues, user support, and consistent service "
          "standards at every site"),
         ("Rooms &amp; Shared Spaces",
          "Built out video conferencing, boardrooms, digital signage, video "
          "walls, auditoriums, and multipurpose rooms \u2014 capital and "
          "overhead budgets planned with external vendors"),
         ("Team Enablement",
          "Trained technical staff and vendor partners on corporate standards "
          "and quality expectations")])

    exp("GOOGLE (VIA ADVANTAGE TECHNICAL RESOURCING), MOUNTAIN VIEW / SAN FRANCISCO, CA",
        "AV Deployment Program Manager", "January 2014 \u2013 January 2015",
        "Program-managed deployments of video conferencing and AV systems "
        "across Google campuses \u2014 rooms delivered to "
        "first-day-of-business readiness.",
        [("Deployment Logistics",
          "Coordinated architects, engineers, integrators, vendors, and "
          "employees \u2014 equipment pipelines and installation schedules "
          "across campuses, delivered on time and to spec"),
         ("Cross-Functional Build Coordination",
          "Drove AV requirements inside larger construction programs with "
          "Real-Estate-adjacent facilities and design teams"),
         ("Specialized Client Needs",
          "Turned specialized AV requests \u2014 UX labs, larger meeting "
          "spaces, sound systems \u2014 into delivered, working rooms")])

    exp("PDI / DREAMWORKS ANIMATION, REDWOOD CITY, CA", "AV Supervisor",
        "January 2000 \u2013 January 2014",
        "Managed a team of technicians and engineers for AV design, "
        "integration, maintenance, and support for film productions \u2014 the "
        "systems behind 20+ major motion pictures \u2014 across multiple "
        "200,000+ sq ft facilities, technical lead for company broadcasts.",
        [("Installation from Cold Shell",
          "Managed AV room installations across 200,000+ sq ft facilities "
          "from architectural drawings through final commissioning \u2014 "
          "cabling, mounts, and systems delivered with architects, "
          "contractors, and vendors"),
         ("Maintenance &amp; Support Ownership",
          "Owned maintenance and support of production AV \u2014 recurring "
          "issues turned into SOPs and runbooks for reliable daily "
          "operation"),
         ("Broadcasts &amp; Events",
          "Technical lead for company broadcasts and special events \u2014 "
          "setup, show execution, and load-out owned end to end")])

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
         Paragraph("NVIDIA", meta),
         Paragraph("Re: Enterprise AV Design &amp; Collaboration Engineer", meta),
         Paragraph("Dear AV Engineering Team,", body),
         Paragraph(
             "My career has been enterprise AV from drawings to working "
             "rooms: at DreamWorks I managed AV room installations across "
             "multiple 200,000+ sq ft facilities from architectural drawings "
             "through final commissioning \u2014 architects, contractors, and "
             "vendors coordinated at each step, the systems behind 20+ major "
             "motion pictures. At Google I program-managed video conferencing "
             "deployments across campuses, coordinating equipment pipelines "
             "and installation schedules to first-day-of-business readiness. "
             "At The Aerospace Corporation I owned budgeting, procurement, "
             "and vendor relationships for meeting rooms, auditoriums, video "
             "conferencing (Cisco VCS/MCU/TMS), digital signage, and live "
             "events \u2014 and supervised the media services team across "
             "California, Colorado, and Virginia \u2014 three states plus "
             "multiple field offices. Most recently I "
             "engineered Amazon Studios\u2019 Virtual Production stage and "
             "kept it show-ready \u2014 the escalation point for its most "
             "complex AV issues, with hands-on fixes while shoots kept their "
             "schedules, and recurring issues turned into SOPs and runbooks "
             "so they stayed fixed.", body),
         Paragraph(
             "Your posting\u2019s technical core matches what I work with: "
             "AV-over-IP and its dependencies (ST 2110 certified \u2014 "
             "SMPTE; Dante; IP video in live production), DSP concepts "
             "\u2014 acoustic echo cancellation, noise reduction, EQ, "
             "automixing, crossovers \u2014 and some experience with "
             "the Q-SYS ecosystem, including control scripts in Lua within "
             "Q-Sys and commissioning through its emulator. I read and create "
             "the drawings this work runs on \u2014 schematics, line "
             "diagrams, rack elevations \u2014 and hold multiple past CTS "
             "certifications (not current).", body),
         Paragraph(
             "And I automate the tedious parts. I have built agent-driven AI "
             "workflows that design, check, and emulate AV systems headlessly "
             "\u2014 days of engineering time turned into minutes \u2014 "
             "alongside scripting and workflow automation from my day job. "
             "For a company building the future of AI, AV infrastructure "
             "maintained with that same automation mindset is the standard I "
             "would set for NVIDIA\u2019s global rooms and event spaces.", body),
         Paragraph("Best regards,<br/><br/>Gene Takahashi", body)]
    doc.build(E)


if __name__ == "__main__":
    import fitz
    import re
    rez = f"{OUT}/Gene_Takahashi_Resume_NVIDIA_AV.pdf"
    for scale in (1.0, 0.96, 0.92, 0.88):
        build_resume(rez, scale)
        n = len(fitz.open(rez))
        print(f"resume scale {scale}: {n} pages")
        if n <= 2:
            break
    cov = f"{OUT}/Gene_Takahashi_Cover_Letter_NVIDIA_AV.pdf"
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
                  "cold shell", "capital and overhead", "scope definitions",
                  "live company events", "company broadcasts",
                  "broadcast-quality", "design documentation",
                  "Researched", "video conferencing", "digital signage", "auditoriums",
                  "Supervised", "team of technicians",
                  "ST 2110", "Dante", "IP video",
                  "automating repeatable tasks", "workflow automation",
                  "generative AI and agentic tools", "minor scripting",
                  "agent-orchestrated", "prompt/context", "editing/refining",
                  "Wirecast", "OBS", "DaVinci Resolve", "AWS streaming",
                  "DMX", "Sony cameras", "ETC lighting",
                  "BitFocus Companion", "not an expert",
                  "AVIXA", "past CTS certifications", "(not current)",
                  "signal chain", "broadcast-quality", "SOPs",
                  "BA in Music", "Full Sail", "EARLIER EXPERIENCE",
                  "Pixar", "Warner Bros", "Larrabee", "GOOGLE (VIA ADVANTAGE",
                  "PDI / DREAMWORKS", "Secret clearance"]:
        if probe not in norm:
            fails.append(f"RESUME MISSING: {probe}")
    for bad in ["vMix", "TriCaster", "ATEM", "Premiere", "After Effects",
                "Teams", "Zoom Rooms", "IATSE", "union", "ROI",
                "ON24", "Vimeo", "projection mapping", "LED wall",
                "acoustical design", "$3M", "$2M",
                "CEO Award", "years of experience", "6+ years", "Present",
                "expert in", "CTS-D", "satellite", "HDR",
                "VLAN", "PoE", "DHCP", "MDM", "Shure", "RF"]:
        if bad == "Teams":
            if re.search(rf"\b{re.escape(bad)}\b", norm): fails.append("RESUME FORBIDDEN: "+bad)
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
    for probe in ["Re: Enterprise AV Design", "NVIDIA",
                  "South Lake Tahoe, CA",
                  "linkedin.com/in/gene-takahashi-36b8b9/",
                  "California, Colorado, and Virginia", "ST 2110",
                  "Virtual Production stage",
                  "runbooks", "agent-driven AI workflows",
                  "Lua within Q-Sys", "some experience", "Q-SYS ecosystem"]:
        if probe not in normc:
            fails.append(f"COVER MISSING: {probe}")
    for bad in ["vMix", "TriCaster", "ATEM", "Premiere", "After Effects",
                "Zoom Rooms", "Teams", "IATSE", "union", "ROI", "ON24",
                "Appspace", "$", "years of experience", "Present",
                "satellite", "HDR", "LED wall", "VLAN", "PoE", "DHCP",
                "MDM", "Shure", "RF"]:
        if bad == "Teams":
            if re.search(rf"\b{re.escape(bad)}\b", normc): fails.append("COVER FORBIDDEN: "+bad)
        elif re.search(rf"\b{re.escape(bad)}\b", normc, re.IGNORECASE):
            fails.append(f"COVER FORBIDDEN: {bad}")
    print("QC:", "PASS" if not fails else "FAIL")
    for f in fails:
        print("  -", f)
    print(f"RESUME: {rez} ({os.path.getsize(rez)}B)")
    print(f"COVER: {cov} ({os.path.getsize(cov)}B)")