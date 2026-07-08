# Provenance: ADAPTED from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/__init__.py on 2026-07-08 —
# Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
# DEVIATION: origin __init__.py is `from . import boq_kit, drawing_kit`. boq_kit.py is
# origin-project-specific (BOQ/tank vendor kit) and was intentionally excluded from this harvest
# per the replication guide's "what NOT to copy blindly" — so the boq_kit import was dropped here
# to avoid an ImportError on a module that does not exist in this package.
"""Sadot design/ shared libraries (harvested subset of Phase 5 technical documentation kit)."""

from . import drawing_kit

__all__ = ["drawing_kit"]
