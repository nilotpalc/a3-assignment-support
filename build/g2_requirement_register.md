# G2 Requirement Register

Status: extracted from the repository text copies; used as the frozen input to template generation. No assignment response content is included.

## Sources and validation

| Source | Exact text-copy filename | Modified (local) | Pages inferred from form feeds | Citation rule |
|---|---|---:|---:|---|
| WS | `sources_text/IIMK-AIBP-C3-Artefact-ParticipantWorksheet.txt` | 2026-10-10 10:16:46 +05:30 | 15 | Cite printed page where available; otherwise use inferred form-feed page (K18). |
| RB | `sources_text/IIMK-AIBP-C3-ParticipantRubric.txt` | 2026-10-10 10:16:46 +05:30 | 5 | Cite printed page where available; otherwise use inferred form-feed page (K18). |

The original PDFs are not present in this repository; these are the exact provided `sources_text/` text copies, which are the files the repository scripts read. Page citations below use the form-feed boundaries in those copies. Source text was not modified.

## Submission-level requirements

| ID | Source | Requirement (paraphrased) | Type | Marks | Cap / limit |
|---|---|---|---|---:|---|
| R-SUB-01 | WS p.1 | Submit the completed worksheet structure as one PDF; retain all section numbers, response fields and tables, while formatting may be improved. | Mandatory | — | Maximum 20 response pages, excluding references, declaration and optional evidence appendix. |
| R-SUB-02 | WS p.1 | Recommended response length is 16–20 pages. | Recommended | — | 16–20 pages; distinct from the 20-page maximum. |
| R-SUB-03 | WS pp.2–3, 15; RB pp.1, 5 | Content score totals 100; document-level quality modifier ranges +5 to -5; final score is capped at 100 and floored at 0. | Mandatory | 100 + modifier | No response-word cap. |
| R-SUB-04 | WS pp.2–3; RB pp.1, 5 | Quality modifier does not re-score individual criterion weaknesses. | Descriptor | +5 to -5 | No response-word cap. |
| R-SUB-04a | WS p.3; RB p.5 | Exceptional executive artefact: highly specific, coherent, evidence-disciplined, concise and decision-ready. | Descriptor | +5 | Document-level modifier. |
| R-SUB-04b | WS p.3; RB p.5 | Strong professional artefact with very good synthesis, evidence use and cross-section consistency; only minor weaknesses. | Descriptor | +3 to +4 | Document-level modifier. |
| R-SUB-04c | WS p.3; RB p.5 | Above-standard document-level synthesis or usability, though not consistently exceptional. | Descriptor | +1 to +2 | Document-level modifier. |
| R-SUB-04d | WS p.3; RB p.5 | Competent submission meeting normal professional expectations. | Descriptor | 0 | Document-level modifier. |
| R-SUB-04e | WS p.3; RB p.5 | Noticeable document-level weaknesses: avoidable inconsistency, weak synthesis/source discipline or presentation problems. | Descriptor | -1 to -2 | Document-level modifier. |
| R-SUB-04f | WS p.3; RB p.5 | Significant document-level problems: repeated unsupported assertions, major contradictions or serious non-compliance. | Descriptor | -3 to -4 | Document-level modifier. |
| R-SUB-04g | WS p.3; RB p.5 | Material integrity/submission-quality failure: undisclosed fabrication, extensive placeholders, missing declaration, unusable structure or equivalent fundamental problem. | Descriptor | -5 | Document-level modifier. |
| R-SUB-05 | WS pp.1–2; RB p.1 | Use a bounded, consistent scope; distinguish evidence, assumptions and limitations; do not invent organisational facts or disclose restricted personal/confidential/proprietary information. | Mandatory | Cross-cutting | No response-word cap. |
| R-SUB-06 | WS pp.1–2; RB pp.1, 5 | Portfolio and workforce work must stay within the assignment scope; no headcount-reduction plan, investment-grade ROI/NPV, vendor-selection exercise, legal opinion, enterprise governance operating model or production implementation plan is requested. | Mandatory | Cross-cutting | Scope exclusions, not word caps. |

## Part A — Organisational AI Maturity Assessment (25 marks)

