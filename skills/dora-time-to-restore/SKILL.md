---
name: dora-time-to-restore
description: Calculates time to restore service or recover from failures in student software projects using failed checks, bug issues, reverts, fixing commits, passing CI, or redeployments. Use when Codex needs the DORA restore-time metric or recovery signal for course repositories.
---

# DORA Time To Restore

## Definition

Measure elapsed time from first credible failure signal to recovery.

## Required Evidence

- failure timestamp
- recovery timestamp
- linked issue, PR, commit, check run, or deployment evidence
- team or student mapping

## GitHub Proxy Order

Failure start:

1. Failed deployment or check timestamp.
2. Bug issue open time.
3. Instructor regression report time.
4. Revert target commit time when no earlier signal exists.

Recovery end:

1. Fixing PR merge time.
2. Fixing commit time.
3. Passing deployment or check time.
4. Bug issue close time.

## Missing Data

- If either timestamp is missing, report `unknown`.
- If a failure is still open, report it as unresolved instead of estimating recovery.
- Do not treat the sprint end as recovery unless the repository evidence shows recovery happened then.

## Student Caveats

- Some course projects do not operate live services, so recovery may mean restoring a passing build or acceptable submission state.
- Students may fix issues without linking commits and issues; note weak linkage.
- Compare recovery patterns cautiously across teams with different project complexity.

## Output Snippet

```markdown
### Time To Restore
- Median: <duration or unknown>
- Average: <duration or unknown>
- Unresolved failures: <count>
- Evidence used: <checks/issues/commits/deployments>
- Caveats: <missing data or recovery-definition context>
```
