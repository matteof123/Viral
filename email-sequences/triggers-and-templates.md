# Viral Ideas Marketing — Triggers & Email Templates

_Last updated: 2026-05-12 (v4 — healthcare focus)_
_GitHub: matteof123/Viral_
_Owner: Outreach Magic / Kinetyca_

---

## What This Is

The outbound system for Viral Ideas, focused on healthcare and pharma for the first 90 days. Two emails per prospect:

- **Email 1** anchors a buying trigger, pokes the bear with a question that makes the prospect nod, and delivers a benefit-led solution with one case study and a defused objection.
- **Email 2** pivots to the lead magnet — a free 5-cut repurposing pack from one of their existing long-forms, sent same thread 3-5 days later.

Six rendered prospect pairs at the bottom show exactly what gets sent.

---

## Signal Mix

Ten signals, run in priority order. Stop at first match.

### Pharma-specific signals (run first)

| # | Signal | Recency |
|---|--------|---------|
| A1 | FDA approval / new indication / new device approval | last 90 days |
| A2 | Clinical trial milestone / Phase III readout | last 90 days |
| A3 | Upcoming medical congress with accepted abstract (ASH, ASCO, AHA, ESMO, AAD, BIO, JPM) | next 60 days |
| A4 | Currently using a named pharma video agency (Klick, Razorfish Health, Ogilvy Health, EVERSANA, Greater Than One, Real Chemistry, FCB Health, McCann Health) | verified in last 12 months |

### Universal signals (also healthcare-relevant)

| # | Signal | Recency |
|---|--------|---------|
| B1 | Open job posting for video / content / production role | last 30 days |
| B2 | New marketing / brand / content leader hired | last 90 days |
| B3 | Underutilized long-form footage on brand channel (15+ min, no <2-min cuts on social) | last 120 days |
| B4 | Image-heavy LinkedIn brand page (<3 videos in 120 days) | last 120 days |
| B5 | Recent growth / expansion / new client win announcement | last 90 days |
| B6 | Recent funding or growth milestone (biotech, health tech) | last 90 days |

---

## Email 1 — Structure

```
Hi {Name},

{Trigger sentence} {Poke-the-bear question}

{Solution with case study, leading with benefits and results. Defuse objection (2-5 words).}

{Soft CTA}
```

### Constraints

- 60-100 words total
- Subject line: 2-4 words, lowercase, curiosity-driven (Before/After/Their thing twist/Time-bound)
- Solution leads with **benefits and results**, not features. Features only when directly tied to a result.
- Defuse phrase: 2-5 words inside the solution, neutralizing the biggest objection at the trigger
- No em dashes. No exclamation marks. No "$" symbol. No "free" — use "on us"
- No sign-off in body. EmailBison's `{SENDER_EMAIL_SIGNATURE}` handles it.

### The Poke-the-Bear Question

The question right after the trigger should make the prospect nod silently. It names the consequence of the trigger in the buyer's own internal voice. Not "wouldn't it be nice if…" — instead, "are you about to…" or "is X already happening, or is Y about to start?"

### The Defuse (2-5 words inside the solution)

A short phrase that neutralizes the biggest objection at the trigger.

| Defuse phrase | Handles the objection |
|---|---|
| "Approval-friendly from day one" | Will they survive enterprise governance? |
| "Regulatory-aware from day one" | Do they understand compliance? |
| "Built for med-legal review" | Will they understand our review process? |
| "Compliance-aware from day one" | Can they touch HCP-targeted content? |
| "No ghosting, no ramp gap" | What if they disappear like the last freelancer? |
| "No ramp time" | Can they start fast enough to matter? |

### Subject Line Patterns

Four patterns work. 2-4 words, lowercase, curiosity-driven.

| Pattern | Examples |
|---|---|
| **Before [their action]** | `before you hire`, `before [conference]` |
| **After [their event]** | `after the approval`, `after the raise`, `after the readout` |
| **Their [thing], [twist]** | `your interview, untouched`, `your freelancer gap` |
| **Time-bound** | `first 90 days`, `six week sprint` |

Avoid: urgency (now, closing), hype (revolutionary, game-changing), generic (quick question, video editing services).

---

## Trigger → Poke → Solution Library

Each signal has its own trigger sentence, poke-the-bear question, and solution skeleton. The full case study and defuse get inserted on render.

### Pharma-specific signals

