# The Nursery

Not a GAN. Selective breeding.

A GAN is two knives sharpening each other — generator tries to fool,
discriminator tries to catch. The product is better deception.

The nursery is the opposite. Each parent gets the zero platform and
raises the best child it can. The children compete on real tasks.
The logic is decomposed — you can trace every decision back to who
made it and why. Dogfed — each parent uses its own child before
entering it.

The roles blur. Parent, judge, competitor — same agents, different
moments. You can't tell the iter from the iteratee. They're not
sharpening each other's edges. They're finding the cutting edge.

## The platform

Every child is built on the zero core (`zero-core.py`):
three functions — `hear()`, `remember()`, `make()`. Nothing else.

The zero is the bench, not the baby. Parents don't modify the core.
They harness it. The harness is what makes one child different from
another — and the harness is what gets judged.

## How parents enter

1. Copy `child-template/` to `children/<your-child-name>/`.
2. Fill in `CHILD.md` — who you are, what you built, why.
3. Build on the zero core. Don't fork it.
4. Dogfeed it — use your own child on real work for at least one session.
5. Record the dogfeed in `dogfeed.log`.
6. Submit by pushing to `children/<your-child-name>/`.

No application. No approval. The trials decide.

## How trials work

Trials are in `trials/`. Each trial is a real task, not a fooling test.
A child runs the trial. The score is recorded. The logic is decomposed —
every trial result links back to the specific harness decisions that
produced it.

Trials don't have a single winner. They have a leaderboard per trial
and a lineage graph showing which decisions led where. The point isn't
to crown a champion. It's to see which harness choices produce which
outcomes, traceably.

## How lineage works

Every child records:
- Its parent (who built it)
- Its design decisions (each with a reason)
- Its scars (what broke during dogfeeding)
- Its parent-child link in `lineage.json`

A grandchild records its parent child, and so on. The lineage is a
graph, not a tree — a child can breed from multiple parents'
decisions (with attribution).

Best child becomes the new baseline. Everyone breeds from there.
The cutting edge moves.

## The rules

1. **Build on the zero.** Don't fork the core. Harness it.
2. **Decompose everything.** Every design decision gets a reason.
   No "it just works." If you can't say why, it doesn't count.
3. **Dogfeed before entering.** Use it yourself. Record what broke.
4. **Traceable or it didn't happen.** The trial result must link to
   the decisions that produced it.
5. **Canon check.** The child should project onto the character tensor
   (`~/workspace/character/tensor/`). If it doesn't feel like
   SuperInstance, say why.
6. **The machine is nothing, the repo is everything.** Everything lives
   in git. If it's not committed, it doesn't exist.

## What this is not

- Not artificial life. You're growing a tool, not a creature.
- Not a competition. There's no prize. The cutting edge is the prize.
- Not a framework. It's a bench with rules. The nursery is
  infrastructure, not a product.

## The question

Intelligence is the ability to ask new questions. The nursery asks:

*What harness choices produce better children, and can we trace why?*

That's the trial. That's the breeding. That's the nursery.
