**Assignment 3 Support Agent and Skills: Design Proposal (v2)**

AIBP Course 3 · AI Opportunity Portfolio with Maturity, Competitive and Workforce Assessment · Prepared for Nilotpal Choudhury · Version 2 · 10 October 2026 · Design stage only

**Status:** Version 2, incorporating your answers of 10 Oct 2026 and your Module 1 notes. Design proposal for your review only. Nothing has been built, configured, published or drafted, and the assignment template has not been generated. **Changes from version 1 are marked \[v2\].** Submission deadline: **15 Oct 2026**.

**Tags used throughout:** **\[V\]** verified in a source document · **\[R\]** my design recommendation · **\[?\]** unresolved question for you. Source codes: **WS** = Participant Worksheet (15 pp), **RB** = Participant Rubric (5 pp), **A1** = Assignment 1 (25 pp), **A2** = Assignment 2 (18 pp), **M2 / M3** = your Notion notes for Course 3 Modules 2 / 3.

**1. Executive overview**

**Recommended design \[R\]:** one orchestrating **Assignment 3 Support Agent** plus **four skills**, all reading from and writing to one **Decision & Evidence Ledger** (the shared reference record). The agent owns sequence, approval gates, the ledger and all contact with you. The skills are stateless procedures: (1) requirements and template, (2) prior-work reuse, (3) course-grounded drafting with public-evidence research, (4) consistency and quality assurance. Drafting cannot start until you have approved this design and, separately, the generated template.

**Why this fits Assignment 3 \[V → R\]:**

- The task is a four-part decision artefact (A 25, B 30, C 20, D 25 marks, plus a ±5 quality modifier) that must "tell one coherent story" (WS p.15; RB p.1). Parts depend on each other: A's weak dimensions must constrain B's portfolio; B's top three feed C3, C4 and D1. A ledger and a dependency map are the minimum needed to keep a 16–20 page document consistent.

- Word budgets are tight and stated per field (e.g. C1 350 words, A1 200 words). A drafting skill that enforces budgets and tags every claim protects the marks the rubric attaches to specificity and evidence discipline.

- Reuse of A1/A2 is permitted only "where the opportunity still fits" (WS p.1), and the prior documents contain traps: a "Now" priority that Course 3 definitions may not call a Quick Win, unfilled placeholders, and vendor material that is out of scope. A dedicated reuse skill makes those calls visible rather than silent.

- The quality modifier penalises placeholders, fabrication and missing declarations (-5) and inconsistency (-1 to -4). A separate QA skill with a seeded-error acceptance test addresses those directly.

- Integrity: AI assistance is allowed only within programme rules, and "analysis and judgement … are my own" (WS p.14). The agent therefore captures your judgements (ratings, classifications, priorities) before drafting, and never completes the declaration for you.

**Five findings that shaped the design:**

1.  All four named source files resolved by exact filename in the project folder; no ambiguity. Assignment 2's link in your instructions carried no folder path, so I resolved it by filename in the same folder.

2.  The stated word budgets sum to roughly 3,600 words before uncapped tables (A2, B1, D2), which sits awkwardly with the "recommended 16–20 pages". This needs your ruling (item K1, section 2.4).

3.  Your Notion pages are learner-made note summaries with transcripts omitted, and they contain at least one probable typo (patent class "GO-6N"). They are good for framework logic but should not be cited as primary evidence (K8). \[v2\] Module 1 notes have now been supplied and read; they close most of the sub-dimension gap (K7).

4.  A1/A2 document five-plus usable opportunities, but no Moonshot, and almost every documented readiness dimension is Red or Amber. An honest Course 3 portfolio may contain few or no Quick Wins; the design forbids manufacturing them (section 6).

5.  Part C comparator evidence is wholly new work (no competitor evidence exists in A1/A2), and Part A evidence for Technology, Talent, Process and Culture is thin. Both need inputs from you or new public research.

**2. Source review and requirement map**

**2.1 Sources reviewed**

| **Source**                          | **Resolved to**                                                                                         | **Reviewed**                                                                                                                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Assignment instructions (WS)        | G:\My Drive\PGP_AI_IIMK\Course 3\IIMK-AIBP-C3-Artefact-ParticipantWorksheet.pdf                         | All 15 pages                                                                                                                                                                                                         |
| Scoring rubric (RB)                 | …\IIMK-AIBP-C3-ParticipantRubric.pdf                                                                    | All 5 pages                                                                                                                                                                                                          |
| Prior assignment 1 (A1)             | …\Assignment1_AIOpportunityScan_NilotpalChoudhury.pdf (dated 23-Aug-2026 in its declaration)            | All 25 pages incl. appendices                                                                                                                                                                                        |
| Prior assignment 2 (A2)             | …\Assignment2_GenAITechnologyAssessment_NilotpalChoudhury.pdf (declaration dated 18/09/2026)            | All 18 pages. Appendix 1 (vendor evidence log) is only an embedded attachment link and is not in the folder; not reviewed                                                                                            |
| Course 3 Module 2 notes (M2)        | Notion page "Course 3 \|\| Module 2 - AI across Business Functions"                                     | Read in full for readiness dimensions, strategy and analytics, and cross-functional value chains; other function sections (finance, HR, legal, operations, customer service) only searched for portfolio-logic terms |
| \[v2\] Course 3 Module 1 notes (M1) | Notion page "Course 3 Module 1 - Organisational AI Maturity Assessment"                                 | Read in full: six dimensions and their sub-dimensions, industry benchmarking, portfolio design lecture                                                                                                               |
| Course 3 Module 3 notes (M3)        | Notion page "Course 3 \|\| Module 3 - Competitive Strategy, AI Disruption and Workforce Transformation" | Read in full                                                                                                                                                                                                         |

**2.2 Verified assignment facts the design rests on \[V\]**

- Marks: A1 3, A2 14, A3 4, A4 4 (A=25) · B1 10, B2 8, B3 8, B4 4 (B=30) · C1 8, C2 5, C3 4, C4 3 (C=20) · D1 3, D2 8, D3 5, D4 5 (D4.1 = 2, D4.2 = 3), D5 4 (D=25). Content 100; quality modifier +5 to -5; final capped at 100, floored at 0 (WS pp.2–3, 15). No weights beyond these are stated.

