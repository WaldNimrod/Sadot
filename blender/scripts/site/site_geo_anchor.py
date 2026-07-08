#!/usr/bin/env python3
# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# scripts/assembly/site_geo_anchor.py on 2026-07-08 — Sadot blender/ pipeline bootstrap
# (WP: SDT-S001-P001-WP001). NOTE: the usage docstring below and GEO_YAML path point at the
# origin project's model filename / data/site/SITE_GEO.yaml — update the blend path in the usage
# example and confirm data/site/SITE_GEO.yaml exists in Sadot before running.
"""
site_geo_anchor.py — Place/update SITE.geo_anchor Empty at engineering datum (0,0,0)
and load WGS84 from data/site/SITE_GEO.yaml onto the object + scene.

Usage:
  blender --background blender/IsraelMicrogreens_024.blend \\
    --python scripts/assembly/site_geo_anchor.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEO_YAML = ROOT / "data/site/SITE_GEO.yaml"
LOG = ROOT / "logs/assembly/site_geo_anchor.json"


def load_geo() -> dict:
    raw = subprocess.check_output(
        [
            "python3",
            "-c",
            "import yaml, json, sys; print(json.dumps(yaml.safe_load(open(sys.argv[1]))))",
            str(GEO_YAML),
        ],
        text=True,
    )
    return json.loads(raw)


def ensure_collection(name: str):
    import bpy

    coll = bpy.data.collections.get(name)
    if coll is None:
        coll = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(coll)
    return coll


def main():
    import bpy

    geo = load_geo()
    wgs = geo["wgs84"]
    datum = geo["blender_datum"]

    coll = ensure_collection("00_REFERENCE")
    name = datum["object_name"]
    obj = bpy.data.objects.get(name)
    if obj is None:
        obj = bpy.data.objects.new(name, None)
        obj.empty_display_type = "ARROWS"
        obj.empty_display_size = 0.5
        coll.objects.link(obj)
    else:
        # ensure in reference collection
        if name not in coll.objects:
            for c in obj.users_collection:
                c.objects.unlink(obj)
            coll.objects.link(obj)

    obj.location = (0.0, 0.0, 0.0)
    obj.rotation_euler = (0.0, 0.0, 0.0)
    obj.scale = (1.0, 1.0, 1.0)

    obj["geo_lat"] = float(wgs["latitude"])
    obj["geo_lon"] = float(wgs["longitude"])
    obj["geo_crs"] = "EPSG:4326"
    obj["geo_itm_epsg"] = geo["itm"]["epsg"]
    obj["geo_anchor_note"] = datum["world_origin_meaning"]
    obj["geo_site_id"] = geo["site_id"]
    obj["geo_updated"] = geo["updated"]

    sc = bpy.context.scene
    sc["site_geo_lat"] = float(wgs["latitude"])
    sc["site_geo_lon"] = float(wgs["longitude"])
    sc["site_geo_crs"] = "EPSG:4326"
    sc["site_geo_yaml"] = str(GEO_YAML.relative_to(ROOT))

    bpy.ops.wm.save_mainfile()

    report = {
        "blend": bpy.data.filepath,
        "object": name,
        "location": list(obj.location),
        "geo_lat": obj["geo_lat"],
        "geo_lon": obj["geo_lon"],
        "yaml": str(GEO_YAML),
        "collection": coll.name,
    }
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("SITE_GEO_ANCHOR_OK", json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
