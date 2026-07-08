# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# scripts/assembly/phase4_site_exterior_pass.py on 2026-07-08 — Sadot blender/ pipeline bootstrap
# (WP: SDT-S001-P001-WP001). NOTE: this script dynamically loads sibling modules
# "wp42_site_environment" and "phase4_apply_realistic_and_render" by filename from
# scripts/assembly/ (origin repo) — those two modules were NOT harvested (they are
# origin-project-specific asset/material scripts). This file will not run as-is in Sadot until
# equivalent modules exist at the referenced ROOT/"scripts"/"assembly"/ path; kept verbatim as a
# worked reference for the site-exterior-pass + path-audit render pattern.
"""wp42 site fix + exterior renders + path audit (no interior Cycles)."""
import importlib.util
import sys
from pathlib import Path

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parent.parent.parent


def _load(name):
    path = ROOT / "scripts" / "assembly" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def render_site_path_audit():
    snap = ROOT / "snapshots" / "site_path_audit_20260705.png"
    sc = bpy.context.scene
    save = {o.name: o.hide_render for o in bpy.data.objects}
    save_cam, save_eng = sc.camera, sc.render.engine
    save_rx, save_ry = sc.render.resolution_x, sc.render.resolution_y
    save_fp = sc.render.filepath

    sc.render.engine = "BLENDER_WORKBENCH"
    sc.render.resolution_x = 1800
    sc.render.resolution_y = 1200
    sc.display.shading.color_type = "MATERIAL"
    sc.display.shading.light = "FLAT"

    show_prefix = ("SITE_path_", "SITE_foundation_", "SHELL.wall_", "SHELL.door", "ELE.gen", "HVAC.ac")
    for o in bpy.data.objects:
        if o.type != "MESH":
            o.hide_render = True
            continue
        o.hide_render = not any(o.name.startswith(p) for p in show_prefix)

    camd = bpy.data.cameras.new("SITE_AUDIT_CAM")
    camd.type = "ORTHO"
    camd.ortho_scale = 28.0
    cam = bpy.data.objects.new("SITE_AUDIT_CAM", camd)
    sc.collection.objects.link(cam)
    sc.camera = cam
    cam.location = Vector((6.0, 3.5, 40.0))
    cam.rotation_euler = (0.0, 0.0, 0.0)

    sc.render.filepath = str(snap.with_suffix(""))
    sc.render.image_settings.file_format = "PNG"
    bpy.ops.render.render(write_still=True)
    for q in snap.parent.glob("site_path_audit_20260705*.png"):
        if q != snap:
            q.rename(snap)

    for o in bpy.data.objects:
        if o.name in save:
            o.hide_render = save[o.name]
    sc.camera, sc.render.engine = save_cam, save_eng
    sc.render.resolution_x, sc.render.resolution_y = save_rx, save_ry
    sc.render.filepath = save_fp
    bpy.data.objects.remove(cam, do_unlink=True)
    bpy.data.cameras.remove(camd, do_unlink=True)
    print("SITE_PATH_AUDIT_SNAP", snap)


def run():
    _load("wp42_site_environment").run()
    phase4 = _load("phase4_apply_realistic_and_render")
    phase4.render_exterior_site()
    phase4.write_showcase_html()
    render_site_path_audit()
    bpy.ops.wm.save_mainfile()
    print("SITE_EXTERIOR_PASS_DONE")


if __name__ == "__main__":
    run()
