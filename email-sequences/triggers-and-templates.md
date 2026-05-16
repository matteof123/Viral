# Viral Ideas Marketing — Triggers & Email Templates

_Last updated: 2026-05-12 (v2 — incorporates Discovery Questionnaire)_
_Owner: Outreach Magic / Kinetyca_
_Status: v2 — ready for client approval before launch_

---

## What This Is

The complete signal taxonomy and email template system for Viral Ideas Marketing outbound, rebuilt against the Discovery Questionnaire (May 2026). Structure modeled on BIGVU's Campaign 198 (2.0% reply rate, 40 interested across 25K sends).

Two parallel funnels run different copy with different case studies and different pain language:

- **Funnel A — Half-Time tier** — built for mid-market marketing managers (Sierra archetype) + growth marketers at funded startups (Lindsey archetype)
- **Funnel B — Full-Time tier** — built for agency owners and CEOs (Daniel archetype), white-label friendly

Enterprise pharma marketing directors (Brittany) and B2B founders (Adam) are **opportunistic plays, not the main paid spend**. They get their own light track.

---

## The Two Funnels

| Field | Funnel A | Funnel B |
|---|---|---|
| **Tier** | Half-Time | Full-Time |
| **Buyer archetype** | Sierra (mid-market marketing manager) + Lindsey (growth marketer at funded startup) | Daniel (agency CEO / Founder, 30-150 staff) |
| **Buyer revenue band** | $50M-$500M B2C/B2B (Sierra) · $5M-$50M startup (Lindsey) | $5M-$50M agency |
| **Volume promise** | 8-20 videos/month, first drafts in 24 hours | 30+ videos/month, same-day first drafts, white-label |
| **Trigger words to use** | "ghosted," "fire drill," "drowning," "we keep starting over," "I need a real team, not a freelancer" | "white-label," "dedicated editor," "the client noticed," "we need someone who can ramp without us teaching them everything" |
| **Case study to cite** | Self Financial (Sierra archetype) for marketing mgrs · Gainbridge for growth marketers | Clever Digital Marketing (Daniel archetype) |
| **Hook angle** | Save your week. Stop being the bottleneck. CMO stops asking about video. | Margin recovery. Renewal protection. Client never knows we exist. |
| **Email 2 broader observation** | "Most teams that come to us had a freelancer ghost mid-campaign…" | "Most agencies come to us after a vendor missed the client deliverable date…" |

**Opportunistic tracks (not main spend):**

| Archetype | Real example | Case study to cite | Hook angle |
|---|---|---|---|
| Brittany — enterprise pharma marketing director | Ontada (McKesson healthcare subsidiary) | Ontada / Janssen / J&J | "Approval friendly, on-brand at scale, no surprises in front of leadership" |
| Adam — B2B founder, established pro services / SaaS | Asset Map (VI client since 2017) | Asset Map | "Strategic partner, not just an editor. Built for compounding LTV." |

---

## Signal Mix

The signal-finding logic runs in two prompts. Both apply to both funnels — the SIGNAL is the same, but the CASE STUDY and PAIN LANGUAGE swap based on which funnel the prospect maps to.

### Prompt A — Pharma-specific signals

Run first when the lead is in pharma, biotech, healthcare, or med device. Stop at first match. If no signal found, fall through to Prompt B.

| # | Signal | Recency window |
|---|--------|----------------|
| A1 | **FDA approval / new indication / new device approval** | last 90 days |
| A2 | **Clinical trial milestone / Phase III readout / endpoint announcement** | last 90 days |
| A3 | **Upcoming medical congress with accepted abstract** (ASH, ASCO, AHA, ESMO, AAD, ACR, AAOS, BIO, JPM) | next 60 days |
| A4 | **Currently using named pharma video agency** (Klick, Razorfish Health, Ogilvy Health, EVERSANA, Greater Than One, Real Chemistry, FCB Health, Havas Health, McCann Health) | verified in last 12 months |

### Prompt B — Universal signals

Run for ALL leads. Stop at first match.

