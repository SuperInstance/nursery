# Trials

Trials are real tasks, not fooling tests. A child runs the trial.
The score is recorded. The score links back to the design decisions
that produced it.

## Trial format

Each trial is a directory with a `TRIAL.md`:

```
trials/<trial-name>/
  TRIAL.md    # what the trial is, how to run it, how to score it
  input/      # input files (specs, prompts, etc.)
```

## How to run a trial

1. Read `TRIAL.md`.
2. Point your child at the input.
3. Record the output and score in your `CHILD.md`.
4. Link the score to your design decisions.

## How scoring works

Scores are not rankings. They're data points. The same child can
score differently on different trials — that's the point. The
leaderboard per trial shows which harness choices work where.

"What is better" depends on the trial. Each `TRIAL.md` defines its
own "better." The nursery doesn't define a universal score.

## The rule

If you can't trace the score back to a specific design decision,
the score doesn't count. "It just scored well" is not a result.
