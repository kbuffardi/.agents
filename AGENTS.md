# AGENTS.md

## Purpose

This is the persistent agent routing guide for this repository. Use it to decide which root agent definition and which repository skill should shape a task before planning, editing, reviewing, or publishing changes.

## Source Of Truth

- Root agent Markdown files are the source definitions for repository agents.
- `skills/*/SKILL.md` files are the source instructions for repository skills. Read the relevant `SKILL.md` completely before using a skill.
- `generated-codex/*.toml` files are generated mirrors for Codex and should not be hand-edited. They are generated from the agents specified in `.`
- `./sync-codex-agents.py` regenerates Codex agent TOML from the root agent Markdown files.
- For persistent agent behavior, update `AGENTS.md` or the relevant source agent/skill file. For one-off feature decisions, use GitHub issue comments, specs, or PR notes.

## Required Workflow

- ALWAYS ON: Unless specifically instructed not to, each project should be affiliated with a GitHub repository. Plans should ALWAYS be documented as GitHub Issues. Any file changes, including plans, should ALWAYS be stored in a new feature branch (as described in `skills/github-workflow/SKILL.md`), and implementations should open GitHub Pull Requests (PRs) as described in `skills/github-workflow/SKILL.md`.
- ALWAYS ON: For any code revision or documentation change, use `skills/git-workflow-and-versioning/SKILL.md` to record revisions with conventional version control.
- ALWAYS ON: Start implemented changes from a dedicated branch off `main` with a type-prefixed name such as `feature/...`, `fix/...`, `chore/...`, or `refactor/...`. Never make changes on the `main` branch
- ALWAYS ON: During implementation and revision, update the issue when plans or decisions change, and open a PR that references the issue with `closes #<issue-number>` as described in `as described in `skills/github-workflow/SKILL.md`
- Keep changes atomic. Do not mix unrelated docs, generator, agent, or skill edits in one PR.

## Agent Routing

- DEFAULT unless specified otherwise, use `plan-agent.md` for all planning: Use for feature planning, implementation specs, task breakdowns, and handoff plans before code changes.
- Upon request, use `plan-reviewer.md`: Use to review a plan for completeness, feasibility, missing context, and implementation readiness before execution.
- `code-reviewer.md`: Use for code review before merge, especially correctness, readability, architecture, security, performance, regressions, and missing tests.
- `refactor-agent.md`: Use for maintainability and simplification reviews when behavior should stay the same.
- `security-auditor.md`: Use for security-focused review, threat modeling, vulnerability detection, and hardening recommendations.
- `test-engineer.md`: Use for test strategy, coverage analysis, test design, and QA review.
- `web-performance-auditor.md`: Use for web performance audits involving Core Web Vitals, loading, rendering, network behavior, or browser performance risks.

## Skill Routing

### Planning And Context

- `using-agent-skills`: Use when starting a session or deciding which skills apply.
- `context-engineering`: Use when setting up or repairing persistent agent context, including this file.
- `interview-me`: Use when the request is underspecified and product intent needs to be extracted before planning.
- `idea-refine`: Use when an idea is still vague or needs structured exploration before convergence.
- `spec-driven-development`: Use when starting a new project, feature, or significant change without a clear spec.
- `planning-and-task-breakdown`: Use when requirements are clear and need ordered implementation tasks.
- `doubt-driven-development`: Use for high-stakes or non-trivial decisions that need adversarial review before acceptance.
- `source-driven-development`: Use when implementation depends on current framework, library, or external API documentation.

### Git, GitHub, And Shipping

- `github-workflow`: Use for GitHub issue and PR lifecycle on every GitHub-backed repository change.
- `git-workflow-and-versioning`: Use for branching, commits, staging, generated files, and version-control hygiene.
- `git-commit`: Use when creating commits that need an intentional message and optional reasoning note.
- `ci-cd-and-automation`: Use when setting up or changing CI, deployment pipelines, quality gates, or automation.
- `shipping-and-launch`: Use when preparing production release plans, rollout checks, monitoring, or rollback strategy.

### Implementation Practices

- `incremental-implementation`: Use when a change touches multiple files or should be delivered in small verified slices.
- `api-and-interface-design`: Use when designing public APIs, module boundaries, schemas, contracts, REST endpoints, or GraphQL interfaces.
- `frontend-ui-engineering`: Use when building or changing user-facing UI.
- `code-simplification`: Use for behavior-preserving simplification and readability improvements.
- `deprecation-and-migration`: Use when removing, replacing, or migrating existing systems, APIs, or features.

### Testing And Debugging

- `code-review-and-quality`: Use before merging changes or when reviewing code written by a human or agent.
- `test-driven-development`: Use when changing logic, fixing bugs, or proving behavior with tests.
- `test-engineer.md`: Use the agent when broader test strategy or coverage analysis is needed.
- `debugging-and-error-recovery`: Use when tests fail, builds break, or behavior differs from expectations.
- `browser-testing-with-devtools`: Use when inspecting browser runtime behavior with Chrome DevTools MCP.
- `test-in-browser`: Use when validating a browser feature through Playwright MCP.

### Security, Performance, And Observability

- `security-and-hardening`: Use when handling user input, authentication, authorization, secrets, data storage, or third-party integrations.
- `security-auditor.md`: Use the agent for independent security review or threat-focused findings.
- `performance-optimization`: Use when performance requirements, regressions, profiling data, or Core Web Vitals optimization are in scope.
- `web-performance-auditor.md`: Use the agent for performance audit reports and prioritized findings.
- `observability-and-instrumentation`: Use when adding logs, metrics, tracing, alerts, or production diagnostics.

### Documentation

- `documentation-and-adrs`: Use when adding durable docs, recording decisions, changing public APIs, or preserving context for future agents.
- `AGENTS.md`: Update this file when persistent routing, workflow, or source-of-truth rules change.
- GitHub issues and PR descriptions: Use for task-specific context, decisions, validation, and review discussion.

### Language-Specific Simplification

- `python-code-simplifier`: Use for recently modified Python code that needs clarity and maintainability review.
- `typescript-code-simplifier`: Use for recently modified TypeScript or JavaScript that needs clarity and maintainability review.

## Common Playbooks

- New feature: `github-workflow`, `interview-me` if intent is unclear, `spec-driven-development`, `plan-agent.md`, `plan-reviewer.md`, `incremental-implementation`, `test-driven-development`, then `code-reviewer.md`.
- Bug fix: `github-workflow`, `debugging-and-error-recovery`, `test-driven-development`, `test-engineer.md` when coverage is unclear, then `code-reviewer.md`.
- Refactor: `github-workflow`, `code-simplification` or the relevant language simplifier, `refactor-agent.md`, focused tests, then `code-reviewer.md`.
- UI or browser work: `github-workflow`, `frontend-ui-engineering`, `browser-testing-with-devtools` or `test-in-browser`, and `web-performance-auditor.md` when performance risk exists.
- Security-sensitive work: `github-workflow`, `security-and-hardening`, `security-auditor.md`, tests for abuse cases, then `code-reviewer.md`.
- Performance work: `github-workflow`, `performance-optimization`, `web-performance-auditor.md`, measured validation, then `code-reviewer.md`.
- Documentation-only change: `github-workflow`, `documentation-and-adrs`, verify file coverage and links, then review for accuracy.

## Repository Notes

- `plan-reviewer.md` currently has source frontmatter `name: plan-reviwer`; generated Codex metadata uses `plan-reviewer`. Treat this as a known source quirk unless a dedicated fix is requested.
- The `python-code-simplifier` skill currently lives under `skills/python-code-simiplifier/`. Use the skill name from its frontmatter and the existing path when referencing the file.
- Do not regenerate or edit `generated-codex/*.toml` for documentation-only changes to this file.
