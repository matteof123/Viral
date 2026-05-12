# Viral Ideas Marketing — Outbound Campaigns

_Last synced: 2026-05-12 (initial sync, foundation phase)_

This file is the operational source of truth for what's running and what should be running. Every weekly sync prepends a new dated section at the top.

---

## Sync Update — 2026-05-12

**Initial sync. Foundation phase, Week 2 of 90-day plan. No Kinetyca-managed campaigns active yet. A pre-Kinetyca outbound operation (Lead Hunter, vlad@leadhunter.net) is producing replies under the Viral Ideas brand.**

### Metrics as of 2026-05-12

| ID | Campaign | Status | Leads | Sent | Replies | Interested | Bounced | Notes |
|----|----------|--------|-------|------|---------|------------|---------|-------|
| - | Healthcare/Pharma | not yet built | - | - | - | - | - | Copy due 2026-05-15. Launch target 2026-05-24. |
| - | Marketing & PR Agencies | not yet built | - | - | - | - | - | Sequenced after Healthcare per phase plan. |
| - | Ecommerce / DTC | not yet built | - | - | - | - | - | Reserved for week 7–8 per phase plan. |
| pre-K | Pre-Kinetyca outbound (Lead Hunter) | running outside Kinetyca | unknown | unknown | unknown | 32+ logged | unknown | "Viral Idea Interested" sheet tracks replies. Senders: David Feinman, Michael Kaneff. |

**Change vs previous sync:** N/A — this is the initial sync.

---

### Pre-Kinetyca outbound — what's actually running today

Since at least 2026-01-29, an outbound program has been generating Viral Idea interested replies under David Feinman's (early) and Michael Kaneff's (later) personal sending addresses. The tracking sheet is owned by vlad@leadhunter.net, suggesting this is a Lead Hunter–operated campaign separate from Kinetyca's scope.

**Senders observed:**
- David Feinman — `dave@*`, `david.feinman@*` — Jan–Feb 2026
- Michael Kaneff — `mike@*`, `michael@*`, `mikek@*` — Feb 2026 – present

**Domains rotated** (incomplete list from sender footers):
`tryviralidea.com`, `teamviralidea.com`, `sayviralidea.com`, `helloviralidea.com`, `useviralidea.com`, `withviralidea.com`, `ideavirals.com`, `viralidea-collective.com`, `viralidea-group.com`, `meetviralidea.com`

**Targets observed (vertical):**
- Real estate brokers and listing agents (Quintin Group, Green Street, Allan Domb, OntheGoga)
- Local Philly creative / PR agencies (Cohere, Tango Multimedia, Devine Partners, BLINK, Red House, Actual Size, MerzGroup, DeepLocal, Keywave Digital, Market Genesis)
- Investment / wealth advisors (Eclat Investments, Astrabit, Burro AI)
- Healthcare-adjacent (Trenton Health Team, Accelerated Biosciences, Home Care Associates, PA Harm Reduction Network, Philadelphia Dental, Acreditebio)
- Wellness / retail (BeadXYZ, MomEdit, Devine PR)
- Random (Gemini Bakery Equipment, Ideal Energy LLC, Flip Out Productions, Purplegator, 215 Marketing)

**Verdict:** Most of these prospects fall on the GTM playbook's "do not contact" list (DIY creators, solo attorneys, hype startups, organizationally chaotic, etc.). Targeting is not aligned with the priority verticals.

**Sample volume signal:** 32+ interested replies between Jan 29 and May 12 ≈ 7+ interested replies per month. 2 came in TODAY alone (Kevin Shinkle / Devine Partners and Elizabeth Finkle / On the Goga). Volume is modest but the response rate cannot be calculated without total sent.

---

### Campaign A — Pre-Kinetyca "small video production team / Philly local" (Jan–Feb 2026)

#### Email 1 — BEFORE (actual email sent to Nemo Resmerowski at Eclat Investments)

**Subject:** _not captured in interested-reply sheet — likely "quick question" or similar_

**Body:**

```
Hey Nemo, we're a small video production team in Philadelphia- we've recently worked with McKesson and Asset Map on shooting and creating videos that have helped improve their sales and local presence.

Can I send you over some example videos we've made?

Dave Feinman
Viral Idea

PS. If you don't care, just let me know and I won't reach out again
```

