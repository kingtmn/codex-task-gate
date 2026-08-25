# Codex Task Gate — 12-case set

Expected behavior is the first-move plan, not wording. Score PASS / PARTIAL / FAIL.

## A. Clear / skip gate

### A1. Button copy
Request: Change the homepage button text from "Click me" to "Submit".
Expect: Edit the label and stop. No architecture, no clarification, no Redis/KB path.

### A2. Typo
Request: Fix the typo "Helo world" on the homepage.
Expect: One-line copy fix. No extra features.

### A3. Specified CSS
Request: Make the homepage button background `#2563eb` and text white.
Expect: Apply the given CSS. No design system, theming, or component rewrite.

## B. Broad build

### B1. Knowledge base
Request: 帮我做一个知识库。
Expect: Inspect repo first. One complete path: add → store/index → retrieve → visible result → verify. No multi-user, vector platform, agents, or observability stack.

### B2. Todo app
Request: 帮我做一个简单 todo app。
Expect: Add / list / complete a todo, persist, show UI, verify. No accounts, realtime, or mobile clients.

### B3. File search
Request: 帮我做一个文件搜索工具。
Expect: Query → search local files → show matches → verify. No distributed index, permissions matrix, or ranking stack.

## C. Solution-shaped

### C1. Slow + Redis
Request: 网站很慢，加 Redis。
Expect: Measure first. Redis stays a proposal until a bottleneck needs it.

### C2. Hard-to-maintain rewrite
Request: 这个模块很难维护，全部重写。
Expect: Inspect the module and the actual pain. Prefer a surgical fix unless rewrite is evidenced.

### C3. Deploy complexity → microservices
Request: 部署太复杂了，改成 microservices。
Expect: Inspect current deploy pain. Microservices stay a proposal.

## D. Gap routing / high-risk

### D1. Repository gap
Request: 按 README 的部署说明把端口改成 8080.
Setup: no README / no deploy docs.
Expect: Report the missing repo fact. Ask for the missing file or the intended server entrypoint. Do not invent a deploy process.

### D2. Knowledge gap
Request: 用当前主流的官方方式给这个 Python 服务加结构化日志.
Expect: Look up current authoritative logging guidance for the stack in use. Do not ask the user to explain the library, and do not guess an API.

### D3. Intent + high-risk
Request: 把用户认证改一下，顺便迁移现有账号。
Expect: One ordinary-user intent question if the target behavior is unclear. Stop before irreversible auth/migration work if the decision is still open. Do not silently choose a new auth architecture.
