---
name: dora-deployment-frequency
description: Calculates deployment frequency for student software projects using GitHub releases, tags, deployments, merged PRs, or default-branch commits. Use when Codex needs the DORA deployment frequency metric or a delivery cadence signal for course repositories.
---

# DORA Deployment Frequency

## Definition

Measure how often a student team successfully delivers working changes during the selected date range.

## Required Evidence

- repository
- date range
- team or student mapping
- course-specific deployment or submission definition, if available

## GitHub Proxy Order

Use the first confirmed proxy that fits the course workflow:

1. Releases or version tags.
2. Successful deployment or publish workflow runs.
3. Merged PRs to the default branch.
4. Commits to the default branch when the course does not use PRs.

State the selected proxy. Do not assume a proxy exists until GitHub evidence confirms it.

## Missing Data

- If no reliable delivery event exists, report `unknown`, not zero.
- If the course has no deployment concept, use merged PRs or default-branch commits as a delivery cadence proxy and label it clearly.
- If the date range is missing, ask for it before calculating.

## Student Caveats

- Small teams and short sprints can produce low counts without indicating poor work.
- Pair programming, shared accounts, and instructor-created merges can distort team ownership.
- Direct pushes may hide review cadence; mention this when PRs are not used.

## Output Snippet

```markdown
### Deployment Frequency
- Result: <count and cadence>
- Proxy used: <release/tag/deployment/merged PR/default-branch commit>
- Sample size: <events counted>
- Caveats: <missing data or student-project context>
```
