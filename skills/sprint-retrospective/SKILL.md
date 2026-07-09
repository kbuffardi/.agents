---
name: sprint-retrospective
description: Facilitates sprint retrospectives for student software teams using GitHub evidence, DORA delivery signals, and qualitative reflection prompts. Use when Codex is asked for sprint reviews, team retrospectives, end-of-iteration coaching, or instructor/student retrospective summaries.
---

# Sprint Retrospective

## Purpose

Turn sprint evidence into coaching-oriented reflection and next-sprint experiments. Use DORA signals as discussion evidence, not grades.

## Required Inputs

- sprint window
- repository or repositories
- team or student mapping
- audience: student team, instructor, or both
- optional sprint goal or milestone

If an input is missing, ask for it. If the user wants a draft anyway, mark missing evidence as `unknown`.

## Evidence Sources

Use available evidence:

1. PRs, commits, issues, releases/tags, deployments, submissions, and CI checks.
2. DORA metric snippets from `student-dora-tracking` or the four metric skills.
3. User-provided qualitative notes, standup notes, sprint goals, or instructor feedback.

Keep evidence and interpretation separate.

## Student-Facing Retrospective

Use this mode for teams or individual students.

- Avoid rankings and grade-like language.
- Highlight what the team can control next sprint.
- Turn DORA signals into reflection prompts.
- Prefer a small number of concrete experiments.

```markdown
# Sprint Retrospective: <team/window>

## Sprint Evidence
- Delivery activity: <summary>
- Quality/recovery signals: <summary>
- Data caveats: <unknowns>

## What Worked
- <practice or outcome>

## What Got Stuck
- <bottleneck or friction>

## Discussion Prompts
- <prompt tied to evidence>
- <prompt tied to collaboration or delivery flow>

## Next-Sprint Experiments
| Experiment | Owner | How We Will Know It Helped |
|---|---|---|
```

## Instructor-Facing Retrospective

Use this mode for course staff or coaching plans.

- Summarize team patterns and intervention opportunities.
- Include evidence quality and caveats.
- Avoid grades unless the instructor supplies a rubric.
- Keep recommendations instructional and actionable.

```markdown
# Sprint Retrospective Summary: <course/project/window>

## Overview
- Teams reviewed: <count/list>
- Evidence quality: <high/medium/low plus reason>

## Patterns
- <positive pattern>
- <risk or bottleneck>

## Team Coaching Notes
| Team | Evidence Signal | Likely Need | Suggested Intervention |
|---|---|---|---|

## Caveats
- <missing data or attribution limits>
```

## Workflow

1. Confirm sprint window, repositories, team mapping, and audience.
2. Gather GitHub and qualitative evidence.
3. Pull DORA metric snippets only when they help explain delivery flow.
4. Choose student-facing or instructor-facing format.
5. Produce reflection prompts and next-sprint actions.
6. List caveats and unknowns.
