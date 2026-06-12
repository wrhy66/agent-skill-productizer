# 499 RMB Private Skill Brief

Use this example to show what a narrow paid customization request should look like.

## Customer Request

```text
I run a small SaaS. Every week I export support tickets and turn them into a product feedback summary for the PM.

Input:
- CSV export from support tool
- tags, customer plan, message text, created date

Output:
- weekly Markdown report
- top themes
- bugs vs feature requests
- severity
- representative quotes
- suggested product actions

Constraints:
- do not include customer names
- separate enterprise account issues
- flag any billing-related complaints
```

## Starter Scope

This fits the 499 RMB starter build because:

- the workflow is narrow
- the input and output are clear
- the buyer can provide a sanitized CSV sample
- the skill can run without private integrations

## Private Skill Deliverable

```text
support-feedback-brief/
  SKILL.md
  references/severity-rubric.md
  references/privacy-rules.md
  assets/templates/weekly-feedback-brief.md
```

## Upgrade Options

Possible larger follow-up work:

- script to normalize CSV exports
- Linear or Jira handoff template
- team-specific product area taxonomy
- monthly maintenance as tags and product areas change