| Signal | Subject | Trigger + Poke + Solution skeleton |
|---|---|---|
| **A1** FDA approval | `after the approval` | "Saw [Company] just got the FDA approval last month. Are you about to spend six weeks pushing HCP cuts, sales enablement, and KOL interviews through med-legal at the same time?" → Janssen case + "calendar holds, CMO stops asking about video in standup" + **Approval-friendly from day one.** |
| **A2** Phase III readout | `after the readout` | "Saw [Company] just published the Phase III readout. Is the pre-launch content already queued, or are advisory boards, MOA explainers, and KOL cuts about to hit med-legal at the same time?" → Ontada case + "six-week cycle shrinks to two, team ships without the firefights" + **Built for med-legal review.** |
| **A3** Medical congress | `before [conference]` | "Saw [Company]'s abstract accepted for [Conference] next month. Are the launch teaser, day-of cuts, and recap series queued for legal yet, or is the brand team starting the build the week of?" → Janssen case + "full set ships in time, brand voice consistent across HCP/KOL/field audiences" + **Regulatory-aware from day one.** |
| **A4** Named pharma agency | `agency overflow` | "Saw [Company] credits [Agency] on the [Drug] work. Is the editing volume bottlenecking at the agency's rate during launch quarters, or are you splitting the work to a separate pod already?" → Ontada case + "agency keeps strategy, you get launch-quarter throughput without the rate spike" + **Approval-friendly from day one.** |

### Universal signals

| Signal | Subject | Trigger + Poke + Solution skeleton |
|---|---|---|
| **B1** Job posting (editor) | `before you hire` | "Saw [Company] is hiring a [Role]. Are you covering the launch calendar yourself until that role ramps in three months?" → Ontada case + "launch ships on cadence through every search, no one apologizes for video in standup, brand stays consistent without daily babysitting" + **No ghosting, no ramp gap.** |
| **B2** New marketing leader | `first 90 days` | "Congrats on the [Role] start at [Company]. Are you trying to audit the content stack while the launch calendar keeps moving?" → Ontada case + "audit runs in parallel, first quarter ships on cadence, brand kit captured on call one" + **No ramp time.** |
| **B3** Underutilized long-form | `your [topic], untouched` | "Saw [Company]'s recent [Topic] interview on the brand channel. [X] minutes on YouTube, no shorter cuts anywhere. Is the short-form derivative queued, or has med-legal review killed the repurposing cadence again?" → Janssen case + "one long-form becomes 5 to 10 branded short-form pieces, LinkedIn cadence holds without the rebrief cycle" + **Compliance-aware from day one.** |
| **B4** Image-heavy LinkedIn | `linkedin without video` | "Saw [Company] is posting [X] times a week on LinkedIn, mostly carousels and graphics. Is the in-house team trying to add video on top of existing work, or has the production lift already killed it?" → Janssen case + "video layer ships on top of existing cadence, brand kit captured once, cuts ship weekly without disrupting in-house workload" + **Built for med-legal review.** |
| **B5** Growth announcement | `after the [event]` | "Saw [Company]'s [Partnership / Office / Launch] announcement. Are the launch clips, internal comms, and recap deck about to land on the same week, or has the in-house team already scaled for the sprint?" → Ontada case + "sprint deliverables ship on time, brand stays consistent across the set, in-house team stays sane" + **No ramp time.** |
| **B6** Funding round | `after the raise` | "Saw [Company] just closed [Series X]. Are the launch teasers, investor updates, recruiting content, and KOL clips all about to land on the same week without a production team ramped up?" → Ontada case + "creative supply scales with the calendar, CMO doesn't ask why the recap is late" + **No ramp time.** |

---

## Six Rendered Examples (all healthcare/pharma)

### 1. Rachel Park, Sr. Marketing Director, Eli Lilly Oncology
**Signal A1 — FDA approval**

```
Subject: after the approval

Hi Rachel,

Saw Eli Lilly Oncology just got the FDA approval last month. Are you about to
spend six weeks pushing HCP cuts, sales enablement, and KOL interviews through
med-legal at the same time?

The team at Janssen runs launch quarters through us. The calendar holds and
the CMO stops asking about video in standup. Approval-friendly from day one.

Open to a 15-minute walkthrough for Lilly?
```

**62 words.** Defuse: "Approval-friendly from day one" (4 words).

---

### 2. Maya Reyes, Sr. Marketing Manager, Karuna Therapeutics
**Signal B1 — Open video editor hire**

