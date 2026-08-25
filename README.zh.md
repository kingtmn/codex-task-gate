# Codex Task Gate

```text
  / \__
 (    @\___
 /         O
/   (_____/
/_____/   U     先看仓库。先做成。验证了再说。
```

Codex 写代码很快。
它也能很快把错误理解写成大量代码。

**Codex Task Gate 拦在那之前。**

不是更聪明的大脑，是更会看门的狗。

先做成，再做大。
自动化可以降级，任务目标不能偷换。

[English](./README.md) | 简体中文

## 为什么要装

普通用户说：

> 帮我做个知识库。

没有门禁时，这句话就够 Agent 脑补：

- 向量库
- 用户和权限
- Agent 和工作流
- 可观测性
- 为想象中的规模准备的架构

真正的问题不是 Codex 不会写代码。

而是：**意图还含糊时，代码已经写得很精确。**

装它，是为了让 Codex 少猜、少问、少把小需求做成大系统，先交出一条能跑、能验的路。遇到现实阻碍时，先找还能完成多少，而不是把报错甩给用户。

## 没有它 / 有它

**没有 Task Gate**

```text
宽泛请求
  → 脑补需求
  → 先上架构
  → 一堆文件
  → 可能是错的系统
```

**有 Task Gate**

```text
宽泛请求
  → 先看仓库
  → 找到当前真实路径
  → 最小充分可运行实现
  → 跑起来
  → 验证
  → 如果被挡住：降低自动化，不偷换真实目标
  → 不够用了再加最小分支
```

## 给谁用

| 谁 | 为什么 |
| --- | --- |
| 普通 Codex 用户 | 知道想做什么，但不会写完整软件规格。 |
| 独立开发 / 快速试做 | 想先拿到能跑的东西，而不是自动生成未来平台。 |
| 有经验的开发者 | 希望 Codex 在 Redis / 重写 / 微服务之前先看证据。 |

普通用户不需要先成为软件架构师。

这不是通用问题路由，不是产品方法论，也不是全自动软件公司。

## 它放在哪里

**早门禁，早让权。**

Codex Task Gate 本来就应该和其他 Codex Skills 一起使用。

它不是领域 Skill，不是 Skill 路由器，也不是总调度器。它不替代测试、安全、数据库或框架类 Skill。

它负责：先把宽泛或带方案的请求边界压清楚，检查自己能查到的事实，尊重明确约束，挡住时找更简单但仍真实的完成路径。然后尽早把具体实现让给真正负责该领域的 Skill 和仓库规则。

```text
用户请求
    ↓
Task Gate（适用时）
    ↓
最小真实可执行边界
    ↓
领域 / 仓库 Skills
    ↓
实现
    ↓
验证
```

这是职责定位，不是声称 Codex runtime 一定首先加载 Task Gate。

Task Gate 去掉的是没有依据的复杂度，不是仓库或专业 Skill 已经证明必要的步骤。如果安全或迁移 Skill 要求回滚和校验，不应为了「更小」把这些步骤删掉。

多 Skill 共存目前仍是设计假设和下一步验证目标。真实交接行为尚未证实。

## 它实际做什么

在非平凡写代码之前：

- 仓库里能查到的，自己查
- 技术事实去权威资料查
- 只问会改变实现路径的用户意图
- 用户点名的技术默认是提案；明确约束或学习目标则尊重
- 默认走最小充分可运行路径
- 理想路径被挡住时，先降低自动化，再把问题交回用户
- 现实证明不够用了，再增加最小必要复杂度

明确的小任务直接放行：改文案、修 typo、指定 CSS。

这里的「最小」不是 stub，也不是代码越少越好。

它是 **最小充分可运行系统**：能跑、覆盖核心能力、路径完整、可以验证。

知识库可以用：录入 → 存储/索引 → 检索 → 结果 → 验证。
CLI、API、诊断修复走：触发 → 核心行为 → 可观察结果 → 验证。

## 30 秒安装

