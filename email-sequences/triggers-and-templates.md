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

[TRIGGER LINE — see trigger table below].

You're already producing the high-value content. The bottleneck is the edit cycle. [Vertical-matched named case study — Janssen / Cortechs.ai for pharma · Clever Digital for agencies · Self Financial / Gainbridge for fintech] runs their video repurposing through our editing pod.

Same dedicated editor every week, managing editor on QA, finished cuts in days.

Worth a quick look?

Cheers,

[Sender]
Viral Ideas Marketing
```

**Word target:** 70-85 words. **No em dashes. No exclamation marks. No spam words. No bracket placeholders in the final render. No apologetic PS. Sign-off is signature only — no in-body taglines.**

---

## Trigger Line Examples by Signal

The trigger is Line 1 of Email 1. Each signal produces a different trigger line. The subject line follows the same trigger pattern (2-4 words, lowercase, anchored to a specific prospect-owned thing).

### Prompt A — Pharma triggers

| Signal | Subject | Trigger line (Line 1 of Email 1) |
|---|---|---|
| **A1** FDA approval | `[drug] launch` | "Congrats on the FDA approval for [Drug]. Launch quarters typically mean six weeks of HCP intros, sales enablement, and KOL content moving through med-legal at the same time." |
| **A2** Clinical trial readout | `[trial] readout` | "Saw [Company] just published the [Trial Name] Phase III readout. The pre-launch cycle that follows usually means advisory board summaries, MOA explainers, and KOL clips queued at once." |
| **A3** Medical congress | `[conference] content` | "Saw [Company]'s team is presenting at [Conference] next month. Conference content usually splits three ways: launch teaser, day-of clips, and the recap series sales uses for the next quarter." |
| **A4** Named pharma agency | `agency overflow` | "Saw [Company] credits [Agency] on the [Drug] work. Most pharma brand teams use a lead agency for strategy and a separate pod for editing volume, especially through launch quarters." |

### Prompt B — Universal triggers

| Signal | Subject | Trigger line (Line 1 of Email 1) |
|---|---|---|
| **B1** Video / content job posting | `video specialist hire` | "I saw [Company] is hiring a [Role Title] for the [Team] team. Open production roles usually mean the brand calendar is already running ahead of the team's editing capacity." |
| **B2** New marketing leader | `new [role] start` | "Congrats on the [Role] start at [Company]. First 90 days for most marketing leaders means a content stack audit and a new cadence to ship by quarter-end." |
| **B3** Underutilized long-form footage | `your [topic] interview` | "I saw [Company]'s recent [Topic] interview on the brand channel — [X] minutes of long-form content. Brand teams that repurpose long-form into short-form usually see 5-10x more reach from the same source material." |
| **B4** Image-heavy LinkedIn | `your video gap` | "I noticed [Company] is posting [X] times a week on LinkedIn — mostly carousels and graphics. Brand teams that add video to the same posting cadence usually see 2-3x the engagement from the same audience." |
| **B5** Growth announcement | `[announcement] content` | "Saw [Company]'s [Partnership / Office / Client / Campaign] announcement. Launches like that typically trigger a content sprint — launch clips, internal comms, social cuts, and a recap deck." |
| **B6** Funding round | `[series] content` | "Congrats on the [Series X]. The 90 days that follow usually mean creative supply becomes the bottleneck — sales enablement, paid ads, and recruiting content all needed at once." |
| **B7** LinkedIn activity (fallback) | `your [topic] post` | "Saw your recent LinkedIn post on [Topic]. Posts that land usually have 5-10x the reach when republished as a short-form video with captions and a branded cut." |

---

## Email 1 — Filled Example (Signal B3)

```
Subject: your moa interview

Hi Brittany,

I saw Ontada's recent MOA interview on the brand channel — 38 minutes of long-form content. Brand teams that repurpose long-form into short-form usually see 5-10x more reach from the same source material.

You're already producing the high-value content. The bottleneck is the edit cycle. Janssen and Cortechs.ai run their HCP video repurposing through our editing pod.

Same dedicated editor every week, managing editor on QA, finished cuts in days.

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

Would you be interested in 5 short-form cuts from one of your existing long-forms? (on us)

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

Would you be interested in 5 short-form cuts from one of your existing long-forms? (on us)

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