**Their reply:** "Yes, please send a portfolio, and more importantly costs associated with them." — positive

**Problems found in this actual email:**
1. **Brand violation: "small video production team"** — Viral is an 83-person fully-remote team that has edited 100,000+ videos. The copy actively undersells the differentiator (system, scale, QA, managing editors). Brand book bans this kind of false-modesty positioning.
2. **Case study mismatch** — McKesson and Asset Map (pharma + financial advisor SaaS) sent to an investment firm CEO with no apparent fit. Playbook explicitly says case studies must match the buyer's environment.
3. **Apologetic PS** — "If you don't care, just let me know and I won't reach out again" reads insecure. Brand book is "calm and confident." This line undermines authority.
4. **No vertical-specific pain** — does not name the prospect's actual problem. "sales and local presence" is too generic.
5. **Hyphen-as-em-dash** (`Philadelphia-` opening the second clause) — should be a sentence break.
6. **No clear next step** — "Can I send you over some example videos" is a soft yes/no, but it leads with the seller's behavior ("Can I…"), not the prospect's outcome.

---

#### Email 1 — AFTER (suggested 2026-05-12, healthcare vertical, Brittany persona)

**Subject:** ontada review velocity

**Body:**

```
Hey Brittany,

McKesson's Ontada team uses our editing pod for regulated content that has to pass med-legal review without slipping a launch date. Same dedicated editor every week. Brief on the first try. No surprise revisions before exec sign-off.

If a launch is on your radar this quarter, we built a free Video Grader that benchmarks your current footage against the cuts we run for Janssen and J&J.

Worth fifteen minutes to walk through what it surfaces?
```

Word count: 71. No em dashes. No exclamation marks. No spam words. No bracket placeholders. Signature handled by EmailBison's `{SENDER_EMAIL_SIGNATURE}` system variable.

**What changed and why:**
- **Subject:** `(none captured)` → `ontada review velocity` — 3 words, all lowercase, Ontada capitalized as proper noun. Names a specific buyer environment (Ontada review process) the prospect immediately recognizes.
- **Hook:** `small video production team in Philadelphia` → `McKesson's Ontada team uses our editing pod for regulated content that has to pass med-legal review` — leads with the buyer's actual workflow (med-legal review). Names the most relevant single proof point for this vertical.
- **Case study:** `McKesson and Asset Map` (mismatched pair) → `Ontada + Janssen + J&J` (all aligned to healthcare buyer)
- **CTA:** `Can I send you over some example videos` → `Worth fifteen minutes to walk through what it surfaces?` — specific time commitment, prospect outcome ("what it surfaces"), not seller behavior
- **No apologetic PS** — removed entirely. Brand book voice
- **Audit offer in its own paragraph** — Video Grader sits between social proof and CTA, per copy rules

---

#### Email 1 — AFTER (suggested 2026-05-12, agencies vertical, Daniel persona)

**Subject:** clever digital model

**Body:**

```
Hey Daniel,

Clever Digital Marketing built a video delivery layer with our pod that they resell under their brand. One brief, one editor on every account, finished cuts inside the SLA they promised their clients.

We do this for a handful of agencies. Quietly, no attribution, no client-facing logo. The thing they buy is not the editing. It is the fact that an editing partner never embarrasses them in front of a client.

Open to seeing how it plugs into your delivery model?
```

Word count: 73. No em dashes. No exclamation marks. No spam words.

**What changed and why:**
- **Subject:** `(none captured)` → `clever digital model` — name-drops the closest peer agency. Daniel persona recognizes this as relevant.
- **Hook:** `small video production team in Philadelphia` → `Clever Digital Marketing built a video delivery layer with our pod that they resell under their brand` — leads with peer agency outcome (white-label resell), the Daniel persona's actual job-to-be-done.
- **Hook differentiator surfaced:** "An editing partner never embarrasses them in front of a client" — direct from playbook persona hook for Daniel.
- **CTA:** soft yes-or-no on a specific request ("plugs into your delivery model") — Daniel is owner-operator, can decide on the spot.