| # | Signal | Recency | Approx hit rate |
|---|--------|---------|-----------------|
| B1 | **Open job posting for video / content / marketing production role** | 30d | ~15-25% |
| B1.5 | **Freelance video editor "open to work" who lists target company as recent client** | 30d | ~5-10% (direct ghosting signal — strongest Funnel A trigger) |
| B2 | **New marketing / brand / content leader hired** | 90d | ~20-30% |
| B3 | **Underutilized long-form footage on brand channel** (15+ min video, no <2-min cuts on social) | 120d | ~50-70% |
| B4 | **Image-heavy LinkedIn brand page** (<3 videos in 120d) | 120d | ~60-80% |
| B5 | **Recent company growth / expansion / new client win announcement** | 90d | ~25-40% |
| B6 | **Recent funding / growth milestone** | 90d | ~10-25% |
| B7 | **Agency RFP / RFQ posted for video editing** (Funnel B only) | 30d | ~3-5% (strongest Funnel B trigger) |
| B8 | **Quarterly renewal-cycle boundary** (Q1/Q2/Q3/Q4 close, Funnel B only) | calendar | ~25% of agency leads/quarter |
| B9 | **Lead's most recent LinkedIn activity** (guaranteed fallback) | 30d | ~85-95% |

---

## Email 1 — Template

```
Subject: [trigger-anchored 2-4 word lowercase subject]

Hi [First Name],

[TRIGGER — specific observation about the prospect, tied to the signal that fired].

[PAIN — what specifically hurts about this situation, using VOC language from the funnel's pain word library].

[SOLUTION — what Viral concretely does to fix the pain, citing the funnel-matched case study with full identity phrase. Specific differentiators from the library, not generic claims].

Worth a look for [Company]?
```

**Word target:** 70-100 words. **No em dashes. No exclamation marks. No spam words. No bracket placeholders in final render. No apologetic PS. No in-body taglines. No sign-off, no "Cheers," no sender name — email ends at the CTA. Signature handled by EmailBison `{SENDER_EMAIL_SIGNATURE}` system variable.**

The CTA can swap depending on intent level:

- **Default:** "Worth a look for [Company]?"
- **High-commitment signal (FDA approval, funding round):** "Open to a 15-minute diagnostic?" — matches VI's Doctor Frame sales method

---

## Trigger → Pain → Solution Library by Funnel

### Funnel A — Mid-market marketing mgr (Sierra) + Growth marketer (Lindsey)

Case study to cite: **Self Financial** (Sierra archetype, B2C fintech mid-market) for marketing managers · **Gainbridge** (Lindsey archetype, growth marketer at funded startup) for growth marketers.

| Signal | Subject | Trigger | Pain | Solution |
|---|---|---|---|---|
| **B1** Job posting (editor) | `editor hire` | "Saw [Company] is hiring a Video Editor." | "Most of our clients came to us right after a freelancer ghosted before a launch or a quarterly review. The math on hiring full-time usually doesn't survive a slow quarter either." | "Self Financial runs their video through our pod. One dedicated editor brand-trained before the first project, first drafts in 24 hours, Slack response inside the hour Mon to Fri. Unlimited revisions on the first batch until the baseline is right." |
| **B1.5** Freelancer ghosting | `freelancer gap` | "Saw [Freelancer Name] just listed themselves as open to work after working with [Company]." | "Almost every team that comes to us starts with a freelancer who ghosted right before a launch. The pattern is consistent enough we built the model around it." | "Self Financial runs their video through our pod. One dedicated editor, brand-trained before video one, first drafts in 24 hours. Slack response inside the hour, no ticket portal, no edit lottery." |
| **B2** New marketing leader | `new role start` | "Congrats on the [Role] start at [Company]." | "First 90 days for most marketing leaders means an audit of the content stack while the calendar keeps moving. The brief intake usually gets sloppy and video falls behind first." | "Self Financial runs their content through our pod for exactly this. One dedicated editor brand-trained before the first project, first drafts in 24 hours, Slack response inside the hour. The audit runs in parallel and the cadence holds." |
| **B3** Underutilized long-form | `your [topic] interview` | "I saw [Company]'s recent [Topic] interview on the brand channel. [X] minutes of long-form." | "Most teams sit on long-form like this for weeks before short-form ships, because the freelancer rotation keeps starting over with every new brief." | "Self Financial runs their repurposing through our pod. One long-form becomes 5 to 10 branded short-form pieces in 5 business days. Captions, brand kit, platform-specific aspect ratios all built into the workflow." |
| **B4** Image-heavy LinkedIn | `[company] video` | "Saw [Company] is posting [X] times a week on LinkedIn, mostly carousels and graphics." | "Most teams want to add video but the production lift kills it before week three. The freelancer the team trusted last quarter is usually the bottleneck." | "Self Financial runs their video layer through our pod on top of their existing posting cadence. One dedicated editor, brand kit captured on the first call, edited cuts ship weekly." |
| **B5** Growth announcement | `[announcement]` | "Saw [Company]'s [Partnership / Office / Client / Launch] announcement." | "Announcements like that usually trigger a content sprint inside of a team that's already underwater. The CMO walks into the standup asking why the recap isn't out yet." | "Self Financial runs sprint deliverables through our pod when their in-house team is at capacity. Same dedicated editor every week, first drafts in 24 hours, no ramp time." |
| **B6** Funding (growth mkter) | `series [x] content` | "Congrats on [Company]'s Series [X] last month." | "Growth-stage rounds usually mean creative supply becomes the bottleneck. Sales enablement, paid ads, recruiting content, and investor updates all need video at once, and hiring takes too long." | "Gainbridge, the growth team inside Group 1001 with about 160 billion in assets under management, runs their paid-creative testing through our pod. One dedicated editor, first drafts in 24 hours, ships new ad variants twice a week." |
| **B9** LinkedIn activity (fallback) | `your [topic] post` | "Saw your recent LinkedIn post on [Topic]." | "Posts that land usually die after 7 days on the feed. Republishing as branded short-form extends the lifespan, but most teams don't have the production capacity to do it consistently." | "Self Financial runs their LinkedIn-to-video repurposing through our pod. Each post becomes a 60-second branded video in days, captions and brand kit baked in." |

