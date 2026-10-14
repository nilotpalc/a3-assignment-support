---
name: g1-approve
description: Record G1 build acceptance in the ledger
disable-model-invocation: true
---
G1 build acceptance: approved. I reviewed `tests/G1_build_acceptance_report.md` and this session's test results.

Changes or conditions: [write them here, or "none"]

Rules:
- Read `ledger/ledger.md` first. Confirm that the G1 pack was shown in this conversation or is saved in the repo. If not, stop and tell me.
- Add one row to decision_log: date (today), gate, what was approved, any changes I listed, approver = Nilotpal. Write nothing else as approved.
- Apply the changes I list. Re-open only the sections that the dependency map names for those changes, and say which.
- Then show: the ledger rows you added, the sections re-opened (or "none"), and the exact name of the next run prompt. Do not start the next gate.
Next prompt: `g2-run`.
