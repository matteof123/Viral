#!/usr/bin/env python3
"""
Viral Ideas Marketing — GTM Playbook v2.

Source-priority hierarchy applied:
  (1) Onboarding call transcript, 2026-04-29 — call narrowed scope to 3 verticals
  (2) UVP and Offer doc
  (3) Business Dev Assessment spreadsheet (where it agrees with the call)

Vertical priority on the call (Dave's words):
  "1, 2, 3 is healthcare, marketing agencies, financial fintech type clients."
  Law firms dropped (legal risk + hard close). SaaS broadly de-prioritized.
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

def page_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawString(0.9*inch, 0.45*inch, f"Viral Ideas Marketing  |  GTM Playbook v2  |  {date.today().isoformat()}")
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
    canvas.drawCentredString(LETTER[0]/2, 1.7*inch, f"Generated {date.today().isoformat()} — v2 (post-call)")
    canvas.drawCentredString(LETTER[0]/2, 1.45*inch, "Prepared by Outreach Magic / Kinetyca")
    canvas.drawCentredString(LETTER[0]/2, 1.20*inch, "CONFIDENTIAL — Internal Use Only")
    canvas.restoreState()

def build():
    doc = SimpleDocTemplate(OUT, pagesize=LETTER,
                            leftMargin=0.9*inch, rightMargin=0.9*inch,
                            topMargin=0.9*inch, bottomMargin=0.8*inch,
                            title="Viral Ideas — GTM Playbook v2")
    story = []
    story.append(PageBreak())  # cover handled by canvas

    # ---------- TOC ----------
    story.append(H("Table of Contents"))
    toc = [
        ("1. Client Overview", "page 3"),
        ("2. UVP &amp; Positioning", "page 4"),
        ("3. Social Proof &amp; Case Studies", "page 5"),
        ("4. Target Verticals — Ranked", "page 6"),
        ("5. Personas (per vertical)", "page 9"),
        ("6. Pain-to-Value Mapping", "page 11"),
        ("7. Signals, Triggers &amp; Timing", "page 12"),
        ("8. Cold Email Messaging Angles", "page 13"),
        ("9. Sales Process &amp; Conversion", "page 15"),
        ("10. Tech Stack &amp; Infrastructure", "page 16"),
        ("11. Goals, Metrics &amp; Phase Plan", "page 17"),
        ("12. Out-of-Scope &amp; Open Questions", "page 18"),
        ("Appendix — Sources, Conflicts Resolved", "page 19"),
    ]
    for t, p in toc:
        story.append(P(f"<b>{t}</b> &nbsp;&nbsp; <i>{p}</i>"))
    story.append(PageBreak())

    # ---------- 1. Overview ----------
    story.append(H("1. Client Overview"))
    story.append(P("<b>Viral Ideas Marketing</b> is a video content engine for marketing teams that need high-performing video at scale, without freelancer chaos or in-house overhead. Founded 2015. 83-person fully-remote production team. 100,000+ videos edited. Past clients include McKesson, P&amp;G, Self Financial, eBay, Sotheby's, Janssen, Johnson &amp; Johnson, and Chevrolet."))

    story.append(H2("Snapshot"))
    snap = [
        ["Field", "Detail"],
        ["Website", "viralideamarketing.com"],
        ["Founded", "2015"],
        ["Team", "83 FTE, fully remote"],
        ["Track record", "100,000+ videos edited"],
        ["Revenue last year", "$1.2M"],
        ["Revenue pacing", "$2.4M"],
        ["12-month goal", "$5M ARR"],
        ["24-month goal", "$10M ARR"],
        ["Average deal size", "$1,500&ndash;$5,000/mo retainer"],
        ["LTV", "~$12K"],
        ["Sales cycle", "~20 days first touch to close"],
        ["First-meeting close rate", "~20% (target 30%+)"],
        ["Target CAC", "$400 (currently $800&ndash;$1,000)"],
        ["Geography", "US first, Canada second (no international)"],
        ["Lead volume target", "175&ndash;200 appointments/month"],
    ]
    story.append(make_table(snap, [1.7*inch, 5.0*inch]))

    story.append(H2("What Viral sells"))
    story.append(B("<b>Content Engine</b> &mdash; ongoing retainer at 10, 20 or 40 editing hours per week. Roughly 50% of revenue."))
    story.append(B("<b>Project work</b> &mdash; one-off campaigns, content libraries, repurposing, event recaps. The other ~50% (Dave: <i>&ldquo;I wish they would all be subscriptions, but they're not&rdquo;</i>)."))
    story.append(B("<b>Limited remote / virtual production</b> &mdash; small slice when fresh footage is needed."))
    story.append(B("<b>Free lead magnet</b> &mdash; Video Grader at <a href='https://video-grader.viralideamarketing.com'>video-grader.viralideamarketing.com</a> + 15-minute strategist walkthrough."))
    story.append(P("Land-and-expand is the documented motion. Recent examples from the call: 2 projects at $800 → $2,500/mo retainer. $100 starter project → largest client. Project-based clients also stay sticky as ongoing project relationships even when they don't convert to retainers."))

    story.append(H2("Three problems Viral solves (Dave's framing)"))
    story.append(B("<b>1. Creative velocity bottleneck.</b> Lots of footage, can't get it edited fast enough."))
    story.append(B("<b>2. Don't know what to make.</b> Lost in the AI sauce. Need a partner to figure out the creative direction."))
    story.append(B("<b>3. In-house team strained.</b> Marketing department of 1&ndash;2 people; need to strategically outsource one function."))

    story.append(H2("Sales org"))
    org = [
        ["Role", "Person", "Function"],
        ["CEO + S&M Director", "Dave Feinman", "Owner, dual-seat until lead flow stabilizes"],
        ["Head of Marketing", "Alejandra van Berkel", "Brand + content; managing 2 video editors"],
        ["Closer", "Ryder", "New business, ~20% close rate today"],
        ["Account Manager", "Jess", "Existing accounts, expansion + renewal"],
        ["Account Manager", "Lui", "Existing accounts, expansion + renewal, onboarding handoff"],
        ["Appointment Setter", "Alina", "Reply triage, Dan-Martell sell-by-chat"],
    ]
    story.append(make_table(org, [1.6*inch, 1.4*inch, 3.7*inch]))
    story.append(PageBreak())

    # ---------- 2. UVP ----------
    story.append(H("2. UVP &amp; Positioning"))
    story.append(P("<b>Primary UVP:</b> &ldquo;We build the content engine that lets marketing teams ship high-performing video at scale, without freelancer chaos or in-house overhead.&rdquo;"))
    story.append(P("<b>Secondary UVP:</b> &ldquo;A reliable, scalable system to never stop producing videos that drive ROI.&rdquo;"))
    story.append(P("<b>The real product is career insurance.</b> Marketing leaders are not buying video. They are buying not-getting-blamed when content slips. Every messaging decision should reflect that."))

    story.append(H2("Five differentiators"))
    diffs = [
        ["Differentiator", "Why no competitor matches it"],
        ["Volume AND quality, no tradeoff",
         "Subscription editors do volume but not enterprise-grade quality. Agencies do quality but cannot ship 500 videos a month. Viral is built for both."],
        ["Strategic creative guidance, not order-taking",
         "Most editors execute briefs. Viral brings hook strategy, platform-specific expertise, and performance thinking before the edit. Doctor Frame: symptom in, diagnosis out."],
        ["Built for scale from day one",
         "Structured pods, managing editors, QA checkpoints. The system handles 5 → 500 videos a month without breaking."],
        ["System over talent",
         "Trained team, standardized processes. A single editor leaving never blows up an engagement."],
        ["Speed without sacrificing quality",
         "Same-day first drafts. Slack reply within an hour on business days. Humans + AI, with humans in control of judgment."],
    ]
    story.append(make_table(diffs, [1.9*inch, 4.8*inch]))

    story.append(H2("Three competitor categories"))
    comp = [
        ["Category", "Examples", "Where Viral wins"],
        ["Subscription editing services", "Design Pickle, BeCreatives", "B2B sophistication, strategic creative input"],
        ["Traditional video production agencies", "Generic regional shops", "Speed, predictability, built-for-volume"],
        ["Freelance editor marketplaces", "Upwork, Fiverr, individual freelancers", "Reliability; system survives any one editor leaving"],
    ]
    story.append(make_table(comp, [1.8*inch, 1.9*inch, 3.0*inch]))

    story.append(H2("Voice rules (from 2026 Brand Book)"))
    story.append(B("Calm and confident. Never urgent or hype-driven."))
    story.append(B("Direct. Lead with the point."))
    story.append(B("Specific: &ldquo;respond within one hour&rdquo; beats &ldquo;responsive.&rdquo;"))
    story.append(B("&ldquo;You&rdquo; over &ldquo;we.&rdquo; Active voice always."))
    story.append(B("Grade 8&ndash;10 reading level."))
    story.append(H3("Banned phrases"))
    story.append(P("Hype: revolutionary, game-changing, disruptive, world-class, best-in-class, cutting-edge. Aggressive: crush, dominate, 10x, skyrocket. Generic agency speak: synergy, holistic, full-funnel, leverage (verb). Vague: &ldquo;we care about your brand,&rdquo; &ldquo;authentic storytelling,&rdquo; &ldquo;elevate your brand.&rdquo; Self-important: guru, ninja, rockstar, white-glove, bespoke."))
    story.append(PageBreak())

    # ---------- 3. Social proof ----------
    story.append(H("3. Social Proof &amp; Case Studies"))
    story.append(P("Viral has the strongest case study library in healthcare and a deep enterprise consumer track record. Anchors below mapped to the three priority verticals plus enterprise-wide credibility."))

    proof = [
        ["Vertical", "Anchor proof"],
        ["#1 Healthcare / Pharma",
         "McKesson (Ontada subsidiary), Janssen, Johnson &amp; Johnson, Cortechs.ai (imaging), Liberty Urgent Care, Ultrasound.ai, SI Bone (med device), Inbody (med device, training &amp; development team)"],
        ["#2 Marketing &amp; PR Agencies",
         "Clever Digital Marketing (Canada, ~$10M, ~80 FTE, performance &mdash; largest customer), Pareto Legal (PPC), B Marketing"],
        ["#3 Financial / Fintech",
         "Self Financial ($100M+), Asset Map (financial advisor SaaS, client since 2017), Insight Cloud, Gainbridge (Group 1001 ~$160B AUM)"],
        ["Enterprise consumer (cross-vertical credibility)",
         "eBay, Procter &amp; Gamble, Sotheby's, Chevrolet, Logitech"],
    ]
    story.append(make_table(proof, [1.9*inch, 4.8*inch]))

    story.append(H2("Voice-of-customer quotes"))
    for q in [
        "I've been through so many editors. Will be back.",
        "Working with David and his team was effortless and great. The communication and end product were sublime.",
        "Your people are Johnny on the spot. I send a message, I get a message back in an hour.",
        "I sent them a brief and got back exactly what I wanted.",
        "I could describe the vision, but they were the ones who operationalized it and executed it beautifully.",
        "Their pricing was fair, their timelines were reliable, and above all, I felt like I could genuinely trust them.",
    ]:
        story.append(Q(q))
    story.append(P("<b>Pattern:</b> clients praise the experience, communication, and reliability — not the editing itself. That is the real product. Outbound should reflect it."))
    story.append(P("<b>Gap to close before campaign 1:</b> 2&ndash;3 specific outcome metrics per priority vertical (e.g., &ldquo;produced X edits/month for Y,&rdquo; &ldquo;cut turnaround from Z days to A days&rdquo;). Action item assigned to Dave on the call."))
    story.append(PageBreak())

    # ---------- 4. Target Verticals (REWRITTEN) ----------
    story.append(H("4. Target Verticals — Ranked"))
    story.append(P("<b>Source: 2026-04-29 onboarding call.</b> Dave: &ldquo;1, 2, 3 is healthcare, marketing agencies, financial fintech type clients.&rdquo; Law firms dropped from scope. SaaS and ecommerce moved to wave 2."))
    story.append(P("Order is fixed. We crush #1 first, layer in #2, then #3. We do not hedge across all three at launch &mdash; per Matteo on the call: &ldquo;We start with one, we nail that one, then we move to the others.&rdquo;"))

    # ---- Vertical 1: Healthcare ----
    story.append(H2("#1 — Healthcare &amp; Pharma  (PRIORITY)"))
    v1 = [
        ["Sub-segments (named on call)",
         "Pharma manufacturers · biotech · health tech · med device · pharma divisions of larger conglomerates · clinics · urgent care centers"],
        ["EXCLUDED",
         "<b>Hospitals</b> (Zach: &ldquo;I don't think we have hospitals&rdquo;)"],
        ["Company size",
         "$1M+ revenue minimum. No upper bound &mdash; even billion-dollar conglomerates work because we tap into smaller divisions (Dave: &ldquo;we get the scraps the larger agencies don't want&rdquo;). Headcount irrelevant."],
        ["Buyer titles",
         "VP Marketing · Sr Director of Brand · Head of Content · Brand Lead · Sr Business Director · Sr Manager Product Management · Triggered Education · Marketing/Creative/Channel Strategy · Motion Graphics &amp; Video Production Specialist · Training &amp; Development Manager (Inbody example). Below $5M revenue: Founder/Owner/CEO. Above: marketing manager / director."],
        ["NEVER target",
         "Finance, Accounting (always). Hospitals (always). McKesson- or J&amp;J-level CEOs (Dave: &ldquo;they would laugh, it would be a waste of their time&rdquo;)."],
        ["Sometimes target",
         "HR (training/dev content), C-suite (only at sub-$5M companies)"],
        ["Pain point",
         "Med-legal-regulatory review eats velocity. In-house teams cannot keep up with HCP and patient content volume. Missing a deadline before a product launch is a career-risk event."],
        ["Anchor proof to cite",
         "McKesson (Ontada), Janssen, J&amp;J, Cortechs.ai (imaging), Liberty Urgent Care, Ultrasound.ai, SI Bone (med device), Inbody"],
        ["Why this vertical first",
         "Largest deal sizes, longest LTV, strongest case study library (the call: <i>&ldquo;the most successful long-term financial clients are healthcare clients&rdquo;</i>). Healthcare in the US has &ldquo;a lot of money.&rdquo; If outbound works in pharma in 60 days, the rest of the strategy compounds."],
        ["Channel signal source",
         "Trade shows. Healthcare buyers go to expos, congresses, NSC-style events. Cortech AI and Inbody both attend trade shows. McKesson is at a trade show right now (per call)."],
    ]
    story.append(make_table(v1, [1.7*inch, 5.0*inch], header=False))

    # ---- Vertical 2: Agencies ----
    story.append(H2("#2 — Marketing &amp; PR Agencies"))
    v2 = [
        ["Critical refinement",
         "<b>NOT full-service agencies.</b> Target agencies that <b>do one thing really well</b> and need to scale. Performance, PPC, paid social, video specialists. Zach: &ldquo;they don't just need one video, they need a thousand a week.&rdquo;"],
        ["Avoid",
         "Full-service agencies (B Marketing-style &mdash; do everything from billboards to videos). They outsource everything in fragments and rarely buy a video engine."],
        ["Why this vertical",
         "One-to-many leverage. Zach: &ldquo;you land one of those as a client, they have 5 to 500 clients of their own.&rdquo; Easiest to close (Dave). But also &ldquo;easy come, easy go&rdquo; &mdash; here one day, gone the next, so don't lead the program with them."],
        ["Company size",
         "$5M&ndash;$50M revenue. 30&ndash;150 FTE."],
        ["Buyer titles",
         "CEO · Founder · COO · Head of Production"],
        ["Champions (corp-card holders)",
         "Marketing Manager · CMO · Director of Marketing · Head of Content · Social Media Marketing Director · Social Media Manager · Brand Manager · Head of Video / Videographer (can run problems up the chain)"],
        ["The Logitech rule (Dave's words)",
         "&ldquo;Find someone with a corp card who can spend a couple thousand a month without approval. They eventually build the case to senior leadership for a vendor relationship.&rdquo;"],
        ["NEVER target",
         "Brand ambassadors (no pull, can't push up the chain). Executive Assistants (no problem to solve, no strategy)."],
        ["Pain point",
         "Editing is the chokepoint on their delivery. They need a partner that disappears behind their brand. One bad video at the wrong moment can cost a contract worth 10x what they pay an editing partner."],
        ["Anchor proof",
         "Clever Digital Marketing (Canada, ~$10M, ~80 FTE, performance) &mdash; largest customer. Pareto Legal (PPC, performance specialty)."],
        ["Channel signal source",
         "Conferences: HubSpot Inbound. Followers of Alex Hormozi or Gary Vee."],
    ]
    story.append(make_table(v2, [1.7*inch, 5.0*inch], header=False))

    # ---- Vertical 3: Fintech ----
    story.append(H2("#3 — Financial / Fintech"))
    v3 = [
        ["Definition (precise &mdash; from call)",
         "<b>NOT banks.</b> Financial technology platforms that sell software to financial advisors / financial institutions. Zach: &ldquo;not being like a bank, but more like fintech &mdash; financial technology.&rdquo;"],
        ["Why this vertical",
         "Highly regulated industry &rarr; sticky vendors. Dave: &ldquo;they will keep you as a vendor for years and years and years.&rdquo; Asset Map has been a Viral client since 2017."],
        ["Anchor proof (named on call)",
         "Self Financial · Asset Map · Insight Cloud · Gainbridge (subsidiary of Group 1001, ~$160B AUM)"],
        ["Company size",
         "$5M&ndash;$50M revenue typical. Growth-stage."],
        ["Buyer titles",
         "Growth Marketer · Head of Marketing · Content Lead · Founder/CEO. Below $5M: Founder/CEO."],
        ["Pain point",
         "Quarterly roadmap shifts content needs weekly. Need to fuel paid ads, organic, and investor-facing brand simultaneously. Cannot scale by hiring."],
        ["Position",
         "Wave 3. Slow first sale, but 8+ year LTV when landed (Asset Map = since 2017). Best for the second sprint once healthcare and agencies are producing predictable lead flow."],
    ]
    story.append(make_table(v3, [1.7*inch, 5.0*inch], header=False))

    # ---- Out of scope summary ----
    story.append(H2("Verticals dropped on the call"))
    out = [
        ["Vertical", "Reason for dropping"],
        ["Law firms",
         "Two reasons: hard close (Zach: &ldquo;really hard to ultimately close&rdquo;) and US legal risk on cold email (Zach: &ldquo;they definitely do know the law&rdquo;). Matteo: &ldquo;they're dangerous for that.&rdquo; Pareto Legal stays as a case-study reference but the vertical is out."],
        ["SaaS startups",
         "Zach: &ldquo;the new startup doing this crazy new thing &mdash; here today, gone tomorrow.&rdquo; NFT/blockchain era a cautionary tale."],
        ["SaaS broadly",
         "Matteo: &ldquo;I would keep SAS off for now.&rdquo; Too generic, weaker reply rates than the three priority verticals."],
        ["Hospitals (within healthcare)",
         "Zach: &ldquo;I don't think we have hospitals.&rdquo; Stays excluded even within #1."],
        ["Ecommerce / DTC",
         "Documented in the assessment but never raised on the call as a priority. Park as wave 2 once the top 3 produce."],
        ["HVAC / home services",
         "Listed in the assessment summary line but appears nowhere else and was not discussed on call. Treat as a typo / superseded."],
    ]
    story.append(make_table(out, [1.7*inch, 5.0*inch]))
    story.append(PageBreak())

    # ---------- 5. Personas ----------
    story.append(H("5. Personas — by priority vertical"))

    story.append(H2("Healthcare/Pharma personas"))
    h1 = [
        ["Persona", "Brittany — Sr Marketing Director at a subsidiary"],
        ["Title", "Senior Marketing Director / Director of Marketing / Senior Business Director"],
        ["Real example", "Brittany Luxon, Sr. Business Director at Ontada (McKesson subsidiary)"],
        ["Real fear", "&ldquo;McKesson doesn't blink at a $50K invoice. But if I choose the wrong partner and something goes wrong, that's my name on it.&rdquo;"],
        ["Outbound hook", "<b>Risk reduction.</b> &ldquo;We get the brief on the first try. We catch issues before they reach your desk.&rdquo;"],
    ]
    story.append(make_table(h1, [1.4*inch, 5.3*inch], header=False))
    h2 = [
        ["Persona", "Sierra — Marketing Manager at structured corporate"],
        ["Title", "Marketing Manager / Senior Marketing Manager"],
        ["Real example", "Sierra Bowman (formerly Self Financial, $100M+ rev)"],
        ["Budget", "$5K&ndash;$10K/mo without major approvals"],
        ["Real fear", "&ldquo;If this vendor makes me look bad to my leadership, I'm the one on the performance review. Not them.&rdquo;"],
        ["Outbound hook", "<b>Reliability + brand consistency.</b> &ldquo;Never wonder if your video is going to land on time again.&rdquo;"],
    ]
    story.append(make_table(h2, [1.4*inch, 5.3*inch], header=False))
    h3 = [
        ["Persona", "Training &amp; Development buyer (med device)"],
        ["Title", "Training &amp; Development Manager"],
        ["Real example", "Inbody T&amp;D Manager"],
        ["Budget", "Department training/comms budget"],
        ["Outbound hook", "<b>Volume and consistency for HCP / training content.</b> Never miss a launch milestone."],
    ]
    story.append(make_table(h3, [1.4*inch, 5.3*inch], header=False))

    story.append(H2("Marketing &amp; PR Agency personas"))
    a1 = [
        ["Persona", "Daniel — agency CEO / Head of Production"],
        ["Title", "CEO / Founder / Head of Production"],
        ["Real example", "Daniel Rahmon, CEO of Clever Digital Marketing (~$10M, ~80 FTE, performance)"],
        ["Real fear", "&ldquo;My reputation with my clients is everything. One bad video at the wrong moment can cost me a contract worth 10x what I'm paying an editing service.&rdquo;"],
        ["Outbound hook", "<b>White-label trust.</b> &ldquo;An editing partner that plugs into your team and never embarrasses you in front of a client.&rdquo;"],
    ]
    story.append(make_table(a1, [1.4*inch, 5.3*inch], header=False))
    a2 = [
        ["Persona", "Champion with corp card (the Logitech buyer)"],
        ["Title", "CMO / Director of Marketing / Marketing Manager / Head of Content / Social Media Director"],
        ["Real example", "Logitech corp-card holder paying ~$2K/mo with no approval needed; built case for senior leadership later"],
        ["Budget", "$2K&ndash;$5K/mo on a corp card with no approval ceiling"],
        ["Outbound hook", "<b>Plug in and scale.</b> &ldquo;We slot into your existing brand, no learning curve, no contract minimum.&rdquo;"],
    ]
    story.append(make_table(a2, [1.4*inch, 5.3*inch], header=False))

    story.append(H2("Fintech personas"))
    f1 = [
        ["Persona", "Adam — fintech founder, long-cycle buyer"],
        ["Title", "Founder / CEO"],
        ["Real example", "Adam Holt, Founder of Asset Map (Viral client since 2017)"],
        ["Real fear", "&ldquo;We've built a strong product and a strong reputation. I don't want the content to be the thing that makes us look smaller than we are.&rdquo;"],
        ["Outbound hook", "<b>Strategic partnership.</b> &ldquo;A team that gets B2B positioning and thinks about your growth long-term.&rdquo;"],
    ]
    story.append(make_table(f1, [1.4*inch, 5.3*inch], header=False))
    f2 = [
        ["Persona", "Lindsey — growth marketer, growth-stage fintech"],
        ["Title", "Growth Marketer / Head of Marketing / Content Lead"],
        ["Real example", "Lindsey McKone, Growth Marketer at Gainbridge (Group 1001, ~$160B AUM)"],
        ["Outbound hook", "<b>Speed + scale.</b> &ldquo;Same-day first drafts. Scale up volume the moment a campaign is working.&rdquo;"],
    ]
    story.append(make_table(f2, [1.4*inch, 5.3*inch], header=False))
    story.append(PageBreak())

    # ---------- 6. Pain to value ----------
    story.append(H("6. Pain-to-Value Mapping"))
    pv = [
        ["Pain", "Value (Viral solution)", "Outcome"],
        ["<b>Production output is unreliable.</b> Freelancers ghost. Agency takes 2 weeks per video. In-house editor leaves and the team starts over.",
         "Dedicated editors in a structured pod. Same-day first drafts. Slack reply within 1 hour business days. The system survives any one editor leaving.",
         "Predictable monthly throughput. Marketing manager stops chasing vendors."],
        ["<b>Volume and quality cannot coexist.</b> One great video from an agency or 50 mediocre from a low-cost platform. Never 50 great videos consistently.",
         "Structured pods, managing editors, QA checkpoints. Volume ramps from 5 → 500 without breaking.",
         "Enterprise-grade quality at startup-grade speed and volume."],
        ["<b>Marketing leaders carry personal career risk.</b> When content slips, leadership blames the manager who chose the vendor. Buyers are buying career insurance, not video.",
         "Vetted enterprise track record (J&amp;J, McKesson, eBay). QA built in. Named editor + managing editor on every account. Brief-on-the-first-try workflow.",
         "Marketing manager keeps their job. No surprise misses before exec review."],
        ["<b>Quarterly KPIs miss when production falls apart.</b> Wasted ad spend, inconsistent brand presence, marketing team managing 5 vendors instead of doing strategy.",
         "One partner instead of five vendors. Platform-specific cuts produced in parallel. Performance feedback loop on which hooks land.",
         "Hit ad-creative refresh cadence. Reclaim 8&ndash;12 hours a week of vendor management."],
        ["<b>Status quo costs more than they realize.</b> Freelancer at $30/hr is $0 when they ghost, $5K in damage when launch slips. In-house: $80&ndash;$120K loaded for one editor.",
         "Production system at $1,500&ndash;$5,000/mo for a whole pod. No hiring overhead, no PTO gaps, no single point of failure.",
         "Replace one in-house editor with a full pod for less than the salary cost."],
    ]
    story.append(make_table(pv, [2.4*inch, 2.4*inch, 1.9*inch]))
    story.append(PageBreak())

    # ---------- 7. Signals ----------
    story.append(H("7. Signals, Triggers &amp; Timing"))
    story.append(P("&ldquo;The list is the message.&rdquo; Signals win the open. Below are the triggers Viral has actually closed against, plus call-confirmed event sources."))

    story.append(H2("Hiring signals (strongest single category)"))
    story.append(B("New CMO, VP Marketing, or Head of Content (90-day window) &mdash; incoming leaders reset the content stack."))
    story.append(B("Open role: Video Editor, Content Producer, Social Media Manager &mdash; production bottleneck already admitted."))
    story.append(B("Open role: Paid Social Manager / Performance Marketer &mdash; paid social runs on creative volume."))
    story.append(B("Open role: Freelance / Contract Video Editor &mdash; active confession of an unsolved gap."))
    story.append(B("Healthcare-specific: Training &amp; Development Manager hire (Inbody pattern)."))

    story.append(H2("Funding &amp; growth signals"))
    story.append(B("Series A&ndash;C funding round (last 90 days) &mdash; budget unlocked."))
    story.append(B("Headcount or revenue growth (Crunchbase, LinkedIn) &mdash; marketing always lags ops."))
    story.append(B("M&amp;A or geographic expansion &mdash; multi-region content variants needed."))

    story.append(H2("Product &amp; content signals"))
    story.append(B("New product launch &mdash; demo videos, sales enablement, ad creative needed in weeks."))
    story.append(B("New podcast / webinar series / YouTube channel &mdash; long-form raw material we repurpose."))
    story.append(B("Increased ad spend on Meta or LinkedIn (visible in ad libraries) &mdash; running through creative faster than they can produce."))

    story.append(H2("Vertical-specific signals (call-confirmed)"))
    story.append(B("<b>Healthcare:</b> FDA approval, clinical trial milestone, new indication launch, partnership with HCP networks. <b>Trade shows:</b> NSC, BIO International, MM+M Awards, healthcare expos. McKesson currently at a trade show; Cortech AI and Inbody attend regularly."))
    story.append(B("<b>Agencies:</b> Announced new client win (especially video-heavy). New office or service line. <b>Conferences:</b> HubSpot Inbound. <b>Influencer signal:</b> followers of Alex Hormozi or Gary Vee."))
    story.append(B("<b>Fintech:</b> New regulation cycle (advisor compliance updates). New product release (web-based platform, app). Funding round."))

    story.append(H2("Negative signals — do NOT contact"))
    story.append(B("Hospitals (excluded inside healthcare)."))
    story.append(B("DIY creators just starting out (no content pipeline)."))
    story.append(B("Budget negotiators benchmarking against $5/hr Fiverr."))
    story.append(B("Wedding videographers, music videos, bar/bat mitzvah, hype-driven startup-bro founders, political campaigns, gambling."))
    story.append(B("Micromanagers (need to approve every 10-second cut)."))
    story.append(B("Full-service agencies (Daniel-pattern is specialty; B Marketing-pattern is not the buyer)."))
    story.append(B("Brand ambassadors, executive assistants &mdash; no pull, no problem to solve."))
    story.append(B("Finance and accounting roles &mdash; never the buyer."))
    story.append(PageBreak())

    # ---------- 8. Cold email angles ----------
    story.append(H("8. Cold Email Messaging Angles — by vertical, in order"))
    story.append(P("Every email passes voice rules. Subject lines lowercase, max 3 words, person/company names capitalized."))

    story.append(H2("#1 Healthcare / Pharma"))
    story.append(B("<b>Persona:</b> Brittany (Sr Director at subsidiary) and Sierra (Marketing Manager)."))
    story.append(B("<b>Hook:</b> med-legal review eats velocity; in-house can't keep up with HCP and patient content; missing a launch deadline is career-risk."))
    story.append(B("<b>Value lead:</b> &ldquo;We get the brief on the first try. We catch issues before they reach your desk.&rdquo;"))
    story.append(B("<b>Proof to cite:</b> J&amp;J, McKesson (Ontada), Janssen, Cortechs.ai, Inbody."))
    story.append(B("<b>Subject direction:</b> <i>content engine</i> · <i>video pipeline</i> · <i>review cycles</i>"))
    story.append(B("<b>Trigger overlay:</b> trade show attendance / clinical trial milestone / new indication."))

    story.append(H2("#2 Marketing &amp; PR Agencies"))
    story.append(B("<b>Persona:</b> Daniel (specialty agency CEO) + the Logitech-style corp-card holder."))
    story.append(B("<b>Hook:</b> editing chokepoint hurts client delivery; one bad video costs a contract worth 10x what you pay an editing partner."))
    story.append(B("<b>Value lead:</b> &ldquo;An editing partner that plugs into your team and never embarrasses you in front of a client.&rdquo;"))
    story.append(B("<b>Proof to cite:</b> Clever Digital Marketing (Canada, ~$10M, performance &mdash; largest customer)."))
    story.append(B("<b>Subject direction:</b> <i>white label</i> · <i>delivery layer</i> · <i>client safety</i>"))
    story.append(B("<b>Trigger overlay:</b> agency announced a new video-heavy client win in last 30 days."))

    story.append(H2("#3 Financial / Fintech"))
    story.append(B("<b>Persona:</b> Adam (founder, long-cycle) + Lindsey (growth marketer at scale-stage)."))
    story.append(B("<b>Hook:</b> premium product, content doesn't match the reputation; quarterly roadmap shifts content needs weekly; can't scale by hiring."))
    story.append(B("<b>Value lead:</b> &ldquo;A team that gets B2B positioning and thinks about your growth long-term.&rdquo;"))
    story.append(B("<b>Proof to cite:</b> Self Financial ($100M+), Asset Map (since 2017), Insight Cloud, Gainbridge."))
    story.append(B("<b>Subject direction:</b> <i>content system</i> · <i>brand fit</i> · <i>positioning</i>"))
    story.append(B("<b>Trigger overlay:</b> new product release / regulator update / funding round."))

    story.append(H2("Email 1 structure (lead-magnet thread)"))
    story.append(B("<b>Hook paragraph:</b> name a vertical-specific pain in their words."))
    story.append(B("<b>Social proof paragraph:</b> drop one named logo from the same vertical."))
    story.append(B("<b>Audit offer paragraph (own paragraph):</b> Video Grader + 15-minute walkthrough."))
    story.append(B("<b>CTA paragraph:</b> one yes/no question. No double-CTA."))
    story.append(P("60&ndash;80 words. No em dashes. No exclamation marks. No spam words. No bracket placeholders. Signature handled by EmailBison's system variable."))

    story.append(H2("Email 2 (service offer thread)"))
    story.append(B("New thread, same lead, ~7 days later. Pivot from audit to retainer."))
    story.append(B("Hook: name the symptom they probably have (e.g., &lsquo;creative refresh slipping into next sprint&rsquo;)."))
    story.append(B("Body: production-engine reframe (system over talent)."))
    story.append(B("CTA: 15-minute call to walk through how a pod plugs into their existing setup."))

    story.append(H2("Lead magnet rules (call-decided)"))
    story.append(B("<b>Use:</b> Video Grader at video-grader.viralideamarketing.com + 15-minute strategist walkthrough. Zach's reverse use case: <i>upload competitor's video, see why theirs performs better</i> &mdash; A/B test against the standard prompt."))
    story.append(B("<b>Avoid:</b> Ebooks. Matteo on call: &ldquo;Ebooks is not something that I would try.&rdquo;"))
    story.append(B("<b>Possible alt to test:</b> photo-to-video repurposing pack (parallel to the BigVu listing-to-video that worked for real estate). For healthcare, e.g., &lsquo;new facility photo set → video.&rsquo;"))
    story.append(PageBreak())

    # ---------- 9. Sales process ----------
    story.append(H("9. Sales Process &amp; Conversion"))
    sp = [
        ["Stage", "Owner", "Goal"],
        ["Lead reply", "Alina (sell-by-chat / Dan Martell)", "Qualify reply, book Ryder"],
        ["Discovery + demo", "Ryder (90% of new business) or Dave", "Doctor Frame: pain in, prescription out"],
        ["Proposal + close", "Ryder", "Standardized template, pain-first then pricing"],
        ["Onboarding handoff", "Lui or Jess", "First deliverable inside 7 days, brand kit captured"],
        ["Expansion", "Lui / Jess", "Pitch volume increase at month 3 and month 6"],
    ]
    story.append(make_table(sp, [1.3*inch, 2.4*inch, 3.0*inch]))

    story.append(H2("Top 3 objections (rehearse responses)"))
    story.append(B("<b>&ldquo;We already have freelancers / in-house editor.&rdquo;</b> &mdash; Reframe as relief valve, not replacement: &ldquo;Keep your in-house editor for the strategic stuff. Use us for the volume that's drowning them.&rdquo;"))
    story.append(B("<b>&ldquo;Your pricing seems high for editing.&rdquo;</b> &mdash; Reframe against total cost. Freelancer at $30/hr = $0 when they ghost, $5K when launch slips. In-house = $80&ndash;$120K loaded. Viral = $1,500&ndash;$5,000/mo for a whole production system."))
    story.append(B("<b>&ldquo;How do we know quality will be consistent?&rdquo;</b> &mdash; Show the system: QA checkpoints, managing editor structure, vertical case studies. Offer paid trial / no-risk first edit. Drop named logos in their environment."))

    story.append(H2("CRM &amp; reporting"))
    story.append(B("CRM: GoHighLevel (just migrated from HubSpot this week)."))
    story.append(B("Outbound source: EmailBison. Replies route to Alina."))
    story.append(B("Cadence: monthly working session with Outreach Magic. Quarterly L10 review feeds reply intelligence into copy, paid ads, and organic content."))
    story.append(PageBreak())

    # ---------- 10. Tech stack ----------
    story.append(H("10. Tech Stack &amp; Outreach Infrastructure"))
    om = [
        ["Tool", "Purpose", "Rule"],
        ["EmailBison", "Cold email send + sequencing", "Per-client workspace. Always create campaigns PAUSED."],
        ["Heyreach", "LinkedIn parallel touch on prioritized accounts", "2&ndash;3 LinkedIn profiles (Dave + Ale + Ryder)."],
        ["Apollo + Sales Nav", "Account list build", "Tag verticals at source; never mix with another client."],
        ["BlitzAPI", "Email finding (priority 1)", "x-api-key header; never Bearer."],
        ["Debounce", "Email validation (priority 2)", "Stop sending if no credits."],
        ["FindyMail", "Email finding (priority 3)", "Email-find only; never enrichment."],
        ["LeadMagic", "Email finding + validation (priority 4)", "Email-find only."],
        ["BounceBan", "Final bounce filter (priority 5)", "Never skip. Bounce ceiling 3%."],
        ["Supabase", "Central leads table", "Project tcyblrzlgdmffkwremqs. Client isolation every query."],
        ["Gemini 2.5 Flash", "Per-lead copy (~$2&ndash;3 per 400 leads)", "Never Claude for bulk copy."],
        ["Validator", "validate_variables.py pre-flight", "Hard-fail brackets, empty PS_LINE, spam words, signatures."],
    ]
    story.append(make_table(om, [1.4*inch, 2.4*inch, 2.9*inch]))
    story.append(P("Viral's own stack: GoHighLevel CRM (migrated from HubSpot), ClickUp project management, Video Grader at video-grader.viralideamarketing.com (built in-house). Cold email tested historically on Instantly with minimal results &mdash; replaced by EmailBison."))
    story.append(PageBreak())

    # ---------- 11. Goals ----------
    story.append(H("11. Goals, Metrics &amp; Phase Plan"))
    g = [
        ["Horizon", "Target"],
        ["12-month revenue", "$5M ARR (close $2.6M gap from $2.4M pace)"],
        ["24-month revenue", "$10M ARR"],
        ["Outbound appointments / month", "175&ndash;200 (current ~3 calls/day, capacity ~12/day)"],
        ["Sales utilization", "Fill the 75% capacity gap"],
        ["Target CAC", "$400 (currently ~$800&ndash;$1,000)"],
        ["First-meeting close rate", "30%+ (currently ~20%)"],
        ["Bounce-rate ceiling", "&lt;3% on every send"],
    ]
    story.append(make_table(g, [2.4*inch, 4.3*inch]))

    story.append(H2("First-90-day phase plan (vertical-ordered)"))
    phases = [
        ("Weeks 1–2 — foundation",
         "GTM playbook complete. EmailBison workspace provisioned. Sending domains warmed (Zapmail). Healthcare list built (~2,500 contacts). Outcome metrics per vertical pulled from Dave."),
        ("Weeks 3–4 — campaign 1: HEALTHCARE",
         "Healthcare/pharma in test batch (50 leads). Copy approved by Dave. Iterate on subject + Email 1 hook. Reply intelligence loop with Alina starts."),
        ("Weeks 5–6 — campaign 2: AGENCIES",
         "Specialty-agency campaign live (performance / PPC / paid social). Reuse healthcare hooks where they map; Email 1 rewritten for white-label-trust angle. Daniel persona is the headline."),
        ("Weeks 7–8 — scale healthcare",
         "Healthcare moves to full volume after iteration. Begin signal-based campaigns (new-CMO, hiring-video-editor, trade-show attendance)."),
        ("Weeks 9–12 — campaign 3: FINTECH",
         "Fintech campaign live (Self Financial / Asset Map / Insight Cloud anchors). All three priority verticals running. First L10 review feeds reply intelligence into messaging, paid ads, organic."),
    ]
    for n, body in phases:
        story.append(H3(n))
        story.append(P(body))

    story.append(H2("Reporting cadence"))
    story.append(B("Weekly: per-vertical reply rate, positive replies, bounces, meetings booked."))
    story.append(B("Monthly: working session with Dave + Ale &mdash; reply intelligence into messaging, paid ads, organic."))
    story.append(B("Quarterly: L10 review &mdash; intelligence flows into the broader marketing function (BBM paid ads, LinkedIn organic, sales enablement)."))
    story.append(PageBreak())

    # ---------- 12. Out-of-scope ----------
    story.append(H("12. Out-of-Scope &amp; Open Questions"))
    story.append(P("Recorded here so nothing slips between sessions."))
    story.append(H2("Out of scope (call-decided)"))
    story.append(B("Law firms (legal risk + hard close)."))
    story.append(B("SaaS startups (here-today-gone-tomorrow risk)."))
    story.append(B("SaaS broadly (Matteo: &ldquo;keep SAS off for now&rdquo;)."))
    story.append(B("Hospitals (within healthcare)."))
    story.append(B("Ecommerce / DTC (park as wave 2)."))
    story.append(B("HVAC / home services (assessment typo, not a real vertical)."))
    story.append(B("Brand ambassadors, executive assistants, finance, accounting (titles)."))
    story.append(B("McKesson- or J&amp;J-level CEOs (out of reach + irrelevant to them)."))

    story.append(H2("Open questions for Dave"))
    story.append(B("2&ndash;3 outcome metrics per priority vertical (campaign-1 proof points)."))
    story.append(B("Pricing transparency in cold body copy &mdash; comfortable with $1,500&ndash;$5,000/mo published, or price-discovery on first call?"))
    story.append(B("Healthcare sub-segment ranking: pharma vs biotech vs med device vs health tech &mdash; which sub-segment first?"))
    story.append(B("Confirmed list of in-scope agency archetypes (performance, PPC, paid social, video specialty) &mdash; any others to add?"))
    story.append(B("Fintech timing &mdash; week 5 or week 9?"))
    story.append(PageBreak())

    # ---------- Appendix ----------
    story.append(H("Appendix"))
    story.append(H2("Sources used (priority order)"))
    story.append(B("<b>(1) Onboarding call</b> &mdash; Onboarding &mdash; Viral &lt;&gt; Kinetyca, 2026-04-29, Fireflies ID 01KPTSQQTYBADSPNV8518RQK77. Attendees: Dave Feinman, Zach Medina, Matteo Fois, David (Kinetyca), Alejandra van Berkel."))
    story.append(B("<b>(2) UVP and Offer doc</b> &mdash; Drive file 1XcJIyVGAkeeg7OKEY81efbDtIVOYAiNq (last modified 2026-04-27)."))
    story.append(B("<b>(3) Business Dev Assessment</b> &mdash; Drive file 1BLBYQt9PA4noXmYCVxuluud-APykPFb7 (last modified 2026-04-29). Three tabs."))
    story.append(B("<b>(4) Email infra setup sheet</b> &mdash; Drive file 1AaOctzNY1t-QlWbG8SEvNHVA1oCZTU27."))
    story.append(B("<b>(5) Prospecting Hub copy testing sheet</b> &mdash; Drive file 133LsUxFmYlCsHTncjhjgvyONaLlh2NzP."))
    story.append(B("<b>(6) Kinetyca Winning Copy library</b> &mdash; Drive file 1i5Qqt3pCCkmnGCX626UvIrUrURA9MDg0."))
    story.append(B("<b>(7) 2026 Brand Book</b> &mdash; referenced inside the assessment, pull at next session."))
    story.append(B("<b>(8) Miro board</b> &mdash; miro.com/app/board/uXjVHa0fswQ=."))

    story.append(H2("Conflicts the call resolved"))
    story.append(B("<b>Vertical order:</b> Spreadsheet listed 6 verticals in detail. Call narrowed to 3 (healthcare, agencies, fintech) and explicitly dropped law firms + SaaS. Call wins."))
    story.append(B("<b>HVAC:</b> Spreadsheet summary line listed it; nowhere else. Treat as superseded."))
    story.append(B("<b>Law firms:</b> Spreadsheet had as #4. Call dropped (legal risk on cold email + hard close). Call wins."))
    story.append(B("<b>Hospitals:</b> Not specifically excluded in spreadsheet. Call: Zach &ldquo;I don't think we have hospitals.&rdquo; Add to negative-signals list."))
    story.append(B("<b>Agency definition:</b> Spreadsheet said mid-to-large agencies broadly. Call refined to specialty agencies that &ldquo;do one thing really well.&rdquo; Use the call's definition."))
    story.append(B("<b>Fintech:</b> Spreadsheet folded into &ldquo;SaaS / B2B&rdquo; and &ldquo;Professional services.&rdquo; Call elevated fintech to its own #3 priority. Use call."))

    doc.build(story, onFirstPage=cover_only, onLaterPages=page_footer)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()