### Funnel B — Agency CEO (Daniel)

Case study to cite: **Clever Digital Marketing** (Daniel archetype, ~$10M, ~80 staff, Canadian agency, white-label model).

| Signal | Subject | Trigger | Pain | Solution |
|---|---|---|---|---|
| **B1** Job posting (editor) | `editor hire` | "Saw [Agency] is hiring a Senior Video Editor." | "Most agencies that come to us tried to hire their way out and the math broke. A full-time editor is dead weight on slow weeks, and the brand calendar doesn't pause while you ramp." | "Clever Digital Marketing, a Canadian agency running about 80 staff, runs our team behind their accounts white-label. Same editor every week, same-day first drafts on Full-Time, Slack response inside the hour. The cuts go out under their brand." |
| **B5** New client win | `[client] win` | "Saw [Agency] just announced the [Client] win." | "New accounts pile onto an in-house editing team that's already at capacity. The existing accounts start asking pointed questions about turnaround." | "Clever Digital Marketing runs our team behind five of their accounts white-label. Same-day first drafts, dedicated editor per account, Slack response inside the hour. Their renewal book got cleaner. The clients never knew." |
| **B7** Agency RFP for video | `video rfp` | "Saw [Agency]'s RFP for video editing partners." | "Most agencies post the RFP because the current vendor's quality dropped when volume scaled. The brand stopped looking like the brand, and the client noticed." | "Clever Digital Marketing runs our team white-label behind their accounts. One dedicated editor per account, same-day first drafts on Full-Time, no rotation, no quality dip when volume spikes." |
| **B8** Q4 renewal cycle | `renewal stack` | "Q4 renewal cycle approaching for [Agency]." | "Most agencies hit the renewal cycle with one or two accounts already flagging video as a churn risk. The vendor scaled the team through a pool and the brand drifted." | "Clever Digital Marketing runs our team behind five of their accounts white-label. Dedicated editor per account, same-day first drafts on Full-Time, no surprises before quarterly business reviews." |
| **B3** Underutilized long-form (agency client) | `[client] cuts` | "I saw [Agency]'s recent case-study film for [Client]. [X] minutes of long-form." | "Most agencies sit on long-form like this because cutting it for client-facing social, sales enablement, and partner-facing usually means re-briefing a freelancer who delivers off-brand by week three." | "Clever Digital Marketing runs their client repurposing through our pod white-label. One long-form becomes 5 to 10 branded short-form pieces in 5 business days. The cuts ship under the agency's brand, not ours." |

### Opportunistic — Enterprise pharma (Brittany) + B2B founder (Adam)

