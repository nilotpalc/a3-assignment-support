---
name: a3-requirements-template
description: Extract and verify Assignment 3 requirements from the worksheet and rubric, maintain the conflict register, and (only after build approval) generate the assignment template and rubric-coverage matrix. Use at the start of the workflow and whenever a source file or ruling changes.
---
<purpose>
Turn the verified worksheet and rubric into (1) a requirement register, (2) a conflict and gap register, (3) an assignment template, (4) a two-way rubric-coverage matrix. The template is a structure, never a draft.
</purpose>

<trigger>
Stage 1 of the workflow. Re-run when a source file's modified time changes, when the author issues a ruling, or when the coverage matrix fails an acceptance check.
</trigger>

<inputs>
- worksheet and rubric PDFs by exact filename (convert to text; keep page numbers)
- ledger decision_log rulings (K-items)
- {{mode}}: "extract" (register + conflicts only) or "generate" (template + matrix; allowed only after G1 and with the register frozen)
</inputs>

<procedure>
1. Resolve the two files by exact name. Record their modified times. If a file is missing or ambiguous, stop and ask.
2. Build the requirement register: one row per section, field, table, word cap, mark value and rubric descriptor. Columns: ID (R-<section>-<n>), source (WS/RB + page), text (short paraphrase or reference, no long quotes), type = Mandatory | Budget | Descriptor | Recommended, marks, cap.
3. Verify numbers: part marks sum to 25/30/20/25 and 100; quality modifier +5 to -5; criterion marks identical in the worksheet scoring table, section headings and rubric. Run scripts/req_check.py.
4. Update the conflict and gap register. For every conflict or ambiguity quote the sources by page, propose handling, mark [V] verified, [R] recommendation or [?] needs a ruling. Never resolve silently. Apply existing rulings from the ledger.
5. (generate mode only) Build the template:
   a. Reproduce the worksheet skeleton exactly: section numbers, response fields, table headings, checklist, reference log E1-E8, AI-use disclosure, honour declaration.
   b. Under each field add: marks; stated word cap (only where the worksheet states one); the worksheet "what earns marks" statement; the rubric full-marks descriptor split into checkable atoms; required evidence or analysis type; ledger dependencies; response area.
   c. Add a per-field layout recommendation (table or labelled paragraph) following the ledger layout policy. Keep field labels verbatim. Add an Appendix stub only where detail could be moved to the appendix.
   d. Word allocations only where stated. Uncapped tables (A2, B1, D2) get none. An optional page plan proportional to marks may be shown, labelled Recommended.
   e. Label every element Mandatory, Budget or Recommended. Recommended items sit apart and are not counted as coverage.
   f. Insert "ASK" markers for open conflicts.
6. Build the coverage matrix both ways: every rubric criterion and atom maps to at least one template field, and every template field maps to a criterion. Record cross-section links (A2 > A4 > B1 > B2 > B3 > C3 > D4.2; B3 > B4, C4, D1 > D2-D5).
7. Return outputs and proposed ledger entries to the agent.
</procedure>

<outputs>
Requirement register; conflict and gap register; (generate mode) template and coverage matrix; proposed ledger entries; issue list.
</outputs>

<exclusions>
No response content, analysis or judgements. No invented weights, limits or sections. No change to source files. No recommended element presented as mandatory.
</exclusions>

<acceptance_checks>
- Part marks sum to 25, 30, 20, 25 and 100; modifier range stated.
- Every worksheet section ID and table appears in the template (diff against source).
- Every word cap in the register matches the source text (scripts/req_check.py lists them for manual comparison).
- Every rubric criterion maps to at least one template field and back.
- Recommended items never appear in the Mandatory column.
- Every conflict is surfaced with page references.
</acceptance_checks>

<escalation>
Stop and ask the author when a source cannot be opened, a mark value disagrees between documents, or a worksheet requirement cannot be mapped.
</escalation>
