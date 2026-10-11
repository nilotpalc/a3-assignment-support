# G4 author input (PRE-FILLED DRAFT for author review)

Superseded as the primary artefact by `build/g4_author_input_template.md` (filled 11 Oct 2026); kept as the working record. How to read this draft. It follows `build/g4_author_input_template.md` field by field. Text marked **[Evidence candidate]** is paraphrased from Assignment 1, Assignment 2, the ledger or Module 1 notes and must be checked against what is true today. Text marked **[Author decision]** is a rating, choice or position that only you can make; none has been filled in. Delete the markers once you have confirmed or replaced each item. Nothing here is a ledger entry or a gate approval.

Rules carried from the repo: H/M/L only (K4); A1 Red/Amber/Green is legacy evidence, not a rating; no placeholders from A1 ([X]%, [N]); no verbatim quotation of prior work; no detail beyond the anonymisation level already used in Assignments 1 and 2; write "Not evidenced" where you have no evidence.

---

## 0. Process choices

- **Compressed gate plan** (combine G4+G5 and G6+G7 for the 15 Oct deadline): [x] Yes (author, 11 Oct 2026).
- **Course notes:** saved under `course_notes/`; Module 1 file name to be pasted in chat at `/g4-approve`.
- **A3 comparators:** [x] I will name them below (NASSCOM, Castrol, Gulf Oil Lubricants India).

---

## A1. Scope and evidence base (cap 200 words, table cells included)

Status: **Author-confirmed (11 Oct 2026)**, synced from the Notion G4 working page. Ledger rulings in force: K11 and K17. The label below extends K11's wording ("Global Lubricants" added); record this at `/g4-run`.

| Field | Response |
|---|---|
| Assessment scope | Function |
| Organisation / context label (use throughout) | Strategy & Analytics, Global Lubricants Sales & Marketing (integrated energy major, anonymised) |
| Why this is an appropriate scope for me to assess | I lead the Strategy & Analytics division, which builds reporting and analytics tools for the wider function and supports its five-year digital roadmap. This gives me a cross-divisional view of sales-related workflows and the pain points stakeholders raise, without claiming visibility of the wider enterprise. |
| Primary evidence available | Direct operational knowledge, including a rule-based customer analytics module in production; recurring conversations with 10+ stakeholders across divisions; my Assignments 1 and 2 for workflow-level evidence; Course 3 Module 1 framework. Public sources for benchmarking (A3) only. Colleague ratings: Not evidenced. |
| Important evidence limitations | Single vantage point: ratings rest on my observation and conversations, not a cross-functional assessment, and some detail cannot be shared. Divisional performance data is not readily available, so value estimates use stated industry heuristics. Enterprise capabilities (cloud, cybersecurity, compliance) are counted only as they reach the function. No energy-sector maturity baseline yet. |

---

## A2. Six-dimension maturity (H/M/L only; cap 150 words after the table for the least-confident note)

Status: **Author-confirmed (11 Oct 2026)**, synced from the Notion G4 working page. Ratings are the author's. Technology moved from H to M on review (infrastructure strong; integration and technical debt partial). Process kept at L by the author. Module 1 rule: overall readiness is capped by the weakest dimension.

