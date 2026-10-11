# G4 author input template (scope and Part A)

Fill this in and paste it into chat, or save it and point the agent to it. Notes, bullets and fragments are fine; the agent drafts the prose. Every rating, choice and comparator here is your judgement, and none will be filled in for you. Where you have no evidence, write "Not evidenced".

Do not add confidential, personal or proprietary detail beyond the anonymisation level already used in Assignments 1 and 2.

---

## 0. Process choices

- **Compressed gate plan** (combine G4+G5 and G6+G7 for the 15 Oct deadline): [x] Yes [ ] No
- **Course notes:** Module 1 (maturity indicators) is needed for A2/A4. Saved under `course_notes/`? [x] Yes, file name: to be pasted in chat at `/g4-approve` [ ] Will paste in chat
- **A3 comparators:** [x] I will name them below (already included in A3) [ ] Agent may propose public candidates for my choice

---

## A1. Scope and evidence base (cap 200 words; feeds every section)

Current ledger rulings: K11 says the scope is Strategy & Analytics within Global Sales & Marketing, using sales-related workflows. K17 says R4 stays in scope.

- **Assessment scope (tick one):** [ ] Whole organisation [ ] Business unit/division [x] Function [ ] Representative/anonymised context
- **Organisation / context label** (exact wording to use throughout): Strategy & Analytics, Global Lubricants Sales & Marketing (integrated energy major, anonymised)
- **Why this scope is appropriate for you to assess** (role, tenure, vantage point): I lead the Strategy & Analytics division, which builds reporting and analytics tools for the wider function and supports its five-year digital roadmap. This gives me a cross-divisional view of sales-related workflows and the pain points stakeholders raise, without claiming visibility of the wider enterprise.
- **Primary evidence available** (direct operational knowledge, internal process documents, published reports, colleague input, public sources): Direct operational knowledge, including a rule-based customer analytics module in production; recurring conversations with 10+ stakeholders across divisions; my Assignments 1 and 2 for workflow-level evidence; Course 3 Module 1 framework. Public sources for benchmarking (A3) only. Colleague ratings: Not evidenced.
- **Important evidence limitations** (what you cannot see or infer): Single vantage point: ratings rest on my observation and conversations, not a cross-functional assessment, and some detail cannot be shared. Divisional performance data is not readily available, so value estimates use stated industry heuristics. Enterprise capabilities (cloud, cybersecurity, compliance) are counted only as they reach the function. No energy-sector maturity baseline yet.

---

## A2. Six-dimension maturity (H/M/L only; A1 RAG ratings are not carried over, per K4)

For each dimension, give a rating and 1–3 concrete indicators: an observed practice, system or artefact, preferably tied to a sub-dimension. Then name the single most material gap.

| Dimension | Sub-dimensions | Rating H/M/L | Indicators / evidence (bullets ok) | Most material gap |
|---|---|---|---|---|
| Technology | Infrastructure; integration; technical debt | M | **Infrastructure:** enterprise Azure Data Lake (ADLS) and contracted compute available on request. **Integration:** SAP data increasingly streamed to ADLS and API links built per project, yet order status is still checked manually across SAP, logistics and credit systems. **Technical debt:** many dashboard products with unclear long-term owners. | Technical debt from build-for-release design: products are delivered by many DIY and IT teams with little attention to sustainability, and adoption collapses when an owner or sponsor moves, leaving unused solutions that complicate portfolio rationalisation. Some lead-time fields sit outside the current SAP extract. |
| Data | Quality; accessibility; strategic value | M | **Quality:** SAP transactions captured at source for over a decade, so transactional error rates are low. **Accessibility:** platform teams reach data through ADLS, with near-real-time SAP feeds growing; business users building their own tools struggle. **Strategic value:** churn signals are transaction-only, with about 1,500 usable churned accounts in one pilot market. | Meaning, not volume. SAP master data no longer reflects how the business segments itself, so manual tags and SharePoint labels drive analysis. History carries no event labels for global or country-level shocks, limiting ML use. No signed-off churn definition or accountable definition owner. Low strategic value offsets good quality and accessibility. |
| Talent | Skills inventory; learning culture; leadership capability | L | **Skills inventory:** frontline teams are strong in Excel-based performance reporting; data science sits in narrow roles, and delivery relies on 2–3 part-time analysts. **Learning culture:** regular central learning sessions exist but are business-focused, so digital literacy in business teams trails IT and data science. | Narrow role scopes limit end-to-end capability: data science stays notebook-centric, with little MLOps practice on the existing Databricks platform. **Leadership capability:** across several projects, ML limits and data-governance needs are underestimated, and deployed solutions are assumed to need little ongoing upkeep. |
| Process | Standardisation; documentation; automation baseline | L | **Documentation:** ESSA (Eliminate, Simplify, Standardise, Automate) framework and process documents exist, but lack governance and accountability. **Standardisation:** order-status and customer updates are manual and inconsistent; complaint-email capture runs against an unmonitored SLA. **Automation baseline:** one governed rule-based churn workflow in production is the exception. | No structured process ownership or governance, so documentation drifts from practice and processes are not standardised. Automation built on them cannot perform consistently or last, which materially blocks scaling AI beyond isolated cases. |
| Culture | Experimentation tolerance; data-driven decisions; cross-functional collaboration; visible leadership commitment | M | **Experimentation:** innovation is encouraged in principle. **Data-driven decisions:** teams want analysis grounded in data, and CRM engagement capture is mandated, but adoption is uneven. **Collaboration:** data is shared reluctantly; Finance and line functions (Sales, Supply Chain) present the same data differently. **Leadership commitment:** Not evidenced beyond stated intent. | Low trust in shared numbers. Without common definitions, dashboards serve leadership reporting rather than insight, while teams revert to their own dashboards or SAP extracts. Functions have little incentive to back a central definitions layer, so stated intent outruns observed practice. |
| Governance | Documented AI/data policies; ethics/risk review; clear accountability; incident response and monitoring | M | **Ethics/risk review and monitoring:** enterprise cybersecurity and ethics & compliance mechanisms are robust and enforced. **Documented policies:** a data governance council covers transaction data, not the broader signal set. **Accountability:** named data-owner roles proposed, appointment pending. **AI-specific policy and incident response:** Not evidenced. | Weak data and process governance inside the function: no review forum for new signals, and pilot governance did not outlast its sponsor in the lead-generation case. Solutions go stale because data or process changes are not fed back into design. |

