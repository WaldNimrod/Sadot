"""
session_mcp_verify.py — Blender connectivity verification for Sadot sessions.
Writes exports/ai_bridge/session_mcp_verify.json + logs.

Provenance: ADAPTED from IsraelMicrogreens-BlenderV2-Project scripts/inspect/session_mcp_verify.py
on 2026-07-08 — Sadot blender/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
DEVIATION from source: the origin file hardcoded a check for `"016" not in bpy.data.filepath`
(a microgreens `_016` model-family filename fragment). That hardcoded check has been generalized
below into the EXPECTED_MODEL_NAME_FRAGMENT constant. MCP port 9876 connectivity check, the
headless (bpy.app.background) field, Blender version field, and the object_count sanity floor are
otherwise unchanged from the source verdict logic.

Run headless:
  Blender --background blender/<sadot_model>.blend --python scripts/inspect/session_mcp_verify.py
"""
import bpy
import json
import socket
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "exports" / "ai_bridge" / "session_mcp_verify.json"
LOG = ROOT / "logs" / "session_mcp_verify.txt"

# Set once Sadot's first .blend exists (Stage 3, 3D Modeling — see blender/CURRENT_MODEL.md).
# Until then this is a placeholder and the fragment check below only emits an informational note,
# never a BLOCK verdict on its own (matching the source script's behavior for its own "016" check).
EXPECTED_MODEL_NAME_FRAGMENT = "sadot"


def mcp_port_open(host="127.0.0.1", port=9876, timeout=1.0):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((host, port))
        s.close()
        return True
    except OSError:
        return False


def main():
    report = {
        "test_id": "session_mcp_verify_20260708",
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "blend_file": bpy.data.filepath,
        "blender_version": list(bpy.app.version),
        "background": bpy.app.background,
        "object_count": len(bpy.data.objects),
        "collection_count": len(bpy.data.collections),
        "mcp_port_9876_open": mcp_port_open(),
        "verdict": "PASS",
        "notes": [],
    }
    if not bpy.data.filepath:
        report["verdict"] = "BLOCK"
        report["notes"].append("No blend file loaded")
    elif EXPECTED_MODEL_NAME_FRAGMENT not in bpy.data.filepath:
        report["notes"].append(
            f"Expected filename fragment '{EXPECTED_MODEL_NAME_FRAGMENT}'; got {bpy.data.filepath}"
        )
    if report["object_count"] < 100:
        report["verdict"] = "BLOCK"
        report["notes"].append(f"Suspiciously low object count: {report['object_count']}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2))
    LOG.write_text(json.dumps(report, indent=2))
    print(f"VERDICT={report['verdict']}")
    print(f"MCP_PORT={report['mcp_port_9876_open']}")
    print(f"OBJECTS={report['object_count']}")
    print(f"REPORT={OUT}")


if __name__ == "__main__":
    main()
