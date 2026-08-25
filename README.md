# Codex Task Gate

```text
  / \__
 (    @\___
 /         O
/   (_____/
/_____/   U     such inspect. very finish. wow verify.
```

Codex can write code fast.
It can also build the wrong thing fast.

**Codex Task Gate sits before that happens.**

Not a bigger brain. A better gate dog.

Build less. Finish more.
When automation fails, the goal should not fail with it.

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

Install this if you want Codex to inspect first, ask less, ship a path that actually runs, and keep working toward a usable result when the preferred path breaks.

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
  → if blocked: lower automation, keep the real goal
  → expand only when required
```

## Who this is for

| Who | Why |
| --- | --- |
| Ordinary Codex users | You know what you want, but you do not write a software spec. |
| Indie / rapid builders | You want something that runs today, not a generated future platform. |
| Experienced developers | You want Codex to check evidence before Redis, rewrites, or microservices. |

Not a general problem router. Not a product coach. Not an AGI controller.

## Where it fits

**Gate early. Yield early.**

Codex Task Gate is meant to work **alongside** other Codex skills. It is not a domain skill, a skill router, a universal orchestrator, or a replacement for testing, security, database, or framework skills.

It is for:

- narrowing broad or solution-shaped requests
- inspecting what Codex can resolve itself
- preserving explicit constraints
- establishing the smallest truthful execution boundary
- recovering a simpler real completion when blocked

Then it should yield to applicable domain and repository instructions for the specialized work.

```text
User request
    ↓
Task Gate (when applicable)
    ↓
Smallest truthful execution boundary
    ↓
Domain / repository skills
    ↓
Implementation
    ↓
Verification
```

This is a conceptual responsibility boundary, not a guarantee that Codex loads Task Gate before every other skill.

Task Gate removes speculative complexity, not complexity justified by the repository or a specialized domain skill. If a security or migration skill requires rollback or validation, keep those steps rather than deleting them just to make the implementation smaller.

Multi-skill coexistence is currently a design hypothesis and a next validation target. The intended role is pre-execution / entrance control. Real handoff behavior is not yet proven.

## What it actually does

Before non-trivial coding:

- inspect self-discoverable repo facts
- research authoritative technical facts
- ask only path-changing user intent
- treat named technologies as proposals unless they are explicit constraints
- default to a minimum sufficient working path
- if that path is blocked, lower automation before handing the task back
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
If the preferred path cannot read the real archive, do not finish on fake sample data. Keep a real search or index path, or say what already works and the one smallest next step.

**Slow site + Redis:** "网站很慢，加 Redis。"
Redis is a proposal. Measure first. Fix the evidenced bottleneck.

Also fits: a todo app, a small CLI, a tiny API, file search, a local automation.

Does not fit: "this project must use SQLite because I am learning SQLite." That is a constraint. Keep SQLite.

## Current evidence

This is an early package (`0.1.0`). There is no tagged release.

These are **developer-operated self-tests**: designed, run, and judged by the project author. They show that the core mechanism behaved as intended in tested workloads. They are not independent validation, not proof of general effectiveness, and not a production metric.

Internal engineering loop for the v0.1 core: design → implementation → failure → refinement → compression → real regression test. External validation is next: other users, their prompts, their environments.

In one developer-operated live test, the compressed 145-line skill was implicitly discovered by Codex (`gpt-5.5`, fresh session) and used on a real ~173 MB ChatGPT export. Codex built a local Python/SQLite CLI, imported 134 conversations and 26,386 text messages, and verified real search without adding embeddings, RAG, a vector database, Web UI, or cloud services. Zero-hit queries were reported as zero. This is one real workload, not independent validation.

Plugin marketplace install is still unverified. Multi-skill coexistence is not yet validated.

## Vision

More tools increase what an agent can do.
A better gate improves what it chooses to do.

The long-term idea is simple: better coding agents may need better entry gates, not just more tools.

The current job is smaller: when an ordinary person gives Codex a fuzzy coding request, Codex still finds a path that runs today, does the core thing, and can be checked. If the fancy path breaks, it should still try to finish the real job.

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