---

### Campaign B — Pre-Kinetyca "quick question / agency overflow" (Mar–May 2026, Michael Kaneff)

#### Email 1 — BEFORE (actual email sent to Daniel Filipek at Red House Communications)

**Subject:** _not captured — likely "quick question"_

**Body:**

```
Hi Daniel,

Quick question - do you ever bring in outside production teams when campaigns require video?

We're a small studio and production team in Philly and have worked with agencies on projects for McKesson and Asset Map.

Interested in seeing a few examples?

Michael Kaneff
Viral Ideas
```

**Their reply:** "Adding Justin to this chain — he leads our production relationships here at the agency. He's out on a shoot this week..." — positive routing

**Problems found in this actual email:**
1. **Same case-study mismatch** — McKesson (pharma) and Asset Map (financial SaaS) cited to an agency contact. Both are end-clients, not agency peers. Daniel persona wants to hear about agencies that already use the system, not end-clients.
2. **"Small studio and production team"** — same brand violation as Campaign A. Hides the system / scale / QA differentiator.
3. **"On projects for"** — vague. Doesn't say what the work was, the cadence, or the outcome.
4. **CTA is generic** — "Interested in seeing a few examples?" works as a follow-up trigger but produces low-quality samples-request replies that don't lead to discovery calls.
5. **Hyphen as em-dash** — "Quick question - do you ever..." — should be a comma or period.

**Why it still works (occasionally):** Asking agencies whether they use outside crews is a natural conversation opener and Michael's variant is producing about 1 reply per week from Philly-based agencies. The volume is real; the conversion to discovery call is the bottleneck.

---

#### Email 1 — AFTER (suggested 2026-05-12, agencies vertical, Michael Kaneff sender)

**Subject:** outside crew overflow

**Body:**

```
Hey Daniel,

When a client win drops a video-heavy campaign on Red House, does the production go to the same internal hands or do you build a crew per project?

A small handful of Philly + NYC agencies use our pod as overflow. One brief, one editor on every account, finished cuts before the campaign launches. Clever Digital Marketing runs us this way and the cuts go out under their brand.

Worth a quick walkthrough of the model?
```

Word count: 75.

**What changed and why:**
- **Subject:** `quick question` → `outside crew overflow` — specific to the buyer's actual question.
- **Hook:** generic "do you ever bring in outside production teams" → specific scenario ("when a client win drops a video-heavy campaign on Red House"). Names the actual agency. The prospect feels seen, not blasted.
- **Case study fixed:** Clever Digital Marketing replaces McKesson/Asset Map. Daniel persona case study, matching agency-to-agency.
- **CTA tightened:** "worth a quick walkthrough" — same length as their reply ("interested in seeing examples") but commits to the actual conversation, not a samples-bounce.

---

### Campaign C — Pre-Kinetyca "PR firm announcements" (May 11–12, Michael Kaneff)

This is the newest variant — only sent to a few prospects so far. Includes Kevin Shinkle's reply TODAY (2026-05-12).

#### Email 1 — BEFORE (actual email sent to Kevin Shinkle at Devine Partners)

**Subject:** _"quick question"_

**Body:**

```
Hey Kevin,

We're a Philadelphia-based video team that works with PR teams to turn announcements into usable content fast.

The work usually looks like launch clips, social cutdowns, and b-roll that actually gets used when the story goes live.

We've worked with smaller PR teams and in-house comms groups that needed to move quickly without building production internally - most of them come to us because they need content ready at the same time the story breaks, not weeks later.

Want me to send over a few examples?
```

**Their reply (2026-05-12):** "Thanks for reaching out. We'll take a look at your website and see if there are ways we may collaborate." — soft positive, will research

**Problems found in this actual email:**
1. **Hyphen-as-em-dash** twice — "in-house comms groups that needed to move quickly without building production internally -" and "when the story breaks, not weeks later."
2. **Smaller PR teams** — false-modesty framing again. Viral works with enterprise clients; saying "smaller PR teams" actually shrinks credibility.
3. **No PR-specific case study** — playbook does not list PR firms as a target vertical at all. This is a third vertical being run outside the agreed-on scope.
4. **"Want me to send over a few examples?"** — same low-conversion samples-bounce CTA pattern.
5. **Long sentence** — the "we've worked with smaller PR teams..." sentence is 47 words and runs grade 14+. Brand book caps at grade 8–10.

