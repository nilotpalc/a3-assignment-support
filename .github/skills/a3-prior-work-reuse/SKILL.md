---
name: a3-prior-work-reuse
description: Build a fact-level ledger of Assignments 1 and 2, assess which opportunities and evidence are relevant to Assignment 3, propose adaptations without copying prose, and list evidence gaps. Use after the requirement register is frozen and before Part A evidence and B1.
---
<purpose>
Make reuse of prior work explicit, accurate and permitted: preserve original facts, separate documented information from proposed extensions, and show what new evidence is needed.
</purpose>

<trigger>
Stage 2. Re-run if a prior assignment changes or if the requirement register changes.
</trigger>

<inputs>
- Assignment1_AIOpportunityScan_NilotpalChoudhury.pdf and Assignment2_GenAITechnologyAssessment_NilotpalChoudhury.pdf (exact filenames; text with section references)
- requirement register (frozen) and ledger (scope, rulings)
</inputs>

<procedure>
1. Extract facts into ledger/prior_work_facts.tsv: id, document (A1/A2), section, exact_text (short exact string copied from the source for verification), status (documented | estimate | placeholder | unfilled), note. Capture every numeric value exactly. Mark unfilled placeholders (for example "[X]%", "[N]") as placeholder and never reuse them.
2. Run scripts/fact_check.py against the source text. Fix every miss.
3. Assess each candidate opportunity and live asset against Assignment 3 fields: relevance (High/Medium/Low) with a one-line reason; applicable section; adaptation needed; evidence gaps. Respect the ledger scope (function Strategy & Analytics within Global Sales & Marketing; sales-related workflows).
4. Label every reuse proposal Documented (as in source), Adapted (state the change) or New proposal. Where the prior document parked or rejected an idea, cite its stated reason; do not reverse it silently.
5. Flag overlaps between candidates to prevent double counting (for example the evidence-pack agent, the proposed CI data product and the existing market-intelligence platform).
6. Re-express Assignment 1 labels under Assignment 3 definitions (for example "Now" is not a Quick Win unless readiness is mostly in place). Do not carry A1 labels, Red/Amber/Green ratings or vendor scores into Assignment 3 as if they were Assignment 3 ratings; they may be cited as evidence.
7. Produce an evidence-gap list by Assignment 3 section (especially Technology, Talent, Process and Culture indicators; Part C comparators; role task data for D2).
8. Write rephrased summaries only; no verbatim blocks. Return proposed ledger entries.
</procedure>

<outputs>
prior_work_facts.tsv; candidate assessment table; reuse proposals per template field; placeholder and unsafe-to-reuse list; evidence-gap list; proposed ledger entries.
</outputs>

<exclusions>
Does not select the portfolio. Adds no new facts. No vendor scoring or vendor evidence from Assignment 2 Part C. No verbatim text blocks. Does not alter facts or rounding.
</exclusions>

<acceptance_checks>
- Every fact has a document and section reference.
- Every numeric value matches the source exactly (scripts/fact_check.py shows zero misses).
- No placeholder is marked reusable.
- Every proposal is labelled documented, adapted or new.
- Every parked or rejected item cites the source's own reason.
</acceptance_checks>

<escalation>
Ask the author when a fact is ambiguous, when two prior documents disagree, or when reuse would need confidential detail.
</escalation>
