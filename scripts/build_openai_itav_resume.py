#!/usr/bin/env python3
"""Build Gene's ITAV Deployment Engineer (OpenAI JD) resume + cover letter.
Source of truth: GTRez.pdf + Gene-supplied facts (AI fluency: minor scripting
at work, generative AI + agentic tools in AV and home projects; streaming tools
past exp: AWS, Wirecast, OBS, DaVinci Resolve, Dante, DMX, Sony cameras, ETC
lighting; Stream Deck/BitFocus past-not-expert). Rules: <=2p resume, <=1p
letter, no age refs, no years-of-experience numbers, Amazon ends Feb 2026 past
tense, South Lake Tahoe + LinkedIn URL, AVIXA multiple past CTS certifications
(not current), education undated, pre-2000 roles as one Earlier Experience
line. OpenAI-JD honesty: NO claims of Q-SYS/Q-LAN/NDI, Logitech/Cisco/Meet/
Zoom/Teams endpoints, VLAN/DHCP/DNS hands-on, punch lists, as-built markups,
or acceptance-criteria processes — GTRez supports build-out delivery
(budgeting/design/installation), multi-campus deployment programs, cold-shell
construction projects, integrator/vendor/architect coordination, design
documentation, IP video (ST 2110 cert), Dante, live troubleshooting, and
scripting/workflow automation + agentic AI. Format: Roku scope+bullets."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                HRFlowable, KeepTogether)

OUT = "/home/mail2/.openclaw/workspace/resume_openai_itav"
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
         Paragraph("ITAV Deployment Engineer | AV Build-Outs, Deployment "
                   "Programs &amp; Systems Delivery", S["headline"]),
         Spacer(1, 2),
         Paragraph(f"South Lake Tahoe, CA &nbsp;|&nbsp; (650) 960-5594 &nbsp;|&nbsp; "
                   f"mail@gene-site.com &nbsp;|&nbsp; {LINK}", S["contact"]),
         HRFlowable(width="100%", thickness=1.4, color=ACCENT, spaceBefore=6)]

    E.append(Paragraph("PROFESSIONAL SUMMARY", S["section"]))
    E.append(Paragraph(
        "AV deployment engineer whose career has been turning approved designs "
        "into installed, working systems \u2014 build-outs from cold shell to "
        "completion across 200,000+ sq ft facilities, multi-campus deployment "
        "programs at Google, corporate room, auditorium, video conferencing, "
        "and digital signage rollouts across a three-state operation, and the "
        "design standards and documentation those builds followed. Has been "
        "both the design engineer defining the standard and the one "
        "delivering to it, coordinating integrators, vendors, architects, and "
        "construction trades through delivery. Hands-on with IP video and "
        "networked AV (ST 2110, Dante), with scripting and workflow automation "
        "at work and generative AI and agentic tools in AV and home projects.",
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
        "Systems engineering for a Virtual Production stage used for film, "
        "video, and live broadcast shoots \u2014 designing, maintaining, and "
        "supporting the AV backbone productions ran on, with direct production "
        "support through live delivery.",
        [("System Design &amp; Delivery",
          "Designed and maintained the stage\u2019s production backbone \u2014 "
          "cameras, lighting, switchers, intercoms, IP video, and the machine "
          "rooms behind them \u2014 kept ready and running for every "
          "production"),
         ("Live Troubleshooting",
          "The technical point of contact while productions were live \u2014 "
          "diagnosing and resolving issues in real time through delivery"),
         ("Vendor &amp; Third-Party Coordination",
          "Interfaced with third parties and vendors across stage projects "
          "\u2014 defining requirements, coordinating schedules, and seeing "
          "deliveries through")])

    exp("FACEBOOK (META), FREMONT, CA", "AV Design Engineer",
        "December 2018 \u2013 December 2021",
        "Designed the audio/video systems used at Facebook \u2014 studio designs "
        "and builds for studio broadcasts, a virtual production stage, and "
        "cloud-based video production, plus live event and conference room "
        "designs as needed.",
        [("Designs &amp; Documentation Deployments Follow",
          "Helped standardize the designs of broadcast-quality live event and "
          "studio spaces and created the design documentation those builds "
          "followed \u2014 the standard deliverers build to"),
         ("Scope &amp; Partner Definition",
          "Worked with users and vendors to define the scope and functions of "
          "each project \u2014 turning business needs into buildable, budgeted "
          "plans"),
         ("Builds Through Operation",
          "Designed studio systems for broadcasts, virtual production, and "
          "cloud-based video production \u2014 production spaces delivered from "
          "concept through operation")])

    exp("THE AEROSPACE CORPORATION, EL SEGUNDO, CA", "AV-Network Manager",
        "July 2017 \u2013 November 2018",
        "Owned the build-out of the audio/video systems supporting company "
        "goals \u2014 budgeting, design, and installation of meeting rooms, "
        "auditoriums, video conferencing, digital signage, and live event "
        "productions.",
        [("Build-Out Ownership",
          "Owned budgeting, design, and installation across event and meeting "
          "spaces \u2014 capital and overhead planning with vendors, executed "
          "on schedule"),
         ("Technology Evaluation",
          "Researched new AV technologies and matched them to the company\u2019s "
          "real needs \u2014 evaluating what was coming before it arrived"),
         ("Live Event Production",
          "Owned technical production for live corporate events \u2014 from "
          "system design and installation through event delivery")])

    exp("THE AEROSPACE CORPORATION, EL SEGUNDO, CA", "EIS Supervisor",
        "August 2015 \u2013 July 2017",
        "Supervised the US Media Services team for Engineering Information "
        "Services across three major locations \u2014 California, Colorado, and "
        "Virginia \u2014 with multiple field offices, supporting live company "
        "events, users, and new AV spaces.",
        [("Multi-Site Rollouts",
          "Supervised a distributed technical team across three states and "
          "multiple field offices \u2014 schedules, standards, and consistent "
          "delivery for live company events at every site"),
         ("Space Build-Outs &amp; Vendors",
          "Built out video conferencing, boardrooms, digital signage, video "
          "walls, auditoriums, and multipurpose rooms; worked with external "
          "vendors to plan capital and overhead budgets"),
         ("Live Company Events",
          "Led technical support for live company events \u2014 setup through "
          "delivery, with user support across all sites")])

    exp("GOOGLE (VIA ADVANTAGE TECHNICAL RESOURCING), MOUNTAIN VIEW / SAN FRANCISCO, CA",
        "AV Deployment Program Manager", "January 2014 \u2013 January 2015",
        "Program-managed deployments of video conferencing and other AV systems "
        "across Google campuses in the Mountain View and San Francisco areas "
        "\u2014 approved designs turned into installed, working systems.",
        [("Deployment Delivery",
          "Worked with architects, engineers, integrators, vendors, and "
          "internal Google teams to deliver AV installations across "
          "multi-campus environments \u2014 coordinated, on-time, to spec"),
         ("Specialized Client Requirements",
          "Partnered with internal Google clients on specialized AV needs "
          "\u2014 UX labs, larger meeting spaces, sound systems \u2014 turning "
          "requests into delivered spaces")])

    exp("PDI / DREAMWORKS ANIMATION, REDWOOD CITY, CA", "AV Supervisor",
        "January 2000 \u2013 January 2014",
        "Managed a team of technicians and engineers for AV design, "
        "integration, maintenance, and support for film productions \u2014 the "
        "systems behind 20+ major motion pictures \u2014 with AV room "
        "installations across multiple 200,000+ sq ft facilities from cold "
        "shell to completion, and technical lead for company broadcasts and "
        "events.",
        [("Cold Shell to Completion",
          "Projects were managed from cold shell to completion \u2014 budgets, "
          "schedules, vendors, architects, engineers, and construction trades "
          "coordinated into finished, working spaces"),
         ("Design, Integration &amp; Support",
          "Managed AV design, integration, maintenance, and support \u2014 the "
          "systems behind 20+ major motion pictures, owned through daily "
          "operation"),
         ("Broadcasts &amp; Events",
          "Technical lead for special events by industry experts \u2014 company "
          "broadcasts and events, owning the technical plan and its "
          "execution")])

    E.append(Paragraph("EARLIER EXPERIENCE", S["section"]))
    E.append(Paragraph(
        "Editorial Engineer, Pixar Animation Studios &nbsp;\u2022&nbsp; "
        "Engineering Support Specialist, Warner Bros. &nbsp;\u2022&nbsp; "
        "Audio Technician, Larrabee Sound Studios", S["earlier"]))

    E.append(Paragraph("AI &amp; TECHNOLOGY SKILLS", S["section"]))
    for line in [
        "AI fluency: minor scripting and workflow automation at work \u2014 "
        "automating repeatable tasks \u2014 and generative AI and agentic tools "
        "in AV and home projects, including agent-orchestrated workflows, "
        "prompt/context engineering, and editing/refining AI-assisted output to "
        "a finished standard",
        "Networked AV &amp; IP video: ST 2110 certified (SMPTE); Dante "
        "(past experience); IP video systems in live production environments",
        "Streaming &amp; production tools (past experience): AWS streaming "
        "services, Wirecast, OBS, DaVinci Resolve",
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
         Paragraph("OpenAI", meta),
         Paragraph("Re: ITAV Deployment Engineer", meta),
         Paragraph("Dear ITAV Team,", body),
         Paragraph(
             "Turning approved designs into installed, working systems \u2014 "
             "and carrying them through to delivery \u2014 has been my entire "
             "career, from both sides of the design. As an AV Design Engineer "
             "at Facebook I defined the designs and wrote the documentation "
             "deployments followed; as AV Deployment Program Manager at Google "
             "I delivered video conferencing and AV installations across "
             "multi-campus environments, coordinated, on-time, to spec; at "
             "The Aerospace Corporation I owned budgeting, design, and "
             "installation of meeting rooms, auditoriums, video conferencing, "
             "and digital signage; and at DreamWorks I managed AV design, "
             "integration, maintenance, and support across multiple 200,000+ "
             "sq ft facilities \u2014 projects run from cold shell to "
             "completion with architects, engineers, vendors, and construction "
             "trades.", body),
         Paragraph(
             "The coordination and troubleshooting sides are equally hands-on: "
             "I supervised a media services team delivering consistent AV "
             "across three states and multiple field offices, and most "
             "recently kept Amazon Studios\u2019 Virtual Production stage "
             "running \u2014 cameras, lighting, switchers, intercoms, IP "
             "video, machine rooms \u2014 diagnosing and resolving issues in "
             "real time while productions were live. I hold an ST 2110 "
             "certification and work with networked AV and IP video in "
             "production environments daily.", body),
         Paragraph(
             "The line in your posting about automating repeatable deployment "
             "work using AI, agentic workflows, and basic scripting describes "
             "how I already work: minor scripting and workflow automation at "
             "work, agent-orchestrated workflows, prompt and context "
             "engineering, and generative AI tools across my AV and home "
             "projects. That combination \u2014 a career of delivering "
             "systems and a current, self-directed AI practice \u2014 is what "
             "I would bring to OpenAI\u2019s ITAV team.", body),
         Paragraph("Best regards,<br/><br/>Gene Takahashi", body)]
    doc.build(E)


if __name__ == "__main__":
    import fitz
    import re
    rez = f"{OUT}/Gene_Takahashi_Resume_OpenAI_ITAVDeployment.pdf"
    for scale in (1.0, 0.96, 0.92, 0.88):
        build_resume(rez, scale)
        n = len(fitz.open(rez))
        print(f"resume scale {scale}: {n} pages")
        if n <= 2:
            break
    cov = f"{OUT}/Gene_Takahashi_Cover_Letter_OpenAI_ITAVDeployment.pdf"
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
                  "cold shell", "capital and overhead", "scope and functions",
                  "live company events", "company broadcasts",
                  "standardize", "design documentation",
                  "Researched new AV technologies",
                  "video conferencing", "digital signage", "video walls",
                  "auditoriums", "Supervised", "team of technicians",
                  "ST 2110", "Dante", "IP video",
                  "automating repeatable tasks", "workflow automation",
                  "generative AI and agentic tools", "minor scripting",
                  "agent-orchestrated", "prompt/context", "editing/refining",
                  "AWS streaming services", "Wirecast", "OBS", "DaVinci Resolve",
                  "DMX", "Sony", "ETC lighting",
                  "BitFocus Companion", "not an expert",
                  "AVIXA", "past CTS certifications", "(not current)",
                  "BA in Music", "Full Sail", "EARLIER EXPERIENCE",
                  "Pixar", "Warner Bros", "Larrabee", "GOOGLE (VIA ADVANTAGE",
                  "PDI / DREAMWORKS", "Secret clearance"]:
        if probe not in norm:
            fails.append(f"RESUME MISSING: {probe}")
    for bad in ["Q-SYS", "QSYS", "Q-LAN", "QLAN", "NDI", "Logitech", "Cisco",
                "Zoom", "Teams", "Google Meet", "VLAN", "DHCP", "DNS",
                "punch list", "as-built", "acceptance criteria",
                "CEO Award", "$", "years of experience", "6+ years",
                "Present", "expert in"]:
        if re.search(rf"\b{re.escape(bad)}\b", norm):
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
    for probe in ["Re: ITAV Deployment Engineer", "OpenAI",
                  "South Lake Tahoe, CA",
                  "linkedin.com/in/gene-takahashi-36b8b9/",
                  "agent-orchestrated", "prompt and context engineering",
                  "cold shell", "ST 2110", "three states"]:
        if probe not in normc:
            fails.append(f"COVER MISSING: {probe}")
    for bad in ["Q-SYS", "QSYS", "Q-LAN", "NDI", "Logitech", "Cisco", "Zoom",
                "Teams", "VLAN", "DHCP", "DNS", "punch list", "as-built",
                "acceptance criteria", "$", "years of experience", "Present"]:
        if re.search(rf"\b{re.escape(bad)}\b", normc):
            fails.append(f"COVER FORBIDDEN: {bad}")
    print("QC:", "PASS" if not fails else "FAIL")
    for f in fails:
        print("  -", f)
    print(f"RESUME: {rez} ({os.path.getsize(rez)}B)")
    print(f"COVER: {cov} ({os.path.getsize(cov)}B)")