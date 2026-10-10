# Assignment 3 support: agent and skills (IIMK AIBP Course 3)

Private repository. Deadline: 15 Oct 2026. Status: build complete. G2 (template generation) is not yet approved: no template, no drafts.

## Layout
- `.github/agents/a3-support-agent.agent.md` : orchestrator (stages, gates, ledger protocol, layout policy, boundaries)
- `.github/skills/a3-requirements-template/` : `SKILL.md` + `scripts/req_check.py`
- `.github/skills/a3-prior-work-reuse/` : `SKILL.md` + `scripts/fact_check.py`
- `.github/skills/a3-course-grounded-drafting/` : `SKILL.md`
- `.github/skills/a3-consistency-qa/` : `SKILL.md` + `scripts/qa_checks.py`
- `ledger/ledger.md` : shared Decision & Evidence Ledger. The agent is the only writer.
- `ledger/prior_work_facts.tsv` : S2 output (empty header)
- `drafts/` : one file per section ID, header `<!-- section=ID cap=N -->`, detailed tables inside `<appendix>` tags
- `sources_text/` : text copies of the worksheet, rubric, Assignment 1 and Assignment 2 (read-only)
- `tests/` : G1 acceptance report and synthetic test material

## Use
1. Open the folder in VS Code or PyCharm. In Copilot chat, select the `a3-support-agent` agent. The four skills load from `.github/skills`.
2. Test one skill first (for example ask the agent to run `a3-requirements-template` in extract mode) before relying on all four.
3. Python 3 only, no packages. Run from the repo root.

## Commands
```
python .github/skills/a3-requirements-template/scripts/req_check.py --ws sources_text/IIMK-AIBP-C3-Artefact-ParticipantWorksheet.txt --rb sources_text/IIMK-AIBP-C3-ParticipantRubric.txt
python .github/skills/a3-prior-work-reuse/scripts/fact_check.py --facts ledger/prior_work_facts.tsv --a1 sources_text/Assignment1_AIOpportunityScan_NilotpalChoudhury.txt --a2 sources_text/Assignment2_GenAITechnologyAssessment_NilotpalChoudhury.txt
python .github/skills/a3-consistency-qa/scripts/qa_checks.py --ledger ledger/ledger.md --drafts drafts --sources sources_text/Assignment1_AIOpportunityScan_NilotpalChoudhury.txt sources_text/Assignment2_GenAITechnologyAssessment_NilotpalChoudhury.txt --expect A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2,D3,D4,D5
```
Add `--strip <folder>` to `qa_checks.py` to write tag-free copies for assembly.

## Rules that hold
- Do not commit PDFs, DOCX files, course notes or anything your office policy treats as confidential (`.gitignore` blocks `*.pdf`, `*.docx`, `course_notes/`).
- The agent never ticks the honour declaration or completes the AI-use disclosure. Judgements stay with the author.
- Word caps are binding. Edit sources in `sources_text/` only if a transcription is wrong, and record it in the ledger.
- Notion pages from the earlier build are a mirror. Do not edit both copies.

## Known limits
Scripts are aids; each `SKILL.md` also describes the manual procedure. Platform capabilities (web search, file writing, PDF rendering) in your Copilot setup are unverified: confirm on first use. See `tests/G1_build_acceptance_report.md` for script limits.
