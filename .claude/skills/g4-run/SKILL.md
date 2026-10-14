---
name: g4-run
description: "G4: scope and Part A drafting loop, one section at a time"
disable-model-invocation: true
---
Start G4. The previous gate must be recorded as approved.

Scope is section A1: confirm the function and workflow scope with me before anything else (K11/K17 rulings are in the ledger). Sections: A1, A2, A3, A4. Public-evidence research for A3 may start early using the research protocol in `a3-course-grounded-drafting`.

For each section in dependency order, do the loop in `section-draft`: judgement capture first, then draft, then QA in delta mode, then my edit and approval, then the ledger update. Use the section prompt for each section; do not batch sections I have not approved.

At the end of the part, run `a3-consistency-qa` in delta mode across all drafts in scope and Part A and show: findings, word counts against caps, and the rubric criteria evidenced so far. Then ask whether I approve G4.

Rules that apply throughout (from the agent instructions):
- Read `ledger/ledger.md` first. Check the decision_log: the previous gate must be recorded as approved by Nilotpal. If it is not, stop and tell me which gate is missing.
- Do not write content for any later stage. Do not invent requirements, weights, facts, citations or platform capabilities. Write "Not evidenced" or "Not applicable" where evidence is missing.
- Skills return proposals as text. You are the only writer of the ledger, and you do not record any gate as approved in this run.
- Never tick, sign or date the honour declaration. Never complete the AI-use disclosure. Never predict a grade.
- Stop and ask me on a source conflict, missing evidence for a mandatory field, a scope question, a need for confidential detail, or an unresolved file or path.
