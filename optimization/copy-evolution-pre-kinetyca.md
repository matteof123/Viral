# Copy Evolution — Pre-Kinetyca Outbound
_Campaign group: Lead Hunter–operated outbound under Viral Ideas brand | Client: Viral Ideas Marketing_

This file tracks the pre-Kinetyca outbound copy as the BEFORE baseline. Every BEFORE is an actual email sent to a real prospect, pulled from the "Viral Idea Interested" sheet (owner: vlad@leadhunter.net). AFTER recommendations align to the GTM playbook (healthcare and agencies priority).

---

## 2026-05-12

### Performance at this sync

| Metric | Value |
|--------|-------|
| Leads | unknown (no campaign-level metrics — only interested-reply sheet) |
| Sent | unknown |
| Open % | unknown |
| Reply % | unknown |
| Positive replies (Jan 29 – May 12) | 35+ logged |
| Negative (target) | low — most "routing" replies are positive |
| Negative (copy) | unknown |
| Bounce % | unknown |

### Reply Intelligence Summary

**Positive replies came from:** ~50% Marketing/PR/Creative agencies (Cohere, Actual Size, Red House, BLINK, 215 Marketing, Purplegator, Tango, Devine, Keywave, Market Genesis, Merz Group, DeepLocal). ~15% real estate brokers (Quintin Group, Green Street, Allan Domb). ~10% healthcare-adjacent (Home Care, Trenton Health, Philadelphia Dental, Accelerated Bio). ~10% video peers (Flip Out Productions). Rest: miscellaneous (energy, bakery equipment, wellness, investment).

**Wrong-target signal:** The agency vertical is producing exactly the right Daniel-persona buyer (Head of Production, Founder, Owner) — this validates playbook Vertical #2. The other replies (real estate brokers, harm-reduction nonprofits, dental offices, restaurants) come from blasting Philly local emails to anyone with a website — they are not playbook-aligned targets.

**Negative (copy) — what turned people off and why:**
- DeepLocal soft-no: "we do not have not done projects in Philly that required this" — copy was over-indexed on Philly framing. Buyers outside Philly default to "this isn't for us."
- Rebecca Dauber (Tango) soft-no: "we currently work with 3 local resources and have an internal resource as well." — copy didn't differentiate Viral from a freelancer or another local shop. The "system over talent" hook is what would have made this land.

### Copy Changes Recommended

Two full BEFORE → AFTER per vertical (healthcare, agencies). Both AFTER versions are ready to paste into EmailBison/Smartlead once the copy approval flow runs.

---

#### Healthcare / Pharma — Email 1

**BEFORE (actual email sent to Yuta Lee, Founder & CEO of Accelerated Biosciences, 2026-02-13):**

```
Hey Yuta, we're a small video production team in Philadelphia- we've recently worked with McKesson and Asset Map on shooting and creating videos that have helped improve their sales and local presence.

Can I send you over some example videos we've made?

Dave Feinman
Viral Ideas

PS. If you don't care, just let me know and I won't reach out again
```

Their reply: "Please send some samples for me to see. Thank you." — positive

**Problems found in this actual email:**
- Brand violation: "small video production team" undersells the 83-person team
- Wrong case study pair: Asset Map (financial SaaS) makes no sense to a biotech CEO; should be Janssen, Cortechs.ai, or J&J
- Apologetic PS contradicts "calm and confident" brand voice
- "Sales and local presence" is too generic; biotech buyer cares about clinical content, HCP communications, regulatory compliance
- "Can I send you over" leads with seller behavior, not prospect outcome
- No mention of the actual buyer pain (med-legal review velocity, HCP content backlog, missing launch deadlines as career risk)

---

**AFTER (suggested 2026-05-12, healthcare biotech variant):**

**Subject:** clinical content cadence

**Body:**

```
Hey Yuta,

Janssen and Cortechs.ai run their HCP and clinical-trial cuts through our editing pod. The reason it works inside regulated workflows is the same dedicated editor every week and a managing editor who catches issues before they reach med-legal.

If your launch calendar is loading up, our Video Grader benchmarks current footage against the cuts running for Janssen.

Worth fifteen minutes to walk through what it surfaces?
```

