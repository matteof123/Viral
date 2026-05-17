#!/usr/bin/env python3
"""
Viral Ideas Marketing — Outbound Email System (client-facing PDF, v4).

Healthcare/pharma focus for the first 90 days. Six rendered prospect pairs
showing the Trigger + Poke-the-bear + Solution-with-Defuse + Soft-CTA pattern.

Written for Dave Feinman and Zach Medina.
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
OUT = os.path.join(OUT_DIR, "Viral_Outbound_Email_System.pdf")

NAVY = colors.HexColor("#0E2A47")
ACCENT = colors.HexColor("#C8362F")
LIGHT = colors.HexColor("#F4F6F9")
TEXT_GRAY = colors.HexColor("#3A3A3A")
EMAIL_BG = colors.HexColor("#FBFAF5")
EMAIL_BORDER = colors.HexColor("#D9D4C0")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("CoverTitle", parent=styles["Title"], fontSize=36,
                          textColor=NAVY, alignment=TA_CENTER, leading=42, spaceAfter=18))
styles.add(ParagraphStyle("H1", parent=styles["Heading1"], fontSize=20,
                          textColor=NAVY, spaceBefore=14, spaceAfter=10, leading=24))
styles.add(ParagraphStyle("H2", parent=styles["Heading2"], fontSize=14,
                          textColor=ACCENT, spaceBefore=12, spaceAfter=6, leading=18))
styles.add(ParagraphStyle("H3", parent=styles["Heading3"], fontSize=11,
                          textColor=NAVY, spaceBefore=8, spaceAfter=3, leading=14))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontSize=10.5,
                          textColor=TEXT_GRAY, alignment=TA_JUSTIFY, leading=15.5, spaceAfter=8))
styles.add(ParagraphStyle("BodyLeft", parent=styles["Normal"], fontSize=10.5,
                          textColor=TEXT_GRAY, alignment=TA_LEFT, leading=15.5, spaceAfter=8))
styles.add(ParagraphStyle("Lead", parent=styles["Normal"], fontSize=12,
                          textColor=NAVY, alignment=TA_LEFT, leading=17, spaceAfter=10,
                          fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("BulletLine", parent=styles["Body"], leftIndent=14,
                          bulletIndent=2, spaceAfter=3))
styles.add(ParagraphStyle("CellBody", parent=styles["Normal"], fontSize=9.5,
                          textColor=TEXT_GRAY, leading=13))
styles.add(ParagraphStyle("CellHead", parent=styles["Normal"], fontSize=10,
                          textColor=colors.white, leading=12, alignment=TA_LEFT))
styles.add(ParagraphStyle("EmailBlock", parent=styles["Normal"], fontName="Helvetica",
                          fontSize=10, textColor=NAVY, leading=15,
                          leftIndent=12, rightIndent=12, spaceBefore=8, spaceAfter=12,
                          backColor=EMAIL_BG, borderColor=EMAIL_BORDER, borderWidth=0.5,
                          borderPadding=12, alignment=TA_LEFT))
styles.add(ParagraphStyle("EmailLabel", parent=styles["Normal"], fontSize=9.5,
                          textColor=ACCENT, alignment=TA_LEFT, spaceBefore=10, spaceAfter=4,
                          fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("ContextNote", parent=styles["Body"], fontSize=10,
                          textColor=colors.HexColor("#5A5A5A"), alignment=TA_LEFT, spaceAfter=8,
                          fontName="Helvetica-Oblique"))

def H(s): return Paragraph(s, styles["H1"])
def H2(s): return Paragraph(s, styles["H2"])
def H3(s): return Paragraph(s, styles["H3"])
def P(s): return Paragraph(s, styles["Body"])
def PL(s): return Paragraph(s, styles["BodyLeft"])
def LEAD(s): return Paragraph(s, styles["Lead"])
def B(s): return Paragraph(f"&bull;&nbsp;&nbsp;{s}", styles["BulletLine"])
def EMAIL(s): return Paragraph(s.replace("\n\n", "<br/><br/>").replace("\n", "<br/>"), styles["EmailBlock"])
def LABEL(s): return Paragraph(s, styles["EmailLabel"])
def NOTE(s): return Paragraph(s, styles["ContextNote"])

def cell(s, head=False):
    style = styles["CellHead"] if head else styles["CellBody"]
    return Paragraph(str(s), style)

def page_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawString(0.9*inch, 0.45*inch, "Viral Ideas Marketing  |  Outbound Email System  |  Prepared by Outreach Magic")
    canvas.drawRightString(7.6*inch, 0.45*inch, f"{doc.page}")
    canvas.restoreState()

def cover_only(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, LETTER[1]-1.4*inch, LETTER[0], 0.18*inch, fill=1, stroke=0)

    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 38)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-3.4*inch, "Outbound Email System")
    canvas.setFillColor(ACCENT)
    canvas.setFont("Helvetica-Bold", 26)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-4.2*inch, "Viral Ideas Marketing")
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 13)
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-5.0*inch,
                             "Healthcare and pharma focus.")
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-5.3*inch,
                             "Ten buying signals. Six emails ready to send.")
    canvas.setFont("Helvetica", 10)
    canvas.setFillColor(colors.HexColor("#BBBBBB"))
    canvas.drawCentredString(LETTER[0]/2, 1.55*inch, f"Prepared {date.today().isoformat()}")
    canvas.drawCentredString(LETTER[0]/2, 1.30*inch, "Outreach Magic for Viral Ideas Marketing")
    canvas.restoreState()

def make_table(rows, col_widths, header=True):
    if header:
        rows = [[cell(c, head=True) for c in rows[0]]] + [[cell(c) for c in r] for r in rows[1:]]
    else:
        rows = [[cell(c) for c in r] for r in rows]
    t = Table(rows, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
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

def email_pair(name, role, company, funnel_note, subject1, body1, body2):
    """Render one prospect's Email 1 + Email 2."""
    elements = []
    elements.append(H2(f"{name}, {role}, {company}"))
    elements.append(NOTE(funnel_note))
    elements.append(LABEL("EMAIL 1"))
    elements.append(EMAIL(f"<b>Subject:</b> {subject1}\n\n{body1}"))
    elements.append(LABEL("EMAIL 2  (same thread, 3 to 5 days later)"))
    elements.append(EMAIL(f"<b>Subject:</b> re: {subject1}\n\n{body2}"))
    return elements

