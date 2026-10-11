---
name: a3_decision_and_evidence_ledger
description: Single shared reference record for Assignment 3. Written only by the agent. Skills read slices and return proposed entries.
---
<ledger_rules>
- Single writer: the agent. Skills never edit this file.
- Every judgement (rating, classification, rank, position, scope) is recorded in <decision_log> with approver = Nilotpal.
- Machine-readable registers use one row per line, fields separated by "|". Lines starting with "#" are comments. Do not use "|" inside a field.
- Claim tags used in drafts: [D:ref] documented in A1/A2 or a source; [C:ref] course notes; [E:ID] public evidence; [A:ID] labelled assumption; [F:ID] ledger figure; [J] author judgement; [R:Dimension=Rating] rating mention; [L:OppID=Classification] classification mention.
</ledger_rules>

<status>
version: 0.1 (build stage)
stage: G4+G5 combined (Parts A and B); Part A sections approved, Part B next; G3 approved
deadline: 2026-10-15
last_updated: 2026-10-10
</status>

<scope_and_context>
function: Strategy & Analytics within Global Sales & Marketing
workflow_focus: sales-related workflows
organisation_label_in_A1_A2: an integrated oil and gas energy major (global lubricants division); function declared in A1/A2 as "Strategy and Analytics (Global Lubricants)"
a3_label: Strategy & Analytics, Global Lubricants Sales & Marketing (integrated energy major, anonymised) (author judgement 2026-10-11)
assessment_scope: Function; sales-related workflows incl. R4 LT evidence pack
</scope_and_context>

<glossary>
# canonical|banned_variants (semicolon separated)
Quick Win|Quick-Win;quick win
Strategic Bet|Strategic-Bet;strategic bet
Moonshot|Moon-shot;moonshot
Fast follow|Fast follower;Fast-follow;Follow;Follower
Wait|Hold;Defer
Irreducibly human|Irreducibly-human
</glossary>

<allowed_vocabulary>
classification: Quick Win;Strategic Bet;Moonshot
position: Lead;Fast follow;Wait
rating: High;Medium;Low
dimensions: Technology;Data;Talent;Process;Culture;Governance
</allowed_vocabulary>

<maturity>
# Dimension|Rating|Confidence|Indicators_source|Weakest_flag
Technology|Medium|Not stated|author observation (A2 input 2026-10-11)|
Data|Medium|Not stated|author observation; A1-038|
Talent|Low|Least confident|author observation (about ten-plus stakeholders)|weakest (tied)
Process|Low|Not stated|author observation|weakest (tied)
Culture|Medium|Not stated|author observation|
Governance|Medium|Not stated|author observation|
# Overall readiness: Low (capped by Talent and Process; weakest-dimension rule, course notes M1)
</maturity>

<portfolio>
# OppID|Name|AI_pattern|Classification|Rank|Dependency_dimension|Dependency_rating|Status
</portfolio>

<figures>
# FigID|Value|Unit|Basis|Status(documented/derived/assumption)|Source_ref|Sections_used
</figures>

<assumptions>
# AssID|Statement|Basis|Label(assumption/estimate/hypothetical)
AS1|The function has an estimated 20-25 core sales and marketing excellence processes to document|Author estimate (G4 input, 2026-10-11)|estimate
</assumptions>

<evidence>
# E_ID|Title|Organisation|Date|URL|Accessed|Used_in
E1|AI Adoption Index 2.0: Tracking India's Sectoral Progress in AI Adoption|NASSCOM|2024|https://nasscom.in/knowledge-center/publications/ai-adoption-index-20-tracking-indias-sectoral-progress-ai-adoption (findings also reproduced at indiaai.gov.in)|2026-10-11|A3
E2|Gulf Oil Lubricants India Limited Annual Report 2025-26 (PDF pp. 27, 29, 44, 54)|Gulf Oil Lubricants India Ltd|2026-08|https://assets.gulfoilltd.com/gulfindia/files/2026-08/GOLIL_Annual_Report_2025-26_0.pdf (listed at https://india.gulfoilltd.com/investors/annual-reports)|2026-10-11|A3
E3|Castrol turns 125 and looks to the future (press release)|Castrol (bp)|2024-01-10|https://www.castrol.com/en/global/corporate/about-castrol/newsroom/castrol-125.html|2026-10-11|A3
</evidence>

<prior_work_facts>
# kept in ledger/prior_work_facts.tsv (S2 output)
</prior_work_facts>