- **Least-confident rating:** Talent (Low).
- **Why you are unsure:** it rests on conversations with roughly ten colleagues, not on a skills inventory or survey, so it may reflect the teams I work with most rather than the whole function. Production today is mostly dashboards, which reveals little about latent capability.
- **Evidence that would confirm or change it:** a simple skills and AI-literacy inventory across divisions; whether deployed ML outputs are used by frontline teams and leaders who can interpret them and act independently; and an independent rating of all six dimensions by a colleague outside my division, compared with mine. With Talent and Process at Low, overall readiness is capped at Low regardless of stronger infrastructure.

---

## A3. Industry / peer benchmark (cap 250 words; distinct from the C1 competitor scan)

Name one industry baseline or one or two peers. Public sources only, with a link or citation.

| Benchmark source / peer | Source link or citation | What it suggests about AI readiness | Most relevant dimension(s) |
|---|---|---|---|
| NASSCOM, India enterprise baseline | AI Adoption Index 2.0, NASSCOM, 2024, [nasscom.in/knowledge-center/publications/ai-adoption-index-20-tracking-indias-sectoral-progress-ai-adoption](https://nasscom.in/knowledge-center/publications/ai-adoption-index-20-tracking-indias-sectoral-progress-ai-adoption), accessed 11 Oct 2026 | India's aggregate AI maturity is 2.47 (Enthusiast stage). Data standardisation and AI risk frameworks are improving; use-case selection and execution discipline need urgent attention. | Process; Data; Governance |
| Castrol (bp), lubricants peer | Castrol turns 125, looks to the future with new strategy, bp press release, 10 Jan 2024; republished at [hellenicshippingnews.com/castrol-turns-125-looks-to-the-future-with-new-strategy](https://www.hellenicshippingnews.com/castrol-turns-125-looks-to-the-future-with-new-strategy/), accessed 11 Oct 2026 | Growth plan names end-to-end digital and service solutions and data-centre cooling; discloses no AI capability or maturity. | Technology |
| Gulf Oil Lubricants India, domestic peer | Annual Report FY2024-25, Gulf Oil Lubricants India Ltd, Jul 2025, [india.gulfoilltd.com/investors/annual-reports](https://india.gulfoilltd.com/investors/annual-reports), accessed 11 Oct 2026 | Digital tools for sales tracking, forecasting and BI; Gulf-ACE and Gulf One SuperApp channels; Salesforce and SAP Cloud performance monitoring; leaders exploring generative AI in marketing and strategy. | Technology; Data; Process |

- **Your view of relative position** (ahead / on par / behind the comparator, and on which dimensions): Absolute: A2 rates Talent and Process Low, capping readiness at Low. Relative, by comparator: NASSCOM: on par on Data and Governance; our Process Low mirrors the sector-wide execution gap. Gulf: on par on Technology; behind on customer-facing channel data; its structured AI execution is not evidenced. Castrol: digital intent only, so no basis for an AI-readiness comparison. Talent and Culture: not evidenced against any comparator.

---

## A4. Weakest-dimension diagnosis (cap 250 words)

These should follow from your A2 and A3 answers. The agent can propose options once A2 is settled.

| Constraint (1, optional 2) | Why it matters | Shortlisted opportunities it could block | Priority intervention | Observable evidence it has improved |
|---|---|---|---|---|
| Data (M): no owned data definitions | Without standard definitions, data cannot be reused as common data products across platforms; duplicated sources multiply, weakening data governance and trust in shared numbers. Chosen over Talent (L) because actions are easier to define, and clear data and process standards help people understand and use data with confidence, supporting upskilling. | Churn early warning; order-status/lead-time exception visibility; sector-matched value cases (including agreed benefit estimates) | Appoint a Data Owner who works with Process Excellence and solution and data architects to define the primary transactional sources behind most current dashboards. | Standards held in one repository, required in Software Architecture High Level Designs (SAHLD) and used on the ground. |
| Process (L): standardisation and documentation | Without documented processes, end-user journeys cannot be mapped, so solutions use the wrong sources or sequence, stakeholders dispute insights, and platforms are not embedded in sales and marketing work. Documentation also underpins process governance. | Explainable lead-generation research; LT evidence-pack workflow | Empower Process Excellence to work with frontline teams to document the core sales and marketing excellence processes (estimated 20–25) in a controlled repository: the single source of truth for process improvement and digital initiatives. | Repository reviewed periodically, certified by the Head of Process Excellence, and used as the baseline for all sales user journeys. |

Shortlisted opportunities, for reference: churn early warning; order-status/lead-time exception visibility; explainable lead-generation research; sector-matched value cases; LT evidence-pack workflow (R4).

---

## Optional, to get ahead (needed for G5/G7, not G4)

- **Part D sales role** (K17 keeps Commercial Strategy Analyst open as an option):
- **15–20 real, representative tasks for that role:**