def build():
    doc = SimpleDocTemplate(OUT, pagesize=LETTER,
                            leftMargin=0.9*inch, rightMargin=0.9*inch,
                            topMargin=0.9*inch, bottomMargin=0.8*inch,
                            title="Viral Ideas — Outbound Email System")
    story = []

    story.append(PageBreak())

    # ---- What this is ----
    story.append(H("What this is"))
    story.append(LEAD("The outbound system we're building for Viral, focused on healthcare and pharma for the first 90 days."))
    story.append(P("Ten buying signals because outbound that ignores triggers wastes everyone's time. Six full emails so you can see exactly what we plan to send before we send it."))
    story.append(P("You should be able to read this end to end in fifteen minutes. The six emails in the middle are the heart of it. Everything else explains why those emails look the way they do."))
    story.append(Spacer(1, 0.15*inch))
    story.append(P("Three things to flag up front. Pricing stays off cold email until we agree it shouldn't. The free five-cut repurposing pack is the lead magnet we offer in the follow-up. And every email ends at the call to action, with no sign-off in the body, because Viral's email signature handles the rest."))

    story.append(PageBreak())

    # ---- Who we're targeting ----
    story.append(H("Who we're targeting"))
    story.append(LEAD("Healthcare and pharma marketing leaders. First 90 days. One vertical at a time."))
    story.append(P("The Discovery work named five archetypes Viral wins with. For the first ninety days of outbound we focus on the three that live in healthcare and pharma."))

    story.append(H2("The marketing manager at a healthcare brand"))
    story.append(P("Mid-market marketing manager or senior marketing manager running a one-to-three person team inside a pharma, biotech, or healthcare brand. She runs a content quota that keeps growing, a freelancer rotation that keeps breaking, and a CMO who walks into the Monday standup and asks pointed questions about video. She's competent and tired of being the last line of defense when a vendor disappears."))

    story.append(H2("The senior marketing director at an enterprise subsidiary"))
    story.append(P("Senior marketing director or business director running a brand inside a McKesson, Johnson and Johnson, or BMS-shape parent company. Budget isn't the friction. Trust and risk are. She won't buy from a vendor that can't survive legal review, brand-compliance audits, and procurement. Her name is on the PO when something goes wrong."))

    story.append(H2("The growth marketer at a funded biotech or health-tech startup"))
    story.append(P("Growth marketer, performance marketer, or demand-gen lead at a VC or PE backed biotech or health-tech company in the five to fifty million revenue range. Her metric is CAC. Her cadence is weekly creative testing. She doesn't care if the video wins a Cannes Lion. She cares that the hook works in three seconds and the retention curve holds."))

    story.append(P("Outside of healthcare, two other archetypes (agency owners and B2B founders) will get their own playbooks once we validate the healthcare motion in the first 90 days. Not in scope for this document."))

    story.append(PageBreak())

    # ---- How we find prospects ----
    story.append(H("How we find prospects"))
    story.append(LEAD("Signal-first sourcing. Ten triggers, run in priority order. Stop at the first match."))
    story.append(P("For each lead, we check the pharma-specific signals first. If none fire, we run the universal set. The same lead never gets two emails about two different triggers; the strongest one wins."))

    story.append(H2("Pharma-specific signals"))
    pharma_signals = [
        ["Signal", "What we look for", "Window"],
        ["FDA approval or new indication", "Drugs@FDA, FDA press releases, company 8-K filings", "Last 90 days"],
        ["Phase III readout or trial milestone", "ClinicalTrials.gov status updates, primary endpoint announcements", "Last 90 days"],
        ["Upcoming medical congress", "Accepted abstracts and posters at ASH, ASCO, AHA, ESMO, AAD, BIO, JPM Healthcare", "Next 60 days"],
        ["Currently using a named pharma video agency", "Agency-of-record credits in press releases and LinkedIn employee bios", "Verified in last 12 months"],
    ]
    story.append(make_table(pharma_signals, [2.0*inch, 3.7*inch, 1.0*inch]))

    story.append(H2("Universal signals"))
    universal_signals = [
        ["Signal", "What we look for", "Window"],
        ["Open job posting for a video, content, or production role", "LinkedIn Jobs and Indeed listings at healthcare companies", "Last 30 days"],
        ["New marketing, brand, or content leader hired", "LinkedIn \"started new position\" at a healthcare company with a marketing or content title", "Last 90 days"],
        ["Underutilized long-form footage on brand channel", "Brand YouTube or Vimeo with a 15-plus minute KOL or webinar video and no short-form derivative", "Last 120 days"],
        ["Image-heavy LinkedIn brand page", "Corporate page posting weekly with fewer than three videos in the window", "Last 120 days"],
        ["Recent growth, expansion, or new client win announcement", "Company LinkedIn brand posts, press releases, newsroom pages", "Last 90 days"],
        ["Recent funding or growth milestone (biotech, health tech)", "Crunchbase, TechCrunch, BioPharma Dive, Endpoints News", "Last 90 days"],
    ]
    story.append(make_table(universal_signals, [2.4*inch, 3.3*inch, 1.0*inch]))

    story.append(PageBreak())

    # ---- The email structure ----
    story.append(H("The email structure"))
    story.append(LEAD("Two emails per prospect, same thread."))
    story.append(P("The first email anchors a buying trigger. The second offers the lead magnet."))

    story.append(H2("Email 1 has four moves"))
    story.append(B("<b>The trigger.</b> One sentence on what we observed about the prospect. FDA approval, hire posted, abstract accepted, KOL interview uploaded. Specific."))
    story.append(B("<b>The poke-the-bear question.</b> Right after the trigger, a question that makes the prospect nod silently. \"Are you about to spend six weeks pushing HCP cuts through med-legal at the same time?\" The prospect's own internal voice, not ours."))
    story.append(B("<b>The solution.</b> One paragraph that names a real client (Janssen or Ontada), the benefit they get (not the feature we provide), and a defused objection in two to five words. \"Approval-friendly from day one.\" \"No ghosting, no ramp gap.\""))
    story.append(B("<b>The call to action.</b> Soft, specific, named. \"Worth a look for [Company]?\" or \"Open to a 15-minute walkthrough?\""))
    story.append(P("The email ends at the call to action. No \"Cheers, Sarah.\" No tagline. EmailBison's signature variable handles the sign-off."))

    story.append(H2("Email 2 lands the magnet"))
    story.append(P("Sent three to five days after Email 1, same thread. Opens with one short paragraph drawing the pattern from our case files (\"Enterprise teams usually come to us after a vendor couldn't survive legal review\"). One sentence describing what Viral physically does. And the offer:"))
    story.append(LEAD("\"Interested in 5 short-form cuts from one of your existing long-forms? (on us)\""))
    story.append(P("When a prospect says yes, we send the cuts inside five business days, branded and captioned and ready to post. The cuts are how the conversation starts, not how it ends. After delivery, the diagnostic call comes naturally."))

    story.append(PageBreak())

    # ---- Subject lines ----
    story.append(H("Subject lines"))
    story.append(LEAD("Two to four words, lowercase, built to create a small curiosity gap."))
    story.append(P("Four patterns work. The first two carry most of the volume."))

    subj_rows = [
        ["Pattern", "What it does", "Examples"],
        ["<b>Before [their action]</b>", "Hints at an alternative they haven't considered",
         "<font face='Courier'>before you hire</font>, <font face='Courier'>before asco</font>"],
        ["<b>After [their event]</b>", "Implies and-now-what",
         "<font face='Courier'>after the approval</font>, <font face='Courier'>after the readout</font>, <font face='Courier'>after the raise</font>"],
        ["<b>Their [thing], [twist]</b>", "Possessive with an intriguing modifier",
         "<font face='Courier'>your interview, untouched</font>, <font face='Courier'>your freelancer gap</font>"],
        ["<b>Time-bound</b>", "Names the window the prospect is in",
         "<font face='Courier'>first 90 days</font>, <font face='Courier'>six week sprint</font>"],
    ]
    story.append(make_table(subj_rows, [1.6*inch, 2.6*inch, 2.5*inch]))

    story.append(P("What we avoid: urgency words (now, closing, last chance), hype words (revolutionary, game-changing, world-class), and generic placeholders (quick question, video editing services). Your brand voice is calm and confident; the subject line is the first place a prospect tests whether we know that."))

    story.append(PageBreak())

    # ---- The solution paragraph ----
    story.append(H("The solution paragraph"))
    story.append(LEAD("The part most cold emails miss."))
    story.append(P("A weak solution lists features. Dedicated editor, fast drafts, good QA. Every subscription editing service in the category says some version of that. Nothing in it tells the reader why Viral instead of any other vendor."))
    story.append(P("A strong solution does three things in three sentences."))
    story.append(P("First, it names a real pharma client and how they use Viral. For Viral's first 90 days that's almost always <b>the team at Janssen</b> or <b>brand teams at Ontada</b>. One named anchor per email."))
    story.append(P("Second, it names the benefit or result the buyer gets. Not the feature we provide. \"The calendar holds and the CMO stops asking about video in standup\" beats \"dedicated editor with QA pass.\" Features only earn a sentence when they're directly tied to a measurable outcome (\"the six-week cycle shrinks to two\" is fine because it pairs the workflow with the result)."))
    story.append(P("Third, it defuses the biggest objection at the trigger in two to five words. \"Approval-friendly from day one.\" \"Built for med-legal review.\" \"No ghosting, no ramp gap.\" Short enough to land, specific enough to neutralize."))

    story.append(H2("The objection map"))
    obj_rows = [
        ["Defuse phrase", "Handles the objection"],
        ["\"Approval-friendly from day one\"", "Will they survive enterprise governance?"],
        ["\"Regulatory-aware from day one\"", "Do they understand compliance?"],
        ["\"Built for med-legal review\"", "Will they understand our review process?"],
        ["\"Compliance-aware from day one\"", "Can they touch HCP-targeted content?"],
        ["\"No ghosting, no ramp gap\"", "What if they disappear like the last freelancer?"],
        ["\"No ramp time\"", "Can they start fast enough to matter?"],
    ]
    story.append(make_table(obj_rows, [2.6*inch, 4.1*inch]))

    story.append(PageBreak())

    # ---- Six emails ----
    story.append(H("Six emails we'd send today"))
    story.append(LEAD("Six healthcare prospects. The trigger, the email, the follow-up."))
    story.append(P("Names and companies are illustrative. The structure and copy are ready. If you want to swap a case study or a phrase, this is the page to mark up."))

    story.append(PageBreak())

    # Prospect 1
    story.extend(email_pair(
        "Rachel Park", "Senior Marketing Director", "Eli Lilly Oncology",
        "Pharma. Trigger: Eli Lilly Oncology received FDA approval last month.",
        "after the approval",
        """Hi Rachel,

Saw Eli Lilly Oncology just got the FDA approval last month. Are you about to spend six weeks pushing HCP cuts, sales enablement, and KOL interviews through med-legal at the same time?

The team at Janssen runs launch quarters through us. The calendar holds and the CMO stops asking about video in standup. Approval-friendly from day one.

Open to a 15-minute walkthrough for Lilly?""",
        """Enterprise teams usually come to us after a vendor couldn't survive legal and brand-compliance review. We've built around the approval cycle, not against it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Lilly long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 2
    story.extend(email_pair(
        "Maya Reyes", "Senior Marketing Manager", "Karuna Therapeutics",
        "Pharma. Trigger: Karuna Therapeutics posted an open Senior Video Editor role.",
        "before you hire",
        """Hi Maya,

Saw Karuna Therapeutics is hiring a Senior Video Editor. Are you covering the launch calendar yourself until that role ramps in three months?

Brand teams at Ontada use us instead of hiring. The launch ships on cadence through every search, no one apologizes for video in standup, and the brand stays consistent without daily babysitting. No ghosting, no ramp gap.

Worth a look for Karuna?""",
        """Almost every team we work with came to us after a freelancer ghosted mid-campaign. The pattern is consistent enough we built the model around it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Karuna long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 3
    story.extend(email_pair(
        "David Chen", "Senior Brand Director", "BMS Hematology",
        "Pharma. Trigger: BMS Hematology's abstract was accepted for ASCO next month.",
        "before asco",
        """Hi David,

Saw BMS Hematology's abstract accepted for ASCO next month. Are the launch teaser, day-of cuts, and recap series queued for legal yet, or is the brand team starting the build the week of?

The team at Janssen runs congress content through us. The full set ships in time, the brand voice stays consistent across all three audiences, and no one chases the editor for the day-of clip. Regulatory-aware from day one.

Worth a 15-minute walkthrough?""",
        """Most pharma teams sit on long-form for weeks because the repurposing cycle keeps colliding with med-legal review. We've built the workflow around that constraint.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing BMS long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 4
    story.extend(email_pair(
        "Sarah Lee", "Senior Marketing Director", "Sage Therapeutics",
        "Pharma. Trigger: Sage Therapeutics published the Phase III readout.",
        "after the readout",
        """Hi Sarah,

Saw Sage Therapeutics just published the Phase III readout. Is the pre-launch content already queued, or are advisory boards, MOA explainers, and KOL cuts about to hit med-legal at the same time?

Brand teams at Ontada run pre-launch content through us. The six-week cycle shrinks to two and the team ships without the firefights. Built for med-legal review.

Open to a 15-minute walkthrough?""",
        """Enterprise teams usually come to us after a vendor couldn't survive legal and brand-compliance review. We've built around the approval cycle, not against it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Sage long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 5
    story.extend(email_pair(
        "Jessica Park", "VP Marketing", "Karyopharm Therapeutics",
        "Pharma. Trigger: Karyopharm uploaded a 38-minute KOL interview to YouTube with no short-form derivative.",
        "your interview, untouched",
        """Hi Jessica,

Saw Karyopharm's recent KOL interview on the brand channel. 38 minutes on YouTube, no shorter cuts anywhere. Is the short-form derivative queued, or has med-legal review killed the repurposing cadence again?

Brand teams at Janssen run KOL repurposing through us. One long-form becomes 5 to 10 branded short-form pieces and the LinkedIn cadence holds without the rebrief cycle. Compliance-aware from day one.

Worth a look for Karyopharm?""",
        """Most pharma teams sit on long-form for weeks because the repurposing cycle keeps colliding with med-legal review. We've built the workflow around that constraint.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Karyopharm long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 6
    story.extend(email_pair(
        "Daniel Hwang", "VP Marketing", "Inozyme Pharma",
        "Biotech. Trigger: Inozyme Pharma closed Series C funding last month.",
        "after the raise",
        """Hi Daniel,

Saw Inozyme Pharma just closed Series C. Are the launch teasers, investor updates, recruiting content, and KOL clips all about to land on the same week without a production team ramped up?

Brand teams at Ontada use us through funding cycles like this. Creative supply scales with the calendar and the CMO doesn't ask why the recap is late. No ramp time.

Open to a 15-minute walkthrough?""",
        """Most growth-stage teams come to us after a quarter where creative supply couldn't keep up with the calendar. Hiring takes too long, vendors collapse under volume.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Inozyme long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # ---- How your buyers talk ----
    story.append(H("How your buyers talk"))
    story.append(LEAD("When clients describe what brought them to Viral, they don't talk like marketers. They talk like people whose week just broke."))
    story.append(P("We use their exact words in the poke-the-bear question and the pain framing. The phrasing is theirs, not ours."))

    story.append(H2("Operational pain (marketing manager and growth marketer)"))
    story.append(P("Ghosted. Dropped the ball. Off brand. Inconsistent. Unreliable. Another fire drill. I'm drowning. Out of bandwidth. We keep starting over. The last batch was rough. I just need someone I can trust. We can't scale this. I need a real team, not a freelancer."))

    story.append(H2("Enterprise pharma pain (senior marketing director at subsidiary)"))
    story.append(P("Approval friendly. On brand at scale. We can't have surprises. Six-week cycle. Med-legal review. Regulatory pass. Brand compliance audit. Missed redaction. Legal flag."))

    story.append(P("These are the pain lines. They're not adjectives we'd pick; they're sentences your clients have already said to you. The poke-the-bear question of every Email 1 above pulls from this list."))

    story.append(PageBreak())

    # ---- What's in every email ----
    story.append(H("What's in every email"))
    story.append(LEAD("A condensed reference for the rules every email respects."))
    rules = [
        "Sixty to one hundred words. Past one hundred, you lose the buyer.",
        "Subject is two to four words, lowercase, anchored to something specific the prospect owns.",
        "No em dashes. Use sentence breaks or commas instead.",
        "No exclamation marks. Brand voice is calm and confident.",
        "No dollar symbols. Pricing belongs on the call, not in cold copy.",
        "No \"free.\" We use \"on us\" or \"complimentary.\"",
        "No bracket placeholders in the final render.",
        "No sign-off in the body. EmailBison's signature variable handles \"Best, [Name].\"",
        "No apologetic PS. \"If this isn't a fit\" reads insecure. Calm and confident only.",
        "No in-body taglines. Brand lines live in the signature.",
        "Email 1 ends at the call to action. Nothing follows it.",
        "Email 2 lands the magnet offer: \"Interested in 5 short-form cuts from one of your existing long-forms? (on us)\"",
        "Case study is always pharma or healthcare. Janssen or Ontada for v1.",
        "Solution leads with benefits and results, not features. Features only when directly tied to a measurable outcome.",
    ]
    for r in rules:
        story.append(B(r))

    story.append(Spacer(1, 0.2*inch))
    story.append(P("Three more notes worth flagging."))
    story.append(P("Pricing is the one item still open. The default position is that we don't put numbers in cold copy because pricing belongs on the discovery call. If you want it included, we'll test it as a variant after the first month of sends."))
    story.append(P("Sender persona is a separate decision. We need to spin up a Viral-branded sender (name, signature, NYC office address, phone number) before the first send. Missing phone or address triggers scam suspicion, especially on a new domain."))
    story.append(P("The lead magnet workflow has to be operational before the first email ships. When a prospect replies to Email 2 asking for the five cuts, the team needs to deliver inside forty-eight hours. That's the conversion moment, and it lives outside this document."))

    doc.build(story, onFirstPage=cover_only, onLaterPages=page_footer)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()
