---
title: How to Contribute
description: How to contribute to this course site — Fork, edit, and PR guide
---

## Contribution Guide

All content on this site is managed on GitHub. Your contributions make the course better!

## What You Can Contribute

- **Fix errors**: Correct typos and code mistakes in lecture content
- **Improve explanations**: Add clarifications to unclear concepts
- **Share lab tips**: Share your troubleshooting experiences
- **Add references**: Link useful papers and blogs
- **Submit assignments**: PR your assignment to the `assignments/` folder

## Quick Start

```bash
# 1. Fork on GitHub (Fork button in the top-right)

# 2. Clone locally
git clone https://github.com/[YOUR_USERNAME]/ai-systems-2026.git
cd ai-systems-2026

# 3. Install dependencies
pnpm install

# 4. Run development server
pnpm run dev
# → http://localhost:4321

# 5. Verify build after changes (required before PR!)
pnpm run build
```

## Creating a PR

```bash
# Create a new branch
git checkout -b fix/week-03-typo

# Commit after making changes
git add .
git commit -m "fix: fix typo in Week 3 MIG description"

# Push
git push origin fix/week-03-typo

# Create PR on GitHub
```

## Further Reading

- [PR Guide](/en/contribute/pr-guide) — PR checklist and review process
- [Content Style Guide](/en/contribute/content-style) — Rules for writing course materials
