#!/usr/bin/env python3
"""Regenerate the public example mirror from the private GitLab examples repository.

The exercise texts are written in ``codeability/development/examples`` on
gitlab.tugraz.at. This script copies the learner-facing part of every example
named in ``courses/*.yaml`` from a given commit of a local checkout of that
repository, then rewrites ``RIGHTS.md``, ``LANGUAGE_AUDIT.md`` and the
provenance paragraph of ``README.md`` so that they name the source commit.

Only these files are published (see ``public_files``):

* ``content/**`` (exercise texts and media),
* ``studentTemplates/**`` (starter code),
* top-level files listed in ``properties.additionalFiles`` (input data),
* ``meta.yaml`` without grading properties.

Solutions, ``localTests``, ``test.yaml``, submission and test files and every
file whose name contains "solution" stay private.

Usage::

    python scripts/refresh_from_examples.py --source ~/code/codeability/examples --ref main
    python scripts/refresh_from_examples.py --source ... --ref main --check   # exit 1 if stale
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "git@gitlab.tugraz.at:codeability/development/examples.git"
COMMIT_URL = "https://gitlab.tugraz.at/codeability/development/examples/-/commit/{sha}"
SOURCE_PREFIX = "python"
MIRROR_DIR = Path("examples") / SOURCE_PREFIX

PUBLIC_DIRS = ("content", "studentTemplates")
PUBLIC_PROPERTIES = ("additionalFiles", "studentTemplates")
PRIVATE_PROPERTIES = ("studentSubmissionFiles", "testFiles")
SOLUTION_NAME = re.compile(r"solution", re.IGNORECASE)


@dataclass(frozen=True)
class SourceCommit:
    sha: str
    date: str
    subject: str


def course_identifiers(root: Path = ROOT) -> list[str]:
    """Every example identifier used by a course manifest, in manifest order."""
    found: list[str] = []

    def walk(nodes):
        for node in nodes:
            identifier = node.get("example_identifier")
            if identifier and identifier not in found:
                found.append(identifier)
            walk(node.get("contents", []))

    for manifest in sorted((root / "courses").glob("*.yaml")):
        walk(yaml.safe_load(manifest.read_text(encoding="utf-8"))["contents"])
    return found


def is_private_name(relative: str) -> bool:
    return any(SOLUTION_NAME.search(part) for part in Path(relative).parts)


def private_names(properties: dict) -> set[str]:
    """File names that hold reference solutions or tests."""
    return {
        str(name).split("/")[-1]
        for key in PRIVATE_PROPERTIES
        for name in properties.get(key) or []
    }


def public_meta(meta: dict) -> dict:
    """meta.yaml without grading details; only public file lists remain."""
    public = {key: value for key, value in meta.items() if key != "properties"}
    properties = meta.get("properties") or {}
    private = private_names(properties)
    kept = {}
    for key in PUBLIC_PROPERTIES:
        files = [
            name for name in properties.get(key) or []
            if not is_private_name(name) and (key != "additionalFiles" or name not in private)
        ]
        if files:
            kept[key] = files
    if kept:
        public["properties"] = kept
    return public


def public_files(example: Path, meta: dict) -> list[str]:
    """Relative paths of the files of one example that may be published."""
    properties = meta.get("properties") or {}
    private = private_names(properties)
    selected = []
    for directory in PUBLIC_DIRS:
        base = example / directory
        if base.is_dir():
            for path in sorted(base.rglob("*")):
                if path.is_file():
                    selected.append(path.relative_to(example).as_posix())
    for name in properties.get("additionalFiles") or []:
        if (example / name).is_file():
            selected.append(Path(name).as_posix())
    result = []
    for relative in dict.fromkeys(selected):
        parts = Path(relative).parts
        if "localTests" in parts or is_private_name(relative):
            continue
        if parts[0] not in PUBLIC_DIRS and parts[-1] in private:
            continue
        result.append(relative)
    return result


def dump_meta(meta: dict) -> str:
    return yaml.safe_dump(meta, sort_keys=False, allow_unicode=True)


def source_commit(source: Path, ref: str) -> SourceCommit:
    out = subprocess.run(
        ["git", "-C", str(source), "show", "-s", "--format=%H%n%cI%n%s", f"{ref}^{{commit}}"],
        check=True, capture_output=True, text=True,
    ).stdout.splitlines()
    return SourceCommit(out[0], out[1], out[2])


def export_tree(source: Path, sha: str, target: Path) -> Path:
    archive = subprocess.run(
        ["git", "-C", str(source), "archive", "--format=tar", sha, SOURCE_PREFIX],
        check=True, capture_output=True,
    ).stdout
    subprocess.run(["tar", "-x", "-C", str(target)], input=archive, check=True)
    return target / SOURCE_PREFIX


def author_names(people) -> str:
    return ", ".join(person["name"] for person in people or [])


def rights_ledger(metas: dict[str, dict], commit: SourceCommit) -> str:
    lines = [
        "# Rights and provenance ledger",
        "",
        f"Source: `{SOURCE_URL}` commit `{commit.sha}`.",
        "",
        "| Example | License | Authors | Maintainers |",
        "| --- | --- | --- | --- |",
    ]
    for identifier in sorted(metas):
        meta = metas[identifier]
        lines.append(
            f"| `{identifier}` | `{meta.get('license')}` | {author_names(meta.get('authors'))}"
            f" | {author_names(meta.get('maintainers'))} |"
        )
    lines += [
        "",
        "The public mirror contains no `localTests`, instructor/reference solution files, or "
        "solution-named media. Per-example metadata remains authoritative for attribution and license.",
    ]
    return "\n".join(lines) + "\n"


def language_audit(mirror: Path, identifiers: list[str]) -> str:
    total = len(identifiers)

    def count(predicate) -> int:
        return sum(1 for identifier in identifiers if predicate(mirror / identifier))

    def meta(folder: Path) -> dict:
        return yaml.safe_load((folder / "meta.yaml").read_text(encoding="utf-8"))

    def clean(folder: Path) -> bool:
        return not any(
            "localTests" in path.parts or is_private_name(path.name) or path.name == "test.yaml"
            for path in folder.rglob("*")
        )

    german = count(lambda f: meta(f).get("language") == "de")
    de_text = count(lambda f: (f / "content" / "index_de.md").is_file())
    en_text = count(lambda f: (f / "content" / "index_en.md").is_file())
    mit = count(lambda f: meta(f).get("license") == "MIT")
    return (
        "# Sprach- und OER-Prüfung / Language and OER audit\n\n"
        f"- Python-Beispiele / Python examples: **{total}/{total}**\n"
        f"- `meta.yaml` mit `language: de` / German source metadata: **{german}/{total}**\n"
        f"- Deutsche Aufgaben / German exercise text (`index_de.md`): **{de_text}/{total}**\n"
        f"- Englische Aufgaben / English exercise text (`index_en.md`): **{en_text}/{total}**\n"
        f"- MIT metadata declarations: **{mit}/{total}**\n"
        f"- Keine Lösungs-/Testartefakte / no solution or test artifacts: **{count(clean)}/{total}**\n\n"
        "German is the content source of truth for this release; English is the maintained translation. "
        "The backend upload package is intentionally separate because it must retain private tests and "
        "reference solutions for automated grading.\n"
    )


PROVENANCE = re.compile(r"The source snapshot is\n.*?\)\. Each example", re.S)


def readme_with_provenance(readme: str, commit: SourceCommit, total: int) -> str:
    url = COMMIT_URL.format(sha=commit.sha)
    block = (
        "The source snapshot is\n"
        f"`{SOURCE_URL}` at\n"
        f"[`{commit.sha}`]({url})\n"
        f"({commit.date}; “{commit.subject}”). Each example"
    )
    updated, replaced = PROVENANCE.subn(lambda _: block, readme)
    if replaced != 1:
        raise SystemExit("README.md: provenance paragraph not found")
    return re.sub(r"declares MIT for all \d+ Python examples",
                  f"declares MIT for all {total} Python examples", updated)


def build(source_tree: Path, commit: SourceCommit, root: Path, out: Path) -> None:
    """Write the regenerated mirror for ``root``'s manifests into ``out``."""
    identifiers = course_identifiers(root)
    mirror = out / MIRROR_DIR
    metas = {}
    for identifier in identifiers:
        example = source_tree / identifier
        if not (example / "meta.yaml").is_file():
            raise SystemExit(f"{identifier}: not found in the source at {commit.sha}")
        meta = yaml.safe_load((example / "meta.yaml").read_text(encoding="utf-8"))
        target = mirror / identifier
        for relative in public_files(example, meta):
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(example / relative, destination)
        target.mkdir(parents=True, exist_ok=True)
        (target / "meta.yaml").write_text(dump_meta(public_meta(meta)), encoding="utf-8")
        metas[identifier] = meta
    (out / "RIGHTS.md").write_text(rights_ledger(metas, commit), encoding="utf-8")
    (out / "LANGUAGE_AUDIT.md").write_text(language_audit(mirror, identifiers), encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")
    (out / "README.md").write_text(readme_with_provenance(readme, commit, len(identifiers)),
                                   encoding="utf-8")


def tree_files(base: Path) -> dict[str, bytes]:
    return {p.relative_to(base).as_posix(): p.read_bytes() for p in base.rglob("*") if p.is_file()}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--source", type=Path, required=True,
                        help="local checkout of codeability/development/examples")
    parser.add_argument("--ref", default="main", help="commit, branch or tag (default: main)")
    parser.add_argument("--check", action="store_true",
                        help="only report whether the mirror differs; change nothing")
    args = parser.parse_args(argv)

    commit = source_commit(args.source, args.ref)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "src").mkdir()
        tree = export_tree(args.source, commit.sha, tmp / "src")
        out = tmp / "out"
        build(tree, commit, ROOT, out)
        new = tree_files(out / MIRROR_DIR)
        old = tree_files(ROOT / MIRROR_DIR)
        changed = sorted(k for k in new.keys() | old.keys() if new.get(k) != old.get(k))
        for name in ("RIGHTS.md", "LANGUAGE_AUDIT.md", "README.md"):
            if (out / name).read_bytes() != (ROOT / name).read_bytes():
                changed.append(name)
        if args.check:
            for name in changed:
                print(f"stale: {name}")
            return 1 if changed else 0
        shutil.rmtree(ROOT / MIRROR_DIR, ignore_errors=True)
        shutil.copytree(out / MIRROR_DIR, ROOT / MIRROR_DIR)
        for name in ("RIGHTS.md", "LANGUAGE_AUDIT.md", "README.md"):
            shutil.copyfile(out / name, ROOT / name)
    print(f"mirror regenerated from {commit.sha} ({len(changed)} files changed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
