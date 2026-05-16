#!/usr/bin/env python3
"""
Viral Ideas Marketing — Outbound Email System (client-facing PDF).

Written for Dave Feinman and Zach Medina as the deliverable that captures the
strategy, signals, structure, and the exact emails we'd send.

No internal benchmarks. No external references to other systems. Prose-driven
voice, written as if briefing the client in person.
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
                             "Two funnels. Eleven buying signals.")
    canvas.drawCentredString(LETTER[0]/2, LETTER[1]-5.3*inch,
                             "The exact emails we plan to send.")
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

def email_pair(name, role, company, funnel_note, subject1, body1, subject2, body2):
    """Render one prospect's Email 1 + Email 2 with context note."""
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

    # Cover
    story.append(PageBreak())

    # ---- What this is ----
    story.append(H("What this is"))
    story.append(LEAD("The outbound system we're building for Viral, captured in one document."))
    story.append(P("Two funnels because your buyers want different things. Eleven buying signals because outbound that ignores triggers wastes everyone's time. Six full emails so you can see exactly what we plan to send before we send it."))
    story.append(P("You should be able to read this end to end in fifteen minutes. The six emails in the middle are the heart of it. Everything else explains why those emails look the way they do."))
    story.append(Spacer(1, 0.15*inch))
    story.append(P("Three things to flag up front. Pricing stays off cold email until we agree it shouldn't. The free five-cut repurposing pack is the lead magnet we offer in the follow-up. And every email ends at the call to action, with no sign-off in the body, because Viral's email signature handles the rest."))

    story.append(PageBreak())

    # ---- The two funnels ----
    story.append(H("The two funnels"))
    story.append(LEAD("Outbound for Viral splits into two motions because your buyers operate in different worlds."))

    story.append(H2("Funnel A &mdash; Half-Time, $2,500 a month"))
    story.append(P("Built for two in-house buyers. The first is the mid-market marketing manager, the Sierra Bowman shape: she runs a one-to-three person team inside a fifty to five hundred million revenue company, signs off on five to ten thousand a month herself, and is personally on the hook every time video shows up off-brand in a Monday standup. The second is the growth marketer at a funded startup, the Lindsey McKone shape: VC or PE backed company, five to fifty million in revenue, weekly creative testing, paid social budget, fourteen-day refresh cycle that should have been five."))
    story.append(P("The hook for Funnel A is operational. Save the week. Stop being the bottleneck. The CMO stops asking about video. The freelancer who ghosted last quarter doesn't get to set the calendar."))

    story.append(H2("Funnel B &mdash; Full-Time, $4,760 a month"))
    story.append(P("Built for the agency owner, the Daniel Rahmon shape: founder or CEO of a five to fifty million revenue marketing or content agency, thirty to a hundred and fifty staff, retention is the whole job. Different math from Funnel A. Agencies don't have a CMO problem; they have a margin problem. Every account they lose is margin lost. Every full-time editor they hire is dead weight on slow weeks."))
    story.append(P("The hook for Funnel B is structural. White-label production. Dedicated editor per account who sits inside the client's Slack channel under the agency's brand. The client never knows a vendor exists. The agency's renewal book gets cleaner."))

    story.append(H2("And two we win when they come to us"))
    story.append(P("Brittany at Ontada and Adam at Asset Map are the enterprise pharma director and the eight-year-tenure founder, respectively. They're opportunistic plays. We win them when they walk in, but we're not spending paid budget chasing them. They get a third, lighter track."))

    story.append(PageBreak())

    # ---- How we find prospects ----
    story.append(H("How we find prospects"))
    story.append(LEAD("Signal-first sourcing. We don't blast to everyone in healthcare or every agency in the country. We find prospects in the middle of a buying moment and write to that moment."))
    story.append(P("The signal logic runs in priority order. Strongest signal fires first; the rest of the cascade only runs if no higher-priority signal is found. For a pharma or biotech lead, we check pharma-specific signals first and fall through to the universal set. For any other lead, we run the universal set directly."))

    story.append(H2("Pharma-specific signals"))
    pharma_signals = [
        ["Signal", "What we look for", "Window"],
        ["FDA approval or new indication", "Drugs@FDA, FDA press releases, company 8-K filings", "Last 90 days"],
        ["Clinical trial milestone", "ClinicalTrials.gov status updates, Phase III readouts, primary endpoint announcements", "Last 90 days"],
        ["Upcoming medical congress", "Accepted abstracts, posters, symposia at ASH, ASCO, AHA, ESMO, AAD, BIO, JPM Healthcare", "Next 60 days"],
        ["Currently using a named pharma video agency", "Agency-of-record credits, press releases, LinkedIn employee bios", "Verified in last 12 months"],
    ]
    story.append(make_table(pharma_signals, [1.7*inch, 4.0*inch, 1.0*inch]))

    story.append(H2("Universal signals"))
    universal_signals = [
        ["Signal", "What we look for", "Window"],
        ["Open job posting for a video, content, or production role", "LinkedIn Jobs and Indeed listings", "Last 30 days"],
        ["Freelance editor publicly open to work after recent client engagement", "LinkedIn open-to-work flag plus prior project history with the target", "Last 30 days"],
        ["New marketing, brand, or content leader hired", "LinkedIn \"started new position\" with target company and a marketing or content title", "Last 90 days"],
        ["Underutilized long-form footage on brand channel", "Brand YouTube or Vimeo with a fifteen-plus minute video and no short-form derivative on LinkedIn or Instagram", "Last 120 days"],
        ["Image-heavy LinkedIn brand page", "Corporate page posting weekly with fewer than three videos in the window", "Last 120 days"],
        ["Recent growth, expansion, or new client win announcement", "Company LinkedIn brand posts, press releases, newsroom pages", "Last 90 days"],
        ["Recent funding or growth milestone", "Crunchbase, TechCrunch, BioPharma Dive, Endpoints News", "Last 90 days"],
        ["Agency RFP for video editing partners (Funnel B)", "Public RFP posts on LinkedIn or agency-specific job boards", "Last 30 days"],
        ["Quarterly renewal-cycle boundary (Funnel B)", "Calendar trigger at end of each quarter", "Continuous"],
        ["Lead's most recent LinkedIn activity (guaranteed fallback)", "Profile activity tab for any post, comment, or repost", "Last 30 days"],
    ]
    story.append(make_table(universal_signals, [2.0*inch, 3.7*inch, 1.0*inch]))

    story.append(PageBreak())

    # ---- The email sequence ----
    story.append(H("The email sequence"))
    story.append(LEAD("Two emails per prospect. Same thread."))
    story.append(P("The first email teases the product. The second offers the lead magnet."))

    story.append(H2("Email 1 has four moves"))
    story.append(B("<b>The trigger.</b> One sentence on what we observed about the prospect. The address of their listing, the role they're hiring, the announcement they made. Specific."))
    story.append(B("<b>The pain.</b> One paragraph in their own words on what hurts. The freelancer ghosted. The brief intake got sloppy. The renewal cycle has a client flagging video."))
    story.append(B("<b>The solution.</b> One paragraph that names a real client, a specific workflow step, the SLA, the tool, and the QA gate. The kind of detail only Viral can say."))
    story.append(B("<b>The call to action.</b> A soft yes-no for most signals (\"Worth a look for [their company]?\"). A diagnostic offer for high-commitment signals (\"Open to a 15-minute diagnostic?\")."))
    story.append(P("The email ends at the call to action. No \"Cheers, Sarah.\" No tagline. EmailBison's signature variable handles the sign-off."))

    story.append(H2("Email 2 lands the magnet"))
    story.append(P("Sent three to five days after Email 1, same thread. Opens with a short paragraph drawing the pattern from our case files (\"Almost every team we work with came to us after a freelancer ghosted mid-campaign\"). One sentence describing what Viral physically does. And the offer:"))
    story.append(LEAD("\"Interested in 5 short-form cuts from one of your existing long-forms? (on us)\""))
    story.append(P("That offer is the door. When a prospect says yes, we send the cuts inside five business days, branded and captioned, ready to post. The cuts are how the conversation starts, not how it ends. After delivery, the diagnostic call comes naturally."))

    story.append(PageBreak())

    # ---- Subject lines ----
    story.append(H("Subject lines"))
    story.append(LEAD("Two to four words, lowercase, built to create a small curiosity gap."))
    story.append(P("Four patterns work. The first three are the workhorses; the fourth is for time-specific moments."))

    subj_rows = [
        ["Pattern", "What it does", "Examples"],
        ["<b>Before [their action]</b>", "Hints at an alternative they haven't considered",
         "<font face='Courier'>before you hire</font>, <font face='Courier'>before the hire</font>"],
        ["<b>After [their event]</b>", "Implies and-now-what",
         "<font face='Courier'>after the raise</font>, <font face='Courier'>after the approval</font>, <font face='Courier'>after the win</font>"],
        ["<b>Their [thing], [twist]</b>", "Possessive with an intriguing modifier",
         "<font face='Courier'>your q4 book</font>, <font face='Courier'>your freelancer gap</font>, <font face='Courier'>your interview, untouched</font>"],
        ["<b>Time-bound reference</b>", "Names the window the prospect is in",
         "<font face='Courier'>first 90 days</font>, <font face='Courier'>six week sprint</font>"],
    ]
    story.append(make_table(subj_rows, [1.6*inch, 2.6*inch, 2.5*inch]))

    story.append(P("Things we avoid: urgency words (now, closing, last chance), hype words (revolutionary, game-changing, world-class), and generic placeholders (quick question, video editing services). Your brand voice is calm and confident; the subject line is the first place a prospect tests whether we know that."))

    story.append(PageBreak())

    # ---- What makes a solution strong ----
    story.append(H("What makes a solution strong"))
    story.append(LEAD("The solution paragraph is the part most cold emails miss."))
    story.append(P("A weak solution lists features. Dedicated editor, fast drafts, good QA. Every subscription editing service in the category says some version of that. Nothing about it tells the reader why Viral instead of any other vendor at the same price."))
    story.append(P("A strong solution does three things in three sentences. First, it names a real client and how they specifically use Viral &mdash; output volume, channel, deliverable type. \"Self Financial runs their video through our pod\" beats \"we work with Fortune 500s.\""))
    story.append(P("Second, it names a workflow step or a measurable outcome. The editor learned the brand from the kit handoff. The editor was catching drift by video three. A six-week cycle shrank to two. New ad variants ship twice a week. These sentences are not feature claims. They're observable details from how Viral actually delivers, the kind of thing a competitor can't just copy."))
    story.append(P("Third, it names the SLA, the tool, and the QA gate. Drafts back in twenty-four hours through Frame.io with timestamped notes. Every cut clears a Project Manager QC pass before it ships. The editor sits inside the client's Slack channel under the agency's brand. Named workflow elements beat adjectives every time."))
    story.append(P("The test we apply when we write a solution: if a sentence could be said by any subscription editing service, we replace it. Strong solutions name what only Viral could name."))

    story.append(PageBreak())

    # ---- Six emails ----
    story.append(H("Six emails we'd send today"))
    story.append(LEAD("What follows is six prospect pairs. The trigger, the email, the follow-up."))
    story.append(P("Names and companies are illustrative. The structure and copy are ready. If you want to swap a case study or a phrase, this is the page to mark up."))

    story.append(PageBreak())

    # Prospect 1
    story.extend(email_pair(
        "Maya Reyes", "Senior Marketing Manager", "Step",
        "Funnel A. Trigger: open video editor job posting last week.",
        "before you hire",
        """Hi Maya, saw Step is hiring a Video Editor. Most of our clients came to us right after a freelancer ghosted before a launch or a quarterly review. The math on hiring full-time usually doesn't survive a slow quarter either.

Self Financial runs their video through our pod. The editor learned the brand from the kit handoff and was catching brand drift by video 3. Drafts back in 24 hours through Frame.io with timestamped notes, every cut clears a Project Manager QC pass before it ships.

Worth a look for Step?""",
        "before you hire",
        """Almost every team we work with came to us after a freelancer ghosted mid-campaign. The pattern is consistent enough we built the model around it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, ready to post on LinkedIn or YouTube.

Interested in 5 short-form cuts from one of your existing Step long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 2
    story.extend(email_pair(
        "Tom Diaz", "Head of Growth", "Mercury",
        "Funnel A. Trigger: Mercury closed Series C last quarter.",
        "after the raise",
        """Hi Tom, congrats on Mercury's Series C last quarter. The 90 days after a round usually mean creative supply becomes the bottleneck. Sales enablement, paid ads, recruiting content, and investor updates all need video at once, and hiring takes too long.

Gainbridge, the growth team inside Group 1001 with about 160 billion in AUM, runs their paid-creative testing through our pod. New ad variants ship twice a week. Hook and retention feedback baked into every test, so the editor knows what scored before shipping the next.

Open to a 15-minute diagnostic?""",
        "after the raise",
        """Most growth teams that come to us have run paid for a quarter on a 14-day refresh cycle that should have been 5. The vendor couldn't keep up.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, ready for paid or organic.

Interested in 5 short-form cuts from one of your existing Mercury long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 3
    story.extend(email_pair(
        "Sarah Chen", "CEO", "Anomaly",
        "Funnel B. Trigger: open Senior Video Editor job posting at the agency.",
        "before the hire",
        """Hi Sarah, saw Anomaly is hiring a Senior Video Editor. Most agencies that come to us tried to hire their way out and the math broke. A full-time editor is dead weight on slow weeks, and the brand calendar doesn't pause while you ramp.

Clever Digital Marketing, a Canadian agency running about 80 staff, runs our team behind their accounts white-label. The editor sits inside each client's Slack under their brand. Same-day first drafts on Full-Time, revisions in Frame.io, every cut clears the account lead's QC pass before going client-facing.

Worth a look for Anomaly?""",
        "before the hire",
        """Most agencies come to us after a vendor that survived strategy meetings but missed the client deliverable date. The math at signup stops working by month three.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, ready to deliver under your label.

Interested in 5 short-form cuts from one of your existing client long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 4
    story.extend(email_pair(
        "Jessica Park", "VP Marketing", "Cala Health",
        "Funnel A. Trigger: Jessica started as VP Marketing six weeks ago.",
        "first 90 days",
        """Hi Jessica, congrats on the VP Marketing start at Cala Health. First 90 days for most marketing leaders means an audit of the content stack while the calendar keeps moving. The brief intake usually gets sloppy and video falls behind first.

Self Financial runs their content production through our pod for exactly this. Brand kit captured on call one, locked into a templates library the editor pulls from. By video 3, the editor was catching brand drift before their marketing lead saw it. First drafts back in 24 hours.

Worth a look for Cala?""",
        "first 90 days",
        """The most common story we hear is great first month, quality slip by month four. Usually that means the vendor scaled the account through a pool. We don't run pools.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, ready to post.

Interested in 5 short-form cuts from one of your existing Cala Health long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 5
    story.extend(email_pair(
        "Rachel Park", "Senior Marketing Director", "Eli Lilly Oncology",
        "Opportunistic enterprise pharma. Trigger: FDA approval at Lilly Oncology last month.",
        "after the approval",
        """Hi Rachel, congrats on the FDA approval at Lilly Oncology last month. Most enterprise launches need approval-friendly volume that survives legal review on the first pass. Most vendors don't survive enterprise governance.

Ontada, the McKesson healthcare-data subsidiary, runs their HCP and clinical-trial cuts through our pod. By the third project, the editor learned the compliance pattern: how their legal team flags claims, how their brand team catches color and font misuse, what triggers a redaction. A six-week cycle shrinks to two.

Open to a 15-minute diagnostic?""",
        "after the approval",
        """Enterprise teams usually come to us after a vendor couldn't survive legal and brand-compliance review. We've built around the approval cycle, not against it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Lilly long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # Prospect 6
    story.extend(email_pair(
        "Marcus Webb", "COO", "Sage Communications",
        "Funnel B. Triggers stacked: new client win announcement plus end-of-Q4 renewal cycle.",
        "your q4 book",
        """Hi Marcus, saw Sage just announced the new client win. Most agencies hitting Q4 with new accounts and an in-house team already at capacity see existing clients start asking pointed questions about turnaround.

Clever Digital Marketing runs our team behind five of their accounts white-label. The editor learned each client's brand from the kit handoff and was catching brand drift by the third project. Same-day first drafts on Full-Time, Slack response inside the hour, every cut clears the account lead's QC pass before going client-facing.

Their renewal book got cleaner. Clients never knew.

Worth a look for Sage?""",
        "your q4 book",
        """Most agencies that come to us have a renewal book with one or two accounts flagging video as a churn risk. The vendor scaled the team through a pool. We don't.

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, ready to deliver under your label.

Interested in 5 short-form cuts from one of your existing client long-forms? (on us)"""
    ))

    story.append(PageBreak())

    # ---- How your buyers talk ----
    story.append(H("How your buyers talk"))
    story.append(LEAD("When clients describe what brought them to Viral, they don't talk like marketers. They talk like people whose week just broke."))
    story.append(P("We use their exact words in the pain paragraph of Email 1. Those words make the prospect feel seen, not pitched. The phrasing is theirs, not ours."))

    story.append(H2("Words every buyer uses"))
    story.append(P("Ghosted. Dropped the ball. Off brand. Inconsistent. Unreliable. Another fire drill. I'm drowning. Out of bandwidth. We keep starting over. The last batch was rough. I just need someone I can trust. We can't scale this. I need a real team, not a freelancer."))

    story.append(H2("Words agencies use"))
    story.append(P("White-label. Dedicated editor. We need someone who can ramp without us teaching them everything. The client noticed."))

    story.append(H2("Words enterprise marketers use"))
    story.append(P("Approval friendly. On brand at scale. We can't have surprises."))

    story.append(P("These are the pain lines. They're not adjectives we'd pick; they're sentences your clients have already said to you. The pain paragraph of every Email 1 above pulls from this list."))

    story.append(PageBreak())

    # ---- What's in every email ----
    story.append(H("What's in every email"))
    story.append(LEAD("A condensed reference for the rules every email respects."))
    rules = [
        "Fifty to one hundred words. Past one hundred, you lose the buyer.",
        "Subject is two to four words, lowercase, anchored to something specific the prospect owns.",
        "No em dashes. Use sentence breaks or commas instead.",
        "No exclamation marks. Brand voice is calm and confident.",
        "No dollar symbols. Pricing belongs on the call, not in cold copy.",
        "No \"free.\" We use \"on us\" or \"complimentary.\"",
        "No bracket placeholders in the final render. Every variable resolved before send.",
        "No sign-off in the body. EmailBison's signature variable handles \"Best, [Name].\"",
        "No apologetic PS lines. \"If this isn't a fit\" reads insecure. Calm and confident only.",
        "No in-body taglines. Brand lines live in the signature.",
        "Email 1 ends at the call to action. Nothing follows it.",
        "Email 2 lands the magnet offer: \"Interested in 5 short-form cuts from one of your existing long-forms? (on us)\"",
        "Funnel-matched case study every time. Self Financial or Gainbridge for Funnel A. Clever Digital for Funnel B. Ontada or Asset Map for opportunistic plays.",
    ]
    for r in rules:
        story.append(B(r))

    story.append(Spacer(1, 0.2*inch))
    story.append(P("Three more notes worth flagging."))
    story.append(P("Pricing is the one item still open. The default position is that we don't put numbers in cold copy because pricing belongs on the discovery call. If you want it included, we'll test it as a variant in healthcare first."))
    story.append(P("Sender persona is a separate decision. We need to spin up a Viral-branded sender (name, signature, NYC office address, phone number) before the first send. This is the single biggest trust signal in the entire system; missing it triggers scam suspicion, especially on a new domain."))
    story.append(P("The lead magnet workflow has to be operational before the first email ships. When a prospect replies to Email 2 asking for the five cuts, the team needs to deliver inside forty-eight hours. That's the conversion moment, and it's the one piece of the system that lives outside this document."))

    doc.build(story, onFirstPage=cover_only, onLaterPages=page_footer)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()
