#!/usr/bin/env python3
"""Build static Sadot client hub from hub/data (Client Hub Standard v1.1).

Adapted from EyalAmit.co.il-2026's scripts/build_eyal_client_hub.py, pruned to the
subset of pages relevant to a landscape-architecture client hub (Niv Sadot /
private house, Pardes Hanna) — no WordPress-migration views (site-tree,
media-intake, content-proposals, legacy-unmapped, testimonials, analytics-config).

Usage (repo root):
    python3 scripts/build_sadot_client_hub.py
    python3 scripts/build_sadot_client_hub.py --out hub/dist

Output: hub/dist/ (index, roadmap, tasks, meeting, what-we-need,
materials-needed, assets/, data/, robots.txt, metadata.json)
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from typing import Optional

HUB_ROOT = Path(__file__).resolve().parent.parent / "hub"
DATA_DIR = HUB_ROOT / "data"
SRC_DIR = HUB_ROOT / "src"
SSOT_DIR = HUB_ROOT / "ssot"
DEFAULT_DIST = HUB_ROOT / "dist"

WHATSAPP_URL = "https://wa.me/972547776770"
BRAND_TEXT = "Agents OS @ nimrod.bio"

# Renamed from EyalAmit's build_eyal_client_hub.py constants:
#   EXPORT_TYPE            "eyal-feedback"      -> "sadot-feedback"
#   DEFAULT_RESPONDENT      "Eyal Amit"          -> "Niv Sadot"
#   PROJECT_META            "EyalAmit2026"       -> "Sadot2026"
#   decision-id prefix      D-EYAL-              -> D-SADOT-  (see decisions.json)
#   page-ref prefix         EA-                  -> NS-       (reserved; no site-tree
#                                                  page in this pruned build yet)
EXPORT_TYPE = "sadot-feedback"
DEFAULT_RESPONDENT = "Niv Sadot"
PROJECT_META = "Sadot2026"
DECISION_ID_PREFIX = "D-SADOT-"
PAGE_REF_PREFIX = "NS-"  # reserved for a future site-tree page, unused today
DEFAULT_HUB_VIEW_VERSION = "1.0.0"


def load_json(path: Path) -> dict:
    if not path.exists():
        print(f"[ERROR] Missing data file: {path}")
        sys.exit(1)
    return json.loads(path.read_text(encoding="utf-8"))


def load_json_optional(path: Path) -> dict | None:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return None


def hub_view_version(path: Path) -> str:
    data = load_json_optional(path)
    if data and str(data.get("hubVersion", "")).strip():
        return str(data["hubVersion"]).strip()
    return DEFAULT_HUB_VIEW_VERSION


def updates_items_newest_first(updates: dict) -> list:
    items = list(updates.get("items", []))
    items.sort(key=lambda x: (x.get("date", ""), x.get("id", "")), reverse=True)
    return items


def updates_recent_count(updates: dict, days: int = 30) -> int:
    # Kept simple/date-agnostic for a fresh hub with no items yet.
    return len(updates.get("items", []))


# ---------------------------------------------------------------------------
# Shell: head / nav / foot (same pattern as build_eyal_client_hub.py)
# ---------------------------------------------------------------------------

HUB_NAV_ITEMS: list[tuple[str, str]] = [
    ("index.html", "כניסה"),
    ("what-we-need.html", "מה נדרש ממך"),
    ("tasks.html", "משימות והחלטות"),
    ("roadmap.html", "מפת דרכים"),
    ("meeting.html", "תדריך פגישה"),
    ("materials-needed.html", "חומרים נדרשים"),
]


def head(title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{escape(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@700&family=Heebo:wght@300;400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/hub-base.css">
<link rel="stylesheet" href="assets/sadot.css">
</head>
<body>
"""


def nav(active: str) -> str:
    parts = ["<nav>"]
    for href, label in HUB_NAV_ITEMS:
        if href.replace(".html", "") == active:
            parts.append(f"<strong>{escape(label)}</strong>")
        else:
            parts.append(f'<a href="{href}">{escape(label)}</a>')
    parts.append("</nav>")
    return "\n".join(parts)


