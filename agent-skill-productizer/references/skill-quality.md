# Skill Quality Reference

Use this reference when reviewing a skill before publishing.

## Agent-Facing Quality

A good skill:

- triggers only for the right tasks
- contains a specific frontmatter description
- keeps `SKILL.md` concise
- tells the agent which resource to read and when
- avoids generic advice
- has deterministic scripts for fragile repeated checks
- includes examples only when they change behavior
- validates with a command or checklist

## Progressive Disclosure

Keep the core workflow in `SKILL.md`. Move optional or detailed material into:

- `references/` for guidance the agent may read
- `scripts/` for repeatable automation
- `assets/` for templates copied into outputs

Avoid deeply nested references. Link directly from `SKILL.md`.

## Human-Facing GitHub Quality

The repository wrapper may include a README, license, examples, and launch material. The skill folder itself should stay focused.

README checklist:

- clear one-sentence promise
- installation or copy instructions
- example user prompt
- example output summary
- folder structure
- license
- paid/customization note if relevant

## Validation Checklist

Before launch:

- `SKILL.md` has valid YAML frontmatter
- frontmatter has only `name` and `description`
- skill name is lowercase hyphen-case
- no TODO placeholders remain
- `agents/openai.yaml` default prompt mentions `$skill-name`
- every referenced file exists
- scripts run successfully
- examples do not contain private or fake claims
- monetization copy avoids guaranteed earnings

