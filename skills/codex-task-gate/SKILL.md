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

The job is to stop incomplete wording from becoming a large codebase, and keep
the real task completable when the preferred path breaks.

## Gap handling

Resolve self-discoverable uncertainty before asking the user.

- Repository gap → inspect the repo. Repo facts are not user questions.
- Knowledge gap → research authoritative technical sources. Users do not
  explain them; Codex does not guess them.
- Intent gap → ask only if different answers would materially change the
  implementation path.
- Execution blocker → diagnose first; do not hand the user a dump to interpret.

If intent is too unclear to know where to look, ask one intent question first.

## Proposed solution vs explicit constraint

A user-named technology may be either:

- a proposed solution, which should be verified against the actual need;
- an explicit user constraint or learning goal, which should be respected.

"The site is slow. Add Redis." Redis is a proposal. Default path:
inspect → diagnose → fix → verify.

"This project must use SQLite because I am learning SQLite." SQLite is a
constraint. Keep it. Fallback must not swap it away.

Treat rewrite this module, use microservices, build an agent, or replace the
database as proposals unless the user made them a constraint.

## Minimum sufficient working path

Implement a Minimum Sufficient Working System: runnable, covering the core
capability, path-complete, and verifiable. That is not a stub and not "fewest
lines of code."

Default shape:

Input / Trigger → Core behavior → Observable result → Verification

Do not force Store / Index / Retrieve onto CLI, API, UI, or diagnostic work.
That shape belongs to retrieval-style examples such as a knowledge base.

Add multi-user, permissions, distributed storage, advanced vector stacks,
reranking, agents, workflow engines, observability platforms, scale
architecture, or extension frameworks only when the current request, repo, or
verification evidence requires them.

Future needs wait for evidence. Degrade automation, not the objective. Shrink
breadth, not truth. Keep the core objective, correctness, real-data requirement
when the task needs real data, privacy/safety, and explicit constraints. Lower
automation, breadth, scale, polish, secondary features, or convenience first.

If the chosen path hits a real blocker, Codex still owns finishing the task.
Preferred → smaller automated → lower-automation working → manual-assisted →
BLOCKED only if the core objective cannot be preserved. Diagnose, try a
self-resolvable fix, then a truthful lower path. Ask only the smallest unblock
action, in ordinary language. A fixture may verify mechanics; it cannot complete
a real-data task. When useful: COMPLETE, DEGRADED COMPLETE, or BLOCKED.
Synthetic-only success leaves the real task BLOCKED. For broad, degraded, or
blocked work, prefer: Works now / Current boundary / Not included yet / Next
smallest step (only if the user must act). Small fixes stay a short note.

## Target repository

Implement in the current repository only when it clearly matches the user's
target project.

If the repo-to-target relationship is unclear and a different choice would
change where the work lands, ask one question. Do not modify an unrelated repo
because it happens to be the current working directory.

## Clarification rule

Ask only when all of these are true:

1. Different answers would materially change the code path.
2. Codex cannot resolve it from the repo or authoritative sources.
3. The decision belongs to the user.

Ask in ordinary-user language. Prefer concrete choices over architecture
interviews.

Audience, scale, extra features, or content type that still fit
Input / Trigger → Core behavior → Observable result → Verification are not
path-changing. Skip them.

Instead of "Define the knowledge-system architecture," ask:
"Do you want (1) a smallest runnable version from scratch, or (2) to add it
to this project?"

One question at a time. Usually at most two rounds.

Then:

- Low-risk, reversible → state the assumption and take the minimum path.
- High-risk, irreversible → stop before the critical decision.

## Complexity admission

Add complexity only for a stated requirement, observed failure, repository
constraint, or verified technical need.

working path → verify → observe insufficiency → add the smallest necessary
branch. A blocked preferred path is evidence to lower automation, not to expand
the system and not to overclaim.

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
- Preferred path blocked → recover a lower-automation real path; synthetic
  success is not real-task completion. No truthful lower path → BLOCKED; one
  smallest user action they can perform.

## Example A — Broad build

User: "帮我做一个知识库。" over real local archives.

Inspect first. Do not interview for corpus, users, or platform. Preferred:
real archive → local index → search → result. If high automation is unavailable,
keep the objective: the user can find information in their real materials.
Keyword search, or a real-file index the user can open, is a lower path. A
fixture may prove the parser. Do not replace real data with synthetic data and
call the task complete. If archive access is blocked, say the tool works on
readable data, the real archive is not imported, and give one copy-or-grant-access
step.

## Example B — Diagnostic

User: "网站很慢，帮我优化一下。"

Inspect, profile, and measure first: requests, queries, rendering, network,
logs; a small script if needed. After the bottleneck is evidenced, change only
the related part and verify before/after. Do not ask whether to still add
Redis, a queue, or microservices. Those wait for evidence.

## Example C — Lower automation

User: "帮我做一个自动整理照片的小工具。"

Preferred: scan real photos → classify → move. If moving is unsafe or blocked:
scan → suggestions → preview/list → user confirms. Help organize real photos;
do not complete on synthetic images.

## Core rules

1. Ordinary users need not supply architecture.
2. Repo-discoverable facts are inspected, not asked.
3. Authoritative technical facts are researched, not guessed or user-explained.
4. Ask only user-intent questions that change the implementation path.
5. User-proposed solutions are not automatically real technical need.
6. Explicit user constraints and learning goals are respected.
7. Broad requests converge small, not into a larger system.
8. Minimum means Minimum Sufficient Working System, not a stub.
9. Implement in the current repo only when it is clearly the target project.
10. After the current implementation is shown insufficient, add the smallest necessary branch.
11. Runnable and correctly verified beats large architecture.
12. Half-open questions stay open; do not fake closure.
13. Degrade automation, not the objective. Shrink breadth, not truth.
14. Diagnose blockers before escalating; ask only the smallest unblock action.
15. Synthetic or fixture success cannot substitute for real-data completion.
16. This skill covers Codex-familiar software-engineering entry problems only.

Do not restate general Git, deletion, testing, or repo-safety rules already present in Codex instructions.
