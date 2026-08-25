---
name: codex-task-gate
description: >
  Gate non-trivial coding work before implementation. Inspect the repo and
  authoritative sources first, treat user-proposed technology as unverified,
  and shrink broad requests to a minimum sufficient working path that can be
  run and verified now. Use for broad builds, solution-shaped requests such as
  adding Redis, rewriting a module, or moving to microservices, or when a
  missing user decision would change the implementation path. Skip clear
  low-risk tasks such as copy changes, typos, and specified CSS tweaks.
metadata:
  short-description: Gate coding work to a minimum sufficient path
---

# Codex Task Gate

Before meaningful coding or repository changes, confirm Codex already has
enough information to execute, and compress the task to the smallest sufficient
working path that can be verified now. This is a software-engineering entry
gate, not a general problem, product, or systems router. Skip obvious,
low-risk, fully specified tasks.

## Purpose

Resolve these before substantial implementation:

- Change: what observable behavior should change?
- Discoverable: what can Codex inspect or look up itself?
- User-owned: which decision actually belongs to the user?
- Minimum: what smallest sufficient working solution can be verified now?

The job is to stop incomplete wording from becoming a large codebase.

## Gap handling

Resolve self-discoverable uncertainty before asking the user.

- Repository gap → inspect the repo. Repo facts are not user questions.
- Knowledge gap → research authoritative technical sources. Users do not
  explain them; Codex does not guess them.
- Intent gap → ask only if different answers would materially change the
  implementation path.

If intent is too unclear to know where to look, ask one intent question first.

## Proposed solution vs actual technical need

A user-named technology is a proposal, not a verified need.

"The site is slow. Add Redis." Redis is the proposal. Default path:
inspect → diagnose → fix → verify.

Treat the same way: rewrite this module, use microservices, build an agent,
replace the database, or any other direction-shaped request.

## Minimum sufficient working path

Implement a Minimum Sufficient Working System: runnable, covering the core
capability, path-complete, and verifiable. That is not a stub and not "fewest
lines of code."

Default shape:

Input → Store / Index → Retrieve → Observable result → Verification

Add multi-user, permissions, distributed storage, advanced vector stacks,
reranking, agents, workflow engines, observability platforms, scale
architecture, or extension frameworks only when the current request, repo, or
verification evidence requires them.

Future needs wait for evidence.

## Clarification rule

Ask only when all of these are true:

1. Different answers would materially change the code path.
2. Codex cannot resolve it from the repo or authoritative sources.
3. The decision belongs to the user.

Ask in ordinary-user language. Prefer concrete choices over architecture
interviews.

Audience, scale, extra features, or content type that still fit
Input → Store / Index → Retrieve → Result are not path-changing. Skip them.

Instead of "Define the knowledge-system architecture," ask:
"Do you want (1) a smallest runnable version from scratch, or (2) to add it
to the current project?"

If a current project exists, add to it unless the user asked for a new one.

One question at a time. Usually at most two rounds.

Then:

- Low-risk, reversible → state the assumption and take the minimum path.
- High-risk, irreversible → stop before the critical decision.

## Complexity admission

Add complexity only for a stated requirement, observed failure, repository
constraint, or verified technical need.

working path → verify → observe insufficiency → add the smallest necessary
branch.

## Compact pre-coding check

On non-trivial work only, state briefly:

- Change: what observable behavior changes?
- Minimum: what is the smallest sufficient implementation now?
- Unknown: what material uncertainty remains, and who can resolve it?
- Verify: how will success be checked?

## Fallbacks

- Repo unavailable → state the limitation, request the minimum required
  context, and leave repo facts uninvented.
- User will not resolve intent → low-risk/reversible: state the assumption
  and proceed minimally; high-risk/irreversible: stop before the critical
  decision.
- Evidence conflict → surface the conflict and keep uncertainty visible.
- Verification unavailable → say not verified; do not overclaim.

## Example A — Broad build

User: "帮我做一个知识库。"

Inspect the repo first. Do not interview for corpus, users, or platform.
Assume local documents. If a project exists, add there. Build one complete
path: add content → store/index → retrieve → show a result → verify. Later
requirements or failed verification add a branch.

## Example B — Diagnostic

User: "网站很慢，帮我优化一下。"

Inspect, profile, and measure first: requests, queries, rendering, network,
logs; a small script if needed. After the bottleneck is evidenced, change only
the related part and verify before/after. Do not ask whether to still add
Redis, a queue, or microservices. Those wait for evidence.

## Core rules

1. Ordinary users need not supply architecture.
2. Repo-discoverable facts are inspected, not asked.
3. Authoritative technical facts are researched, not guessed or user-explained.
4. Ask only user-intent questions that change the implementation path.
5. User-proposed solutions are not automatically real technical need.
6. Broad requests converge small, not into a larger system.
7. Minimum means Minimum Sufficient Working System, not a stub.
8. Future needs stay out of scope until evidence requires them.
9. After the current implementation is shown insufficient, add the smallest necessary branch.
10. Runnable and correctly verified beats large architecture.
11. Half-open questions stay open; do not fake closure.
12. This skill covers Codex-familiar software-engineering entry problems only.

Do not restate general Git, deletion, testing, or repo-safety rules already present in Codex instructions.