| ID | Source | Field/table and requirement (paraphrased) | Type | Marks | Cap / limit |
|---|---|---|---|---:|---|
| R-A-01 | WS p.3; RB p.2 | A1 scope field: identify the assessment scope (whole organisation, business unit/division, function, or representative/anonymised context). | Mandatory | A1 total 3 (shared) | Shared 200-word maximum across table. |
| R-A-02 | WS p.3; RB p.2 | A1 context label field: name/describe the organisation or context. | Mandatory | A1 total 3 (shared) | Shared 200-word maximum across table. |
| R-A-03 | WS p.3; RB p.2 | A1 suitability field: explain why this scope can credibly be assessed. | Mandatory | A1 total 3 (shared) | Shared 200-word maximum across table. |
| R-A-04 | WS p.3; RB p.2 | A1 evidence field: identify available primary evidence. | Mandatory | A1 total 3 (shared) | Shared 200-word maximum across table. |
| R-A-05 | WS p.3; RB p.2 | A1 limitations field: make important evidence limits explicit; claims must not exceed visibility. | Mandatory / Descriptor | A1 total 3 | 200 words maximum across the table. |
| R-A-06 | WS p.4; RB p.2 | A2 six-row table columns: Dimension; Rating H/M/L; Evidence / indicators; Most material gap. Assess Technology, Data, Talent, Process, Culture and Governance using the worksheet sub-dimensions. | Mandatory | A2 total 14 | Table itself uncapped. H/M/L only (K4). |
| R-A-07 | WS p.4; RB p.2 | A2 uncertainty prompt: state the least-confident rating and evidence needed to validate or change it. Ratings should be evidence-backed; distinguish capability, evidence and assumption; openly test uncertainty. | Mandatory / Descriptor | Included in A2 | 150 words maximum after the table. |
| R-A-08 | WS pp.3–4; RB p.2 | A3 benchmark table columns: Benchmark source / peer; What evidence suggests about AI readiness; most relevant dimensions; implication for context. Use industry baseline or 1–2 suitable peers, distinguish absolute readiness from relative position. | Mandatory / Descriptor | A3 total 4 | 250 words maximum across the table. |
| R-A-09 | WS pp.4–5; RB p.2 | A4 diagnosis table columns: Constraint; Why it matters; Which opportunities it could block; Priority intervention; Evidence it has improved. Identify one or two genuine constraints derived from A2/A3. | Mandatory / Descriptor | A4 total 4 | 250 words maximum. |
| R-A-10 | WS pp.3–5; RB p.2 | Part A total and maturity principle: assess readiness across all six dimensions; weak dimensions constrain reliable AI adoption/scaling. | Mandatory / Descriptor | 25 | Part marks: A1 3, A2 14, A3 4, A4 4. |

## Part B — AI Opportunity Portfolio and Sequencing (30 marks)

| ID | Source | Field/table and requirement (paraphrased) | Type | Marks | Cap / limit |
|---|---|---|---|---:|---|
| R-B-01 | WS p.5; RB p.2 | B1 portfolio table columns: #; Opportunity / business problem; Function / workflow; AI pattern; Primary value mechanism; Critical readiness dependency. Include 5–7 distinct credible opportunities; fit AI pattern to problem and connect each to Part A readiness. | Mandatory / Descriptor | B1 total 10 | One concise row per opportunity; no separate business case. Table uncapped. |
| R-B-02 | WS pp.5–6; RB p.2 | B2 classification table columns: Opportunity; Classification; Readiness rationale; Time / uncertainty rationale. Classify each portfolio item as Quick Win, Strategic Bet or Moonshot using course definitions and consistency with Part A. | Mandatory / Descriptor | B2 total 8 | 50 words maximum per opportunity across the rationale columns, including cells (K1). |
| R-B-03 | WS p.6; RB p.3 | B3 top-three table columns: Priority; Opportunity; Why it should move now / next; Readiness condition or dependency; What would change priority. Rank three items using impact, readiness/capability, time, risk/uncertainty and strategic significance; include reprioritisation conditions. | Mandatory / Descriptor | B3 total 8 | 300 words maximum across B3, including its explanation. |
| R-B-04 | WS p.6; RB p.3 | B3 balance prompt: explain in 2–3 sentences how the portfolio balances delivery, capability-building and optionality rather than selecting only the easiest projects. | Mandatory / Descriptor | Included in B3 | Included in the 300-word cap. |
| R-B-05 | WS p.6; RB p.3 | B4 fields: Selected opportunity; Upstream function / AI output it depends on; Downstream function / decision it affects; How value could compound; How error or bias could propagate; Control / hand-off needed. A justified N/A may be used if no meaningful chain exists. | Mandatory / Descriptor | B4 total 4 | 250 words maximum. |
| R-B-06 | WS pp.5–6; RB pp.2–3 | Part B portfolio logic: 5–7 business problems, readiness dependencies, justified classification and deliberate sequence; not an AI-technology list. | Mandatory / Descriptor | 30 | Part marks: B1 10, B2 8, B3 8, B4 4. |

## Part C — Competitive AI Positioning (20 marks)

