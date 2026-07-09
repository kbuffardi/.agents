---
name: dora-lead-time-for-changes
description: Calculates lead time for changes in student software projects using GitHub PRs, commits, releases, tags, deployments, or submissions. Use when Codex needs the DORA lead time metric or wants to understand how long work takes from start to delivery.
---

# DORA Lead Time For Changes

## Definition

Measure elapsed time from change start to delivery during the selected date range.

## Required Evidence

- repository
- date range
- team or student mapping
- change start timestamp
- delivery timestamp

## GitHub Proxy Order

Start timestamp:

1. PR open time when PRs are used.
2. First commit timestamp in the delivered change.
3. Issue start time only when commits or PRs cannot establish a start point.

End timestamp:

1. PR merge time.
2. Release or tag time.
3. Successful deployment or publish workflow time.
4. Final default-branch commit time for direct-push workflows.

## Missing Data

- If either timestamp is missing, report that change as `unknown`.
- Do not substitute the analysis time, issue close time, or sprint deadline unless the course explicitly defines that as delivery.
- Report sample size so unknowns do not disappear from the interpretation.

## Student Caveats

- Long-running branches may reflect learning, review delays, or unclear requirements rather than low effort.
- Pair programming and shared commits can blur individual attribution.
- Prefer median plus range over a single average.

## Output Snippet

```markdown
### Lead Time For Changes
- Median: <duration or unknown>
- Average: <duration or unknown>
- Fastest / slowest: <durations>
- Sample size: <known>/<total changes>
- Caveats: <missing data or workflow context>
```
