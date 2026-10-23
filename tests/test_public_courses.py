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
            elif node["path"] == "welcome":
                assert title == "Willkommen", f"{manifest.name}: {node['path']}"
            else:
                week = re.fullmatch(r"week_(\d+)", node["path"]).group(1)
                assert title == f"Woche {week}", f"{manifest.name}: {node['path']}"


def test_beginner_course_opens_with_a_welcome_item_for_the_extension():
    """The VS Code extension opens this item when a workspace launches.

    The conditions mirror ``welcomeItem()`` in computor-vscode
    (src/services/WorkspaceCourseLanding.ts) and the welcome ids of
    computor-web/scripts/build-public-learning.mjs in computor-backend.
    """
    course = yaml.safe_load((ROOT / "courses" / "python-beginner.yaml").read_text())
    welcome, first_week = course["contents"][:2]
    kinds = {kind["slug"]: kind["kind"] for kind in course["content_types"]}
    assert kinds[welcome["content_type"]] == "unit", "Only non-assignment items are welcome items"
    assert welcome["position"] < first_week["position"]
    assert welcome["path"] in ("welcome", "start_here", "introduction")
    assert re.fullmatch(r"willkommen", welcome["title"], re.I)
    assert not welcome.get("contents") and "example_identifier" not in welcome
    text = welcome["description"]
    first = first_week["contents"][0]
    assert f"„{first_week['title']}“" in text and f"„{first['title']}“" in text
    assert "@lena" in text, "Help in this course comes from Lena"
    assert len(text) < 3000, "The welcome text should stay short"
