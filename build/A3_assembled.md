# Assignment 3: AI Opportunity Portfolio with Maturity Assessment, Competitive Analysis, and Workforce Impact Scan
Nilotpal Choudhury | AIBP Course 3

## Part A: Organisational AI Maturity Assessment

### A1. Define the assessment scope and evidence base

**Assessment scope:** Function.

**Organisation / context label:** Strategy & Analytics, Global Lubricants Sales & Marketing (integrated energy major, anonymised). The assessment covers the function's sales-related workflows, including the leadership-team evidence pack that supports Sales & Marketing decisions.

**Why this is an appropriate scope for you to assess:** I lead the Strategy & Analytics division, which builds reporting and analytics tools for the function and supports its five-year digital roadmap. This gives me a cross-divisional view of sales workflows and stakeholder pain points, but not of the wider enterprise.

**Primary evidence available:** Direct operational knowledge, including a rule-based customer analytics module in production; recurring discussions with more than ten stakeholders across divisions; workflow evidence from Assignments 1 and 2; the Course 3 Module 1 maturity framework (course notes, Module 1); public sources, used only for benchmarking. Colleague ratings: Not evidenced.

**Important evidence limitations:** Ratings rest on one vantage point, my observation and conversations, not a cross-functional assessment; some detail cannot be shared. Divisional performance data is not readily available, so value estimates use stated industry heuristics. Enterprise capabilities (cloud, cybersecurity, compliance) count only where they reach the function. No energy-sector maturity baseline is available to me.

### A2. Six-Dimension AI Maturity Assessment

| Dimension| Sub-dimensions taught in Course 3| Rating H/M/L| Evidence / indicators| Most material gap|
|---|---|---|---|---|
| Technology| Infrastructure; integration; technical debt| Medium| **Infrastructure:** enterprise Azure Data Lake (ADLS), with contracted compute available on request. **Integration:** SAP data increasingly streamed to ADLS and API links built per project, yet order status is still checked manually across SAP, logistics and credit systems. **Technical debt:** many dashboard products lack a clear long-term owner.| Build-for-release delivery: many DIY and IT teams ship products with little attention to sustainability, so adoption collapses when an owner or sponsor moves and unused solutions complicate portfolio rationalisation. Some lead-time fields sit outside the current SAP extract.|
| Data| Quality; accessibility; strategic value| Medium| **Quality:** SAP transactions captured at source for over a decade, so transactional error rates are low. **Accessibility:** platform teams reach data through ADLS, with near-real-time SAP feeds growing; business users building their own tools struggle. **Strategic value:** churn signals are transaction-only, with roughly 1,500 usable churned accounts in one pilot market.| Meaning rather than volume: SAP master data no longer reflects how the business segments customers, so manual tags and SharePoint labels drive analysis. History carries no event labels for global or country-level shocks, limiting ML use, and no churn definition is signed off or owned. Low strategic value offsets good quality and access.|
| Talent| Skills inventory; learning culture; leadership capability| Low| **Skills inventory:** frontline teams are strong in Excel-based performance reporting; data science sits in narrow roles, and delivery relies on 2–3 part-time analysts. **Learning culture:** regular central learning sessions exist but are business-focused, so business teams' digital literacy trails IT and data science. **Leadership capability:** across several projects, ML limits and data-governance needs are underestimated and deployed solutions are assumed to need little upkeep.| Narrow role scopes limit end-to-end capability: data science remains notebook-centric, with little MLOps practice on the existing Databricks platform.|
| Process| Standardisation; documentation; automation baseline| Low| **Documentation:** the ESSA framework (Eliminate, Simplify, Standardise, Automate) and process documents exist but lack governance and accountability. **Standardisation:** order-status and customer updates are manual and inconsistent; complaint-email capture runs against an unmonitored SLA. **Automation baseline:** one governed rule-based churn workflow in production is the exception.| No structured process ownership or governance, so documentation drifts from practice and processes stay unstandardised. Automation built on them cannot perform consistently or last, which materially blocks scaling AI beyond isolated cases.|
| Culture| Experimentation tolerance; data-driven decisions; cross-functional collaboration; visible leadership commitment| Medium| **Experimentation:** innovation is encouraged in principle. **Data-driven decisions:** teams want analysis grounded in data and CRM engagement capture is mandated, but adoption is uneven. **Collaboration:** data is shared reluctantly; Finance and line functions (Sales, Supply Chain) present the same data differently. **Leadership commitment:** Not evidenced beyond stated intent.| Low trust in shared numbers: without common definitions, dashboards serve leadership reporting rather than insight, and teams revert to their own dashboards or SAP extracts. Functions have little incentive to back a central definitions layer, so stated intent outruns observed practice.|
| Governance| Documented AI/data policies; ethics/risk review; clear accountability; incident response and monitoring| Medium| **Ethics/risk review and monitoring:** enterprise cybersecurity and ethics and compliance mechanisms are robust and enforced. **Documented policies:** a data governance council covers transaction data, not the broader signal set. **Accountability:** named data-owner roles proposed; appointment pending. **AI-specific policy and incident response:** Not evidenced.| Weak data and process governance inside the function: no review forum for new signals, and lead-generation pilot governance did not outlast its sponsor. Solutions go stale because data or process changes are not fed back into design.|
| **Overall readiness**| All six dimensions| **Low**| Talent and Process are both Low; under the weakest-dimension rule, readiness is capped by the weakest dimension rather than lifted by stronger Technology and Data (course notes, Module 1).| Talent and Process.|

**Which rating are you least confident about, and what additional evidence would you need to validate or change it?**

