"""Published assignments must be readable in both offered languages."""
import re
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


def plain_title(heading):
    """A Markdown heading as plain text, as course titles are shown unrendered."""
    return heading.replace("$\\pi$", "π").replace("$-$", "–").replace("*", "")


def titled_nodes(nodes):
    for node in nodes:
        yield node
        yield from titled_nodes(node.get("contents", []))


def test_course_titles_are_german_and_match_the_assignment_heading():
    """Without a title the server falls back to the path ("Math Constants")."""
    for manifest in sorted((ROOT / "courses").glob("*.yaml")):
        course = yaml.safe_load(manifest.read_text())
        for node in titled_nodes(course["contents"]):
            title = node.get("title")
            assert title, f"{manifest.name}: '{node['path']}' has no title"
            if "example_identifier" in node:
                text = (ROOT / "examples" / "python" / node["example_identifier"]
                        / "content" / "index_de.md").read_text()
                heading = re.search(r"^#\s+(.+?)\s*#*\s*$", text, re.M).group(1)
                assert title == plain_title(heading), f"{manifest.name}: {node['path']}"
            else:
                # Units are weeks only: the extension's generic Welcome page is
                # the guide, a course item would repeat it (computor-org/issues#546).
                week = re.fullmatch(r"week_(\d+)", node["path"]).group(1)
                assert title == f"Woche {week}", f"{manifest.name}: {node['path']}"


def test_course_item_titles_are_unique_within_a_course():
    """The title is all a learner sees in the tree, so it must name one item."""
    for manifest in sorted((ROOT / "courses").glob("*.yaml")):
        course = yaml.safe_load(manifest.read_text())
        seen: dict[str, str] = {}
        for node in titled_nodes(course["contents"]):
            title = node["title"]
            assert title not in seen, (
                f"{manifest.name}: title '{title}' used by '{seen[title]}' "
                f"and '{node['path']}'"
            )
            seen[title] = node["path"]


LANGUAGES = ("de", "en")


def heading(folder, language):
    text = (folder / "content" / f"index_{language}.md").read_text()
    return plain_title(re.search(r"^#\s+(.+?)\s*#*\s*$", text, re.M).group(1))


def assert_bilingual(label, entry, key, source):
    """Both reading languages are filled; German, the source, equals the plain field."""
    variants = entry.get(key)
    assert isinstance(variants, dict), f"{label}: no {key}"
    for language in LANGUAGES:
        text = variants.get(language)
        assert isinstance(text, str) and text.strip(), f"{label}: {key} has no '{language}'"
    assert variants["de"] == entry.get(source), f"{label}: {key}['de'] differs from {source}"


def test_course_metadata_is_bilingual():
    """The server shows these maps in the reader's language (computor-org/issues#551)."""
    for manifest in sorted((ROOT / "courses").glob("*.yaml")):
        course = yaml.safe_load(manifest.read_text())
        name = manifest.name
        assert course.get("language_code") == "de", f"{name}: language_code"
        assert_bilingual(name, course, "title_i18n", "name")
        assert_bilingual(name, course, "description_i18n", "description")
        for content_type in course["content_types"]:
            label = f"{name}: content type {content_type['slug']}"
            assert_bilingual(label, content_type, "title_i18n", "title")
            assert_bilingual(label, content_type, "description_i18n", "description")
        for node in titled_nodes(course["contents"]):
            label = f"{name}: {node['path']}"
            assert_bilingual(label, node, "title_i18n", "title")
            if "example_identifier" in node:
                meta = yaml.safe_load((ROOT / "examples" / "python" / node["example_identifier"]
                                       / "meta.yaml").read_text())
                assert node["title_i18n"] == meta["title_i18n"], label
            else:
                assert_bilingual(label, node, "description_i18n", "description")


def test_example_metadata_is_bilingual_and_matches_the_headings():
    for manifest in sorted((ROOT / "courses").glob("*.yaml")):
        course = yaml.safe_load(manifest.read_text())
        for identifier in assignments(course["contents"]):
            folder = ROOT / "examples" / "python" / identifier
            meta = yaml.safe_load((folder / "meta.yaml").read_text())
            assert meta["language"] == "de", identifier
            assert_bilingual(identifier, meta, "title_i18n", "title")
            assert_bilingual(identifier, meta, "description_i18n", "description")
            for language in LANGUAGES:
                assert meta["title_i18n"][language] == heading(folder, language), (
                    f"{identifier}: title_i18n['{language}'] is not the heading of index_{language}.md"
                )
