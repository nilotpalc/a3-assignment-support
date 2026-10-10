# G4 author input (PRE-FILLED DRAFT for author review)

How to read this draft. It follows `build/g4_author_input_template.md` field by field. Text marked **[Evidence candidate]** is paraphrased from Assignment 1, Assignment 2, the ledger or Module 1 notes and must be checked against what is true today. Text marked **[Author decision]** is a rating, choice or position that only you can make; none has been filled in. Delete the markers once you have confirmed or replaced each item. Nothing here is a ledger entry or a gate approval.

Rules carried from the repo: H/M/L only (K4); A1 Red/Amber/Green is legacy evidence, not a rating; no placeholders from A1 ([X]%, [N]); no verbatim quotation of prior work; no detail beyond the anonymisation level already used in Assignments 1 and 2; write "Not evidenced" where you have no evidence.

---

## 0. Process choices

- **Compressed gate plan** (combine G4+G5 and G6+G7 for the 15 Oct deadline): [ ] Yes [ ] No — **[Author decision]**. The ledger (K13) allows it only with your consent. The deadline is 5 days away, and you still have Parts B, C and D after this.
- **Course notes:** Module 1 is already saved: [x] Yes, file name: `course_notes/c3-module 1-ai-maturity.md` (K7 records it as supplied).
- **A3 comparators:** [ ] I will name them below [ ] Agent may propose public candidates for my choice — **[Author decision]**. Starting points are in A3.

---

## A1. Scope and evidence base (cap 200 words, table cells included)

Ledger rulings in force: K11 (Strategy & Analytics within Global Sales & Marketing, using sales-related workflows) and K17 (R4 stays in scope).

- **Assessment scope (tick one):** **[Author decision]**. Candidate reading of K11 is "Function", with the function being Strategy & Analytics, but you must tick it.
- **Organisation / context label** (exact wording to use throughout): **[Author decision]**. One wording conflict to settle. Assignments 1 and 2 label the function "Strategy and Analytics (Global Lubricants)" and the organisation as an integrated oil and gas energy major (global lubricants division). K11 says the scope sits within Global Sales & Marketing. Pick one label and use it in every section.
- **Why this scope is appropriate for you to assess** (role, tenure, vantage point): **[Evidence candidate]**
  - You lead development of reporting and analytics tools for the function.
  - You support the global marketing function on its five-year digital strategy roadmap.
  - Add your tenure and vantage point in your own words (not evidenced in the repo files).
- **Primary evidence available:** **[Evidence candidate]**
  - Direct operational knowledge of the rule-based customer analytics module in production (account scale roughly 50,000 accounts).
  - Your own Assignments 1 and 2, covering order-status, churn, lead-generation, sector value-case and evidence-pack workflows.
  - Course 3 Module 1 notes for the six-dimension framework.
  - Public sources (A3 only).
  - Colleague input: Not evidenced yet. See the Module 1 action item at the end of A2.
- **Important evidence limitations:** **[Evidence candidate]**
  - Several ratings rest on your own vantage point, not on a cross-functional assessment.
  - Real values for items A1 left as placeholders are not available, so they are omitted (K10).
  - Energy and lubricants maturity baselines are not evidenced (K7).
  - Anything outside Strategy & Analytics and the sales-related workflows is not visible to you.

---

## A2. Six-dimension maturity (H/M/L only; cap 150 words after the table for the least-confident note)

All ratings are **[Author decision]**. The right-hand column is evidence only. The Module 1 rule applies: overall readiness is capped by the weakest dimension, not the strongest.

