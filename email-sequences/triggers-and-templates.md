# Viral Ideas Marketing — Triggers & Email Templates

_Last updated: 2026-05-12_
_Owner: Outreach Magic / Kinetyca_
_Status: v1 — ready for client approval before launch_

---

## What This Is

The complete signal taxonomy and email template system for Viral Ideas Marketing outbound. Modeled on the live structure of BIGVU's Campaign 198 (2.0% reply rate, 40 interested replies across 25K sends). The structure is intentionally simple, the variable is the trigger line.

The system uses **two signal-finding prompts** that run in priority order:

- **Prompt A — Pharma-specific** (run first for pharma/biotech/healthcare leads)
- **Prompt B — Universal** (run for all leads; fallback for pharma leads where Prompt A finds nothing)

For agency or fintech leads, skip Prompt A entirely and run Prompt B.

Each signal produces a different **Email 1 trigger line**. The rest of Email 1 stays identical. Email 2 is the lead-magnet pivot (free 5-cut repurposing pack) and is the same across all signals.

---

## Signal Mix

### Prompt A — Pharma-Specific Signals

Run first when the lead is in pharma, biotech, healthcare, med device, or pharma-adjacent industries. Stop at first match.

| # | Signal | Recency window | What to look for |
|---|--------|----------------|-------------------|
| A1 | **FDA approval / new indication / new device approval** | last 90 days | Drugs@FDA, FDA press releases, BioPharma Dive, FiercePharma, company press releases, SEC 8-K filings |
| A2 | **Clinical trial milestone / Phase III readout / endpoint announcement** | last 90 days | ClinicalTrials.gov, company press releases, biopharma trade press |
| A3 | **Upcoming medical congress with accepted abstract / poster / symposium** | next 60 days | Conference programs and late-breaker lists: ASH, ASCO, AHA, ESMO, AAD, ACR, AAOS, BIO, JPM Healthcare, ENDO, DDW |
| A4 | **Currently using a named pharma video agency of record** | verified in last 12 months | Case study credits, press releases, LinkedIn employee bios. Agencies to flag: Klick Health, Razorfish Health, Ogilvy Health, EVERSANA, Greater Than One, Real Chemistry, FCB Health, Saatchi & Saatchi Wellness, Havas Health & You, McCann Health |

If no signal found → fall through to Prompt B.

### Prompt B — Universal Signals (works across pharma, agencies, fintech)

Run for ALL leads. Stop at first match.

| # | Signal | Recency window | Approx hit rate | Where to look |
|---|--------|----------------|-----------------|---------------|
| B1 | **Open job posting for video / content / marketing production role** | last 30 days | ~15-25% | LinkedIn Jobs, Indeed. Title contains "Video," "Multimedia," "Motion," "Content Producer," "Video Editor" |
| B2 | **New marketing / brand / content leader hired** | last 90 days | ~20-30% | LinkedIn "Started new position" + vertical filter + marketing/content/brand titles |
| B3 | **Underutilized long-form footage on brand channel** (15+ min video, no <2-min cuts on social) | last 120 days | ~50-70% | YouTube / Vimeo brand channels, cross-check LinkedIn + Instagram for derivative cuts |
| B4 | **Image-heavy LinkedIn brand page** (fewer than 3 videos in 120 days) | last 120 days | ~60-80% | Company LinkedIn page post feed; count video vs image/text posts |
| B5 | **Recent company growth / expansion announcement** (any "we just X" post) | last 90 days | ~25-40% | Company LinkedIn brand page, press releases, "Newsroom" pages |
| B6 | **Recent funding / growth milestone** | last 90 days | ~10-25% (vertical-dependent) | Crunchbase, TechCrunch, BioPharma Dive, Endpoints News |
| B7 | **Lead's most recent personal LinkedIn activity** (guaranteed fallback) | last 30 days | ~85-95% | Lead's LinkedIn profile activity tab |

---

## Email 1 — Template

The trigger line is the variable. Everything else stays the same across all signals.

```
Subject: [trigger-anchored 2-4 word lowercase subject]

Hi [First Name],

[TRIGGER — specific observation about the prospect, tied to the signal that fired].

[PAIN — what specifically hurts about this situation. Granted to the trigger.]

[SOLUTION — what Viral concretely does to fix the pain. Specific and verifiable.]

Worth a quick look?

Cheers,

[Sender]
Viral Ideas Marketing
```

