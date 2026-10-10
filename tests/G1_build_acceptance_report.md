# G1 build acceptance report (10 Oct 2026)

<summary>
Build complete for the agent, four skills, ledger and three helper scripts. Light acceptance tests were run on existing documents and synthetic data only. No Assignment 3 content, template or draft exists. Awaiting your G1 decision.
</summary>

<tests_run>
| Skill | Test | Result |
|---|---|---|
| S1 requirements | req_check.py on worksheet and rubric text: criterion marks extracted from three places (worksheet summary table, section headings, rubric) and compared | 18 criteria; Part totals 25/30/20/25; content total 100; no disagreements (D4 appears as D4.1 = 2 and D4.2 = 3 in headings and rubric). 17 stated response budgets listed for manual comparison with the register; all match the worksheet wording |
| S2 reuse | fact_check.py on 24 facts taken from A1 and A2 (numbers, estimates, 2 placeholders) | 0 misses; 2 placeholders flagged as non-reusable. A first run missed one fact because of a line-wrapped hyphen; the matcher was fixed and re-run |
| S2 reuse | planted misses (a wrong account count, a wrong analyst-day figure) | both detected |
| S4 QA | control draft set with a consistent ledger | 0 blocking, 0 warnings |
| S4 QA | seeded set: contradictory rating, changed figure, duplicated rationale, untagged numeric claim, Quick Win on a Low dependency, missing section, placeholder, verbatim reuse (plus cap overrun, undefined evidence ID, classification mismatch, banned term) | all planted errors detected: 10 blocking, 2 warnings; exit code 1 |
Outputs: tests/out_s1_req_check.txt, out_s2_fact_check.txt, out_s4_seeded_error.txt.
</tests_run>

<not_tested_yet>
- S1 generate mode (template and coverage matrix): intentionally not run before G1.
- S2 candidate assessment and reuse proposals: judgement work, first run at Stage 2.
- S3 drafting and the public-evidence protocol: first run on Part A and on A3/C1/C2 research.
- Any platform: the files are portable but I have not verified web search, PDF reading, file writing or Notion access in Notion, GitHub Copilot or other runtimes. Confirm on first use.
</not_tested_yet>

<known_limits_of_the_scripts>
- Untagged-claim check flags only sentences with numbers, percentages or currency and no claim tag; it cannot detect unsupported non-numeric claims. S4 manual review covers those.
- Repetition check uses shared 8-word phrases; paraphrased repetition is not caught.
- Verbatim-reuse check uses shared 10-word phrases against the text files; very common short phrases (for example the organisation label) may need an allow-list.
- Figure check is proximity-based (the ledger value must appear next to the [F:ID] tag).
- Ledger parsing needs one row per line with "|" separators.
- Fact check ignores spaces and hyphens but requires digits and symbols to match exactly. Prefer prose passages over wrapped table cells when choosing exact_text.
- Scripts need Python 3 and text extracted from the PDFs (done here with pdftotext; copies are in sources_text/).
</known_limits_of_the_scripts>

<deviations_from_design>
None material. Additions: --expect (required section list), --strip (tag-free copies for assembly), and a verbatim-overlap check to enforce your K14 ruling.
</deviations_from_design>

<decisions_for_you_at_G1>
1. Approve the build (G1) or list changes.
2. Confirm where you will run the scripts (any machine with Python 3) and which runtime will host the agent and skills.
3. Give the go-ahead to run S1 in generate mode to produce the template, coverage matrix and layout recommendations for your G2 review.
</decisions_for_you_at_G1>
