# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/sheet_export.py on 2026-07-08 —
# Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
"""Export sheet bundle: SVG + HTML + PDF."""
from __future__ import annotations

from pathlib import Path

from . import drawing_kit as dk


def export_sheet(
    out_dir: str | Path,
    stem: str,
    svg_body: str,
    html_title: str = "",
) -> dict[str, Path]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    svg_path = out_dir / f"{stem}.svg"
    html_path = out_dir / f"{stem}.html"
    pdf_path = out_dir / f"{stem}.pdf"

    page = dk.PAGE_LANDSCAPE.format(b=svg_body)
    svg_path.write_text(page, encoding="utf-8")

    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{html_title or stem}</title>
<style>
@page {{ size: 420mm 297mm; margin: 0; }}
html, body {{ margin: 0; padding: 0; }}
svg {{ display: block; width: 420mm; height: 297mm; }}
</style></head><body>{page}</body></html>"""
    html_path.write_text(html, encoding="utf-8")

    import weasyprint

    weasyprint.HTML(filename=str(html_path)).write_pdf(str(pdf_path))

    return {"svg": svg_path, "html": html_path, "pdf": pdf_path}
