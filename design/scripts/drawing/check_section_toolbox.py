#!/usr/bin/env python3
# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project scripts/drawing/check_section_toolbox.py
# on 2026-07-08 — Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
"""Check whether Section Toolbox (or similar) is available in this Blender build."""
from __future__ import annotations

import sys

try:
    import bpy
except ImportError:
    print("NO_BLENDER")
    sys.exit(2)

found = []
for pref in bpy.context.preferences.addons.keys():
    low = pref.lower()
    if "section" in low or "stb" in low:
        found.append(pref)

if found:
    print("SECTION_TOOLBOX_ENABLED", found)
    sys.exit(0)

print("SECTION_TOOLBOX_NOT_INSTALLED")
print("See scripts/drawing/install_section_toolbox.md")
sys.exit(1)