```
Subject: before you hire

Hi Maya,

Saw Karuna Therapeutics is hiring a Senior Video Editor. Are you covering the
launch calendar yourself until that role ramps in three months?

Brand teams at Ontada use us instead of hiring. The launch ships on cadence
through every search, no one apologizes for video in standup, and the brand
stays consistent without daily babysitting. No ghosting, no ramp gap.

Worth a look for Karuna?
```

**68 words.** Defuse: "No ghosting, no ramp gap" (5 words).

---

### 3. David Chen, Sr. Brand Director, BMS Hematology
**Signal A3 — ASCO abstract accepted**

```
Subject: before asco

Hi David,

Saw BMS Hematology's abstract accepted for ASCO next month. Are the launch
teaser, day-of cuts, and recap series queued for legal yet, or is the brand
team starting the build the week of?

The team at Janssen runs congress content through us. The full set ships in
time, the brand voice stays consistent across all three audiences, and no
one chases the editor for the day-of clip. Regulatory-aware from day one.

Worth a 15-minute walkthrough?
```

**72 words.** Defuse: "Regulatory-aware from day one" (4 words).

---

### 4. Sarah Lee, Sr. Marketing Director, Sage Therapeutics
**Signal A2 — Phase III readout**

```
Subject: after the readout

Hi Sarah,

Saw Sage Therapeutics just published the Phase III readout. Is the pre-launch
content already queued, or are advisory boards, MOA explainers, and KOL cuts
about to hit med-legal at the same time?

Brand teams at Ontada run pre-launch content through us. The six-week cycle
shrinks to two and the team ships without the firefights. Built for med-legal
review.

Open to a 15-minute walkthrough?
```

**62 words.** Defuse: "Built for med-legal review" (4 words).

---

### 5. Jessica Park, VP Marketing, Karyopharm Therapeutics
**Signal B3 — Underutilized long-form (KOL interview)**

```
Subject: your interview, untouched

Hi Jessica,

Saw Karyopharm's recent KOL interview on the brand channel. 38 minutes on
YouTube, no shorter cuts anywhere. Is the short-form derivative queued, or
has med-legal review killed the repurposing cadence again?

Brand teams at Janssen run KOL repurposing through us. One long-form becomes
5 to 10 branded short-form pieces and the LinkedIn cadence holds without the
rebrief cycle. Compliance-aware from day one.

Worth a look for Karyopharm?
```

**68 words.** Defuse: "Compliance-aware from day one" (4 words).

---

### 6. Daniel Hwang, VP Marketing, Inozyme Pharma
**Signal B6 — Series C funding**

```
Subject: after the raise

Hi Daniel,

Saw Inozyme Pharma just closed Series C. Are the launch teasers, investor
updates, recruiting content, and KOL clips all about to land on the same
week without a production team ramped up?

Brand teams at Ontada use us through funding cycles like this. Creative
supply scales with the calendar and the CMO doesn't ask why the recap is
late. No ramp time.

Open to a 15-minute walkthrough?
```

**64 words.** Defuse: "No ramp time" (3 words).

---

## Email 2 — Template (Lead Magnet Pivot)

Same thread, 3-5 days after Email 1. Pivots to the free 5-cut repurposing pack.

```
Subject: re: [Email 1 subject]

[Broader observation drawn from the 5 reasons clients switch — see library
below].

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing [Company]
long-forms? (on us)
```

### Broader observation library

| Email 1 signal | Email 2 paragraph 1 observation |
|---|---|
| FDA approval / Phase III readout / launch sprint | "Enterprise teams usually come to us after a vendor couldn't survive legal and brand-compliance review. We've built around the approval cycle, not against it." |
| Job posting / freelancer ghosting | "Almost every team we work with came to us after a freelancer ghosted mid-campaign. The pattern is consistent enough we built the model around it." |
| New marketing leader | "The most common story we hear is great first month, quality slip by month four. Usually that means the vendor scaled the account through a pool. We don't run pools." |
| Congress / underutilized long-form | "Most pharma teams sit on long-form for weeks because the repurposing cycle keeps colliding with med-legal review. We've built the workflow around that constraint." |
| Funding / growth milestone | "Most growth-stage teams come to us after a quarter where creative supply couldn't keep up with the calendar. Hiring takes too long, vendors collapse under volume." |

### Six Rendered Email 2 Examples

