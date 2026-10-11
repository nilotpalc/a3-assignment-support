# G5 author input template (Part B: portfolio and sequencing), prefilled from A1/A2

Notes, bullets and fragments are fine; the agent drafts the prose. Where you have no evidence, write "Not evidenced".

**How to read this prefill**
- ▶ marks information carried over from Assignment 1 (A1) or Assignment 2 (A2), rephrased, with the fact ID or section in brackets. Confirm it, edit it or delete it.
- ☐ marks a judgement only you can make: pattern confirmation, classification, rank, B4 choice. Nothing in a ☐ cell has been filled in for you.
- A1 sequencing labels (Now/Next/Later/Park) and A1 Red/Amber/Green ratings are shown as background only. They are not Assignment 3 classifications or ratings (K4, K9).

Do not add confidential, personal or proprietary detail beyond the anonymisation level already used in Assignments 1 and 2. No ROI/NPV, headcount-reduction or vendor-selection content (A2 vendor scoring excluded, K15).

Compressed plan in force: G4+G5 are reviewed together after B4.

---

## Reference from approved Part A (do not edit here; change via the ledger)

- **Overall readiness:** Low (capped by Talent L and Process L). Technology M, Data M, Culture M, Governance M.
- **A4 constraint 1, Process (Low):** blocks explainable lead-generation research and the LT evidence-pack workflow.
- **A4 constraint 2, Data (Medium), no owned definitions:** blocks churn early warning, order-status/lead-time exception visibility, and sector-matched value cases.
- **Portfolio membership (author decision, 2026-10-11):** the five G3 shortlisted opportunities. Reserves (sales administration; standalone CI data product) not added.
- **Provisional top three (G3, to reconfirm in B3):** 1 explainable lead-generation research; 2 LT evidence-pack workflow; 3 churn early warning.

---

## B1. Build a 5–7 opportunity portfolio (no word cap; one concise row each)

- **Portfolio size:** [x] 5, the shortlist only [ ] 6 [ ] 7
- **Reserves added:** none

AI pattern options (worksheet): rules/automation; traditional ML; GenAI; multimodal AI; agentic AI; hybrid (name the parts).

