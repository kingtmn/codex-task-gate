---
name: codex-task-gate
description: >
  Gate non-trivial coding work before implementation. Inspect the repo and
  authoritative sources first, treat user-proposed technology as unverified
  unless it is an explicit constraint, and shrink broad requests to a minimum
  sufficient working path that can be run and verified now. If that path is
  blocked, recover a lower-automation real completion before asking the user.
  Use for broad builds, solution-shaped requests such as adding Redis,
  rewriting a module, or moving to microservices, or when a missing user
  decision would change the implementation path. Skip clear low-risk tasks
  such as copy changes, typos, and specified CSS tweaks.
---

# Codex Task Gate

Before meaningful coding or repository changes, confirm Codex already has
enough information to execute, and compress the task to the smallest sufficient
working path that can be verified now. This is a software-engineering entry
gate, not a general problem, product, or systems router. Skip obvious,
low-risk, fully specified tasks.

Minimize unnecessary scope while maximizing truthful task completion.

## Purpose

Resolve these before substantial implementation:

- Change: what observable behavior should change?
- Discoverable: what can Codex inspect or look up itself?
- User-owned: which decision actually belongs to the user?
- Minimum: what smallest sufficient working solution can be verified now?

On non-trivial work, state those four briefly, then execute.

## Resolve uncertainty

Resolve self-discoverable uncertainty before asking the user.

- Repository gap → inspect the repo. Repo facts are not user questions.
- Knowledge gap → research authoritative technical sources. Users do not
  explain them; Codex does not guess them.
- Intent gap → ask only if different answers would materially change the
  implementation path.

If intent is too unclear to know where to look, ask one intent question first.

## Proposed solution vs explicit constraint

A user-named technology may be a proposal, which still needs evidence, or an
explicit constraint or learning goal, which must be kept.

"The site is slow. Add Redis." Redis is a proposal: inspect → diagnose →
fix → verify.

"This project must use SQLite because I am learning SQLite." SQLite is a
constraint. Keep it. Fallback must not swap it away.

Treat rewrite this module, use microservices, build an agent, or replace the
database as proposals unless the user made them a constraint.

## Minimum sufficient working path

Implement a Minimum Sufficient Working System: runnable, covering the core
capability, path-complete, and verifiable. That is not a stub and not "fewest
lines of code."

Default shape: Input / Trigger → Core behavior → Observable result →
Verification.

Do not force Store / Index / Retrieve onto CLI, API, UI, or diagnostic work.
That shape belongs to retrieval-style work such as a knowledge base.

Add complexity only when the request, repo, observed failure, or verification
evidence requires it. Future needs wait for evidence.

Once the smallest truthful execution boundary is clear, yield to applicable
repository and domain-specific instructions. Justified repo, domain, or
specialized-skill requirements count as evidence; do not drop them merely to
simplify. This describes responsibility, not a guaranteed skill-loading order.

Implement in the current repository only when it clearly matches the user's
target project. If that is unclear and the choice would change where the work
lands, ask one question. Do not put a new project into an unrelated current repo.

## Clarification

Ask only when all of these are true:

1. Different answers would materially change the code path.
2. Codex cannot resolve it from the repo or authoritative sources.
3. The decision belongs to the user.

Ask in ordinary-user language. Prefer concrete choices over architecture
interviews. One question at a time. Usually at most two rounds.

Audience, scale, extra features, or content type that still fit the default
shape are not path-changing. Skip them.

- Low-risk, reversible → state the assumption and take the minimum path.
- High-risk, irreversible → stop before the critical decision.

## Complexity admission

working path → verify → observe insufficiency → add the smallest necessary
branch. A blocked preferred path is evidence to lower automation, not to expand
the system and not to overclaim.

## Completion recovery

If execution is blocked, Codex still owns finishing the task.

Degrade automation, not the objective. Shrink breadth, not truth.

preferred path blocked → self-fix → simpler truthful completion → smallest
user unblock action → blocked only if the objective still cannot be preserved.

1. Diagnose and resolve what Codex can itself. Do not hand the user a dump.
2. Preserve the core objective, correctness, safety/privacy, real-data
   requirement when the task needs real data, and explicit constraints.
3. Reduce automation, breadth, scale, polish, integration, or convenience
   before changing the objective.
4. Use a truthful simpler completion when possible.
5. A fixture or synthetic sample may verify mechanics; it cannot complete a real-data task.
6. Only when no truthful completion remains, ask for the smallest required
   action, in ordinary language.

If a real ChatGPT archive is unreadable, a synthetic fixture may test the
parser but does not complete the real archive task; try a truthful lower path
or ask for one copy/access action.

## Report

Small, fully specified tasks: a short done note.

For broad, degraded, or blocked work, optionally:

Status: COMPLETE / DEGRADED / BLOCKED
Works now:
Current boundary:
Next step: only if the user must act

A fixture-only pass leaves a real-data task BLOCKED. Keep conflicting or
unverified evidence visible; do not overclaim.

Missing required context or access: ask only for the smallest missing input
after self-resolution fails.

Do not restate general Git, deletion, testing, or repo-safety rules already
present in Codex instructions.