- Submit one PDF; retain all section numbers, response fields and tables; recommended 16–20 pages; maximum 20 pages excluding references, declaration and optional evidence appendix (WS p.1).

- Current requirements are authoritative; prior work may be reused where it still fits (WS p.1). The assignment is not an ROI case, vendor selection, legal opinion, implementation plan, governance model or headcount-reduction plan (WS p.2).

- No source assignment template exists; none is mentioned in WS or RB.

**2.3 Requirement map**

Responsibility key: **S1** requirements & template · **S2** prior-work reuse · **S3** drafting & research · **S4** consistency & QA · **Agent** orchestration/ledger. "Ledger check" means S4 compares the draft against ledger entries.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Ref / marks</strong></th>
<th><strong>Requirement or criterion [V]</strong></th>
<th><strong>Responsible</strong></th>
<th><strong>Expected output</strong></th>
<th><strong>Validation check</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>X1</p>
<p>WS p.1</p></td>
<td>One PDF; keep all section numbers, fields, tables</td>
<td>S1 builds template; Agent assembles PDF</td>
<td>Template preserving structure; final PDF</td>
<td>Structural diff of final vs worksheet: every section ID and table present</td>
</tr>
<tr class="even">
<td><p>X2</p>
<p>WS p.1</p></td>
<td>Recommended 16–20 pp; max 20 pp excl. references, declaration, optional appendix</td>
<td>Agent renders; S4 reports</td>
<td>Page-count report on rendered PDF</td>
<td>Body ≤ 20 pp measured on the PDF, not estimated</td>
</tr>
<tr class="odd">
<td><p>X3</p>
<p>WS p.2</p></td>
<td>Single consistent scope; no invented organisational facts; assumptions labelled; no confidential data</td>
<td>S3 drafts; S4 audits</td>
<td>Claim-tag sheet (Documented / Course / Public E-ID / Assumption / Judgement)</td>
<td>Any untagged factual claim, or claim beyond declared scope, is a blocking issue</td>
</tr>
<tr class="even">
<td><p>X4</p>
<p>WS p.2; RB p.1</p></td>
<td>Out-of-scope content: ROI/NPV case, vendor selection, governance operating model, headcount reduction, "most advanced tech"</td>
<td>S3, S4</td>
<td>Scope-creep list</td>
<td>Scan finds none</td>
</tr>
<tr class="odd">
<td><p>X5</p>
<p>WS p.13; RB p.5</p></td>
<td>Submission checklist (16 items); rubric self-check (11 items); reference log E1–E8 (excluded from page limit)</td>
<td>S4; S3 keeps log</td>
<td>Checklist status with evidence location; populated log</td>
<td>Every ticked item points to where it is satisfied; every public claim maps to an E-ID</td>
</tr>
<tr class="even">
<td><p>X6</p>
<p>WS p.14</p></td>
<td>AI-use disclosure and honour declaration</td>
<td>Agent drafts facts of AI use; you complete and sign</td>
<td>Draft disclosure facts</td>
<td>Agent never ticks, signs or dates the declaration</td>
</tr>
<tr class="odd">
<td><p>X7</p>
<p>WS p.3; RB p.5</p></td>
<td>Quality modifier: -5 for undisclosed fabrication, extensive placeholders, missing declaration; -1 to -4 for inconsistency, unsupported assertions</td>
<td>S4</td>
<td>Modifier-risk list</td>
<td>Zero placeholders, zero contradictions, declaration present</td>
</tr>
<tr class="even">
<td><p>A1</p>
<p>WS p.3; RB p.2</p>
<p>3 marks</p></td>
<td>Scope tick, label, why appropriate, evidence, limits. ≤200 words across table</td>
<td>S3 (your inputs); S2 supplies prior context</td>
<td>Completed field table</td>
<td>≤200 words; scope matches evidence you can access (K11)</td>
</tr>
<tr class="odd">
<td><p>A2</p>
<p>WS p.4; RB p.2</p>
<p>14 marks</p></td>
<td>Six dimensions rated H/M/L using taught sub-dimensions, evidence, most material gap; ≤150 words on least-confident rating</td>
<td>S3; S2 seeds evidence; ratings are yours</td>
<td>Six rated rows + uncertainty note</td>
<td>Each row cites an indicator per sub-dimension or says "Not evidenced"; ≤150 words after table; no rating without a stated source</td>
</tr>
<tr class="even">
<td><p>A3</p>
<p>WS p.4; RB p.2</p>
<p>4 marks</p></td>
<td>Industry baseline or 1–2 peers; evidence; implication; ≤250 words</td>
<td>S3 research protocol</td>
<td>Benchmark table with E-IDs</td>
<td>Absolute vs relative position distinguished; every claim has E-ID or "Not evidenced"</td>
</tr>
<tr class="odd">
<td><p>A4</p>
<p>WS p.5; RB p.2</p>
<p>4 marks</p></td>
<td>One or two weakest dimensions; why it matters; blocked opportunities; intervention; evidence of improvement; ≤250 words</td>
<td>S3</td>
<td>Constraint table</td>
<td>Constraint is among the lowest in A2; every blocked opportunity exists in B1</td>
</tr>
<tr class="even">
<td><p>B1</p>
<p>WS p.5; RB p.2</p>
<p>10 marks</p></td>
<td>5–7 distinct opportunities: problem, function/workflow, AI pattern, value mechanism, readiness dependency; not "all GenAI"</td>
<td>S2 candidates; S3 drafts; you choose</td>
<td>Portfolio table</td>
<td>Count 5–7; each dependency maps to an A2 dimension; ≥1 non-GenAI pattern or stated reason; business problems, not technologies</td>
</tr>
<tr class="odd">
<td><p>B2</p>
<p>WS pp.5–6; RB p.2</p>
<p>8 marks</p></td>
<td>Quick Win / Strategic Bet / Moonshot using Course 3 definitions; ≤50 words per opportunity</td>
<td>S3; S4 rule check</td>
<td>Classification table</td>
<td>Quick Win has no Low-rated dependency without explanation; time/uncertainty rationale present; ≤50 words each</td>
</tr>
<tr class="even">
<td><p>B3</p>
<p>WS p.6; RB p.3</p>
<p>8 marks</p></td>
<td>Top three ranked using impact, readiness, time, risk, strategic significance; condition and change trigger; 2–3 sentence balance statement; ≤300 words</td>
<td>S3; you decide</td>
<td>Ranking table + statement</td>
<td>Consistent with A2/A4; trigger stated; not simply the easiest three</td>
</tr>
<tr class="odd">
<td><p>B4</p>
<p>WS p.6; RB p.3</p>
<p>4 marks</p></td>
<td>One top-three opportunity: upstream, downstream, compounded value, propagated error, control; N/A allowed if reasoned; ≤250 words</td>
<td>S3</td>
<td>Value-chain table</td>
<td>Value and risk both addressed; control named</td>
</tr>
<tr class="even">
<td><p>C1</p>
<p>WS p.7; RB p.3</p>
<p>8 marks</p></td>
<td>Two comparators (third optional) × five signal sources; Experimenting/Scaling/Embedded; closest-attention conclusion; ≤350 words incl. explanation</td>
<td>S3 research protocol</td>
<td>Scan table + conclusion</td>
<td>Every cell has E-ID or "Not evidenced"/"N/A"; position supported by ≥2 signal types; sources current and dated</td>
</tr>
<tr class="odd">
<td><p>C2</p>
<p>WS p.7; RB p.3</p>
<p>5 marks</p></td>
<td>Five Forces through AI lens: direction, which side, implication; one force linked to a Part B opportunity; ≤200 words after table</td>
<td>S3</td>
<td>Forces table + link</td>
<td>Linked opportunity ID exists in B1</td>
</tr>
<tr class="even">
<td><p>C3</p>
<p>WS p.8; RB p.3</p>
<p>4 marks</p></td>
<td>Top three: data-moat potential, regulatory clarity/risk, readiness → Lead / Fast follow / Wait; ≤50 words each</td>
<td>S3</td>
<td>Positioning table</td>
<td>Uses all three factors; positions differ where evidence differs; readiness matches A2</td>
</tr>
<tr class="odd">
<td><p>C4</p>
<p>WS p.8; RB p.3</p>
<p>3 marks</p></td>
<td>Three-question moat test on one opportunity; conclusion; strengthen/erode; ≤250 words</td>
<td>S3</td>
<td>Moat table</td>
<td>Conclusion follows the three answers, not data volume</td>
</tr>
<tr class="even">
<td><p>D1</p>
<p>WS p.9; RB p.4</p>
<p>3 marks</p></td>
<td>Role affected by a top-three opportunity (prefer Priority 1), bottleneck, "what should not be assumed"; ≤200 words</td>
<td>S3; you choose</td>
<td>Focus table</td>
<td>Role links to a top-three ID; no headcount framing</td>
</tr>
<tr class="odd">
<td><p>D2</p>
<p>WS pp.9–10; RB p.4</p>
<p>8 marks</p></td>
<td>15–20 discrete tasks: share/frequency, classification, why, AI/human boundary</td>
<td>S3</td>
<td>Task table</td>
<td>15–20 rows; each a discrete task; classification uses the three tests (deterministic rule set, outside context, comfort without review)</td>
</tr>
<tr class="even">
<td><p>D3</p>
<p>WS p.11; RB p.4</p>
<p>5 marks</p></td>
<td>Current vs redesigned composition, redeployment of capacity, success measures; ≤300 words</td>
<td>S3</td>
<td>Redesign table + statement</td>
<td>Released capacity has a named destination; measures change</td>
</tr>
<tr class="odd">
<td><p>D4.1 / D4.2</p>
<p>WS p.12; RB p.4</p>
<p>2 + 3 marks</p></td>
<td>One of six role families; build/hire/source; one of three frameworks fitted to Part A maturity; ≤200 words combined</td>
<td>S3</td>
<td>Decision tables</td>
<td>Framework choice cites A2/A4 evidence</td>
</tr>
<tr class="even">
<td><p>D5</p>
<p>WS p.12; RB p.4</p>
<p>4 marks</p></td>
<td>Human alone / AI alone / Human+AI test, metrics, frontier tasks, retain and redesign triggers; ≤300 words</td>
<td>S3</td>
<td>Evaluation plan</td>
<td>Three conditions present; metric beyond speed; redesign trigger stated; Human+AI not assumed to win</td>
</tr>
</tbody>
</table>

