---
name: student-dora-tracking
description: Measures and reports DORA-style delivery metrics for student software projects. Use when instructors or course staff ask Codex to track deployment frequency, lead time, change failure rate, time to restore, or delivery health across student GitHub repositories, teams, or submissions.
---

# Student DORA Tracking

## Purpose

Measure DORA-inspired delivery patterns for student projects using GitHub evidence. Keep the report fair, transparent, and instructional. Do not invent missing data and do not convert metrics into grades unless the instructor supplies a grading rubric.

## Required Inputs

Before calculating metrics, identify:

- repository list
- date range or course milestone window
- student/team mapping
- deployment definition for the course

If an input is missing, ask for it. If the user wants a draft without complete data, mark unknown fields as `unknown` and list the missing input in the caveats.

## GitHub Data Sources

Use available GitHub evidence in this order:

1. Pull requests, including open time, merge time, reviewers, labels, and linked issues.
2. Commits, including author, timestamp, branch, and commit message.
3. Releases and tags.
4. GitHub Actions or other CI check runs.
5. Issues, including bug labels, reopen events, close times, and links to PRs.

Record which sources were available. Do not assume a repository uses PRs, releases, tags, or CI unless the data confirms it.

## Metric Skills

Use the metric-specific skills for calculations and evidence rules:

- `dora-deployment-frequency`: delivery cadence using releases, tags, deployments, merged PRs, or default-branch commits.
- `dora-lead-time-for-changes`: elapsed time from change start to delivery.
- `dora-change-failure-rate`: delivered changes with credible failure evidence divided by total delivered changes.
- `dora-time-to-restore`: elapsed time from first failure signal to recovery.

When producing a full DORA report, gather the shared inputs once, apply each metric skill with the same repository list, date range, and team mapping, then assemble the metric snippets into the final report. If a user asks for only one metric, use the specific metric skill and do not force a full report.

## Fairness Rules

- Treat missing data as `unknown`, not zero.
- Separate team-level observations from individual contribution claims.
- Flag small sample sizes instead of ranking teams aggressively.
- Flag shared machines, shared accounts, pair programming, uneven PR usage, and instructor-created commits.
- Avoid punitive wording. Frame findings as coaching signals and workflow evidence.

## Output Modes

Choose the output mode from the user's role or request.

### Instructor Report

Use this mode for course staff, grading support, milestone reviews, team comparisons, or intervention planning.

- Compare teams cautiously and include sample sizes.
- Include evidence links or identifiers.
- Highlight data quality, fairness caveats, and likely workflow bottlenecks.
- Recommend instructional interventions, not grades or penalties.

### Student Report

Use this mode for students, teams, retrospectives, or coaching.

- Avoid rankings across students or teams unless the instructor explicitly asks for them.
- Focus on actionable workflow habits: smaller PRs, earlier integration, clearer issue links, CI repair, and release/submission discipline.
- Explain DORA metrics as signals, not judgments.
- Keep sensitive instructor-only comparisons and rubric interpretation out of the student version unless explicitly requested.

## Report Format

Use this structure for instructor reports:

```markdown
# Student DORA Report: <course/project/window>

## Summary
- Repositories analyzed: <count/list>
- Date range: <range>
- Deployment proxy: <proxy>
- Data quality: <high/medium/low plus reason>

## Metrics By Team
| Team | Deployments | Lead Time Median | Lead Time Avg | Change Failure Rate | Time To Restore Median | Caveats |
|---|---:|---:|---:|---:|---:|---|

## Observations
- <delivery pattern>
- <risk or bottleneck>
- <positive practice>

## Suggested Interventions
- <coaching action>
- <process adjustment>

## Assumptions And Caveats
- <proxy and missing data notes>

## Evidence
- <links or identifiers for PRs, releases, issues, and workflows>
```

Use this structure for student reports:

```markdown
# Team Delivery Check-in: <project/window>

## Summary
- Date range: <range>
- Delivery proxy: <proxy>
- Data quality: <high/medium/low plus reason>

## Your Delivery Signals
| Metric | Result | What It Suggests | Next Step |
|---|---:|---|---|

## What Is Working
- <positive practice>

## What To Improve Next
- <coaching action>
- <process adjustment>

## Assumptions And Caveats
- <proxy and missing data notes>
```

## Workflow

1. Confirm inputs and date range.
2. Inspect GitHub evidence for each repository.
3. Use the four metric skills to calculate deployment frequency, lead time for changes, change failure rate, and time to restore.
4. Choose instructor or student output mode.
5. Compare patterns cautiously and include sample sizes when comparisons are appropriate.
6. Produce the report using the selected format.
7. List unknowns and recommend what data would improve the next report.
