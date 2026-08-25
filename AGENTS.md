# AGENTS.md

- Branch: main
- Repository: kingtmn/codex-task-gate

---

This repository is a Codex-native plugin package. Treat it as a reusable skill, not as a generic prompt dump.

## Source of truth

- Plugin manifest: `.codex-plugin/plugin.json`
- Repo marketplace: `.agents/plugins/marketplace.json`
- Skill behavior: `skills/codex-task-gate/SKILL.md`
- Custom Instructions copy-paste version: `instruction.md`
- Usage examples: `EXAMPLES.md`
- Public overview: `README.md` and `README.zh.md`

## Package intent

Teach Codex a pre-coding gate for software-engineering work:

- inspect self-discoverable gaps before asking,
- treat user-proposed technology as unverified unless it is an explicit constraint,
- shrink broad requests to a minimum sufficient working path,
- if that path is blocked, recover a lower-automation real completion before asking the user,
- implement in the current repo only when it is clearly the target project,
- skip the gate on clear, low-risk tasks.

## Maintenance rules

- Keep this repository Codex-native.
- Keep `SKILL.md` as the behavioral source of truth.
- Keep `instruction.md` self-contained so it works without `AGENTS.md`.
- Do not expand this skill into a general problem router, cognitive router, skill router, or product methodology.
- Multi-skill positioning is narrow-then-yield; do not turn Task Gate into an orchestrator.
- Completion recovery must preserve the core objective and truth. Synthetic success cannot count as real-task completion.
- Do not restate general Git, deletion, testing, or repo-safety rules already present in Codex instructions.
- README copy may be playful. Skill instructions stay imperative and dense.
- Keep examples concrete and code-adjacent.

## Quality bar

Before publishing a change, confirm:

- The file list still matches the Codex package shape.
- The manifest points at this repository.
- README, instruction, and SKILL describe the same behavior.
- `instruction.md` can be pasted into Codex Custom Instructions.
- `SKILL.md` stays short enough to load as a skill, not as an essay.
- Do not point privacy or terms URLs at LICENSE.
