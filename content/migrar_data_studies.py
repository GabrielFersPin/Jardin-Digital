#!/usr/bin/env python3
"""Migrate learning-note metadata and sections inside Data Studies.

The migration is additive: note bodies are preserved and existing frontmatter
values are not replaced. Run without --apply to preview the affected files.
"""

import argparse
import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "Data Studies"
APPLICATION = """\n\n## 🧪 Aplicación\n\n- [ ] Explicarlo sin consultar la nota\n- [ ] Resolver un caso nuevo o escribir un ejemplo\n- [ ] Compararlo con una alternativa\n- [ ] Usarlo en un proyecto\n"""
CONNECTIONS = """\n## 🔗 Conexiones explicadas\n\n- [[ ]] — Se relaciona porque...\n"""


def frontmatter_bounds(lines):
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return 0, index
    return None


def fields(lines):
    result = {}
    for line in lines:
        match = re.match(r"^([^:#][^:]*):\s*(.*)$", line.rstrip("\n"))
        if match:
            result[match.group(1).strip()] = match.group(2).strip()
    return result


def empty(value):
    return value is None or value.strip().strip('"\'') in {"", "null"}


def add_field(frontmatter, key, value):
    if not any(line.startswith(f"{key}:") for line in frontmatter):
        frontmatter.insert(-1, f"{key}: {value}\n")
        return True
    return False


def migrate(path: Path, apply: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    if path.name.lower().startswith("dashboard"):
        return False
    bounds = frontmatter_bounds(lines)
    if not bounds:
        return False

    start, end = bounds
    frontmatter = lines[start : end + 1]
    metadata = fields(frontmatter[1:-1])
    tipo = metadata.get("tipo_nota", "").strip().strip('"\'')
    if tipo in {"dashboard-general", "dashboard-area", "dashboard-asignatura", "hub"}:
        return False
    if "excalidraw-plugin: parsed" in original[:1000]:
        return False

    changed = False
    if empty(metadata.get("tipo_nota")):
        changed |= add_field(frontmatter, "tipo_nota", "tecnica")

    if empty(metadata.get("area")) and not empty(metadata.get("asignatura")):
        changed |= add_field(frontmatter, "area", metadata["asignatura"])

    if empty(metadata.get("proxima-revision")):
        legacy_date = metadata.get("proxima_revision")
        if not empty(legacy_date):
            changed |= add_field(frontmatter, "proxima-revision", legacy_date)
        else:
            days = metadata.get("dias-para-revision")
            if days and re.fullmatch(r"-?\d+", days.strip()):
                date = dt.date.today() + dt.timedelta(days=int(days))
                changed |= add_field(frontmatter, "proxima-revision", date.isoformat())

    changed |= add_field(frontmatter, "resultado-repaso", '""')
    changed |= add_field(frontmatter, "intervalo-dias", "7")
    changed |= add_field(frontmatter, "prioridad", '"media"')

    body = "".join(lines[end + 1 :])
    if "## 🧪 Aplicación" not in body:
        body += APPLICATION
        changed = True
    if "## 🔗 Conexiones explicadas" not in body:
        body += CONNECTIONS
        changed = True

    if changed and apply:
        path.write_text("".join(frontmatter) + body, encoding="utf-8")
    return changed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the migration")
    args = parser.parse_args()

    affected = []
    for path in sorted(ROOT.rglob("*.md")):
        if migrate(path, args.apply):
            affected.append(path.relative_to(ROOT))

    mode = "migrated" if args.apply else "would migrate"
    print(f"{mode}: {len(affected)} notes")
    for path in affected:
        print(path)


if __name__ == "__main__":
    main()