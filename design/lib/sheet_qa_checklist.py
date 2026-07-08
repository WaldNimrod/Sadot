# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/sheet_qa_checklist.py on
# 2026-07-08 — Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
"""Pre-delivery QA checks for a drawing sheet folder (English labels)."""
from __future__ import annotations

import re
import sys
from pathlib import Path


def validate_sheet_folder(folder: Path, extracts_dir: Path | None = None) -> list[str]:
    errors: list[str] = []
    folder = Path(folder)
    pdf = list(folder.glob("*.pdf"))
    svg = list(folder.glob("*.svg"))
    if not pdf:
        errors.append("missing PDF")
    if not svg:
        errors.append("missing SVG")
    if svg:
        text = svg[0].read_text(encoding="utf-8")
        text_check = re.sub(r'href="data:image[^"]*"', "", text)
        if "Sheet" not in text_check and "FOR CONSTRUCTION" not in text_check:
            errors.append("missing title block")
        dims = len(re.findall(r"\d+\s*mm", text_check))
        if dims < 3:
            errors.append(f"too few dimensions ({dims})")
        if "Parts index" not in text_check:
            errors.append("missing parts index")
        if "Model context" not in text_check and "<image" not in text and "mesh extract" not in text_check.lower():
            errors.append("missing context or model-native source note")
        if re.search(r"-\d+\s*mm", text_check):
            errors.append("contains negative dimension label")
        if re.search(r"\bTBD\b|\bTODO\b", text_check):
            errors.append("contains TBD/TODO")
        if re.search(r"\bair\s+gap\b", text_check, re.I) and "no air gap" not in text_check.lower():
            errors.append("air gap detail must not appear (use elbow-to-mid-depth)")
        # Model-native: require vector line geometry from extract embed
        line_count = text.count("<line ")
        if line_count < 10:
            errors.append(f"too few vector lines from mesh extract ({line_count})")
    if extracts_dir:
        extracts_dir = Path(extracts_dir)
        if not extracts_dir.exists():
            errors.append(f"missing extracts dir {extracts_dir}")
        else:
            svgs = list(extracts_dir.glob("*.svg"))
            if len(svgs) < 1:
                errors.append("no extraction SVG files")
            for p in svgs:
                t = p.read_text(encoding="utf-8")
                if "<line " not in t and "<path " not in t:
                    errors.append(f"extract has no vector geometry: {p.name}")
    return errors


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("usage: sheet_qa_checklist.py <sheet_folder> [extracts_dir]")
        return 1
    folder = Path(argv[0])
    extracts = Path(argv[1]) if len(argv) > 1 else None
    errs = validate_sheet_folder(folder, extracts)
    if errs:
        print("QA_FAIL", errs)
        return 1
    print("QA_PASS", folder)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