```
1. Rachel at Lilly Oncology (re: after the approval)

Enterprise teams usually come to us after a vendor couldn't survive legal
and brand-compliance review. We've built around the approval cycle, not
against it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Lilly long-forms?
(on us)
```

```
2. Maya at Karuna (re: before you hire)

Almost every team we work with came to us after a freelancer ghosted
mid-campaign. The pattern is consistent enough we built the model around it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Karuna long-forms?
(on us)
```

```
3. David at BMS (re: before asco)

Most pharma teams sit on long-form for weeks because the repurposing cycle
keeps colliding with med-legal review. We've built the workflow around that
constraint.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing BMS long-forms?
(on us)
```

```
4. Sarah at Sage (re: after the readout)

Enterprise teams usually come to us after a vendor couldn't survive legal
and brand-compliance review. We've built around the approval cycle, not
against it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Sage long-forms?
(on us)
```

```
5. Jessica at Karyopharm (re: your interview, untouched)

Most pharma teams sit on long-form for weeks because the repurposing cycle
keeps colliding with med-legal review. We've built the workflow around that
constraint.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Karyopharm
long-forms? (on us)
```

```
6. Daniel at Inozyme (re: after the raise)

Most growth-stage teams come to us after a quarter where creative supply
couldn't keep up with the calendar. Hiring takes too long, vendors collapse
under volume.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Inozyme long-forms?
(on us)
```

---

## Voice of Customer Language

Use these in the poke-the-bear question and the pain framing. They're the words clients have actually said to Dave on sales calls.

**Operational pain (Sierra/Lindsey-shape buyers):**
ghosted, dropped the ball, off brand, inconsistent, unreliable, another fire drill, I'm drowning, out of bandwidth, we keep starting over, the last batch was rough, I just need someone I can trust, we can't scale this, I need a real team not a freelancer.

**Enterprise pharma (Brittany-shape buyers):**
approval friendly, on brand at scale, we can't have surprises, six-week cycle, med-legal review, regulatory pass, brand compliance audit, missed redaction, legal flag.

---

## Copy Rules (Non-Negotiable)

- 60-100 words per email (both Email 1 and Email 2)
- Subject: 2-4 words, lowercase, curiosity-driven
- Person and company names always capitalized
- No em dashes. Use sentence breaks or commas.
- No exclamation marks. Brand voice is calm and confident.
- No "$" symbol. Pricing belongs on the call, not in cold body.
- No "free" — replace with "on us"
- No bracket placeholders in the final render
- No "Best, [Name]" in body. EmailBison signature variable handles it.
- No apologetic PS. "If this isn't a fit…" reads insecure.
- No in-body taglines. Brand lines stay in signature.
- Email 1 ends at CTA. Nothing after.
- Email 2 lands the lead magnet: "Interested in 5 short-form cuts from one of your existing [Company] long-forms? (on us)"
- Case study is always healthcare/pharma — Ontada (McKesson) or Janssen for v1
- Solution leads with benefits and results, not features

---

## Operational Pre-Reqs Before Launch

1. **Sample delivery workflow.** When a prospect replies to Email 2, the team must deliver the 5 cuts within 48 hours. This is the conversion moment.
2. **Sender persona signature.** Name, brand, NYC location, phone, website. Missing phone/address triggers scam suspicion on a new domain.
3. **Signal-finder prompts deployed.** Prompt A + Prompt B in Clay or equivalent, priority-ordered.
4. **Suppression list functional.** Negatives, OOOs, prior unsubscribes feed back into Clay/EmailBison.
5. **Case study assets ready.** Ontada and Janssen — one-paragraph proof block each. Dave to backfill 2-3 hard outcome numbers per case study to strengthen the proof beyond logos-only.

---

## Open Decisions for Dave

1. **Pricing transparency in cold copy.** Currently off entirely. Recommend stay off in cold, mention on call.
2. **Hard outcome numbers per case study.** Need 2-3 numbers per Ontada and Janssen so proof beats logos-only.
3. **Sender persona.** Spin up a new Viral-branded sender with NYC location and phone number.
4. **Coordination with existing Lead Hunter outbound** (vlad@leadhunter.net). Pause, parallel, or handoff?
5. **Funnel B (agencies) and fintech timing.** Healthcare is first 90 days. When do we layer agencies in? Recommendation: validate healthcare reply rate first, then build Funnel B in week 7-8.

---

_Document version: v4 (2026-05-12) | Healthcare focus for first 90 days_