<decision_log>
2026-10-10 | G0 | Design approved ("Approved, proceed to build") | Nilotpal
2026-10-10 | Platform | Portable skill files in XML-tag convention; confirm capabilities at build | Nilotpal
2026-10-10 | Working location | Subfolder A3_working inside Course 3 folder | Nilotpal
2026-10-10 | Repo move | Master copy moves to a private GitHub repository (.github/agents, .github/skills; worked in VS Code / PyCharm / GitHub Copilot). Notion pages become a mirror and are not edited. Supersedes the working location above | Nilotpal
2026-10-10 | File formats | Markdown/XML ledger; DOCX template and drafts; PDF final | Nilotpal
2026-10-10 | Skill count | Four skills | Nilotpal
2026-10-10 | K1/K2 | Table cells use page space; agent recommends table vs paragraph per field | Nilotpal
2026-10-10 | K16 | Multi-row comparison tables stay tables; two-column Field|Response tables may become labelled paragraphs (labels verbatim); detailed tables may go in an Appendix kept below the response while writing, moved to the consolidated appendix at the end | Nilotpal
2026-10-10 | K7 | Module 1 notes supplied | Nilotpal
2026-10-10 | K14 | No verbatim quotation of prior work; rephrase in professional tone | Nilotpal
2026-10-10 | K11/K17 | Function scope S&A within Global S&M; sales-related workflows; the leadership-team evidence-pack agent counts as sales-related (supports S&M-driven strategy dilemmas) | Nilotpal
2026-10-10 | Peers | Public comparators may be named in Part C | Nilotpal
2026-10-10 | AI assistance | Drafting only after user supplies judgement; programme confirmation given by user | Nilotpal
2026-10-10 | K13 | Deadline 15 Oct 2026 | Nilotpal
2026-10-10 | G1 | Build acceptance approved; no changes or conditions listed | Nilotpal
2026-10-10 | G2-K1 | Table cells consume page space; recommend table/paragraph per field. Worksheet caps: A1, A3, A4, B2 rationale columns, B3, B4, C1, C3, C4, D1, D3, D4, D5 include table cells; A2 and C2 caps apply after tables; B1 and D2 have no stated word cap. Caps bind; 16-20 pages recommended and 20-page response maximum excludes references, declaration and optional evidence appendix. | Nilotpal
2026-10-10 | G2-K2 | C1 telegraphic cells with E-IDs are permitted only if cells count toward the 350-word maximum. | Nilotpal
2026-10-10 | G2-K3 | Worksheet governs D2: 15-20 discrete representative tasks in main submission; optional 30-50 task decomposition may go in appendix. | Nilotpal
2026-10-10 | G2-K4 | Use H/M/L maturity ratings only; A1 RAG may seed evidence but is not carried over as a rating. | Nilotpal
2026-10-10 | G2-K5 | Use positioning labels Lead / Fast follow / Wait. | Nilotpal
2026-10-10 | G2-K6 | C1 uses two comparators plus an optional third, following worksheet. | Nilotpal
2026-10-10 | G2-K7 | Module 1 notes supplied and used for indicators and weakest-dimension rule; energy/lubricants baseline requires new evidence or "Not evidenced". | Nilotpal
2026-10-10 | G2-K8 | Cite M2/M3 frameworks as "course notes"; verify figures before presenting as external facts; notes are not primary evidence. | Nilotpal
2026-10-10 | G2-K9 | Re-classify A1 opportunities under Course 3 definitions; Quick Win requires most required readiness already in place. | Nilotpal
2026-10-10 | G2-K10 | Do not carry A1 placeholders [X]%, [N], [3-4]; request real values or omit. | Nilotpal
2026-10-10 | G2-K11 | Scope is Strategy & Analytics within Global Sales & Marketing, using sales-related workflows. | Nilotpal
2026-10-10 | G2-K12 | Author confirmed with programme that this level of AI assistance is allowed; author remains responsible for disclosure, accuracy and analysis. | Nilotpal
2026-10-10 | G2-K13 | Deadline 15 Oct 2026; compressed gate plan may be used only with author consent. | Nilotpal
2026-10-10 | G2-K14 | No verbatim quotation of prior work; professionally rephrase and keep A1/A2 fact references in ledger. | Nilotpal
2026-10-10 | G2-K15 | Exclude vendor scoring from A2 Part C; reuse only the use case. | Nilotpal
2026-10-10 | G2-K16 | Keep listed multi-row comparison tables compact; two-column Field/Your response tables may be labelled paragraphs with every worksheet field label verbatim. Detailed supporting tables may move to consolidated optional appendix; main text stands alone. Word caps remain unchanged. | Nilotpal
2026-10-10 | G2-K17 | R4 leadership-team evidence-pack agent stays in scope as a sales-related workflow supporting S&M-driven strategy dilemmas. | Nilotpal
2026-10-10 | G2-K18 | Use inferred form-feed page numbers when PDF page labels are unavailable. | Nilotpal
2026-10-10 | G2 | Template, requirement register, conflict register, coverage matrix and K1-K18 rulings approved; changes: none | Nilotpal
2026-10-10 | G3 provisional shortlist | Approved five candidates: churn early warning; order-status/lead-time exception visibility; explainable lead-generation research; sector-matched value cases; LT evidence-pack workflow. Sales administration and a standalone CI data product remain reserves because of prior parking/overlap. | Nilotpal
2026-10-10 | Provisional B3 preference supplied at G3 | 1 Explainable lead-generation research; 2 LT evidence-pack workflow; 3 Churn early warning. Reconfirm after A2/A4 maturity evidence; not a final B3 ranking. | Nilotpal
2026-10-10 | G3 prior-work fact ledger | ledger/prior_work_facts.tsv confirmed correct (72 facts). A1 Red/Amber/Green rows A1-014 to A1-022 kept as legacy evidence, not transferable as Assignment 3 ratings (K4). Tightening of A1-002, A1-024, A1-032, A1-034, A2-006 to unique exact strings approved. | Nilotpal
2026-10-10 | Provisional B3 preference reconfirmed | Top three unchanged: 1 Explainable lead-generation research; 2 LT evidence-pack workflow; 3 Churn early warning. Still subject to A2/A4 maturity evidence. | Nilotpal
2026-10-10 | G3-K17 | R4 (LT evidence-pack workflow) stays in scope: counted as sales-related because it supports Global Sales & Marketing leadership decisions. Top three unchanged. | Nilotpal
2026-10-10 | G3 | Prior-work fact ledger (72 facts, 0 misses), candidate assessment and five-candidate shortlist approved; changes: A1-002, A1-024, A1-032, A1-034, A2-006 tightened to source-unique exact strings; K17 ruled (R4 in scope); provisional top three unchanged | Nilotpal
2026-10-11 | A1 scope (author judgement) | Assessment scope = Function; label "Strategy & Analytics, Global Lubricants Sales & Marketing (integrated energy major, anonymised)"; sales-related workflows incl. R4 | Nilotpal
2026-10-11 | A1 section | drafts/A1.md approved as drafted (194/200 words) | Nilotpal
2026-10-11 | A2 ratings (author judgement) | Technology Medium; Data Medium; Talent Low; Process Low; Culture Medium; Governance Medium; overall Low (capped by Talent and Process); least-confident = Talent | Nilotpal
2026-10-11 | A2 Talent indicator (author judgement) | "Delivery relies on 2-3 part-time analysts" confirmed as a current observed fact (distinct from A1-042, which was proposed resourcing) | Nilotpal
2026-10-11 | A2 section | drafts/A2_table.md (table, no cap) and drafts/A2.md (129/150) approved as drafted | Nilotpal
2026-10-11 | A3 comparators (author judgement) | NASSCOM AI Adoption Index 2.0 (E1); Gulf Oil Lubricants India AR FY2025-26 as primary, verified wording only (E2); Castrol (bp) 125 release kept as optional third row, "AI readiness not disclosed" (E3) | Nilotpal
2026-10-11 | A3 relative position (author judgement) | On par: NASSCOM on Data and Governance (Process Low mirrors sector execution gap); Gulf on Technology. Behind Gulf on customer-facing channel data and structured sales-talent development. Castrol: no basis for comparison. Culture not evidenced against any comparator | Nilotpal
2026-10-11 | A3 section | drafts/A3.md approved as drafted (245/250), closing absolute-vs-relative paragraph kept below the table | Nilotpal
2026-10-11 | A4 constraints (author judgement) | Constraint 1 = Process (Low), standardisation and documentation; constraint 2 = Data (Medium), no owned data definitions; Talent (Low) addressed through process and data standards rather than as a separate constraint. Blocked opportunities: Process -> explainable lead-generation research, LT evidence pack; Data -> churn early warning, order-status/lead-time visibility, sector-matched value cases | Nilotpal
2026-10-11 | A4 section | drafts/A4.md approved as drafted (240/250), incl. note on why Talent is not a separate constraint | Nilotpal
2026-10-11 | Compressed gate plan | Author consents to combining G4+G5 (Parts A and B) and G6+G7 (Parts C and D) into one review each for the 15 Oct 2026 deadline. A combined gate passes only on explicit written approval of all parts in it; G4 is held open and reviewed with Part B. Post-gate edits re-open only sections named by the dependency map. G8 and G9 unchanged | Nilotpal
</decision_log>