Word count: 70. No em dashes. No exclamation marks. No spam words. No bracket placeholders.

**What changed and why:**
- **Subject:** none → `clinical content cadence` (3 words, lowercase, biotech-specific)
- **Hook:** "small video production team" → names two healthcare proof points (Janssen + Cortechs.ai) and the buyer's actual workflow (HCP and clinical-trial cuts, regulated workflows, med-legal review)
- **Case study fixed:** dropped Asset Map (irrelevant), added Janssen + Cortechs.ai (vertical-matched)
- **Differentiator surfaced:** "same dedicated editor every week and a managing editor who catches issues before they reach med-legal" — names the system over talent advantage in healthcare terms
- **CTA tightened:** specific time commitment ("fifteen minutes"), prospect outcome ("what it surfaces"), single yes/no
- **Apologetic PS removed**

**Machine-readable diff:**
```json
{
  "campaign_group": "pre-kinetyca-healthcare",
  "email_step": 1,
  "sync_date": "2026-05-12",
  "evidence": {
    "lead_name": "Yuta Lee",
    "company": "Accelerated Biosciences",
    "title": "Founder & CEO",
    "reply_quote": "Please send some samples for me to see. Thank you.",
    "reply_classification": "positive"
  },
  "changes": {
    "subject": { "before": "(none captured)", "after": "clinical content cadence", "reason": "3-word vertical-specific subject, biotech buyer recognizes the term" },
    "hook": { "before": "small video production team in Philadelphia", "after": "Janssen and Cortechs.ai run their HCP and clinical-trial cuts through our editing pod", "reason": "vertical-matched proof + buyer workflow" },
    "case_study": { "before": "McKesson and Asset Map", "after": "Janssen and Cortechs.ai", "reason": "biotech CEO needs biotech proof, not financial SaaS" },
    "body": { "before": "videos that have helped improve their sales and local presence", "after": "same dedicated editor every week and a managing editor who catches issues before they reach med-legal", "reason": "names the differentiator in the buyer's domain language" },
    "cta": { "before": "Can I send you over some example videos we've made?", "after": "Worth fifteen minutes to walk through what it surfaces?", "reason": "specific time, prospect outcome, single CTA" },
    "ps": { "before": "PS. If you don't care, just let me know and I won't reach out again", "after": "(removed)", "reason": "apologetic line violates 'calm and confident' brand voice" }
  }
}
```

---

#### Marketing & PR Agencies — Email 1

**BEFORE (actual email sent to Aasim Ayub at Keywave Digital, 2026-05-06; reply 2026-05-08):**

```
Aasim, short question —

When a client project needs video, does your team produce it in-house or bring in an outside crew?

We're a small Philly production team that agencies occasionally bring in for shoots — experienced across a wide range of industries and flexible with the type of projects we do.

Worth sending over a couple examples?

- Michael Kaneff
Viral Ideas
```

Their reply: "yes" — positive (terse)

**Problems found in this actual email:**
- Two em dashes (violates copy rule)
- "Small Philly production team" — false-modesty positioning again; doesn't match Daniel-persona's need for white-label trust
- "Experienced across a wide range of industries and flexible with the type of projects" — vague, generic
- No agency-peer case study (Clever Digital Marketing, sagefrog, bemarketing are sitting unused)
- CTA is the same low-conversion samples-bounce pattern

---

**AFTER (suggested 2026-05-12, agencies variant):**

**Subject:** outside crew overflow

**Body:**

```
Hey Aasim,

When a client win drops a video-heavy campaign on Keywave, does production stay internal or do you pull in a crew per project?

A small handful of Philly and NYC agencies use our pod as overflow. One brief, one dedicated editor, cuts finished inside the SLA they promised their clients. Clever Digital Marketing runs us this way and the cuts go out under their brand.

Open to a quick walkthrough of how it plugs in?
```

