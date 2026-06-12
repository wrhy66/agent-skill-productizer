---
name: agent-skill-productizer
description: Turn repeatable prompts, workflows, SOPs, automations, or niche expertise into publishable AI agent skills. Use when Codex needs to design, create, audit, package, or launch a GitHub-ready skill with SKILL.md, progressive-disclosure references, reusable scripts/assets, README positioning, launch copy, and monetization paths.
---

# Agent Skill Productizer

## Workflow

Use this skill to convert a useful repeatable workflow into a small, installable agent skill that can be shared on GitHub and used as a lead magnet for paid templates, consulting, or private versions.

Follow this order:

1. Define the buyer/user and the repeated job.
2. Choose the narrowest useful skill promise.
3. Design the skill folder with progressive disclosure.
4. Write `SKILL.md` for agents, not humans.
5. Add only resources that make execution more reliable.
6. Audit the skill with `scripts/audit_skill.py`.
7. Package the GitHub launch materials from `assets/templates/`.

## Product Strategy

Prefer skills that save a buyer time on urgent, repeated, high-friction work:

- turning messy inputs into polished deliverables
- checking fragile release or compliance steps
- producing niche documents, reports, tests, migrations, or launch assets
- coordinating tools where the exact sequence matters
- embedding a practitioner's private checklist into an agent workflow

Reject vague skills such as "better writing" or "business helper." Narrow them until the output, trigger, and buyer are obvious.

Use this positioning formula:

```text
For [specific user], this skill turns [messy input] into [valuable output] using [workflow/resources] so they can [urgent outcome].
```

## Skill Structure

Create a standard skill folder:

```text
skill-name/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
  assets/
```

Only keep resource directories that are actually used. Keep `SKILL.md` short and procedural. Put detailed examples, templates, scoring rubrics, and launch material in references or assets.

Use references when the agent may need to read detailed guidance. Use scripts when repeated checks or transformations should be deterministic. Use assets when the agent should copy a template into the user's final output.

## Creation Steps

### 1. Extract The Repeatable Job

Ask or infer:

- Who uses this?
- What input do they start with?
- What output should the agent produce?
- What mistakes should the skill prevent?
- What parts are deterministic enough for scripts?
- What examples prove the skill works?

If the user wants revenue, choose an offer with a paid upgrade path:

```text
Free GitHub skill -> paid template pack -> custom private skill -> implementation service
```

### 2. Name And Trigger

Use lowercase hyphen-case under 64 characters. Prefer verb-led names:

```text
productize-skill
audit-launch-page
gh-release-brief
convert-sop-to-skill
```

Write the frontmatter `description` with both capability and triggers. Include file types, contexts, and tasks that should invoke the skill.

### 3. Write The Agent Instructions

In `SKILL.md`, use imperative workflow guidance. Avoid marketing copy. Include:

- decision steps
- do/don't rules
- exact resource routing
- validation commands
- output expectations

Do not include long explanations the model already knows.

### 4. Add Launch Materials

When making a GitHub-ready package, copy and fill:

- `assets/templates/github-readme.md`
- `assets/templates/launch-posts.md`
- `assets/templates/paid-upgrade-map.md`

These templates are for the repository wrapper, not for the skill folder itself.

### 5. Audit

Run:

```bash
python scripts/audit_skill.py <path-to-skill-or-repo>
```

Fix all `fail` items. Treat `warn` items as launch quality improvements.

## Resource Routing

Read `references/productization.md` when choosing the niche, offer, launch angle, or paid upgrade path.

Read `references/skill-quality.md` when writing or reviewing `SKILL.md`, references, scripts, and assets.

Use `scripts/audit_skill.py` before calling the skill ready.

Copy templates from `assets/templates/` when the user asks for GitHub publishing, launch copy, or monetization material.

## Revenue-Safe Rules

Do not promise guaranteed revenue, rankings, stars, or sales.

Do not create fake testimonials, fake usage numbers, fake screenshots, or fake endorsements.

Do not add dark patterns, credential harvesting, platform spam, or misleading install instructions.

Make the free skill useful on its own. Paid offers may add convenience, private customization, templates, or implementation time, but not artificial lock-in.

