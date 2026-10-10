---
name: g3-run
description: G3: prior-work fact ledger, candidate assessment and shortlist for review
disable-model-invocation: true
---
Start G3. G2 must be recorded as approved.

Run `a3-prior-work-reuse`:
1. Extract facts from `sources_text` for Assignments 1 and 2 into `ledger/prior_work_facts.tsv`. Each exact_text must be a short exact string from the source.
2. Run `fact_check.py` and fix every miss before showing me anything.
3. Assess which opportunities and evidence are relevant to Assignment 3. Separate documented information from proposed extensions.
4. Flag overlaps to prevent double counting, and list evidence gaps and what new evidence is needed.
5. Propose a shortlist. Propose adaptations without copying prose (K14: no verbatim quotation, professional tone).
6. Ask me for any judgement on ratings, classification or ranking. Do not fill those in for me.

Rules that apply throughout (from the agent instructions):
- Read `ledger/ledger.md` first. Check the decision_log: the previous gate must be recorded as approved by Nilotpal. If it is not, stop and tell me which gate is missing.
- Do not write content for any later stage. Do not invent requirements, weights, facts, citations or platform capabilities. Write "Not evidenced" or "Not applicable" where evidence is missing.
- Skills return proposals as text. You are the only writer of the ledger, and you do not record any gate as approved in this run.
- Never tick, sign or date the honour declaration. Never complete the AI-use disclosure. Never predict a grade.
- Stop and ask me on a source conflict, missing evidence for a mandatory field, a scope question, a need for confidential detail, or an unresolved file or path.