**2.4 Conflicts, ambiguities and gaps (flagged, not silently resolved)**

| **ID** | **Issue**                                                                                                                                                                                                                                                                                      | **Sources**           | **Proposed handling \[R\]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **Status**                         |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| K1     | Stated caps total ≈3,600 words (A1 200, A2 150, A3 250, A4 250, B2 250–350, B3 300, B4 250, C1 350, C2 200, C3 150, C4 250, D1 200, D3 300, D4 200, D5 300) plus uncapped tables (A2, B1, D2). Unclear whether "across the table" caps include table cells; unclear how this reaches 16–20 pp. | WS pp.1, 3–12         | \[v2\] Your ruling: table cells consume page space, so the agent recommends table or paragraph layout per field. Caps as worded in WS: A1, A3, A4, B3, B4, C1, C3, C4, D1, D3, D4, D5 and B2 (rationale columns) include table cells; A2 and C2 caps apply to text after the table; B1 and D2 have no stated cap. Caps stay binding; page range is recommended; S4 reports both. Layout limits: see K16.                                                                                                                                            | \[v2\] Ruled; layout conflict K16  |
| K2     | C1: two or three comparators × five signals plus an explanation in 350 words.                                                                                                                                                                                                                  | WS p.7                | Telegraphic cells with E-IDs; allow only if cells count toward the cap as stated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \[?\]                              |
| K3     | Task decomposition: 30–50 (Video 24, M3) vs 15–20 in the main submission.                                                                                                                                                                                                                      | WS p.9; RB p.1; M3    | Worksheet governs. Optional 30–50 list goes in the appendix.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | \[V\] resolved by source hierarchy |
| K4     | Rating scales: H/M/L (WS), 1-2-5 (M2 action item), Red/Amber/Green on three questions (A1).                                                                                                                                                                                                    | WS p.4; M2; A1 A2.1   | Use H/M/L only. A1 RAG ratings can seed evidence but not be copied as ratings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | \[V\]                              |
| K5     | Positioning labels: "Lead / Fast follow / Wait" (table) vs "lead/follow/wait" (headings, checklist, M3).                                                                                                                                                                                       | WS pp.8, 13; RB p.3   | Use the table labels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | \[V\]                              |
| K6     | Comparators: two plus optional third (WS) vs "top 3" (M3).                                                                                                                                                                                                                                     | WS p.7; M3            | Worksheet governs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | \[V\]                              |
| K7     | Module 1 content (sub-dimension indicator definitions, benchmarking method, portfolio background) is referenced but absent from the supplied pages. WS lists the sub-dimension names only.                                                                                                     | WS p.4; M2            | \[v2\] Module 1 notes supplied. They give indicators for each dimension (Technology: infrastructure, integration, technical debt; Data: quality, accessibility, strategic value; Talent: skills inventory, learning culture, leadership capability; Process: standardisation, documentation, automation baseline; Culture: four indicators; Governance: four components) and the weakest-dimension rule. Residual: the notes give only high-level benchmarking method and India-centred sources, so the energy/lubricants baseline is new research. | \[v2\] Mostly resolved             |
| K8     | M2/M3 are summaries with transcripts omitted; probable typo "GO-6N"; salary and statistics figures self-flagged as unverified.                                                                                                                                                                 | M2, M3                | Cite as "course notes" for frameworks; verify any figure before presenting it as external fact.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \[R\]                              |
| K9     | A1 sequences churn as "Now" although its data and governance readiness are Red; Course 3 defines Quick Win as "most required readiness already in place".                                                                                                                                      | A1 D1.3, A2.1; WS p.5 | Re-classify under Course 3 definitions; do not import A1 labels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | \[R\]                              |
| K10    | A1 charter holds unfilled placeholders (\[X\]%, \[N\], \[3–4\]).                                                                                                                                                                                                                               | A1 D2.1               | Never carry; ask you for real values or omit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | \[V\]                              |
| K11    | A1/A2 anchor on "Strategy and Analytics (Global Lubricants)", but several A1 opportunities belong to sales or supply-chain workflows.                                                                                                                                                          | A1 cover; WS p.2      | \[v2\] Your ruling: function scope (Strategy & Analytics within Global Sales & Marketing), using sales-related workflows. Open point: whether R4 (leadership-team evidence-pack agent, an internal strategy workflow) counts as sales-related (see section 6).                                                                                                                                                                                                                                                                                      | \[v2\] Ruled; one open point       |
| K12    | Rule against uploading restricted employer information to public AI tools; programme's detailed rules not supplied; A1/A2 contain internal-looking figures (anonymised label).                                                                                                                 | WS p.14               | Confirm prior content is cleared for use with the tool you choose; agent works only from submitted, anonymised material and requests no new confidential detail.                                                                                                                                                                                                                                                                                                                                                                                    | \[?\]                              |
| K13    | No submission deadline appears in any source.                                                                                                                                                                                                                                                  | WS, RB                | \[v2\] Deadline 15 Oct 2026. Compressed gate plan proposed in section 8.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \[v2\] Resolved                    |
| K14    | No rule on verbatim reuse of earlier text.                                                                                                                                                                                                                                                     | WS p.1                | \[v2\] Your ruling: no verbatim quotation; rephrase messaging in a professional tone suited to the assignment. S3 and S4 enforce this (S4 flags long matches to A1/A2 text).                                                                                                                                                                                                                                                                                                                                                                        | \[v2\] Resolved                    |
| K15    | Vendor scoring in A2 Part C vs "not a vendor-selection exercise".                                                                                                                                                                                                                              | A2 Part C; WS p.2     | Exclude vendor scoring; reuse only the use case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | \[V\]                              |
| K16    | \[v2\] Your layout ruling (convert tables to paragraphs where answers are short) conflicts with WS p.1: "retain all section numbers, response fields and tables".                                                                                                                              | WS p.1                | Keep multi-row comparison tables (A2, A3, B1–B3, C1–C3, D2, D3, D5 test conditions) as tables, compactly set. For two-column "Field \| Your response" tables (A1, B4, C4, D1, D4, D5 decision rows) the agent may recommend a labelled-paragraph layout that keeps every field label verbatim. You confirm before G2 that you accept this reading.                                                                                                                                                                                                  | \[?\]                              |
| K17    | \[v2\] "Sales-related workflows" scope may exclude R4 and its natural D1 role (Commercial Strategy Analyst); sales roles have thinner task evidence in A1/A2.                                                                                                                                  | Your ruling; A1, A2   | Decide at G3 whether R4 stays in scope; supply real task data for the chosen role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | \[?\]                              |

