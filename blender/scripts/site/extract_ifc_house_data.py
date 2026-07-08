#!/usr/bin/env python3
# Sadot — IFC house/window/deck/material extraction tool, authored 2026-07-08 (team_110, tooling-architecture WP).
#
# Requires ifcopenshell (installed for /Library/Developer/CommandLineTools/usr/bin/python3 on this machine —
# NOT the homebrew python3). Run: /Library/Developer/CommandLineTools/usr/bin/python3 extract_ifc_house_data.py
#
# WHAT THIS DOES: real ifcopenshell-API extraction (no regex on raw STEP text) of the architect's house model,
# for cross-reference against the landscape design. See design/CANONICAL/HOUSE_IFC_REFERENCE.md for the curated
# findings this script produced (storeys, windows, materials, stairs) and the KNOWN DATA-QUALITY ISSUES section
# (unreliable IsExternal flags, a coordinate-system mismatch between this file and the real ITM survey grid,
# and one deck/terrace-named element whose position doesn't spatially match the rest of the house).

from __future__ import annotations
import ifcopenshell
import ifcopenshell.util.placement as placement
import ifcopenshell.util.element as element
import ifcopenshell.util.unit as unit_util

IFC_PATH = "raw-materials/from-client/NSB02.ifc"  # run from repo root, or pass an absolute path


def psets(elem) -> dict:
    out = {}
    for rel in getattr(elem, "IsDefinedBy", []) or []:
        if rel.is_a("IfcRelDefinesByProperties"):
            pdef = rel.RelatingPropertyDefinition
            if pdef.is_a("IfcPropertySet"):
                for p in pdef.HasProperties:
                    if p.is_a("IfcPropertySingleValue") and p.NominalValue:
                        out[p.Name] = p.NominalValue.wrappedValue
    return out


def world_xyz_m(elem, scale: float):
    m = placement.get_local_placement(elem.ObjectPlacement)
    return (m[0][3] * scale, m[1][3] * scale, m[2][3] * scale)


def main(path: str = IFC_PATH):
    f = ifcopenshell.open(path)
    scale = unit_util.calculate_unit_scale(f)  # 0.01 for this file (cm -> m)

    print(f"schema={f.schema} unit_scale_to_m={scale}")

    print("\n-- storeys --")
    for s in sorted(f.by_type("IfcBuildingStorey"), key=lambda s: s.Elevation):
        print(f"  {s.Name!r}  elevation={s.Elevation * scale:.3f}m")

    print("\n-- windows --")
    for w in f.by_type("IfcWindow"):
        x, y, z = world_xyz_m(w, scale)
        storey = element.get_container(w)
        p = psets(w)
        print(f"  tag={w.Tag} name={w.Name!r} {w.OverallWidth*scale:.2f}x{w.OverallHeight*scale:.2f}m "
              f"storey={storey.Name if storey else None} pos=({x:.2f},{y:.2f},{z:.2f}) IsExternal={p.get('IsExternal')}")

    print("\n-- stairs (Pset ground truth, NOT raw RiserHeight/TreadLength attrs — those are in feet in this file) --")
    for st in f.by_type("IfcStair"):
        p = psets(st)
        print(f"  {st.Name!r}  risers={p.get('NumberOfRiser')} treads={p.get('NumberOfTreads')} "
              f"riser_h_cm={p.get('RiserHeight')} tread_len_cm={p.get('TreadLength')} IsExternal={p.get('IsExternal')}")
    print(f"  IfcRamp count: {len(f.by_type('IfcRamp'))}  (0 = no exterior ramp modeled)")

    print("\n-- materials (first 20 of {}) --".format(len(f.by_type("IfcMaterial"))))
    for m in f.by_type("IfcMaterial")[:20]:
        print(f"  {m.Name}")


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else IFC_PATH)