Word count: 72. No em dashes. No exclamation marks. No spam words.

**What changed and why:**
- **Subject:** none → `outside crew overflow` (3 words, lowercase, agency-specific)
- **Hook:** generic "short question" → named scenario at the actual agency ("when a client win drops a video-heavy campaign on Keywave")
- **Case study:** dropped vague "agencies occasionally bring in" → named Clever Digital Marketing (agency peer, white-label proof)
- **Differentiator surfaced:** "One brief, one dedicated editor, cuts finished inside the SLA they promised their clients" — names the actual buyer pain (delivery SLA risk)
- **CTA tightened:** "quick walkthrough of how it plugs in" — specific, white-label-trust framing
- **No em dashes** — replaced with sentence breaks

**Machine-readable diff:**
```json
{
  "campaign_group": "pre-kinetyca-agencies",
  "email_step": 1,
  "sync_date": "2026-05-12",
  "evidence": {
    "lead_name": "Aasim Ayub",
    "company": "Keywave Digital",
    "title": "Founder",
    "reply_quote": "yes",
    "reply_classification": "positive"
  },
  "changes": {
    "subject": { "before": "(none captured)", "after": "outside crew overflow", "reason": "agency-specific 3-word subject" },
    "hook": { "before": "short question — When a client project needs video, does your team produce it in-house or bring in an outside crew?", "after": "When a client win drops a video-heavy campaign on Keywave, does production stay internal or do you pull in a crew per project?", "reason": "named scenario; named agency; specific trigger (client win)" },
    "case_study": { "before": "agencies occasionally bring in for shoots — experienced across a wide range of industries", "after": "Clever Digital Marketing runs us this way and the cuts go out under their brand", "reason": "named agency-peer proof; white-label angle" },
    "body": { "before": "experienced across a wide range of industries and flexible with the type of projects we do", "after": "One brief, one dedicated editor, cuts finished inside the SLA they promised their clients", "reason": "specific differentiator framed for agency buyer (SLA risk)" },
    "cta": { "before": "Worth sending over a couple examples?", "after": "Open to a quick walkthrough of how it plugs in?", "reason": "white-label trust framing; specific outcome" },
    "em_dashes": { "before": 2, "after": 0, "reason": "copy rule" }
  }
}
```

---

#### Email 2 — Service offer thread (for both verticals)

The pre-Kinetyca outbound does NOT appear to send a structured Email 2 / follow-up thread — only same-thread follow-ups. The playbook calls for a separate-thread Email 2 7 days after Email 1, pivoting from audit/lead magnet to retainer.

**NO BEFORE EVIDENCE — Email 2 not yet sent in pre-Kinetyca campaigns.**

When Kinetyca launches, recommend the following Email 2 structure (per playbook):

- Same lead, separate thread, ~7 days after Email 1
- Hook: name the symptom they probably have (e.g., "creative refresh slipping into next sprint" for DTC, "med-legal review backlog" for healthcare, "agency client asking for cuts before the launch" for agencies)
- Body: production-engine reframe (system over talent, named editor, managing editor, QA)
- CTA: 15-minute call to walk through how a pod plugs into their existing setup

**Draft Email 2 — Healthcare (Brittany persona):**

**Subject:** review backlog math

**Body:**

```
Hey Brittany,

Sent a note last week about the editing pod we run for the Ontada team. Wanted to share the part that usually matters most.

The editor assigned to your account writes back inside one hour on business days, runs every cut through a managing editor before delivery, and has the regulatory checklist baked into the QA pass. The pod replaces a freelancer rotation that breaks every six months and a $90K in-house editor seat.

Fifteen minutes next week to show how it plugs into your existing review cycle?
```

Word count: 80. No em dashes. No spam words.

**Draft Email 2 — Agencies (Daniel persona):**

**Subject:** delivery layer math

**Body:**