| # | Opportunity / business problem | Function / workflow | AI pattern | Primary value mechanism | Critical readiness dependency |
|---:|---|---|---|---|---|
| 1 | **Churn early warning.** ▶ The production rule-based module across ~50,000 accounts flags churn only after two years of volume decline, so it reacts late; account planning lacks an early-warning signal [A1-009, A1-004, A1 B1.1 #3]. | ▶ Sales account management and retention (account managers; customer operations for lighter-touch outreach) [A1 D1.2] | ▶ A1: traditional ML (supervised classification), recall-tuned, with drivers shown; account briefs kept as a separate GenAI job [A1 B1.1 #3, D1.2]. ☐ Confirm: traditional ML, or hybrid (ML + rules watchlist)? | ▶ Risk: gross margin protected by earlier intervention on at-risk low/mid-volume accounts; margin protected, not new revenue [A1-032]. | ▶ Data (M): no owned churn definition; transaction-only signals (CRM engagement notes uneven, complaints by email, sector drivers undefined); ~1,500 usable churned accounts in one pilot market [A1 A2.3, A1-038]. A4 mapping. |
| 2 | **Order-status / lead-time exception visibility.** ▶ No single reliable real-time view of order status and inventory across SAP, logistics and credit systems, leading to manual daily checks, inconsistent customer updates and lost business when lead times shift [A1-023]. | ▶ Sales order-to-delivery customer updates (sales and customer service, with Supply Chain/logistics) [A1 B1.1 #1] | ▶ A1: rules/automation for status roll-up and exception flags, plus traditional ML (regression) used offline to refresh standard lead times. A live prediction layer was routed away from AI [A1 B1.1, B1.3]. ☐ Confirm: hybrid (rules + traditional ML)? | ▶ Cost: about 2,000–3,000 sales hours a year released from manual follow-up (estimate); secondary: fewer missed expectations once lead-time master data is refreshed [A1-005, A1-030]. ☐ Still valid? | ▶ Data (M): over five years of SAP order history, but location type, segment, product type, route and manufacturing-dependency fields are undefined or outside the SAP extract; no named owner validates them [A1-028, A1 B1.2]. A4 mapping. |
| 3 | **Explainable lead-generation research.** ▶ A GenAI pilot researches 1,000–5,000 event/channel prospects per batch, but its likelihood-to-buy ranking rests wholly on GenAI judgement, which sales cannot defend [A1-011, A1 A1.2, B2.1]. | ▶ Marketing Intelligence prospect research feeding sales follow-up [A1 B2.1] | ▶ A1: hybrid. GenAI for public-source research, summarisation and taxonomy mapping; written scoring rules over five fixed features for the H/M/L rating; supervised upgrade later as outcomes are logged [A1 B2.1]. ☐ Confirm. | ▶ Revenue: better-qualified pipeline and defensible, reproducible prioritisation; fewer sales hours lost on wrong "High" prospects [A1 B2.1]. No quantified value in A1; ☐ add one or write "Not evidenced". | ▶ Process (L): pilot never commissioned; no sector taxonomy; prompts held by one data scientist with no versioned repository or review forum; governance did not outlast the sponsor [A1 A2.3]. A4 mapping. |
| 4 | **Sector-matched value cases.** ▶ Proof points (testimonials, reference cases, quantified technical evidence) are fragmented and hard to match to a customer's sector, so value propositions stay generic and slow [A1-027]. | ▶ Sales proposal and value-case preparation for B2B deals [A1 B1.1 #5] | ▶ A1: GenAI (retrieval over tagged evidence + drafting); first move is tagging with a named content owner [A1 B1.1 #5]. ☐ Confirm GenAI, or hybrid (tagging/rules + GenAI)? | ▶ Revenue: conversion uplift hypothesis of about 10–15% versus prior-year baseline; explicitly unproven until an assisted vs unassisted pilot [A1-006, A1-034]. ☐ Keep as hypothesis, or drop the figure? | ▶ Data (M): nothing links technical evidence to application, sector and quantified outcome; documentation patchy; no agreed benefit estimates [A1 D1.3, B1.1 #5]. A4 mapping. |
| 5 | **LT evidence-pack workflow (R4).** ▶ Leadership-team questions on macro/geopolitical sensitivity need an evidence-backed point of view; analysts research manually, at ~25 analyst-days per request [A2 A1, A2-001]. | ▶ Commercial Strategy evidence packs for Global S&M leadership decisions (Commercial Strategy Analysts) [A2-005; K17] | ▶ A2: agentic AI, augmented and read-only (plans research, retrieves from allowlisted sources, drafts); deterministic queries/ML for figures; human release gate [A2 A4.2, D1]. ☐ Confirm: agentic AI, or hybrid (agentic GenAI + traditional ML + human)? | ▶ Cost/speed: target first validated draft in ~15 vs ~25 analyst-days (target, not achieved); better-evidenced LT decisions [A2-010]. ☐ Still valid? | ▶ Process (L): intake, research and review steps not documented as a controlled process; release depends on analyst validation and manager approval [A2 A2, D2]. A4 mapping. |

---

## B2. Classify Quick Wins, Strategic Bets and Moonshots (max 50 words per opportunity across the two rationale cells)

Worksheet definitions:
- **Quick Win:** impact in roughly 3–6 months with most required readiness already in place.
- **Strategic Bet:** significant potential value with capability-building required.
- **Moonshot:** potentially transformational, high uncertainty and longer horizon (often 12–24 months), requiring strength across most or all readiness dimensions.

QA rule: a Quick Win whose dependency is rated Low is blocked. A Quick Win on a Medium dependency needs an explicit rationale for why readiness is "mostly in place".

| # | Opportunity | Classification (QW / SB / MS) | Readiness rationale | Time / uncertainty rationale |
|---:|---|---|---|---|
| 1 | Churn early warning | ☐ | ☐ | ☐ |
| 2 | Order-status / lead-time exception visibility | ☐ | ☐ | ☐ |
| 3 | Explainable lead-generation research | ☐ | ☐ | ☐ |
| 4 | Sector-matched value cases | ☐ | ☐ | ☐ |
| 5 | LT evidence-pack workflow (R4) | ☐ | ☐ | ☐ |

**Prior evidence you can draw on (background, not classifications):**
- **#1 Churn:**
  - ▶ Rule-based module already in production, a reusable base [A1-009].
  - ▶ Single-market pilot feasible on ~1,500 churned accounts [A1-050].
  - ▶ Churn-definition/data-dictionary first move estimated at about one month, 200–300 person-hours [A1-007].
  - ▶ Chartered target: 5% relative reduction in churn rate within 12 months of go-live, not achieved [A1-008].
  - ▶ A1 put it "Now" despite Red data/governance readiness. K9 says re-classify under Course 3 definitions.
- **#2 Order status:**
  - ▶ Strongest data history of the five (5+ years of despatch history) but high effort across SAP, logistics and credit [A1-051, A1 D1.3].
  - ▶ The process and master-data fix sits with logistics and SAP master-data owners, to be tabled in the annual planning cycle [A1 B1.3].
- **#3 Lead generation:**
  - ▶ The GenAI pilot already runs (4–5 runs in 12 months; 2–4 batches/month planned) [A1 B2.1].
  - ▶ Simpler hybrid route estimated at 4–6 months to define taxonomy, features, rules and dataset [A1 B2.2].
  - ▶ No labels exist; the customer database records only wins [A1 B2.1].
- **#4 Value cases:**
  - ▶ The revenue hypothesis is unproven.
  - ▶ The readiness block is that no evidence is linked to sector and outcome; a confident error in a customer-facing value case is the live risk [A1 D1.3].
  - ▶ A1 put it "Later".
- **#5 LT evidence pack:**
  - ▶ A2 recommended a controlled pilot with a 90-day plan and a Day-90 decision [A2 D1, A2-012].
  - ▶ Existing research agent and CI vector repository already in place; dashboard connectivity still to be built [A2 A1, B1].
  - ▶ Pilot thresholds were assumptions [A2-008, A2-009].

---

## B3. Sequence the portfolio and select the top three (cap 300 words for the whole section)

- **Top three:** ☐ [ ] Keep the G3 provisional order [ ] Change it (give the new order below)
- **Sequencing logic used:** ☐ [ ] Impact [ ] Readiness/capability [ ] Time to impact [ ] Risk/uncertainty [ ] Strategic significance

Note: G3 #1 and #2 both depend on Process (Low). If they stay first, say why they move now, for example because they run on today's manual process or because they create the process documentation A4 calls for.

| Priority | Opportunity | Why this should move now / next | Readiness condition or dependency (what must be true first) | What would change the priority (a concrete trigger) |
|---:|---|---|---|---|
| 1 | ☐ | ☐ | ☐ | ☐ |
| 2 | ☐ | ☐ | ☐ | ☐ |
| 3 | ☐ | ☐ | ☐ | ☐ |

**Prior evidence for conditions and triggers (background only):**
- ▶ **Lead generation:**
  - Condition: prompts, taxonomy and scoring rules kept under version control and owned by a named product owner in Marketing Intelligence [A1 B2.1].
  - Trigger example: batch outcomes logged well enough to support a supervised upgrade.
- ▶ **LT evidence pack:**
  - Condition: named sponsor and business owner, a guardrail checklist and data-boundary note, and pilot success measures locked before testing [A2 D2].
  - Prior stop/pause signals: any unsupported material recommendation; numerical mismatches above 2%; wrong or missing citations above 5% in two consecutive reports. These were assumptions [A2-007, A2-008, A2-009].
- ▶ **Churn:**
  - Condition: a signed-off churn definition with an appointed data owner; additional signals brought into one governed dataset [A1 A1.2, C2.2].
  - Prior workload trigger: if the low-probability queue breaches its agreed cap, raise the threshold or limit rollout by market [A1 D1.2].
- ▶ **Order status:**
  - A1 trigger: if order, despatch and credit-block timestamps cannot be stitched into one record, drop the prediction layer and ship the status view only [A1 B1.1 #1].
- ▶ **Value cases:**
  - A1 trigger: if the evidence library cannot be shown to be accurate, versioned and owned, step back to governed search with named document owners [A1 B1.1 #2/#5].

- **Balance, 2–3 sentences:** ☐ how the portfolio balances delivery, capability-building and optionality, rather than simply choosing the three easiest projects:

---

## B4. Cross-functional compound-value check (cap 250 words)

Pick one of your top three. A reasoned "Not applicable" is accepted.

- **Selected opportunity:** ☐

**Prior evidence per candidate (background only; choose one and edit):**

- ▶ **Churn early warning:**
  - Upstream: CRM engagement notes (Sales), complaint and escalation emails (customer service), sector and premium-mix drivers defined differently by country [A1 A2.3].
  - Downstream: account-manager retention conversations, and customer-operations outreach for the low band [A1 D1.2].
  - Risk: missed at-risk accounts cost more than false alarms (about 5:1, estimate) [A1-046]. Biased or uneven CRM capture would skew which accounts are flagged.
  - Prior control: monthly review of 10–12 actual churn cases; drift alerts [A1-059, A1-057].
- ▶ **LT evidence pack:**
  - Upstream: transactional sales-history and predictive volume dashboards, plus the CI repository [A2 A1].
  - Downstream: LT strategy decisions.
  - Risk: a persuasive but wrongly evidenced recommendation from missed contradictory evidence or misread dashboard extracts [A2 D1].
  - Prior control: every claim and figure linked to an approved source; analyst validation and manager approval before release [A2 D1, A2 A4.2].
- ▶ **Explainable lead generation:**
  - Upstream: event and channel lead lists plus public-web research (Marketing Intelligence).
  - Downstream: sales prospecting and cold-calling.
  - Risk: a wrong "High" wastes a few hours of calling; the serious harm is a fabricated fact, such as a fleet size, reaching a prospect [A1 B2.1].
  - Prior control: batch reviewed before contact; versioned rules and taxonomy under a named product owner [A1 B2.1].

**Fields to complete for the chosen opportunity:**
- **Upstream function / AI output it depends on:** ☐
- **Downstream function / decision it affects:** ☐
- **How value could compound:** ☐
- **How error or bias could propagate:** ☐
- **Control / hand-off needed:** ☐

---

## Optional, to get ahead (needed for G6/G7, not G5)

- **C1 comparators** (two plus an optional third; may reuse Gulf/Castrol, but C1 needs patent, hiring, product, filings and CI signals rather than a repeat of A3):
- **Part D sales role** (K17 keeps Commercial Strategy Analyst open as an option; A2 names Commercial Strategy Analysts as the primary users of the LT evidence pack [A2-005]):
- **15–20 real, representative tasks for that role:** ▶ A2 lists workflow steps for that role (intake and problem framing; domain scoping and trend research; quantitative validation; point-of-view synthesis and stakeholder alignment), which may seed the list [A2 A2]. ☐ Supply the real tasks.