**3. Agent design**

| **Element**          | **Design \[R\]**                                                                                                                                                                                                                                                                                                                                                              |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose              | Help you develop Assignment 3 as one coherent, evidence-disciplined artefact aligned to the worksheet and rubric, consistent with your A1/A2 work, with every judgement remaining yours.                                                                                                                                                                                      |
| In scope             | Requirement extraction; template generation (after approval); reuse analysis of A1/A2; judgement-capture questions; section drafting within word caps; public-evidence research for A3, C1, C2; consistency checks; final rubric audit; page/word measurement; draft disclosure facts.                                                                                        |
| Out of scope         | Building or running anything before approval; ticking or signing the declaration; deciding ratings, classifications, priorities or positions without your input; headcount-reduction analysis; ROI/vendor/governance-model content; promising a grade; editing source files; saving outside the project folder.                                                               |
| Inputs               | The four PDFs (exact filenames); Notion M2/M3 pages; your Module 1 notes if supplied \[?\]; your answers at judgement-capture prompts; public web sources found under the research protocol; the ledger.                                                                                                                                                                      |
| Orchestration        | Stage 1 requirements & conflicts → G2 template → Stage 2 reuse ledger → G3 → Stage 3 drafting by part in dependency order (A → B → C → D), each part: judgement capture → S3 draft → S4 delta check → your edit/approval → ledger update → Stage 4 assembly and full audit → G8.                                                                                              |
| Operating boundaries | Single writer to the ledger (the agent). Skills return proposed entries; the agent applies them. Work on copies; sources untouched; outputs only in the Course 3 folder (working subfolder, see decision 2). Stops and asks you on: source conflicts, missing evidence for a mandatory field, scope decisions, any need for confidential detail, any unresolved path or file. |

