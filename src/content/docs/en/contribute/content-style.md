---
title: Content Style Guide
description: Rules for writing course materials — MDX component usage and writing principles
---

## Writing Principles

1. **Clarity first**: Explain complex concepts accessibly
2. **Code examples required**: Always follow theoretical explanations with code examples
3. **English throughout**: Technical terms remain in English
4. **Keep it concise**: Remove unnecessary explanations

## Starlight Component Usage

### Aside (Callout)

```mdx
import { Aside } from '@astrojs/starlight/components';

<Aside type="note" title="Note">Notes or additional information</Aside>
<Aside type="tip" title="Tip">Useful tips</Aside>
<Aside type="caution" title="Caution">Warnings</Aside>
<Aside type="danger" title="Danger">Dangerous content</Aside>
```

### Steps (Step-by-step procedure)

```mdx
import { Steps } from '@astrojs/starlight/components';

<Steps>
1. **First step** — description
2. **Second step** — description
</Steps>
```

### Tabs

```mdx
import { Tabs, TabItem } from '@astrojs/starlight/components';

<Tabs>
  <TabItem label="macOS">macOS content</TabItem>
  <TabItem label="Linux">Linux content</TabItem>
</Tabs>
```

### Card & CardGrid

```mdx
import { Card, CardGrid } from '@astrojs/starlight/components';

<CardGrid>
  <Card title="Card Title" icon="rocket">Card content</Card>
</CardGrid>
```

## Weekly Lecture Note Template

```mdx
---
title: "Week N: Title"
description: Description
week: N
phase: 1|2|3|4|5
phase_title: Phase Name
date: "YYYY-MM-DD"
theory_topics: ["Topic 1", "Topic 2"]
lab_topics: ["Lab 1"]
assignment: "Lab XX: Assignment Name"
assignment_due: "YYYY-MM-DD"
difficulty: beginner|elementary|intermediate|advanced
estimated_time: Xh
---

## Theory
...

## Practicum
...

## Assignment

<div class="assignment-box">
### Lab XX: Title
**Due**: YYYY-MM-DD
...
</div>
```

## Code Block Rules

- Always specify language: ` ```python `, ` ```bash `, ` ```json `, etc.
- Use runnable example code
- Comments may be written in English

## Prohibited

- Reproducing copyrighted material without permission
- Unverified code examples
- Excessive emoji usage