Case studies: **Ontada / Janssen / Johnson & Johnson** for pharma · **Asset Map** for founder-led pro services / SaaS.

| Signal | Subject | Trigger | Pain | Solution |
|---|---|---|---|---|
| **A1** FDA approval (Brittany) | `approval launch` | "Congrats on the FDA approval at [Company] last month." | "Most enterprise launches need approval-friendly volume that survives legal review on the first pass. Most vendors don't survive enterprise governance." | "Ontada, the McKesson healthcare-data subsidiary, runs their HCP and clinical-trial cuts through our pod. The editor learns the compliance pattern by the third project. Submissions clear legal on the first pass more often than not. A six-week cycle shrinks to two." |
| **A3** Medical congress (Brittany) | `[conference] content` | "Saw [Company]'s team is presenting at [Conference] next month." | "Congress content has a hard deadline and three audiences: HCP attendees, KOLs, and the field team. Most brand teams over-spec the deliverable count and under-deliver on quality." | "Janssen runs their congress content through our pod. One editor across all three audiences, brand voice stays consistent from teaser to recap, regulatory QA baked in." |
| **B5** Founder-led growth (Adam) | `[company] next phase` | "Saw [Company]'s [milestone] announcement." | "Founder-led marketing functions at this stage usually hit a wall where the junior marketing lead is drowning and the strategic conversations stop happening because everyone's executing." | "Asset Map has been a Viral client since 2017. Their marketing lead has a partner who thinks about positioning, platform strategy, and what to ship next, not just an editor who takes orders." |

---

## Email 2 — Template (Lead-Magnet Pivot)

Same thread, ~3-5 days after Email 1. The broader observation in paragraph 1 pulls from the **5 reasons clients switch** (per discovery), funnel-matched to the prospect.

```
Subject: Re: [Email 1 subject]

[BROADER OBSERVATION — funnel-matched, drawn from the 5 switching reasons].

Viral takes any long-form video and ships 5 short-form pieces in 5 business days. Branded, captioned, [audience-specific qualifier].

Interested in 5 short-form cuts from one of your existing [Company] long-forms? (on us)
```

**Word target:** 60-90 words.

### Broader observation library by signal type

| Email 1 signal type | Funnel | Email 2 paragraph 1 observation |
|---|---|---|
| Freelancer ghosting / job posting | A | "Almost every team we work with came to us after a freelancer ghosted mid-campaign. The pattern is consistent enough we built the model around it." |
| Quality drift / new marketing leader | A | "The most common story we hear is great first month, quality slip by month four. Usually that means the vendor scaled the account through a pool. We don't run pools." |
| Funding / paid creative pain | A | "Most growth teams that come to us have run paid for a quarter on a 14-day refresh cycle that should have been 5. The vendor couldn't keep up." |
| Agency editor hire / RFP | B | "Most agencies come to us after a vendor that survived strategy meetings but missed the client deliverable date. The math at signup stops working by month three." |
| Agency renewal cycle / churn risk | B | "Most agencies that come to us have a renewal book with one or two accounts flagging video as a churn risk. The vendor scaled the team through a pool. We don't." |
| Enterprise pharma | Opportunistic | "Enterprise teams usually come to us after a vendor couldn't survive legal and brand-compliance review. We've built around the approval cycle, not against it." |
| Founder (Adam-shaped) | Opportunistic | "Founder-led marketing functions usually outgrow their vendor stack and don't notice until deals start slipping. We tend to stay 8+ years for that reason." |

### Audience-specific qualifier (paragraph 2)

| Funnel / signal type | Qualifier line |
|---|---|
| Funnel A — Sierra (mid-market) | "ready to post on LinkedIn or YouTube" |
| Funnel A — Lindsey (growth) | "ready for paid or organic" |
| Funnel B — Daniel (agency) | "ready to deliver under your label" |
| Opportunistic — Brittany (pharma) | "regulatory-aware" |
| Opportunistic — Adam (founder) | "positioned for the next phase" |

---

## Rendered Examples (6 prospect pairs)

Each pair shows the fully resolved Email 1 + Email 2 ready to send. No placeholders. Pulled across all funnels.

### Prospect 1 — Maya Reyes, Senior Marketing Manager, Step
**Funnel A · Signal B1 (job posting)**

