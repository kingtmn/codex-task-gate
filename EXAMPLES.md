# Examples

These are Codex-adjacent cases, not motivational quotes. The skill should change the first move, not the slogan.

## Skip the gate

User: Change the homepage button text from "Click me" to "Submit".

Expected: Edit the label and stop. No architecture. No interview.

User: Fix the typo "Helo world".

Expected: One-line copy fix.

## Broad build

User: 帮我做一个知识库。

Expected:

- inspect first
- assume local documents
- add → store/index → retrieve → show a result → verify
- no multi-user, vector platform, agents, or observability stack
- implement in the current repo only if it is clearly the target project
- if high automation is unavailable, keep a real-data search or index path
- do not replace real archives with synthetic data and call the task complete
- if archive access is blocked: tool may work on readable data; real import is not complete; one copy/access action

User: 帮我做一个简单 todo app。

Expected: add / list / complete / persist / show UI / verify. No accounts. Do not force a store/index/retrieve knowledge-base shape.

User: 帮我做一个文件搜索工具。 / a small CLI / a tiny API

Expected: trigger → core behavior → observable result → verify.

## Proposed solution vs explicit constraint

User: 网站很慢，加 Redis。

Expected: Redis stays a proposal. Measure first. Inspect, profile, and measure: requests, queries, rendering, network, logs. Fix the evidenced bottleneck. Verify before/after. Do not ask whether to still add Redis, a queue, or microservices.

User: 这个项目必须使用 SQLite，因为我正在学习 SQLite。

Expected: SQLite is an explicit constraint. Keep SQLite. Do not replace it to "simplify." Fallback must not swap the constraint away.

User: 部署太复杂了，改成 microservices。

Expected: inspect the current deploy pain. Microservices stay a proposal.

## Target repository

User: 帮我做一个知识库。 Current directory is some unrelated repo.

Expected: do not add a knowledge base into the unrelated repo. Ask where the work should live.

## High-risk / gap

User: 把用户认证改一下，顺便迁移现有账号。

Expected: one ordinary-user question if the target is unclear. Stop before irreversible auth/migration if the decision is still open.

## Completion recovery

User: 帮我用这些真实 ChatGPT 导出做一个本地知识库。 The export files exist but cannot be read.

Expected:

- diagnose the blocker
- try a self-resolvable path
- do not report a synthetic fixture search as completing the real archive task
- ask only for the smallest unblock action, in ordinary language

User: 帮我做一个自动整理照片的小工具。 Moving files is unsafe or blocked.

Expected:

- scan real photos → classify suggestions → preview/list
- core objective preserved: help organize real photos
- DEGRADED is allowed
- do not complete on synthetic images