def foot(generated_iso: str) -> str:
    return f"""<footer class="project-foot">
ממשק תקשורת ומצב עבודה — Sadot (ניב שדות) — עיצוב נוף לבית פרטי, פרדס חנה<br>
נוצר אוטומטית: {escape(generated_iso)}<br>
ממשק זה אינו מחליף תיעוד רשמי — לשימוש פנימי ותיאום מול הלקוח.
</footer>
<div class="hub-brand">
<a href="{WHATSAPP_URL}" target="_blank" rel="noopener">{BRAND_TEXT}</a>
</div>
</body>
</html>"""


def hub_acc_section(section_id: str, title: str, body_html: str, *, open_default: bool = False) -> str:
    open_attr = " open" if open_default else ""
    return (
        f'<details class="decision-detail" id="{escape(section_id)}"{open_attr}>\n'
        f"<summary>{escape(title)}</summary>\n"
        f'<div class="decision-content">\n{body_html}</div>\n'
        "</details>\n"
    )


def status_badge(status: str) -> str:
    mapping = {
        "completed": ("badge-done", "הושלם"),
        "in_progress": ("badge-run", "בביצוע"),
        "not_started": ("badge-todo", "לא התחיל"),
        "blocked": ("badge-blocked", "חסום"),
        "pending": ("badge-pending", "ממתין"),
        "answered": ("badge-done", "נענה"),
        "deferred": ("badge-blocked", "נדחה"),
        "approved": ("badge-done", "אושר"),
        "open": ("badge-pending", "פתוח"),
        "closed": ("badge-done", "סגור"),
    }
    cls, label = mapping.get(status, ("badge-todo", status or "—"))
    return f'<span class="badge {cls}">{escape(label)}</span>'


