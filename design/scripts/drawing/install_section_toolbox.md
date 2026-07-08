> **Provenance:** harvested verbatim from `IsraelMicrogreens-BlenderV2-Project` `scripts/drawing/install_section_toolbox.md` on 2026-07-08 — Sadot `design/` pipeline bootstrap (WP: `SDT-S001-P001-WP001`). The pinned model path below (`blender/IsraelMicrogreens_022.blend`) is the origin project's; substitute Sadot's own model per `blender/CURRENT_MODEL.md` once one exists.

# Section Toolbox — install and verification (Blender 5.0.1)

**Addon:** [Section Toolbox](https://extensions.blender.org/add-ons/stb-section-toolbox/) (`stb-section-toolbox`)  
**Blender:** 5.0.1 (`/Applications/Blender.app`)  
**Project model:** `blender/IsraelMicrogreens_022.blend`

## Install (GUI — one-time)

1. Open Blender 5.0.1 with network access.
2. **Edit → Preferences → Get Extensions**.
3. Search **Section Toolbox** → Install → Enable.
4. Restart Blender.

## Verify

```bash
/Applications/Blender.app/Contents/MacOS/Blender --background --python-expr "
import addon_utils
mods = [m[0] for m in addon_utils.modules()]
print('STB_FOUND', any('section' in m.lower() and 'toolbox' in m.lower() for m in mods))
for m in bpy.context.preferences.addons.keys():
    if 'stb' in m.lower() or 'section' in m.lower():
        print('ENABLED', m)
" 2>&1 | tail -5
```

Or run project check:

```bash
/Applications/Blender.app/Contents/MacOS/Blender --background \
  --python scripts/drawing/check_section_toolbox.py
```

## Pinned reference

| Item | Value |
|------|-------|
| Extension ID | `stb-section-toolbox` |
| Min Blender | 4.2 LTS |
| Export formats | SVG, DXF (view-aligned, Flip X/Y) |
| Workflow | Box section or planar section → Generate → Export |

## Automation fallback

If Section Toolbox is not installed or cannot run headless, `export_sheet_views.py` uses **mesh orthographic edge projection** (`mesh_ortho_export.py`) — still model-native vectors, not hand-drawn shapes.

Manual STB workflow (interactive):

1. Open `_022`, load collections per `drawings/view_presets/P-101_reservoir.yaml`.
2. Section Toolbox → Create Box → fit rear-yard selection.
3. Generate section → Export SVG/DXF to `drawings/_extracts/`.
4. Run `compose_sheet.py --sheet P101`.

## Related

- WP4.3 shot S9 ortho top plan: `_communication/team_100_engineering/WP_PHASE4_RENDER/04_WP4.3_camera_shotlist.md`
- Model-native standard: `WP_PHASE5_TECHNICAL_DOCS/MODEL_NATIVE_DRAWING_STANDARD.md`
