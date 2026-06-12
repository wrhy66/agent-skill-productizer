# Agent Skill Productizer

Turn repeatable prompts, SOPs, and niche workflows into GitHub-ready AI agent skills.

This repository contains an installable `agent-skill-productizer` skill plus launch templates for publishing useful agent skills without making fake income claims or bloated prompt packs.

## Who It Is For

Builders who want to turn a repeatable AI workflow into a reusable skill, open-source GitHub repo, lead magnet, or paid customization offer.

## What It Does

- Designs a narrow, useful agent skill around a real repeated job.
- Creates agent-facing `SKILL.md` instructions with progressive disclosure.
- Adds references, scripts, and launch templates only when they improve execution.
- Audits the skill for TODOs, metadata, missing files, and risky sales claims.
- Generates GitHub positioning and launch copy for ethical distribution.

## Example Prompt

```text
Use $agent-skill-productizer to turn my customer-support refund SOP into a publishable agent skill with a GitHub README and paid customization offer.
```

## Install

Copy the `agent-skill-productizer/` folder into your Codex skills directory.

Typical location:

```text
~/.codex/skills/agent-skill-productizer
```

Then start a new Codex thread and invoke:

```text
Use $agent-skill-productizer to productize this workflow...
```

## Repository Structure

```text
agent-skill-productizer/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
  assets/templates/
examples/
  example-workflow.md
LAUNCH.md
```

## Audit

Run:

```bash
python agent-skill-productizer/scripts/audit_skill.py .
```

## Monetization

The free skill is useful as-is. Paid work can include private workflow customization, setup help, niche example packs, integration scripts, or team training.

No revenue, ranking, stars, traffic, or sales outcome is guaranteed.

## Custom Private Skill

Want this adapted to your own workflow?

I can turn one repeatable business or coding workflow into a private agent skill:

- workflow interview
- installable skill folder
- custom `SKILL.md`
- references, templates, or scripts as needed
- one revision round
- handoff instructions

Starter price: 499 RMB for one narrow workflow.

Open a [Custom Skill Request](../../issues/new?template=custom-skill-request.yml) and describe the workflow you want to productize.

## License

MIT