```
Hey Daniel,

Followed up last week on the white-label overflow model. Wanted to share the math that usually closes it.

A freelancer at thirty an hour costs nothing the day they ghost and roughly five thousand the day a client launch slips. An in-house editor seat is ninety thousand loaded. Our pod for the whole agency runs less than a single seat and survives any one editor leaving.

Worth fifteen minutes to walk through how it plugs into Keywave's delivery model?
```

Word count: 79. No em dashes. No spam words.

---

### Targeting Changes Recommended

#### Pre-Kinetyca outbound targeting — BEFORE

- Job titles: any visible website email (broker, owner, founder, ED, VP, CEO — no filtering)
- Industries: real estate, creative agencies, healthcare-adjacent, restaurants, energy, dental, nonprofits, harm reduction, bakery equipment, wellness, investment, biotech, SaaS, video peers
- Company size: not filtered
- Geography: Philadelphia + Pittsburgh metro
- Signals used: none visible

#### AFTER — suggested for Kinetyca launches

- **Job titles to ADD:**
  - VP Marketing, Senior Director of Brand, Head of Content, Senior Business Director (healthcare)
  - CEO, Founder, COO, Head of Production (agencies)
  - Triggered Education / Training & Development (healthcare specialized)
- **Job titles to REMOVE:**
  - Brokers, listing agents
  - Owners of dental offices, harm-reduction nonprofits, bakery equipment companies
  - Solo wedding videographers / video peers
- **Industries to ADD:**
  - Pharma (manufacturers, biotech, med device)
  - Healthcare systems, clinics, health tech (with $1M+ revenue + VP/Director marketing buyer)
  - $5M–$50M marketing/PR agencies with 30–150 FTE
- **Industries to REMOVE:**
  - Real estate brokerages (negative signal: solo / commission-driven)
  - Nonprofits (no budget)
  - Restaurants, bakeries, energy, dental practices (below ICP / no fit)
  - Wedding / event videographers (negative signal)
- **Signals to PRIORITIZE:**
  - Hiring signal: new CMO / VP Marketing / Head of Content in last 30 days
  - Hiring signal: open role Video Editor / Content Producer / Social Media Manager
  - Hiring signal: open role Paid Social Manager / Performance Marketer
  - Hiring signal: open role Freelance / Contract Video Editor
  - Funding signal: Series A–C in last 90 days
  - Product signal: new product launch announced
  - Vertical (pharma): FDA approval, clinical trial milestone, new indication launch
  - Vertical (agencies): new client win, new office or service line
- **Geography:**
  - Expand from Philadelphia-only to US-first nationally
  - Add Canada as secondary
  - Do NOT pursue international until US/CA are saturated

**Machine-readable diff:**
```json
{
  "campaign_group": "pre-kinetyca-targeting",
  "sync_date": "2026-05-12",
  "targeting_changes": {
    "add_titles": ["VP Marketing", "Sr. Director of Brand", "Head of Content", "Sr. Business Director", "CEO of agency", "Founder of agency", "COO of agency", "Head of Production", "Triggered Education", "Training & Development Manager"],
    "remove_titles": ["Real estate broker", "Listing agent", "Solo dental practice owner", "Nonprofit Executive Director", "Bakery equipment owner", "Wedding videographer"],
    "add_industries": ["Pharma manufacturers", "Biotech", "Med device", "Health tech with $1M+ revenue", "$5M-$50M marketing/PR agencies (30-150 FTE)"],
    "remove_industries": ["Real estate brokerages", "Nonprofits", "Restaurants", "Bakeries", "Energy", "Dental practices", "Wedding/event videographers"],
    "add_signals": ["New CMO/VP Marketing/Head of Content hire 30d", "Open role Video Editor / Content Producer / Social Media Manager", "Open role Paid Social Manager", "Open role Freelance Video Editor", "Series A-C funding 90d", "New product launch announcement", "FDA approval (pharma)", "Clinical trial milestone (pharma)", "New client win (agencies)"],
    "remove_signals": ["Generic Philly metro keyword match"],
    "geography_before": "Philadelphia + Pittsburgh metro",
    "geography_after": "US first, Canada second"
  }
}
```
