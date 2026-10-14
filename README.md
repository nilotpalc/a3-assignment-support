# Assignment 3 support: agent and skills (IIMK AIBP Course 3)

Private repository. Deadline: 15 Oct 2026. Status: build complete. G2 (template generation) is not yet approved: no template, no drafts.

## Layout
- `.github/agents/a3-support-agent.agent.md` : orchestrator (stages, gates, ledger protocol, layout policy, boundaries) for GitHub Copilot. A copy lives at `.claude/agents/a3-support-agent.md` for Claude Code; keep the two identical apart from the file name.
- `.claude/skills/a3-requirements-template/` : `SKILL.md` + `scripts/req_check.py`
- `.claude/skills/a3-prior-work-reuse/` : `SKILL.md` + `scripts/fact_check.py`
- `.claude/skills/a3-course-grounded-drafting/` : `SKILL.md`
- `.claude/skills/a3-consistency-qa/` : `SKILL.md` + `scripts/qa_checks.py`
- `.claude/skills/<gate or command name>/` : 22 slash-command skills (`g1-run` to `g8-approve`, `g9-prep`, `section-draft`, `delta-qa`, `reopen-after-change`, `compress-gates`, `status`), each a single `SKILL.md`. Migrated from the former `.github/prompts/` files, which no longer exist
- `ledger/ledger.md` : shared Decision & Evidence Ledger. The agent is the only writer.
- `ledger/ledger.md` also holds `<k_register>`: the K1 to K17 conflict and ambiguity definitions from the design proposal. Rulings go in `decision_log`
- `design/` : copy of the design proposal (background reference only)
- `ledger/prior_work_facts.tsv` : S2 output (empty header)
- `drafts/` : one file per section ID, header `<!-- section=ID cap=N -->`, detailed tables inside `<appendix>` tags
- `sources_text/` : text copies of the worksheet, rubric, Assignment 1 and Assignment 2 (read-only)
- `tests/` : G1 acceptance report and synthetic test material

## Use
1. Open the folder in VS Code or PyCharm. In Copilot chat, select the `a3-support-agent` agent in the agent dropdown **before** running any slash command. The skills load from `.claude/skills` (VS Code Copilot, the Copilot app and Claude Code all read this folder).
2. Test one skill first (for example ask the agent to run `a3-requirements-template` in extract mode) before relying on all four.
3. Python 3.10 or newer; the scripts currently use only the standard library. Run from the repo root.

## Python environment (uv)
Run `uv sync` to create `.venv` and sync dependencies from `pyproject.toml`.
The project sets `[tool.uv] package = false`, so uv manages dependencies without
building or installing this repository as a Python package.

Use `uv run python` in place of `python` in the commands below, for example:
```
uv run python .claude/skills/a3-requirements-template/scripts/req_check.py --help
```
Add future runtime dependencies with `uv add <package>` or development tools with
`uv add --dev <package>`. Commit the resulting `pyproject.toml` and `uv.lock` changes
so the environment stays reproducible.

## Commands
```
python .claude/skills/a3-requirements-template/scripts/req_check.py --ws sources_text/IIMK-AIBP-C3-Artefact-ParticipantWorksheet.txt --rb sources_text/IIMK-AIBP-C3-ParticipantRubric.txt
python .claude/skills/a3-prior-work-reuse/scripts/fact_check.py --facts ledger/prior_work_facts.tsv --a1 sources_text/Assignment1_AIOpportunityScan_NilotpalChoudhury.txt --a2 sources_text/Assignment2_GenAITechnologyAssessment_NilotpalChoudhury.txt
python .claude/skills/a3-consistency-qa/scripts/qa_checks.py --ledger ledger/ledger.md --drafts drafts --sources sources_text/Assignment1_AIOpportunityScan_NilotpalChoudhury.txt sources_text/Assignment2_GenAITechnologyAssessment_NilotpalChoudhury.txt --expect A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2,D3,D4,D5
```
Add `--strip <folder>` to `qa_checks.py` to write tag-free copies for assembly.

## Rules that hold
- All project files sync to the private repository, including `build/`, `design/`, PDFs, DOCX files and course notes (`.gitignore` only excludes caches and the virtual environment). Do not add anything your office policy treats as confidential.
- The agent never ticks the honour declaration or completes the AI-use disclosure. Judgements stay with the author.
- Word caps are binding. Edit sources in `sources_text/` only if a transcription is wrong, and record it in the ledger.
- Notion pages from the earlier build are a mirror. Do not edit both copies.

## Known limits
Scripts are aids; each `SKILL.md` also describes the manual procedure. Platform capabilities (web search, file writing, PDF rendering) in your Copilot setup are unverified: confirm on first use. See `tests/G1_build_acceptance_report.md` for script limits.

## Slash commands (`.claude/skills/`)
VS Code now treats `.prompt.md` files as legacy, so the former prompts were migrated to skills. Each one is a folder with a `SKILL.md` and runs from Copilot chat by typing `/` and the name (keep typing, for example `/g1`, to filter the list). Each gate has a `run` command that produces the pack for review and an `approve` command that records your written approval. Edit the bracketed text in an `approve` command before sending it.

The four `a3-*` skills do the work and load automatically. The 22 commands below set `disable-model-invocation: true`, so only you can start them from the `/` menu and the agent cannot run a gate on its own. If the agent says it cannot load the named skill, it is following the instructions already in your message, and that is expected.

| Command | Use |
|---|---|
| `g1-run`, `g1-approve` | Build acceptance |
| `g2-run`, `g2-approve` | Template, requirement register, coverage matrix, K1 to K17 rulings |
| `g3-run`, `g3-approve` | Prior-work fact ledger and shortlist |
| `g4-run`, `g4-approve` | Scope and Part A |
| `g5-run`, `g5-approve` | Part B |
| `g6-run`, `g6-approve` | Part C |
| `g7-run`, `g7-approve` | Part D |
| `g8-run`, `g8-approve` | Assembly and full audit |
| `g9-prep` | Submission checklist and AI-use fact sheet (G9 itself is yours alone) |
| `section-draft` | One section: judgement capture, draft, delta QA, ledger update (asks for the section ID) |
| `delta-qa` | Delta QA after any edit |
| `reopen-after-change` | Lists what an edit reopens after a gate; changes nothing until you confirm |
| `compress-gates` | Records consent to combine G4+G5 and/or G6+G7 for the deadline |
| `status` | Read-only status: gates, word counts, next prompt |

Migration dropped the old `agent: a3-support-agent` line, so a command runs under whichever agent is selected. Select `a3-support-agent` first. Skill front matter uses `name`, `description`, `disable-model-invocation` and `argument-hint`. Quote every value that contains a colon, or the file fails to parse and is silently skipped.
Outputs the agent writes (ledger entries, drafts, `build/` files) are saved in the repo; chat replies such as review packs and `status` output are not.

## Ledger view
`ledger/ledger.md` stays pipe-delimited so the scripts can parse it, which VS Code's Markdown preview does not draw as tables. For a readable copy run `python ledger/render_ledger.py` and open `build/ledger_view.md` in preview. The view is generated and read-only: never edit it, and the agent and QA scripts do not read it.