| Dimension | Sub-dimensions | Rating H/M/L | Indicators / evidence candidates (verify; rephrase in your words) | Most material gap (your call) |
|---|---|---|---|---|
| Technology | Infrastructure; integration; technical debt | **[Author decision]** | Order status and inventory sit across SAP, logistics and credit systems and are checked manually each day. More than five years of SAP order history is in the central data warehouse. Some lead-time fields (for example manufacturing dependency) are not consistently defined or are outside the current SAP extract. The A2 evidence-pack workflow assumes read-only integration with competitive-intelligence repositories, and integration is the largest expected cost. Infrastructure and compute: Not evidenced. | |
| Data | Quality; accessibility; strategic value | **[Author decision]** | No signed-off churn definition or early-warning attributes. No accountable business owner for the definitions behind the churn signal. Roughly 1,500 usable churned accounts in one pilot market. Training signals are transaction-only and no decision has been tabled to broaden them. Sales engagement capture in the CRM is mandated but adoption and capture are uneven. Approved collateral is scattered. | |
| Talent | Skills inventory; learning culture; leadership capability | **[Author decision]** | Data engineering or data science capacity for the first move is not confirmed and competes with existing reporting work. Resourcing is expected to rely on roughly 2–3 analysts part-time. Skills pyramid, AI literacy and learning culture: Not evidenced. Leadership capability: Not evidenced. | |
| Process | Standardisation; documentation; automation baseline | **[Author decision]** | The current churn workflow is a documented rule-based production process with rules, named ownership and periodic review. Order-status updates and customer updates are manual and inconsistent. Complaint-email capture is manual against an SLA nobody monitors. | |
| Culture | Experimentation tolerance; data-driven decisions; cross-functional collaboration; visible leadership commitment | **[Author decision]** | CRM engagement capture is mandated but adoption is uneven (a data-driven-decision indicator). Pilot-first sequencing and stop thresholds exist in A1 and A2 as design intent, not as observed culture. Leadership commitment and experimentation tolerance: Not evidenced. | |
| Governance | Documented AI/data policies; ethics/risk review; clear accountability; incident response and monitoring | **[Author decision]** | A data governance council exists and is the proposed forum for churn definitions. Governance exists for transaction data but not for the broader signal set. Named owner roles are proposed, with appointment pending. No formal review forum for new signals. Pilot governance did not outlast its sponsor in the lead-generation case. The A1 Red ratings on governance are legacy evidence only and not transferable (K4). | |

Dimensions where evidence is thin and you should either gather something or write "Not evidenced": **Talent** (almost nothing in the repo), **Culture** (mostly design intent), and **Technology infrastructure**.

- **Least-confident rating:** **[Author decision]**
- **Why you are unsure:** **[Author decision]**
- **Evidence that would confirm or change it:** **[Author decision]**. One option straight from the Module 1 action item: ask one colleague outside your function to rate the same six dimensions and compare. The gap shows blind spots, and it is also a credible way to raise evidence quality. Optional and quick; only worth it if you can do it before the deadline.

---

## A3. Industry / peer benchmark (cap 250 words, table cells included; distinct from the C1 competitor scan)

Public sources only, each with a link or citation. Nothing below is verified and no figures are to be used until you have opened the source. The course notes carry these figures, and K8 says to cite them as "course notes" and verify before presenting them as external facts.

| Benchmark source / peer | Source link or citation | What it suggests about AI readiness | Most relevant dimension(s) |
|---|---|---|---|
| **[Author decision]** | | | |
| **[Author decision]** | | | |
| Optional third | | | |

Candidate starting points, to verify and choose from (your selection):
- NASSCOM AI Adoption Index 2024 (named in Module 1 notes; India-grounded, useful as an industry baseline for readiness).
- A public AI-governance survey (PwC 2025 and an EY finding are named in the Module 1 notes; governance baseline).
- Public reports or disclosures from one or two energy or lubricants peers: none identified yet. This is the evidence gap you flagged (K7).

- **Your view of relative position** (ahead / on par / behind, and on which dimensions): **[Author decision]**

---

## A4. Weakest-dimension diagnosis (cap 250 words, table cells included)

This section follows from A2 and A3, so I have not filled it. Once A2 is settled, the repo agent can propose options. For orientation only, the A1/A2 evidence points to blockers that recur across the five shortlisted opportunities. These are unranked candidates, not a diagnosis:

- **Ownership of data definitions** (churn definition and signals): could block churn early warning and the sector-matched value cases.
- **Master-data and SAP extract completeness** (lead-time fields, no named validating owner): could block order-status/lead-time exception visibility.
- **Governance that outlasts a sponsor** (named owner, review forum, access control): could block explainable lead-generation research and the LT evidence-pack workflow.

| Constraint (1, optional 2) | Why it matters | Shortlisted opportunities it could block | Priority intervention | Observable evidence it has improved |
|---|---|---|---|---|
| **[Author decision]** | | | | |
| Optional second | | | | |

Shortlisted opportunities, for reference: churn early warning; order-status/lead-time exception visibility; explainable lead-generation research; sector-matched value cases; LT evidence-pack workflow (R4). The G3 provisional B3 preference (explainable lead-generation research, then LT evidence-pack workflow, then churn early warning) is not final and should be reconfirmed after A2/A4.

---

## Optional, to get ahead (needed for G5/G7, not G4)

- **Part D sales role** (K17 keeps Commercial Strategy Analyst open as an option): **[Author decision]**
- **15–20 real, representative tasks for that role:** **[Author input needed]**. Sales roles have thinner task evidence in A1/A2 (K17).

---

## Open points for you before handing this to the agent

1. Settle the scope label wording (A1): "Strategy and Analytics (Global Lubricants)" versus K11's Global Sales & Marketing framing.
2. Decide whether to use the compressed gate plan.
3. Confirm each evidence candidate is still true. A1 and A2 describe the position at the time of writing.
