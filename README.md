# Agent Skill Productizer

[![Audit Skill](https://github.com/wrhy66/agent-skill-productizer/actions/workflows/audit.yml/badge.svg)](https://github.com/wrhy66/agent-skill-productizer/actions/workflows/audit.yml)
[![Release](https://img.shields.io/github/v/release/wrhy66/agent-skill-productizer)](https://github.com/wrhy66/agent-skill-productizer/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Turn repeatable prompts, SOPs, and niche workflows into installable AI agent skills with a GitHub-ready wrapper and a clean paid customization path.

Use it when you have a workflow that already works in chat, but is still trapped in scattered prompts, private notes, or a manual checklist.

## Custom Private Skill - 499 RMB

Have one repeated workflow you want packaged for your own business, repo, or team?

I can build a private installable agent skill for one narrow workflow:

- custom `SKILL.md`
- references, templates, or scripts when useful
- one revision round
- handoff instructions

Start here: [Custom Skill Request](https://github.com/wrhy66/agent-skill-productizer/issues/new?template=custom-skill-request.yml)

Payment is requested after the workflow scope is confirmed. Do not paste secrets or private customer data into public issues.

中文说明：[499 RMB 私有 Skill 定制](CUSTOM_SKILL_SERVICE.zh-CN.md)

## Fast Path

1. Copy `agent-skill-productizer/` into your Codex skills directory.
2. Start a new Codex thread.
3. Paste your repeated workflow and run:

```text
Use $agent-skill-productizer to turn this workflow into a publishable agent skill with a README and paid customization offer.
```

Want a private version for your own business workflow? Open a [Custom Skill Request](https://github.com/wrhy66/agent-skill-productizer/issues/new?template=custom-skill-request.yml). Starter price: 499 RMB for one narrow workflow.

## Who It Is For

Builders, operators, indie hackers, consultants, and teams who want to turn a repeated AI workflow into a reusable skill, open-source GitHub repo, lead magnet, or paid customization offer.

Good fits:

- weekly reports built from messy inputs
- code review, release, migration, or QA checklists
- customer support triage and product feedback summaries
- niche documents with a repeatable structure
- private SOPs that need safer agent execution

Poor fits:

- broad "do everything" assistants
- vague writing helpers
- spam, fake accounts, credential collection, or platform loopholes
- workflows where the output cannot be inspected

## What It Does

- Finds the narrowest useful skill promise around a real repeated job.
- Creates agent-facing `SKILL.md` instructions with progressive disclosure.
- Adds references, scripts, and launch templates only when they improve execution.
- Audits the skill for TODOs, metadata, missing files, and risky sales claims.
- Generates GitHub positioning, example copy, and launch assets for ethical distribution.

## Example Result

Input workflow:

```text
Every Friday, I turn messy customer feedback from support tickets into a product summary for the PM team.
```

Productized skill:

```text
feedback-triage-brief/
  SKILL.md
  references/severity-rubric.md
  assets/templates/weekly-brief.md
  examples/sanitized-feedback.md
```

Positioning:

```text
For product managers, this skill turns messy customer feedback into a weekly triage brief with themes, quotes, severity, and recommended actions.
```

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

## Examples

- [Example workflow](examples/example-workflow.md)
- [499 RMB private skill brief](examples/private-skill-brief.md)
- [Skill idea catalog](examples/skill-idea-catalog.md)
- [Launch and promotion copy](PROMOTION.md)
- [Custom skill service details](CUSTOM_SKILL_SERVICE.md)
- [499 RMB 中文定制说明](CUSTOM_SKILL_SERVICE.zh-CN.md)
- [Today sales sprint](TODAY_SALES_SPRINT.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

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

## Update Cadence

This project should stay visibly maintained without noisy fake momentum:

- weekly: examples, issue replies, copy improvements, and launch learnings
- monthly: small releases when there is a visible improvement
- quarterly: review pricing, scope, examples, and conversion path

See [Roadmap](ROADMAP.md) and [Changelog](CHANGELOG.md).

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

Best fit: a workflow with clear inputs, clear outputs, and at least one sanitized example.

Open a [Custom Skill Request](https://github.com/wrhy66/agent-skill-productizer/issues/new?template=custom-skill-request.yml) and describe the workflow you want to productize. See [Custom Skill Service](CUSTOM_SKILL_SERVICE.md) for scope and examples.

## License

MIT