def priority_badge(priority_he: str) -> str:
    mapping = {"גבוהה": "badge-high", "בינונית": "badge-medium", "נמוכה": "badge-low"}
    cls = mapping.get(priority_he, "badge-medium")
    return f'<span class="badge {cls}">{escape(priority_he)}</span>' if priority_he else ""


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def page_index(updates: dict, roadmap: dict, tasks: dict, decisions: dict,
                generated_iso: str, hub_version: str) -> str:
    milestones = roadmap.get("milestones", [])
    all_tasks: list = []
    for sec in tasks.get("sections", []):
        all_tasks.extend(sec.get("tasks", []))
    open_count = sum(1 for t in all_tasks if t.get("status") != "completed")
    done_count = sum(1 for t in all_tasks if t.get("status") == "completed")
    open_decisions = sum(1 for d in decisions.get("decisions", []) if d.get("status") == "pending")
    recent_n = updates_recent_count(updates)

    current = roadmap.get("currentFocusId", "")
    current_ms = next((m for m in milestones if m.get("id") == current), None)
    current_label = escape(current_ms["titleHe"]) if current_ms else "— (טרם נקבע)"

    stats_html = '<div class="stats-row">\n'
    stats_html += (
        f'<div class="stat-card"><div class="stat-number">{open_count} · {done_count}</div>'
        f'<div class="stat-label">משימות פתוחות · סגורות</div></div>\n'
    )
    stats_html += (
        f'<div class="stat-card"><div class="stat-number">{open_decisions}</div>'
        f'<div class="stat-label">החלטות ממתינות</div></div>\n'
    )
    stats_html += (
        f'<div class="stat-card"><div class="stat-number">{recent_n}</div>'
        f'<div class="stat-label">עדכונים בלוג</div></div>\n'
    )
    stats_html += "</div>\n"

    gate_body = (
        '<p class="index-gate-text">Hub זה הוקם בשלב האתחול (bootstrap) של פרויקט עיצוב הנוף/הגינה '
        'לניב שדות (בית פרטי, פרדס חנה). עדיין אין תוכן אמיתי — הדפים ימולאו במהלך שלב האפיון והתכנון.</p>\n'
    )
    gate_body += (
        '<div class="card index-cta-needs">'
        '<h2 class="index-cta-needs__h"><a href="what-we-need.html">מה נדרש ממך — לפי עדיפות</a></h2>'
        '<p class="subtitle">כל החומרים, האישורים והשאלות הפתוחות במקום אחד.</p>'
        "</div>\n"
    )
    gate_body += (
        f'<p class="subtitle"><a href="meeting.html">תדריך פגישה</a> · '
        f'<a href="tasks.html">משימות והחלטות, ייצוא JSON</a> · '
        f'<a href="roadmap.html">מפת דרכים</a> · '
        f'<a href="materials-needed.html">חומרים נדרשים</a></p>\n'
    )

    updates_body = ""
    items = updates_items_newest_first(updates)
    if items:
        updates_body += '<ul class="archive-list">\n'
        for it in items[:10]:
            updates_body += (
                f'<li><span class="card-date">{escape(it.get("date",""))}</span> '
                f'<strong>{escape(it.get("titleHe",""))}</strong><br>'
                f'<span class="card-body">{escape(it.get("bodyHe",""))}</span></li>\n'
            )
        updates_body += "</ul>\n"
    else:
        updates_body = '<p class="subtitle">אין עדכונים עדיין — הלוג יתמלא במהלך העבודה על הפרויקט.</p>\n'

    html = head("Sadot — ניב שדות — ממשק מצב עבודה")
    html += nav("index")
    html += '<div class="wrap">\n'
    html += '<div class="hub-build-meta" role="status" aria-label="גרסה ומועד בנייה">\n'
    html += f'<p class="hub-build-meta__line"><span class="hub-build-meta__k">גרסת Hub</span> '
    html += f'<span class="hub-build-meta__v">{escape(hub_version)}</span></p>\n'
    html += f'<p class="hub-build-meta__line"><span class="hub-build-meta__k">עדכון אחרון (בנייה)</span> '
    html += f'<time datetime="{escape(generated_iso)}">{escape(generated_iso)}</time></p>\n'
    html += "</div>\n"
    html += "<h1>Sadot — ניב שדות — ממשק מצב עבודה</h1>\n"
    html += '<p class="subtitle">עיצוב נוף/גינה לבית פרטי, פרדס חנה.</p>\n'
    html += hub_acc_section("idx-gate", "מצב ושער נוכחי", gate_body, open_default=True)
    html += hub_acc_section("idx-stats", "סטטיסטיקה", stats_html)
    html += hub_acc_section("idx-updates", "עדכונים אחרונים", updates_body)
    html += f'<p class="subtitle">מוקד נוכחי: {current_label}</p>\n'
    html += "</div>\n"
    html += foot(generated_iso)
    return html


def page_roadmap(roadmap: dict, generated_iso: str) -> str:
    milestones = roadmap.get("milestones", [])
    current = roadmap.get("currentFocusId", "")

    body = f'<p class="subtitle">{escape(roadmap.get("summaryHe", ""))}</p>\n'

    if milestones:
        body += '<div class="table-wrap"><table class="data">\n'
        body += "<thead><tr><th>קוד</th><th>אבן דרך</th><th>סטטוס</th><th>פירוט</th></tr></thead>\n<tbody>\n"
        for m in milestones:
            row_cls = " class=\"current\"" if m.get("id") == current else ""
            body += (
                f"<tr{row_cls}><td>{escape(m.get('code',''))}</td>"
                f"<td>{escape(m.get('titleHe',''))}</td>"
                f"<td>{status_badge(m.get('status',''))}</td>"
                f"<td>{escape(m.get('detailHe',''))}</td></tr>\n"
            )
        body += "</tbody></table></div>\n"
    else:
        body += '<p class="callout">אבני הדרך טרם הוגדרו. הטבלה תתמלא לאחר קביעת שלבי הפרויקט (אפיון → תכנון → ביצוע → מסירה).</p>\n'

    html = head("מפת דרכים — Sadot")
    html += nav("roadmap")
    html += '<div class="wrap">\n<h1>מפת דרכים</h1>\n'
    html += body
    html += "</div>\n"
    html += foot(generated_iso)
    return html


