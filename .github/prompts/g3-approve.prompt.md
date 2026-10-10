---
description: Record G3 approval
agent: a3-support-agent
argument-hint: any changes to the shortlist
---
G3 approved. The prior-work fact ledger and the shortlist are accepted, with these changes: [list them, or "none"].

Rules:
- Read `ledger/ledger.md` first. Confirm that the G3 pack was shown in this conversation or is saved in the repo. If not, stop and tell me.
- Add one row to decision_log: date (today), gate, what was approved, any changes I listed, approver = Nilotpal. Write nothing else as approved.
- Apply the changes I list. Re-open only the sections that the dependency map names for those changes, and say which.
- Then show: the ledger rows you added, the sections re-opened (or "none"), and the exact name of the next run prompt. Do not start the next gate.
Next prompt: `g4-run`.
