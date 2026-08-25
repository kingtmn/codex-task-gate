# Codex Task Gate

```text
  / \__
 (    @\___
 /         O
/   (_____/
/_____/   U     such inspect. very minimum. wow verify.
```

A [Codex](https://github.com/openai/codex) skill that sits at the door before non-trivial coding starts.

Not a bigger brain. A better gate dog.

Ordinary people should be able to say "帮我做一个知识库" without drawing an architecture diagram. Codex should inspect first, shrink the request, ship a path that actually runs, and prove it.

English | [Simplified Chinese](./README.zh.md)

## Why this exists

Coding agents fail in a very doge way:

- much Redis, no measurement
- very microservice, such deploy pain
- so knowledge base, many agents, zero documents
- wow rewrite, still the same bug

`codex-task-gate` is the small ritual that stops incomplete wording from becoming a large codebase.

It does **not** try to understand the world. It only answers:

1. What observable behavior should change?
2. What can Codex discover itself?
3. What decision actually belongs to the user?
4. What is the smallest sufficient working solution that can be verified now?

## What you get

| Situation | Gate dog does |
| --- | --- |
| Clear tiny task | Walks past. Change the button. Fix the typo. Apply the CSS. |
| Broad build | One complete path: input → store/index → retrieve → visible result → verify |
| "Add Redis / rewrite / microservices" | Treats that as a proposal. Inspects. Diagnoses. Then maybe that tech. |
| Missing user intent on a dangerous change | Asks one ordinary question, or stops before auth/migration |

Minimum here means **Minimum Sufficient Working System**: runnable, core capability complete, path intact, verifiable. Not a stub. Not "fewest lines." Not tomorrow's platform.

## Install in Codex

Use this repository as a local Codex plugin source.

1. Add the repository to your Codex plugin sources.
2. Codex reads [`.codex-plugin/plugin.json`](./.codex-plugin/plugin.json).
3. Codex loads [`skills/codex-task-gate/SKILL.md`](./skills/codex-task-gate/SKILL.md).

Plugin name:

```text
codex-task-gate
```

Skill name:

```text
codex-task-gate
```

Or copy the skill into your user skills directory:

```bash
mkdir -p ~/.codex/skills/codex-task-gate
curl -fsSL https://raw.githubusercontent.com/kingtmn/codex-task-gate/main/skills/codex-task-gate/SKILL.md \
  -o ~/.codex/skills/codex-task-gate/SKILL.md
```

Restart Codex after installing. The next session can discover `$codex-task-gate`.

## Use without installing

If you do not want a plugin or an `AGENTS.md`:

1. Open [`instruction.md`](./instruction.md).
2. Copy the block under "Paste the block below".
3. Paste it into Codex Settings → Custom Instructions.

That version is self-contained. Codex can apply the same gate without reading this repo.

You do not need both the plugin and the paste. Pick one.

## Repository layout

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

## The dream, kept small

The pitch is not "autonomous software company."

The pitch is: a normal person gives Codex a fuzzy coding request, and Codex still finds a path that runs today, does the core thing, and can be checked. When that path is not enough, add the smallest next branch. Not a platform. Not a framework. A dog at the gate.

Such future. Very later. Wow now.

## License

MIT