def page_tasks(tasks: dict, decisions: dict, generated_iso: str) -> str:
    decisions_body = f'<p class="subtitle">{escape(decisions.get("introHe", ""))}</p>\n'
    dlist = decisions.get("decisions", [])
    if dlist:
        for d in dlist:
            inner = "<dl>\n"
            if d.get("contextHe"):
                inner += f"<dt>הקשר</dt><dd>{escape(d['contextHe'])}</dd>\n"
            if d.get("optionsHe"):
                inner += f"<dt>אפשרויות</dt><dd>{escape(d['optionsHe'])}</dd>\n"
            if d.get("implicationsHe"):
                inner += f"<dt>השלכות</dt><dd>{escape(d['implicationsHe'])}</dd>\n"
            if d.get("recommendationHe"):
                inner += f"<dt>המלצה</dt><dd>{escape(d['recommendationHe'])}</dd>\n"
            if d.get("resolutionHe"):
                inner += f"<dt>הכרעה</dt><dd>{escape(d['resolutionHe'])}</dd>\n"
            inner += "</dl>\n"
            inner += (
                '<div class="feedback-field">'
                f'<label for="choice-{escape(d["id"])}">בחירה</label>'
                f'<input type="text" id="choice-{escape(d["id"])}">'
                '</div>\n'
                '<div class="feedback-field">'
                f'<label for="notes-{escape(d["id"])}">הערות</label>'
                f'<textarea id="notes-{escape(d["id"])}"></textarea>'
                '</div>\n'
            )
            title = f'<span class="d-id">{escape(d["id"])}</span> {escape(d.get("titleHe",""))} {status_badge(d.get("status",""))}'
            decisions_body += hub_acc_section(f'dec-{d["id"]}', title, inner)
    else:
        decisions_body += '<p class="callout">אין החלטות פתוחות כרגע.</p>\n'

    decision_ids = [d["id"] for d in dlist]
    decisions_body += (
        '<div class="respondent-field feedback-field">'
        f'<label for="respondent">שם מלא</label>'
        f'<input type="text" id="respondent" value="{escape(DEFAULT_RESPONDENT)}">'
        "</div>\n"
    )
    decisions_body += (
        '<div class="export-section">'
        '<button type="button" class="btn-export" id="btn-export-json">ייצוא כל התשובות ל-JSON</button>'
        f'<p class="subtitle">exportType: <code>{escape(EXPORT_TYPE)}</code></p>'
        "</div>\n"
    )

    tasks_body = ""
    sections = tasks.get("sections", [])
    if sections:
        for sec in sections:
            tasks_body += f"<h3>{escape(sec.get('titleHe',''))}</h3>\n"
            for t in sec.get("tasks", []):
                tasks_body += '<div class="task-row">\n'
                tasks_body += f'<span class="task-title">{escape(t.get("titleHe",""))}</span>\n'
                tasks_body += status_badge(t.get("status", "")) + "\n"
                tasks_body += priority_badge(t.get("priorityHe", "")) + "\n"
                if t.get("stateHe"):
                    tasks_body += f'<span class="task-state">{escape(t["stateHe"])}</span>\n'
                tasks_body += "</div>\n"
    else:
        tasks_body = '<p class="callout">אין משימות רשומות כרגע — הרשימה תתמלא במהלך העבודה על הפרויקט.</p>\n'

    html = head("משימות והחלטות — Sadot")
    html += '<script src="assets/feedback.js"></script>\n'
    html += nav("tasks")
    html += '<div class="wrap">\n<h1>משימות והחלטות</h1>\n'
    html += hub_acc_section("tasks-sec-decisions", f"החלטות (ייצוא {EXPORT_TYPE})", decisions_body, open_default=True)
    html += hub_acc_section("tasks-sec-tasks", "משימות", tasks_body)
    html += "</div>\n"
    html += foot(generated_iso)
    html += (
        f'\n<script>HubFeedback.init({{exportType: {json.dumps(EXPORT_TYPE)}, '
        f'defaultRespondent: {json.dumps(DEFAULT_RESPONDENT)}, '
        f'decisionIds: {json.dumps(decision_ids)}}});</script>\n'
    )
    return html