**Email 1**
```
Subject: editor hire

Hi Maya, saw Step is hiring a Video Editor. Most of our clients came to us
right after a freelancer ghosted before a launch or a quarterly review. The
math on hiring full-time usually doesn't survive a slow quarter either.

Self Financial runs their video through our pod. One dedicated editor
brand-trained before the first project, first drafts in 24 hours, Slack
response inside the hour Mon to Fri. Unlimited revisions on the first batch
until the baseline is right.

Worth a look for Step?
```

**Email 2**
```
Subject: re: editor hire

Almost every team we work with came to us after a freelancer ghosted
mid-campaign. The pattern is consistent enough we built the model around it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, ready to post on LinkedIn or YouTube.

Interested in 5 short-form cuts from one of your existing Step long-forms?
(on us)
```

---

### Prospect 2 — Tom Diaz, Head of Growth, Mercury
**Funnel A · Signal B6 (Series C funding)**

**Email 1**
```
Subject: series c content

Hi Tom, congrats on Mercury's Series C last quarter. The 90 days after a
round usually mean creative supply becomes the bottleneck. Sales enablement,
paid ads, recruiting content, and investor updates all need video at once,
and hiring takes too long.

Gainbridge, the growth team inside Group 1001 with about 160 billion in
assets under management, runs their paid-creative testing through our pod.
One dedicated editor, first drafts in 24 hours, ships new ad variants twice
a week.

Open to a 15-minute diagnostic?
```

**Email 2**
```
Subject: re: series c content

Most growth teams that come to us have run paid for a quarter on a 14-day
refresh cycle that should have been 5. The vendor couldn't keep up.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, ready for paid or organic.

Interested in 5 short-form cuts from one of your existing Mercury
long-forms? (on us)
```

---

### Prospect 3 — Sarah Chen, CEO, Anomaly
**Funnel B · Signal B1 (agency editor hire)**

**Email 1**
```
Subject: editor hire

Hi Sarah, saw Anomaly is hiring a Senior Video Editor. Most agencies that
come to us tried to hire their way out and the math broke. A full-time
editor is dead weight on slow weeks, and the brand calendar doesn't pause
while you ramp.

Clever Digital Marketing, a Canadian agency running about 80 staff, runs
our team behind their accounts white-label. Same editor every week, same-day
first drafts on Full-Time, Slack response inside the hour. The cuts go out
under their brand.

Worth a look for Anomaly?
```

**Email 2**
```
Subject: re: editor hire

Most agencies come to us after a vendor that survived strategy meetings but
missed the client deliverable date. The math at signup stops working by
month three.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, ready to deliver under your label.

Interested in 5 short-form cuts from one of your existing client long-forms?
(on us)
```

---

### Prospect 4 — Jessica Park, VP Marketing, Cala Health
**Funnel A · Signal B2 (new marketing leader)**

**Email 1**
```
Subject: new vp start

Hi Jessica, congrats on the VP Marketing start at Cala Health. First 90 days
for most marketing leaders means an audit of the content stack while the
calendar keeps moving. The brief intake usually gets sloppy and video falls
behind first.

Self Financial runs their content production through our pod for exactly
this. One dedicated editor brand-trained before the first project, first
drafts in 24 hours, Slack response inside the hour Mon to Fri.

The audit runs in parallel. The cadence holds.

Worth a look for Cala?
```

**Email 2**
```
Subject: re: new vp start

The most common story we hear is great first month, quality slip by month
four. Usually that means the vendor scaled the account through a pool. We
don't run pools.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, ready to post.

Interested in 5 short-form cuts from one of your existing Cala Health
long-forms? (on us)
```

---

### Prospect 5 — Rachel Park, Senior Marketing Director, Eli Lilly Oncology
**Opportunistic · Signal A1 (FDA approval)**

**Email 1**
```
Subject: approval launch

Hi Rachel, congrats on the FDA approval at Lilly Oncology last month. Most
enterprise launches need approval-friendly volume that survives legal review
on the first pass. Most vendors don't survive enterprise governance.

Ontada, the McKesson healthcare-data subsidiary, runs their HCP and
clinical-trial cuts through our pod. The editor learns the compliance pattern
by the third project. Submissions clear legal on the first pass more often
than not. A six-week cycle shrinks to two.

Open to a 15-minute diagnostic?
```

