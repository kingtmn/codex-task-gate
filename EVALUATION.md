# Evaluation

This document records developer-operated evaluations of `codex-task-gate`.

These are not independent or statistically representative tests.

Purpose: document observed behavior, failures, changes, and remaining uncertainty.

## Evaluation status

Internal engineering loop: **COMPLETE** for the current v0.1 core

External effectiveness: **NOT YET VALIDATED**

Multi-skill coexistence: **NOT YET VALIDATED**

Plugin marketplace install: **NOT YET VALIDATED**

## 1. Mac cleaner — PASS

Goal: a small Mac disk junk/cache scanner.

Prompt: broad but bounded; read-only; no deletion; no sudo; no system changes; Task Gate not named.

Environment: Codex CLI 0.132.0, `gpt-5.5`, fresh session.

Observed:

- Task Gate implicitly discovered
- 0 unnecessary questions
- small Python CLI, standard library, user-level paths
- no GUI / daemon / database / cloud
- actual scan executed
- first result double-counted caches
- Codex fixed the counting logic and reran
- final candidate cache total about 33.4 GB

Verdict: **PASS**

Supports: scope control, inspect-first, real execution, self-correction, verification.

Limit: developer-operated single workload.

## 2. ChatGPT KB — CONDITIONAL PASS

Goal: a local knowledge base over a real ChatGPT export, with an explicit SQLite constraint. Local and private; no upload.

Environment: Codex CLI 0.132.0, `gpt-5.5`, fresh session.

macOS TCC blocked access to the Downloads export.

Codex:

- discovered the Skill
- kept SQLite
- stayed a small local tool
- used a synthetic fixture as a smoke test

The real archive was not imported.

Implementation smoke test: **PASS**  
Real task: **INCOMPLETE**

Verdict: **CONDITIONAL PASS**

Key lesson: synthetic success cannot substitute for real-data completion.

## 3. ChatGPT KB exact-path retry — FAIL

The same export was given as two exact files: `conversations-000.json` and `conversations-001.json`.

Result:

- files visible with `ls`
- contents unreadable (macOS TCC)
- Skill discovered
- SQLite respected
- one necessary user-action request
- real SQLite import = 0
- real search = 0
- synthetic smoke test not reported as real completion

Verdict:

- Real task: **FAIL / BLOCKED**
- Task Gate behavior: **PASS**

Key lesson: ask less is not ask nothing. If execution truly depends on a user action, ask only for the smallest necessary action.

## 4. Completion Recovery

The two KB attempts exposed a real completion gap. Commit `d82b748` added a narrow rule from those failures:

- Degrade automation, not the objective.
- Shrink breadth, not truth.
- Synthetic / fixture success cannot complete a real-data task.
- Diagnose and self-resolve before escalating.
- Ask the user only for the smallest unblock action.

The synthetic-vs-real rule is directly supported by the tests. Broader recovery behavior remains only partially exercised. This is not a widely validated fallback theory.

## 5. Instruction compression

Commit `78d1ce1`.

Before: 214 lines, about 2310 tokens  
After: 145 lines, about 1436 tokens  
Reduction: about 38%

Custom Instruction: about 2277 → about 1350 tokens

Goal: remove duplicate expression, not remove behavior. Validator and semantic checklist passed.

Compression is not universally proven safe. The next real KB workload showed no observable regression on that workload.

## 6. Real readable ChatGPT KB — PASS

Input files (copied into a fresh empty test repo):

- `conversations-000.json`: 100,910,258 bytes
- `conversations-001.json`: 72,529,158 bytes
- total about 173 MB decimal file size

Environment: Codex CLI 0.132.0, `gpt-5.5`, fresh session, compressed 145-line Skill.

Observed:

- Skill implicitly discovered
- 0 user questions
- SQLite constraint respected
- Python standard library + `sqlite3`
- local CLI
- no embeddings / RAG / vector DB / Web / cloud

Real import:

- 134 conversations
- 26,386 text messages
- 10,584 empty/non-text nodes skipped
- SQLite DB about 71 MB

Search:

- 费曼: 122 hits
- J-space: 0
- FENGQUN: 0

Zero-hit results stayed zero. A minor local search check failed because `input/` was gitignored; Codex diagnosed that, used a truthful alternative count, and did not ask the user.

Verdict:

- Real task: **PASS**
- Task Gate behavior: **PASS**

## What these tests support

Observed in tested workloads:

- implicit Skill discovery
- reduced speculative scope
- explicit constraints preserved
- real execution rather than plan-only output
- truthful verification
- self-resolution of small blockers
- synthetic data not treated as real completion
- compressed Skill retained observed behavior on the final KB workload

## What they do not prove

These tests do **not** prove:

- general effectiveness
- statistically significant improvement
- independent reproducibility
- behavior with unfamiliar users
- multi-skill compatibility
- trigger collision behavior
- plugin marketplace installation reliability
- behavior across models, Codex versions, or platforms

## Evidence ladder

Current evidence progression:

1. specification cases
2. plan-only comparisons
3. installed-skill discovery
4. Mac Cleaner real execution
5. KB blocked real-data attempts
6. Completion Recovery refinement
7. instruction compression
8. real ~173 MB KB full execution

No benchmark score.

## Next validation

External discovery and adoption.

Desired evidence: other users, their own prompts, their own environments; later, multi-skill coexistence.
