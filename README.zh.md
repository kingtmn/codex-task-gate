# Codex Task Gate

```text
  / \__
 (    @\___
 /         O
/   (_____/
/_____/   U     先看仓库。最小能跑。验证了再说。
```

这是一只给 [Codex](https://github.com/openai/codex) 用的看门狗。

不是更聪明的大脑，是更会拦的门。

普通用户不该先学会画架构图，才能让 AI 写代码。你说「帮我做一个知识库」，它不该立刻上向量库、权限、Agent 和可观测性平台。它该先看仓库，收成一条能录入、能检索、能看见结果、能验证的路。

[English](./README.md) | 简体中文

## 为什么需要看门狗

Coding agent 翻车姿势很固定，而且很狗：

- 网站慢 → 直接上 Redis
- 模块乱 → 直接重写
- 部署烦 → 直接微服务
- 需求宽 → 直接未来架构

然后你得到一堆明天才会用到的系统，今天还跑不起来。

`codex-task-gate` 只做一件事：在非平凡改代码开始前，确认 Codex 已经有足够信息动手，并把任务压成 **当前最小充分、可运行、可验证** 的实现路径。

它不理解世界。它只问：

1. 要改变什么可观察行为？
2. 哪些事实 Codex 自己能查到？
3. 哪个决策真正属于用户？
4. 现在最小充分、能验证的解是什么？

## 它会怎样看门

| 场景 | 狗子的反应 |
| --- | --- |
| 改按钮文案 / 修 typo / 指定 CSS | 放行。不加仪式。 |
| 「做个知识库 / todo / 文件搜索」 | 收成一条完整路径，不补全大系统。 |
| 「很慢，加 Redis」 | Redis 只是提案。先测量，再决定。 |
| 认证迁移这类高风险 | 先问一个普通人能答的问题，或停在不可逆决策前。 |

这里的「最小」不是 stub，也不是代码越少越好。

它是 **Minimum Sufficient Working System**：能跑、覆盖核心能力、路径完整、可以验证。今天不够用了，再加最小必要的下一分支。未来的平台，等未来的证据。

画饼到此为止。饼要能入口：先有一条能跑通的路。

## 在 Codex 里安装

把本仓库当作本地 Codex 插件源：

1. 将本仓库加入 Codex 插件源。
2. Codex 读取 [`.codex-plugin/plugin.json`](./.codex-plugin/plugin.json)。
3. Codex 加载 [`skills/codex-task-gate/SKILL.md`](./skills/codex-task-gate/SKILL.md)。

插件名：

```text
codex-task-gate
```

Skill 名：

```text
codex-task-gate
```

也可以只拷 Skill：

```bash
mkdir -p ~/.codex/skills/codex-task-gate
curl -fsSL https://raw.githubusercontent.com/kingtmn/codex-task-gate/main/skills/codex-task-gate/SKILL.md \
  -o ~/.codex/skills/codex-task-gate/SKILL.md
```

装完后重新开一个 Codex 会话。下一轮才能发现 `$codex-task-gate`。

## 不安装也可以用

不想装插件，也不想依赖 `AGENTS.md`：

1. 打开 [`instruction.md`](./instruction.md)。
2. 复制「Paste the block below」下面的区块。
3. 粘贴到 Codex Settings → Custom Instructions。

这是自包含版本。Codex 不用读仓库也能按同一套门禁做事。

插件和粘贴二选一即可，不必两套一起上。仓库自己的 `AGENTS.md` 冲突时，以仓库为准。

## 仓库结构

```text
.codex-plugin/plugin.json
AGENTS.md
EXAMPLES.md
instruction.md
LICENSE
README.md
README.zh.md
skills/codex-task-gate/SKILL.md
tests/
```

## 还想画的饼

理想状态很土：一个不会架构的人随口提一个软件需求，Codex 仍能找到今天能跑、能验的最小完整路径。慢了再量。不够用再加一枝。不要一上来就创业。

狗子坐门口。架构以后再说。

## License

MIT