Talent (Low). The rating rests on conversations with the stakeholders cited in A1 rather than a skills inventory or survey, so it may reflect the teams I work with most rather than the whole function. Because production work today is mostly dashboards, latent capability is hard to observe. Three pieces of evidence would confirm or change it: a simple skills and AI-literacy inventory across divisions; whether the frontline teams and leaders who receive deployed ML outputs can interpret them and act independently; and an independent six-dimension rating by a colleague outside my division, compared with mine. Even if Talent moved to Medium, Process (Low) would keep overall readiness at Low.

### A3. Industry / peer benchmark

| Benchmark source / peer| What the evidence suggests about AI readiness| Dimension(s) most relevant| Implication for your context|
|---|---|---|---|
| NASSCOM, AI Adoption Index 2.0 (2024): India cross-sector baseline (E1)| Aggregate score 2.47 on a four-point scale, at the Enthusiast stage; data standardisation and AI risk frameworks improving; use-case selection and execution discipline still weak (E1).| Process; Data; Governance| On par on Data and Governance; our Low Process mirrors the sector-wide execution gap, so it is a shared constraint, not a peer disadvantage. National cross-sector index, not energy-specific.|
| Gulf Oil Lubricants India, Annual Report FY2025-26 (2026): domestic lubricants peer (E2)| Salesforce CRM, SAP S/4HANA Cloud and IBP, an enterprise data lake and Power BI dashboards giving real-time sales and channel visibility; early steps to embed AI and machine learning; AI-enabled sales-talent programme (E2).| Technology; Data; Talent| On par on Technology; behind on customer-facing channel data and on structured sales-talent development. Structured AI execution not evidenced.|
| Castrol (bp), Castrol turns 125 (2024): global lubricants peer (E3)| Names end-to-end digital and service solutions and data-centre cooling as growth areas; AI readiness not disclosed (E3).| Technology| No basis for an AI-readiness comparison.|

**Absolute versus relative position:** Absolute: Talent and Process, rated Low in A2, cap our readiness at Low whatever peers do. Relative: we are broadly on par on Technology, Data and Governance but behind Gulf on channel data and sales talent; Culture is not evidenced against any comparator. Implication: closing the Process and Talent gaps matters more than matching peer technology.

### A4. Weakest-dimension diagnosis and readiness priorities

| Constraint| Why it matters| Which opportunities it could block| Priority intervention| Evidence that it has improved|
|---|---|---|---|---|
| **1. Process (Low): standardisation and documentation**| Without documented processes, end-user journeys cannot be mapped, so solutions draw on the wrong sources or sequence, stakeholders dispute insights, and platforms are never embedded in sales and marketing work. Documentation also underpins process governance.| Explainable lead-generation research; LT evidence-pack workflow| Empower Process Excellence to document, with frontline teams, the core sales and marketing excellence processes (an estimated 20–25) in one controlled repository: the single source of truth for process improvement and digital initiatives.| Repository reviewed periodically, certified by the Head of Process Excellence, and used as the baseline for all sales user journeys.|
| **2. Data (Medium): no owned data definitions**| Without standard definitions, data cannot be reused as common data products across platforms; duplicated sources multiply, weakening governance and trust in shared numbers.| Churn early warning; order-status/lead-time exception visibility; sector-matched value cases, including agreed benefit estimates| Appoint a Data Owner to work with Process Excellence and solution and data architects to define the primary transactional sources behind most current dashboards.| Standards held in one repository, required in Software Architecture High-Level Designs (SAHLD) and used in practice.|

**Why Talent (Low) is not a separate constraint:** Clear process and data standards help people understand and use data with confidence, so these two interventions are the most concrete route to upskilling the function.

## Part B: AI Opportunity Portfolio and Sequencing

### B1. Build a 5-7 opportunity portfolio

| #| Opportunity / business problem| Function / workflow| AI pattern| Primary value mechanism| Critical readiness dependency|
|---:|---|---|---|---|---|
| 1| **Churn early warning.** The production rule-based module covers about 50,000 accounts but flags churn only after two years of falling volume, so account plans react too late.| Sales account management and retention: account managers, with customer operations handling lighter-touch outreach| Hybrid: traditional ML (supervised classification) detects early risk signals; GenAI turns flagged accounts into briefs for account managers| Risk: gross margin protected through earlier intervention on at-risk accounts; protected margin, not new revenue| Data: no owned churn definition; signals are transaction-only, with uneven CRM notes and complaints held in email; a single pilot market holds roughly 1,500 churned-account records fit for training|
| 2| **Order-status / lead-time exception visibility.** No single reliable view of order status and inventory across SAP, logistics and credit systems; daily checks are manual, customer updates inconsistent and business is lost when lead times shift.| Sales order-to-delivery customer updates: sales and customer service, with supply chain and logistics| Hybrid: rules/automation roll up status and flag exceptions; traditional ML (regression and classification) predicts lead-time shifts and delay risk| Cost: an estimated 2,000–3,000 sales hours a year released from manual follow-up; fewer missed delivery expectations| Data: over five years of SAP order history, but route, location, segment and logistics-network fields are undefined or outside the SAP extract, with no named owner|
| 3| **Explainable lead-generation research.** A GenAI pilot researches 1,000 to 5,000 event and channel prospects per batch, but its likelihood-to-buy ranking rests wholly on model judgement that sales cannot defend.| Marketing Intelligence prospect research feeding sales follow-up| Hybrid: GenAI for public-source research, summarisation and taxonomy mapping; written scoring rules over fixed features give the High/Medium/Low prospect grade; supervised ML once outcomes are logged| Revenue: a better-qualified pipeline and reproducible, defensible prioritisation; fewer sales hours spent on mis-graded prospects. Quantified value: Not evidenced| Process: pilot never commissioned; no sector taxonomy; prompts held by one data scientist with no versioned repository or review forum|
| 4| **Sector-matched value cases.** Testimonials, reference cases and quantified technical evidence are fragmented and hard to match to a customer's sector, so value propositions stay generic and slow to build.| Sales proposal and value-case preparation for B2B deals| Hybrid: traditional ML (BERT-family text classifiers) tags evidence by sector, application and outcome; GenAI retrieves tagged evidence and drafts through a conversational assistant| Revenue: conversion uplift hypothesis of about 10–15% against the prior-year baseline, unproven until an assisted-versus-unassisted pilot| Data: nothing links technical evidence to application, sector and quantified outcome; documentation patchy; no agreed benefit estimates|
| 5| **LT evidence-pack workflow.** Leadership-team questions on macroeconomic and geopolitical sensitivity need an evidence-backed point of view; analysts research manually, at about 25 analyst-days per request.| Commercial Strategy evidence packs for Global Sales & Marketing leadership decisions (Commercial Strategy Analysts)| Hybrid: read-only agentic GenAI plans research, retrieves from allowlisted sources and drafts; deterministic queries and traditional ML supply figures; human release gate| Cost and speed: target first validated draft in about 15 rather than 25 analyst-days (a target, not achieved); better-evidenced leadership decisions| Process: intake, research and review steps not documented as a controlled process; release depends on analyst validation and manager approval|

