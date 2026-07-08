# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/sheet_gate.py on 2026-07-08 —
# Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
# NOTE: SHEET_ORDER below ("C4","C1","C3","C2") is the origin project's legacy sheet queue —
# replace with Sadot's own DRAWING_SHEET_INDEX.yaml production_order once that exists.
"""Per-sheet approval gate — no sheet N+1 before explicit Nimrod approval on N."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "APPROVAL_LOG.md"

# Production order per DRAWING_DELIVERY_STANDARD / Phase 5 plan
SHEET_ORDER = ("C4", "C1", "C3", "C2")


def _approved(sheet_id: str) -> bool:
    if not LOG.exists():
        return False
    text = LOG.read_text(encoding="utf-8")
    # Row must name the sheet and have a non-empty Nimrod reply (not AWAITING / rejected)
    for line in text.splitlines():
        if sheet_id not in line or "|" not in line:
            continue
        if "AWAITING" in line or "rejected" in line.lower():
            continue
        cols = [c.strip() for c in line.split("|")]
        if len(cols) < 7:
            continue
        item, reply = cols[3], cols[6]
        if sheet_id in item and reply and reply not in ("—", "-", ""):
            return True
    return False


def require_prior(sheet_id: str) -> None:
    idx = SHEET_ORDER.index(sheet_id)
    if idx == 0:
        return
    prior = SHEET_ORDER[idx - 1]
    if not _approved(prior):
        raise SystemExit(
            f"GATE: {sheet_id} blocked — {prior} not approved in APPROVAL_LOG.md "
            f"(Nimrod must approve {prior} PDF before building {sheet_id})"
        )


def gate_status() -> dict[str, str]:
    out: dict[str, str] = {}
    for sid in SHEET_ORDER:
        out[sid] = "approved" if _approved(sid) else "blocked"
    return out