**Word target:** 70-85 words. **No em dashes. No exclamation marks. No spam words. No bracket placeholders in the final render. No apologetic PS. Sign-off is signature only — no in-body taglines.**

The trigger, pain, and solution all change based on the signal that fired. The rest of the structure (greeting, CTA, sign-off) stays identical.

---

## Trigger → Pain → Solution Library by Signal

This is the working library. For each signal, the table provides:
- The **subject line** pattern
- The **trigger line** (Line 1 — what we observed)
- The **pain line** (Line 2 — what specifically hurts, tied to the trigger)
- The **solution line** (Line 3 — what Viral does about it, specific and verifiable)

### Prompt A — Pharma signals

| Signal | Subject | Trigger | Pain | Solution |
|---|---|---|---|---|
| **A1** FDA approval | `[drug] launch` | "Congrats on the FDA approval for [Drug] last [Month]." | "Launch quarters compress six weeks of HCP intros, sales enablement, and KOL content into med-legal at the same time. In-house production rarely scales fast enough for that sprint." | "Viral runs the editing team for your launch quarter. One dedicated editor across all assets, managing editor on regulatory QA, brief-on-the-first-try workflow that cuts revisions roughly in half." |
| **A2** Clinical trial readout | `[trial] readout` | "Saw the [Trial Name] Phase III readout from [Company] last [Month]." | "The 90 days between readout and launch usually means advisory board summaries, MOA explainers, and KOL interview cuts all queuing through med-legal at once. Each cycle adds 2-3 weeks to the next deliverable." | "Viral runs the pre-launch content backlog as one workflow. Same dedicated editor every week, managing editor catches regulatory issues before they reach your desk, finished cuts in days not weeks." |
| **A3** Medical congress | `[conference] content` | "Saw [Company]'s team is presenting at [Conference] next month." | "Congress content has a hard deadline and three different audiences: HCP attendees, KOLs, and the field team. Most brand teams over-spec the deliverable count and under-deliver on quality." | "Viral builds the launch teaser, day-of clips, and recap series as one workflow with one editor. Brand voice stays consistent across all three audiences, regulatory QA baked in." |
| **A4** Named pharma agency | `agency overflow` | "Saw [Company] credits [Agency] on the [Drug] work." | "Lead agencies are built for strategy and tentpole productions. The volume editing underneath usually bottlenecks at the agency's hourly rate, and switching agencies mid-launch is too risky." | "Viral plugs in as the editing layer underneath the lead agency, taking high-volume cuts off their plate. The agency keeps strategy and tentpole work, you get launch-quarter throughput without the rate spike." |

### Prompt B — Universal signals