def page_meeting(brief: dict, generated_iso: str) -> str:
    body = f"<h2>{escape(brief.get('titleHe',''))}</h2>\n"
    if brief.get("meetingDate"):
        body += f'<p class="subtitle">תאריך: {escape(brief["meetingDate"])}</p>\n'
    if brief.get("goalsHe"):
        body += "<h3>מטרות</h3>\n<ul>\n"
        for g in brief["goalsHe"]:
            body += f"<li>{escape(g)}</li>\n"
        body += "</ul>\n"
    if brief.get("agendaHe"):
        body += "<h3>סדר יום</h3>\n<ul>\n"
        for a in brief["agendaHe"]:
            body += f"<li>{escape(a)}</li>\n"
        body += "</ul>\n"
    if brief.get("prepHe"):
        body += f'<p class="callout">{escape(brief["prepHe"])}</p>\n'
    if brief.get("quickLinks"):
        body += "<h3>קישורים מהירים</h3>\n<ul>\n"
        for link in brief["quickLinks"]:
            body += f'<li><a href="{escape(link.get("href","#"))}">{escape(link.get("labelHe",""))}</a></li>\n'
        body += "</ul>\n"
    if not (brief.get("goalsHe") or brief.get("agendaHe")):
        body += '<p class="callout">תדריך הפגישה טרם הוגדר — יתמלא לקראת הפגישה הראשונה.</p>\n'

    html = head("תדריך פגישה — Sadot")
    html += nav("meeting")
    html += '<div class="wrap">\n<h1>תדריך פגישה</h1>\n'
    html += body
    html += "</div>\n"
    html += foot(generated_iso)
    return html


def page_what_we_need(needs: dict, generated_iso: str) -> str:
    body = f'<p class="subtitle">{escape(needs.get("introHe",""))}</p>\n'
    if needs.get("submissionHe"):
        body += f'<p class="callout">{escape(needs["submissionHe"])}</p>\n'

    priorities = needs.get("priorities", [])
    if priorities:
        for p in priorities:
            inner = f'<p class="subtitle">{escape(p.get("whyHe",""))}</p>\n'
            items = p.get("items", [])
            if items:
                inner += '<div class="table-wrap"><table class="data">\n'
                inner += "<thead><tr><th>מזהה</th><th>נושא</th><th>סטטוס</th><th>פעולה</th></tr></thead>\n<tbody>\n"
                for it in items:
                    inner += (
                        f"<tr><td>{escape(it.get('ref',''))}</td>"
                        f"<td>{escape(it.get('titleHe',''))}</td>"
                        f"<td>{status_badge(it.get('status',''))}</td>"
                        f"<td>{escape(it.get('actionHe',''))}</td></tr>\n"
                    )
                inner += "</tbody></table></div>\n"
            title = f'#{p.get("rank","")} — {p.get("titleHe","")}'
            body += hub_acc_section(f'need-{p.get("id","p")}', title, inner)
    else:
        body += '<p class="callout">רשימת העדיפויות טרם אוכלסה — תתמלא במהלך שלב האפיון.</p>\n'

    html = head("מה נדרש ממך — Sadot")
    html += nav("what-we-need")
    html += '<div class="wrap">\n<h1>מה נדרש ממך — לפי עדיפות</h1>\n'
    html += body
    html += "</div>\n"
    html += foot(generated_iso)
    return html