最可靠的是直接装 Skill。官方本地 Skill 位置包括 `$HOME/.agents/skills`，见 [Codex Skills](https://developers.openai.com/codex/skills)。

```bash
mkdir -p ~/.agents/skills/codex-task-gate/agents
curl -fsSL https://raw.githubusercontent.com/kingtmn/codex-task-gate/main/skills/codex-task-gate/SKILL.md \
  -o ~/.agents/skills/codex-task-gate/SKILL.md
curl -fsSL https://raw.githubusercontent.com/kingtmn/codex-task-gate/main/skills/codex-task-gate/agents/openai.yaml \
  -o ~/.agents/skills/codex-task-gate/agents/openai.yaml
```

重启 Codex，或开一个新会话。然后可以说 `$codex-task-gate`，或直接丢一个宽泛 / 带技术方案的 coding 请求。

有些环境也会读 `~/.codex/skills`。如果没出现，把同样的文件拷过去。

### 不安装也可以用

1. 打开 [`instruction.md`](./instruction.md)。
2. 复制「Paste the block below」下面的区块。
3. 粘贴到 Codex Settings → Custom Instructions。

Skill 和粘贴二选一即可。

### 插件安装（可选）

本仓库也带 Codex 插件清单。插件用于 ChatGPT 桌面端 / Codex CLI，[不用于 IDE 扩展](https://developers.openai.com/codex/plugins)。

```bash
codex plugin marketplace add kingtmn/codex-task-gate
codex plugin add codex-task-gate@codex-task-gate
```

然后开一个新的 Codex 会话。如果插件没出现，用上面的 Skill 拷贝。本项目把 Skill 安装当作主路径。

## 例子

**知识库：**「帮我做一个知识库。」
先看仓库。不要脑补企业架构。做一条能加入内容、能检索、能看见结果的完整路径。
如果读不到真实档案，不要用假数据宣布完成。缩范围，不缩真实性。真做不了时，只告诉用户最小下一步。

**网站慢 + Redis：**「网站很慢，加 Redis。」
Redis 是提案。先测量，再改真正的瓶颈。

也适用：todo、小 CLI、小 API、文件搜索、本地自动化。

不适用当成提案的例子：「这个项目必须用 SQLite，因为我正在学 SQLite。」这是明确约束，应保留 SQLite。

## 当前证据

这是早期包（`0.1.0`）。还没有正式 tag / release。

这些是**开发者自己设计、运行和判定的自测**。它们说明核心机制在已测工作负载上按预期工作，不是独立验证，也不是通用有效性或生产指标。

v0.1 核心的内部工程闭环已经走完：设计 → 实现 → 失败 → 精炼 → 压缩 → 真实回归。外部验证是下一阶段。插件市场安装仍未实测。多 Skill 共存也尚未验证。

### 真实测试

**Mac Cleaner。** 全新 Codex 会话未点名就发现了已安装 Skill，把宽泛清理请求收成只读本地扫描，并真正扫了这台机器。第一次结果重复计数，Codex 修正后重跑，候选缓存合计约 33.4 GB。没有 GUI、守护进程、数据库或云架构。

**ChatGPT 知识库。** 压缩后的 145 行 Skill 在全新 `gpt-5.5` 会话中被隐式发现，SQLite 约束被遵守，并对约 173 MB 真实导出做了完整导入：134 个会话、26,386 条文本消息，本地 CLI。`费曼` 122 次命中；`J-space` 和 `FENGQUN` 如实为 0。没有 embeddings、RAG、向量库、Web 或云。

这些是开发者自测，不是第三方独立验证，也不是生产指标。

完整测试过程，包括失败记录，见 [EVALUATION.md](./EVALUATION.md)。

## 愿景

更多工具增加 Agent 能做的事。
更好的门禁改善它选择做的事。

长期想法很简单：更好的 coding agent 可能需要更好的入口门禁，而不只是更多工具。

当前任务更土：一个不会架构的人随口提一个软件需求，Codex 仍能找到今天能跑、能验的最小完整路径。理想路径断了，真实目标也不该一起断。

狗子坐门口。架构以后再说。

## 仓库结构

```text
.agents/plugins/marketplace.json
.codex-plugin/plugin.json
AGENTS.md
EXAMPLES.md
instruction.md
LICENSE
README.md
README.zh.md
EVALUATION.md
skills/codex-task-gate/SKILL.md
tests/
```

## License

MIT
