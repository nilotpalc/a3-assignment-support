---
name: g8-run
description: G8: assemble the document and run the full audit
disable-model-invocation: true
---
Start G8. G7 (or the combined gates under the compressed plan) must be recorded as approved.

1. Assemble the document from the approved drafts: use `--strip` in `qa_checks.py` to write tag-free copies into `build/`. Move all `<appendix>` content into one consolidated optional evidence appendix. Keep main text standalone.
2. Render the PDF. Measure pages and words from the rendered PDF, not from estimates. State the page limit from the worksheet and whether the main body is within it.
3. Run `a3-consistency-qa` in full mode: contradictions, repetition, unsupported claims, caps, formats, section numbers and tables, and the final rubric audit showing where each criterion is evidenced. Do not rewrite, grade or predict marks.
4. Report blocking findings and warnings, and the exact words or figures involved.
5. Ask whether I approve G8.

If you cannot render a PDF in this session, say so and tell me what you need instead of estimating pages.

Rules that apply throughout (from the agent instructions):
- Read `ledger/ledger.md` first. Check the decision_log: the previous gate must be recorded as approved by Nilotpal. If it is not, stop and tell me which gate is missing.
- Do not write content for any later stage. Do not invent requirements, weights, facts, citations or platform capabilities. Write "Not evidenced" or "Not applicable" where evidence is missing.
- Skills return proposals as text. You are the only writer of the ledger, and you do not record any gate as approved in this run.
- Never tick, sign or date the honour declaration. Never complete the AI-use disclosure. Never predict a grade.
- Stop and ask me on a source conflict, missing evidence for a mandatory field, a scope question, a need for confidential detail, or an unresolved file or path.