**3.1 Approval checkpoints**

| **Gate** | **What you approve**                                                                                                | **Blocks**                               |
|----------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| G0       | This design, and your answers to the decisions in section 8                                                         | Any building                             |
| G1       | Build acceptance: skills pass their acceptance tests on existing documents (section 4); you review the test outputs | Running skills on Assignment 3 content   |
| G2       | The generated template, requirement register, coverage matrix and rulings on K1–K17 (separate from G0)              | Reuse analysis sign-off and all drafting |
| G3       | Prior-work fact ledger (spot-checked against A1/A2) and the shortlist of candidate opportunities                    | Part B drafting                          |
| G4       | Scope and Part A (A1–A4), including every rating as your own judgement                                              | Part B                                   |
| G5       | Part B: portfolio, classifications, top three, compound-value check                                                 | Parts C3, C4, D                          |
| G6 / G7  | Part C (with reference log reviewed) / Part D                                                                       | Assembly                                 |
| G8       | Assembled document and final rubric audit                                                                           | Your declaration                         |
| G9       | You complete disclosure, declaration, signature and submit (human only)                                             | Submission                               |

Any edit after a gate re-opens only the sections the dependency map (section 7) marks as impacted.

**3.2 Boundary between the agent and the skills**

| **Agent (orchestration)**                                                                    | **Skills (procedures)**                                                          |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Decides which skill runs, in what order, on which inputs; enforces gates                     | Execute one defined procedure against the inputs they are given                  |
| Talks to you; asks judgement-capture questions; records your decisions as "author judgement" | Never contact you directly; return questions to the agent                        |
| Owns the ledger: the only writer; versions it; logs every change                             | Read the ledger slice supplied; return proposed entries                          |
| Holds tool access (files, web, Notion) and file locations                                    | Carry no state between runs; define input/output contracts and acceptance checks |
| Assembles and renders the document; measures pages                                           | Report issues; never rewrite content silently                                    |

**4. Skills scope**

Four skills are proposed. **Why not fewer:** merging QA into drafting would let the drafter grade itself; merging requirements into reuse would blur verified requirements with optional material. **Why not more:** public-evidence research, judgement capture and word-budget enforcement all belong to drafting and share its inputs; ledger maintenance is the agent's job. If drafting proves too long to maintain, the first candidate to split out is the research protocol (decision 4).

| **Skill (working name)**           | **Purpose**                                                                                                                                   | **Trigger**                                                                               | **Inputs**                                                                                                   | **Outputs**                                                                                                                                                                       | **Exclusions**                                                                                                                                                                                        | **Acceptance checks**                                                                                                                                                                                                                      |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **S1** a3-requirements-template    | Extract and verify requirements; keep the conflict register; generate the template; build the rubric-coverage matrix                          | After G0 and build; re-run if a source file's modified time changes or you issue a ruling | WS, RB (exact filenames); ledger rulings                                                                     | Requirement register (ID, source page, type Mandatory / Budget / Descriptor / Recommended); conflict register; working template; coverage matrix                                  | No response content; no judgements; no invented weights or limits; does not alter sources                                                                                                             | Part marks sum to 25/30/20/25 and 100; every WS section ID and table retained (diff vs source); every word cap matches source text; every rubric criterion maps to ≥1 template field and back; Recommended items never appear as Mandatory |
| **S2** a3-prior-work-reuse         | Fact-level inventory of A1/A2; relevance to A3 fields; adaptation notes; evidence gaps                                                        | After requirement register is frozen; before Part A evidence and B1                       | A1, A2 (exact filenames); requirement register; ledger                                                       | Prior-work fact ledger (location, status: documented / estimate / placeholder); candidate assessment; reuse proposals per field; "new evidence needed" list                       | Does not choose the portfolio; adds no facts; no vendor scoring; no verbatim blocks; flags placeholders                                                                                               | Every fact has a section reference; all numerics match source exactly (full check); sampled facts re-verified; each proposal labelled documented / adapted / new; parked or rejected items cite A1's own reason                            |
| **S3** a3-course-grounded-drafting | Judgement-capture prompts; draft each section from ledger, course concepts and public evidence; run the public-evidence protocol (A3, C1, C2) | Per section at its gate, in dependency order                                              | Template section; ledger slice; M2/M3 (and Module 1 if supplied); reuse proposals; your answers; web sources | Draft content in the recommended layout; claim-tag sheet; word count; proposed ledger entries; open questions; E-ID entries (title, organisation, date, URL, access date)         | Decides no rating/classification/position; no verbatim copying of A1/A2 prose (rephrase in professional tone); no headcount framing; no unsourced competitor claim; no ledger writes; no declarations | Within stated cap; every claim tagged; every public claim has an E-ID or reads "Not evidenced"; course definitions used as worksheet states them; all fields filled; zero placeholders                                                     |
| **S4** a3-consistency-qa           | Delta consistency check after each change; repetition and unsupported-claim scan; final rubric audit; limits and integrity checks             | After each draft or edit (delta mode); before each gate; before assembly (full audit)     | Draft; ledger; coverage matrix; RB; description of the change                                                | Issue list (blocking / warning); impacted-section list; rubric audit table (criterion → where evidenced → descriptor met / partial / gap); checklist status; page and word report | Does not rewrite, grade or predict marks; does not write the ledger                                                                                                                                   | Seeded-error test passes (planted contradiction, changed figure, duplicated rationale, untagged claim, Quick Win on a Low dependency, missing section ID all caught); page count from rendered PDF                                         |