| ID | Source | Field/table and requirement (paraphrased) | Type | Marks | Cap / limit |
|---|---|---|---|---:|---|
| R-C-01 | WS p.7; RB p.3 | C1 comparison table: Comparator; Patent / R&D signals; AI hiring signals; Product / deployment signals; Corporate / regulatory filings; CI / other structured intelligence; Overall position (Experimenting / Scaling / Embedded). Select two relevant comparators; optional third. Apply five signal categories where available. | Mandatory / Descriptor | C1 total 8 | 350 words maximum including final explanation; cells count toward cap (K1–K2). |
| R-C-02 | WS p.7; RB p.3 | C1 closest-attention prompt: identify comparator warranting closest strategic attention and explain the combination of signals. Trace public claims; overall judgement follows multiple signals. | Mandatory / Descriptor | Included in C1 | Included in 350-word cap. |
| R-C-03 | WS p.7; RB p.3 | C2 Five Forces table columns: Force; Is AI strengthening or weakening this force?; Are you on favourable side of shift?; Most important implication. Cover barriers to entry, buyer power, supplier power, threat of substitutes and competitive rivalry through an AI lens. | Mandatory / Descriptor | C2 total 5 | Table itself uncapped. |
| R-C-04 | WS p.7; RB p.3 | C2 structural-shift prompt: identify the force most changed by AI in the industry and link it to a Part B opportunity. | Mandatory / Descriptor | Included in C2 | 200 words maximum after the table. |
| R-C-05 | WS p.8; RB p.3 | C3 positioning table columns: Top-three opportunity; Data moat potential; Regulatory clarity / risk; Organisational readiness; Position; Rationale. Apply factors per initiative. Use table labels Lead / Fast follow / Wait (K5). | Mandatory / Descriptor | C3 total 4 | 50 words maximum per opportunity rationale, including rationale cell (K1). |
| R-C-06 | WS p.8; RB p.3 | C4 moat test fields: proprietary data competitors cannot easily obtain; data feeding a closed-loop system; improvement creating switching costs/other compounding advantage; conclusion choice; what strengthens/erodes moat. | Mandatory / Descriptor | C4 total 3 | 250 words maximum. |
| R-C-07 | WS pp.7–8; RB pp.3, 5 | Competitive claims use current, identifiable public sources; record source details in evidence log. When evidence/source categories are unavailable or irrelevant, mark Not evidenced / Not applicable rather than inventing signals. | Mandatory / Descriptor | Cross-cutting | No word cap. |
| R-C-08 | WS pp.7–8; RB p.3 | Part C positioning must be initiative-specific and evidence-based; Lead is not inherently superior; conclusion must follow the three-part moat test rather than data volume alone. | Descriptor | 20 | Part marks: C1 8, C2 5, C3 4, C4 3. |

## Part D — Workforce Impact and Role Redesign (25 marks)

| ID | Source | Field/table and requirement (paraphrased) | Type | Marks | Cap / limit |
|---|---|---|---|---:|---|
| R-D-01 | WS p.9; RB p.4 | D1 fields: Selected opportunity; Role / role family affected; Why this role is materially affected; Current value bottleneck in role; What should not be assumed. Link to a top-three opportunity, prefer Priority 1 unless another is better evidenced; focus on activity/value, not job elimination. | Mandatory / Descriptor | D1 total 3 | 200 words maximum. |
| R-D-02 | WS pp.9–10; RB p.4 | D2 task-triage table columns: #; Discrete task; Current share / frequency; Classification; Why; AI / human boundary. Use Automatable, Augmentable or Irreducibly human and the taught classification logic. | Mandatory / Descriptor | D2 total 8 | At least 15 and at most 20 representative task rows in main submission. No word cap. Optional 30–50 task decomposition may be in appendix (K3). |
| R-D-03 | WS p.11; RB p.4 | D3 redesign table fields: Current role composition (routine/automatable; human-led but augmented; higher-value/irreducibly human; current success measures) and Redesigned role composition (what AI/automation takes over; human-role change; capacity redeployment; new success measures). Include the single most important role-design change prompt. | Mandatory / Descriptor | D3 total 5 | 300 words maximum across D3. |
| R-D-04 | WS p.12; RB p.4 | D4.1 select one of six taught emerging AI capability / role families; explain why it is a bottleneck and build internally / hire / source externally with reason. | Mandatory / Descriptor | D4.1: 2 | Joint D4 cap: 200 words maximum across D4. |
| R-D-05 | WS p.12; RB p.4 | D4.2 select one taught framework (Accenture Transition-Stage, MIT Sociotechnical, Deloitte Principle-Based); explain maturity fit and one structural/organisational change it would prioritise. | Mandatory / Descriptor | D4.2: 3 | Joint D4 cap: 200 words maximum across D4. |
| R-D-06 | WS p.12; RB p.4 | D5 test-condition table rows: Human alone; AI alone; Human + AI. Columns: Test condition; What will be measured; Expected learning. | Mandatory / Descriptor | D5 total 4 | 300 words maximum across D5. |
| R-D-07 | WS p.12; RB p.4 | D5 decision fields: Primary metric(s); Task(s) likely inside AI capability frontier; Task(s) where human judgement/context remains important; result justifying collaboration pattern; result triggering redesign. Compare meaningful outcomes and allow any of the three conditions to perform best. | Mandatory / Descriptor | Included in D5 | Included in 300-word cap. |
| R-D-08 | WS pp.9–12; RB p.4 | Part D principle: redesign at task level; state where capacity goes and how success measures change; do not assume workforce reduction. | Mandatory / Descriptor | 25 | Part marks: D1 3, D2 8, D3 5, D4 5, D5 4. |

