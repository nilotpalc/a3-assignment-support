# G8 Assembly and Full Audit Report (2026-10-17)

Reports only: no content rewritten, no marks assigned or predicted. G8 not approved.

## Outputs
- `build/A3_assembled.pdf` (full submission, 13 pages) and `.md` / `.html`; `build/A3_main_body.pdf` (Parts A-D only, used for measurement).
- `build/assemble.py`, `build/a3_print.css` (assembly and render; pandoc 3 -> HTML -> Microsoft Edge headless print, A4, 10.5 pt body, 9 pt tables).
- `build/g8_ai_use_facts.md` (draft facts for the author's disclosure).
- Assembly rules (author choice 2026-10-17): public evidence tags shown as "(En)", course-note tags as "(course notes, Module n)", internal tags removed; worksheet section titles used verbatim; no wording changed.

## Pages and words (measured from the rendered PDFs with pypdf)
| Item | Pages | Words (PDF text) |
|---|---:|---:|
| Main body, Parts A-D | 11 | 6,672 |
| Submission checklist, evidence log, disclosure, declaration, optional appendix | 2 | 586 |
| Full document | 13 | 7,258 |

Worksheet limit: recommended 16-20 pages of learner responses; maximum 20 excluding references, declaration and optional evidence appendix. Main body: 11 pages, within the maximum, below the recommended range.

## Findings
Blocking: none.

| # | Severity | Location | Finding |
|---|---|---|---|
| W1 | Warning | Whole document | Main body is 11 pages against a recommended 16-20 (maximum 20 met). The 20-page figure is a ceiling; the recommendation is not a mark criterion. |
| W2 | Warning | A3 vs C1 | A3 describes Gulf Oil as taking "early steps to embed AI and machine learning" with "Structured AI execution not evidenced" (E2); C1 rates Gulf "Scaling (early, lower confidence)" (E5, E6). Reconcilable (different sources and lens) but a reader may see tension. |
| W3 | Warning | B3 vs B4, C3, C4 (P4) | B3: "source content changes rarely, so little immediate governance effort is needed". C3: readiness "content exists but is fragmented across sources, with no governance". C4: "weak governance lets content go stale". B4: an unversioned repository may recommend "withdrawn, discontinued or superseded products". |
| W4 | Warning | Ledger evidence register | E3 is cited in C1 ("newer than A3's source (E3)") but its used_in field lists "A3, C2". The reference log uses the draft-derived value "A3, C1, C2". Proposed ledger fix: E3 used_in -> "A3, C1, C2". |
| W5 | Warning (carried) | Ledger / B2 | qa_checks.py: P4 is a Quick Win with a Medium (Data) dependency and needs an explicit rationale. B2 row 4 gives one: "remaining gaps do not block release", "No significant technical hurdles; deployment within 3-6 months". The script reads only the ledger, so the warning persists mechanically. |
| N1 | Note | Assembly | Not reproduced: worksheet instruction boxes (D2 "Assessment adaptation" and "Classification test") and the Participant-Facing Scoring Summary (reference tables, no response fields). D4.1 and D4.2 checkbox rows appear as stated choices ("AI Product Managers", "Accenture Transition-Stage") under the approved labelled-paragraph layout. |
| N2 | Note | D2 "Why" column | The three taught tests are explicit in most rows; in rows 5, 12 and 14 they are implicit (for example row 14: "apparent similarity does not prove that outcomes will transfer"). |
| N3 | Note | D3 | Success measures are unchanged in name ("the same three measures"); the change is a 10-15% target rise, labelled "an author target and unproven". |

Mechanical checks (qa_checks.py, 19 drafts): 0 blocking, 1 warning (W5). No placeholders, untagged numeric claims, undefined IDs, rating or classification mismatches, cross-section repetition or verbatim reuse of Assignments 1-2. Assembled text: no residual tags, comments or empty citations.

Cross-section chain: A2 ratings = ledger maturity (Technology M, Data M, Talent L, Process L, Culture M, Governance M; overall Low); B2 classifications and B3 ranks = ledger portfolio; C3, C4, D1 use P4 as Priority 1; D4.2 cites Talent and Process Low; D3 and D5 task numbers match D2 classifications (13 Augmentable, 7 Irreducibly human, 0 Automatable).

## Caps and formats
| Section | Cap | Used | Section | Cap | Used |
|---|---|---|---|---|---|
| A1 | 200 | 194 | C1 | 350 | 274 |
| A2 | 150 (table uncapped) | 129 | C2 | 200 (after table) | 122 |
| A3 | 250 | 245 | C3 | 50 per rationale | 45/42/48 |
| A4 | 250 | 240 | C4 | 250 | 246 |
| B1 | none (5-7 rows) | 5 rows | D1 | 200 | 155 |
| B2 | 50 per row | 49/44/46/43/45 | D2 | 15-20 rows | 20 rows |
| B3 | 300 | 280 | D3 | 300 | 291 |
| B4 | 250 | 201 | D4 | 200 | 199 |
| | | | D5 | 300 | 268 |

Section numbers retained: Parts A-D; A1-A4, B1-B4, C1-C4, D1-D5, D4.1, D4.2; checklist, evidence reference log (E1-E10), disclosure, honour declaration. Optional evidence appendix: no appendix material in any draft; main text stands alone.

## Rubric audit (descriptor atoms; no marks)
| Criterion | Evidenced | Partly evidenced / observations |
|---|---|---|
| A1 | Scope (Function), bounded context, evidence sources, explicit limitations (A1) | - |
| A2 | Six dimensions on taught sub-dimensions, indicators, gaps, uncertainty test (A2 table and response) | Culture leadership commitment and Governance AI policy marked Not evidenced |
| A3 | Baseline (E1) + two peers (E2, E3), absolute vs relative, implication (A3) | Castrol row: no basis for comparison |
| A4 | Two constraints from A2, blocked opportunities, interventions, improvement evidence (A4) | - |
| B1 | Five distinct problems, pattern, value mechanism, Part A dependency (B1) | P3 quantified value Not evidenced |
| B2 | All five classified, readiness and time/uncertainty rationales (B2) | W5 |
| B3 | Top three, readiness conditions, change triggers, balance (B3) | Sequencing line names impact, readiness and capability; time-to-impact and risk sit in B2 and row text |
| B4 | Upstream/downstream chain, compounding, propagation, control (B4) | - |
| C1 | Two comparators, five categories, traceable E4-E10, positions, attention conclusion (C1) | C1 states the multiple-signal test is "only partly met"; W2 |
| C2 | Five forces, direction, side, link to P4 and P2 (C2) | - |
| C3 | Three factors per initiative; positions differ: Lead, Wait, Fast follow (C3) | W3 |
| C4 | Three tests separately, proportionate conclusion, strengthen/erode (C4) | - |
| D1 | Role linked to Priority 1, bottleneck, no headcount assumption (D1) | - |
| D2 | 20 discrete tasks, frequency basis, classification, boundary (D2) | N2 |
| D3 | Automation scope, augmented work, redeployment, measures (D3) | N3 |
| D4.1 | Role family, bottleneck, build choice (D4) | - |
| D4.2 | Taught framework tied to Part A maturity, one structural change (D4) | - |
| D5 | Three conditions, metrics, frontier tasks, retain and redesign conditions (D5) | - |

## Submission checklist (16 items; ticks are the author's)
| # | Item (short) | Where satisfied |
|---|---|---|
| 1 | Scope and evidence | A1 |
| 2 | Six dimensions with sub-dimensions | A2 table |
| 3 | Self-assessment vs benchmark | A2 vs A3 |
| 4 | 5-7 opportunities, not all GenAI | B1 (5; hybrid ML/rules/GenAI) |
| 5 | Classifications match readiness | B2 (W5) |
| 6 | Top three consistent with Part A | B3, A4 |
| 7 | Competitive claims sourced or Not evidenced | A3, C1, C2; log E1-E10 |
| 8 | Five signal categories | C1 |
| 9 | Initiative-specific positions | C3 |
| 10 | Tasks, not job elimination | D1, D3 |
| 11 | At least 15 tasks | D2 (20) |
| 12 | Capacity redeployed | D3 |
| 13 | Framework matches maturity | D4.2 |
| 14 | Three-condition evidence plan | D5 |
| 15 | Assumptions labelled | A1, D2 frequency basis, D3, D5 |
| 16 | AI assistance disclosed | Author to complete (disclosure blank) |

## Rubric self-check (11 items)
Items 1-10: satisfied at A1; A2; B1; B2; B3; A3/C1/log; C3; D2; D3; D5 respectively. Item 11 (assumptions, anonymisation, hypothetical elements and AI assistance disclosed): assumptions and anonymisation labelled (A1, D2, D3); AI assistance pending the author's disclosure.

## Quality-modifier risks
- Missing declaration or disclosure: both blank by design; the rubric's -5 descriptor names "missing declaration". Author must complete before submission (G9).
- Placeholders, unsupported assertions, fabrication: none found by the mechanical checks.
- Contradictions: W2 and W3 for the author to review.
