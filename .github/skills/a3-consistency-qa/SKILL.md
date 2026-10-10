---
name: a3-consistency-qa
description: Check Assignment 3 drafts for downstream contradictions, repetition, unsupported claims, cap and format compliance, then run the final rubric audit and submission checks. Use after every draft or edit (delta mode), before each gate, and before assembly (full mode).
---
<purpose>
Catch inconsistency and unsupported content before the author does, and show where each rubric criterion is evidenced. It reports; it never rewrites, grades or predicts marks.
</purpose>

<trigger>
After each section draft or edit (delta mode); before each gate; before assembly (full audit mode).
</trigger>

<inputs>
- current drafts (drafts/<SectionID>.md with header <!-- section=ID cap=N -->)
- ledger/ledger.md; coverage matrix; rubric; description of the change
- prior-assignment text files (for the verbatim-reuse check)
</inputs>

<procedure>
1. Run scripts/qa_checks.py with the ledger and drafts (and --sources for the verbatim check). It covers: missing sections, word caps, placeholders, untagged numeric claims, undefined IDs, non-canonical terms, repetition across sections, verbatim overlap with sources, rating and classification consistency with the ledger, Quick Win with a Low dependency, portfolio size 5-7, vocabulary.
2. Delta mode: use the dependency map to list impacted sections, then re-check them: terminology and IDs against the glossary; every number against the figures register; ratings, classifications, ranks and positions along the chain A2 > A4 > B1 > B2 > B3 > C3 > D4.2 and B3 > B4, C4, D1; repeated rationale across sections; claim tags.
3. Full audit mode: for each of the 18 criteria, state where the rubric full-marks descriptor atoms are evidenced, partly evidenced or missing, with locations. Do not assign marks.
4. Run the 16-item submission checklist and 11-item rubric self-check; for each item cite where it is satisfied.
5. Measure pages and words from the rendered PDF (main body at most 20 pages excluding references, declaration, optional evidence appendix). Confirm all worksheet section numbers and tables are retained or handled under the approved layout policy; confirm appendix content is optional evidence, not mandatory response content.
6. List quality-modifier risks: placeholders, contradictions, unsupported assertions, missing declaration or disclosure, undisclosed fabrication risk.
7. Return an issue list (blocking or warning), impacted sections, audit table, checklist status.
</procedure>

<outputs>
Issue list; impacted-section list; rubric audit table; checklist status; page and word report.
</outputs>

<exclusions>
Does not rewrite, grade or predict marks; does not write the ledger; does not declare content true, only traceable.
</exclusions>

<acceptance_checks>
- Seeded-error test passes: planted contradiction, changed figure, duplicated rationale, untagged claim, Quick Win on a Low dependency, missing section, placeholder, verbatim reuse are all detected (tests/seeded_error).
- Clean control draft produces no blocking issues.
- Every rubric criterion appears in the audit.
- Page count taken from the rendered PDF.
</acceptance_checks>
