---
name: g4-approve
description: Record G4 approval
disable-model-invocation: true
argument-hint: any changes to Part A
---
G4 approved. Scope and Part A (A1 to A4) are accepted, with these changes: [list them, or "none"].

Rules:
- Read `ledger/ledger.md` first. Confirm that the G4 pack was shown in this conversation or is saved in the repo. If not, stop and tell me.
- Add one row to decision_log: date (today), gate, what was approved, any changes I listed, approver = Nilotpal. Write nothing else as approved.
- Apply the changes I list. Re-open only the sections that the dependency map names for those changes, and say which.
- Then show: the ledger rows you added, the sections re-opened (or "none"), and the exact name of the next run prompt. Do not start the next gate.
Next prompt: `g5-run`.