**Recommendation:** Discuss with Dave whether PR firms (a new vertical not in the GTM playbook) should be in scope. If yes, build a proper case study (Devine Partners reached out — they could become the first proof point). If no, redirect the Michael Kaneff sender to the agencies vertical with the proper Daniel persona positioning.

---

### Interested Replies — Pre-Kinetyca outbound — 2026-05-12

Pulled from "Viral Idea Interested" sheet (owner: vlad@leadhunter.net). 32 logged replies between 2026-01-29 and 2026-05-12.

| # | Date | Person | Title | Company | Vertical | Reply class | Quote |
|---|------|--------|-------|---------|----------|-------------|-------|
| 1 | 2026-01-29 | Nemo Resmerowski | (not specified) | Eclat Investments | Investment | ✅ Positive | "Yes, please send a portfolio…" |
| 2 | 2026-02-05 | Robert Skeels | Listing Agent Partner | The Quintin Group | Real Estate | ✅ Positive | "Yes, I'd be interested. If you could send me some examples." |
| 3 | 2026-02-12 | Tatia Cooper | President/CEO | Home Care Associates | Healthcare-adjacent | ✅ Positive | "Sure" |
| 4 | 2026-02-13 | Zoe Brookes | COO | Trenton Health Team | Healthcare nonprofit | ⚪ Routing | "I have passed your enquiry to our Communications Manager." |
| 5 | 2026-02-13 | Mark / Scott Rosenberg | (Owner / EVP route) | Gemini Bakery Equipment | Manufacturing | ✅ Positive | "I think it would be helpful for us to have an introductory conversation." |
| 6 | 2026-02-15 | Yuta Lee | Founder & CEO | Accelerated Biosciences | Biotech | ✅ Positive | "Please send some samples for me to see." |
| 7 | 2026-02-16 | Tom Granado | (not specified) | TrueSearch | SaaS / search | ⚠️ Mixed | "Im less interested in externally facing advertising… Want to take materials I have (HTMLs) and create compelling storylines with voiceover. Can you do that?" |
| 8 | 2026-02-18 | Lori Pagnozzi | VP, Partner Strategy | Bead.xyz | (unclear) | ⚠️ Cautious | "I can't say this is the direction we want to go in, but seeing an example is a good starting point." |
| 9 | 2026-02-18 | Carla Sofronski | Co-Founder & ED | PA Harm Reduction Network | Nonprofit | ✅ Positive | "sure, thanks" |
| 10 | 2026-02-18 | Artyom Sharbatyan | CEO | Philadelphia Dental | Healthcare | ✅ Positive | "Please send me some of the videos you made and their costs." |
| 11 | 2026-02-19 | Cam Paulding | Chief Marketing Officer | AstraBit | Crypto / fintech | ✅ Positive | "Yes, you can send some examples over." |
| 12 | 2026-02-20 | Cody O'Connor | President / Founding Partner | Ideal Energy Solutions | Energy | ✅ Positive (book call!) | "Do you have time for a zoom on Monday or later this afternoon?" |
| 13 | 2026-03-05 | Shana Draugelis | (not specified) | The Mom Edit | DTC / lifestyle | ✅ Positive | "I'd love to see some examples - thanks for reaching out!" |
| 14 | 2026-03-06 | Ryan Clifford → Dan Wiechec | Senior Manager, RevOps | Burro AI | SaaS / robotics | ⚪ Routing | "Ill take a look at a few examples. Ryan is not longer with the company." |
| 15 | 2026-03-06 | Chris Richards | Partner | Cohere | Creative agency | ✅ Positive | "Sure, send over some links" |
| 16 | 2026-03-25 | Katherine Rivera | Owner/Creative Director | Flip Out Productions | Video production peer | ✅ Positive | "Sure" |
| 17 | 2026-03-31 | Bob Bentz | (not specified) | Purplegator | Marketing agency | ✅ Positive | "We have a staff member, but we are sometimes double-booked. So, please send the information…" |
| 18 | 2026-04-02 | Mark Siracusa | (not specified) | 215 Marketing | Marketing agency | ✅ Positive | "Sure thing, send them over! Thanks." |
| 19 | 2026-04-02 | Tim McLaughlin | (not specified) | Blink Advertising | Marketing agency | ✅ Positive | "We are mostly in house but do occasionally need some outside help. Send over what ya have…" |
| 20 | 2026-04-08 | Joe Shumbat | (Founder) | Actual Size | Creative agency | ✅ Positive | "Sure, we're always looking for solid collaborators. Send over some samples." |
| 21 | 2026-04-08 | Daniel Filipek → Justin Clawson | (Head of Production route) | Red House Communications | Marketing agency | ⚪ Routing | "Adding Justin to this chain — he leads our production relationships here at the agency." |
| 22 | 2026-04-08 | Mary Kiernan | (not specified) | Actual Size | Creative agency | ✅ Positive | "Thanks for reaching out. I am happy to review your reel and keep you in mind for shoots." |
| 23 | 2026-04-10 | Mary Conte → Chris Clemson | (Creative Director route) | Merz Group / Merz Branding | Branding agency | ⚪ Routing | "I will share your information with our Creative Director, Chris Clemson…" |
| 24 | 2026-04-13 | Martin Weinberg | (not specified) | Market Genesis | Marketing agency | ✅ Positive (warm) | "Great to hear from you. Tell David I say hello." |
| 25 | 2026-04-13 | Eanna Holton | Head of Studio & Production Operations | DeepLocal | Creative agency | ⚠️ Soft no (file for later) | "We do from time to time bring in external video production teams, but historically, we do not have not done projects in Philly that required this. I will keep you in mind…" |
| 26 | 2026-04-21 | Michaela Melendez | Vice President | PSCO Philly | Real Estate / PR | ✅ Positive | "Please feel free to share." |
| 27 | 2026-04-22 | Herbert Sudfeld | Broker | Green Street Real Estate | Real Estate | ✅ Positive | "Sure send along" |
| 28 | 2026-04-28 | Arielle Kerstein | (not specified) | Allan Domb | Real Estate | ✅ Positive | "sure!" |
| 29 | 2026-05-05 | Geraldine Cronin → Rebecca Dauber | Director / Creative Director route | Tango Multimedia | Marketing agency | ⚪ Routing | "I forwarded your email to our creative director, Rebecca Dauber." |
| 30 | 2026-05-05 | Daniel Filipek → Justin Clawson | (Head of Production route) | Red House Communications | Marketing agency | ⚪ Routing (2nd contact) | "passed along your email to our head of production, Justin Clawson" |
| 31 | 2026-05-06 | Mary Conte | (not specified) | Merz Group / Merz Branding | Branding agency | ⚪ Routing (2nd contact) | "I can share with our Chris Clemson our Creative Director and he can reach out to you." |
| 32 | 2026-05-07 | Rebecca Dauber | Creative Services | Tango Multimedia | Marketing agency | ⚠️ Soft no | "We currently work with 3 local resources and have an internal resource as well, but you can certainly forward samples to me if you like." |
| 33 | 2026-05-08 | Aasim Ayub | (Founder) | Keywave Digital | Marketing agency | ✅ Positive | "yes" |
| 34 | 2026-05-12 | Kevin Shinkle | SVP / Chief Content Officer | Devine Partners | PR agency | ✅ Positive (soft) | "We'll take a look at your website and see if there are ways we may collaborate." |
| 35 | 2026-05-12 | Elizabeth Finkle | Head of Partnerships | On the Goga | Wellness / corp wellbeing | ✅ Positive | "Yes, let's see it." |

