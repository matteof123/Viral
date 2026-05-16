#!/usr/bin/env python3
"""
Viral Ideas Marketing — Triggers & Email Templates PDF generator.

v2: Incorporates Discovery Questionnaire — two-funnel split, funnel-matched
case studies, VOC pain language, real differentiators, 6 rendered examples.

Brand-matched to the GTM playbook (NAVY + ACCENT).
"""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from datetime import date

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(OUT_DIR, "Viral_Triggers_and_Email_Templates.pdf")

NAVY = colors.HexColor("#0E2A47")
ACCENT = colors.HexColor("#C8362F")
LIGHT = colors.HexColor("#F4F6F9")
TEXT_GRAY = colors.HexColor("#3A3A3A")
CODE_BG = colors.HexColor("#F7F7F2")
CODE_BORDER = colors.HexColor("#DDDDDD")

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
styles.add(ParagraphStyle("CodeBlock", parent=styles["Normal"], fontName="Courier",
                          fontSize=8.5, textColor=NAVY, leading=11.5,
                          leftIndent=10, rightIndent=10, spaceBefore=6, spaceAfter=6,
                          backColor=CODE_BG, borderColor=CODE_BORDER, borderWidth=0.5,
                          borderPadding=8, alignment=TA_LEFT))
styles.add(ParagraphStyle("Caption", parent=styles["Body"], fontSize=8.5,
                          textColor=colors.HexColor("#888888"), alignment=TA_LEFT, spaceAfter=4,
                          fontName="Helvetica-Oblique"))

def H(s): return Paragraph(s, styles["H1"])
def H2(s): return Paragraph(s, styles["H2"])
def H3(s): return Paragraph(s, styles["H3"])
def P(s): return Paragraph(s, styles["Body"])
def B(s): return Paragraph(f"&bull;&nbsp; {s}", styles["BulletLine"])
def C(s): return Paragraph(s.replace("\n", "<br/>").replace(" ", "&nbsp;"), styles["CodeBlock"])
def CAP(s): return Paragraph(s, styles["Caption"])

def cell(s, head=False):
    style = styles["CellHead"] if head else styles["CellBody"]
    return Paragraph(str(s), style)

def page_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawString(0.9*inch, 0.45*inch, f"Viral Ideas Marketing  |  Triggers & Email Templates v2  |  {date.today().isoformat()}")
    canvas.drawRightString(7.6*inch, 0.45*inch, f"Page {doc.page}")
    canvas.restoreState()