| Signal | Subject | Trigger | Pain | Solution |
|---|---|---|---|---|
| **B1** Video / content job posting | `video specialist hire` | "Saw [Company] is hiring a [Role Title] for the [Team] team." | "Full-time editors take 60-90 days to source, ramp, and reach productive output. The brand calendar doesn't pause while you hire." | "Viral's pod starts producing in week one with a dedicated editor and managing editor on QA. When the in-house hire ramps, Viral becomes the overflow layer." |
| **B2** New marketing leader | `new [role] start` | "Congrats on the [Role] start at [Company]." | "First 90 days for most marketing leaders means a content stack audit while still shipping. Most in-house teams can't both audit and produce at the same cadence." | "Viral handles the production volume during the audit so the new leader's first quarter ships on cadence. Same dedicated editor every week, brand kit captured on call one." |
| **B3** Underutilized long-form footage | `your [topic] interview` | "I saw [Company]'s recent [Topic] interview on the brand channel. [X] minutes of long-form." | "Most teams sit on long-form like this for weeks before short-form cuts ship. The production queue compounds with every derivative cut." | "Viral takes one long-form and ships 5-10 branded short-form pieces in 5 business days. Captions, brand kit, and platform-specific aspect ratios all built into the workflow." |
| **B4** Image-heavy LinkedIn | `your video gap` | "I noticed [Company] is posting [X] times a week on LinkedIn, mostly carousels and graphics." | "Image and carousel posts cap engagement at the algorithm ceiling. Adding video doubles the production load, which most in-house teams can't absorb on top of existing work." | "Viral produces the video layer on top of your existing posting cadence. Brand kit captured once, edited cuts ship weekly, no disruption to in-house workload." |
| **B5** Growth announcement | `[announcement] content` | "Saw [Company]'s [Partnership / Office / Client / Campaign] announcement." | "Announcements trigger a content sprint: launch clips, internal comms, social cuts, and a recap deck for the next board update. In-house teams rarely scale up for the sprint, so quality drops." | "Viral's pod takes the sprint deliverables off your in-house team's plate. They ship on time, you don't burn out the existing editors, brand consistency stays intact." |
| **B6** Funding round | `[series] content` | "Congrats on the [Series X]." | "Growth-stage funding usually means a creative-supply problem. Sales enablement, paid ads, recruiting content, and investor updates all need video at the same time, and hiring takes too long." | "Viral plugs in as the creative-supply layer in week one. Dedicated editor scales output as the team's needs grow, no hiring overhead, no ramp time." |
| **B7** LinkedIn activity (fallback) | `your [topic] post` | "Saw your recent LinkedIn post on [Topic]." | "Most posts that land die after 7 days on the feed. Republishing as branded short-form video extends the lifespan, but most teams don't have the production capacity to do it consistently." | "Viral turns LinkedIn posts and other written assets into branded short-form videos in days. Captions, voiceover, brand kit baked in, ready to repost across channels." |

---

## Email 1 — Filled Example (Signal B3)

```
Subject: your moa interview

Hi Brittany,

I saw Ontada's recent MOA interview on the brand channel. 38 minutes of long-form.

Most teams sit on long-form like this for weeks before short-form cuts ship. The production queue compounds with every derivative cut.

Viral takes one long-form and ships 5-10 branded short-form pieces in 5 business days. Captions, brand kit, and platform-specific aspect ratios all built into the workflow.

Worth a quick look?

Cheers,

Sarah Stanfield
Viral Ideas Marketing
```

**Word count:** 79.

---

## Email 2 — Template (Lead-Magnet Pivot)

Same thread, ~3-5 days after Email 1. Pivots from product-tease to the lead magnet offer.

```
Subject: Re: [Email 1 subject]

Hi [First Name],

[New broader observation about the company — their content cadence, recent activity, something visible. NOT a repeat of the Email 1 trigger].

Viral can turn any long-form video into a set of branded short-form cuts in days, eliminating the multi-week edit cycle most brand teams hit.

Interested in 5 short-form cuts from one of your existing long-forms? (on us)

Cheers,

[Sender]
Viral Ideas Marketing
```

**Word target:** 60-80 words.

---

## Email 2 — Filled Example

```
Subject: Re: your moa interview

Hi Brittany,

It looks like Ontada is putting out long-form content on a regular cadence — the MOA interview is one example.

Viral can turn any long-form video into a set of branded short-form cuts in days, eliminating the multi-week edit cycle most brand teams hit.

Interested in 5 short-form cuts from one of your existing long-forms? (on us)

Cheers,

Sarah Stanfield
Viral Ideas Marketing
```

**Word count:** 71.

---

## Copy Rules (Non-Negotiable)

Pulled from the 2026 Brand Book + Viral's GTM playbook. Every email must pass these checks before send.

| Rule | Why |
|------|-----|
| 50-80 words per email | Brand-book grade 8-10 reading level. Above 80 words loses the buyer. |
| Subject line: 2-4 words, lowercase, anchored to a specific prospect-owned thing | "your moa interview" beats "video production services for pharma" |
| Person and company names always capitalized | Even in lowercase subject lines |
| No em dashes | Use sentence breaks or commas |
| No exclamation marks | Brand book: calm and confident, never urgent |
| No spam words | Especially "free" — replace with "on us" |
| No bracket placeholders in final render | Every variable must be resolved before send |
| No "Best, Sender Name" inside body | Signature is handled by EmailBison `{SENDER_EMAIL_SIGNATURE}` system variable |
| No apologetic PS | "If this isn't a fit..." reads insecure. Calm and confident only. |
| No in-body taglines | Viral equivalent of BIGVU's "Be Brilliant On Camera" bug — keep brand lines in signature, not body |
| Soft yes/no CTA in Email 1 | "Worth a quick look?" beats "Want me to build a sample? 24 hours." |
| Lead magnet drops in Email 2 only | Email 1 teases the product. Email 2 offers the 5-cut pack. |