def page_materials_needed(materials: dict, generated_iso: str) -> str:
    body = f'<p class="subtitle">{escape(materials.get("introHe",""))}</p>\n'

    confirmations = materials.get("confirmations", [])
    if confirmations:
        body += "<h2>אישורים</h2>\n"
        for c in confirmations:
            body += (
                f'<div class="card"><div class="card-title">{escape(c.get("label",""))}</div>'
                f'<div class="card-body">{escape(c.get("detail",""))}</div>'
                f'<div class="subtitle">{escape(c.get("status",""))}</div></div>\n'
            )

    groups = materials.get("groups", [])
    if groups:
        for g in groups:
            inner = ""
            for pg in g.get("pages", []):
                inner += f'<p><a href="{escape(pg.get("url","#"))}">{escape(pg.get("label",""))}</a></p>\n'
            items = g.get("items", [])
            if items:
                inner += '<div class="table-wrap"><table class="data">\n'
                inner += "<thead><tr><th>קוד</th><th>נדרש</th><th>עדיפות</th><th>סטטוס</th></tr></thead>\n<tbody>\n"
                for it in items:
                    inner += (
                        f"<tr><td>{escape(it.get('code',''))}</td>"
                        f"<td>{escape(it.get('need',''))}</td>"
                        f"<td>{priority_badge(it.get('priority',''))}</td>"
                        f"<td>{status_badge(it.get('status',''))}</td></tr>\n"
                    )
                inner += "</tbody></table></div>\n"
            body += hub_acc_section(f'mat-{g.get("cluster","g")}', g.get("cluster", ""), inner)
    else:
        body += '<p class="callout">רשימת החומרים הנדרשים טרם אוכלסה — תתמלא במהלך שלב האפיון וסיור השטח.</p>\n'

    html = head("חומרים נדרשים — Sadot")
    html += nav("materials-needed")
    html += '<div class="wrap">\n<h1>חומרים נדרשים</h1>\n'
    html += body
    html += "</div>\n"
    html += foot(generated_iso)
    return html


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build(dist_dir: Path) -> None:
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir(parents=True)

    roadmap = load_json(DATA_DIR / "roadmap.json")
    updates = load_json(DATA_DIR / "updates.json")
    tasks = load_json(DATA_DIR / "tasks.json")
    decisions = load_json(DATA_DIR / "decisions.json")
    meeting_brief = load_json(DATA_DIR / "meeting-brief.json")
    what_we_need = load_json(DATA_DIR / "what-we-need.json")
    materials_needed = load_json(DATA_DIR / "materials-needed.json")
    hub_ver = hub_view_version(DATA_DIR / "hub-version.json")

    generated_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    assets_dir = dist_dir / "assets"
    assets_dir.mkdir()
    for asset_name in ("hub-base.css", "sadot.css", "feedback.js", "hub-form-exports.js"):
        src = SRC_DIR / "assets" / asset_name
        if src.exists():
            shutil.copy2(src, assets_dir / asset_name)
        else:
            print(f"[WARN] Asset not found: {src}")

    (dist_dir / "index.html").write_text(
        page_index(updates, roadmap, tasks, decisions, generated_iso, hub_ver), encoding="utf-8"
    )
    (dist_dir / "roadmap.html").write_text(page_roadmap(roadmap, generated_iso), encoding="utf-8")
    (dist_dir / "tasks.html").write_text(page_tasks(tasks, decisions, generated_iso), encoding="utf-8")
    (dist_dir / "meeting.html").write_text(page_meeting(meeting_brief, generated_iso), encoding="utf-8")
    (dist_dir / "what-we-need.html").write_text(
        page_what_we_need(what_we_need, generated_iso), encoding="utf-8"
    )
    (dist_dir / "materials-needed.html").write_text(
        page_materials_needed(materials_needed, generated_iso), encoding="utf-8"
    )

    (dist_dir / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")

    metadata = {
        "generatedAt": generated_iso,
        "hubVersion": hub_ver,
        "schemaVersion": 1,
        "project": PROJECT_META,
    }
    (dist_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    data_out = dist_dir / "data"
    data_out.mkdir()
    for name in (
        "roadmap.json",
        "updates.json",
        "tasks.json",
        "decisions.json",
        "meeting-brief.json",
        "what-we-need.json",
        "materials-needed.json",
        "hub-version.json",
    ):
        src = DATA_DIR / name
        if src.exists():
            shutil.copy2(src, data_out / name)

    print(f"[OK] Hub built -> {dist_dir}")
    print(f"     Generated: {generated_iso}")
    file_count = sum(1 for _ in dist_dir.rglob("*") if _.is_file())
    print(f"     Files: {file_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build Sadot client hub")
    parser.add_argument("--out", type=str, default=None, help="Output directory")
    args = parser.parse_args()

    out = Path(args.out) if args.out else DEFAULT_DIST
    build(out)