| Dimension | Sub-dimensions | Rating H/M/L | Indicators / evidence | Most material gap |
|---|---|---|---|---|
| Technology | Infrastructure; integration; technical debt | M | **Infrastructure:** enterprise Azure Data Lake (ADLS) and contracted compute available on request. **Integration:** SAP data increasingly streamed to ADLS and API links built per project, yet order status is still checked manually across SAP, logistics and credit systems. **Technical debt:** many dashboard products with unclear long-term owners. | Technical debt from build-for-release design: products are delivered by many DIY and IT teams with little attention to sustainability, and adoption collapses when an owner or sponsor moves, leaving unused solutions that complicate portfolio rationalisation. Some lead-time fields sit outside the current SAP extract. |
| Data | Quality; accessibility; strategic value | M | **Quality:** SAP transactions captured at source for over a decade, so transactional error rates are low. **Accessibility:** platform teams reach data through ADLS, with near-real-time SAP feeds growing; business users building their own tools struggle. **Strategic value:** churn signals are transaction-only, with about 1,500 usable churned accounts in one pilot market. | Meaning, not volume. SAP master data no longer reflects how the business segments itself, so manual tags and SharePoint labels drive analysis. History carries no event labels for global or country-level shocks, limiting ML use. No signed-off churn definition or accountable definition owner. Low strategic value offsets good quality and accessibility. |
| Talent | Skills inventory; learning culture; leadership capability | L | **Skills inventory:** frontline teams are strong in Excel-based performance reporting; data science sits in narrow roles, and delivery relies on 2–3 part-time analysts. **Learning culture:** regular central learning sessions exist but are business-focused, so digital literacy in business teams trails IT and data science. | Narrow role scopes limit end-to-end capability: data science stays notebook-centric, with little MLOps practice on the existing Databricks platform. **Leadership capability:** across several projects, ML limits and data-governance needs are underestimated, and deployed solutions are assumed to need little ongoing upkeep. |
| Process | Standardisation; documentation; automation baseline | L | **Documentation:** ESSA (Eliminate, Simplify, Standardise, Automate) framework and process documents exist, but lack governance and accountability. **Standardisation:** order-status and customer updates are manual and inconsistent; complaint-email capture runs against an unmonitored SLA. **Automation baseline:** one governed rule-based churn workflow in production is the exception. | No structured process ownership or governance, so documentation drifts from practice and processes are not standardised. Automation built on them cannot perform consistently or last, which materially blocks scaling AI beyond isolated cases. |
| Culture | Experimentation tolerance; data-driven decisions; cross-functional collaboration; visible leadership commitment | M | **Experimentation:** innovation is encouraged in principle. **Data-driven decisions:** teams want analysis grounded in data, and CRM engagement capture is mandated, but adoption is uneven. **Collaboration:** data is shared reluctantly; Finance and line functions (Sales, Supply Chain) present the same data differently. **Leadership commitment:** Not evidenced beyond stated intent. | Low trust in shared numbers. Without common definitions, dashboards serve leadership reporting rather than insight, while teams revert to their own dashboards or SAP extracts. Functions have little incentive to back a central definitions layer, so stated intent outruns observed practice. |
| Governance | Documented AI/data policies; ethics/risk review; clear accountability; incident response and monitoring | M | **Ethics/risk review and monitoring:** enterprise cybersecurity and ethics & compliance mechanisms are robust and enforced. **Documented policies:** a data governance council covers transaction data, not the broader signal set. **Accountability:** named data-owner roles proposed, appointment pending. **AI-specific policy and incident response:** Not evidenced. | Weak data and process governance inside the function: no review forum for new signals, and pilot governance did not outlast its sponsor in the lead-generation case. Solutions go stale because data or process changes are not fed back into design. |

- **Least-confident rating:** Talent (Low).
- **Why I am unsure:** it rests on conversations with roughly ten colleagues, not on a skills inventory or survey, so it may reflect the teams I work with most rather than the whole function. Production today is mostly dashboards, which reveals little about latent capability.
- **Evidence that would confirm or change it:** a simple skills and AI-literacy inventory across divisions; whether deployed ML outputs are used by frontline teams and leaders who can interpret them and act independently; and an independent rating of all six dimensions by a colleague outside my division, compared with mine. With Talent and Process at Low, overall readiness is capped at Low regardless of stronger infrastructure.

---

## A3. Industry / peer benchmark (cap 250 words, table cells included; distinct from the C1 competitor scan)

Status: **Author-drafted (11 Oct 2026)**, synced from the Notion G4 working page after review. Comparators are the author's. Columns follow the worksheet (Implication for my context included). About 226 words. Author confirmed the bp and Gulf findings against the sources (11 Oct 2026); the bp.com link did not resolve, so a republished copy is cited.