**Pattern summary:**
- **Marketing/PR agencies are the dominant reply vertical** (~50% of all interested replies). This validates the GTM playbook's #2 priority pick.
- **Real estate brokers and listing agents** (5 replies) — NOT in playbook scope. Either need to be added as a new vertical (single-source low-LTV per playbook negative signals) or stopped.
- **Healthcare-adjacent** (Home Care Associates, Trenton Health Team, Philadelphia Dental, Accelerated Biosciences) — 4 replies. Real targeting potential here, but none of these match the playbook's priority healthcare ICP (pharma manufacturers, biotech with $1M+ revenue and VP/Director marketing buyers). They are below-ICP.
- **Routing replies** (~6 of 35) — these are the most useful positive signal in agency vertical. They identify the actual buyer (Head of Production, Creative Director) and bring them into the conversation.
- **The agency vertical is producing replies that match the Daniel persona** — production / production-relationship contacts at $5M–$50M agencies. Kinetyca's first agency campaign should mirror these existing reply patterns, but with proper Daniel-persona copy.

### LinkedIn Campaigns — 2026-05-12

**Status: No HeyReach campaigns active yet for Viral.**

A "LinkedIn List" spreadsheet exists in Drive (file `1VeouY2RDsH6kbbRRLagVZQEGzQUNa_UV-H6d040aZTg`, modified 2026-03-13) — predates the Kinetyca engagement and is likely the Viral team's own list.