<k_register>
# Definitions copied from design/A3_Agent_Skills_Design_Proposal_v2.md section 2.4. Rulings made after the proposal are recorded in decision_log, not here.
# K_ID|Issue|Sources|Proposed_handling|Status_in_proposal
K1|Stated caps total ≈3,600 words (A1 200, A2 150, A3 250, A4 250, B2 250–350, B3 300, B4 250, C1 350, C2 200, C3 150, C4 250, D1 200, D3 300, D4 200, D5 300) plus uncapped tables (A2, B1, D2). Unclear whether "across the table" caps include table cells; unclear how this reaches 16–20 pp.|WS pp.1, 3–12|[v2] Your ruling: table cells consume page space, so the agent recommends table or paragraph layout per field. Caps as worded in WS: A1, A3, A4, B3, B4, C1, C3, C4, D1, D3, D4, D5 and B2 (rationale columns) include table cells; A2 and C2 caps apply to text after the table; B1 and D2 have no stated cap. Caps stay binding; page range is recommended; S4 reports both. Layout limits: see K16.|[v2] Ruled; layout conflict K16
K2|C1: two or three comparators × five signals plus an explanation in 350 words.|WS p.7|Telegraphic cells with E-IDs; allow only if cells count toward the cap as stated.|[?]
K3|Task decomposition: 30–50 (Video 24, M3) vs 15–20 in the main submission.|WS p.9; RB p.1; M3|Worksheet governs. Optional 30–50 list goes in the appendix.|[V] resolved by source hierarchy
K4|Rating scales: H/M/L (WS), 1-2-5 (M2 action item), Red/Amber/Green on three questions (A1).|WS p.4; M2; A1 A2.1|Use H/M/L only. A1 RAG ratings can seed evidence but not be copied as ratings.|[V]
K5|Positioning labels: "Lead / Fast follow / Wait" (table) vs "lead/follow/wait" (headings, checklist, M3).|WS pp.8, 13; RB p.3|Use the table labels.|[V]
K6|Comparators: two plus optional third (WS) vs "top 3" (M3).|WS p.7; M3|Worksheet governs.|[V]
K7|Module 1 content (sub-dimension indicator definitions, benchmarking method, portfolio background) is referenced but absent from the supplied pages. WS lists the sub-dimension names only.|WS p.4; M2|[v2] Module 1 notes supplied. They give indicators for each dimension (Technology: infrastructure, integration, technical debt; Data: quality, accessibility, strategic value; Talent: skills inventory, learning culture, leadership capability; Process: standardisation, documentation, automation baseline; Culture: four indicators; Governance: four components) and the weakest-dimension rule. Residual: the notes give only high-level benchmarking method and India-centred sources, so the energy/lubricants baseline is new research.|[v2] Mostly resolved
K8|M2/M3 summaries omit transcripts; probable typo "GO-6N"; salary and statistics figures self-flagged as unverified.|M2, M3|Cite as "course notes" for frameworks; verify any figure before presenting it as external fact.|[R]
K9|A1 sequences churn as "Now" although its data and governance readiness are Red; Course 3 defines Quick Win as "most required readiness already in place".|A1 D1.3, A2.1; WS p.5|Re-classify under Course 3 definitions; do not import A1 labels.|[R]
K10|A1 charter holds unfilled placeholders ([X]%, [N], [3–4]).|A1 D2.1|Never carry; ask you for real values or omit.|[V]
K11|A1/A2 anchor on "Strategy and Analytics (Global Lubricants)", but several A1 opportunities belong to sales or supply-chain workflows.|A1 cover; WS p.2|[v2] Your ruling: function scope (Strategy & Analytics within Global Sales & Marketing), using sales-related workflows. Open point: whether R4 (leadership-team evidence-pack agent, an internal strategy workflow) counts as sales-related (see section 6).|[v2] Ruled; one open point
K12|Rule against uploading restricted employer information to public AI tools; programme's detailed rules not supplied; A1/A2 contain internal-looking figures (anonymised label).|WS p.14|Confirm prior content is cleared for use with the tool you choose; agent works only from submitted, anonymised material and requests no new confidential detail.|[?]
K13|No submission deadline appears in any source.|WS, RB|[v2] Deadline 15 Oct 2026. Compressed gate plan proposed in section 8.|[v2] Resolved
K14|No rule on verbatim reuse of earlier text.|WS p.1|[v2] Your ruling: no verbatim quotation; rephrase messaging in a professional tone suited to the assignment. S3 and S4 enforce this (S4 flags long matches to A1/A2 text).|[v2] Resolved
K15|Vendor scoring in A2 Part C vs "not a vendor-selection exercise".|A2 Part C; WS p.2|Exclude vendor scoring; reuse only the use case.|[V]
K16|[v2] Your layout ruling (convert tables to paragraphs where answers are short) conflicts with WS p.1: "retain all section numbers, response fields and tables".|WS p.1|Keep multi-row comparison tables (A2, A3, B1–B3, C1–C3, D2, D3, D5 test conditions) as tables, compactly set. For two-column "Field \/ Your response" tables (A1, B4, C4, D1, D4, D5 decision rows) the agent may recommend a labelled-paragraph layout that keeps every field label verbatim. You confirm before G2 that you accept this reading.|[?]
K17|[v2] "Sales-related workflows" scope may exclude R4 and its natural D1 role (Commercial Strategy Analyst); sales roles have thinner task evidence in A1/A2.|Your ruling; A1, A2|Decide at G3 whether R4 stays in scope; supply real task data for the chosen role.|[?]
K18|Page-citation policy. Use inferred form-feed page numbers when PDF page labels are unavailable.|WS/RB source text copies|Use inferred form-feed page numbers when PDF page labels are unavailable.|Added for G2
</k_register>

