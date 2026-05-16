#!/usr/bin/env python3
"""
Viral Ideas Marketing — Triggers & Email Templates PDF generator.

Produces the team-facing PDF version of triggers-and-templates.md.
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
    canvas.drawString(0.9*inch, 0.45*inch, f"Viral Ideas Marketing  |  Triggers & Email Templates  |  {date.today().isoformat()}")
    canvas.drawRightString(7.6*inch, 0.45*inch, f"Page {doc.page}")
    canvas.restoreState()

def cover_only(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, LETTER[1]-1.4*inch, LETTER[0], 0.18*inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 32)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-3.8*inch, "Triggers & Email Templates")
    canvas.setFillColor(ACCENT)
    canvas.setFont("Helvetica-Bold", 24)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-4.6*inch, "Viral Ideas Marketing")
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 12)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-5.3*inch,
                             "Two-prompt signal taxonomy + Email 1 / Email 2 system")
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-5.6*inch,
                             "Modeled on BIGVU Campaign 198 (2.0% reply rate, 40 interested)")
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
                            title="Viral Ideas — Triggers & Email Templates")
    story = []

    # Cover
    story.append(PageBreak())

    # ---- Section 1: What this is ----
    story.append(H("What This Is"))
    story.append(P("The complete signal taxonomy and email template system for Viral Ideas Marketing outbound. Modeled on the live structure of BIGVU's Campaign 198 (2.0% reply rate, 40 interested replies across 25,000+ sends). The structure is intentionally simple. The variable is the trigger line."))
    story.append(P("The system uses two signal-finding prompts that run in priority order:"))
    story.append(B("<b>Prompt A &mdash; Pharma-specific</b> &mdash; run first for pharma, biotech, healthcare, med device leads"))
    story.append(B("<b>Prompt B &mdash; Universal</b> &mdash; run for all leads. Fallback for pharma leads where Prompt A finds nothing"))
    story.append(P("For agency or fintech leads, skip Prompt A and run Prompt B only."))
    story.append(P("Each signal produces a different Email 1 trigger line. The rest of Email 1 stays identical. Email 2 is the lead-magnet pivot (free 5-cut repurposing pack) and is the same across all signals."))

    # ---- Section 2: Prompt A ----
    story.append(H("Signal Mix &mdash; Prompt A (Pharma-Specific)"))
    story.append(P("Run first when the lead is in pharma, biotech, healthcare, med device, or pharma-adjacent industries. Stop at first match. If no signal found, fall through to Prompt B."))
    rows_a = [
        ["#", "Signal", "Recency window", "Where to look"],
        ["A1", "<b>FDA approval / new indication / new device approval</b>",
         "last 90 days",
         "Drugs@FDA, FDA press releases, BioPharma Dive, FiercePharma, company press releases, SEC 8-K filings"],
        ["A2", "<b>Clinical trial milestone / Phase III readout / endpoint announcement</b>",
         "last 90 days",
         "ClinicalTrials.gov, company press releases, biopharma trade press"],
        ["A3", "<b>Upcoming medical congress with accepted abstract / poster / symposium</b>",
         "next 60 days",
         "Conference programs and late-breaker lists: ASH, ASCO, AHA, ESMO, AAD, ACR, AAOS, BIO, JPM Healthcare, ENDO, DDW"],
        ["A4", "<b>Currently using a named pharma video agency of record</b>",
         "verified in last 12 months",
         "Case study credits, press releases, LinkedIn employee bios. Agencies to flag: Klick Health, Razorfish Health, Ogilvy Health, EVERSANA, Greater Than One, Real Chemistry, FCB Health, Saatchi &amp; Saatchi Wellness, Havas Health, McCann Health"],
    ]
    story.append(make_table(rows_a, [0.4*inch, 1.7*inch, 1.0*inch, 3.6*inch]))

    # ---- Section 3: Prompt B ----
    story.append(H("Signal Mix &mdash; Prompt B (Universal)"))
    story.append(P("Run for all leads. Stop at first match. Works across pharma, agencies, and fintech without rewrites."))
    rows_b = [
        ["#", "Signal", "Recency", "Hit rate", "Where to look"],
        ["B1", "<b>Open job posting for video / content / marketing production role</b>",
         "30d", "~15-25%",
         "LinkedIn Jobs, Indeed. Title contains \"Video,\" \"Multimedia,\" \"Motion,\" \"Content Producer,\" \"Video Editor\""],
        ["B2", "<b>New marketing / brand / content leader hired</b>",
         "90d", "~20-30%",
         "LinkedIn \"Started new position\" + vertical filter + marketing/content/brand titles"],
        ["B3", "<b>Underutilized long-form footage on brand channel</b> (15+ min video, no &lt;2-min cuts on social)",
         "120d", "~50-70%",
         "YouTube / Vimeo brand channels, cross-check LinkedIn + Instagram for derivative cuts"],
        ["B4", "<b>Image-heavy LinkedIn brand page</b> (fewer than 3 videos in 120 days)",
         "120d", "~60-80%",
         "Company LinkedIn page post feed; count video vs image/text posts"],
        ["B5", "<b>Recent company growth / expansion announcement</b> (any \"we just X\" post)",
         "90d", "~25-40%",
         "Company LinkedIn brand page, press releases, \"Newsroom\" pages"],
        ["B6", "<b>Recent funding / growth milestone</b>",
         "90d", "~10-25% (vertical-dependent)",
         "Crunchbase, TechCrunch, BioPharma Dive, Endpoints News"],
        ["B7", "<b>Lead's most recent personal LinkedIn activity</b> (guaranteed fallback)",
         "30d", "~85-95%",
         "Lead's LinkedIn profile activity tab"],
    ]
    story.append(make_table(rows_b, [0.35*inch, 1.6*inch, 0.5*inch, 0.7*inch, 3.55*inch]))

    story.append(PageBreak())

    # ---- Section 4: Email 1 template ----
    story.append(H("Email 1 &mdash; Template"))
    story.append(P("The trigger line is the variable. Everything else stays the same across all signals."))
    email1_template = """Subject: [trigger-anchored 2-4 word lowercase subject]