**5. Assignment-template generation plan**

Runs only after G0 and G1. The template is a structure, not a draft: it contains no analysis and no prefilled answers.

| **Step** | **What S1 does**                                                                                                                                                                                          | **Output**                       | **Status label**                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|----------------------------------------------------|
| 1        | Freeze a requirement register from WS/RB text: one row per section, field, table, word cap, mark value and descriptor, each with source page                                                              | Register with IDs (e.g. R-B2-03) | Mandatory \[V\] or Budget \[V\]                    |
| 2        | Reproduce the worksheet skeleton exactly: section numbers, table headings and response fields, checklist, reference log E1–E8, disclosure, declaration                                                    | Skeleton                         | Mandatory \[V\]                                    |
| 3        | Under each field add: marks; stated word cap; WS "what earns marks" text; rubric full-marks descriptor split into checkable atoms; required evidence or analysis type; ledger dependencies; response area | Field entries                    | Descriptor-derived \[V\]; evidence-type tags \[R\] |
| 4        | Word allocations only where a cap is stated. Uncapped tables (A2, B1, D2) get none. An optional page plan proportional to marks (≈5 / 6 / 4 / 5 pages for A / B / C / D of 20) may be shown, labelled     | Allocation line per field        | Cap \[V\]; page plan \[R\]                         |
| 5        | Insert inline "ASK" markers at every K-item that needs your ruling, and a per-field **layout recommendation** (table or labelled paragraph) following your ruling and K16                                 | Marked template                  | \[?\] / \[R\]                                      |
| 6        | Build the rubric-coverage checklist: every criterion and atom → template field; every field → criterion; cross-section links (A2→A4→B1→B2→B3→C3→D4.2; B3→B4, C4, D1→D2–D5)                                | Coverage matrix                  | \[V\] / \[R\] for links                            |
| 7        | Add back matter: optional evidence appendix (D2 full 30–50 list, per WS p.9), references, declarations                                                                                                    | Appendix stubs                   | Optional \[V\]                                     |

**Distinguishing mandatory from recommended:** every template element carries one of three visible labels (Mandatory, Budget, Recommended). Recommended items sit in a separate, collapsible "suggested approach" line under the field and are never counted in coverage. **Validation of rubric coverage:** the two-way matrix is checked at G2 and recomputed in the final audit.

**What you must approve before drafting begins \[R\]:** (a) this design (G0); (b) build acceptance (G1); (c) the generated template, the coverage matrix, the layout recommendations and your confirmation of K16 and K17 (G2). The agent will not start Part A until G2 is explicit, in writing.

**6. Prior-assignment reuse plan**

Facts below are **documented in A1/A2 \[V\]** unless marked otherwise. Relevance and adaptation are **my assessment \[R\]**; you decide what enters the portfolio. Opportunity IDs here are provisional reuse labels, not portfolio numbers.

| **Candidate**                                                             | **Source**                               | **Documented facts to preserve**                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Relevance to A3**                                                                                                                                  | **Adaptation needed**                                                                                                                 | **Evidence gaps**                                                                                                                                    |
|---------------------------------------------------------------------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **R1** Churn early-warning signal                                         | A1 B1.1 \#3, A2.1, C1–C3, D1.2, D1.3, D2 | Supervised classification, recall-tuned; ~50K accounts/market, 5+ yrs history; current rule fires only after two years of volume decline; ~1,500 usable churned records in one market; min dataset ~5,000 accounts/market, 12–15 months; error cost ~5:1 (≈USD 15K vs 3K); readiness Amber / Red / Red; definitions fix ≈1 month, 200–300 person-hours; owner role pending appointment; target 5% relative churn reduction in 12 months; cross-border clearance "Unclear" | High: B1, B2, B4, A4 (data, governance), C3, C4; candidate for D1 (account manager role)                                                             | Re-classify under Course 3 definitions (K9); drop A1 Now/Next/Later labels; translate RAG evidence into A2 dimension indicators       | Baseline \[X\]% and \[N\] never filled (K10); Talent and Culture evidence; whether pilot is approved; role task data for D2                          |
| **R2** Order-status and lead-time visibility                              | A1 B1.1 \#1, B1.2, B1.3, D1.3            | Regression plus rules; live prediction layer routed away from AI; 2,000–3,000 sales hours/yr; 5+ yrs SAP order history; target variable clear, two of three ingredients Partial; owners in logistics / SAP masterdata                                                                                                                                                                                                                                                     | High: shows a non-GenAI pattern (B1); Process and Data dependencies                                                                                  | Express as rules plus regression hybrid; confirm "Next" is consistent with B3                                                         | Basis of hours estimate; named field owner                                                                                                           |
| **R3** Sector-matched value cases                                         | A1 B1.1 \#5, D1.1, D1.3                  | Generative retrieval and drafting over tagged proof points; potential 10–15% conversion uplift held as a hypothesis; blocked by missing tagging and owner                                                                                                                                                                                                                                                                                                                 | Medium–High: Strategic Bet candidate; absorbs parked R6                                                                                              | Merge with parked collateral Q&A to avoid double counting; keep "hypothesis" wording                                                  | No pilot data; content owner; tagging status                                                                                                         |
| **R4** Leadership-team evidence-pack research agent                       | A2 Parts A, B, D (whole use case)        | LT question → draft evidence pack; ~25 analyst-days today, target ~15; 4–5 recommendations each with 3 primary and 3 supporting evidences; augmented, read-only; routed models; hard thresholds (≤2% numerical mismatch, ≤5% citation errors); proceed to controlled pilot; 90-day plan                                                                                                                                                                                   | \[v2\] Scope question (K17): an internal strategy workflow, not a sales workflow. If kept, strongest source for D; if excluded, D needs a sales role | Reuse the use case only; exclude vendor scoring (K15); cost range was an AI-assisted directional estimate and A3 asks for no ROI case | Fits "sales-related workflows"?; whether pilot started; task-level time shares for D2; overlap with R7 and the existing market-intelligence platform |
| **R5** Lead-generation assistant, hybrid                                  | A1 A1.1, A2.1–A2.3, B2.1–B2.3            | GenAI research over 1K–5K prospects; \<1 run/month today, 2–4/month planned; verdict hybrid with written scoring over five features; governance Red (one data scientist, no repository)                                                                                                                                                                                                                                                                                   | Medium: tangible Governance dependency; productionisation opportunity                                                                                | Frame as "productionise with governance" rather than a new build                                                                      | No labels; unclear business value size                                                                                                               |
| **R6** Parked: approved-collateral Q&A; sales admin automation            | A1 D1.3 (Park)                           | R-collateral parked as duplicate of R3; sales admin parked on undefined "good report"                                                                                                                                                                                                                                                                                                                                                                                     | Low by default                                                                                                                                       | Exclude unless new evidence changes A1's stated reasons                                                                               | —                                                                                                                                                    |
| **R7** CI data product (proposed) and market-intelligence platform (live) | A1 A1.1 \#5, A2.1; A2 A1                 | Proposed product readiness Green / Red / Red; existing GenAI platform in production                                                                                                                                                                                                                                                                                                                                                                                       | Medium: possible overlap with R4                                                                                                                     | Keep distinct or merge; never list both as separate opportunities without a clear boundary                                            | Boundary between R4 and R7 undocumented                                                                                                              |
| **Live assets and retired system**                                        | A1 A1.1, Appendix 1                      | Five systems incl. channel dashboard (hybrid), segmentation (retired, 500+ activations, low-six-figure USD)                                                                                                                                                                                                                                                                                                                                                               | Evidence for Technology and Process in A2                                                                                                            | Use as indicators, not opportunities                                                                                                  | Why segmentation was retired is not stated                                                                                                           |

