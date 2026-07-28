#!/usr/bin/env python3
# Sadot — IFC → OBJ shell export for Blender ingest (SDT-S002-P007-WP001).
#
# Thin CLI wrapper around the proven mesh export in
# blender/scripts/site/export_house_shell_obj.py — adds argparse defaults to the
# newer NSB02_v2 fixture and a P007-oriented output path under blender/data/ingest/.
#
# Run from repo root:
#   /Library/Developer/CommandLineTools/usr/bin/python3 blender/scripts/ingest/export_shell_obj.py

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SITE_SCRIPT = REPO_ROOT / "blender/scripts/site/export_house_shell_obj.py"
DEFAULT_IFC = REPO_ROOT / "raw-materials/from-client/NSB02_v2_2026-07-13.ifc"
FALLBACK_IFC = REPO_ROOT / "raw-materials/from-client/NSB02.ifc"
DEFAULT_OUT = REPO_ROOT / "blender/data/ingest/house_shell_smoke.obj"


def load_site_exporter():
    spec = importlib.util.spec_from_file_location("export_house_shell_obj", SITE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SITE_SCRIPT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def resolve_ifc(path: Path | None) -> Path:
    if path is not None:
        p = path if path.is_absolute() else REPO_ROOT / path
        if not p.is_file():
            raise FileNotFoundError(f"IFC not found: {p}")
        return p
    if DEFAULT_IFC.is_file():
        return DEFAULT_IFC
    if FALLBACK_IFC.is_file():
        return FALLBACK_IFC
    raise FileNotFoundError(
        f"No fixture IFC at {DEFAULT_IFC} or {FALLBACK_IFC}"
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Sadot IFC→OBJ shell export (ingest)")
    ap.add_argument("ifc", nargs="?", type=Path, help="Input .ifc")
    ap.add_argument(
        "-o",
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help=f"Output .obj (default: {DEFAULT_OUT})",
    )
    args = ap.parse_args(argv)

    try:
        ifc_path = resolve_ifc(args.ifc)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    out_path = args.out if args.out.is_absolute() else REPO_ROOT / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)

    mod = load_site_exporter()
    # Site script writes verts in file length units with USE_WORLD_COORDS;
    # it already documents meters after conversion via unit_scale in header.
    # Call its main() with absolute paths as strings.
    print(f"ifc={ifc_path}")
    print(f"out={out_path}")
    mod.main(str(ifc_path), str(out_path))

    if not out_path.is_file() or out_path.stat().st_size < 100:
        print(f"ERROR: output missing or tiny: {out_path}", file=sys.stderr)
        return 1
    print(f"OK bytes={out_path.stat().st_size}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