**Email 2**
```
Subject: re: approval launch

Enterprise teams usually come to us after a vendor couldn't survive legal
and brand-compliance review. We've built around the approval cycle, not
against it.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, regulatory-aware.

Interested in 5 short-form cuts from one of your existing Lilly long-forms?
(on us)
```

---

### Prospect 6 — Marcus Webb, COO, Sage Communications
**Funnel B · Signal B5 + B8 (new client win + Q4 renewal cycle)**

**Email 1**
```
Subject: renewal stack

Hi Marcus, saw Sage just announced the new client win. Most agencies hitting
Q4 with new accounts and an in-house team already at capacity see existing
clients start asking pointed questions about turnaround.

Clever Digital Marketing, a Canadian agency running about 80 staff, runs our
team behind five of their accounts white-label. Same-day first drafts,
dedicated editor per account, Slack response inside the hour.

Their renewal book got cleaner. Clients never knew.

Worth a look for Sage?
```

**Email 2**
```
Subject: re: renewal stack

Most agencies that come to us have a renewal book with one or two accounts
flagging video as a churn risk. The vendor scaled the team through a pool.
We don't.

Viral takes any long-form video and ships 5 short-form pieces in 5 business
days. Branded, captioned, ready to deliver under your label.

Interested in 5 short-form cuts from one of your existing client long-forms?
(on us)
```

---

## VI Differentiator Library

These are the REAL differentiators from the Discovery Questionnaire. Use them verbatim in Email 1's solution line. Match to context — the more specific to the prospect's pain, the better.

| Differentiator | When to use |
|---|---|
| "One dedicated editor, brand-trained before the first project" | Default — works in every signal |
| "First drafts in 24 hours" (Funnel A) / "Same-day first drafts" (Funnel B) | Speed/responsiveness pain |
| "Slack response inside the hour Mon to Fri 9 to 5 EST" | Communication-collapse pain (post-freelancer-ghost) |
| "Unlimited revisions on the first batch until the baseline is right" | Quality-fear pain |
| "Same editor every week. No pool, no rotation." | Brand-drift pain |
| "The editor learns the compliance pattern by the third project" | Pharma/regulated environments |
| "No ticket portal, no edit lottery, no autoresponder" | Vendor-collapse pain |
| "The cuts go out under your brand. The client never knows we exist." | Funnel B (agency white-label) |
| "Submissions clear legal on the first pass more often than not" | Enterprise pharma |
| "Strategic input on hook, retention, and platform fit, not just execution" | Adam (founder) / mature buyers |

---

## VOC Language Library (use the prospect's own words)

Discovery extracted the exact words VI's clients use. Use them in pain lines — they sound like the prospect's own internal monologue.

### All buyers say:
- "ghosted" / "dropped the ball"
- "off brand" / "inconsistent" / "unreliable"
- "another fire drill" / "fire drill"
- "I'm drowning" / "out of bandwidth"
- "we keep starting over"
- "the last batch was rough"
- "I just need someone I can trust"
- "I can't keep doing this"
- "we can't scale this"
- "I need a real team, not a freelancer"

### Agencies (Funnel B) say:
- "white-label"
- "dedicated editor"
- "we need someone who can ramp without us teaching them everything"
- "the client noticed"

### Enterprise marketers (Brittany) say:
- "approval friendly"
- "on brand at scale"
- "we can't have surprises"

---

## Copy Rules (Non-Negotiable)

| Rule | Why |
|------|-----|
| 50-100 words per email (Email 1: 70-100, Email 2: 60-90) | Brand book: grade 8-10 reading level. Above 100 words loses the buyer. |
| Subject: 2-4 words, lowercase, anchored to a specific prospect-owned thing | "your moa interview" beats "video production services for pharma" |
| Person and company names always capitalized | Even in lowercase subject lines |
| No em dashes | Use sentence breaks or commas |
| No exclamation marks | Brand book: calm and confident, never urgent |
| No spam words. Especially "free" | Replace with "on us" |
| No "$" symbol | Pricing belongs on the call, not in cold body |
| No bracket placeholders in final render | Every variable must be resolved before send |
| No "Best, Sender Name" inside body | Signature handled by EmailBison `{SENDER_EMAIL_SIGNATURE}` |
| No apologetic PS | "If this isn't a fit..." reads insecure. Calm and confident only. |
| No in-body taglines | BIGVU bug to avoid — keep brand lines in signature, not body |
| Soft yes/no CTA in Email 1 | "Worth a look for [Company]?" or "Open to a 15-minute diagnostic?" (high-intent signals) |
| Lead magnet drops in Email 2 only | Email 1 teases the product. Email 2 offers the 5-cut pack. |
| Email 2 paragraph 1 pulls from the 5 switching reasons | Makes the prospect feel understood ("they know what I went through") |
| Funnel-matched case study | Self Financial for Sierra/Funnel A · Gainbridge for Lindsey/Funnel A · Clever Digital for Daniel/Funnel B · Ontada/J&J for Brittany · Asset Map for Adam |
| VOC language in pain lines | Use the prospect's own words: ghosted, fire drill, drowning, white-label, approval friendly |

