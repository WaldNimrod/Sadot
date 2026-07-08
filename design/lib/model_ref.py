# Provenance: ADAPTED from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/model_ref.py on 2026-07-08 —
# Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
# DEVIATION: origin file hardcodes LIVE_BLEND = ".../blender/IsraelMicrogreens_022.blend", which
# does not exist in Sadot (no .blend has been created yet — see blender/CURRENT_MODEL.md). The
# path below is left as a placeholder pointing at Sadot's blender/ dir; update the filename once
# Sadot's first .blend exists (Stage 3, 3D Modeling).
"""Canonical LIVE .blend path for design/ read-only geometry reads (Sadot)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # repo root (design/lib/model_ref.py -> repo root)
LIVE_BLEND = ROOT / "blender" / "TBD_first_sadot_model.blend"  # set once first .blend exists
INVENTORY_JSON = ROOT / "exports" / "ai_bridge" / "phase3_inventory.json"
