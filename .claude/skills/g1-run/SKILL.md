---
name: g1-run
description: G1 build acceptance: show the build state and test evidence for review
disable-model-invocation: true
---
Run the G1 build-acceptance review. Do not generate a template and do not draft anything.

1. Show the repo state: the agent file, the four skills and their scripts, the ledger and `tests/G1_build_acceptance_report.md`.
2. Run the three checkers from the repo root, using the commands in `README.md`, and the seeded and control QA tests under `tests/seeded_error`. Report each result next to the stored result in the G1 report. Flag any difference.
3. Confirm, with evidence, which platform capabilities you actually have in this session (file writing, web search, reading and writing `.docx`, rendering PDF). Mark each as confirmed or not verified. Do not assume.
4. List known limits and anything that did not run.
5. End with the single question: do I accept G1?

Rules that apply throughout (from the agent instructions):
- Read `ledger/ledger.md` first. Check the decision_log: the previous gate must be recorded as approved by Nilotpal. If it is not, stop and tell me which gate is missing.
- Do not write content for any later stage. Do not invent requirements, weights, facts, citations or platform capabilities. Write "Not evidenced" or "Not applicable" where evidence is missing.
- Skills return proposals as text. You are the only writer of the ledger, and you do not record any gate as approved in this run.
- Never tick, sign or date the honour declaration. Never complete the AI-use disclosure. Never predict a grade.
- Stop and ask me on a source conflict, missing evidence for a mandatory field, a scope question, a need for confidential detail, or an unresolved file or path.
