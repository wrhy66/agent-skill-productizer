#!/usr/bin/env python3
"""Audit an agent skill or GitHub skill repo for release readiness."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_skill_root(path: Path) -> Path | None:
    if (path / "SKILL.md").exists():
        return path
    matches = list(path.glob("*/SKILL.md"))
    if len(matches) == 1:
        return matches[0].parent
    skill_dirs = [p.parent for p in path.rglob("SKILL.md") if ".git" not in p.parts]
    if len(skill_dirs) == 1:
        return skill_dirs[0]
    return None


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            data[f"invalid:{line}"] = ""
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def result(status: str, item: str, detail: str) -> dict[str, str]:
    return {"status": status, "item": item, "detail": detail}


def audit(path: Path) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    skill_root = find_skill_root(path)
    if not skill_root:
        return [result("fail", "skill-root", "Could not find exactly one SKILL.md")]

    skill_text = read_text(skill_root / "SKILL.md")
    frontmatter, body = parse_frontmatter(skill_text)
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    out.append(result("pass", "skill-root", str(skill_root)))

    if set(frontmatter.keys()) == {"name", "description"}:
        out.append(result("pass", "frontmatter-keys", "Only name and description are present"))
    else:
        out.append(result("fail", "frontmatter-keys", f"Found keys: {sorted(frontmatter.keys())}"))

    if NAME_RE.match(name):
        out.append(result("pass", "name", name))
    else:
        out.append(result("fail", "name", "Name must be lowercase hyphen-case and under 64 chars"))

    if len(description.split()) >= 18 and "use" in description.lower():
        out.append(result("pass", "description", "Description includes capability and trigger language"))
    else:
        out.append(result("warn", "description", "Description may be too short or missing trigger language"))

    if "TODO" in skill_text or "[TODO" in skill_text:
        out.append(result("fail", "todos", "TODO placeholder remains"))
    else:
        out.append(result("pass", "todos", "No TODO placeholders found"))

    line_count = len(skill_text.splitlines())
    if line_count <= 500:
        out.append(result("pass", "skill-length", f"{line_count} lines"))
    else:
        out.append(result("warn", "skill-length", f"{line_count} lines; consider references"))

    openai_yaml = skill_root / "agents" / "openai.yaml"
    if openai_yaml.exists():
        yaml_text = read_text(openai_yaml)
        if f"${name}" in yaml_text:
            out.append(result("pass", "openai-default-prompt", f"Mentions ${name}"))
        else:
            out.append(result("warn", "openai-default-prompt", f"Default prompt should mention ${name}"))
    else:
        out.append(result("warn", "openai-yaml", "agents/openai.yaml missing"))

    referenced = sorted(set(re.findall(r"`((?:references|scripts|assets)/[^`]+)`", skill_text)))
    for rel in referenced:
        if (skill_root / rel).exists():
            out.append(result("pass", f"reference:{rel}", "Exists"))
        else:
            out.append(result("fail", f"reference:{rel}", "Referenced file is missing"))

    for script in (skill_root / "scripts").glob("*.py") if (skill_root / "scripts").exists() else []:
        text = read_text(script)
        if "__main__" in text:
            out.append(result("pass", f"script:{script.name}", "Has CLI entrypoint"))
        else:
            out.append(result("warn", f"script:{script.name}", "No CLI entrypoint found"))

    repo_readme = path / "README.md"
    if repo_readme.exists():
        readme = read_text(repo_readme)
        if name in readme and "Install" in readme:
            out.append(result("pass", "repo-readme", "README includes skill name and install section"))
        else:
            out.append(result("warn", "repo-readme", "README should include skill name and install section"))
    else:
        out.append(result("warn", "repo-readme", "No repository README found"))

    banned_claims = [
        "we guarantee revenue",
        "we guarantee sales",
        "guaranteed $",
        "guaranteed income",
        "guaranteed profit",
        "guaranteed sales outcome",
    ]
    combined = skill_text.lower()
    if repo_readme.exists():
        combined += "\n" + read_text(repo_readme).lower()
    if any(claim in combined for claim in banned_claims):
        out.append(result("fail", "claims", "Remove guaranteed revenue or sales claims"))
    else:
        out.append(result("pass", "claims", "No obvious guaranteed-sales claims found"))

    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    rows = audit(Path(args.path).resolve())
    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        for row in rows:
            print(f"{row['status'].upper():5} {row['item']}: {row['detail']}")

    return 1 if any(row["status"] == "fail" for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())
