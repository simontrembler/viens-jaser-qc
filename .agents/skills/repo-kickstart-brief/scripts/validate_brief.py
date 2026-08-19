#!/usr/bin/env python3
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "## 0) Repository hierarchy (emoji map)",
    "## 1) Stack at a glance",
    "## 2) What to run first",
    "## 3) Evidence found",
    "## 4) Risks or unknowns",
    "## 5) Next 3 steps",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: validate_brief.py <brief.md>")
        sys.exit(2)

    brief_path = Path(sys.argv[1])
    if not brief_path.exists():
        fail(f"File not found: {brief_path}")

    text = brief_path.read_text(encoding="utf-8", errors="ignore")

    if not text.startswith("# Repo Kickstart Brief"):
        fail("Missing title '# Repo Kickstart Brief'")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            fail(f"Missing required heading: {heading}")

    # Require hierarchy section with emoji-coded entries.
    hierarchy_section_match = re.search(
        r"## 0\) Repository hierarchy \(emoji map\)(.*?)## 1\) Stack at a glance",
        text,
        re.S,
    )
    if not hierarchy_section_match:
        fail("Could not parse repository hierarchy section")
    hierarchy_block = hierarchy_section_match.group(1)
    hierarchy_hits = re.findall(r"-\s+(📁|📄)\s+.+", hierarchy_block)
    if len(hierarchy_hits) < 3:
        fail("Hierarchy section needs at least 3 emoji-coded entries (📁/📄)")

    # Require at least 3 evidence bullets with backticked paths.
    evidence_section_match = re.search(
        r"## 3\) Evidence found(.*?)## 4\) Risks or unknowns", text, re.S
    )
    if not evidence_section_match:
        fail("Could not parse evidence section")
    evidence_block = evidence_section_match.group(1)
    evidence_hits = re.findall(r"-\s+`[^`]+`:\s+.+", evidence_block)
    if len(evidence_hits) < 3:
        fail("Evidence section needs at least 3 bullet points with path + proof")

    # Require numbered next steps 1..3
    next_steps_match = re.search(r"## 5\) Next 3 steps(.*)$", text, re.S)
    if not next_steps_match:
        fail("Could not parse next steps section")
    next_steps = next_steps_match.group(1)
    for n in ("1.", "2.", "3."):
        if n not in next_steps:
            fail("Next steps must include numbered items 1., 2., and 3.")

    print("PASS: brief structure is valid")


if __name__ == "__main__":
    main()