| Benchmark source / peer | Source link or citation | What it suggests about AI readiness | Most relevant dimension(s) | Implication for my context |
|---|---|---|---|---|
| NASSCOM, India enterprise baseline | AI Adoption Index 2.0, NASSCOM, 2024, [nasscom.in/knowledge-center/publications/ai-adoption-index-20-tracking-indias-sectoral-progress-ai-adoption](https://nasscom.in/knowledge-center/publications/ai-adoption-index-20-tracking-indias-sectoral-progress-ai-adoption), accessed 11 Oct 2026 | India's aggregate AI maturity is 2.47 (Enthusiast stage). Data standardisation and AI risk frameworks are improving; use-case selection and execution discipline need urgent attention. | Process; Data; Governance | Data, Governance: on par. Process (L) mirrors the sector-wide execution gap. Talent: not compared. |
| Castrol (bp), lubricants peer | Castrol turns 125, looks to the future with new strategy, bp press release, 10 Jan 2024; republished at [hellenicshippingnews.com/castrol-turns-125-looks-to-the-future-with-new-strategy](https://www.hellenicshippingnews.com/castrol-turns-125-looks-to-the-future-with-new-strategy/), accessed 11 Oct 2026 | Growth plan names end-to-end digital and service solutions and data-centre cooling; discloses no AI capability or maturity. | Technology | Digital intent only; no basis for an AI-readiness comparison. |
| Gulf Oil Lubricants India, domestic peer | Annual Report FY2024-25, Gulf Oil Lubricants India Ltd, Jul 2025, [india.gulfoilltd.com/investors/annual-reports](https://india.gulfoilltd.com/investors/annual-reports), accessed 11 Oct 2026 | Digital tools for sales tracking, forecasting and BI; Gulf-ACE and Gulf One SuperApp channels; Salesforce and SAP Cloud performance monitoring; leaders exploring generative AI in marketing and strategy. | Technology; Data; Process | Technology: on par. Data: peer appears ahead on customer-facing channel data. Structured AI execution: not evidenced. |

- **Your view of relative position** (ahead / on par / behind, and on which dimensions): Absolute: A2 rates Talent and Process Low, capping readiness at Low. Relative: on par with India's enterprise baseline on Data and Governance; Process Low reflects a sector-wide execution gap; behind Gulf on customer-facing channel data; Castrol offers no basis for comparison. Talent and Culture: not evidenced against any comparator.

---

## A4. Weakest-dimension diagnosis (cap 250 words, table cells included)

Status: **Author-drafted (11 Oct 2026)**, synced from the Notion G4 working page after review; wording tightened to fit the cap (about 205 words). Constraints are the author's: Data (M) chosen over Talent (L) as constraint 1, with the rationale stated in the table (author judgement, 11 Oct 2026). To log at `/g4-run`: "20–25 processes" as an assumption.

| Constraint (1, optional 2) | Why it matters | Shortlisted opportunities it could block | Priority intervention | Observable evidence it has improved |
|---|---|---|---|---|
| Data (M): no owned data definitions | Without standard definitions, data cannot be reused as common data products across platforms; duplicated sources multiply, weakening data governance and trust in shared numbers. Chosen over Talent (L) because actions are easier to define, and clear data and process standards help people understand and use data with confidence, supporting upskilling. | Churn early warning; order-status/lead-time exception visibility; sector-matched value cases (including agreed benefit estimates) | Appoint a Data Owner who works with Process Excellence and solution and data architects to define the primary transactional sources behind most current dashboards. | Standards held in one repository, required in Software Architecture High Level Designs (SAHLD) and used on the ground. |
| Process (L): standardisation and documentation | Without documented processes, end-user journeys cannot be mapped, so solutions use the wrong sources or sequence, stakeholders dispute insights, and platforms are not embedded in sales and marketing work. Documentation also underpins process governance. | Explainable lead-generation research; LT evidence-pack workflow | Empower Process Excellence to work with frontline teams to document the core sales and marketing excellence processes (estimated 20–25) in a controlled repository: the single source of truth for process improvement and digital initiatives. | Repository reviewed periodically, certified by the Head of Process Excellence, and used as the baseline for all sales user journeys. |

Shortlisted opportunities, for reference: churn early warning; order-status/lead-time exception visibility; explainable lead-generation research; sector-matched value cases; LT evidence-pack workflow (R4). The G3 provisional B3 preference (explainable lead-generation research, then LT evidence-pack workflow, then churn early warning) is not final and should be reconfirmed after A2/A4.

---

## Optional, to get ahead (needed for G5/G7, not G4)

- **Part D sales role** (K17 keeps Commercial Strategy Analyst open as an option): **[Author decision]**
- **15–20 real, representative tasks for that role:** **[Author input needed]**. Sales roles have thinner task evidence in A1/A2 (K17).

---

## Open points for you before handing this to the agent

1. ~~Settle the scope label wording (A1).~~ Done: see A1 label.
2. ~~Decide whether to use the compressed gate plan.~~ Yes.
3. Confirm each evidence candidate is still true. A1 and A2 describe the position at the time of writing.
4. ~~Resolve the A3 and A4 confirmation points.~~ Done (11 Oct 2026).
