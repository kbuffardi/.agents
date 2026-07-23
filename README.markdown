# .agents

Reusable agent definitions and skills for GitHub-backed software projects. This repository is the editable source for root agent instructions, repository skills, and the generated Codex agent mirrors derived from them.

## What this repository contains

```text
.
├── plan-agent.md
├── code-reviewer.md
├── refactor-agent.md
├── security-auditor.md
├── test-engineer.md
├── web-performance-auditor.md
├── skills/
│   ├── github-workflow/SKILL.md
│   ├── git-workflow-and-versioning/SKILL.md
│   └── ...
├── generated-codex/
│   ├── plan-agent.toml
│   ├── code-reviewer.toml
│   └── ...
└── sync-codex-agents.py
```

### Roles

| Path | Role |
|---|---|
| `*.md` at the repository root | Files mirrored by `sync-codex-agents.py` into Codex TOML. In this repository, those root Markdown files are the agent definitions such as `plan-agent`, `code-reviewer`, and `security-auditor`. |
| `skills/*/SKILL.md` | Source instructions for reusable repository skills. |
| `generated-codex/*.toml` | Generated Codex mirrors of the repository root `*.md` files. Do not edit by hand. |
| `sync-codex-agents.py` | Regenerates `generated-codex/*.toml` and links `~/.codex/agents` to this repository output. |

## Source of truth and generated files

Edit the Markdown sources:

- root `*.md` files for mirrored Codex agent content
- `skills/*/SKILL.md` for skills

Do **not** hand-edit `generated-codex/*.toml`. They are generated output from `sync-codex-agents.py`, which mirrors every root `*.md` file in this repository.

## How to use this repository

1. Update the relevant source file:
   - root `*.md` for mirrored Codex agent content
   - `skills/*/SKILL.md` for a skill
   - `README.markdown` for repository documentation
2. If you changed a root `*.md` file, regenerate Codex mirrors:

   ```bash
   python3 sync-codex-agents.py
   ```

3. Review the generated diff in `generated-codex/`.
4. If you changed only a skill or documentation file, no generated Codex mirror should change.
5. Submit the change through the repository GitHub workflow: issue-first planning, short-lived branch, and PR review.

## Always-loaded files vs skills

This distinction is the main operating model of this repository:

- **Always-loaded files** hold short, non-negotiable defaults the agent should follow on every relevant task.
- **Skills** hold the detailed playbook, rationale, examples, and task-specific procedure.

If a rule only exists in a skill, agents may treat it as advisory because they first have to discover that the skill applies. If a rule belongs on every relevant task, put the short version in an always-loaded file and use the skill for the long version.

### Good pattern

```markdown
## Mandatory GitHub workflow

For any code or documentation change in this repository:
- work on a dedicated branch from `main`
- validate or create a GitHub issue before implementation
- update the issue when plans or requirements change
- open or update a PR that includes `closes #<issue-number>`
- use the repository GitHub workflow skill for the detailed procedure
```

### Anti-pattern

```markdown
Use the github-workflow skill when relevant.
```

That is too indirect to reliably enforce default behavior.

## Adopt this pattern in your project

Use this repository as a reference or copy selected agents and skills into your own project. The key adoption rule is simple:

> Put mandatory defaults in the file your agent always loads. Put the detailed procedure in skills.

### Student DORA tracking

If students may not invoke a named DORA agent, put the short DORA default in the downstream project's always-loaded `AGENTS.md` and keep the detailed workflow in `skills/student-dora-tracking/SKILL.md`. The top-level DORA skill can coordinate metric-specific skills for deployment frequency, lead time for changes, change failure rate, and time to restore.

```markdown
## Student DORA defaults

For student or course repositories:
- preserve DORA-relevant evidence while working, including PRs, commits, releases/tags, CI results, issues, failures, fixes, and deployment or submission events
- use `student-dora-tracking` for delivery metrics, workflow health, project progress, PR summaries, milestone reports, or course/instructor reporting
- use the metric-specific DORA skills when only one metric is needed
- use `sprint-retrospective` for end-of-sprint reflection and coaching
- do not assign grades, scores, penalties, or rankings from DORA metrics unless an instructor-provided rubric explicitly defines that interpretation
- frame student-facing output as coaching and workflow-improvement guidance
```

### Codex projects: `AGENTS.md`

For Codex, the always-loaded project file is `AGENTS.md`. This repository uses that pattern as downstream guidance; keep the file short and directive in projects that adopt these agents and skills.

```markdown
# Project agent rules

## Mandatory GitHub workflow

For any code or documentation change in this repository:
- use a dedicated branch from `main` named `feature/...`, `fix/...`, `chore/...`, or `refactor/...`
- validate an existing GitHub issue or create one before implementation
- update the issue when plans or requirements change
- open or update a PR for the branch and include `closes #<issue-number>` in the PR description

## Detailed procedure

- Use `skills/github-workflow/SKILL.md` for the full issue, branch, and PR playbook.
- Use `skills/git-workflow-and-versioning/SKILL.md` for branching, commits, and staging hygiene.
```

### GitHub Copilot projects: `.github/copilot-instructions.md`

For GitHub Copilot, put the same mandatory defaults in `.github/copilot-instructions.md`.

```markdown
# Copilot instructions

For any code or documentation change in this repository:
- work on a dedicated branch from `main`
- validate or create a GitHub issue before implementation
- update the issue when plans or requirements change
- open or update a PR that includes `closes #<issue-number>`

Use the project's workflow skills or docs for the detailed procedure.
```

### What to copy first

If you are adopting this repository into a new project, start with:

1. a short `AGENTS.md` or `.github/copilot-instructions.md` with mandatory workflow defaults
2. the skill files that explain those defaults in detail
3. any root agent definitions you want to expose as named agents

## GitHub workflow defaults for downstream projects

This repository assumes GitHub is the system of record for planning and review. The minimum defaults to carry into downstream projects are:

1. **Issue first.** Validate an existing issue or create one before implementation.
2. **Short-lived branch.** Branch from `main` using a type-prefixed name such as `feature/task-creation`, `fix/duplicate-tasks`, `chore/update-deps`, or `refactor/auth-module`.
3. **Keep the issue current.** When the plan changes, add a comment that records the new decision and the human input that caused it, including quoted prompts or decisions when they materially change the plan.
4. **PR closes the issue.** Open a PR from the branch and include `closes #<issue-number>` in the description.
5. **Keep changes atomic.** Do not mix unrelated documentation, generator, agent, or skill edits in one PR.

Example:

```text
Issue: #9
Branch: chore/add-readme-markdown
PR description: closes #9
```

## Where detailed guidance belongs

Use always-loaded files for the short rules. Put the long-form operating guide in skills such as:

- `skills/github-workflow/SKILL.md`
- `skills/git-workflow-and-versioning/SKILL.md`
- `skills/documentation-and-adrs/SKILL.md`

That split keeps the default behavior obvious without turning the always-loaded file into a policy manual.
