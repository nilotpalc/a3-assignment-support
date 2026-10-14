---
name: section-draft
description: Draft one section: judgement capture, draft, delta QA, ledger update
disable-model-invocation: true
argument-hint: "section ID, e.g. B2"
---
Work on section ${input:section:Section ID, e.g. A3} only.

1. Check the gate for its part is open (see the ledger decision_log). If the section's inputs from earlier sections have changed since I last approved them, say so and stop.
2. Judgement capture: if the section contains a rating, classification, rank, position, role choice or framework choice, list each one with the options and the evidence the skills prepared, and ask me. Do not draft until I answer. Record each answer as "author judgement".
3. Run `a3-course-grounded-drafting` for this section. Write to `drafts/${input:section:Section ID}.md`. First line: `<!-- section=${input:section:Section ID} cap=N -->` with N from the worksheet cap. Tag every claim as the skill defines. Put detailed tables in `<appendix>` tags. Stay within the word cap; the cap is binding.
4. Run `a3-consistency-qa` in delta mode on this section and everything that depends on it. Show findings.
5. Show me the draft and the findings. I edit and approve. After my approval, update the ledger registers (maturity, portfolio, figures, assumptions, evidence, word_counts, change_log) and resolve ID collisions before writing.

Rules that apply throughout (from the agent instructions):
- Read `ledger/ledger.md` first. Check the decision_log: the previous gate must be recorded as approved by Nilotpal. If it is not, stop and tell me which gate is missing.
- Do not write content for any later stage. Do not invent requirements, weights, facts, citations or platform capabilities. Write "Not evidenced" or "Not applicable" where evidence is missing.
- Skills return proposals as text. You are the only writer of the ledger, and you do not record any gate as approved in this run.
- Never tick, sign or date the honour declaration. Never complete the AI-use disclosure. Never predict a grade.
- Stop and ask me on a source conflict, missing evidence for a mandatory field, a scope question, a need for confidential detail, or an unresolved file or path.