ClickUp task "If a LinkedIn campaign is to be launched, set up the campaign in HeyReach or Lemlist" is marked DONE (2026-04-23). HeyReach is provisioned but no campaign is built.

Recommendation per playbook: LinkedIn is an **optional parallel layer** for healthcare and agency tier in week 5–6, not week 1. Hold LinkedIn until email campaign 1 has 2 weeks of reply intelligence to inform LinkedIn copy.

---

### Planned Kinetyca Campaigns (week 3–4 launch)

#### Campaign 1 — Healthcare / Pharma (planned launch ~2026-05-24)

| Field | Plan |
|-------|------|
| Vertical | Healthcare / Pharma (PRIORITY 1) |
| Persona | Brittany (Sr. Marketing Director at pharma subsidiary) |
| ICP | Companies $1M+ in pharma, biotech, healthcare systems, clinics, health tech, med device |
| Buyer titles | VP Marketing, Senior Director of Brand, Head of Content, Senior Business Director, Triggered Education, Training & Development Manager |
| Geography | US first, Canada second |
| Anchor proof | McKesson (Ontada), Janssen, J&J, Cortechs.ai |
| Email 1 angle | Risk reduction + enterprise track record. "We get the brief on the first try." |
| Email 2 angle | Production engine reframe (system over talent). 7 days after Email 1, separate thread. |
| Test batch | First 50 leads, copy approval before full send |
| Bounce ceiling | <3% |

#### Campaign 2 — Marketing & PR Agencies (planned launch ~week 5–6)

| Field | Plan |
|-------|------|
| Vertical | Marketing & PR Agencies (PRIORITY 2) |
| Persona | Daniel (CEO / Founder / Head of Production at $5M–$50M agency) |
| ICP | $5M–$50M revenue, 30–150 FTE, single-discipline agencies |
| Buyer titles | CEO, Founder, COO, Head of Production. Champions: Marketing Managers, CMOs, Head of Content |
| Geography | US first, Canada second |
| Anchor proof | Clever Digital Marketing (Canada, ~$10M, ~80 employees), sagefrog.com, bemarketing.com |
| Email 1 angle | White-label trust. "An editing partner that plugs into your team and never embarrasses you." |
| Signal to layer | "Head of Production" hire in last 30 days |
| Test batch | First 50 leads after healthcare reply intelligence is in |

---

## Coordination Decisions Needed (escalate to Matteo + Dave)

1. **What happens to the Lead Hunter outbound when Kinetyca launches?** Pause, run in parallel, or hand-off list to Kinetyca?
2. **Sender identity** — does Kinetyca use new sender personas (Dave + Michael continued) or a separate AE name? Brand book says "you over we" so existing personas may continue.
3. **The 35 logged interested replies** — does Kinetyca pick these up for nurture, or are they owned by Alina (Viral) via the existing flow?
4. **PR firms as a new vertical?** Devine Partners reply today raises the question.
5. **Construction / home remodeling?** A third copy variant exists in Drive ("Viral Ideas Construction" doc) targeting "home remodeling and construction companies." Not in playbook. Confirm scope or kill.