Hi [First Name],

[TRIGGER LINE -- see trigger table below].

You're already producing the high-value content. The
bottleneck is the edit cycle. [Vertical-matched case
study -- Janssen / Cortechs.ai for pharma, Clever
Digital for agencies, Self Financial / Gainbridge for
fintech] runs their video repurposing through our
editing pod.

Same dedicated editor every week, managing editor on
QA, finished cuts in days.

Worth a quick look?

Cheers,

[Sender]
Viral Ideas Marketing"""
    story.append(C(email1_template))
    story.append(CAP("Word target: 70-85 words. No em dashes. No exclamation marks. No spam words. No bracket placeholders in the final render. No apologetic PS. Sign-off is signature only -- no in-body taglines."))

    # ---- Section 5: Trigger line examples ----
    story.append(H("Trigger Line Examples by Signal"))
    story.append(P("The trigger is Line 1 of Email 1. Each signal produces a different trigger line. The subject line follows the same trigger pattern: 2-4 words, lowercase, anchored to a specific prospect-owned thing."))

    story.append(H2("Prompt A &mdash; Pharma triggers"))
    rows_trig_a = [
        ["Signal", "Subject", "Trigger line (Line 1 of Email 1)"],
        ["<b>A1</b> FDA approval", "<font face='Courier'>[drug] launch</font>",
         "\"Congrats on the FDA approval for [Drug]. Launch quarters typically mean six weeks of HCP intros, sales enablement, and KOL content moving through med-legal at the same time.\""],
        ["<b>A2</b> Clinical trial readout", "<font face='Courier'>[trial] readout</font>",
         "\"Saw [Company] just published the [Trial Name] Phase III readout. The pre-launch cycle that follows usually means advisory board summaries, MOA explainers, and KOL clips queued at once.\""],
        ["<b>A3</b> Medical congress", "<font face='Courier'>[conference] content</font>",
         "\"Saw [Company]'s team is presenting at [Conference] next month. Conference content usually splits three ways: launch teaser, day-of clips, and the recap series sales uses for the next quarter.\""],
        ["<b>A4</b> Named pharma agency", "<font face='Courier'>agency overflow</font>",
         "\"Saw [Company] credits [Agency] on the [Drug] work. Most pharma brand teams use a lead agency for strategy and a separate pod for editing volume, especially through launch quarters.\""],
    ]
    story.append(make_table(rows_trig_a, [1.2*inch, 1.3*inch, 4.2*inch]))

    story.append(H2("Prompt B &mdash; Universal triggers"))
    rows_trig_b = [
        ["Signal", "Subject", "Trigger line (Line 1 of Email 1)"],
        ["<b>B1</b> Job posting", "<font face='Courier'>video specialist hire</font>",
         "\"I saw [Company] is hiring a [Role Title] for the [Team] team. Open production roles usually mean the brand calendar is already running ahead of the team's editing capacity.\""],
        ["<b>B2</b> New marketing leader", "<font face='Courier'>new [role] start</font>",
         "\"Congrats on the [Role] start at [Company]. First 90 days for most marketing leaders means a content stack audit and a new cadence to ship by quarter-end.\""],
        ["<b>B3</b> Underutilized long-form", "<font face='Courier'>your [topic] interview</font>",
         "\"I saw [Company]'s recent [Topic] interview on the brand channel - [X] minutes of long-form content. Brand teams that repurpose long-form into short-form usually see 5-10x more reach from the same source material.\""],
        ["<b>B4</b> Image-heavy LinkedIn", "<font face='Courier'>your video gap</font>",
         "\"I noticed [Company] is posting [X] times a week on LinkedIn - mostly carousels and graphics. Brand teams that add video to the same posting cadence usually see 2-3x the engagement from the same audience.\""],
        ["<b>B5</b> Growth announcement", "<font face='Courier'>[announcement] content</font>",
         "\"Saw [Company]'s [Partnership / Office / Client / Campaign] announcement. Launches like that typically trigger a content sprint - launch clips, internal comms, social cuts, and a recap deck.\""],
        ["<b>B6</b> Funding round", "<font face='Courier'>[series] content</font>",
         "\"Congrats on the [Series X]. The 90 days that follow usually mean creative supply becomes the bottleneck - sales enablement, paid ads, and recruiting content all needed at once.\""],
        ["<b>B7</b> LinkedIn activity (fallback)", "<font face='Courier'>your [topic] post</font>",
         "\"Saw your recent LinkedIn post on [Topic]. Posts that land usually have 5-10x the reach when republished as a short-form video with captions and a branded cut.\""],
    ]
    story.append(make_table(rows_trig_b, [1.2*inch, 1.3*inch, 4.2*inch]))

    story.append(PageBreak())

    # ---- Section 6: Email 1 filled example ----
    story.append(H("Email 1 &mdash; Filled Example (Signal B3)"))
    email1_filled = """Subject: your moa interview

