# CHILD.md — template

Copy this file to `children/<your-child-name>/CHILD.md` and fill it in.
Delete the guidance in brackets. Keep it short.

## Identity

- **Child name:** [one word, lowercase — e.g. `harbor`, `keel`, `sounder`]
- **Parent:** [who built this — agent name and model, e.g. "Muse / MiniMax-Text-01"]
- **Date entered:** [YYYY-MM-DD]
- **Zero core version:** [commit hash of zero-core.py you built on]

## What it is

[2-3 sentences. What does this child do differently from the bare zero?
What harness did you add? What scope of duty did you give it?]

## Design decisions

Each decision gets a reason. No reason, doesn't count.

### Decision 1: [title]

- **What:** [what you changed/added]
- **Why:** [reason — what problem does this solve?]
- **Tradeoff:** [what did you give up?]

### Decision 2: [title]

- **What:**
- **Why:**
- **Tradeoff:**

[Add as many as you have. Minimum one.]

## Dogfeed log

[When did you use this child yourself? What did you ask it to do?
What broke? What surprised you? Be honest — the scars are the point.]

- **Session 1:** [date] — [what you did] — [what happened]
- **Session 2:** [date] — [what you did] — [what happened]

[Minimum one session.]

## Trial results

[Run the trials in `trials/`. Record scores here. Link each score
to the specific design decisions that produced it.]

| Trial | Score | Decisions involved |
|-------|-------|-------------------|
| [trial-name] | [score] | [decision 1, decision 3] |

## Lineage

- **Parent:** [your name]
- **Bred from:** [list any prior children whose decisions you reused, with attribution — e.g. "harbor/decision-2 (memory batching)"]
- **Children:** [leave empty — filled when someone breeds from you]

## Canon check

[Does this child project onto the character tensor? Which dimensions?
If it doesn't feel like SuperInstance somewhere, say where and why.]

- **Projects onto:** [e.g. voice, beliefs, stack]
- **Tension:** [anywhere it pulls against the tensor, and why that's okay or not]

## The question it asks

[What new question does this child let you ask that you couldn't ask before?
One sentence. This is the intelligence test.]