### B2. Classify Quick Wins, Strategic Bets and Moonshots

| Opportunity| Classification| Readiness rationale| Time / uncertainty rationale|
|---|---|---|---|
| 1. Churn early warning| Moonshot| A rule-based module exists but covers one market, with almost no data governance; at 1–2% annual churn, a genuine training set needs mapped historical losses plus qualitative attributes.| New attributes need engineering and labelling, so training-data timing, and a global build beyond 12–15 months, is highly uncertain.|
| 2. Order-status / lead-time exception visibility| Strategic Bet| Data (Medium): missing logistics-network attributes can be sourced per market from third-party or transporter data in 6–9 months; selecting the delay-prediction model takes a further 6–9 months.| Third-party extraction is now low-complexity, so a mature-market release within 12–15 months is predictable.|
| 3. Explainable lead-generation research| Strategic Bet| Technology is ready: web-search tooling, curated datasets and partner IT retrieval skills exist, and H/M/L rules are simple. Process is Low: taxonomy, versioned prompts and governance must first be built through functional Excellence teams.| Technical risk is low; timing depends on establishing process ownership, not engineering.|
| 4. Sector-matched value cases| Quick Win| Data (Medium) is mostly in place: source documents exist, though fragmented, and SMEs add bridging knowledge assets. An augmented assistant with front-end vetting keeps people in control, so remaining gaps do not block release.| No significant technical hurdles; deployment within 3–6 months.|
| 5. LT evidence-pack workflow| Strategic Bet| Reuses the lead-generation web-search capability, but needs data governance for explainable financial predictions, orchestrated tool hand-offs and trained human-in-the-loop validators; Process is Low.| Orchestration, regression accuracy and human-in-the-loop capability take time; with a monthly cycle, learning extends beyond 12 months, so uncertainty is relatively high.|

### B3. Sequence the portfolio and select the top three

Sequencing logic: impact weighed against readiness and capability.

| Priority| Opportunity| Why this should move now / next| Readiness condition or dependency| What would change the priority|
|---:|---|---|---|---|
| 1| Sector-matched value cases| Visible, frequent use across sales teams; the smallest data-readiness gap; source content changes rarely, so little immediate governance effort is needed.| A version-controlled knowledge repository with named content owners.| Existing documentation proves poor or incomplete; or a full product-portfolio revamp makes the content obsolete.|
| 2| Explainable lead-generation research| The main gap, governance, can be agreed within a quarter. It follows value cases because batches run less often, so it builds trust in AI more slowly.| Prompts, taxonomy and scoring rules under version control, owned by a named Marketing Intelligence product owner.| Prompt designs vary so much by industry sector that standardisation fails, leaving ad hoc use rather than a governed platform.|
| 3| Order-status / lead-time exception visibility| Cuts the order-update fire-fighting that absorbs sales and customer-operations time, freeing it for revenue conversations.| A cleaned, integrated delivery-level dataset with logistics-network attributes, covering six months per target market.| If order, despatch and credit-block timestamps cannot be joined into one record, the prediction layer fails and the use case reverts to a reporting view rather than AI.|

**Balance:** Value cases deliver early, visible impact and build confidence in AI. Lead generation and order status are capability builds that create the process standards and owned data definitions identified as the two binding constraints in A4. Churn early warning and the LT evidence pack are held back as options, not dropped: they reuse these foundations (governed data products; web-search tooling and process governance) once their triggers are met.

### B4. Cross-functional compound-value check

**Selected opportunity:** Sector-matched value cases (Priority 1).

**Upstream function / AI output it depends on:** Product and technical teams supply well-defined technical literature, customer success stories, equipment-specific recommendation guidelines and product performance analysis, including entry, mainstream and premium tier positioning and the machine-performance reasons to move up a tier. The AI-tagged evidence library built from this content is the upstream output the assistant relies on.

**Downstream function / decision it affects:** Sales teams' choice of the right lubricant for a customer's equipment, and their wallet-expansion offers.

