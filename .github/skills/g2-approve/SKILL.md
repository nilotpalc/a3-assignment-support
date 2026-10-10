---
name: g2-approve
description: Record G2 approval and rulings
disable-model-invocation: true
argument-hint: any changes to the pack
---
G2 approved. The template, requirement register, conflict register, coverage matrix and the K1 to K17 rulings are accepted, with these changes: [list them, or write "none"].

For any K item I answered in this conversation, record the ruling as an author judgement with its option and date.

Rules:
- Read `ledger/ledger.md` first. Confirm that the G2 pack was shown in this conversation or is saved in the repo. If not, stop and tell me.
- Add one row to decision_log: date (today), gate, what was approved, any changes I listed, approver = Nilotpal. Write nothing else as approved.
- Apply the changes I list. Re-open only the sections that the dependency map names for those changes, and say which.
- Then show: the ledger rows you added, the sections re-opened (or "none"), and the exact name of the next run prompt. Do not start the next gate.
Next prompt: `g3-run`.
