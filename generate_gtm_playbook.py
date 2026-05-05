#!/usr/bin/env python3
"""
Viral Ideas Marketing — GTM Playbook generator.

Builds the definitive cold-outreach playbook for Viral Ideas (viralideamarketing.com)
synthesized from:
  - Onboarding call (Fireflies, 2026-04-29)
  - Business Dev Assessment spreadsheet (Drive)
  - UVP and Offer doc (Drive)
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from datetime import date

OUT = "/tmp/viral-gtm/Viral_GTM_Playbook.pdf"
NAVY = colors.HexColor("#0E2A47")
ACCENT = colors.HexColor("#C8362F")
LIGHT = colors.HexColor("#F4F6F9")
TEXT_GRAY = colors.HexColor("#3A3A3A")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("CoverTitle", parent=styles["Title"], fontSize=34,
                          textColor=NAVY, alignment=TA_CENTER, leading=40, spaceAfter=18))
styles.add(ParagraphStyle("CoverClient", parent=styles["Title"], fontSize=26,
                          textColor=ACCENT, alignment=TA_CENTER, leading=32, spaceAfter=12))
styles.add(ParagraphStyle("CoverSub", parent=styles["Normal"], fontSize=12,
                          textColor=TEXT_GRAY, alignment=TA_CENTER, leading=16))
styles.add(ParagraphStyle("H1", parent=styles["Heading1"], fontSize=18,
                          textColor=NAVY, spaceBefore=14, spaceAfter=8, leading=22))
styles.add(ParagraphStyle("H2", parent=styles["Heading2"], fontSize=14,
                          textColor=ACCENT, spaceBefore=10, spaceAfter=4, leading=18))
styles.add(ParagraphStyle("H3", parent=styles["Heading3"], fontSize=11,
                          textColor=NAVY, spaceBefore=6, spaceAfter=2, leading=14))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontSize=10,
                          textColor=TEXT_GRAY, alignment=TA_JUSTIFY, leading=14, spaceAfter=4))
styles.add(ParagraphStyle("BulletLine", parent=styles["Body"], leftIndent=14,
                          bulletIndent=2, spaceAfter=2))
styles.add(ParagraphStyle("CellBody", parent=styles["Normal"], fontSize=8.5,
                          textColor=TEXT_GRAY, leading=11))
styles.add(ParagraphStyle("CellHead", parent=styles["Normal"], fontSize=9,
                          textColor=colors.white, leading=11, alignment=TA_CENTER))
styles.add(ParagraphStyle("Quote", parent=styles["Body"], fontSize=10,
                          textColor=NAVY, leftIndent=20, rightIndent=20,
                          fontName="Helvetica-Oblique", spaceBefore=6, spaceAfter=6))

def H(s): return Paragraph(s, styles["H1"])
def H2(s): return Paragraph(s, styles["H2"])
def H3(s): return Paragraph(s, styles["H3"])
def P(s): return Paragraph(s, styles["Body"])
def B(s): return Paragraph(f"&bull;&nbsp; {s}", styles["BulletLine"])
def Q(s): return Paragraph(f'“{s}”', styles["Quote"])

def cell(s, head=False):
    style = styles["CellHead"] if head else styles["CellBody"]
    return Paragraph(str(s), style)

def page_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawString(0.9*inch, 0.45*inch, f"Viral Ideas Marketing  |  GTM Playbook  |  {date.today().isoformat()}")
    canvas.drawRightString(7.6*inch, 0.45*inch, f"Page {doc.page}")
    canvas.restoreState()

def cover_only(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, LETTER[1]-1.4*inch, LETTER[0], 0.18*inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 36)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-3.8*inch, "Go-To-Market Playbook")
    canvas.setFillColor(ACCENT)
    canvas.setFont("Helvetica-Bold", 28)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-4.6*inch, "Viral Ideas Marketing")
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 13)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-5.3*inch,
                             "The content engine for high-performing video at scale")
    canvas.setFont("Helvetica", 10)
    canvas.setFillColor(colors.HexColor("#BBBBBB"))
    canvas.drawCentredString(LETTER[0]/2, 1.7*inch, f"Generated {date.today().isoformat()}")
    canvas.drawCentredString(LETTER[0]/2, 1.45*inch, "Prepared by Outreach Magic / Kinetyca")
    canvas.drawCentredString(LETTER[0]/2, 1.20*inch, "CONFIDENTIAL — Internal Use Only")
    canvas.restoreState()

def make_table(rows, col_widths, header=True):
    if header:
        rows = [[cell(c, head=True) for c in rows[0]]] + [[cell(c) for c in r] for r in rows[1:]]
    else:
        rows = [[cell(c) for c in r] for r in rows]
    t = Table(rows, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#CCCCCC")),
    ]
    if header:
        style += [
            ("BACKGROUND", (0,0), (-1,0), NAVY),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
        ]
    t.setStyle(TableStyle(style))
    return t

def build():
    doc = SimpleDocTemplate(OUT, pagesize=LETTER,
                            leftMargin=0.9*inch, rightMargin=0.9*inch,
                            topMargin=0.9*inch, bottomMargin=0.8*inch,
                            title="Viral Ideas — GTM Playbook")
    story = []

    # Cover -- handled by page draw, just push a page break
    story.append(PageBreak())

    # ---- Table of Contents ----
    story.append(H("Table of Contents"))
    toc = [
        ("1. Client Overview", "page 3"),
        ("2. Unique Value Proposition & Positioning", "page 4"),
        ("3. Social Proof & Case Studies", "page 6"),
        ("4. Target Verticals", "page 7"),
        ("5. Ideal Customer Profiles & Personas", "page 9"),
        ("6. Pain-to-Value Mapping", "page 12"),
        ("7. Signals, Triggers & Timing", "page 15"),
        ("8. Cold Email Messaging Angles", "page 16"),
        ("9. Sales Process & Conversion", "page 18"),
        ("10. Tech Stack & Outreach Infrastructure", "page 19"),
        ("11. Goals, Metrics & Timeline", "page 20"),
        ("12. AI-Identified Opportunities", "page 21"),
        ("Appendix: Data Sources & Open Questions", "page 22"),
    ]
    for title_, p in toc:
        story.append(P(f"<b>{title_}</b> &nbsp;&nbsp; <i>{p}</i>"))
    story.append(PageBreak())

    # ---- Section 1 ----
    story.append(H("1. Client Overview"))
    story.append(P("<b>Viral Ideas Marketing</b> is a video content engine built to let marketing teams ship high-performing video at scale, without freelancer chaos or in-house overhead. Founded in 2015, the company runs an 83-person fully-remote production team that has edited over 100,000 videos for clients including McKesson, Procter &amp; Gamble, eBay, Self Financial, Sotheby's, Janssen, Johnson &amp; Johnson, and Chevrolet."))
    story.append(P("Roughly 95% of revenue comes from monthly editing retainers ($1,500&ndash;$5,000/mo). The remainder is project-based editing and limited remote / virtual production. Viral does not sell videos. It sells the system that makes video work at scale."))
    story.append(H2("Snapshot"))
    snapshot = [
        ["Field", "Detail"],
        ["Website", "viralideamarketing.com"],
        ["Founded", "2015"],
        ["Team", "83 people, fully remote"],
        ["Track record", "100,000+ videos edited"],
        ["Revenue (last year)", "$1.2M"],
        ["Revenue (current year, pacing)", "$2.4M"],
        ["Revenue goal (12 months)", "$5M"],
        ["Revenue goal (24 months)", "$10M"],
        ["Average deal size", "$1,500&ndash;$5,000/mo"],
        ["LTV", "~$12K"],
        ["Sales cycle", "~20 days first touch to close"],
        ["First-meeting close rate", "~20%"],
        ["Target CAC", "$400 (currently $800&ndash;$1,000)"],
        ["Geography", "US first, Canada second (no international)"],
        ["Lead volume target", "175&ndash;200 appointments / month"],
    ]
    story.append(make_table(snapshot, [1.7*inch, 5.0*inch]))
    story.append(H2("Core Product Tiers"))
    story.append(B("<b>Content Engine (ongoing retainer)</b> &mdash; ~95% of revenue. Three tiers based on weekly editing capacity: 10 hrs/wk, 20 hrs/wk, 40 hrs/wk."))
    story.append(B("<b>Project-based editing</b> &mdash; one-off campaigns, content libraries, repurposing engagements, event recaps."))
    story.append(B("<b>Remote / virtual production</b> &mdash; remote shoots when fresh footage is needed. Intentionally a small part of the mix."))
    story.append(B("<b>Lead magnet (free)</b> &mdash; Video Grader at <a href='https://video-grader.viralideamarketing.com'>video-grader.viralideamarketing.com</a> + 15-minute strategist walkthrough."))
    story.append(H2("Sales Org"))
    org = [
        ["Role", "Person", "Function"],
        ["CEO + S&M Director", "Dave Feinman", "Strategy, owner, currently dual-seat until lead flow stabilizes"],
        ["Head of Marketing", "Alejandra van Berkel", "Brand, content, manages two video editors"],
        ["Closer", "Ryder", "New business, ~20% close rate"],
        ["Account Manager", "Jess", "Existing account expansion / renewal"],
        ["Account Manager", "Lui", "Existing account expansion / renewal, onboarding handoff"],
        ["Appointment Setter", "Alina", "Reply triage, meeting booking via chat (Dan Martell method)"],
    ]
    story.append(make_table(org, [1.6*inch, 1.4*inch, 3.7*inch]))
    story.append(PageBreak())

    # ---- Section 2 ----
    story.append(H("2. Unique Value Proposition &amp; Positioning"))
    story.append(P("<b>Primary UVP:</b> &ldquo;We build the content engine that lets marketing teams ship high-performing video at scale, without freelancer chaos or in-house overhead.&rdquo;"))
    story.append(P("<b>Secondary UVP:</b> &ldquo;We give marketing teams a reliable, scalable system to never stop producing videos that drive ROI.&rdquo;"))

    story.append(H2("The Real Product"))
    story.append(P("Marketing leaders are not buying video. They are buying career insurance. When content slips, leadership blames the manager who chose the vendor &mdash; not the vendor. Every messaging decision should reflect that."))

    story.append(H2("Five Differentiators (use these in copy)"))
    diffs = [
        ("Volume AND quality, no tradeoff",
         "Subscription editors do volume but not enterprise-grade quality. Agencies do quality but cannot ship 500 videos a month. Viral is the only model in the category built specifically to deliver both at scale."),
        ("Strategic creative guidance, not order-taking",
         "Most editors execute briefs. Viral brings platform-specific expertise, hook strategy, and performance thinking before the edit starts. Doctor Frame in practice &mdash; symptom in, diagnosis out."),
        ("Built for scale from day one",
         "Structured pods, managing editors, QA checkpoints, standardized workflows. Anyone can make 5 videos. Few can reliably make 500."),
        ("System over talent",
         "Trained team, standardized processes, QA. Does not depend on finding unicorn editors. A single editor leaving never blows up an engagement."),
        ("Speed without sacrificing quality",
         "Same-day first drafts. Predictable turnaround. Slack response inside one hour on business days. Humans + AI, with humans in control of creativity and judgment."),
    ]
    drows = [["Differentiator", "Why no competitor matches it"]]
    for n, d in diffs:
        drows.append([n, d])
    story.append(make_table(drows, [1.9*inch, 4.8*inch]))

    story.append(H2("Top 3 Competitor Categories"))
    comp_rows = [
        ["Category", "Examples", "Where Viral wins"],
        ["Subscription editing services", "Design Pickle, BeCreatives", "B2B sophistication and strategic creative input"],
        ["Traditional video production agencies", "Generic regional shops", "Speed, predictability, built-for-volume infrastructure"],
        ["Freelance editor marketplaces", "Upwork, Fiverr, individual freelancers", "Reliability and a system that survives any one editor leaving"],
    ]
    story.append(make_table(comp_rows, [1.8*inch, 1.9*inch, 3.0*inch]))

    story.append(H2("Voice and Messaging Guardrails"))
    story.append(P("Pulled from the 2026 Brand Book. Every cold email must pass these tests before it ships."))
    story.append(B("<b>Calm and confident.</b> Never urgent or hype-driven."))
    story.append(B("<b>Direct.</b> Lead with the point. No fluff, no hedging, no corporate speak."))
    story.append(B("<b>Specific.</b> &ldquo;We respond within one hour on business days&rdquo; beats &ldquo;we&rsquo;re responsive.&rdquo;"))
    story.append(B("<b>You over we.</b> The client&rsquo;s world is the center of the conversation."))
    story.append(B("<b>Active voice always.</b> &ldquo;Our team delivers same-day&rdquo; not &ldquo;first drafts are delivered same-day.&rdquo;"))
    story.append(B("<b>Grade 8&ndash;10 reading level.</b> Smart and busy audience &mdash; short words and clear sentences are a courtesy."))
    story.append(H3("On-brand phrases (use freely)"))
    for ph in ['"Here\'s the plan."', '"We know what works."', '"What actually moves the needle."',
               '"We build content engines, not single videos."', '"Plug in and trust it."', '"Clarity, not chaos."',
               '"We&rsquo;re not here to make one great video. We&rsquo;re here to make sure you never stop producing them."']:
        story.append(B(ph))
    story.append(H3("Off-brand language &mdash; banned"))
    story.append(P("These phrases torpedo the brand even if they boost reply rates short-term:"))
    story.append(B("Hype: revolutionary, game-changing, disruptive, world-class, best-in-class, cutting-edge."))
    story.append(B("Aggressive sales: crush, dominate, 10x, skyrocket, hack the algorithm, blow up your brand, don&rsquo;t get left behind."))
    story.append(B("Generic agency speak: synergy, holistic strategy, full-funnel ecosystem, leverage (verb), omnichannel excellence."))
    story.append(B("Vague claims: &ldquo;we care about your brand,&rdquo; &ldquo;we create amazing content,&rdquo; &ldquo;passionate about storytelling.&rdquo;"))
    story.append(B("Self-important titles: guru, ninja, rockstar, visionary, white-glove, bespoke, elite."))
    story.append(B("Overused content phrases: &ldquo;authentic storytelling,&rdquo; &ldquo;elevate your brand,&rdquo; &ldquo;drive awareness,&rdquo; &ldquo;telling your story.&rdquo;"))
    story.append(PageBreak())

    # ---- Section 3 ----
    story.append(H("3. Social Proof &amp; Case Studies"))
    story.append(P("Viral has the strongest case study library in pharma/healthcare and a deep enterprise consumer track record. Below is the bench available for vertical-tagged outreach."))
    story.append(H2("Anchor logos by vertical"))
    proof = [
        ["Vertical", "Anchor proof points"],
        ["Healthcare / Pharma",
         "McKesson (Ontada subsidiary), Janssen, Johnson &amp; Johnson, Cortechs.ai, Ultrasound.ai, si-bone.com, Inbody"],
        ["Ecommerce / DTC", "eBay (enterprise consumer), Procter &amp; Gamble, plus active growth-stage DTC client work"],
        ["Marketing &amp; PR Agencies", "Clever Digital Marketing (Canada, ~$10M, ~80 employees), sagefrog.com, bemarketing.com"],
        ["SaaS / B2B", "Self Financial ($100M+ revenue), Gainbridge (subsidiary of Group 1001, ~$160B AUM)"],
        ["Professional Services", "Asset Map (financial advisor SaaS, client since 2017), AICPA"],
        ["Enterprise consumer", "Sotheby&rsquo;s, Chevrolet"],
    ]
    story.append(make_table(proof, [1.9*inch, 4.8*inch]))

    story.append(H2("Voice-of-customer quotes (use directly in copy)"))
    quotes = [
        "I&rsquo;ve been through so many editors. Will be back.",
        "Working with David and his team was effortless and great. The communication and end product were sublime.",
        "Your people are Johnny on the spot. I send a message, I get a message back in an hour.",
        "I sent them a brief and got back exactly what I wanted.",
        "I could describe the vision, but they were the ones who operationalized it and executed it beautifully. The final product was better than I could have imagined.",
        "Their pricing was fair, their timelines were reliable, and above all, I felt like I could genuinely trust them.",
    ]
    for q in quotes:
        story.append(Q(q))
    story.append(P("<b>Pattern across reviews:</b> clients praise the experience, communication, and reliability &mdash; not the editing itself. That is the real product. Outbound should reflect that."))
    story.append(P("<b>Gap to close:</b> 2&ndash;3 named outcome metrics per priority vertical (e.g., &ldquo;produced X edits/month for Y,&rdquo; &ldquo;cut turnaround from Z days to A days&rdquo;) &mdash; assigned to Dave to backfill before campaign 1 launches."))
    story.append(PageBreak())

    # ---- Section 4 ----
    story.append(H("4. Target Verticals"))
    story.append(P("Six verticals exist on the table; the first 90 days focus heavily on Healthcare/Pharma. Once one vertical produces predictable lead flow, the model branches out. Verticals are ranked by expected return on outbound effort &mdash; deal size, sales-cycle clarity, and case study density."))
    verticals = [
        ("1. Healthcare &amp; Pharma — PRIORITY", "Client-confirmed",
         "Pharma manufacturers, biotech, healthcare systems, clinics, health tech, pharma divisions of larger conglomerates, med device.",
         "Revenue $1M+. Size of headcount does not matter; usually tap into smaller divisions.",
         "VP Marketing, Senior Director of Brand, Head of Content, Brand Lead, Senior Business Director, Sr. Manager of Product Management, Triggered Education, Marketing/Creative/Channel Strategy, Motion Graphics &amp; Video Production Specialist, Training &amp; Development Manager (sometimes HR). Below $5M: Founder/Owner/CEO. Never finance or accounting.",
         "Regulated content workflow is slow and expensive; med-legal-regulatory review eats velocity; in-house teams cannot keep up with HCP and patient content volume; missing a deadline before a product launch is a career-risk event.",
         "McKesson (Ontada), Janssen, J&amp;J, Cortechs.ai, Ultrasound.ai, si-bone.com, Inbody.",
         "Largest deal sizes, longest LTV, most enterprise wins, strongest existing case study library. If outbound works in pharma in 60 days the rest of the strategy compounds."),
        ("2. Marketing &amp; PR Agencies", "Client-confirmed (fastest to close)",
         "Mid-to-large agencies, $5M&ndash;$50M revenue, 30&ndash;150 employees, that resell video to their own clients. Focus on agencies that do one thing really well (so volume of one offer scales).",
         "$5M&ndash;$50M revenue, 30&ndash;150 FTE.",
         "CEO, Founder, COO, Head of Production. Champions: Marketing Managers, CMOs, Head of Content, Social Media Marketing, Content/Brand/Video leads &mdash; the ones with a corporate card and decision-power.",
         "Editing is the chokepoint on their delivery. Need a partner that disappears behind their brand. One bad video at the wrong moment can cost a contract worth 10x what they pay an editing partner.",
         "Clever Digital Marketing (Canada, ~$10M, ~80 employees), sagefrog.com, bemarketing.com.",
         "Fastest sales cycle of any vertical. Sticky once landed. Best-fit buyer for the &lsquo;white-label trust&rsquo; angle."),
        ("3. Ecommerce / DTC", "Client-confirmed",
         "Product-driven, high-volume content brands. $5M+ DTC revenue. Heaviest fit with brands that run weekly creative iterations on Meta / TikTok / YouTube.",
         "$5M+ DTC revenue.",
         "Founder, Head of Creative, Head of Performance, Growth Marketer.",
         "Weekly cadence of ad creative variations across Meta, TikTok, YouTube; in-house teams burn out; freelancer rosters are inconsistent; running out of fresh creative mid-campaign.",
         "eBay (enterprise consumer), P&amp;G, plus active growth-stage DTC client work.",
         "High-volume vertical; recurring monthly need; great fit for tier 2 (20 hrs/wk) and tier 3 (40 hrs/wk) packages."),
        ("4. SaaS / B2B", "In-scope (TBD priority)",
         "Well-funded SaaS or growth-stage B2B, $5M&ndash;$50M revenue.",
         "$5M&ndash;$50M revenue. Series B&ndash;C lifecycle.",
         "Growth Marketer, Head of Marketing, Content Lead, Founder/CEO.",
         "Quarterly roadmap shifts content needs weekly; needs to fuel paid ads, organic, and investor-facing brand presence simultaneously; cannot scale by hiring.",
         "Self Financial ($100M+), Gainbridge (Group 1001 ~$160B AUM).",
         "Sophisticated buyers; respond to platform expertise framing. Needs Dave to confirm priority for first 90 days."),
        ("5. Professional Services (financial / consulting)", "In-scope (TBD priority)",
         "Premium-positioned firms whose content does not match their reputation; long-term relationship buyers, not project shoppers.",
         "$5M&ndash;$30M revenue. Established practices.",
         "Founder, Head of Marketing, Director of Communications.",
         "Brand-content mismatch &mdash; firm looks bigger than its content suggests. Premium reputation but shallow video presence.",
         "Asset Map (client since 2017), AICPA, broader financial/accounting heritage.",
         "High LTV when landed (8+ year client relationships). Slow first sale. Best in second wave."),
        ("6. Law Firms", "Lower priority (call note: avoid as primary)",
         "Multi-office regional firms and AmLaw-adjacent. NOT solo attorneys.",
         "Multi-office regional or AmLaw-adjacent.",
         "Director of Marketing, Chief Marketing Officer, Business Development Lead.",
         "Compliance-sensitive content; needs to look premium without feeling slick; partners distrust generic agencies.",
         "pareto.legal.",
         "Onboarding call flagged law firms as &lsquo;high-risk targets&rsquo; to avoid in v1. Brand book lists them; assessment lists HVAC instead. Reconcile with Dave before adding to scope."),
    ]
    for i, (name, conf, target, size, buyer, pain, proof_, why) in enumerate(verticals):
        rows = [
            ["Targets", target],
            ["Company size sweet spot", size],
            ["Buyer titles", buyer],
            ["Pain point", pain],
            ["Anchor proof", proof_],
            ["Why this vertical", why],
        ]
        story.append(H2(f"{name}"))
        story.append(P(f"<i>Confidence: {conf}</i>"))
        story.append(make_table(rows, [1.5*inch, 5.2*inch], header=False))
    story.append(PageBreak())

    # ---- Section 5 ----
    story.append(H("5. Ideal Customer Profiles &amp; Personas"))
    story.append(P("Five named personas pulled directly from the assessment, each with a real-world example the sales team has actually closed. Each persona has a distinct hook for outbound."))
    personas = [
        ("Sierra — the buttoned-up Marketing Manager",
         "Marketing Manager / Senior Marketing Manager",
         "$50M&ndash;$500M B2C or B2B, structured corporate environment",
         "Sierra Bowman (formerly Self Financial, $100M+ revenue)",
         "$5K&ndash;$10K/mo without major approvals",
         "&ldquo;If this vendor makes me look bad to my leadership, I&rsquo;m the one on the performance review. Not them.&rdquo;",
         "Reliability and brand consistency. <b>&ldquo;Never wonder if your video is going to land on time again.&rdquo;</b>",
         "Branded content, social cuts, sales enablement, brand films, recurring corporate communications.",
         "Approves $5K/mo without escalation. Anything above $10K needs CMO sign-off."),
        ("Brittany — Senior Marketing Director at a subsidiary",
         "Senior Marketing Director / Director of Marketing / Senior Business Director",
         "Pharma, healthcare, or enterprise subsidiary of a $500M&ndash;$10B parent",
         "Brittany Luxon, Sr. Business Director at Ontada (McKesson subsidiary)",
         "Budget is not the constraint &mdash; trust and risk are",
         "&ldquo;McKesson doesn&rsquo;t blink at a $50K invoice. But if I choose the wrong partner and something goes wrong, that&rsquo;s my name on it.&rdquo;",
         "Risk reduction. <b>&ldquo;We get the brief on the first try. We catch issues before they reach your desk.&rdquo;</b>",
         "Regulated HCP and patient content, clinical trial visualizations, medical congresses, KOL interviews.",
         "Spends to avoid risk, not to chase savings. Lean hard into J&amp;J / McKesson logos and the &lsquo;does not make me look bad&rsquo; frame."),
        ("Lindsey — growth marketer at a structured startup",
         "Growth Marketer / Head of Marketing / Content Lead",
         "Well-funded startup or growth-stage, $5M&ndash;$50M revenue",
         "Lindsey McKone, Growth Marketer at Gainbridge (Group 1001, ~$160B AUM)",
         "Tactical $1.5K&ndash;$5K/mo retainers; can pull strings on bigger if performance is proven",
         "&ldquo;If our content pipeline dries up in the middle of our growth push, we lose momentum, and I lose credibility.&rdquo;",
         "Speed and scale on demand. <b>&ldquo;Same-day first drafts. Scale up volume instantly when a campaign is working.&rdquo;</b>",
         "Paid ads creative, brand explainers, founder content, podcast clips, performance UGC repurposing.",
         "Pilots small ($1.5K), expands fast if month 1 produces. Best fit for tier 1 retainer."),
        ("Daniel — the agency partner",
         "CEO / Founder / Head of Production",
         "Mid-to-large marketing or creative agency, $5M&ndash;$50M revenue, 30&ndash;150 FTE",
         "Daniel Rahmon, CEO of Clever Digital Marketing (Canada, ~$10M revenue, ~80 employees)",
         "Owner-operator, can sign on the spot",
         "&ldquo;My reputation with my clients is everything. One bad video at the wrong moment can cost me a contract worth 10x what I&rsquo;m paying an editing service.&rdquo;",
         "White-label trust. <b>&ldquo;An editing partner that plugs into your team and never embarrasses you in front of a client.&rdquo;</b>",
         "White-labeled retainer that resells under their brand to their end clients.",
         "Warm channel: agency that wins a video-heavy client triggers a buying window in week 1. Hire signal &lsquo;Head of Production&rsquo; is the strongest tell."),
        ("Adam — the forward-thinking founder",
         "Founder / CEO",
         "Established professional-services startup or SaaS, $5M&ndash;$30M revenue",
         "Adam Holt, Founder of Asset Map (client since 2017)",
         "CEO budget &mdash; whatever is needed",
         "&ldquo;We&rsquo;ve built a strong product and a strong reputation. I don&rsquo;t want the content to be the thing that makes us look smaller than we are.&rdquo;",
         "Strategic partnership. <b>&ldquo;Not just execution &mdash; a team that gets B2B positioning and thinks about your growth long-term.&rdquo;</b>",
         "Brand-positioning content, founder thought leadership, customer story films, conference content recycling.",
         "Long-cycle but extreme LTV (8+ years for Asset Map). Best for second-wave campaigns once core verticals run."),
    ]
    for name, title, company, example, budget, fear, hook, content, note in personas:
        story.append(H2(name))
        rows = [
            ["Title", title],
            ["Company", company],
            ["Real example", example],
            ["Budget authority", budget],
            ["Real fear", fear],
            ["Outbound hook", hook],
            ["Content needs", content],
            ["Targeting note", note],
        ]
        story.append(make_table(rows, [1.4*inch, 5.3*inch], header=False))
    story.append(PageBreak())

    # ---- Section 6 ----
    story.append(H("6. Pain-to-Value Mapping"))
    story.append(P("Every pain maps to a value. Every value is tied to a metric the buyer actually owns. No orphans."))

    pain_value = [
        ("Production Output Is Unreliable",
         "Freelancers ghost mid-campaign. Agency takes two weeks per video. In-house editor leaves and the team starts over. Production becomes a single point of failure for the entire marketing function.",
         "Dedicated editors backed by a structured pod. Same-day first drafts. Slack response within one hour on business days. The system survives any one editor leaving.",
         "Predictable monthly throughput. Marketing manager stops chasing vendors and starts spending time on strategy."),
        ("Volume and Quality Cannot Coexist Today",
         "They can get one great video from an agency, or 50 mediocre ones from a low-cost platform. They cannot get 50 great videos consistently. The system that produces volume sacrifices quality. The system that produces quality cannot scale.",
         "Structured pods, managing editors, QA checkpoints, standardized workflows. Volume can ramp from 5 videos a month to 500 without breaking.",
         "Maintain enterprise-grade quality at startup-grade speed and volume. Same brand consistency at 10x output."),
        ("Marketing Leaders Carry Personal Career Risk",
         "When content slips, leadership does not blame the vendor. They blame the marketing manager who chose the vendor. The buyer is rarely buying video. They are buying career insurance.",
         "Risk-reducing system: vetted enterprise track record (J&amp;J, McKesson, eBay, Self Financial), QA built in, named editor and managing editor on every account, brief-on-the-first-try workflow.",
         "Marketing manager keeps their job. No surprise misses before exec review. Career insurance baked into every deliverable."),
        ("Quarterly KPIs Miss When Production Falls Apart",
         "Wasted ad spend because creative refreshes are too slow. Inconsistent brand presence across LinkedIn, YouTube, Instagram, TikTok. Marketing team manages five vendors instead of doing strategy.",
         "One partner instead of five vendors. Platform-specific cuts produced in parallel. Performance feedback loop on which hooks land.",
         "Hit ad-creative refresh cadence. Stop missing campaign launch dates. Reclaim 8&ndash;12 hours a week of vendor management."),
        ("Status Quo Costs More Than They Realize",
         "Freelancer at $30/hr is $0 when they ghost, $5,000 in damage when a campaign launch slips. In-house editor: $80K&ndash;$120K fully loaded for one person. Subscription editing services serve smaller, less sophisticated clients.",
         "Production system at $1,500&ndash;$5,000/mo for a whole pod. No hiring overhead, no PTO gaps, no single point of failure. Reframe against total cost of ownership.",
         "Replace one in-house editor with a full pod for less than the salary cost. Eliminate freelancer recovery costs."),
    ]
    pv_rows = [["Pain", "Value (Viral solution)", "Outcome / metric"]]
    for n, p, v, o in pain_value:
        pv_rows.append([f"<b>{n}</b><br/>{p}", v, o])
    story.append(make_table(pv_rows, [2.4*inch, 2.4*inch, 1.9*inch]))
    story.append(PageBreak())

    # ---- Section 7 ----
    story.append(H("7. Signals, Triggers &amp; Timing"))
    story.append(P("&ldquo;The list is the message.&rdquo; Each signal below tells us a prospect has either admitted a content gap or just unlocked budget. The list build is signal-first; ICP filtering is the secondary screen."))

    story.append(H2("Hiring signals (strongest single category)"))
    for s in [
        "New CMO, VP of Marketing, or Head of Content posted on LinkedIn &mdash; incoming leaders almost always reset their content stack inside the first 90 days.",
        "Open role: Video Editor, Content Producer, or Social Media Manager &mdash; they have already admitted production is the bottleneck.",
        "Open role: Paid Social Manager or Performance Marketer &mdash; paid social runs on creative volume; a new hire creates immediate creative demand.",
        "Open role: Freelance Video Editor or Contract Editor &mdash; an active confession of a content gap.",
    ]:
        story.append(B(s))

    story.append(H2("Funding and growth signals"))
    for s in [
        "Recent funding round (Series A&ndash;C) &mdash; budget unlocked; growth marketing mandated.",
        "Revenue or headcount growth (Crunchbase, LinkedIn) &mdash; marketing always lags ops; content needs explode.",
        "Acquisition or merger announcement &mdash; brand consolidation drives a six-month surge in repurposing needs.",
        "Geographic expansion or new market entry &mdash; same brand, multiple regional content variants needed.",
    ]:
        story.append(B(s))

    story.append(H2("Product and content signals"))
    for s in [
        "New product launch announced &mdash; demo videos, sales enablement, ad creative all needed within weeks.",
        "New podcast, webinar series, or YouTube channel launched &mdash; long-form raw material we repurpose.",
        "New website launch &mdash; fresh assets need video versions for every platform.",
        "Increased ad spend on Meta or LinkedIn (visible via ad libraries) &mdash; running through creative faster than they can produce.",
    ]:
        story.append(B(s))

    story.append(H2("Vertical-specific triggers"))
    for s in [
        "<b>Pharma/biotech:</b> FDA approval, clinical trial milestone, new indication launch, partnership with HCP networks.",
        "<b>Ecommerce:</b> new product line, seasonal launch (BFCM, holiday, summer), shift to a new ad platform.",
        "<b>Marketing agencies:</b> announced new client win (especially video-heavy), opened a new office or service line.",
        "<b>Pro services:</b> new partner announcement, new practice area, regulatory or class-action moment driving client demand.",
    ]:
        story.append(B(s))

    story.append(H2("Negative signals &mdash; do NOT contact"))
    for s in [
        "DIY creators just starting out (no content pipeline, no footage flow).",
        "Budget negotiators benchmarking against $5/hr Fiverr editors.",
        "Wrong-industry: wedding videographers, music video producers, bar/bat mitzvah, hype-driven startup-bro founders, political campaigns, gambling.",
        "Micromanagers: need to approve every 10-second cut.",
        "Full-service expectation: want graphic design, copywriting, web dev, SEO from one team.",
        "Organizationally chaotic: no internal process, no clear approval chain.",
        "Solo attorneys (vs multi-office firms).",
    ]:
        story.append(B(s))
    story.append(PageBreak())

    # ---- Section 8 ----
    story.append(H("8. Cold Email Messaging Angles"))
    story.append(P("Each vertical gets at least two angles. Subject lines lowercase, max 3 words, person/company names capitalized."))

    angles = [
        ("Healthcare / Pharma",
         "Sierra/Brittany",
         "Med-legal-regulatory review eats velocity; in-house cannot keep up with HCP and patient content volume; missing a launch deadline is a career-risk event.",
         "Risk reduction + enterprise track record. &ldquo;We get the brief on the first try. We catch issues before they reach your desk.&rdquo;",
         "J&amp;J, McKesson (Ontada), Janssen, Cortechs.ai by name &mdash; they want to hear logos that match their environment.",
         "<i>content engine</i> | <i>video pipeline</i> | <i>review cycles</i>"),
        ("Ecommerce / DTC",
         "Lindsey",
         "Weekly creative refresh on Meta/TikTok burns out in-house teams; running out of fresh ad creative mid-campaign.",
         "Speed and scale on demand. &ldquo;Same-day first drafts. Scale up volume instantly when a campaign is working.&rdquo;",
         "eBay enterprise consumer footprint, P&amp;G, active growth-stage DTC clients. Mention specific creative-volume metrics where available.",
         "<i>creative volume</i> | <i>same day cuts</i> | <i>weekly refresh</i>"),
        ("Marketing &amp; PR Agencies",
         "Daniel",
         "Editing chokepoint hurts client delivery; one bad video costs an account 10x what they pay an editing partner.",
         "White-label trust. &ldquo;An editing partner that plugs into your team and never embarrasses you in front of a client.&rdquo;",
         "Clever Digital Marketing (Canada, ~$10M, ~80 FTE), sagefrog.com, bemarketing.com.",
         "<i>white label</i> | <i>delivery layer</i> | <i>client safety</i>"),
        ("SaaS / B2B",
         "Lindsey/Adam",
         "Quarterly roadmap shifts content needs weekly; can&rsquo;t scale by hiring; needs paid + organic + investor brand simultaneously.",
         "Scalable system, not another vendor. &ldquo;Plug in and trust it.&rdquo; Platform-specific hook strategy, not generic editing.",
         "Self Financial ($100M+), Gainbridge (Group 1001 ~$160B AUM).",
         "<i>content system</i> | <i>scale not hire</i> | <i>roadmap content</i>"),
        ("Pro Services (financial / consulting)",
         "Adam",
         "Premium-positioned firm whose content does not match its reputation; long-term relationship buyers, not project shoppers.",
         "Strategic partnership. &ldquo;A team that gets B2B positioning and thinks about your growth long-term.&rdquo;",
         "Asset Map (client since 2017), AICPA, broader financial/accounting heritage.",
         "<i>brand fit</i> | <i>premium content</i> | <i>positioning</i>"),
    ]
    for vert, persona, hook, value, proof_, subj in angles:
        story.append(H2(vert))
        story.append(P(f"<b>Primary persona:</b> {persona}"))
        story.append(B(f"<b>Hook:</b> {hook}"))
        story.append(B(f"<b>Value lead:</b> {value}"))
        story.append(B(f"<b>Proof to cite:</b> {proof_}"))
        story.append(B(f"<b>Subject line direction:</b> {subj}"))

    story.append(H2("Email 1 structure (lead magnet thread)"))
    story.append(B("<b>Hook paragraph:</b> name a vertical-specific pain in their words."))
    story.append(B("<b>Social proof paragraph:</b> drop one named logo from the same vertical."))
    story.append(B("<b>Audit offer paragraph (own paragraph):</b> Video Grader + 15-minute walkthrough."))
    story.append(B("<b>CTA paragraph:</b> ask one yes/no question. No double-CTA."))
    story.append(P("60&ndash;80 words. No em dashes. No exclamation marks. No spam words. No bracketed placeholders. Signature handled by the EmailBison system variable."))
    story.append(H2("Email 2 (service offer thread)"))
    story.append(B("Same lead, separate thread, ~7 days later. Pivot from audit to retainer."))
    story.append(B("Hook: name the symptom they probably have (e.g., &lsquo;creative refresh slipping into next sprint&rsquo;)."))
    story.append(B("Body: the production-engine reframe (system over talent)."))
    story.append(B("CTA: 15-minute call to walk through how a pod would plug into their existing setup."))
    story.append(PageBreak())

    # ---- Section 9 ----
    story.append(H("9. Sales Process &amp; Conversion"))
    story.append(P("Lead reply lands in Alina&rsquo;s queue first &mdash; she follows the Dan Martell sell-by-chat pattern, qualifies, then books Ryder for the closing call. Account managers Jess and Lui handle expansion at month 3 and month 6."))
    sales_table = [
        ["Stage", "Owner", "Goal", "Watch-outs"],
        ["Lead reply", "Alina (appointment setter)", "Qualify reply, BANT-style, book a demo with Ryder", "Sell-by-chat method; do not pitch in DM"],
        ["Discovery call", "Ryder (closing 90% of new business) or David", "Understand pain, prescribe Doctor Frame, qualify volume need", "Lead with their problem before any pricing"],
        ["Proposal &amp; close", "Ryder", "Standard proposal template; Doctor-Frame-first, then pricing", "~20% close rate today, target 30%+"],
        ["Onboarding handoff", "Lui or Jess", "Dedicated editor assigned, brand kit captured, first deliverable inside 7 days", "Capture brand kit on call 1, do not delay"],
        ["Expansion", "Lui / Jess", "Pitch volume increases at month 3 and month 6", "Use churn-risk Slack channel (Zach) to spot stalls"],
    ]
    story.append(make_table(sales_table, [1.2*inch, 1.5*inch, 2.4*inch, 1.6*inch]))

    story.append(H2("Top 3 objections + responses"))
    obj = [
        ("&ldquo;We already have freelancers / an in-house editor.&rdquo;",
         "Don&rsquo;t replace them. Be the relief valve. &ldquo;Keep your in-house editor for the strategic stuff. Use us for the volume that&rsquo;s drowning them.&rdquo;"),
        ("&ldquo;Your pricing seems high for editing.&rdquo;",
         "Reframe against total cost. A freelancer at $30/hr = $0 when they ghost, $5K in damage when launch slips. In-house = $80K&ndash;$120K loaded. Viral = $1,500&ndash;$5,000/mo for a whole production system."),
        ("&ldquo;How do we know quality will be consistent?&rdquo;",
         "Show the system: QA checkpoints, managing editor structure, vertical case studies. Offer a paid trial period or no-risk first edit. Drop named logos in their environment (J&amp;J, McKesson, eBay, Self Financial, Asset Map)."),
    ]
    for q, a in obj:
        story.append(B(f"<b>{q}</b>"))
        story.append(P(a))

    story.append(H2("CRM workflow"))
    story.append(B("CRM: GoHighLevel (transitioned from HubSpot this week). Used daily by sales."))
    story.append(B("Outbound source: EmailBison (this engagement). Replies route to Alina."))
    story.append(B("Reporting cadence: monthly working session with Outreach Magic. Weekly numbers, monthly L10 review feeds reply intelligence back to messaging, paid ads, organic content."))
    story.append(PageBreak())

    # ---- Section 10 ----
    story.append(H("10. Tech Stack &amp; Outreach Infrastructure"))
    story.append(H2("Outreach Magic stack (this engagement)"))
    om = [
        ["Tool", "Purpose", "Rule"],
        ["EmailBison", "Cold email send, sequencing, reply routing", "Per-client workspace. Always create campaigns PAUSED. Verify workspace before any operation."],
        ["Heyreach", "LinkedIn parallel touch on prioritized accounts", "Optional layer for healthcare/agency tier. Mirror copy rules."],
        ["Apollo / Sales Nav", "Account list build (firmographics + roles)", "Tag verticals at source; never mix with another client's lists."],
        ["BlitzAPI", "Email finding (priority 1 in waterfall)", "x-api-key header; never Bearer."],
        ["Debounce", "Email validation (priority 2)", "Stop sending if no credits."],
        ["FindyMail", "Email finding (priority 3)", "Email-find only; never company / domain enrichment."],
        ["LeadMagic", "Email finding + validation (priority 4)", "Email-find only. No enrichment fallback."],
        ["BounceBan", "Final bounce filter (priority 5)", "Skip = 31% bounce risk. Never skip."],
        ["Supabase", "Central leads table", "Project tcyblrzlgdmffkwremqs. Client isolation filter every query."],
        ["Gemini 2.5 Flash", "Per-lead copy generation", "~$2&ndash;3 per 400 leads. Never Claude for bulk copy."],
        ["DeepSeek", "Personalization openers, scoring", "Only after the email waterfall passes."],
        ["EmailBison validator", "validate_variables.py pre-flight", "Hard-fail on brackets, empty PS_LINE, spam words, signatures."],
    ]
    story.append(make_table(om, [1.4*inch, 2.4*inch, 2.9*inch]))

    story.append(H2("Viral&rsquo;s own stack"))
    story.append(B("CRM: GoHighLevel (just migrated from HubSpot)."))
    story.append(B("Cold email tested historically: Instantly &mdash; minimal results. Replaced by EmailBison for this engagement."))
    story.append(B("Project management: ClickUp."))
    story.append(B("Lead magnet tool: Video Grader at video-grader.viralideamarketing.com (built in-house)."))
    story.append(B("Paid ads: ran for sister brand BBM &mdash; performance disappointing relative to spend."))
    story.append(PageBreak())

    # ---- Section 11 ----
    story.append(H("11. Goals, Metrics &amp; Timeline"))
    goals = [
        ["Horizon", "Target"],
        ["12-month revenue", "$5M (closing the $2.6M gap from $2.4M pace)"],
        ["24-month revenue", "$10M"],
        ["Outbound appointments / month", "175&ndash;200 (current: ~3 calls/day; capacity: ~12/day)"],
        ["Sales utilization (close)", "Fill the 75% capacity gap from current 25%"],
        ["Target CAC", "$400 (current ~$800&ndash;$1,000)"],
        ["First-meeting close rate", "30%+ (current ~20%)"],
        ["Bounce rate ceiling", "&lt;3% on every send"],
        ["Reply-rate target by vertical", "Set baselines after first 4 weeks of sends"],
    ]
    story.append(make_table(goals, [2.6*inch, 4.1*inch]))

    story.append(H2("Phase plan (first 90 days)"))
    phases = [
        ("Weeks 1&ndash;2 — foundation",
         "GTM playbook complete (this document). EmailBison workspace provisioned. Sending domains warmed. List build for healthcare/pharma vertical ready (target ~2,500 contacts)."),
        ("Weeks 3&ndash;4 — campaign 1: healthcare",
         "Healthcare/pharma campaign live in test batch (50 leads). Copy approved by Dave. Iterate on subject and Email 1 hook. Begin reply intelligence loop with Alina."),
        ("Weeks 5&ndash;6 — campaign 2: agencies",
         "Agencies campaign live. Reuse healthcare hooks where they map; rewrite Email 1 for white-label trust angle. Daniel persona is the headline."),
        ("Weeks 7&ndash;8 — scale healthcare",
         "Healthcare moves to full volume after iteration. Add ecommerce campaign (Lindsey persona)."),
        ("Weeks 9&ndash;12 — full pipeline",
         "Three verticals running concurrently. Begin signal-based campaigns (new-CMO, hiring-video-editor). First L10 review feeds reply intelligence into copy."),
    ]
    for n, body in phases:
        story.append(H3(n))
        story.append(P(body))

    story.append(H2("Reporting"))
    story.append(B("Weekly: per-vertical reply rate, positive replies, bounces, meetings booked."))
    story.append(B("Monthly: working session with Dave + Ale to feed reply intelligence into messaging, paid ads, and organic content."))
    story.append(B("Quarterly: L10 review feeds intelligence into the broader marketing function (BBM paid ads, LinkedIn organic, sales playbook)."))
    story.append(PageBreak())

    # ---- Section 12 ----
    story.append(H("12. AI-Identified Opportunities"))
    story.append(P("Hypotheses surfaced from cross-referencing the assessment, the brand book, and the call transcript that Dave has not yet validated. Treat as test bets, not confirmed strategy."))
    aio = [
        ("Healthcare-only first 90 days",
         "Dave explicitly said he would rather we crush one vertical than hedge across six. Brand book and assessment both rank healthcare first. <b>Recommendation:</b> commit weeks 1&ndash;6 to healthcare/pharma only; resist pressure to spread early."),
        ("Trigger-first list build over flat ICP filter",
         "Assessment lists rich trigger taxonomy (FDA approval, new CMO, hiring video editor) but no current channel uses them. <b>Recommendation:</b> the first signal-based campaign should be &lsquo;hiring video editor in last 30 days&rsquo; &mdash; it is an active confession of pain."),
        ("Doctor-Frame proposal as inbound qualifier",
         "Free Video Grader + 15-min walkthrough is the strongest acquisition lever the brand book describes. <b>Recommendation:</b> route every &lsquo;interested but not ready&rsquo; reply into the grader before Ryder ever takes a call. Let the tool pre-qualify."),
        ("Past-champion campaign (untouched)",
         "Brand book hints at &lsquo;old lists&rsquo; and an ebook-driven nurture but neither is currently running. <b>Recommendation:</b> evergreen campaign #1 is past-champions / closed-lost from HubSpot import."),
        ("Unbranded benchmark for the agency vertical",
         "Daniel persona buys white-label trust. The Video Grader page is on viralideamarketing.com &mdash; agency buyers will not send a client there. <b>Recommendation:</b> build a no-logo agency-friendly version (gradevideo.com or similar) before campaign 2."),
        ("BBM paid-ad post-mortem feeds messaging",
         "BBM paid-ads report is referenced but not yet integrated. <b>Recommendation:</b> Dave to attach to next working session; reply intelligence + ad data should converge."),
        ("Pricing transparency in cold email (open question)",
         "Brand book values &ldquo;clear pricing with no surprises.&rdquo; Open question whether to put $1,500&ndash;$5,000/mo in cold copy. <b>Recommendation:</b> A/B test &mdash; transparent in healthcare (helps trust), price-discovery in agencies (helps close rate)."),
    ]
    for n, body in aio:
        story.append(H3(n))
        story.append(P(body))
    story.append(PageBreak())

    # ---- Appendix ----
    story.append(H("Appendix"))
    story.append(H2("Data sources used"))
    story.append(B("<b>Onboarding call:</b> Onboarding &ndash; Viral &lt;&gt; Kinetyca, 2026-04-29, Fireflies ID 01KPTSQQTYBADSPNV8518RQK77. Attendees: David Feinman, Zach Medina, Matteo Fois, David (Kinetyca), Alejandra van Berkel."))
    story.append(B("<b>Business Dev Assessment:</b> Drive file 1BLBYQt9PA4noXmYCVxuluud-APykPFb7 (last modified 2026-04-29). Three tabs: Company, Sales, Marketing."))
    story.append(B("<b>UVP and Offer doc:</b> Drive file 1XcJIyVGAkeeg7OKEY81efbDtIVOYAiNq (last modified 2026-04-27)."))
    story.append(B("<b>2026 Brand Book:</b> referenced inside the assessment. Pull at next session."))
    story.append(B("<b>Miro board:</b> miro.com/app/board/uXjVHa0fswQ= &mdash; populated as a visual companion to this playbook."))

    story.append(H2("Open questions for Dave to resolve"))
    story.append(B("HVAC vs. law firms &mdash; assessment lists HVAC #3, brand book lists law firms instead, call summary says &lsquo;avoid law firms.&rsquo; Pick one."))
    story.append(B("Outcome metrics per vertical &mdash; pull 2&ndash;3 named outcomes per priority vertical for cold email proof points."))
    story.append(B("First-meeting-to-client conversion rate &mdash; confirm the actual rate over the most recent 90-day window."))
    story.append(B("Are SaaS/B2B and pro services in scope for the first 90 days, or is healthcare exclusive?"))
    story.append(B("Pricing transparency &mdash; comfortable putting $1,500&ndash;$5,000/mo in cold body copy?"))

    story.append(H2("Source-priority hierarchy applied"))
    story.append(P("Where sources diverged, this playbook follows the priority order: <b>(1) call transcript &gt; (2) UVP and assessment docs &gt; (3) brand book &gt; (4) AI inference</b>. Two known divergences are recorded above (HVAC vs law firms; law-firm scope). Both flagged for Dave."))

    doc.build(story, onFirstPage=cover_only, onLaterPages=page_footer)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()