**How value could compound:** Once reliable, the conversational assistant could evolve into a customer self-service offer for routine queries, freeing scarce technical experts for complex problem-solving and for curating the knowledge that improves the assistant further.

**How error or bias could propagate:** If the knowledge repository is not version-controlled, the assistant may recommend withdrawn, discontinued or superseded products. That error passes straight into customer conversations, risking brand erosion and, at worst, lost tenders or product-performance liabilities.

**Control / hand-off needed:** Product or usage recommendations returned with low confidence are escalated to a subject-matter expert before reaching the customer. This depends on named content owners keeping the repository versioned, the readiness condition set in B3.

## Part C: Competitive AI Positioning

### C1. Five-source competitive intelligence scan

| Comparator| Patent / R&D signals| AI hiring signals| Product / deployment signals| Corporate / regulatory filings| CI / other structured intelligence| Overall position|
|---|---|---|---|---|---|---|
| Gulf Oil Lubricants India (domestic peer)| Not evidenced: no attributable G06N filing; Espacenet coverage incomplete (E9)| Not evidenced: no dated AI vacancy on LinkedIn or Indeed| AI insights for account management and sales (E5) (2024); AI sales academy, personalised learning chatbot, AI retail tools (E6) (2025)| Data lake framed as AI foundation; IT spend doubled, not AI-specific (E6). AI budget line, board oversight: Not evidenced| AI-specific: Not evidenced; Tirex acquisition is EV charging (E8) (2023)| Scaling (early, lower confidence)|
| Castrol India (global major)| Not evidenced: no attributable G06N filing (E9)| Not evidenced: no India AI vacancy; group roles excluded| AI supply-chain decisions; Kinaxis planning; GenAI WhatsApp support chatbot, 43,000+ users (E4) (2026)| AI learning via bp platform (E4). AI budget line, board oversight: Not evidenced| AI-specific: Not evidenced; KMS stake is aftermarket services (E7) (2023); bp selling 65% to Stonepeak (E10) (2025)| Scaling (moderate confidence)|

**Which comparator warrants the closest strategic attention, and what combination of signals supports that conclusion?**
Gulf warrants closest attention. Two consecutive annual reports describe AI in sales and account support, sales-talent development and retail tools (E5; E6), the same commercial space as our top three opportunities, and they build on the channel-data lead noted in A3. Castrol's signals are more certain but sit mainly in supply chain (E4). For both, product and filings signals come from the companies' own annual reports, and three of five categories are Not evidenced, so the multiple-signal test is only partly met. Three of Castrol's four positive findings rest on E4 alone, which is newer than A3's source (E3). AI-specific hiring or a dedicated AI line in Gulf's next annual report would raise its position; evidence that its tools remained pilots would lower it.

### C2. AI-enhanced Five Forces scan

| Force| Is AI strengthening or weakening this force?| Are you on the favourable side of the shift?| Most important implication|
|---|---|---|---|
| Barriers to entry| Strengthening: incumbents hold machine and lubricant performance data that a new product-level entrant cannot quickly assemble| Yes| The barrier only protects us if that performance data is clean and usable|
| Buyer power| Strengthening: conversational AI lets buyers research needs and self-diagnose, so they rely less on our representatives| No| Differentiate through customer-linked or bundled solutions, not the product alone|
| Supplier power| Weakening: AI-enabled logistics and procurement intermediaries reduce dependence on traditional providers, though physical reliability still dominates| Partly| Transporters may withhold network data; those with strong data and integration could command a premium and raise our switching costs|
| Threat of substitutes| Strengthening: the lubricant itself is not displaced, but AI diagnostic apps can substitute after-sales and product-linked services; a global peer names digital and service solutions as a growth area (E3)| Yes: our performance data and OEM approvals support better AI-enabled services than app-only entrants can offer| Data quality, user experience and integration across customer touchpoints become core to solution design|
| Competitive rivalry| Strengthening: AI makes insight generation cheaper across domains and channels, raising the minimum standard; a domestic peer is investing in CRM, planning and BI tools (E2)| No| Advantage shifts to acting on insights quickly, not only producing them|

**Which one force is changing most because of AI in your industry, and which opportunity in Part B best responds to that shift?**
Threat of substitutes is changing most. Industrial and OEM customers increasingly judge suppliers on cost-effective solutions built from product-performance insight, and AI diagnostic tools could take over the after-sales advice that currently binds them to us. P4, sector-matched value cases (Priority 1, Quick Win), responds best. It turns our technical literature and customer success stories into sector-specific value propositions, which brings us closer to each B2B customer's operating needs, aligns the portfolio to them and supports customer-linked after-sales service that raises switching costs. Buyer power is a close second in the B2C segment, where self-research weakens our traditional marketing channels; P2, order-status / lead-time exception visibility (Priority 3), is the better response there because reliable availability across channels supports DIY and mechanic purchases.

### C3. Lead / follow / wait positioning for the top three opportunities