**6.1 Reuse rules \[R\]**

- Preserve each fact exactly; label it **Documented**, **Adapted** (with the change stated) or **New proposal**; every reuse carries its A1/A2 section reference in the ledger.

- \[v2\] No verbatim quotation (your K14 ruling): reuse facts and decisions, rephrase in a professional tone suited to the assignment, and keep each fact's A1/A2 reference in the ledger.

- Never carry placeholders, vendor scores or A1 portfolio labels. Never reverse A1's own parking decisions silently.

- Keep the A1/A2 anonymised organisation label ("an integrated oil and gas energy major, global lubricants division"). \[v2\] You have accepted naming public peers in Part C despite the anonymised employer label.

**6.2 Observations that constrain the portfolio \[R\]**

- A1/A2 provide five to six credible opportunities (R1–R5, plus R3 absorbing R6), so the 5–7 count is reachable from documented work.

- No Moonshot is documented. Candidates would be the "scoped-out" extensions in A1 (cross-sell/up-sell, generative account brief) as clearly labelled proposals, or no Moonshot at all, which the worksheet allows.

- Quick Wins may be scarce: R1, R5 and R7 are Red on governance or data in A1. B2 must follow the worksheet definition, not the desire for early wins.

- \[v2\] Priority 1 drives D1. With your sales-workflow scope, R1 (account manager) and R2/R3 (sales teams) are natural, but A1/A2 hold little task-level evidence for sales roles; D2 needs 15–20 discrete tasks that only you can supply accurately. R4 gives rich evidence but may fall outside the scope you set (K17). Decide at G3/G5.

- \[v2\] M1's portfolio lecture illustrates a mix of 4 Quick Wins, 2 Strategic Bets and 1 Moonshot from a 50-idea backlog. The worksheet requires only 5–7 opportunities and no mix, and the rubric penalises labelling by intuition, so this is an example, not a target.

- Part C comparators, A3 benchmarks and Part A indicators for Technology, Talent, Process and Culture are new work needing your input or public research.

**7. Consistency and quality-control plan**

**7.1 Decision & Evidence Ledger (shared reference record) \[R\]**

| **Register**                 | **Contents**                                                                                                                                                  | **Used by**      |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Scope & context              | Chosen scope, anonymised context label, fixed organisation wording                                                                                            | All parts        |
| Glossary & IDs               | Canonical terms (dimension names, H/M/L, Quick Win / Strategic Bet / Moonshot, Lead / Fast follow / Wait); opportunity IDs O1–O7 with one canonical name each | S3, S4           |
| Maturity & constraints       | Six ratings with sub-dimension indicators, source tag, confidence; designated weakest dimension(s)                                                            | A, B, D4.2       |
| Portfolio                    | Per opportunity: problem, pattern, value mechanism, dependency, classification, rank, status                                                                  | B, C, D          |
| Prior-work facts             | Each fact: value, A1/A2 section, status (documented / adapted / new)                                                                                          | S2, S3           |
| Figures                      | Number, unit, basis, derived or documented, every section where it appears                                                                                    | S4 numeric match |
| Assumptions                  | ID, statement, basis, label (assumption / estimate / hypothetical)                                                                                            | S3, S4           |
| Evidence log                 | E-ID, title, organisation, date, URL, access date, section used (feeds WS reference log)                                                                      | C1, C2, A3       |
| Decision log                 | Date, decision, alternatives, approver (always you for judgements)                                                                                            | Agent            |
| Open questions & word counts | Unresolved items; words used vs cap per section                                                                                                               | Agent, S4        |
| Change log                   | Every edit with the sections it touched                                                                                                                       | S4               |

**7.2 Detecting downstream contradictions, repetition and unsupported claims**

| **When this changes**         | **Re-check**                                                   |
|-------------------------------|----------------------------------------------------------------|
| Scope (A1)                    | Everything                                                     |
| A2 rating or indicator        | A4 → B1 dependencies → B2 → B3 → C3 readiness → D4.2 framework |
| B1 membership or pattern      | B2, B3, B4, C2 link, C3, C4, D1                                |
| B2 classification or B3 order | C3, D1, D5 context, executive consistency of "story"           |
| Top three or Priority 1       | B4, C3, C4, D1 → D2 → D3 → D4 → D5                             |
| Any figure or assumption      | Every ledger location of that figure                           |
| Any E-ID source               | Every cell citing it; C1 position; C2 conclusion               |