def cover_only(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, LETTER[1]-1.4*inch, LETTER[0], 0.18*inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 30)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-3.6*inch, "Triggers & Email Templates")
    canvas.setFillColor(ACCENT)
    canvas.setFont("Helvetica-Bold", 22)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-4.3*inch, "Viral Ideas Marketing")
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 12)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-5.0*inch,
                             "Two-funnel signal taxonomy + Email 1 / Email 2 system")
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-5.3*inch,
                             "v2 — rebuilt against Discovery Questionnaire (May 2026)")
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
                            title="Viral Ideas — Triggers & Email Templates v2")
    story = []

    # Cover
    story.append(PageBreak())

    # ---- What This Is ----
    story.append(H("What This Is"))
    story.append(P("The complete signal taxonomy and email template system for Viral Ideas Marketing outbound, rebuilt against the Discovery Questionnaire (May 2026). Structure modeled on BIGVU's Campaign 198 (2.0% reply rate, 40 interested across 25K sends)."))
    story.append(P("Two parallel funnels run different copy with different case studies and different pain language:"))
    story.append(B("<b>Funnel A &mdash; Half-Time tier</b> &mdash; mid-market marketing managers (Sierra) + growth marketers at funded startups (Lindsey)"))
    story.append(B("<b>Funnel B &mdash; Full-Time tier</b> &mdash; agency owners and CEOs (Daniel), white-label friendly"))
    story.append(P("Enterprise pharma marketing directors (Brittany) and B2B founders (Adam) are opportunistic plays, not the main paid spend. They get their own light track."))

    # ---- Two Funnels ----
    story.append(H("The Two Funnels"))
    funnel_rows = [
        ["Field", "Funnel A", "Funnel B"],
        ["<b>Tier</b>", "Half-Time", "Full-Time"],
        ["<b>Buyer archetype</b>",
         "Sierra (mid-market marketing manager) + Lindsey (growth marketer at funded startup)",
         "Daniel (agency CEO/Founder, 30-150 staff)"],
        ["<b>Buyer revenue band</b>",
         "$50M-$500M B2C/B2B (Sierra) · $5M-$50M startup (Lindsey)",
         "$5M-$50M agency"],
        ["<b>Volume promise</b>",
         "8-20 videos/month, first drafts in 24 hours",
         "30+ videos/month, same-day first drafts, white-label"],
        ["<b>Trigger words</b>",
         "\"ghosted,\" \"fire drill,\" \"drowning,\" \"we keep starting over,\" \"I need a real team, not a freelancer\"",
         "\"white-label,\" \"dedicated editor,\" \"the client noticed,\" \"we need someone who can ramp without us teaching them everything\""],
        ["<b>Case study</b>",
         "Self Financial (marketing mgrs) · Gainbridge (growth marketers)",
         "Clever Digital Marketing"],
        ["<b>Hook angle</b>",
         "Save your week. Stop being the bottleneck. CMO stops asking about video.",
         "Margin recovery. Renewal protection. Client never knows we exist."],
    ]
    story.append(make_table(funnel_rows, [1.4*inch, 2.6*inch, 2.7*inch]))

    story.append(H2("Opportunistic tracks (not main spend)"))
    opp_rows = [
        ["Archetype", "Real example", "Case study", "Hook angle"],
        ["<b>Brittany</b> &mdash; enterprise pharma mkt director", "Ontada (McKesson subsidiary)",
         "Ontada / Janssen / J&amp;J",
         "\"Approval friendly, on-brand at scale, no surprises in front of leadership\""],
        ["<b>Adam</b> &mdash; B2B founder, pro services/SaaS", "Asset Map (VI client since 2017)",
         "Asset Map",
         "\"Strategic partner, not just an editor. Built for compounding LTV.\""],
    ]
    story.append(make_table(opp_rows, [1.7*inch, 1.6*inch, 1.4*inch, 2.0*inch]))

    story.append(PageBreak())

    # ---- Signal Mix ----
    story.append(H("Signal Mix"))
    story.append(P("The signal-finding logic runs in two prompts. Both apply to both funnels &mdash; the SIGNAL is the same, but the CASE STUDY and PAIN LANGUAGE swap based on which funnel the prospect maps to."))

    story.append(H2("Prompt A &mdash; Pharma-specific signals"))
    story.append(P("Run first when the lead is in pharma, biotech, healthcare, or med device. Stop at first match. If no signal found, fall through to Prompt B."))
    rows_a = [
        ["#", "Signal", "Recency"],
        ["A1", "<b>FDA approval / new indication / new device approval</b>", "last 90 days"],
        ["A2", "<b>Clinical trial milestone / Phase III readout / endpoint announcement</b>", "last 90 days"],
        ["A3", "<b>Upcoming medical congress with accepted abstract</b> (ASH, ASCO, AHA, ESMO, AAD, ACR, AAOS, BIO, JPM)", "next 60 days"],
        ["A4", "<b>Currently using named pharma video agency</b> (Klick, Razorfish Health, Ogilvy Health, EVERSANA, Greater Than One, Real Chemistry, FCB Health, McCann Health)", "last 12 months"],
    ]
    story.append(make_table(rows_a, [0.4*inch, 5.0*inch, 1.3*inch]))

    story.append(H2("Prompt B &mdash; Universal signals"))
    story.append(P("Run for ALL leads. Stop at first match."))
    rows_b = [
        ["#", "Signal", "Recency", "Hit rate"],
        ["B1", "<b>Open job posting for video / content / marketing production role</b>", "30d", "~15-25%"],
        ["B1.5", "<b>Freelance video editor 'open to work' who lists target company as recent client</b>", "30d", "~5-10% &mdash; direct ghosting signal (strongest Funnel A trigger)"],
        ["B2", "<b>New marketing / brand / content leader hired</b>", "90d", "~20-30%"],
        ["B3", "<b>Underutilized long-form footage on brand channel</b> (15+ min video, no &lt;2-min cuts on social)", "120d", "~50-70%"],
        ["B4", "<b>Image-heavy LinkedIn brand page</b> (&lt;3 videos in 120d)", "120d", "~60-80%"],
        ["B5", "<b>Recent company growth / expansion / new client win announcement</b>", "90d", "~25-40%"],
        ["B6", "<b>Recent funding / growth milestone</b>", "90d", "~10-25%"],
        ["B7", "<b>Agency RFP / RFQ posted for video editing</b> (Funnel B only)", "30d", "~3-5% (strongest Funnel B trigger)"],
        ["B8", "<b>Quarterly renewal-cycle boundary</b> (Funnel B only)", "calendar", "~25% of agency leads/qtr"],
        ["B9", "<b>Lead's most recent LinkedIn activity</b> (guaranteed fallback)", "30d", "~85-95%"],
    ]
    story.append(make_table(rows_b, [0.35*inch, 3.3*inch, 0.5*inch, 2.55*inch]))

    story.append(PageBreak())

    # ---- Email 1 Template ----
    story.append(H("Email 1 &mdash; Template"))
    email1_tpl = """Subject: [trigger-anchored 2-4 word lowercase subject]

Hi [First Name],

[TRIGGER -- specific observation about the prospect,
tied to the signal that fired].

[PAIN -- what specifically hurts, using VOC language
from the funnel's pain word library].

[SOLUTION -- what Viral concretely does, citing the
funnel-matched case study with full identity phrase.
Specific differentiators from the library, not generic
claims].

Worth a look for [Company]?"""
    story.append(C(email1_tpl))
    story.append(CAP("Word target: 70-100 words. No em dashes. No exclamation marks. No spam words. No bracket placeholders. No apologetic PS. No in-body taglines. NO sign-off -- email ends at the CTA. Signature handled by EmailBison {SENDER_EMAIL_SIGNATURE} system variable."))
    story.append(P("The CTA can swap depending on intent level:"))
    story.append(B("<b>Default:</b> \"Worth a look for [Company]?\""))
    story.append(B("<b>High-commitment signal</b> (FDA approval, funding round): \"Open to a 15-minute diagnostic?\" &mdash; matches VI's Doctor Frame sales method"))

    # ---- Funnel A Library ----
    story.append(H("Trigger &rarr; Pain &rarr; Solution Library &mdash; Funnel A"))
    story.append(P("<b>Buyer:</b> Sierra (mid-market marketing manager) + Lindsey (growth marketer at funded startup). <b>Case study to cite:</b> Self Financial (Sierra archetype) for marketing managers; Gainbridge (Lindsey archetype) for growth marketers."))
    funnel_a_lib = [
        ["Signal", "Subject", "Trigger", "Pain", "Solution"],
        ["<b>B1</b> Job posting", "<font face='Courier'>editor hire</font>",
         "\"Saw [Company] is hiring a Video Editor.\"",
         "\"Most of our clients came to us right after a freelancer ghosted before a launch or a quarterly review. The math on hiring full-time usually doesn't survive a slow quarter either.\"",
         "\"Self Financial runs their video through our pod. One dedicated editor brand-trained before the first project, first drafts in 24 hours, Slack response inside the hour Mon to Fri. Unlimited revisions on the first batch.\""],
        ["<b>B1.5</b> Freelancer ghosting", "<font face='Courier'>freelancer gap</font>",
         "\"Saw [Freelancer] just listed themselves as open to work after working with [Company].\"",
         "\"Almost every team that comes to us starts with a freelancer who ghosted right before a launch. The pattern is consistent enough we built the model around it.\"",
         "\"Self Financial runs their video through our pod. One dedicated editor, brand-trained before video one, first drafts in 24 hours. No ticket portal, no edit lottery.\""],
        ["<b>B2</b> New marketing leader", "<font face='Courier'>new role start</font>",
         "\"Congrats on the [Role] start at [Company].\"",
         "\"First 90 days for most marketing leaders means an audit of the content stack while the calendar keeps moving. The brief intake usually gets sloppy and video falls behind first.\"",
         "\"Self Financial runs their content through our pod for exactly this. One dedicated editor brand-trained before the first project, first drafts in 24 hours, Slack response inside the hour. The audit runs in parallel and the cadence holds.\""],
        ["<b>B3</b> Underutilized long-form", "<font face='Courier'>your [topic] interview</font>",
         "\"I saw [Company]'s recent [Topic] interview on the brand channel. [X] minutes of long-form.\"",
         "\"Most teams sit on long-form like this for weeks before short-form ships, because the freelancer rotation keeps starting over with every new brief.\"",
         "\"Self Financial runs their repurposing through our pod. One long-form becomes 5 to 10 branded short-form pieces in 5 business days. Captions, brand kit, platform-specific aspect ratios all built in.\""],
        ["<b>B6</b> Funding (growth mkter)", "<font face='Courier'>series [x] content</font>",
         "\"Congrats on [Company]'s Series [X] last month.\"",
         "\"Growth-stage rounds usually mean creative supply becomes the bottleneck. Sales enablement, paid ads, recruiting content, and investor updates all need video at once, and hiring takes too long.\"",
         "\"Gainbridge, the growth team inside Group 1001 with about 160 billion in assets under management, runs their paid-creative testing through our pod. One dedicated editor, first drafts in 24 hours, ships new ad variants twice a week.\""],
    ]
    story.append(make_table(funnel_a_lib, [0.85*inch, 1.05*inch, 1.4*inch, 1.6*inch, 1.8*inch]))

    story.append(PageBreak())

    # ---- Funnel B Library ----
    story.append(H("Trigger &rarr; Pain &rarr; Solution Library &mdash; Funnel B"))
    story.append(P("<b>Buyer:</b> Daniel (agency CEO/Founder, 30-150 staff, $5M-$50M revenue). <b>Case study to cite:</b> Clever Digital Marketing (Daniel archetype, ~$10M, ~80 staff, Canadian agency, white-label model)."))
    funnel_b_lib = [
        ["Signal", "Subject", "Trigger", "Pain", "Solution"],
        ["<b>B1</b> Agency editor hire", "<font face='Courier'>editor hire</font>",
         "\"Saw [Agency] is hiring a Senior Video Editor.\"",
         "\"Most agencies that come to us tried to hire their way out and the math broke. A full-time editor is dead weight on slow weeks, and the brand calendar doesn't pause while you ramp.\"",
         "\"Clever Digital Marketing, a Canadian agency running about 80 staff, runs our team behind their accounts white-label. Same editor every week, same-day first drafts on Full-Time, Slack response inside the hour. The cuts go out under their brand.\""],
        ["<b>B5</b> New client win", "<font face='Courier'>[client] win</font>",
         "\"Saw [Agency] just announced the [Client] win.\"",
         "\"New accounts pile onto an in-house editing team already at capacity. The existing accounts start asking pointed questions about turnaround.\"",
         "\"Clever Digital Marketing runs our team behind five of their accounts white-label. Same-day first drafts, dedicated editor per account, Slack response inside the hour. Their renewal book got cleaner. The clients never knew.\""],
        ["<b>B7</b> Agency RFP for video", "<font face='Courier'>video rfp</font>",
         "\"Saw [Agency]'s RFP for video editing partners.\"",
         "\"Most agencies post the RFP because the current vendor's quality dropped when volume scaled. The brand stopped looking like the brand and the client noticed.\"",
         "\"Clever Digital Marketing runs our team white-label behind their accounts. One dedicated editor per account, same-day first drafts on Full-Time, no rotation, no quality dip when volume spikes.\""],
        ["<b>B8</b> Q4 renewal cycle", "<font face='Courier'>renewal stack</font>",
         "\"Q4 renewal cycle approaching for [Agency].\"",
         "\"Most agencies hit the renewal cycle with one or two accounts already flagging video as a churn risk. The vendor scaled the team through a pool and the brand drifted.\"",
         "\"Clever Digital Marketing runs our team behind five of their accounts white-label. Dedicated editor per account, same-day first drafts on Full-Time, no surprises before quarterly business reviews.\""],
    ]
    story.append(make_table(funnel_b_lib, [0.85*inch, 1.05*inch, 1.4*inch, 1.6*inch, 1.8*inch]))

    # ---- Opportunistic Library ----
    story.append(H("Trigger &rarr; Pain &rarr; Solution &mdash; Opportunistic"))
    story.append(P("<b>Buyers:</b> Brittany (enterprise pharma marketing director) + Adam (B2B founder, established pro services or SaaS). <b>Case studies:</b> Ontada / Janssen / J&amp;J for pharma; Asset Map for founder-led pro services / SaaS."))
    opp_lib = [
        ["Signal", "Subject", "Trigger", "Pain", "Solution"],
        ["<b>A1</b> FDA approval (Brittany)", "<font face='Courier'>approval launch</font>",
         "\"Congrats on the FDA approval at [Company] last month.\"",
         "\"Most enterprise launches need approval-friendly volume that survives legal review on the first pass. Most vendors don't survive enterprise governance.\"",
         "\"Ontada, the McKesson healthcare-data subsidiary, runs their HCP and clinical-trial cuts through our pod. The editor learns the compliance pattern by the third project. Submissions clear legal on the first pass more often than not. A six-week cycle shrinks to two.\""],
        ["<b>A3</b> Medical congress (Brittany)", "<font face='Courier'>[conference] content</font>",
         "\"Saw [Company]'s team is presenting at [Conference] next month.\"",
         "\"Congress content has a hard deadline and three audiences: HCP attendees, KOLs, and the field team. Most brand teams over-spec the deliverable count and under-deliver on quality.\"",
         "\"Janssen runs their congress content through our pod. One editor across all three audiences, brand voice stays consistent from teaser to recap, regulatory QA baked in.\""],
        ["<b>B5</b> Founder-led growth (Adam)", "<font face='Courier'>[company] next phase</font>",
         "\"Saw [Company]'s [milestone] announcement.\"",
         "\"Founder-led marketing functions at this stage usually hit a wall where the junior marketing lead is drowning and the strategic conversations stop happening because everyone's executing.\"",
         "\"Asset Map has been a Viral client since 2017. Their marketing lead has a partner who thinks about positioning, platform strategy, and what to ship next, not just an editor who takes orders.\""],
    ]
    story.append(make_table(opp_lib, [0.95*inch, 1.05*inch, 1.4*inch, 1.5*inch, 1.8*inch]))

    story.append(PageBreak())

    # ---- Email 2 Template ----
    story.append(H("Email 2 &mdash; Template (Lead-Magnet Pivot)"))
    story.append(P("Same thread, ~3-5 days after Email 1. The broader observation in paragraph 1 pulls from the <b>5 reasons clients switch</b> (per discovery), funnel-matched to the prospect."))
    email2_tpl = """Subject: Re: [Email 1 subject]

[BROADER OBSERVATION -- funnel-matched, drawn from
the 5 switching reasons].

Viral takes any long-form video and ships 5 short-form
pieces in 5 business days. Branded, captioned,
[audience-specific qualifier].

Interested in 5 short-form cuts from one of your
existing [Company] long-forms? (on us)"""
    story.append(C(email2_tpl))
    story.append(CAP("Word target: 60-90 words"))

    story.append(H2("Broader observation library by signal type"))
    obs_rows = [
        ["Email 1 signal type", "Funnel", "Email 2 paragraph 1 observation"],
        ["Freelancer ghosting / job posting", "A",
         "\"Almost every team we work with came to us after a freelancer ghosted mid-campaign. The pattern is consistent enough we built the model around it.\""],
        ["Quality drift / new marketing leader", "A",
         "\"The most common story we hear is great first month, quality slip by month four. Usually that means the vendor scaled the account through a pool. We don't run pools.\""],
        ["Funding / paid creative pain", "A",
         "\"Most growth teams that come to us have run paid for a quarter on a 14-day refresh cycle that should have been 5. The vendor couldn't keep up.\""],
        ["Agency editor hire / RFP", "B",
         "\"Most agencies come to us after a vendor that survived strategy meetings but missed the client deliverable date. The math at signup stops working by month three.\""],
        ["Agency renewal cycle / churn risk", "B",
         "\"Most agencies that come to us have a renewal book with one or two accounts flagging video as a churn risk. The vendor scaled the team through a pool. We don't.\""],
        ["Enterprise pharma", "Opportunistic",
         "\"Enterprise teams usually come to us after a vendor couldn't survive legal and brand-compliance review. We've built around the approval cycle, not against it.\""],
        ["Founder (Adam-shaped)", "Opportunistic",
         "\"Founder-led marketing functions usually outgrow their vendor stack and don't notice until deals start slipping. We tend to stay 8+ years for that reason.\""],
    ]
    story.append(make_table(obs_rows, [1.6*inch, 0.9*inch, 4.2*inch]))

    story.append(H2("Audience-specific qualifier (Email 2 paragraph 2)"))
    qual_rows = [
        ["Funnel / signal type", "Qualifier line"],
        ["Funnel A &mdash; Sierra (mid-market)", "\"ready to post on LinkedIn or YouTube\""],
        ["Funnel A &mdash; Lindsey (growth)", "\"ready for paid or organic\""],
        ["Funnel B &mdash; Daniel (agency)", "\"ready to deliver under your label\""],
        ["Opportunistic &mdash; Brittany (pharma)", "\"regulatory-aware\""],
        ["Opportunistic &mdash; Adam (founder)", "\"positioned for the next phase\""],
    ]
    story.append(make_table(qual_rows, [2.5*inch, 4.2*inch]))

    story.append(PageBreak())

    # ---- Rendered Examples ----
    story.append(H("Rendered Examples"))
    story.append(P("Six prospect pairs, fully resolved Email 1 + Email 2 ready to send. No placeholders. Pulled across all funnels."))

    # Prospect 1
    story.append(H2("Prospect 1 &mdash; Maya Reyes, Senior Marketing Manager, Step"))
    story.append(P("<b>Funnel A &middot; Signal B1 (job posting)</b>"))
    story.append(H3("Email 1"))
    story.append(C("""Subject: editor hire

Hi Maya, saw Step is hiring a Video Editor. Most of our
clients came to us right after a freelancer ghosted
before a launch or a quarterly review. The math on
hiring full-time usually doesn't survive a slow quarter
either.

Self Financial runs their video through our pod. One
dedicated editor brand-trained before the first
project, first drafts in 24 hours, Slack response
inside the hour Mon to Fri. Unlimited revisions on the
first batch until the baseline is right.

Worth a look for Step?"""))
    story.append(H3("Email 2"))
    story.append(C("""Subject: re: editor hire

Almost every team we work with came to us after a
freelancer ghosted mid-campaign. The pattern is
consistent enough we built the model around it.

Viral takes any long-form video and ships 5 short-form
pieces in 5 business days. Branded, captioned, ready to
post on LinkedIn or YouTube.

Interested in 5 short-form cuts from one of your
existing Step long-forms? (on us)"""))

    story.append(PageBreak())

    # Prospect 2
    story.append(H2("Prospect 2 &mdash; Tom Diaz, Head of Growth, Mercury"))
    story.append(P("<b>Funnel A &middot; Signal B6 (Series C funding)</b>"))
    story.append(H3("Email 1"))
    story.append(C("""Subject: series c content

Hi Tom, congrats on Mercury's Series C last quarter.
The 90 days after a round usually mean creative supply
becomes the bottleneck. Sales enablement, paid ads,
recruiting content, and investor updates all need video
at once, and hiring takes too long.

Gainbridge, the growth team inside Group 1001 with
about 160 billion in assets under management, runs
their paid-creative testing through our pod. One
dedicated editor, first drafts in 24 hours, ships new
ad variants twice a week.

Open to a 15-minute diagnostic?"""))
    story.append(H3("Email 2"))
    story.append(C("""Subject: re: series c content

Most growth teams that come to us have run paid for a
quarter on a 14-day refresh cycle that should have been
5. The vendor couldn't keep up.

Viral takes any long-form video and ships 5 short-form
pieces in 5 business days. Branded, captioned, ready
for paid or organic.

Interested in 5 short-form cuts from one of your
existing Mercury long-forms? (on us)"""))

    story.append(PageBreak())

    # Prospect 3
    story.append(H2("Prospect 3 &mdash; Sarah Chen, CEO, Anomaly"))
    story.append(P("<b>Funnel B &middot; Signal B1 (agency editor hire)</b>"))
    story.append(H3("Email 1"))
    story.append(C("""Subject: editor hire

Hi Sarah, saw Anomaly is hiring a Senior Video Editor.
Most agencies that come to us tried to hire their way
out and the math broke. A full-time editor is dead
weight on slow weeks, and the brand calendar doesn't
pause while you ramp.

Clever Digital Marketing, a Canadian agency running
about 80 staff, runs our team behind their accounts
white-label. Same editor every week, same-day first
drafts on Full-Time, Slack response inside the hour.
The cuts go out under their brand.

Worth a look for Anomaly?"""))
    story.append(H3("Email 2"))
    story.append(C("""Subject: re: editor hire

Most agencies come to us after a vendor that survived
strategy meetings but missed the client deliverable
date. The math at signup stops working by month three.

Viral takes any long-form video and ships 5 short-form
pieces in 5 business days. Branded, captioned, ready to
deliver under your label.

Interested in 5 short-form cuts from one of your
existing client long-forms? (on us)"""))

    story.append(PageBreak())

    # Prospect 4
    story.append(H2("Prospect 4 &mdash; Jessica Park, VP Marketing, Cala Health"))
    story.append(P("<b>Funnel A &middot; Signal B2 (new marketing leader)</b>"))
    story.append(H3("Email 1"))
    story.append(C("""Subject: new vp start

Hi Jessica, congrats on the VP Marketing start at Cala
Health. First 90 days for most marketing leaders means
an audit of the content stack while the calendar keeps
moving. The brief intake usually gets sloppy and video
falls behind first.

Self Financial runs their content production through
our pod for exactly this. One dedicated editor
brand-trained before the first project, first drafts in
24 hours, Slack response inside the hour Mon to Fri.

The audit runs in parallel. The cadence holds.

Worth a look for Cala?"""))
    story.append(H3("Email 2"))
    story.append(C("""Subject: re: new vp start

The most common story we hear is great first month,
quality slip by month four. Usually that means the
vendor scaled the account through a pool. We don't run
pools.

Viral takes any long-form video and ships 5 short-form
pieces in 5 business days. Branded, captioned, ready to
post.

Interested in 5 short-form cuts from one of your
existing Cala Health long-forms? (on us)"""))

    story.append(PageBreak())

    # Prospect 5
    story.append(H2("Prospect 5 &mdash; Rachel Park, Sr. Marketing Director, Eli Lilly Oncology"))
    story.append(P("<b>Opportunistic &middot; Signal A1 (FDA approval)</b>"))
    story.append(H3("Email 1"))
    story.append(C("""Subject: approval launch

Hi Rachel, congrats on the FDA approval at Lilly
Oncology last month. Most enterprise launches need
approval-friendly volume that survives legal review on
the first pass. Most vendors don't survive enterprise
governance.

Ontada, the McKesson healthcare-data subsidiary, runs
their HCP and clinical-trial cuts through our pod. The
editor learns the compliance pattern by the third
project. Submissions clear legal on the first pass more
often than not. A six-week cycle shrinks to two.

Open to a 15-minute diagnostic?"""))
    story.append(H3("Email 2"))
    story.append(C("""Subject: re: approval launch

Enterprise teams usually come to us after a vendor
couldn't survive legal and brand-compliance review.
We've built around the approval cycle, not against it.

Viral takes any long-form video and ships 5 short-form
pieces in 5 business days. Branded, captioned,
regulatory-aware.

Interested in 5 short-form cuts from one of your
existing Lilly long-forms? (on us)"""))

    story.append(PageBreak())

    # Prospect 6
    story.append(H2("Prospect 6 &mdash; Marcus Webb, COO, Sage Communications"))
    story.append(P("<b>Funnel B &middot; Signal B5 + B8 (new client win + Q4 renewal cycle)</b>"))
    story.append(H3("Email 1"))
    story.append(C("""Subject: renewal stack

Hi Marcus, saw Sage just announced the new client win.
Most agencies hitting Q4 with new accounts and an
in-house team already at capacity see existing clients
start asking pointed questions about turnaround.

Clever Digital Marketing, a Canadian agency running
about 80 staff, runs our team behind five of their
accounts white-label. Same-day first drafts, dedicated
editor per account, Slack response inside the hour.

Their renewal book got cleaner. Clients never knew.

Worth a look for Sage?"""))
    story.append(H3("Email 2"))
    story.append(C("""Subject: re: renewal stack

Most agencies that come to us have a renewal book with
one or two accounts flagging video as a churn risk. The
vendor scaled the team through a pool. We don't.

Viral takes any long-form video and ships 5 short-form
pieces in 5 business days. Branded, captioned, ready to
deliver under your label.

Interested in 5 short-form cuts from one of your
existing client long-forms? (on us)"""))

    story.append(PageBreak())

    # ---- VI Differentiator Library ----
    story.append(H("VI Differentiator Library"))
    story.append(P("The REAL differentiators from the Discovery Questionnaire. Use them verbatim in Email 1's solution line. Match to context."))
    diff_rows = [
        ["Differentiator", "When to use"],
        ["\"One dedicated editor, brand-trained before the first project\"", "Default &mdash; works in every signal"],
        ["\"First drafts in 24 hours\" (Funnel A) / \"Same-day first drafts\" (Funnel B)", "Speed/responsiveness pain"],
        ["\"Slack response inside the hour Mon to Fri 9 to 5 EST\"", "Communication-collapse pain (post-freelancer-ghost)"],
        ["\"Unlimited revisions on the first batch until the baseline is right\"", "Quality-fear pain"],
        ["\"Same editor every week. No pool, no rotation.\"", "Brand-drift pain"],
        ["\"The editor learns the compliance pattern by the third project\"", "Pharma / regulated environments"],
        ["\"No ticket portal, no edit lottery, no autoresponder\"", "Vendor-collapse pain"],
        ["\"The cuts go out under your brand. The client never knows we exist.\"", "Funnel B (agency white-label)"],
        ["\"Submissions clear legal on the first pass more often than not\"", "Enterprise pharma"],
        ["\"Strategic input on hook, retention, and platform fit, not just execution\"", "Adam (founder) / mature buyers"],
    ]
    story.append(make_table(diff_rows, [3.3*inch, 3.4*inch]))

    # ---- VOC Language ----
    story.append(H("VOC Language Library (prospect's own words)"))
    story.append(P("Use these in pain lines. They sound like the prospect's own internal monologue."))
    story.append(H3("All buyers say"))
    story.append(P("\"ghosted,\" \"dropped the ball,\" \"off brand,\" \"inconsistent,\" \"unreliable,\" \"another fire drill,\" \"I'm drowning,\" \"out of bandwidth,\" \"we keep starting over,\" \"the last batch was rough,\" \"I just need someone I can trust,\" \"I can't keep doing this,\" \"we can't scale this,\" \"I need a real team, not a freelancer.\""))
    story.append(H3("Agencies (Funnel B) say"))
    story.append(P("\"white-label,\" \"dedicated editor,\" \"we need someone who can ramp without us teaching them everything,\" \"the client noticed.\""))
    story.append(H3("Enterprise marketers (Brittany) say"))
    story.append(P("\"approval friendly,\" \"on brand at scale,\" \"we can't have surprises.\""))

    story.append(PageBreak())

    # ---- Copy Rules ----
    story.append(H("Copy Rules (Non-Negotiable)"))
    rules_rows = [
        ["Rule", "Why"],
        ["50-100 words per email (Email 1: 70-100, Email 2: 60-90)", "Brand book grade 8-10 reading level. Above 100 words loses the buyer."],
        ["Subject: 2-4 words, lowercase, anchored to prospect-owned thing", "\"editor hire\" beats \"video production services for B2B SaaS\""],
        ["Person and company names always capitalized", "Even in lowercase subject lines"],
        ["No em dashes", "Use sentence breaks or commas"],
        ["No exclamation marks", "Brand book: calm and confident, never urgent"],
        ["No spam words (especially \"free\")", "Replace with \"on us\""],
        ["No \"$\" symbol", "Pricing belongs on the call, not in cold body"],
        ["No bracket placeholders in final render", "Every variable resolved before send"],
        ["No \"Best, [Name]\" inside body", "Signature handled by EmailBison {SENDER_EMAIL_SIGNATURE}"],
        ["No apologetic PS", "\"If this isn't a fit...\" reads insecure. Calm and confident only."],
        ["No in-body taglines", "BIGVU bug to avoid &mdash; keep brand lines in signature, not body"],
        ["Soft yes/no CTA in Email 1", "\"Worth a look for [Company]?\" or \"Open to a 15-min diagnostic?\""],
        ["Lead magnet drops in Email 2 only", "Email 1 teases the product. Email 2 offers the 5-cut pack."],
        ["Email 2 paragraph 1 pulls from the 5 switching reasons", "Prospect feels understood (\"they know what I went through\")"],
        ["Funnel-matched case study", "Self Financial/Gainbridge for A &middot; Clever Digital for B &middot; Ontada/Asset Map for opportunistic"],
        ["VOC language in pain lines", "Use prospect's own words: ghosted, fire drill, drowning, white-label, approval friendly"],
    ]
    story.append(make_table(rules_rows, [3.0*inch, 3.7*inch]))

    # ---- Pre-Reqs ----
    story.append(H("Operational Pre-Requisites Before Launch"))
    story.append(B("<b>Sample delivery workflow.</b> When a prospect replies to Email 2, the team must deliver the 5-cut pack within 24-48 hours. Same single point of failure that broke BIGVU's funnel."))
    story.append(B("<b>Funnel-matched case study assets.</b> Self Financial, Gainbridge, Clever Digital, Ontada, Asset Map &mdash; each needs a one-paragraph proof block. Hard outcome numbers are the gap (Dave to backfill 2-3 per case study)."))
    story.append(B("<b>Sender persona signature.</b> Name, brand, NYC location, phone number, website. Missing phone/address triggers scammer suspicion."))
    story.append(B("<b>Signal-finder prompts deployed.</b> Prompt A + Prompt B in Clay or equivalent, priority-ordered evaluation."))
    story.append(B("<b>Suppression list functional.</b> Negative replies, OOOs, prior unsubscribes feed back into Clay / EmailBison suppression."))
    story.append(B("<b>Funnel-routing logic.</b> Lead's title + industry determines which funnel. Mid-market mkt mgr + growth marketer &rarr; Funnel A. Agency owner/CEO &rarr; Funnel B. Enterprise pharma + B2B founder &rarr; opportunistic."))

    # ---- Open Decisions ----
    story.append(H("Open Decisions for Dave Before Launch"))
    story.append(B("<b>Lead magnet for Email 2.</b> Current default is the 5-cut pack. Video Grader (self-service) is inbound. 15-min diagnostic is the Doctor Frame closer. Recommend 5-cut for cold, Diagnostic as Email 3."))
    story.append(B("<b>Pricing transparency in cold copy.</b> Currently removed entirely. Recommend stay off pricing in cold, mention on call."))
    story.append(B("<b>Hard outcome numbers per case study.</b> Dave owes 2-3 numbers per case study so proof line beats logos-only."))
    story.append(B("<b>Coordination with existing Lead Hunter outbound</b> (vlad@leadhunter.net). Pause, parallel, or handoff?"))
    story.append(B("<b>Sender persona</b> &mdash; spin up a new Viral persona, do not reuse BIGVU's Sarah Stanfield."))

    story.append(Spacer(1, 0.2*inch))
    story.append(CAP(f"Document version: v2 ({date.today().isoformat()}) | github.com/matteof123/Viral"))

    doc.build(story, onFirstPage=cover_only, onLaterPages=page_footer)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()
