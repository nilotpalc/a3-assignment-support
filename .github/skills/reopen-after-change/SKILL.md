---
name: reopen-after-change
description: Re-open sections after an edit that follows an approved gate
disable-model-invocation: true
argument-hint: what changed
---
After a gate, I want to change: ${input:change:What changes and where}.

1. Using the dependency map, list the sections and ledger entries this reopens. Name each one and say why.
2. State which gates would be affected and which approved decisions need my re-approval.
3. Make no edit yet. Ask me to confirm the list. After I confirm, apply the change through `section-draft` for each affected section and record it in the change_log.

Rules that apply throughout (from the agent instructions):
- Read `ledger/ledger.md` first. Check the decision_log: the previous gate must be recorded as approved by Nilotpal. If it is not, stop and tell me which gate is missing.
- Do not write content for any later stage. Do not invent requirements, weights, facts, citations or platform capabilities. Write "Not evidenced" or "Not applicable" where evidence is missing.
- Skills return proposals as text. You are the only writer of the ledger, and you do not record any gate as approved in this run.
- Never tick, sign or date the honour declaration. Never complete the AI-use disclosure. Never predict a grade.
- Stop and ask me on a source conflict, missing evidence for a mandatory field, a scope question, a need for confidential detail, or an unresolved file or path.