| **Check (S4)**               | **Method**                                                                                                         | **Result**              |
|------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------|
| Terminology and ID match     | Compare each section's terms and IDs to the glossary                                                               | List of mismatches      |
| Numeric consistency          | Match every number to the Figures register                                                                         | Mismatch list           |
| Cross-section contradictions | Compare ratings, classifications and priorities along the dependency map                                           | Blocking issues         |
| Repetition                   | Find near-duplicate rationale text across sections (e.g. B2 vs B3 vs C3)                                           | Warnings with locations |
| Unsupported claims           | Every factual claim must carry a tag: Documented, Course, Public E-ID, Assumption or Judgement; untagged = flagged | Blocking issues         |
| Rule compliance              | Word caps, row counts (5–7 opportunities, 15–20 tasks), label vocabulary                                           | Pass/fail per field     |

**7.3 Final rubric audit and integrity controls**

- For each of the 18 criteria S4 states where the rubric's full-marks descriptor atoms are evidenced, partly evidenced or missing, with locations. It does not predict marks and I make no promise of any grade.

- Runs the 16-item submission checklist and the 11-item rubric self-check with evidence locations; measures pages from the rendered PDF; confirms all section numbers and tables are retained; confirms the reference log has E-IDs for every public claim.

- Lists quality-modifier risks: placeholders, contradictions, unsupported assertions, missing declaration or disclosure.

- Judgement ownership: ratings, classifications, priorities and positions are recorded as "author judgement" with your approval; the agent produces draft disclosure facts (tools used and how) for you to correct and sign.

**8. Proposed build sequence and approval decisions**

| **Step** | **Activity**                                                                                                                                                  | **Output**                  | **Gate** |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------|
| 0        | You review this design and answer the decisions below                                                                                                         | Approved or revised design  | G0       |
| 1        | Fix platform, working folder and file formats; create ledger schema                                                                                           | Ledger template             | —        |
| 2        | Build S1 and run it on WS/RB; build S4 and run the seeded-error test; build S2 and verify facts against A1/A2; build S3 and test on a non-Assignment-3 sample | Test results for each skill | G1       |
| 3        | S1 generates requirement register, conflict rulings and the template                                                                                          | Template + coverage matrix  | G2       |
| 4        | S2 builds the prior-work fact ledger and candidate assessment                                                                                                 | Ledger, shortlist           | G3       |
| 5        | Drafting loop for A, then B, then C, then D (research for A3/C1/C2 may start early)                                                                           | Approved sections           | G4–G7    |
| 6        | Assembly, PDF render, page and word measurement, full audit                                                                                                   | Draft PDF + audit           | G8       |
| 7        | You finalise disclosure, declaration and submit                                                                                                               | Submission                  | G9       |

**\[v2\] Your answers (recorded)**

| **\#** | **Decision**           | **Your answer**                                                                                | **Effect on the design**                                        |
|--------|------------------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| 1      | Platform               | Agree: portable skill files in XML-tag convention; confirm capabilities at build               | Build step 1                                                    |
| 2      | Working location       | Agree: an "A3_working" subfolder inside the Course 3 folder                                    | Created only after G0                                           |
| 3      | File formats           | Agree: Markdown/XML ledger, DOCX template and drafts, PDF final                                | Fixed                                                           |
| 4      | Skill count            | Four skills                                                                                    | Fixed                                                           |
| 5      | Rulings K1/K2, K7, K14 | Layout advisory (tables vs paragraphs); Module 1 notes supplied; no verbatim quotation         | K1/K2 ruled with conflict K16; K7 mostly resolved; K14 resolved |
| 6      | Peer naming            | Yes                                                                                            | Part C may name public comparators                              |
| 7      | AI-assistance level    | Agree: agent drafts only after you supply judgement                                            | Judgement-capture gate stays                                    |
| 8      | Scope                  | Function scope (Strategy & Analytics within Global Sales & Marketing), sales-related workflows | K11 ruled; K17 open                                             |
| 9      | Deadline               | 15 Oct 2026                                                                                    | Compressed schedule below                                       |

**\[v2\] Still needed from you \[?\]**

6.  **Explicit G0 approval.** Your answers agree with my recommendations, but you have not yet said "approved, proceed to build". Per your original instruction I will not build anything until you do.

7.  **K16:** do you accept that two-column "Field \| Response" tables may become labelled paragraphs (all field labels kept verbatim) while multi-row comparison tables stay as tables, given WS p.1 says to retain tables?

8.  **K17:** does "sales-related workflows" exclude R4 (the leadership-team evidence-pack agent)? Which sales role do you want for Part D, and can you supply 15–20 real tasks for it?

9.  **Programme-rule check (K12):** you agreed to the recommended level. If you have not already, please confirm with the programme that this level of AI assistance is allowed; the agent cannot verify it.

**\[v2\] Compressed schedule for a 15 Oct deadline \[R\]**

Five days leave little room for the full gate sequence. Proposed plan, all dates 2026 and provisional:

| **Date**   | **Work**                                                                                                                                                                                 | **Gate**         |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Sat 10 Oct | You approve G0 and answer K16/K17. Lean build: ledger template and four skill files, light acceptance tests (requirements check on WS/RB, fact check on A1/A2, seeded-error test for S4) | G0, G1           |
| Sun 11 Oct | Template, coverage matrix and layout recommendations; reuse ledger and shortlist                                                                                                         | G2, G3           |
| Mon 12 Oct | Part A and Part B drafting after your judgement inputs; public research for A3 and C1/C2 starts in parallel                                                                              | G4 + G5 combined |
| Tue 13 Oct | Parts C and D drafting                                                                                                                                                                   | G6 + G7 combined |
| Wed 14 Oct | Assembly, PDF render, page and word checks, full audit; your edits                                                                                                                       | G8               |
| Thu 15 Oct | You complete disclosure and declaration and submit                                                                                                                                       | G9               |

Combining gates keeps the dependency checks but halves the number of review rounds. The critical path is your turnaround on judgement inputs (ratings, classifications, top three, role tasks) rather than the agent's drafting.

**This is still the design-only stage. I will not build the agent or skills, generate the template or draft any section until you give explicit approval.**