| Top-three opportunity| Data moat potential| Regulatory clarity / risk| Organisational readiness| Position| Rationale|
|---|---|---|---|---|---|
| Priority 1: Sector-matched value cases| High: internal customer success stories, technical literature and sector insight| High risk, clear rules: commercial and contract liability if a wrong recommendation is executed, not regulatory exposure| Medium: content exists but is fragmented across sources, with no governance| Lead| Proprietary success stories and technical literature give a moat that compounds once customer feedback on shared value cases flows back. Commercial risk is high but rules are clear; SME sign-off before release contains it. Readiness is Medium; Lead depends on the B3 version-controlled repository.|
| Priority 2: Explainable lead-generation research| Medium: a curated profile layer for industrial customers, not directly linked to conversion| Low: poor output adds manual effort but no financial or legal exposure| Low: Process Low; taxonomy, versioned prompts and governance still to be built; consistent with B2 Process Low| Wait| Maturing LLM features may make research on CRM-logged leads a standard CRM capability, so a separate agent risks wasted effort. Readiness is Low and the moat modest. The B3 governance work (taxonomy, versioned prompts) still proceeds, as any tool needs it.|
| Priority 3: Order-status / lead-time exception visibility| High: integrated internal and logistics-provider data could improve network planning beyond peers| Medium: wrong delay flags cause customer friction; no personal data, so low export-control risk, though contractual checks apply| Medium: control towers using logistics-vendor data run in selected markets| Fast follow| Network-optimisation AI is well established, so the edge lies in integrating logistics-provider data well enough to flag lead-time exceptions accurately. Wrong flags cause customer friction; the data holds no personal information, though contractual and export checks still apply. Readiness is Medium: control towers exist in selected markets.|

### C4. Proprietary-data moat / flywheel test

**Selected opportunity:** P4, sector-matched value cases (Priority 1).

**Does the opportunity generate proprietary data competitors cannot easily obtain?**
Yes. P4 draws on our own product technical literature and customer success stories. The technical reasons behind each customer outcome sit only in company databases and are guarded as trade secrets, so peers cannot rebuild them from public sources.

**Does that data feed a closed-loop system that improves the AI with continued use?**
Not yet; yes by design. The proposed solution would capture SME feedback on low-confidence escalations and bring in performance-analysis data, so that technical knowledge and sector insights are updated with use. This loop is part of the design only and is not built today.

**Does the improving system create switching costs or another compounding advantage?**
Potentially. As answers improve, the system could become a customer self-service and diagnosis tool bundled with our products. That raises loyalty and B2B switching costs, which is the substitutes response set out in C2.

**Conclusion**
Partial/conditional. The proprietary data test is met, but compounding depends on a learning loop that is not yet built, so the moat is potential rather than defensible today.

**What would strengthen or erode the moat?**
Building and running the SME feedback loop, with data governance that keeps recommendation quality high, would strengthen it and could support a move to a customer-facing service. If the loop is never built, or weak governance lets content go stale or leak, P4 is reduced to a copyable content tool.

## Part D: Workforce Impact and Role Redesign

### D1. Select the workforce focus - 3 marks

**Selected opportunity**
P4, sector-matched value cases, our Priority 1.

**Role / role family affected**
Sales Account Manager.

**Why this role is materially affected**
Interviews with sales managers suggest that about 40% of their time goes on administrative work. Most of it is searching for product and customer information needed to answer customer queries or build a value proposition. P4 targets exactly this retrieval and drafting effort.

**Current value bottleneck in the role**
Relevant content is spread across document libraries with no structured ownership, so it goes stale and may not fit the case in hand. Each answer or proposal therefore needs lengthy human checking before analysis can begin.

**What should not be assumed**
P4 is not a headcount-reduction initiative. The aim is to cut administrative retrieval and checking so that account managers spend more time on account planning, account strategy reviews and customer engagement. Any time released is an estimate until it is measured (see D5).

### D2. Task triage: Decompose -> Classify -> Redesign

**Frequency basis.** The frequency categories (High = every customer interaction; Medium = interactions needing a lubrication investigation, a proposal or follow-up; Low = complex investigation scenarios only) are the author's estimates from interviews with sales managers, the same basis as D1. They are event-based, not time-and-motion data, and do not represent shares of total role time.

