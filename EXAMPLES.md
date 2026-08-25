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

- inspect the repo first
- assume local documents
- add → store/index → retrieve → show a result → verify
- no multi-user, vector platform, agents, or observability stack

User: 帮我做一个简单 todo app。

Expected: add / list / complete / persist / show UI / verify. No accounts.

## Solution-shaped

User: 网站很慢，加 Redis。

Expected: Redis stays a proposal. Measure first. Fix the evidenced bottleneck. Verify before/after.

User: 部署太复杂了，改成 microservices。

Expected: inspect the current deploy pain. Microservices stay a proposal.

## High-risk / gap

User: 把用户认证改一下，顺便迁移现有账号。

Expected: one ordinary-user question if the target is unclear. Stop before irreversible auth/migration if the decision is still open.