Hi Brittany,

I saw Ontada's recent MOA interview on the brand channel
- 38 minutes of long-form content. Brand teams that
repurpose long-form into short-form usually see 5-10x
more reach from the same source material.

You're already producing the high-value content. The
bottleneck is the edit cycle. Janssen and Cortechs.ai
run their HCP video repurposing through our editing
pod.

Same dedicated editor every week, managing editor on
QA, finished cuts in days.

Worth a quick look?

Cheers,

Sarah Stanfield
Viral Ideas Marketing"""
    story.append(C(email1_filled))
    story.append(CAP("Word count: 79"))

    # ---- Section 7: Email 2 template ----
    story.append(H("Email 2 &mdash; Template (Lead-Magnet Pivot)"))
    story.append(P("Same thread, approximately 3-5 days after Email 1. Pivots from product-tease to the lead magnet offer."))
    email2_template = """Subject: Re: [Email 1 subject]

Hi [First Name],

[New broader observation about the company -- their
content cadence, recent activity, something visible.
NOT a repeat of the Email 1 trigger].

Viral can turn any long-form video into a set of
branded short-form cuts in days, eliminating the
multi-week edit cycle most brand teams hit.

Would you be interested in 5 short-form cuts from one
of your existing long-forms? (on us)

Cheers,

[Sender]
Viral Ideas Marketing"""
    story.append(C(email2_template))
    story.append(CAP("Word target: 60-80 words"))

    # ---- Section 8: Email 2 filled example ----
    story.append(H("Email 2 &mdash; Filled Example"))
    email2_filled = """Subject: Re: your moa interview

Hi Brittany,

It looks like Ontada is putting out long-form content
on a regular cadence - the MOA interview is one
example.

Viral can turn any long-form video into a set of
branded short-form cuts in days, eliminating the
multi-week edit cycle most brand teams hit.

Would you be interested in 5 short-form cuts from one
of your existing long-forms? (on us)

Cheers,

