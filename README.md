# Codex Task Gate

```text
  / \__
 (    @\___
 /         O
/   (_____/
/_____/   U     such inspect. very minimum. wow verify.
```

Codex can write code fast.
It can also build the wrong thing fast.

**Codex Task Gate sits before that happens.**

Not a bigger brain. A better gate dog.

English | [Simplified Chinese](./README.zh.md)

## Why install this?

A normal user says:

> 帮我做个知识库。

Without a gate, that sentence is enough for an agent to invent:

- a vector stack
- users and permissions
- agents and workflows
- observability
- architecture for imagined scale

The problem is not that Codex cannot write code.

The problem is that **vague intent can become precise code before anyone notices the intent was vague.**

Install this if you want Codex to inspect first, ask less, and ship a path that actually runs.

## Without / with

**Without Task Gate**

```text
Broad request
  → imagined requirements
  → architecture
  → many files
  → maybe the wrong system
```

**With Task Gate**

```text
Broad request
  → inspect repo
  → identify the actual path
  → smallest sufficient working implementation
  → run
  → verify
  → expand only when required
```

## Who this is for

| Who | Why |
| --- | --- |
| Ordinary Codex users | You know what you want, but you do not write a software spec. |
| Indie / rapid builders | You want something that runs today, not a generated future platform. |
| Experienced developers | You want Codex to check evidence before Redis, rewrites, or microservices. |

Not a general problem router. Not a product coach. Not an AGI controller.

## What it actually does

Before non-trivial coding:

- inspect self-discoverable repo facts
- research authoritative technical facts
- ask only path-changing user intent
- treat named technologies as proposals unless they are explicit constraints
- default to a minimum sufficient working path
- add complexity after evidence, not before

Clear tiny tasks skip the gate: button copy, typos, specified CSS.

Minimum here means **Minimum Sufficient Working System**: runnable, core capability complete, path intact, verifiable. Not a stub. Not "fewest lines." Not tomorrow's platform.

A knowledge base still uses add → store/index → retrieve → result → verify.
A CLI, API, or diagnostic fix uses trigger → core behavior → observable result → verify.

## 30-second install

The reliable path is a local skill. [Official Codex skill locations](https://developers.openai.com/codex/skills) include `$HOME/.agents/skills`.

```bash
mkdir -p ~/.agents/skills/codex-task-gate/agents
curl -fsSL https://raw.githubusercontent.com/kingtmn/codex-task-gate/main/skills/codex-task-gate/SKILL.md \
  -o ~/.agents/skills/codex-task-gate/SKILL.md
curl -fsSL https://raw.githubusercontent.com/kingtmn/codex-task-gate/main/skills/codex-task-gate/agents/openai.yaml \
  -o ~/.agents/skills/codex-task-gate/agents/openai.yaml
```

Restart Codex, or start a new session. Then mention `$codex-task-gate` or let it match a broad / solution-shaped coding request.

Some Codex setups also load `~/.codex/skills`. If the skill does not appear, copy the same files there.

### Use without installing

1. Open [`instruction.md`](./instruction.md).
2. Copy the block under "Paste the block below".
3. Paste it into Codex Settings → Custom Instructions.

You do not need both the skill and the paste.

### Plugin install (optional)

This repository also has a Codex plugin manifest. Plugins are for ChatGPT desktop / Codex CLI, [not the IDE extension](https://developers.openai.com/codex/plugins).

```bash
codex plugin marketplace add kingtmn/codex-task-gate
codex plugin add codex-task-gate@codex-task-gate
```

Then start a new Codex session. If the plugin does not appear, use the skill copy above. That path is the one this project treats as primary.

## Examples

**Knowledge base:** "帮我做一个知识库。"
Inspect. Do not invent an enterprise stack. One complete path that can add, retrieve, and show a result.

**Slow site + Redis:** "网站很慢，加 Redis。"
Redis is a proposal. Measure first. Fix the evidenced bottleneck.

Also fits: a todo app, a small CLI, a tiny API, file search, a local automation.

Does not fit: "this project must use SQLite because I am learning SQLite." That is a constraint. Keep SQLite.

## Current evidence

This is an early package (`0.1.0`). There is no tagged release.

What we have:

- 4 live plan-only pairs
- 8 static / specification cases
- no completed real installed-skill Codex discovery test

Early evaluation suggests:

- less speculative architecture
- fewer unnecessary questions
- better diagnosis before user-named technology

That is a signal, not a production metric.

**Real installed-skill Codex evaluation is next.**

## Vision

More tools increase what an agent can do.
A better gate improves what it chooses to do.

The long-term idea is simple: better coding agents may need better entry gates, not just more tools.

The current job is smaller: when an ordinary person gives Codex a fuzzy coding request, Codex still finds a path that runs today, does the core thing, and can be checked.

Such future. Very later. Wow now.

## Repository layout

```text
.agents/plugins/marketplace.json
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

## License

MIT
