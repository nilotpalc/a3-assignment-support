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
stage: G1 build acceptance pending
deadline: 2026-10-15
last_updated: 2026-10-10
</status>

<scope_and_context>
function: Strategy & Analytics within Global Sales & Marketing
workflow_focus: sales-related workflows
organisation_label_in_A1_A2: an integrated oil and gas energy major (global lubricants division); function declared in A1/A2 as "Strategy and Analytics (Global Lubricants)"
label_to_confirm_at_G4: exact organisation and function wording for Assignment 3 (keep consistent with A1/A2 anonymisation; public peers may be named in Part C)
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
</maturity>

<portfolio>
# OppID|Name|AI_pattern|Classification|Rank|Dependency_dimension|Dependency_rating|Status
</portfolio>

<figures>
# FigID|Value|Unit|Basis|Status(documented/derived/assumption)|Source_ref|Sections_used
</figures>

<assumptions>
# AssID|Statement|Basis|Label(assumption/estimate/hypothetical)
</assumptions>

<evidence>
# E_ID|Title|Organisation|Date|URL|Accessed|Used_in
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
K8|M2/M3 are summaries with transcripts omitted; probable typo "GO-6N"; salary and statistics figures self-flagged as unverified.|M2, M3|Cite as "course notes" for frameworks; verify any figure before presenting it as external fact.|[R]
K9|A1 sequences churn as "Now" although its data and governance readiness are Red; Course 3 defines Quick Win as "most required readiness already in place".|A1 D1.3, A2.1; WS p.5|Re-classify under Course 3 definitions; do not import A1 labels.|[R]
K10|A1 charter holds unfilled placeholders ([X]%, [N], [3–4]).|A1 D2.1|Never carry; ask you for real values or omit.|[V]
K11|A1/A2 anchor on "Strategy and Analytics (Global Lubricants)", but several A1 opportunities belong to sales or supply-chain workflows.|A1 cover; WS p.2|[v2] Your ruling: function scope (Strategy & Analytics within Global Sales & Marketing), using sales-related workflows. Open point: whether R4 (leadership-team evidence-pack agent, an internal strategy workflow) counts as sales-related (see section 6).|[v2] Ruled; one open point
K12|Rule against uploading restricted employer information to public AI tools; programme's detailed rules not supplied; A1/A2 contain internal-looking figures (anonymised label).|WS p.14|Confirm prior content is cleared for use with the tool you choose; agent works only from submitted, anonymised material and requests no new confidential detail.|[?]
K13|No submission deadline appears in any source.|WS, RB|[v2] Deadline 15 Oct 2026. Compressed gate plan proposed in section 8.|[v2] Resolved
K14|No rule on verbatim reuse of earlier text.|WS p.1|[v2] Your ruling: no verbatim quotation; rephrase messaging in a professional tone suited to the assignment. S3 and S4 enforce this (S4 flags long matches to A1/A2 text).|[v2] Resolved
K15|Vendor scoring in A2 Part C vs "not a vendor-selection exercise".|A2 Part C; WS p.2|Exclude vendor scoring; reuse only the use case.|[V]
K16|[v2] Your layout ruling (convert tables to paragraphs where answers are short) conflicts with WS p.1: "retain all section numbers, response fields and tables".|WS p.1|Keep multi-row comparison tables (A2, A3, B1–B3, C1–C3, D2, D3, D5 test conditions) as tables, compactly set. For two-column "Field \/ Your response" tables (A1, B4, C4, D1, D4, D5 decision rows) the agent may recommend a labelled-paragraph layout that keeps every field label verbatim. You confirm before G2 that you accept this reading.|[?]
K17|[v2] "Sales-related workflows" scope may exclude R4 and its natural D1 role (Commercial Strategy Analyst); sales roles have thinner task evidence in A1/A2.|Your ruling; A1, A2|Decide at G3 whether R4 stays in scope; supply real task data for the chosen role.|[?]
</k_register>

<open_questions>
- Exact organisation/function wording for Assignment 3 (G4)
- Sales role for Part D and the 15-20 real tasks (G3/G5)
- Whether word caps that say "across the table" still apply when a table becomes a labelled paragraph (agent default: yes, same cap)
</open_questions>

<word_counts>
# SectionID|Cap|Used|Date
</word_counts>

<change_log>
2026-10-10 | Ledger initialised with approvals and rulings only; no assignment content
</change_log>
