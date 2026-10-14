---
name: delta-qa
description: Run delta QA after any edit
disable-model-invocation: true
---
I changed ${input:what:What changed, e.g. B1 ratings or a figure}. Run `a3-consistency-qa` in delta mode.

1. Use the dependency map to list every section and ledger location affected. Show the list before you check anything.
2. Run `qa_checks.py` with the ledger and `drafts/`, plus the Assignment 1 and 2 text as sources for the verbatim check, and `--expect` for the sections that exist.
3. Report blocking findings and warnings with the exact text. Do not rewrite anything. Propose changes as text for me to approve.

Rules that apply throughout (from the agent instructions):
- Read `ledger/ledger.md` first. Check the decision_log: the previous gate must be recorded as approved by Nilotpal. If it is not, stop and tell me which gate is missing.
- Do not write content for any later stage. Do not invent requirements, weights, facts, citations or platform capabilities. Write "Not evidenced" or "Not applicable" where evidence is missing.
- Skills return proposals as text. You are the only writer of the ledger, and you do not record any gate as approved in this run.
- Never tick, sign or date the honour declaration. Never complete the AI-use disclosure. Never predict a grade.
- Stop and ask me on a source conflict, missing evidence for a mandatory field, a scope question, a need for confidential detail, or an unresolved file or path.