---

## Why This Structure Works (Evidence from BIGVU Campaign 198)

BIGVU has been running this exact structure for ~4 weeks at the time of writing. Stats:

- **Campaign 198:** 25,000+ sent, 285 replies (1.1%), 40 marked interested (14% positive-of-reply ratio)
- **Email 1 alone:** 156 of 270 unique replies (58% of all replies)
- **Email 2 alone:** 47 unique replies, 7 interested
- **Top-performing subject patterns:** `your [city] listing`, `new [city] listing video`, `your [topic] interview`

The same structural skeleton, dropped onto Viral's signals + Viral's lead magnet, is what this document encodes.

---

## What Changed vs Pre-Kinetyca Viral Outbound

The pre-Kinetyca outbound (David Feinman + Michael Kaneff via Lead Hunter, 32+ interested replies since 2026-01-29) has known structural flaws documented in `optimization/copy-evolution-pre-kinetyca.md`:

| Pre-Kinetyca issue | Fixed in this template |
|---|---|
| "Small video production team" — false-modesty positioning | Replaced with product-strength framing ("We help brand teams… Janssen runs their video repurposing through our editing pod") |
| Same "McKesson and Asset Map" pair in every email regardless of vertical | Vertical-matched case study per signal (Janssen/Cortechs.ai for pharma, Clever Digital for agencies, Self Financial for fintech) |
| Apologetic PS line | Removed |
| "Can I send you over some examples?" — low-conversion samples-bounce CTA | Soft yes/no in Email 1, lead magnet question in Email 2 |
| No vertical-specific trigger | Trigger line varies per signal — 11 trigger variations covering pharma + universal |
| Em dashes / hyphen-as-em-dash | Replaced with sentence breaks |
| Random multi-vertical targeting (real estate brokers, harm reduction nonprofits, dental offices) | Signals scoped to playbook ICPs only |

---

## Operational Pre-Requisites Before Launch

These must be in place before Email 1 ships:

1. **Sample delivery workflow.** When a prospect replies to Email 2 saying "yes, send the cuts," the team must be able to deliver the 5-cut pack within 24-48 hours. This is the single point in BIGVU's funnel that breaks (per Apr 30 call data — positives go cold after Calendly pivot). Viral cannot fall into the same trap.
2. **Vertical-matched case study assets.** Janssen, Cortechs.ai, Clever Digital, Self Financial — all need at least a one-paragraph proof block ready to reference. Hard outcome numbers are the playbook gap (Dave owes us "produced X edits/month for Y, cut turnaround from Z days to A days").
3. **Sender persona signature.** Name, brand, NYC location, phone number, website. Missing phone/address triggers scammer suspicion (BIGVU lesson: Beverly Amerman flagged this directly).
4. **Signal-finder prompts deployed.** Prompt A and Prompt B must be running in Clay or equivalent, with priority-ordered evaluation logic.
5. **Suppression list functional.** Negative replies, OOOs, and prior unsubscribes must feed back into Clay / EmailBison suppression. (BIGVU lesson: Dan Conlon re-emailed in May after April negative reply — brand-damaging.)

---

## Open Decisions for Dave Before Launch

These are flagged in CLAUDE.md and need resolution before campaign 1 ships:

- HVAC vs. law firms in scope?
- Outcome metrics per vertical (the case-study hard numbers we currently lack)
- Pricing transparency in cold copy ($1,500-$5,000/mo in body, or price-discovery on call?)
- SaaS / pro services in or out of first 90 days?
- Coordination with existing Lead Hunter outbound (pause, parallel, or handoff?)
- Construction / remodeling angle — kill or add?
- PR firms as a new vertical (per the recent Devine Partners reply)?

---

_Document version: v1 (2026-05-12)_
_GitHub: https://github.com/matteof123/Viral/blob/main/email-sequences/triggers-and-templates.md_
