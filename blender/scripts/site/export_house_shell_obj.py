#!/usr/bin/env python3
# Sadot — export real IFC house geometry (walls, windows, doors, roofs, deck slab) to a single OBJ for Blender
# import, authored 2026-07-09 (team_110, initial-model WP). Extends extract_ifc_house_data.py's inspection pass
# with actual mesh export via ifcopenshell.geom (real triangulated geometry, not a placeholder box).
#
# Requires ifcopenshell (installed for /Library/Developer/CommandLineTools/usr/bin/python3 on this machine —
# NOT the homebrew python3). Run:
#   /Library/Developer/CommandLineTools/usr/bin/python3 blender/scripts/site/export_house_shell_obj.py
#
# SCOPE (v1, initial model — see design/CANONICAL/BLENDER_SHELL_BUILD_PLAN_v1.0.0.md): exports ALL walls
# (interior partitions included — the exterior-only wall-axis-chaining reconstruction described in that plan's
# §2 is a later refinement, not done here) + all windows/doors as real openings + roofs (excluding the 1 stray
# ~133m-offset fragment, auto-detected by distance from the model's own centroid) + the deck slab (IfcSlab #51836).
# Output is in the IFC's OWN native world coordinates (meters, already converted) — NOT yet anchored to the real
# ITM survey grid. See §0.1 of HOUSE_IFC_REFERENCE.md for the coordinate-reconciliation caveat.

import ifcopenshell
import ifcopenshell.geom as geom
import ifcopenshell.util.unit as unit_util

IFC_PATH = "raw-materials/from-client/NSB02.ifc"
OUT_OBJ = "blender/data/site/house_shell_v1.obj"
DECK_SLAB_TAG = "51836"  # IfcSlab #51836, the real deck candidate — see HOUSE_IFC_REFERENCE.md §4


def main(ifc_path: str = IFC_PATH, out_path: str = OUT_OBJ):
    f = ifcopenshell.open(ifc_path)
    scale = unit_util.calculate_unit_scale(f)

    settings = geom.settings()
    settings.set(settings.USE_WORLD_COORDS, True)

    # collect candidate elements
    walls = f.by_type("IfcWall")
    windows = f.by_type("IfcWindow")
    doors = f.by_type("IfcDoor")
    roofs = f.by_type("IfcRoof")
    deck = next((s for s in f.by_type("IfcSlab") if str(s.id()) == DECK_SLAB_TAG), None)

    # detect + exclude the stray roof fragment: compute each roof's shape centroid, flag any
    # roof whose centroid is > 50m from the median roof centroid (real roofs cluster together;
    # the known stray fragment sits ~133m away per HOUSE_IFC_REFERENCE.md's own finding).
    roof_centroids = []
    for r in roofs:
        try:
            shape = geom.create_shape(settings, r)
            verts = shape.geometry.verts
            n = len(verts) // 3
            cx = sum(verts[0::3]) / n
            cy = sum(verts[1::3]) / n
            roof_centroids.append((r, cx, cy))
        except Exception as e:
            print(f"  [skip roof {r.Name!r}: {e}]")
    if roof_centroids:
        xs = sorted(c[1] for c in roof_centroids)
        ys = sorted(c[2] for c in roof_centroids)
        med_x, med_y = xs[len(xs) // 2], ys[len(ys) // 2]
        kept_roofs = []
        for r, cx, cy in roof_centroids:
            d = ((cx - med_x) ** 2 + (cy - med_y) ** 2) ** 0.5
            if d > 50:
                print(f"  [excluding stray roof {r.Name!r} — {d:.1f}m from median centroid]")
            else:
                kept_roofs.append(r)
    else:
        kept_roofs = []

    elements_by_group = {
        "walls": walls,
        "windows": windows,
        "doors": doors,
        "roofs": kept_roofs,
        "deck": [deck] if deck else [],
    }

    vert_offset = 0
    n_ok, n_fail = 0, 0
    with open(out_path, "w") as out:
        out.write("# Sadot house shell — real IFC geometry, native IFC world coords (meters)\n")
        out.write(f"# source: {ifc_path}, schema={f.schema}, unit_scale={scale}\n")
        out.write("# NOT yet anchored to real ITM survey grid — see HOUSE_IFC_REFERENCE.md §0.1\n")
        for group, elems in elements_by_group.items():
            for elem in elems:
                try:
                    shape = geom.create_shape(settings, elem)
                except Exception as e:
                    n_fail += 1
                    print(f"  [FAIL {group} {elem.Name!r}: {e}]")
                    continue
                verts = shape.geometry.verts
                faces = shape.geometry.faces
                name = f"{group}_{elem.id()}_{(elem.Name or '').replace(' ', '_')[:30]}"
                out.write(f"o {name}\n")
                for i in range(0, len(verts), 3):
                    out.write(f"v {verts[i]:.4f} {verts[i+1]:.4f} {verts[i+2]:.4f}\n")
                for i in range(0, len(faces), 3):
                    a, b, c = faces[i] + 1 + vert_offset, faces[i+1] + 1 + vert_offset, faces[i+2] + 1 + vert_offset
                    out.write(f"f {a} {b} {c}\n")
                vert_offset += len(verts) // 3
                n_ok += 1

    print(f"\nWrote {out_path}: {n_ok} elements exported, {n_fail} failed.")
    print(f"Groups: walls={len(walls)}, windows={len(windows)}, doors={len(doors)}, "
          f"roofs kept={len(kept_roofs)}/{len(roofs)}, deck={'found' if deck else 'NOT FOUND — check DECK_SLAB_TAG'}")


if __name__ == "__main__":
    main()