| #| Discrete task| Current share / frequency| Classification| Why| AI / human boundary|
| ---:| ---| ---| ---| ---| ---|
| 1| Research the customer and site before engagement: summarise its activities, equipment and current lubricant use.| High: before each new customer or site engagement; refreshed for material changes| Augmentable| Retrieval and summarisation can be assisted, but sources may be incomplete or outdated; customer context must be checked before it is used in a formal engagement.| AI drafts a research summary from permitted sources; the human verifies relevance and unknowns before engagement.|
| 2| Agree the engagement scope, attendees and site-access requirements, including safety induction, protective equipment and photography permissions.| High: before each initial site visit; reconfirmed for later visits| Irreducibly human| Agreement and safety accountability depend on people and site-specific conditions, not a deterministic rule set.| Authorised customer representatives confirm scope, permissions and safety requirements with the sales manager, in person or by email or virtual meeting; AI may only draft the visit checklist.|
| 3| Capture the customer's question and pain points, such as equipment failures, lubricant consumption or maintenance difficulties, in a problem brief.| High: each new enquiry and substantive discovery discussion| Augmentable| AI can structure permitted recordings, handwritten notes and customer documents, but the customer's priorities and intended meaning need human confirmation.| AI drafts the brief from permitted notes; the human clarifies ambiguity and confirms the problem with the customer.|
| 4| Compile equipment and operating-condition data: equipment identity, components, duty cycle, manufacturer details, speed, load and temperature.| Medium: per equipment or application assessed; updated when operating conditions change| Augmentable| Structured capture is repeatable, but equipment identity and actual operating conditions need site validation.| AI organises supplied data and flags gaps; the human verifies measurements and equipment identity without inferring missing specifications.|
| 5| Compile the current lubricant inventory and application methods, including supplier, grade, pack information and permitted label photographs.| High: per initial site or equipment assessment; refreshed after product or application changes| Augmentable| Extraction can be assisted (company products from internal systems; competitor products through web search and image extraction), but labels and records may not match actual use.| AI extracts and structures permitted records and images; the human confirms the product in use, competitor details and how it is applied.|
| 6| Record environmental, contamination and maintenance factors, including temperature range, dust and water exposure, drain intervals and maintenance practices.| Low: per complex site assessment; revisited after seasonal or maintenance changes| Irreducibly human| The significance of contamination and maintenance factors depends on site observation and customer practice; AI only structures the record.| AI structures observations and flags missing fields; the human observes, validates conditions and confirms maintenance history.|
| 7| Retrieve and confirm the equipment manufacturer's lubricant requirements, specifications and applicable approvals.| High: per equipment or application recommendation; rechecked when documentation changes| Augmentable| Retrieval is assistable, but document applicability, version and approval scope need technical review; some specifications are not available online and must be compiled by a person.| AI retrieves candidate requirements from approved current sources where available; the human confirms applicability and resolves conflicts before any recommendation.|
| 8| Identify candidate equivalent grades for the current or competitor lubricant using equipment information, manufacturer manuals and approved product-selection resources.| High: per product-conversion or equivalent-grade enquiry| Augmentable| Equivalence depends on operating context and approvals, not name similarity; AI analysis is only as reliable as the in-house technical and performance data behind it.| AI proposes candidates with supporting evidence; a qualified human validates suitability and escalates uncertainty before customer use.|
| 9| Shortlist candidate lubricant grades from the relevant application guides, including mainstream and premium options and documented exceptions.| High: per application-specific recommendation| Augmentable| Search can narrow options from in-house guides and performance data, but guide exceptions and fit to the customer's recorded operating conditions require judgement.| AI retrieves options and exceptions; the human checks current guidance and approves the shortlist.|
| 10| Determine the viscosity grade and required lubricant properties from the equipment's speed, load, lubrication method and temperature.| Medium: per new or materially changed application| Augmentable| Calculations may follow rules, but input validity and application-specific interpretation require expertise.| AI supports calculations using approved methods; a qualified human validates inputs, requirements and the resulting recommendation.|
| 11| Check current technical data sheets for approvals, performance evidence, compatibility limits and documented application cautions.| High: for each shortlisted product before recommendation; rechecked on revision| Augmentable| Extraction is repeatable, but conflicting evidence and application-specific exclusions make unsupervised clearance inappropriate.| AI flags relevant clauses and gaps; the human confirms compliance and refers unresolved cautions to an SME.|
| 12| Review permitted equipment or component images for condition clues and possible lubrication-related damage, where suitable images exist.| Low: per condition or failure enquiry with usable images| Augmentable| Images may be incomplete or misleading; pattern recognition alone does not establish a cause.| AI may flag visual clues for expert review; the human validates findings and seeks inspection or further evidence rather than accepting an AI diagnosis.|
| 13| Review available oil-analysis and condition-monitoring results to assess lubricant condition and possible maintenance actions.| Medium: on receipt of each relevant analysis report or condition alert| Augmentable| Trends can be summarised, but sampling quality, operating history and maintenance consequences require context.| AI summarises trends and anomalies; qualified people interpret the evidence and authorise any maintenance recommendation.|
| 14| Retrieve comparable documented customer-value cases by sector, application, equipment and problem; assess relevance to the shortlisted grade.| High: per value-case or recommendation preparation; repeated if the shortlist changes| Augmentable| Retrieval is assistable, but apparent similarity does not prove that outcomes will transfer.| AI finds and summarises approved cases; the human checks comparability, evidence quality and limits on claims.|
| 15| Obtain expert challenge of the proposed recommendation by sharing a structured case summary with an experienced colleague or technical specialist.| Low: for novel, complex or low-confidence recommendations| Irreducibly human| Independent expert challenge and accountability are the purpose of the task; AI cannot replace that judgement.| AI prepares the case summary and questions; a human specialist challenges and refines the advice; low-confidence recommendations are escalated to an SME.|
| 16| Escalate unclear or failure cases for specialist root-cause assessment, arranging inspection or sample analysis through authorised channels.| Low: whenever unresolved uncertainty or a suspected failure warrants it| Irreducibly human| Escalation urgency, investigation scope and accountability depend on uncertain real-world consequences.| AI assembles the evidence pack; authorised people decide escalation, arrange investigation and approve conclusions.|
| 17| Identify and validate non-lubricant causes and corrective actions, such as alignment, filtration or contamination-control issues.| Medium: per diagnostic case where evidence suggests a non-lubricant contributor| Irreducibly human| Causal judgement needs broader equipment and site context; responsibility for corrective action cannot rest on an unverified inference.| AI organises hypotheses and evidence gaps; qualified people validate causes and agree safe corrective actions.|
| 18| Prepare the customer value case using supported consumption, downtime and component-life inputs; distinguish measured benefits from estimates.| Medium: per qualified proposal needing value justification| Augmentable| AI can assist the arithmetic and draft a first-pass case from standard templates, but attribution, assumptions and relevance to customer outcomes need review.| AI structures the value narrative and calculations; the human validates inputs and claims.|
| 19| Issue the reviewed written recommendation with relevant technical information and limitations, and agree implementation arrangements with the customer.| High: per approved recommendation; revised when the agreed solution changes| Irreducibly human| Customer agreement, explanation of limitations and release accountability depend on relationships and judgement.| AI drafts the communication; an authorised human approves release, explains limitations and secures customer agreement.|
| 20| Coordinate a suitable trial, review performance with the customer and record the validated outcome in a call report or customer-value record.| Medium: per agreed trial, at agreed milestones and close-out| Irreducibly human| Trial decisions and outcome acceptance depend on site context, customer agreement and accountable interpretation.| AI supports tracking and report drafting; authorised people agree trial conditions, review results and validate outcome claims.|

