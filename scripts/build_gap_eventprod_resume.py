#!/usr/bin/env python3
"""Build Gene's Manager, Multimedia Event Production (Gap Inc. JD) resume + cover letter.
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

OUT = "/home/mail2/.openclaw/workspace/resume_gap_eventprod"
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
         Paragraph("Multimedia Event Production Manager | Live &amp; Broadcast "
                   "Production Leadership", S["headline"]),
         Spacer(1, 2),
         Paragraph(f"South Lake Tahoe, CA &nbsp;|&nbsp; (650) 960-5594 &nbsp;|&nbsp; "
                   f"mail@gene-site.com &nbsp;|&nbsp; {LINK}", S["contact"]),
         HRFlowable(width="100%", thickness=1.4, color=ACCENT, spaceBefore=6)]

    E.append(Paragraph("PROFESSIONAL SUMMARY", S["section"]))
    E.append(Paragraph(
        "Multimedia production and AV leader with a career spanning studio "
        "broadcasts, live corporate events, and enterprise event technology "
        "\u2014 has supervised technical teams across three states and multiple "
        "field offices, owned budgets with capital and overhead planning, "
        "standardized broadcast-quality studio and live event designs "
        "enterprise-wide, and provided hands-on production support while "
        "productions run live. Managed the AV systems behind 20+ major motion "
        "pictures across DreamWorks and Pixar facilities, and kept Amazon "
        "Studios\u2019 Virtual Production stage ready for film, video, and live "
        "broadcast shoots. Hands-on with IP video and networked AV (ST 2110, "
        "Dante), with scripting and workflow automation at work and generative "
        "AI and agentic tools in AV and home projects.",
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
        "live broadcast shoots \u2014 design and maintenance of the production "
        "systems on the stage and its machine rooms, with direct support "
        "through live delivery.",
        [("Multi-Camera Live Production Ops",
          "Kept the stage\u2019s full production chain \u2014 cameras, lighting, "
          "switchers, intercoms, IP video, and the machine rooms behind them "
          "\u2014 designed, maintained, and show-ready for film, video, and "
          "live broadcast productions"),
         ("Live Show Support",
          "Provided direct production support during shoots and live events "
          "\u2014 hands-on troubleshooting while productions ran"),
         ("Vendor &amp; Third-Party Coordination",
          "Interfaced with third parties and vendors across stage projects "
          "\u2014 requirements, schedules, and delivery through completion")])

    exp("FACEBOOK (META), FREMONT, CA", "AV Design Engineer",
        "December 2018 \u2013 December 2021",
        "Designed the audio/video systems used at Facebook \u2014 studio "
        "broadcasts, a virtual production stage, and cloud-based video "
        "production, plus live event and conference room designs when needed.",
        [("Broadcast-Quality Standards",
          "Helped standardize designs for broadcast-quality live event and "
          "studio spaces \u2014 the technical standards enterprise-wide "
          "buildouts followed"),
         ("Standards &amp; SOP Documentation",
          "Created the design documentation those builds followed \u2014 "
          "turning each project\u2019s scope and functions into buildable, "
          "repeatable specifications with users and vendors"),
         ("Partner-Aligned Delivery",
          "Worked with users and vendors to define project scope and "
          "functions \u2014 translating production needs into systems that "
          "delivered broadcast-quality results")])

    exp("THE AEROSPACE CORPORATION, EL SEGUNDO, CA", "AV-Network Manager",
        "July 2017 \u2013 November 2018",
        "Owned the build-out of the company's audio/video systems \u2014 "
        "budgeting, design, and installation of meeting rooms, auditoriums, "
        "video conferencing, digital signage, and live event productions.",
        [("Budget &amp; Vendor Ownership",
          "Owned budgeting for AV build-outs \u2014 planned with vendors and "
          "delivered capital and overhead projects on schedule"),
         ("Live Event Production",
          "Owned technical production for live corporate events \u2014 from "
          "system design and installation through event delivery"),
         ("Technology Evaluation",
          "Researched and vetted new AV technologies against real company "
          "needs \u2014 building the case for what the enterprise should "
          "adopt next")])

    exp("THE AEROSPACE CORPORATION, EL SEGUNDO, CA", "EIS Supervisor",
        "August 2015 \u2013 July 2017",
        "Supervised the US Media Services team across three major locations "
        "\u2014 California, Colorado, and Virginia \u2014 with multiple field "
        "offices, supporting live company events, users, and new AV spaces.",
        [("Multi-Site Team Leadership",
          "Supervised a distributed technical team across three states and "
          "multiple field offices \u2014 schedules, standards, and consistent "
          "delivery at every site"),
         ("Planning &amp; Budgeting",
          "Planned and budgeted capital and overhead with external vendors "
          "\u2014 from new AV spaces through enterprise-wide AV programs"),
         ("Live Company Events",
          "Led technical support for live company events \u2014 setup through "
          "delivery, with user support across all sites")])

    exp("GOOGLE (VIA ADVANTAGE TECHNICAL RESOURCING), MOUNTAIN VIEW / SAN FRANCISCO, CA",
        "AV Deployment Program Manager", "January 2014 \u2013 January 2015",
        "Program-managed deployments of video conferencing and AV systems "
        "across Google campuses \u2014 coordinated architects, engineers, "
        "integrators, and vendors through multi-campus installations.",
        [("Cross-Functional Coordination",
          "Coordinated project teams across engineering, facilities, IT, and "
          "external integrators \u2014 installations delivered on time, to "
          "spec, across campuses"),
         ("Specialized Event &amp; Space Requirements",
          "Partnered with internal clients on specialized AV needs \u2014 "
          "larger meeting spaces, sound systems \u2014 turning requests into "
          "delivered spaces")])

    exp("PDI / DREAMWORKS ANIMATION, REDWOOD CITY, CA", "AV Supervisor",
        "January 2000 \u2013 January 2014",
        "Managed a team of technicians and engineers for AV design, "
        "integration, maintenance, and support for film productions \u2014 the "
        "systems behind 20+ major motion pictures \u2014 with AV room "
        "installations across multiple 200,000+ sq ft facilities, and "
        "technical lead for company broadcasts and events.",
        [("Live Broadcasts &amp; Events",
          "Technical lead for special events by industry experts \u2014 "
          "company broadcasts and events, owning the technical plan and its "
          "execution end to end"),
         ("Build-Outs with Vendor Coordination",
          "Managed AV room installations across multiple 200,000+ sq ft "
          "facilities from cold shell to completion \u2014 architects, "
          "engineers, vendors, and construction trades coordinated to delivery"),
         ("Standards for Production Spaces",
          "Designed and managed AV for production, post production, and "
          "business usage \u2014 streaming, remote recording/playback, color "
          "grading, review rooms, and editing suites built to working "
          "standards")])

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
        "Networked AV &amp; IP video: ST 2110 certified (SMPTE); Dante (past "
        "experience); IP video systems in live production environments",
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
         Paragraph("Gap Inc. (Old Navy, Gap, Banana Republic, Athleta)", meta),
         Paragraph("Re: Manager, Multimedia Event Production", meta),
         Paragraph("Dear Multimedia Production Leadership,", body),
         Paragraph(
             "My career has been multimedia and event production from the "
             "technical side \u2014 supervising a media services team across "
             "California, Colorado, and Virginia and multiple field offices, "
             "owning budgeting, design, and installation of the AV systems "
             "behind corporate meeting rooms, auditoriums, video conferencing, "
             "and digital signage, standardizing broadcast-quality studio and "
             "live event designs enterprise-wide at Facebook, and technical "
             "lead for company broadcasts and industry-expert events at "
             "DreamWorks across multiple 200,000+ sq ft production facilities "
             "\u2014 projects run from cold shell to completion with "
             "architects, engineers, vendors, and construction trades. Most "
             "recently I kept Amazon Studios\u2019 Virtual Production stage "
             "\u2014 cameras, lighting, switchers, intercoms, IP video \u2014 "
             "designed, maintained, and show-ready for film, video, and live "
             "broadcast shoots, supporting productions directly while they ran.",
             body),
         Paragraph(
             "The leadership and operations parts of this role are where I "
             "have consistently delivered: consistent technical standards "
             "across multi-site operations, capital and overhead budget "
             "planning with external vendors, design documentation teams "
             "build to, and hands-on support when productions need it \u2014 "
             "including troubleshooting while shows run live. I hold an ST "
             "2110 certification and have worked with IP video and networked "
             "AV in production environments; I also carry multiple past CTS "
             "certifications (not current), and keep a current AI practice "
             "\u2014 scripting, workflow automation, and agentic AI tools "
             "\u2014 that streamlines repeatable production and engineering "
             "work.", body),
         Paragraph(
             "Your posting\u2019s emphasis on production excellence, "
             "standardization across locations, and a high-performing team "
             "environment describes the work I have done and led for most of "
             "my career. I would bring it to Gap Inc.\u2019s multimedia "
             "production team with both the technical depth and the "
             "leadership habits already built.", body),
         Paragraph("Best regards,<br/><br/>Gene Takahashi", body)]
    doc.build(E)


if __name__ == "__main__":
    import fitz
    import re
    rez = f"{OUT}/Gene_Takahashi_Resume_Gap_EventProduction.pdf"
    for scale in (1.0, 0.96, 0.92, 0.88):
        build_resume(rez, scale)
        n = len(fitz.open(rez))
        print(f"resume scale {scale}: {n} pages")
        if n <= 2:
            break
    cov = f"{OUT}/Gene_Takahashi_Cover_Letter_Gap_EventProduction.pdf"
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
                  "broadcast-quality", "design documentation",
                  "Researched", "and vetted new AV technologies",
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
                  "PDI / DREAMWORKS", "Secret clearance"]:
        if probe not in norm:
            fails.append(f"RESUME MISSING: {probe}")
    for bad in ["vMix", "TriCaster", "ATEM", "Premiere", "After Effects",
                "Zoom", "Teams", "Google Meet", "IATSE", "union", "ROI",
                "ON24", "YouTube", "Vimeo", "projection mapping", "LED wall",
                "satellite", "$3M", "$2M", "CEO Award", "years of experience",
                "6+ years", "Present", "expert in", "Q-SYS"]:
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
    for probe in ["Re: Manager, Multimedia Event Production", "Gap Inc.",
                  "South Lake Tahoe, CA",
                  "linkedin.com/in/gene-takahashi-36b8b9/",
                  "California, Colorado, and Virginia", "cold shell", "ST 2110",
                  "past CTS certifications", "Virtual Production stage"]:
        if probe not in normc:
            fails.append(f"COVER MISSING: {probe}")
    for bad in ["vMix", "TriCaster", "ATEM", "Premiere", "After Effects",
                "Zoom", "Teams", "IATSE", "union", "ROI", "ON24", "YouTube",
                "Vimeo", "$", "years of experience", "Present"]:
        if bad == "Teams":
            if re.search(rf"\b{re.escape(bad)}\b", normc): fails.append("COVER FORBIDDEN: "+bad)
        elif re.search(rf"\b{re.escape(bad)}\b", normc, re.IGNORECASE):
            fails.append(f"COVER FORBIDDEN: {bad}")
    print("QC:", "PASS" if not fails else "FAIL")
    for f in fails:
        print("  -", f)
    print(f"RESUME: {rez} ({os.path.getsize(rez)}B)")
    print(f"COVER: {cov} ({os.path.getsize(cov)}B)")