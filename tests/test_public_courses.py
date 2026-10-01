"""Published assignments must be readable in both offered languages."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def assignments(nodes):
    for node in nodes:
        if "example_identifier" in node:
            yield node["example_identifier"]
        yield from assignments(node.get("contents", []))


def test_published_assignments_have_bilingual_descriptions_and_templates():
    seen = set()
    for manifest in sorted((ROOT / "courses").glob("*.yaml")):
        course = yaml.safe_load(manifest.read_text())
        # YAML 1.1 interprets an unquoted 'off' as a boolean. The assistant
        # contract requires a completion enum that survives real parsing.
        assert course["properties"]["assistant_policy"]["completion"] in ("off", "single-line", "multi-line")
        for identifier in assignments(course["contents"]):
            assert identifier not in seen, f"Assignment repeated across course levels: {identifier}"
            seen.add(identifier)
            folder = ROOT / "examples" / "python" / identifier
            for language in ("en", "de"):
                assert len((folder / "content" / f"index_{language}.md").read_text().strip()) > 80
            metadata = yaml.safe_load((folder / "meta.yaml").read_text())
            assert metadata["slug"] == identifier
            for filename in metadata.get("properties", {}).get("additionalFiles", []):
                assert (folder / filename).is_file(), f"Missing public input file: {filename}"
    assert seen, "Published courses must contain accessible assignments"