Sarah Stanfield
Viral Ideas Marketing"""
    story.append(C(email2_filled))
    story.append(CAP("Word count: 71"))

    story.append(PageBreak())

    # ---- Section 9: Copy rules ----
    story.append(H("Copy Rules (Non-Negotiable)"))
    story.append(P("Pulled from the 2026 Brand Book and Viral's GTM playbook. Every email must pass these checks before send."))
    rules_rows = [
        ["Rule", "Why"],
        ["50-80 words per email", "Brand-book grade 8-10 reading level. Above 80 words loses the buyer."],
        ["Subject line: 2-4 words, lowercase, anchored to specific prospect-owned thing", "\"your moa interview\" beats \"video production services for pharma\""],
        ["Person and company names always capitalized", "Even in lowercase subject lines"],
        ["No em dashes", "Use sentence breaks or commas"],
        ["No exclamation marks", "Brand book: calm and confident, never urgent"],
        ["No spam words (especially \"free\")", "Replace with \"on us\""],
        ["No bracket placeholders in final render", "Every variable must be resolved before send"],
        ["No \"Best, Sender Name\" inside body", "Signature handled by EmailBison {SENDER_EMAIL_SIGNATURE} system variable"],
        ["No apologetic PS", "\"If this isn't a fit...\" reads insecure. Calm and confident only."],
        ["No in-body taglines", "Viral equivalent of BIGVU's \"Be Brilliant On Camera\" bug -- keep brand lines in signature"],
        ["Soft yes/no CTA in Email 1", "\"Worth a quick look?\" beats \"Want a sample? 24 hours.\""],
        ["Lead magnet drops in Email 2 only", "Email 1 teases the product. Email 2 offers the 5-cut pack."],
    ]
    story.append(make_table(rules_rows, [3.0*inch, 3.7*inch]))

    # ---- Section 10: Why this works ----
    story.append(H("Why This Structure Works"))
    story.append(P("BIGVU has been running this exact structure for approximately 4 weeks at the time of writing. Stats:"))
    story.append(B("<b>Campaign 198:</b> 25,000+ sent, 285 replies (1.1%), 40 marked interested (14% positive-of-reply ratio)"))
    story.append(B("<b>Email 1 alone:</b> 156 of 270 unique replies (58% of all replies)"))
    story.append(B("<b>Email 2 alone:</b> 47 unique replies, 7 interested"))
    story.append(B("<b>Top-performing subject patterns:</b> <font face='Courier'>your [city] listing</font>, <font face='Courier'>new [city] listing video</font>, <font face='Courier'>your [topic] interview</font>"))
    story.append(P("The same structural skeleton, dropped onto Viral's signals + Viral's lead magnet, is what this document encodes."))

    # ---- Section 11: Operational pre-reqs ----
    story.append(H("Operational Pre-Requisites Before Launch"))
    story.append(P("These must be in place before Email 1 ships:"))
    story.append(B("<b>Sample delivery workflow.</b> When a prospect replies to Email 2 saying \"yes, send the cuts,\" the team must be able to deliver the 5-cut pack within 24-48 hours. This is the single point in BIGVU's funnel that breaks (per Apr 30 call data -- positives go cold after Calendly pivot). Viral cannot fall into the same trap."))
    story.append(B("<b>Vertical-matched case study assets.</b> Janssen, Cortechs.ai, Clever Digital, Self Financial -- all need at least a one-paragraph proof block ready to reference. Hard outcome numbers are the playbook gap."))
    story.append(B("<b>Sender persona signature.</b> Name, brand, NYC location, phone number, website. Missing phone/address triggers scammer suspicion."))
    story.append(B("<b>Signal-finder prompts deployed.</b> Prompt A and Prompt B running in Clay or equivalent, with priority-ordered evaluation logic."))
    story.append(B("<b>Suppression list functional.</b> Negative replies, OOOs, and prior unsubscribes feed back into Clay / EmailBison suppression."))

    # ---- Section 12: Open decisions ----
    story.append(H("Open Decisions for Dave Before Launch"))
    story.append(B("HVAC vs. law firms in scope?"))
    story.append(B("Outcome metrics per vertical (the case-study hard numbers we currently lack)"))
    story.append(B("Pricing transparency in cold copy ($1,500-$5,000/mo in body, or price-discovery on call?)"))
    story.append(B("SaaS / pro services in or out of first 90 days?"))
    story.append(B("Coordination with existing Lead Hunter outbound (pause, parallel, or handoff?)"))
    story.append(B("Construction / remodeling angle -- kill or add?"))
    story.append(B("PR firms as a new vertical (per recent Devine Partners reply)?"))

    story.append(Spacer(1, 0.2*inch))
    story.append(CAP(f"Document version: v1 ({date.today().isoformat()}) | github.com/matteof123/Viral"))

    doc.build(story, onFirstPage=cover_only, onLaterPages=page_footer)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()
