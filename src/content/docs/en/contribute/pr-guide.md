---
title: PR Guide
description: Step-by-step guide from creating a pull request to merge
---

## PR Checklist

Before submitting a PR, verify the following:

- [ ] `pnpm run build` completes successfully
- [ ] No Markdown syntax errors
- [ ] Spelling and grammar reviewed
- [ ] Image/link paths verified to work
- [ ] For assignment submissions: confirm path is `assignments/[lab/week]-XX/[student-id]/`

## Commit Message Convention

```
<type>: <description>

# Examples
feat: add HOTL diagram to Week 1 lecture notes
fix: fix MIG code example error in Week 3
docs: clarify Lab 04 submission requirements
chore: update dependencies
```

**Types**:
- `feat`: New content added
- `fix`: Error corrected
- `docs`: Documentation improved
- `style`: Formatting change (no content change)
- `chore`: Other maintenance tasks

## Assignment Submission PR

```
# PR title format
[Submit] Lab 04 - 20230001 Hong Gildong

# PR body example
## Submission Contents
- harness.sh implementation (ralph loop + backpressure)
- PROMPT.md written (3 tasks)
- pytest-based test suite

## Execution Results
- Loop log showing success after 2 failures attached
- Garbage collection behavior confirmed
```

## Review Process

1. PR created → GitHub Actions automated build check
2. Build passes → instructor/peer review
3. Review approved → merge → automatic deployment

## Responding to Review Comments

When a reviewer requests changes:

```bash
# After making fixes
git add .
git commit -m "fix: address review - fix XXX"
git push origin [branch-name]
# PR updates automatically
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Build fails | Run `pnpm run build` locally and check errors |
| Branch is behind main | Run `git pull upstream main` then rebase |
| Wrong assignment path | Re-check `assignments/lab-XX/[student-id]/` format |
