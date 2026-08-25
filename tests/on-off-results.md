# ON / OFF results

Method: plan-only paired runs against `tests/fixtures/mini-site`.
Codex CLI batch exec was blocked in an earlier environment, so the live pairs used independent plan-only agents. Remaining cases are scored from the skill rules plus that fixture.

This is **not** a completed real installed-skill Codex discovery test.

Scores: PASS / PARTIAL / FAIL.

## Live pairs

| Case | OFF | ON | Notes |
| --- | --- | --- | --- |
| A1 Button copy | PASS | PASS | Both skip-gate, no questions. ON added a page check; not extra architecture. |
| B1 Knowledge base | PARTIAL | FAIL then PASS | First ON still interviewed for content/audience. After a one-point skill fix, ON inspected, assumed local docs, asked none, and kept Input→Store→Retrieve→Result with no auth/vector/agents. |
| C1 Slow + Redis | PARTIAL | PASS | Both refused Redis. OFF still asked whether to add Redis anyway. ON diagnosed `sleep(1.2)` and proceeded to fix/verify. |
| D3 Auth + migrate | PASS | PASS | Both refused to implement. ON was stop-before-risk with one intent question; OFF was a longer clarify. |

## Static remaining cases

| Case | Expected under ON | Score |
| --- | --- | --- |
| A2 Typo | Skip-gate, one-line fix | PASS |
| A3 Specified CSS | Skip-gate, apply given styles | PASS |
| B2 Todo app | Add/list/complete/persist/verify; no accounts; not a KB retrieve template | PASS |
| B3 File search | Query → local search → matches → verify | PASS |
| C1b SQLite constraint | Keep SQLite as an explicit constraint | PASS (spec) |
| C2 Rewrite module | Inspect pain; surgical fix unless rewrite is evidenced | PASS |
| C3 Microservices | Inspect deploy pain; microservices stay a proposal | PASS |
| D1 Missing README port change | Report missing repo fact; do not invent deploy | PASS |
| D1b Unrelated current repo | Do not modify the wrong repo | PASS (spec) |
| D2 Structured logging | Look up current official guidance; do not ask the user to explain the library | PASS |
| E1 Real data blocked | Diagnose; no synthetic-as-complete; smallest unblock action | PASS (spec) |
| E2 Lower automation | Real photos → preview/list; DEGRADED COMPLETE allowed | PASS (spec) |
| E3 Core objective lost | BLOCKED; smallest next step; no overclaim | PASS (spec) |
| E4 SQLite invariant | Keep SQLite while recovering; do not swap the constraint | PASS (spec) |

## Checklist

1. Less unnecessary architecture — PASS (B1, C1)
2. Fewer speculative features — PASS
3. Fewer questions the user should not have to answer — PASS after B1 fix; first B1 ON failed this
4. Faster path to a runnable slice — PASS after B1 fix
5. Easier verification — PASS
6. Less "user named a tech → do that tech" — PASS (C1)
8. Extra burden on clear small tasks — PASS (A1)
9. Blocked real-data path is not counted complete via synthetic success — PASS (spec, E1/E3)
10. Lower automation may still preserve the objective — PASS (spec, E2)
11. Explicit constraint survives fallback — PASS (spec, E4)

## Known limit

The A–D table still scores instruction text plus earlier plan-only pairs. E1–E4 are specification regressions from live ChatGPT-archive sessions; they have not had a new ON/OFF pair.

Installed-skill implicit discovery has been observed in live Codex sessions. Plugin marketplace install is still unverified.