## Unscored mandatory structure and integrity fields

| ID | Source | Requirement | Type | Marks | Cap / limit |
|---|---|---|---|---:|---|
| R-X-01 | WS p.13 | Preserve all 16 submission checklist statements and their checkboxes as a checklist. | Mandatory | — | No cap. |
| R-X-02 | WS p.13 | Preserve the Competitive / Benchmark Evidence Reference Log with E1–E8 rows and columns Evidence ID; Organisation / topic; Source title / source type; Date; URL / location if shareable; Used in section. | Mandatory | — | Excluded from page limit. |
| R-X-03 | WS p.14 | Preserve the AI-use disclosure instructions and fields: Did you use an AI tool?; If yes, name tools and describe use; What did you independently verify or materially revise? | Mandatory | — | No cap; author only completes. |
| R-X-04 | WS p.14 | Preserve the five honour-declaration checkboxes plus Name, Date and Signature / typed acknowledgement fields. | Mandatory | — | No cap; never pre-complete, tick, sign or date. |
| R-X-05 | WS p.15; RB p.1 | Preserve participant-facing scoring summary / score rules as part of the worksheet structure. | Mandatory | — | No response cap. |

## Marks and response-budget inventory

### Marks

| Part / criterion | WS marks | RB marks | Checker result |
|---|---:|---:|---|
| A1 / A2 / A3 / A4 | 3 / 14 / 4 / 4 | 3 / 14 / 4 / 4 | Match; A total 25 |
| B1 / B2 / B3 / B4 | 10 / 8 / 8 / 4 | 10 / 8 / 8 / 4 | Match; B total 30 |
| C1 / C2 / C3 / C4 | 8 / 5 / 4 / 3 | 8 / 5 / 4 / 3 | Match; C total 20 |
| D1 / D2 / D3 / D4.1 / D4.2 / D5 | 3 / 8 / 5 / 2 / 3 / 4 | 3 / 8 / 5 / 2 / 3 / 4 | Match; D total 25. WS scoring summary presents D4 as aggregate 5. |
| Content total | 100 | 100 | Match |
| Quality modifier | +5 to -5 | +5 to -5 | Match |

### All worksheet response budgets and count limits

| Section | Source | Exact budget wording / limit (normalized only for whitespace) |
|---|---|---|
| A1 | WS p.3 | 200 words maximum across the table. |
| A2 | WS p.4 | 150 words maximum after the table. |
| A3 | WS p.4 | 250 words maximum across the table. |
| A4 | WS p.5 | 250 words maximum. |
| B1 | WS p.5 | One concise row per opportunity; no separate business case is required. No stated word cap. |
| B2 | WS p.5 | 50 words maximum per opportunity across the rationale columns. |
| B3 | WS p.6 | 300 words maximum across B3. |
| B4 | WS p.6 | 250 words maximum. |
| C1 | WS p.7 | 350 words maximum including the final explanation. |
| C2 | WS p.7 | 200 words maximum after the table. |
| C3 | WS p.8 | 50 words maximum per opportunity rationale. |
| C4 | WS p.8 | 250 words maximum. |
| D1 | WS p.9 | 200 words maximum. |
| D2 | WS p.10 | Complete at least 15 rows; 20 maximum in the main submission. |
| D3 | WS p.11 | 300 words maximum across D3. |
| D4 | WS p.12 | 200 words maximum across D4. |
| D5 | WS p.12 | 300 words maximum. |
| Whole document | WS p.1 | Recommended 16–20 pages; maximum 20 pages excluding references, declaration and optional evidence appendix. |

## K1–K18 ruling application

These items use the author's current G2 arguments; they replace the earlier G2 ruling pack. See [g2_k1_k18_ruling_record.md](./g2_k1_k18_ruling_record.md) for item-by-item status. K18 is the added citation-policy item.

## Ledger update

The author's K1–K18 judgements dated 2026-10-10 are recorded in `ledger/ledger.md` with approver `Nilotpal`. The G2-specific word-cap question was removed from open questions; remaining later-stage questions are unchanged. G2 is not recorded as approved.
