---
name: dora-change-failure-rate
description: Calculates change failure rate for student software projects using failed CI, failed deployments, reverts, bug issues, reopened issues, or instructor-labeled regressions. Use when Codex needs the DORA change failure metric or a reliability signal for course repositories.
---

# DORA Change Failure Rate

## Definition

Measure the share of delivered changes that caused credible failure evidence during the selected date range.

## Required Evidence

- delivered changes for the date range
- failure evidence linked to those changes
- team or student mapping
- known flaky CI or instructor-created activity, if available

## GitHub Proxy Order

Failure evidence includes:

1. Failed deployment or publish workflow caused by the change.
2. Merged change followed by a revert.
3. Bug issue linked to the change.
4. Reopened issue tied to the change.
5. Instructor-labeled regression.
6. CI failure that blocks or invalidates the submitted change.

Count failures only when evidence plausibly ties the failure to the delivered change.

## Missing Data

- If delivered changes are known but failure evidence is unavailable, report failure data quality as low.
- Do not count unrelated flaky CI as a change failure.
- Do not assume no failures just because issues are absent.

## Student Caveats

- Student teams may underreport bugs or use issues inconsistently.
- Early failures can be productive learning signals.
- Avoid punitive language; describe reliability patterns and next practices.

## Output Snippet

```markdown
### Change Failure Rate
- Result: <percentage or unknown>
- Failed changes: <count>
- Delivered changes: <count>
- Evidence used: <CI/reverts/issues/regressions>
- Caveats: <missing data or failure attribution context>
```