**Evidence and coverage.** The 20 tasks cover the Sales Account Manager workflow from pre-engagement research to trial close-out. The author reviewed and revised the classifications, including task 6 to Irreducibly human and task 12 to Augmentable. No task is classified Automatable, because no step is yet acceptable without human review. Tasks 2, 19 and 20 are kept whole because each has one accountable output: an agreed visit scope, a released recommendation and a validated trial outcome.

### D3. Redesign the role and redeploy capacity

| Current role composition| Redesigned role composition|
| ---| ---|
| **Routine / automatable work now consuming capacity:** collating scattered information and first drafts within D2 tasks 1, 7, 8, 9, 11, 14 and 18. No whole task is Automatable.| **What AI/automation will take over:** collation, summarisation and first-pass analysis. Scope, relevance and sign-off stay human.|
| **Work that remains human-led but AI-augmented:** Augmentable D2 tasks 3, 4, 5, 10, 12 and 13. The manager gathers customer inputs; AI structures them.| **How the human role changes:** less time compiling, more on judgement: validating AI-retrieved technical and competitor data, checking fit-for-purpose properties in performance diagnosis, and weighing trade-offs before deciding.|
| **Higher-value / irreducibly human work currently constrained:** Irreducibly human D2 tasks 2, 6, 15, 16, 17, 19 and 20. Trade-offs and final recommendations suffer because collation crowds out analysis.| **Where released capacity will be redeployed:** evaluating product recommendations and commercial value to grow volume and share of customer portfolio. Part of the gain is offset by verifying AI outputs (tasks 7, 8, 11), SME escalation (tasks 15, 16), training, rework from stale sources and repository upkeep. Net capacity is unquantified; the D1 administrative share is a current-effort estimate, not a saving. No headcount change.|
| **Current success measures:** Deal Conversion Ratio; Product Recommendation Conversion Ratio; number of customer success stories.| **New success measures after redesign:** the same three measures, targeting a 10–15% rise in recorded values, an author target and unproven.|

**What is the single most important role-design change required so that people experience AI as capability expansion rather than role erosion?**
Make AI the account manager's research assistant, not the decision-maker. AI identifies, organises and synthesises qualitative, quantitative and image-based evidence; the manager owns framing the problem, investigating, gathering the missing context and making the trade-offs behind the final recommendation.

### D4. Capability and organisational redesign response

#### D4.1 Emerging AI capability / role family

**Role family:** AI Product Managers.

**Why this role/capability is the current bottleneck:** The P4 assistant must fit how account managers build value cases today, with SME review and approval points built into the experience. Someone must translate that workflow into AI scope across retrieval-based GenAI synthesis and deep-learning image and video processing. Supporting need: AI Systems Engineers to integrate a prototype embedding approval and governance steps.

**Build internally / hire / source externally - and why:** Build internally: existing lubricant-solution product owners gain AI product credentials, and internal AI Systems Engineers are allocated. Hiring would delay a Quick Win; internal owners know the content and can run the SME feedback that keeps it current.

#### D4.2 Role-redesign framework

**Framework selected:** Accenture Transition-Stage.

**Why this framework fits the maturity evidence from Part A and what one structural/organisational change it would prioritise:** Talent and Process are Low, yet the function is pushing from GenAI experiments to agentic AI. Staged capability-building suits this better than sociotechnical redesign or principle-led structure, which assume absent maturity (course notes, Module 3). Priority change: hub-and-spoke, with certified product owners embedded in Sales as AI product managers, drawing standards, engineers and reusable components from the group AI CoE so central expertise does not become a silo.

### D5. Human-AI collaboration evidence plan - 4 marks

Proposed plan only: no trial has been run, and no output reaches a customer before human review. Ten anonymised or synthetic enquiries per condition, matched for difficulty and rotated across conditions; one SME scores outputs blind to condition.

| Condition| What will be measured| Expected learning|
| ---| ---| ---|
| Human alone| SLA time for data collation, proposal build, decision and end to end| Baseline performance|
| AI alone| Same SLA times, plus accuracy, wrong-source count and SME recommendation rating (0-5)| Where AI fails without human context|
| Human + AI| Same measures, plus review, correction and escalation effort| Whether collaboration beats both, and at what review cost|

**Primary metric(s):** Average end-to-end SLA time; accuracy and explainability rated 0-5 by the SME, target at least 4/5.

**Task(s) likely inside AI capability frontier:** D2 tasks 1, 4, 5, 9, 11 and 14, and task 7 for retrieval only: research, data structuring, retrieval and clause extraction.

**Task(s) where human judgement/context remains important:** Tasks 6 and 17 (external conditions versus performance); 10, 13, 15 and 16 (equipment-specific expert guidance); 7 (whether OEM guidance applies); 2 and 19 (customer preferences). Task 7 sits on both sides, illustrating the jagged frontier (course notes, Module 3).

**What result would justify the redesigned collaboration pattern:** Human + AI cuts average end-to-end SLA by 20-40% against the baseline with a rating of at least 4/5, keeping AI as the account manager's research assistant.

**What result would make you redesign the workflow again:** SLA reduction below 20% with a rating below 3/5. Ratings between 3 and 4, or mixed results such as strong SLA gains with a rating below 4, are inconclusive: extend the trial with more cases before deciding.

<div class="pagebreak"></div>

## Submission Checklist

