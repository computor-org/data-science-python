"""The mirror script publishes only learner-facing files of an example."""
import importlib.util
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("refresh", ROOT / "scripts" / "refresh_from_examples.py")
refresh = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = refresh
spec.loader.exec_module(refresh)

META = {
    "slug": "itpcp.pgph.py.demo",
    "title": "Demo",
    "language": "de",
    "license": "MIT",
    "authors": [{"name": "A. Author"}],
    "maintainers": [{"name": "M. Maintainer"}],
    "properties": {
        "studentSubmissionFiles": ["demo.py"],
        "additionalFiles": ["data.txt", "check_demo.py"],
        "testFiles": ["check_demo.py"],
        "studentTemplates": ["studentTemplates/demo.py"],
        "executionBackend": {"slug": "itpcp.exec.py", "settings": {}, "version": "3.13"},
    },
}

FILES = {
    "content/index_de.md": "# Demo\n\nSchreib dein Programm.\n",
    "content/index_en.md": "# Demo\n\nWrite your program.\n",
    "content/mediaFiles/plot.png": "png",
    "content/mediaFiles/Solution.PNG": "secret",
    "studentTemplates/demo.py": "# starter\n",
    "studentTemplates/demo_solution.py": "secret",
    "data.txt": "1 2 3\n",
    "demo.py": "secret reference solution",
    "check_demo.py": "secret test",
    "test.yaml": "secret",
    "notes.txt": "unlisted",
    "localTests/correctSolution/demo.py": "secret",
}

PUBLIC = [
    "content/index_de.md",
    "content/index_en.md",
    "content/mediaFiles/plot.png",
    "studentTemplates/demo.py",
    "data.txt",
]


def make_example(base: Path) -> Path:
    example = base / META["slug"]
    for relative, text in FILES.items():
        (example / relative).parent.mkdir(parents=True, exist_ok=True)
        (example / relative).write_text(text)
    (example / "meta.yaml").write_text(yaml.safe_dump(META, sort_keys=False))
    return example


def test_only_texts_templates_and_listed_inputs_are_public(tmp_path):
    example = make_example(tmp_path)
    assert sorted(refresh.public_files(example, META)) == sorted(PUBLIC)


def test_meta_keeps_attribution_but_drops_grading_properties():
    meta = refresh.public_meta(META)
    assert meta["authors"] == META["authors"] and meta["license"] == "MIT"
    assert meta["properties"] == {
        "additionalFiles": ["data.txt"],
        "studentTemplates": ["studentTemplates/demo.py"],
    }
    bare = dict(META, properties={"studentSubmissionFiles": ["demo.py"], "additionalFiles": []})
    assert "properties" not in refresh.public_meta(bare)


def test_build_writes_mirror_ledger_and_provenance(tmp_path):
    source = tmp_path / "source"
    make_example(source)
    root = tmp_path / "repo"
    (root / "courses").mkdir(parents=True)
    (root / "courses" / "demo.yaml").write_text(yaml.safe_dump(
        {"contents": [{"path": "week_1", "contents": [{"path": "week_1.demo",
                                                       "example_identifier": META["slug"]}]}]}))
    (root / "README.md").write_text(
        "The source snapshot is\n`old` at\n[`old`](old)\n(old; “old”). Each example keeps\n"
        "snapshot declares MIT for all 70 Python examples.\n")
    commit = refresh.SourceCommit("a" * 40, "2026-10-24T10:00:00+02:00", "Use du")
    out = tmp_path / "out"
    refresh.build(source, commit, root, out)

    mirror = out / "examples" / "python" / META["slug"]
    published = sorted(p.relative_to(mirror).as_posix() for p in mirror.rglob("*") if p.is_file())
    assert published == sorted(PUBLIC + ["meta.yaml"])
    assert "secret" not in "".join((mirror / name).read_text() for name in published)
    assert "a" * 40 in (out / "RIGHTS.md").read_text()
    readme = (out / "README.md").read_text()
    assert f"[`{'a' * 40}`](https://gitlab.tugraz.at/" in readme and "“Use du”" in readme
    assert "for all 1 Python examples" in readme
    assert "no solution or test artifacts: **1/1**" in (out / "LANGUAGE_AUDIT.md").read_text()


def test_committed_mirror_contains_no_private_files():
    mirror = ROOT / "examples" / "python"
    for path in mirror.rglob("*"):
        relative = path.relative_to(mirror)
        assert "localTests" not in relative.parts, relative
        assert path.name != "test.yaml", relative
        assert not refresh.is_private_name(relative.as_posix()), relative