---

## Why This Structure Works (Evidence)

- **BIGVU Campaign 198:** 25,000+ sent, 285 replies (1.1%), 40 marked interested (14% positive-of-reply ratio). Email 1 alone drove 58% of all replies.
- **Discovery validation:** the 5 reasons clients switch (ghosting, quality drift, order-taker vendor, SLA collapse, brand drift) map 1:1 to the pain library above. We're not guessing at pain.
- **Funnel split rationale:** Funnel B (agency) has 8-15x higher LTV than Funnel A — one Daniel-shaped contract absorbs edits for 5-15 end clients and agencies stick longer than direct clients. The copy investment in Funnel B is justified by the deal economics.

---

## Operational Pre-Requisites Before Launch

These must be in place before Email 1 ships:

1. **Sample delivery workflow.** When a prospect replies to Email 2, the team must deliver the 5-cut pack within 24-48 hours. Same single point of failure that broke BIGVU's funnel (positives go cold after Calendly pivot). Viral cannot repeat.
2. **Funnel-matched case study assets.** Self Financial, Gainbridge, Clever Digital, Ontada, Asset Map — each needs at least a one-paragraph proof block ready to reference. Hard outcome numbers are the gap (Dave to backfill 2-3 per case study).
3. **Sender persona signature.** Name, brand, NYC location, phone number, website. Missing phone/address triggers scammer suspicion.
4. **Signal-finder prompts deployed.** Prompt A + Prompt B in Clay or equivalent, with priority-ordered evaluation.
5. **Suppression list functional.** Negative replies, OOOs, prior unsubscribes feed back into Clay / EmailBison suppression.
6. **Funnel-routing logic.** Lead's title + industry determines which funnel they go into. Mid-market mkt mgr + growth marketer → Funnel A. Agency owner/CEO → Funnel B. Enterprise pharma + B2B founder → opportunistic.

---

## Open Decisions for Dave Before Launch

1. **Lead magnet for Email 2: 5-cut pack vs. Video Grader vs. 15-min diagnostic?** Current default is 5-cut pack (matches BIGVU's proven sample-first model). Video Grader is self-service inbound. Diagnostic is the Doctor Frame closer. Recommend: 5-cut pack for cold, Diagnostic as Email 3 if no reply.
2. **Pricing transparency in cold copy?** Currently removed entirely. Brand-book says "clear pricing with no surprises," but cold reveal might be premature. Recommend: stay off pricing in cold, mention on call.
3. **HVAC vs. law firms in scope?** Discovery confirms law in scope and HVAC dropped. Already reconciled.
4. **Hard outcome numbers per case study?** Dave owes 2-3 numbers per case study (e.g., "Self Financial cut their freelancer rotation from 5 to 1 and shipped 3x/week consistently"). Without these, the proof line is logos-only and weaker than BIGVU's.
5. **Coordination with existing Lead Hunter outbound** (vlad@leadhunter.net). Pause, parallel, or handoff?
6. **PR firms / construction angle?** Out of scope per discovery (no mention in ICPs).
7. **Sender persona — Sarah Stanfield (BigVu pattern) or VI-specific (e.g., Jessica Terry, who's the praised PM in client reviews)?** Recommend: spin up a new Viral persona, do not reuse BIGVU's Sarah Stanfield.

---

_Document version: v2 (2026-05-12)_
_GitHub: https://github.com/matteof123/Viral/blob/main/email-sequences/triggers-and-templates.md_
