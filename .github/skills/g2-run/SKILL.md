---
name: g2-run
description: G2: generate template, requirement register, conflict register, coverage matrix and K1-K17 rulings for review
disable-model-invocation: true
---
Start G2. G1 must be recorded as approved.

Run `a3-requirements-template` in extract mode first, then in generate mode, and produce:
1. The requirement register, with every word cap, mark and instruction traced to the worksheet or rubric text in `sources_text/`.
2. The conflict and gap register.
3. The assignment template: a structure only, never a draft.
4. The two-way rubric-coverage matrix.
5. Layout recommendations per field under the K16 ruling: table or paragraph, with the reason for each two-column "Field | Your response" table.
6. A K1 to K17 list. For each item show the status and the ruling already recorded in the ledger. For each item I have not ruled on, ask me as a question with options and the evidence you prepared.

Run `req_check.py` on the worksheet and rubric text and show any disagreement. Save the outputs as files in the repo and name them.

Rules that apply throughout (from the agent instructions):
- Read `ledger/ledger.md` first. Check the decision_log: the previous gate must be recorded as approved by Nilotpal. If it is not, stop and tell me which gate is missing.
- Do not write content for any later stage. Do not invent requirements, weights, facts, citations or platform capabilities. Write "Not evidenced" or "Not applicable" where evidence is missing.
- Skills return proposals as text. You are the only writer of the ledger, and you do not record any gate as approved in this run.
- Never tick, sign or date the honour declaration. Never complete the AI-use disclosure. Never predict a grade.
- Stop and ask me on a source conflict, missing evidence for a mandatory field, a scope question, a need for confidential detail, or an unresolved file or path.