- [ ] My assessment scope is clear and my claims do not exceed the evidence I can credibly access.
- [ ] All six maturity dimensions are rated using the Course 3 sub-dimensions and evidence.
- [ ] I have distinguished self-assessment from industry/peer benchmarking.
- [ ] My portfolio contains 5-7 distinct opportunities and does not force every problem into GenAI.
- [ ] Quick Win / Strategic Bet / Moonshot classifications match readiness and time/uncertainty.
- [ ] My top-three sequence is consistent with Part A maturity constraints.
- [ ] Competitive claims are publicly sourced or marked Not evidenced / Not applicable.
- [ ] I have applied all five competitive-intelligence signal categories without inventing unavailable evidence.
- [ ] Lead / follow / wait positions are initiative-specific and use data moat, regulatory clarity/risk and readiness.
- [ ] My workforce analysis focuses on tasks and role redesign rather than assuming job elimination.
- [ ] I completed at least 15 representative tasks in the task-triage table.
- [ ] Released capacity is deliberately redeployed to higher-value human/augmented work.
- [ ] The selected organisational redesign framework matches Part A maturity.
- [ ] The human-AI evidence plan compares Human alone / AI alone / Human + AI.
- [ ] Assumptions, anonymisation and hypothetical elements are clearly labelled.
- [ ] AI assistance, if used, is disclosed and I remain responsible for the final submission.

## Competitive / Benchmark Evidence Reference Log

| Evidence ID | Organisation / topic | Source title / source type | Date | URL / location if shareable | Used in section |
|---|---|---|---|---|---|
| E1 | NASSCOM | AI Adoption Index 2.0: Tracking India's Sectoral Progress in AI Adoption | 2024 | https://nasscom.in/knowledge-center/publications/ai-adoption-index-20-tracking-indias-sectoral-progress-ai-adoption (findings also reproduced at indiaai.gov.in) | A3 |
| E2 | Gulf Oil Lubricants India Ltd | Gulf Oil Lubricants India Limited Annual Report 2025-26 (PDF pp. 27, 29, 44, 54) | 2026-08 | https://assets.gulfoilltd.com/gulfindia/files/2026-08/GOLIL_Annual_Report_2025-26_0.pdf (listed at https://india.gulfoilltd.com/investors/annual-reports) | A3, C2 |
| E3 | Castrol (bp) | Castrol turns 125 and looks to the future (press release) | 2024-01-10 | https://www.castrol.com/en/global/corporate/about-castrol/newsroom/castrol-125.html | A3, C1, C2 |
| E4 | Castrol India Ltd | CIL Annual Report 2025 (annual report) | 2026-02-25 | https://www.castrol.com/content/dam/castrol/country-sites-new/en_in/india/home/documents/investors/cil-annual-report-2025.pdf | C1 |
| E5 | Gulf Oil Lubricants India Ltd | Annual Report 2023-24 (annual report) | 2024-08-21 | https://assets.gulfoilltd.com/gulfindia/files/2025-05/Gulf%20Oil_Annual%20Report%202023-24.pdf | C1 |
| E6 | Gulf Oil Lubricants India Ltd | Annual Report 2024-25 (annual report) | 2025-09-05 | https://assets.gulfoilltd.com/gulfindia/files/2025-09/Gulf%20Oil%20Lubricants%20India%20Limited%20-%20Annual%20Report%202024-25.pdf?VersionId=DWK7zTpKHEHMm1tUSZ9Lumstc9bdya9C | C1 |
| E7 | Castrol India Ltd | NSE intimation: investment in ki Mobility Solutions (exchange filing) | 2023-01-11 | https://archives.nseindia.com/corporate/CASTROLIND_11012023112638_SEIntimationNitro11Jan2023signed.pdf | C1 |
| E8 | Gulf Oil Lubricants India Ltd | Completion of Tirex Transmission acquisition (exchange filing) | 2023-10-30 | https://assets.gulfoilltd.com/gulfindia/files/2023-10/Acquisition.pdf?VersionId=QZGjj7vg98KK1eSJZAL7XaK3wK_MBVdA | C1 |
| E9 | Google Patents | Google Patents, CPC G06N assignee searches (live database; two queries: Castrol, Gulf Oil) | Undated (live) | https://patents.google.com/?assignee=Castrol&cpc=G06N<br>https://patents.google.com/?assignee=Gulf+Oil&cpc=G06N | C1 |
| E10 | bp plc | bp press release: agreement to sell 65% of Castrol to Stonepeak | 2025-12-24 | https://www.castrol.com/content/dam/castrol/country-sites-new/en_in/india/home/documents/investors/press-release-from-bp-plc.pdf | C1 |

## Academic Integrity and AI-Assistance Disclosure

| Disclosure field | Your response |
|---|---|
| Did you use an AI tool while preparing this assignment? | [ ] No [ ✓] Yes |
| If yes, name the tool(s) and describe how they were used | GitHub Copilot App |
| What did you independently verify or materially revise? | |

## Honour Declaration

- [x] The analysis and judgement in this submission are my own.
- [x] Organisational facts are accurate to the best of my knowledge; estimates, assumptions, anonymisation and hypothetical elements are clearly labelled.
- [x] I have not fabricated benchmark, competitor, patent, hiring, product, filing or other competitive-intelligence evidence.
- [x] I have not disclosed confidential, personal or proprietary information that I am not authorised to share.
- [x] Where I used AI assistance, I have disclosed it above and remain responsible for the final submission.

| Name | Date | Signature / typed acknowledgement |
|---|---|---|
| | | |

## Optional Evidence Appendix

No optional evidence appendix material is included.
