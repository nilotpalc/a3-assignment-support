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
</decision_log>

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