<open_questions>
- Sales role for Part D and the 15-20 real tasks (G5); K17 keeps the Commercial Strategy Analyst role open as an option
</open_questions>

<word_counts>
# SectionID|Cap|Used|Date
A1|200|194|2026-10-11
A2|150 (after table; table uncapped)|129 (table 623)|2026-10-11
A3|250|245|2026-10-11
A4|250|240|2026-10-11
</word_counts>

<change_log>
2026-10-10 | Ledger initialised with approvals and rulings only; no assignment content
2026-10-10 | Recorded author G2 K1-K18 rulings; generated requirement register, conflict/gap register, structure-only template and two-way coverage matrix for review; G2 approved with no changes requested
2026-10-10 | Recorded author-approved G3 candidate pool and provisional top-three preference; G3 gate not recorded as approved
2026-10-10 | prior_work_facts.tsv: A1-002, A1-024, A1-032, A1-034, A2-006 replaced with source-unique exact strings and clarified notes; fact_check 72 facts, 0 misses, 3 placeholders flagged; author confirmed fact ledger and top three; G3 gate still not recorded as approved
2026-10-10 | K17 ruled (R4 in scope); G3 approved by author; stage moved to G4 scope and Part A
2026-10-10 | g3-approve re-run for consistency: single G3 approval row reworded to the standard gate format (no duplicate added); changes already applied; no sections re-opened; build/ledger_view.md regenerated
2026-10-10 | Duplicate G2 approval row removed at author request; kept the K1-K18 row (K18 page-citation ruling is part of G2); no sections re-opened
2026-10-11 | G4 started. A1 drafted (drafts/A1.md, 194/200), delta QA 0 blocking / 0 warnings, approved by author; label recorded in scope_and_context and decision_log; open question on label closed. Stray duplicate </change_log> tag removed (format fix only)
2026-10-11 | A3 research (early): NASSCOM claims verified; Castrol claims verified (AI appears once, heritage video only); Gulf FY2024-25 claims partly verified (genAI claim not found); E-IDs not yet assigned pending author choice
2026-10-11 | A2 drafted as two files (A2_table.md uncapped table; A2.md 150-word response) so the QA cap check applies only to capped text; ratings recorded in maturity register; delta QA 0 blocking / 0 warnings; approved by author
2026-10-11 | A3 drafted with E1-E3 (verified: NASSCOM; Gulf AR FY2025-26 replaced FY2024-25 at author choice; Castrol release 10 Jan 2024); delta QA 0 blocking after trim 254->245; approved by author
2026-10-11 | A4 drafted (Process Low first, Data Medium second, per author reorder); AS1 added to assumptions; delta QA 0 blocking / 0 warnings; approved by author. All Part A sections approved; G4 not yet approved
2026-10-11 | Compressed plan recorded: G4+G5 and G6+G7 combined; status stage updated; no gate recorded as approved; no sections re-opened</change_log>