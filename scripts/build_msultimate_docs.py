#!/usr/bin/env python3
"""
MSUltimate Documentation Site Builder
Reads markdown documentation under assets/Documentations/MSUltimate/ and
assets/Notice/MSUltimate_Core_Community_EULA.md, resolves cross-document links,
renders Graphite+Amber HTML pages + category/package explorers + search index,
and verifies all generated internal/cross-page links.

Usage:
    python scripts/build_msultimate_docs.py
"""

from __future__ import annotations

import html
import json
import os
import re
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
DOCS_ROOT = WORKSPACE / "assets" / "Documentations" / "MSUltimate"
COMPARISON_MD = WORKSPACE / "assets" / "Descriptions" / "MSUltimate_Ecosystem_Comparison_Guide.md"
EULA_MD = WORKSPACE / "assets" / "Notice" / "MSUltimate_Core_Community_EULA.md"

EMOJI_RE = re.compile(
    r"[\U0001F300-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+",
    flags=re.UNICODE,
)

CATEGORY_LABELS = {
    # Core
    "groups-and-layouts": "Groups & Layouts",
    "conditional": "Conditional Visibility",
    "fields": "Specialized Fields",
    "buttons": "Buttons & Actions",
    "collections": "Collections",
    "types": "Serializers & Extended Types",
    "validation": "Core Validation",
    "callbacks": "Callbacks & Events",
    "decorators": "Decorators & Visuals",
    "scene-debug": "Scene & Gizmo Debug",
    "windowing": "Windowing",
    "advanced": "Advanced",
    "core": "Core Base & Infrastructure",
    "others": "Utilities",
    # Animated
    "core-animated": "Core Animated & Base",
    "combat-and-hud": "Combat & HUD",
    "scifi-and-fx": "Sci-Fi & FX",
    "particle-simulations": "Particle Simulations",
    "typography": "Kinetic Typography",
    "data-visualizers": "Data Visualizers",
    "feedback-and-alerts": "Feedback & Alerts",
    "gamification": "Gamification",
    "physics-and-interactions": "Physics & Interactions",
    "audio-and-haptics": "Audio & Haptics",
    "productivity": "Productivity",
    "spatial-controls": "Spatial Controls",
    "transitions": "Transitions",
    # Component
    "core-styling": "Core Component Styling",
    "atmospheric-vfx": "Atmospheric VFX",
    "header-controls": "Header Controls",
    "layout-and-ergonomics": "Layout & Ergonomics",
    "safety-and-architecture": "Safety & Architecture",
    "sensory-and-audio": "Sensory & Audio",
    "themes-and-shells": "Themes & Genre Shells",
    # Hierarchy
    "core-hierarchy": "Core Hierarchy",
    "tree-and-structure": "Tree & Structure",
    "telemetry-and-visualizers": "Telemetry & Visualizers",
    "diagnostics-and-performance": "Diagnostics & Performance",
    "interactions-and-tools": "Interactions & Tools",
    "styling-and-vfx": "Styling & VFX",
    "typography-and-naming": "Typography & Naming",
    "validation-and-safety": "Validation & Safety",
    # Customizer chapters
    "01-getting-started": "01 · Getting Started",
    "02-inspector-customizer-window": "02 · Customizer Window",
    "03-makeover-graph": "03 · Makeover Graph",
    "04-ai-decorator": "04 · Multi-LLM AI Decorator",
    "05-templates-and-recipes": "05 · Templates & Recipes",
    "06-code-baking": "06 · C# Code Baking",
    "07-component-defaults-and-rules": "07 · Defaults & Ignore Rules",
    "08-workflows-and-context-menus": "08 · Workflows & Context Menus",
    "09-preferences-and-settings": "09 · Preferences & Settings",
}

CORE_CAT_ORDER = [
    "groups-and-layouts",
    "conditional",
    "fields",
    "buttons",
    "collections",
    "types",
    "validation",
    "callbacks",
    "decorators",
    "scene-debug",
    "windowing",
    "advanced",
    "core",
    "others",
]

# Populated before rendering HTML: norm_md_path -> (doc_page, slug, title)
LINK_REGISTRY: dict[str, tuple[str, str, str]] = {}


def strip_emoji(text: str, strip_edges: bool = True) -> str:
    cleaned = EMOJI_RE.sub("", text)
    cleaned = cleaned.replace("\ufe0f", "").replace("\u200d", "")
    cleaned = re.sub(r" {2,}", " ", cleaned)
    return cleaned.strip() if strip_edges else cleaned


def clean_latex_expr(expr: str) -> tuple[str, bool]:
    raw = expr.strip()
    if raw in (r"\rightarrow", r"\to"):
        return "→", False
    if raw == r"\leftarrow":
        return "←", False
    if raw == r"\leftrightarrow":
        return "↔", False
    if raw in (r"\le", r"\leq"):
        return "≤", False
    if raw in (r"\ge", r"\geq"):
        return "≥", False
    if raw == r"\times":
        return "×", False
    if raw == r"\Delta":
        return "Δ", False

    s = raw
    s = re.sub(r"\\text\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\frac\{([^}]*)\}\{([^}]*)\}", r"(\1) / (\2)", s)
    s = s.replace(r"\rightarrow", "→").replace(r"\to", "→")
    s = s.replace(r"\leftarrow", "←")
    s = s.replace(r"\cdot", "·").replace(r"\times", "×")
    s = s.replace(r"\sin", "sin").replace(r"\cos", "cos")
    s = s.replace(r"\pi", "π").replace(r"\Delta", "Δ")
    s = s.replace(r"\le", "≤").replace(r"\ge", "≥")
    s = s.replace(r"\infty", "∞").replace("^2", "²").replace("^3", "³")
    s = re.sub(r"\s+", " ", s).strip()
    is_formula = any(c in s for c in ("=", "/", "sin", "cos", "²", "³", "+", "(", "px/s", "m/s", "ms"))
    return s, is_formula


def slugify(name: str) -> str:
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "section"


def human_title_from_md(md_text: str, fallback_stem: str) -> str:
    for line in md_text.splitlines():
        m = re.match(r"^\s*#\s+(.+?)\s*$", line)
        if m:
            t = strip_emoji(m.group(1))
            return t.replace("`", "").strip()
    return fallback_stem.replace("-", " ").replace("_", " ").title()


def extract_description(md_text: str) -> str:
    in_code = False
    for line in md_text.splitlines():
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s or s.startswith("#") or s.startswith("---"):
            continue
        if s.startswith("|") or s.startswith("├──") or s.startswith("└"):
            continue
        if s.startswith(">"):
            s = s.lstrip(">").strip()
            if not s:
                continue
        s = strip_emoji(s)
        s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
        s = s.replace("`", "").replace("**", "").replace("*", "")
        s = re.sub(r"\s+", " ", s).strip()
        if len(s) > 15:
            return s[:220] + ("..." if len(s) > 220 else "")
    return ""


def extract_blockquote_summary(md_text: str) -> str:
    lines = []
    started = False
    for line in md_text.splitlines():
        s = line.strip()
        if s.startswith(">"):
            started = True
            txt = strip_emoji(s.lstrip(">").strip())
            txt = re.sub(r"\*\*([^*]+)\*\*", r"\1", txt).replace("`", "")
            if txt:
                lines.append(txt)
        elif started:
            break
    return " ".join(lines)


def resolve_href(raw_href: str, src_path: Path, current_page: str) -> tuple[str, bool]:
    href = raw_href.strip()
    if href.startswith(("http://", "https://", "mailto:")):
        return href, True
    if href.endswith(".html") or ".html#" in href:
        return href, False
    if href.startswith("#"):
        return href, False

    path_part, _, _ = href.partition("#")
    target = (src_path.parent / path_part).resolve()
    key = os.path.normcase(os.path.normpath(str(target)))
    if key in LINK_REGISTRY:
        t_page, t_slug, _ = LINK_REGISTRY[key]
        return (f"#{t_slug}" if t_page == current_page else f"{t_page}#{t_slug}"), False

    alias_pages = {
        "msultimate-animatedattributes": "msultimate-animated-docs.html",
        "msultimate-componentdesigner": "msultimate-component-docs.html",
        "msultimate-hierarchydesigner": "msultimate-hierarchy-docs.html",
        "msultimate-validationmodule": "msultimate-validation-docs.html",
        "msultimate-inspectorcustomizer": "msultimate-customizer-docs.html",
        "msultimate-toolbox-vol1": "msultimate-toolbox-docs.html",
    }
    lower_href = path_part.lower()
    for alias, page in alias_pages.items():
        if alias in lower_href:
            return f"{page}#overview", False

    if target.is_dir():
        idx_key = os.path.normcase(os.path.normpath(str(target / "index.md")))
        if idx_key in LINK_REGISTRY:
            t_page, t_slug, _ = LINK_REGISTRY[idx_key]
            return (f"#{t_slug}" if t_page == current_page else f"{t_page}#{t_slug}"), False

    return ("#" + slugify(Path(path_part).stem) if path_part else raw_href), False


def format_inline(text: str, src_path: Path, current_page: str) -> str:
    tokens: list[str] = []

    def stash(html_snip: str) -> str:
        idx = len(tokens)
        tokens.append(html_snip)
        return f"\x00TOK{idx}\x00"

    def finalize_string(chunk: str) -> str:
        cleaned = strip_emoji(chunk, strip_edges=False)
        escaped = html.escape(cleaned, quote=False)
        escaped = re.sub(r"\*\*([^\n*]+?)\*\*", r"<strong>\1</strong>", escaped)
        escaped = re.sub(
            r"(?<![A-Za-z0-9])\*([^\s*][^*\n]*?[^\s*]|\S)\*(?![A-Za-z0-9])",
            r"<em>\1</em>",
            escaped,
        )
        return re.sub(r"\x00TOK(\d+)\x00", lambda mt: tokens[int(mt.group(1))], escaped)

    def repl_code(m: re.Match) -> str:
        code_body = html.escape(m.group(1), quote=False)
        return stash(f"<code>{code_body}</code>")

    s = re.sub(r"`([^`]+)`", repl_code, text)

    def repl_math(m: re.Match) -> str:
        txt, is_formula = clean_latex_expr(m.group(1))
        esc = html.escape(strip_emoji(txt), quote=False)
        if is_formula:
            return stash(f'<code class="math-expr">{esc}</code>')
        return stash(esc)

    s = re.sub(r"\$([^$\n]+)\$", repl_math, s)

    def repl_link_clean(m: re.Match) -> str:
        label_raw = m.group(1)
        href_raw = m.group(2)
        resolved, is_ext = resolve_href(href_raw, src_path, current_page)
        label_html = finalize_string(label_raw)
        attrs = ' target="_blank" rel="noopener"' if is_ext else ""
        return stash(f'<a href="{html.escape(resolved, quote=True)}"{attrs}>{label_html}</a>')

    s = re.sub(r"\[((?:[^\[\]]|\[[^\[\]]*\])+)\]\(([^)]+)\)", repl_link_clean, s)
    return finalize_string(s)


def parse_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [c.strip() for c in stripped.split("|")]


def md_to_html(
    md_text: str,
    src_path: Path,
    current_page: str,
    strip_first_h1: bool = True,
    omit_sections: set[str] | None = None,
) -> str:
    """Convert CommonMark/GFM markdown into semantic studio.css HTML."""
    lines = md_text.splitlines()
    out: list[str] = []
    i = 0
    n = len(lines)
    removed_h1 = False
    omit_lower = {s.lower() for s in omit_sections} if omit_sections else set()

    def is_table_start(idx: int) -> bool:
        if idx + 1 >= n:
            return False
        l1 = lines[idx].strip()
        l2 = lines[idx + 1].strip()
        if "|" not in l1 or "|" not in l2:
            return False
        return bool(re.match(r"^\|?[\s:\-|]+\|?$", l2)) and "-" in l2

    skip_until_h2 = False

    while i < n:
        line = lines[i]
        stripped = line.strip()

        hm = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if hm:
            lvl = len(hm.group(1))
            heading_txt = hm.group(2).strip()
            clean_h = strip_emoji(heading_txt).lower()
            if lvl == 2:
                skip_until_h2 = any(clean_h.startswith(prefix) for prefix in omit_lower)
                if skip_until_h2:
                    i += 1
                    continue

        if skip_until_h2:
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            lang = stripped[3:].strip() or "text"
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            code_str = html.escape("\n".join(code_lines), quote=False)
            lang_label = html.escape(lang.upper() if len(lang) <= 5 else lang, quote=False)
            out.append(
                '<div class="code-block-wrapper">'
                '<div class="code-block-bar">'
                f"<span>{lang_label}</span>"
                '<button type="button" class="copy-code-btn" aria-label="Copy code">'
                '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                '<rect width="14" height="14" x="8" y="8" rx="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>'
                '</svg><span class="copy-label">Copy</span></button></div>'
                f"<pre><code>{code_str}</code></pre></div>"
            )
            continue

        if re.match(r"^(\-{3,}|\*{3,}|_{3,})$", stripped):
            # Avoid duplicate divider directly under leading blockquote
            if out and out[-1].startswith("<blockquote>") and len(out) <= 2:
                i += 1
                continue
            out.append("<hr>")
            i += 1
            continue

        if hm:
            lvl = len(hm.group(1))
            heading_txt = hm.group(2).strip()
            if lvl == 1 and strip_first_h1 and not removed_h1:
                removed_h1 = True
                i += 1
                continue
            out.append(f"<h{lvl}>{format_inline(heading_txt, src_path, current_page)}</h{lvl}>")
            i += 1
            continue

        if stripped.startswith(">"):
            bq_lines = []
            while i < n and lines[i].strip().startswith(">"):
                content = lines[i].strip()[1:].lstrip()
                bq_lines.append(content)
                i += 1
            p_groups: list[list[str]] = [[]]
            for bl in bq_lines:
                if not bl:
                    if p_groups[-1]:
                        p_groups.append([])
                else:
                    p_groups[-1].append(bl)
            p_html = []
            for grp in p_groups:
                if not grp:
                    continue
                joined = "<br>".join(format_inline(g, src_path, current_page) for g in grp)
                p_html.append(f"<p>{joined}</p>")
            out.append(f"<blockquote>{''.join(p_html)}</blockquote>")
            continue

        if is_table_start(i):
            headers = parse_table_row(lines[i])
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(parse_table_row(lines[i]))
                i += 1
            # Clean redundant Status columns with stripped emoji text ("Complete")
            status_col_idx = next((idx for idx, h in enumerate(headers) if h.strip().lower() == "status"), None)
            th_html = "".join(f"<th>{format_inline(h, src_path, current_page)}</th>" for h in headers)
            tr_html = []
            for r in rows:
                padded = r + [""] * (len(headers) - len(r))
                tds = []
                for c_idx, cell in enumerate(padded[: len(headers)]):
                    clean_c = strip_emoji(cell).strip()
                    if status_col_idx is not None and c_idx == status_col_idx and clean_c.lower() in ("complete", "verified", "ready"):
                        tds.append('<td><span class="tag tag-positive">Documented</span></td>')
                    else:
                        tds.append(f"<td>{format_inline(cell, src_path, current_page)}</td>")
                tr_html.append(f"<tr>{''.join(tds)}</tr>")
            out.append(
                '<div class="doc-table-wrap"><table class="studio-table">'
                f"<thead><tr>{th_html}</tr></thead>"
                f"<tbody>{''.join(tr_html)}</tbody>"
                "</table></div>"
            )
            continue

        lm = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.+)$", line)
        if lm:
            def render_list(start_idx: int, base_indent: int) -> tuple[str, int]:
                items: list[str] = []
                first_marker = re.match(r"^(\s*)([-*+]|\d+\.)\s+", lines[start_idx]).group(2)
                tag = "ol" if first_marker.endswith(".") else "ul"
                j = start_idx
                while j < n:
                    cur = lines[j]
                    if not cur.strip():
                        k = j + 1
                        while k < n and not lines[k].strip():
                            k += 1
                        if k < n and re.match(r"^(\s*)([-*+]|\d+\.)\s+", lines[k]):
                            j = k
                            continue
                        break
                    m_cur = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.+)$", cur)
                    if not m_cur:
                        break
                    ind = len(m_cur.group(1).replace("\t", "  "))
                    cur_tag = "ol" if m_cur.group(2).endswith(".") else "ul"
                    if ind < base_indent or (ind == base_indent and cur_tag != tag):
                        break
                    if ind > base_indent:
                        sub_html, j = render_list(j, ind)
                        if items:
                            items[-1] = items[-1][:-5] + sub_html + "</li>"
                        else:
                            items.append(f"<li>{sub_html}</li>")
                        continue
                    item_html = format_inline(m_cur.group(3), src_path, current_page)
                    items.append(f"<li>{item_html}</li>")
                    j += 1
                return f"<{tag}>{''.join(items)}</{tag}>", j

            base_ind = len(lm.group(1).replace("\t", "  "))
            list_html, i = render_list(i, base_ind)
            out.append(list_html)
            continue

        p_lines = []
        while i < n:
            cur = lines[i]
            cur_s = cur.strip()
            if (
                not cur_s
                or cur_s.startswith("```")
                or cur_s.startswith(">")
                or re.match(r"^#{1,4}\s+", cur_s)
                or re.match(r"^(\-{3,}|\*{3,}|_{3,})$", cur_s)
                or re.match(r"^(\s*)([-*+]|\d+\.)\s+", cur)
                or is_table_start(i)
            ):
                break
            p_lines.append(cur_s)
            i += 1
        out.append(f"<p>{' '.join(format_inline(p, src_path, current_page) for p in p_lines)}</p>")

    return "\n".join(out)


def parse_directory_table(md_text: str, src_path: Path) -> list[dict]:
    """Extract structured rows from an index.md attribute directory table."""
    lines = md_text.splitlines()
    rows_out = []
    i = 0
    n = len(lines)
    while i + 1 < n:
        l1 = lines[i].strip()
        l2 = lines[i + 1].strip()
        if "|" in l1 and "|" in l2 and re.match(r"^\|?[\s:\-|]+\|?$", l2) and "-" in l2:
            headers = [h.strip().lower() for h in parse_table_row(l1)]
            if "attribute" in headers and "description" in headers:
                i += 2
                while i < n and "|" in lines[i] and lines[i].strip():
                    cells = parse_table_row(lines[i])
                    row_map = {headers[k]: (cells[k] if k < len(cells) else "") for k in range(len(headers))}
                    attr_raw = row_map.get("attribute", "")
                    m = re.search(r"\[(.+)\]\(([^)\s]+)\)", attr_raw.strip())
                    label = strip_emoji(m.group(1)).replace("`", "").replace("**", "").strip() if m else strip_emoji(attr_raw).replace("`", "")
                    href_raw = m.group(2).strip() if m else ""
                    if not href_raw:
                        for col_k, col_v in row_map.items():
                            if col_k != "attribute":
                                lm = re.search(r"\[([^\]]+)\]\(([^)\s]+)\)", col_v.strip())
                                if lm:
                                    href_raw = lm.group(2).strip()
                                    break
                    target_raw = row_map.get("target", "").replace("`", "").strip()
                    tool_raw = row_map.get("tool system", "").replace("`", "").strip()
                    desc_raw = row_map.get("description", "")
                    rows_out.append({
                        "label": label,
                        "href_raw": href_raw,
                        "target": target_raw,
                        "tool": tool_raw,
                        "desc_raw": desc_raw,
                    })
                    i += 1
                continue
        i += 1
    return rows_out


def extract_attr_target_fallback(md_text: str) -> str:
    m = re.search(r"\|\s*\*\*Attribute Target\*\*\s*\|\s*`?([^|\n]+?)`?\s*\|", md_text)
    return m.group(1).strip() if m else ""


def render_category_index_body(entry: dict, child_entries: list[dict], doc_page: str) -> str:
    """Render intro prose + live interactive Attribute Filter Explorer for category index.md."""
    md_txt = entry["md"]
    src_path = entry["path"]
    intro_html = md_to_html(
        md_txt,
        src_path,
        doc_page,
        strip_first_h1=True,
        omit_sections={"attribute directory"},
    )

    dir_rows = parse_directory_table(md_txt, src_path)
    items = []
    if dir_rows:
        for r in dir_rows:
            resolved, _ = resolve_href(r["href_raw"], src_path, doc_page)
            if not resolved or resolved == "#" or resolved.startswith("#cat-"):
                clean_lbl = r["label"].replace("[", "").replace("]", "").strip().lower()
                for child in child_entries:
                    ch_clean = child["title"].replace("[", "").replace("]", "").strip().lower()
                    if clean_lbl == ch_clean or clean_lbl.replace(" ", "-") == child["slug"] or clean_lbl == child["slug"].replace("-", ""):
                        resolved = f"#{child['slug']}"
                        break
            items.append({
                "label": r["label"],
                "href": resolved,
                "target": r["target"] or "Member",
                "tool": r["tool"],
                "desc_html": format_inline(r["desc_raw"], src_path, doc_page),
                "search_text": f"{r['label']} {r['target']} {r['tool']} {r['desc_raw']}".lower(),
            })
    else:
        for child in child_entries:
            tgt = extract_attr_target_fallback(child["md"]) or "Member"
            items.append({
                "label": child["title"],
                "href": f"#{child['slug']}",
                "target": tgt,
                "tool": "",
                "desc_html": html.escape(child["desc"]),
                "search_text": f"{child['title']} {tgt} {child['desc']}".lower(),
            })

    # Collect distinct atomic targets (split by '/' or ',' or '|')
    target_counts: dict[str, int] = {}
    row_target_tokens = []
    for it in items:
        parts = [p.strip() for p in re.split(r"[/,|]+", it["target"]) if p.strip()]
        row_target_tokens.append("|".join(p.lower() for p in parts))
        for p in parts:
            target_counts[p] = target_counts.get(p, 0) + 1

    has_tool_col = any(it["tool"] for it in items)
    cat_label = entry.get("cat_label") or entry["category"]

    pills_html = ['<button type="button" class="cat-target-pill is-active" data-target-filter="all">All</button>']
    if len(target_counts) > 1:
        for tgt, cnt in sorted(target_counts.items(), key=lambda kv: (-kv[1], kv[0])):
            pills_html.append(
                f'<button type="button" class="cat-target-pill" data-target-filter="{html.escape(tgt.lower(), quote=True)}">'
                f'{html.escape(tgt)} ({cnt})</button>'
            )

    rows_html = []
    for idx, it in enumerate(items):
        tool_td = f'<td class="mono">{html.escape(it["tool"])}</td>' if has_tool_col else ""
        raw_targets = [t.strip() for t in it["target"].split(",") if t.strip()]
        if len(raw_targets) > 1:
            target_pills = "".join(f'<span class="tag">{html.escape(t)}</span>' for t in raw_targets)
            target_td = f'<td><div class="tag-group">{target_pills}</div></td>'
        else:
            target_td = f'<td><span class="tag">{html.escape(it["target"])}</span></td>'
        rows_html.append(
            f'<tr data-cat-row data-cat-targets="{html.escape(row_target_tokens[idx], quote=True)}" '
            f'data-cat-search="{html.escape(it["search_text"], quote=True)}">'
            f'<td class="mono"><a href="{html.escape(it["href"], quote=True)}"><strong>{html.escape(it["label"])}</strong></a></td>'
            f'{target_td}'
            f'{tool_td}'
            f'<td>{it["desc_html"]}</td>'
            '</tr>'
        )

    tool_th = "<th>Tool System</th>" if has_tool_col else ""
    explorer_html = (
        '<div data-cat-explorer>'
        '<div class="cat-filter-bar">'
        f'<input type="search" class="cat-filter-input" placeholder="Filter {len(items)} entries in {html.escape(cat_label)}..." aria-label="Filter {html.escape(cat_label)}">'
        f'<div class="cat-target-pills">{"".join(pills_html)}</div>'
        f'<span class="cat-filter-count">Showing {len(items)} of {len(items)}</span>'
        '</div>'
        '<div class="doc-table-wrap"><table class="studio-table">'
        f'<thead><tr><th>Attribute</th><th>Target</th>{tool_th}<th>Description</th></tr></thead>'
        f'<tbody>{"".join(rows_html)}</tbody>'
        '</table></div>'
        '</div>'
    )

    return f"{intro_html}\n{explorer_html}"


def render_package_overview_body(entry: dict, cat_groups: list[tuple[str, str, dict | None, list[dict]]], doc_page: str) -> str:
    """Render package overview prose plus interactive Category Explorer Cards."""
    intro_html = md_to_html(
        entry["md"],
        entry["path"],
        doc_page,
        strip_first_h1=True,
        omit_sections={"core attribute categories", "feature categories"},
    )

    cards_html = []
    for _, cat_label, cat_entry, entries in cat_groups:
        if not cat_entry and not entries:
            continue
        target_hash = f"#{cat_entry['slug']}" if cat_entry else f"#{entries[0]['slug']}"
        summary = cat_entry.get("summary") or cat_entry.get("desc") if cat_entry else ""
        chips = "".join(
            f'<a href="#{html.escape(e["slug"], quote=True)}" class="doc-index-chip">{html.escape(e["title"])}</a>'
            for e in entries[:4]
        )
        more = f'<span class="doc-index-chip" style="color: var(--text-muted);">+{len(entries) - 4} more</span>' if len(entries) > 4 else ""
        cards_html.append(
            '<div class="doc-index-card">'
            '<div class="doc-index-card-head">'
            f'<a href="{target_hash}" class="doc-index-card-title">{html.escape(cat_label)}</a>'
            f'<span class="tag tag-accent mono">{len(entries)}</span>'
            '</div>'
            f'<p class="doc-index-card-desc">{html.escape(summary or f"Browse all {len(entries)} entries in {cat_label}.")}</p>'
            f'<div class="doc-index-chips">{chips}{more}</div>'
            '</div>'
        )

    heading = "<h2>Browse by Category</h2>" if cards_html else ""
    grid = f'<div class="doc-index-grid">{"".join(cards_html)}</div>' if cards_html else ""
    return f"{intro_html}\n{heading}\n{grid}"


def render_nav(active_dropdown_href: str = "msultimate.html") -> str:
    return f"""    <nav class="site-nav" aria-label="Main navigation">
        <div class="container nav-inner">
            <a class="brand" href="index.html">
                <span class="brand-mark" aria-hidden="true">MS</span>
                <span>Maharaja Studio</span>
            </a>

            <ul class="nav-menu">
                <li><a class="nav-link" href="index.html">Home</a></li>
                <li class="nav-dropdown">
                    <button type="button" class="nav-link" data-dropdown-trigger aria-expanded="false" aria-haspopup="true">
                        Assets
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
                    </button>
                    <div class="nav-dropdown-panel" role="menu">
                        <a class="nav-dropdown-item{' is-current' if active_dropdown_href == 'msultimate.html' else ''}" href="msultimate.html" role="menuitem">
                            <span class="nav-dropdown-thumb"><img src="assets/Images/MSUltimate_Logo.png" alt=""></span>
                            <span>
                                <span class="nav-dropdown-title">MSUltimate Ecosystem</span>
                                <span class="nav-dropdown-meta">454+ attributes · Core &amp; 6 addons</span>
                            </span>
                        </a>
                        <a class="nav-dropdown-item" href="ms-motion.html" role="menuitem">
                            <span class="nav-dropdown-thumb"><img src="assets/Images/MSMotion_Logo.png" alt=""></span>
                            <span>
                                <span class="nav-dropdown-title">MSMotion v2.0</span>
                                <span class="nav-dropdown-meta">Multi-actor choreography &amp; FX</span>
                            </span>
                        </a>
                        <a class="nav-dropdown-item" href="scriptable-studio-pro.html" role="menuitem">
                            <span class="nav-dropdown-thumb"><img src="assets/Images/ScriptableStudioPro_Logo.png" alt=""></span>
                            <span>
                                <span class="nav-dropdown-title">Scriptable Studio Pro v4.5</span>
                                <span class="nav-dropdown-meta">Grid editor &amp; Prefab Studio</span>
                            </span>
                        </a>
                        <a class="nav-dropdown-item" href="tactical-cover-retreat-ai-system.html" role="menuitem">
                            <span class="nav-dropdown-thumb"><img src="assets/Images/Tactical_Cover_&_Retreat_AI_System_Logo.png" alt=""></span>
                            <span>
                                <span class="nav-dropdown-title">Tactical Cover &amp; Retreat AI</span>
                                <span class="nav-dropdown-meta">v3.0 squad maneuvers &amp; cover</span>
                            </span>
                        </a>
                        <a class="nav-dropdown-item" href="object-finder-pro.html" role="menuitem">
                            <span class="nav-dropdown-thumb"><img src="assets/Images/ObjectFinderPro_Logo.png" alt=""></span>
                            <span>
                                <span class="nav-dropdown-title">Object Finder Pro</span>
                                <span class="nav-dropdown-meta">Async query &amp; reference search</span>
                            </span>
                        </a>
                        <a class="nav-dropdown-item" href="ultimate-quick-inspector.html" role="menuitem">
                            <span class="nav-dropdown-thumb"><img src="assets/Images/UltimateQuickInspector_Logo.png" alt=""></span>
                            <span>
                                <span class="nav-dropdown-title">Ultimate Quick Inspector</span>
                                <span class="nav-dropdown-meta">Multi-page GUID pin drawer</span>
                            </span>
                        </a>
                    </div>
                </li>
                <li><a class="nav-link active" href="documentation.html">Documentation</a></li>
                <li><a class="nav-link" href="support.html">Support</a></li>
                <li><a class="nav-link" href="contact.html">Contact</a></li>
            </ul>

            <div class="nav-actions">
                <button type="button" class="theme-btn" data-theme-toggle aria-label="Switch theme">
                    <svg class="icon-moon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>
                    <svg class="icon-sun" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>
                </button>
                <a class="btn btn-primary btn-sm" href="msultimate.html#editions">Editions</a>
                <button type="button" class="mobile-menu-btn" data-mobile-menu-toggle aria-label="Toggle navigation menu" aria-expanded="false">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="7" y2="7"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="17" y2="17"/></svg>
                </button>
            </div>
        </div>
    </nav>

    <div class="mobile-drawer" aria-label="Mobile navigation">
        <div class="mobile-drawer-group">
            <span class="mobile-drawer-label">Navigation</span>
            <a href="index.html">Home</a>
            <a href="documentation.html" class="active">Documentation</a>
            <a href="support.html">Support</a>
            <a href="contact.html">Contact</a>
        </div>
        <div class="mobile-drawer-group">
            <span class="mobile-drawer-label">MSUltimate Docs</span>
            <a href="msultimate.html">MSUltimate Overview</a>
            <a href="msultimate-docs.html">Ecosystem Docs Hub</a>
            <a href="msultimate-core-docs.html">Core Framework (156+)</a>
            <a href="msultimate-animated-docs.html">Animated Attributes (99)</a>
            <a href="msultimate-component-docs.html">Component Designer (74)</a>
            <a href="msultimate-hierarchy-docs.html">Hierarchy Designer (82)</a>
            <a href="msultimate-validation-docs.html">Validation Module (39)</a>
            <a href="msultimate-customizer-docs.html">Inspector Customizer (30 Guides)</a>
            <a href="msultimate-toolbox-docs.html">ToolBox Vol. 1 (4 Tools + 4)</a>
            <a href="msultimate-license.html">License &amp; Community EULA</a>
        </div>
    </div>"""


ECO_TABS = [
    ("msultimate-docs.html", "Hub", "454+"),
    ("msultimate-core-docs.html", "Core", "156+"),
    ("msultimate-animated-docs.html", "Animated", "99"),
    ("msultimate-component-docs.html", "Component", "74"),
    ("msultimate-hierarchy-docs.html", "Hierarchy", "82"),
    ("msultimate-validation-docs.html", "Validation", "39"),
    ("msultimate-customizer-docs.html", "Customizer", "30 guides"),
    ("msultimate-toolbox-docs.html", "ToolBox Vol. 1", "4 tools"),
    ("msultimate-license.html", "License", "EULA"),
]


def render_eco_subnav(current_page: str) -> str:
    links = []
    for href, label, badge in ECO_TABS:
        cls = "eco-pill is-active" if href == current_page else "eco-pill"
        links.append(
            f'<a href="{href}" class="{cls}"><span>{html.escape(label)}</span>'
            f'<span class="eco-pill-count">{html.escape(badge)}</span></a>'
        )
    return (
        '    <div class="eco-subnav" aria-label="MSUltimate documentation packages">\n'
        '        <div class="container">\n'
        f'            <div class="eco-subnav-inner">{"".join(links)}</div>\n'
        '        </div>\n'
        '    </div>'
    )


def render_footer() -> str:
    return """    <footer class="site-footer">
        <div class="container footer-inner">
            <div>
                <span>&copy; 2026 Maharaja Studio. All rights reserved.</span>
                <span style="margin: 0 8px;">·</span>
                <a href="msultimate.html" style="color: var(--text-secondary);">MSUltimate Overview</a>
                <span style="margin: 0 8px;">·</span>
                <a href="msultimate-license.html" style="color: var(--text-secondary);">License &amp; EULA</a>
            </div>
            <div class="footer-links">
                <a href="https://youtube.com/@king_of_games-l9e?si=EleZSFthz6ZBPPao" target="_blank" rel="noopener">YouTube</a>
                <a href="https://discord.gg/GamF5bez3h" target="_blank" rel="noopener">Discord</a>
                <a href="mailto:maharajastudiocustomerservice@gmail.com">Email</a>
            </div>
        </div>
    </footer>"""


def make_entry(fp: Path, slug: str, title: str, cat_label: str, is_pkg_overview: bool = False, is_cat_index: bool = False) -> dict:
    md_txt = fp.read_text(encoding="utf-8", errors="replace")
    return {
        "slug": slug,
        "title": title,
        "raw_name": title.replace("[", "").replace("]", ""),
        "category": cat_label,
        "cat_label": cat_label,
        "path": fp,
        "md": md_txt,
        "desc": extract_description(md_txt),
        "summary": extract_blockquote_summary(md_txt),
        "is_pkg_overview": is_pkg_overview,
        "is_cat_index": is_cat_index,
        "cat_slug": "",
    }


def collect_attribute_package(pkg_name: str, doc_page: str, base_dir: Path, cat_order: list[str] | None = None):
    used_slugs: set[str] = set()

    def alloc_slug(desired: str, cat_prefix: str) -> str:
        s = slugify(desired)
        if s not in used_slugs:
            used_slugs.add(s)
            return s
        s2 = slugify(f"{cat_prefix}-{desired}")
        used_slugs.add(s2)
        return s2

    pinned_entries: list[dict] = []
    main_idx = base_dir / "index.md"
    if main_idx.exists():
        ov_title = f"{pkg_name} Overview" if pkg_name == "Core Framework" else human_title_from_md(main_idx.read_text(encoding="utf-8", errors="replace"), f"{pkg_name} Overview")
        pinned_entries.append(make_entry(main_idx, alloc_slug("overview", "pkg"), ov_title, "Overview", is_pkg_overview=True))

    if pkg_name == "Core Framework":
        for fname, sl, fallback in [
            ("core-systems/index.md", "core-systems", "Core Systems Architecture"),
            ("tutorials/index.md", "tutorials", "Tutorials & Recipes"),
            ("packages-comparison.md", "packages-comparison", "Ecosystem Comparison Guide"),
        ]:
            fp = base_dir / fname
            if fp.exists():
                t = human_title_from_md(fp.read_text(encoding="utf-8", errors="replace"), fallback)
                pinned_entries.append(make_entry(fp, alloc_slug(sl, "ov"), t, "Overview & Architecture"))
    elif pkg_name == "Validation Module":
        for fname, sl, fallback in [
            ("tools/validation-engine/index.md", "validation-engine", "ValidationEngine & ValidationWindow"),
            ("custom-rules/index.md", "custom-rules", "Authoring Custom Rules"),
        ]:
            fp = base_dir / fname
            if fp.exists():
                t = human_title_from_md(fp.read_text(encoding="utf-8", errors="replace"), fallback)
                pinned_entries.append(make_entry(fp, alloc_slug(sl, "ov"), t, "Engine & Custom Rules"))

    cat_groups: list[tuple[str, str, dict | None, list[dict]]] = []
    attr_root = base_dir / "attributes"
    if not attr_root.exists():
        return {"pinned": pinned_entries, "categories": cat_groups}

    subdirs = [d for d in attr_root.iterdir() if d.is_dir()]
    if not subdirs:
        flat_files = sorted(f for f in attr_root.glob("*.md") if f.name != "index.md")
        cat_label = "Validation Attributes"
        cat_idx_fp = attr_root / "index.md"
        cat_slug = alloc_slug("attributes-index", "attr") if cat_idx_fp.exists() else ""
        cat_entry = make_entry(cat_idx_fp, cat_slug, f"{cat_label} Directory", cat_label, is_cat_index=True) if cat_idx_fp.exists() else None
        entries = []
        for fp in flat_files:
            t = human_title_from_md(fp.read_text(encoding="utf-8", errors="replace"), fp.stem)
            e = make_entry(fp, alloc_slug(fp.stem, "attr"), t, cat_label)
            e["cat_slug"] = cat_slug
            entries.append(e)
        cat_groups.append(("validation-attributes", cat_label, cat_entry, entries))
        return {"pinned": pinned_entries, "categories": cat_groups}

    dir_names = sorted(d.name for d in subdirs)
    ordered = ([c for c in cat_order if c in dir_names] + [c for c in dir_names if c not in cat_order]) if cat_order else dir_names

    for cat in ordered:
        cat_dir = attr_root / cat
        cat_label = CATEGORY_LABELS.get(cat, cat.replace("-", " ").title())
        idx_file = cat_dir / "index.md"
        cat_slug = alloc_slug(f"cat-{cat}", cat) if idx_file.exists() else ""
        cat_entry = make_entry(idx_file, cat_slug, f"{cat_label}", cat_label, is_cat_index=True) if idx_file.exists() else None

        entries = []
        for fp in sorted(f for f in cat_dir.glob("*.md") if f.name != "index.md"):
            t = human_title_from_md(fp.read_text(encoding="utf-8", errors="replace"), fp.stem)
            e = make_entry(fp, alloc_slug(fp.stem, cat), t, cat_label)
            e["cat_slug"] = cat_slug
            entries.append(e)

        cat_groups.append((cat, cat_label, cat_entry, entries))

    return {"pinned": pinned_entries, "categories": cat_groups}


def collect_customizer_package(doc_page: str, base_dir: Path):
    used_slugs: set[str] = set()

    def alloc_slug(desired: str, prefix: str) -> str:
        s = slugify(desired)
        if s not in used_slugs:
            used_slugs.add(s)
            return s
        s2 = slugify(f"{prefix}-{desired}")
        used_slugs.add(s2)
        return s2

    pinned_entries: list[dict] = []
    idx_fp = base_dir / "index.md"
    if idx_fp.exists():
        t = human_title_from_md(idx_fp.read_text(encoding="utf-8", errors="replace"), "Inspector Customizer Overview")
        pinned_entries.append(make_entry(idx_fp, alloc_slug("overview", "ic"), t, "Overview", is_pkg_overview=True))

    cat_groups: list[tuple[str, str, dict | None, list[dict]]] = []
    for ch in sorted(d for d in base_dir.iterdir() if d.is_dir()):
        cat_label = CATEGORY_LABELS.get(ch.name, ch.name.replace("-", " ").title())
        entries = []
        for fp in sorted(ch.glob("*.md")):
            t = human_title_from_md(fp.read_text(encoding="utf-8", errors="replace"), fp.stem)
            entries.append(make_entry(fp, alloc_slug(fp.stem, ch.name), t, cat_label))
        if entries:
            cat_groups.append((ch.name, cat_label, None, entries))

    return {"pinned": pinned_entries, "categories": cat_groups}


def collect_toolbox_package(doc_page: str, base_dir: Path):
    used_slugs: set[str] = set()

    def alloc_slug(desired: str, prefix: str) -> str:
        s = slugify(desired)
        if s not in used_slugs:
            used_slugs.add(s)
            return s
        s2 = slugify(f"{prefix}-{desired}")
        used_slugs.add(s2)
        return s2

    pinned_entries: list[dict] = []
    idx_fp = base_dir / "index.md"
    if idx_fp.exists():
        t = human_title_from_md(idx_fp.read_text(encoding="utf-8", errors="replace"), "ToolBox Vol. 1 Overview")
        pinned_entries.append(make_entry(idx_fp, alloc_slug("overview", "tb"), t, "Overview", is_pkg_overview=True))

    cat_groups: list[tuple[str, str, dict | None, list[dict]]] = []

    tool_entries = []
    for folder, fixed_slug in [
        ("tools/advanced-console/index.md", "advanced-console"),
        ("tools/history-track/index.md", "history-track-tool"),
        ("tools/lifetime-track/index.md", "lifetime-track"),
        ("tools/live-track/index.md", "live-track-tool"),
    ]:
        fp = base_dir / folder
        if fp.exists():
            t = human_title_from_md(fp.read_text(encoding="utf-8", errors="replace"), fixed_slug)
            tool_entries.append(make_entry(fp, alloc_slug(fixed_slug, "tool"), t, "Standalone Tools"))
    cat_groups.append(("tools", "4 Standalone Tools", None, tool_entries))

    acs_dir = base_dir / "Advanced_Console_System"
    if acs_dir.exists():
        acs_order = ["Introduction.md", "Getting-Started.md", "Core-Concepts.md", "How-To-Guide.md"]
        files = [acs_dir / f for f in acs_order if (acs_dir / f).exists()] + [
            f for f in sorted(acs_dir.glob("*.md")) if f.name not in acs_order
        ]
        acs_entries = []
        for fp in files:
            t = f"Console Guide · {human_title_from_md(fp.read_text(encoding='utf-8', errors='replace'), fp.stem)}"
            acs_entries.append(make_entry(fp, alloc_slug(f"console-{fp.stem}", "acs"), t, "Advanced Console Guides"))
        cat_groups.append(("console-system", "Advanced Console Guides", None, acs_entries))

    attr_dir = base_dir / "attributes"
    if attr_dir.exists():
        cat_label = "Integration Attributes"
        attr_idx_fp = attr_dir / "index.md"
        cat_slug = alloc_slug("attributes-index", "tbattr") if attr_idx_fp.exists() else ""
        cat_entry = make_entry(attr_idx_fp, cat_slug, "ToolBox Integration Attributes", cat_label, is_cat_index=True) if attr_idx_fp.exists() else None
        attr_entries = []
        for fp in sorted(f for f in attr_dir.glob("*.md") if f.name != "index.md"):
            t = human_title_from_md(fp.read_text(encoding="utf-8", errors="replace"), fp.stem)
            e = make_entry(fp, alloc_slug(fp.stem, "attr"), t, cat_label)
            e["cat_slug"] = cat_slug
            attr_entries.append(e)
        cat_groups.append(("toolbox-attributes", cat_label, cat_entry, attr_entries))

    return {"pinned": pinned_entries, "categories": cat_groups}


def iter_package_entries(pm: dict):
    """Yield every renderable section dict inside a package in display/pagination order."""
    for e in pm["data"]["pinned"]:
        yield e, None
    for _, _, cat_entry, entries in pm["data"]["categories"]:
        if cat_entry:
            yield cat_entry, entries
        for e in entries:
            yield e, None


def render_addon_doc_page(pm: dict) -> str:
    doc_page = pm["doc_page"]
    pkg_name = pm["pkg_name"]
    page_title = pm["page_title"]
    pinned = pm["data"]["pinned"]
    cat_groups = pm["data"]["categories"]

    # Sidebar Top Pinned Links
    pinned_links_html = []
    for e in pinned:
        label = "Package Overview" if e["is_pkg_overview"] else e["title"]
        badge = '<span class="eco-pill-count">Start</span>' if e["is_pkg_overview"] else ""
        pinned_links_html.append(
            f'<a href="#{html.escape(e["slug"], quote=True)}" class="docs-nav-link">'
            f'<span>{html.escape(label)}</span>{badge}</a>'
        )
    pinned_block = (
        '<div class="docs-pinned-group">'
        '<div class="docs-pinned-label">Overview &amp; Guides</div>'
        f'{"".join(pinned_links_html)}'
        '</div>'
    )

    # Sidebar Category Accordions (Category link + Chevron when category index exists, otherwise full toggle button)
    sidebar_groups_html = [pinned_block]
    for cat_idx, (_, cat_label, cat_entry, entries) in enumerate(cat_groups):
        collapsed = " is-collapsed" if cat_idx >= 1 and len(cat_groups) > 2 else ""
        expanded = "false" if collapsed else "true"
        li_items = "".join(
            f'<li><a href="#{html.escape(e["slug"], quote=True)}" class="docs-nav-link">{html.escape(e["title"])}</a></li>'
            for e in entries
        )
        chevron_svg = (
            '<svg class="docs-cat-chevron" width="13" height="13" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="m6 9 6 6 6-6"/></svg>'
        )
        if cat_entry:
            header_html = (
                '<div class="docs-cat-head">'
                f'<a href="#{html.escape(cat_entry["slug"], quote=True)}" class="docs-cat-link docs-nav-link">'
                f'<span>{html.escape(cat_label)}</span>'
                f'<span class="docs-cat-count">{len(entries)}</span>'
                '</a>'
                f'<button type="button" class="docs-cat-toggle" aria-expanded="{expanded}" aria-label="Toggle {html.escape(cat_label)}">{chevron_svg}</button>'
                '</div>'
            )
        else:
            header_html = (
                f'<button type="button" class="docs-cat-btn" aria-expanded="{expanded}">'
                f'<span>{html.escape(cat_label)} <span class="docs-cat-count">({len(entries)})</span></span>'
                f'{chevron_svg}'
                '</button>'
            )

        sidebar_groups_html.append(
            f'<div class="docs-cat-group{collapsed}">{header_html}<ul class="docs-nav-menu">{li_items}</ul></div>'
        )

    # Main Content Sections
    sections_html = []
    overview_slug = pinned[0]["slug"] if pinned else "overview"
    all_section_count = 0

    for entry, child_entries in iter_package_entries(pm):
        all_section_count += 1
        if entry["is_pkg_overview"]:
            body_html = render_package_overview_body(entry, cat_groups, doc_page)
            crumb_html = f'<span class="tag tag-accent">{html.escape(pkg_name)}</span><span>/</span><span>Overview</span>'
        elif entry["is_cat_index"]:
            body_html = render_category_index_body(entry, child_entries or [], doc_page)
            crumb_html = (
                f'<a href="#{html.escape(overview_slug, quote=True)}" class="doc-crumb-link">{html.escape(pkg_name)}</a>'
                f'<span>/</span><span class="tag tag-accent">{html.escape(entry["cat_label"])} Index</span>'
            )
        else:
            body_html = md_to_html(entry["md"], entry["path"], doc_page, strip_first_h1=True)
            cat_part = (
                f'<a href="#{html.escape(entry["cat_slug"], quote=True)}" class="doc-crumb-link">{html.escape(entry["category"])}</a>'
                if entry["cat_slug"]
                else f'<span>{html.escape(entry["category"])}</span>'
            )
            crumb_html = (
                f'<a href="#{html.escape(overview_slug, quote=True)}" class="doc-crumb-link">{html.escape(pkg_name)}</a>'
                f'<span>/</span>{cat_part}<span>/</span><span>{html.escape(entry["title"])}</span>'
            )

        sections_html.append(
            f'<section class="docs-section" id="{html.escape(entry["slug"], quote=True)}" '
            f'data-doc-title="{html.escape(entry["title"], quote=True)}">\n'
            '    <article class="doc-article">\n'
            '        <div class="doc-article-head">\n'
            f'            <div class="doc-article-meta">{crumb_html}</div>\n'
            f'            <h1>{html.escape(entry["title"])}</h1>\n'
            '        </div>\n'
            f'        {body_html}\n'
            '    </article>\n'
            '</section>'
        )

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(page_title)} — MSUltimate Docs</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/studio.css">
</head>

<body class="docs-workspace">
{render_nav()}
{render_eco_subnav(doc_page)}

    <main>
        <div class="container">
            <div class="docs-shell">
                <aside class="docs-sidebar" aria-label="Documentation navigation">
                    <div class="docs-sidebar-head">
                        <div class="docs-sidebar-title-row">
                            <span class="docs-sidebar-title">{html.escape(pkg_name)}</span>
                            <span class="mono" style="font-size: 11px; color: var(--text-muted);">{all_section_count} pages</span>
                        </div>
                        <div class="docs-search-wrap">
                            <svg class="docs-search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
                            <input type="search" id="doc-search" class="docs-search-input" placeholder="Search ecosystem (454+)" aria-label="Search MSUltimate documentation" autocomplete="off">
                            <span class="docs-search-kbd">Ctrl+K</span>
                        </div>
                    </div>
                    <div class="docs-sidebar-body">
                        {"".join(sidebar_groups_html)}
                    </div>
                </aside>

                <div class="docs-main">
                    <div class="docs-mobile-toolbar">
                        <button type="button" id="doc-sidebar-toggle" class="btn btn-secondary btn-sm" aria-expanded="false">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="17" y2="17"/></svg>
                            Browse {html.escape(pkg_name)} ({all_section_count})
                        </button>
                        <a href="msultimate-docs.html" class="link-arrow">All packages</a>
                    </div>

                    {"".join(sections_html)}

                    <nav class="docs-pager" aria-label="Page pagination">
                        <button type="button" id="prev-doc" class="docs-pager-btn">
                            <span class="docs-pager-dir">Previous</span>
                            <span class="docs-pager-title">Start of guide</span>
                        </button>
                        <button type="button" id="next-doc" class="docs-pager-btn is-next">
                            <span class="docs-pager-dir">Next</span>
                            <span class="docs-pager-title">Next guide</span>
                        </button>
                    </nav>
                </div>
            </div>
        </div>
    </main>

{render_footer()}
    <script src="js/studio.js"></script>
    <script src="js/msultimate-search-index.js"></script>
    <script src="js/msultimate-omnisearch.js"></script>
</body>

</html>
"""


def render_hub_page(packages_meta: list[dict]) -> str:
    dir_cards = []
    for pm in packages_meta:
        cat_blocks = []
        for _, cat_label, cat_entry, entries in pm["data"]["categories"]:
            links = "".join(
                f'<a href="{pm["doc_page"]}#{html.escape(e["slug"], quote=True)}" class="hub-attr-chip" '
                f'data-hub-item="{html.escape((e["title"] + " " + cat_label + " " + pm["pkg_name"]).lower(), quote=True)}">'
                f'{html.escape(e["title"])}</a>'
                for e in entries
            )
            cat_title_html = (
                f'<a href="{pm["doc_page"]}#{html.escape(cat_entry["slug"], quote=True)}" '
                f'style="color: var(--accent-text); text-decoration: none;">{html.escape(cat_label)} ({len(entries)})</a>'
                if cat_entry
                else f'{html.escape(cat_label)} ({len(entries)})'
            )
            if links:
                cat_blocks.append(
                    f'<div class="hub-cat-group" style="margin-bottom: 16px;">'
                    f'<div class="mono" style="font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 8px;">'
                    f'{cat_title_html}</div>'
                    f'<div class="hub-chip-grid">{links}</div></div>'
                )

        dir_cards.append(
            f'<article class="card hub-pkg-card" style="padding: 24px;">'
            f'<div class="asset-meta-row" style="justify-content: space-between; margin-bottom: 8px;">'
            f'<a href="{pm["doc_page"]}" class="card-title" style="font-size: 18px; color: var(--text-primary);">{html.escape(pm["pkg_name"])}</a>'
            f'<span class="tag tag-accent">{html.escape(pm["badge"])}</span>'
            f'</div>'
            f'<p style="font-size: 13px; color: var(--text-secondary); margin: 0 0 16px;">{html.escape(pm["summary"])}</p>'
            f'{"".join(cat_blocks)}'
            f'</article>'
        )

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MSUltimate Ecosystem Docs Hub — Maharaja Studio</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/studio.css">
</head>

<body>
{render_nav()}
{render_eco_subnav("msultimate-docs.html")}

    <header class="hero" style="padding: var(--space-12) 0;">
        <canvas class="hero-canvas" data-glyph-mode="ecosystem" aria-hidden="true"></canvas>
        <div class="container">
            <div class="hero-breadcrumb">
                <a href="documentation.html">Documentation</a>
                <span>/</span>
                <a href="msultimate.html">MSUltimate</a>
                <span>/</span>
                <span class="mono" style="color: var(--accent-text);">Ecosystem Hub</span>
            </div>
            <h1 style="max-width: 24ch; margin-bottom: var(--space-4);">MSUltimate Documentation Hub</h1>
            <p class="hero-sub" style="margin-bottom: var(--space-6);">
                Complete reference manuals for MSUltimate Core (156+ concrete attributes / 161 classes) and all 6 standalone addons — 454+ concrete attributes (463 total classes), 30 Inspector Customizer manuals, ToolBox Vol. 1 tools, and 6,115 test cases across 573 test files.
            </p>
            <div class="hub-search-box">
                <svg class="docs-search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="left: 14px;"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
                <input type="search" id="doc-search" class="hub-search-input" placeholder="Search 454+ attributes, tools, or Customizer manuals (Ctrl+K or /)..." aria-label="Search MSUltimate documentation" autocomplete="off">
            </div>
        </div>
    </header>

    <main>
        <section class="section-compact">
            <div class="container">
                <div class="stats-strip stats-strip-6">
                    <div class="stat-cell">
                        <div class="stat-label">Attributes</div>
                        <div class="stat-value mono">454+</div>
                        <div class="stat-note">463 classes total</div>
                    </div>
                    <div class="stat-cell">
                        <div class="stat-label">Core Framework</div>
                        <div class="stat-value mono">156+</div>
                        <div class="stat-note">Free Community / $149.99</div>
                    </div>
                    <div class="stat-cell">
                        <div class="stat-label">Animated / Comp / Hier</div>
                        <div class="stat-value mono" style="font-size: 22px; white-space: nowrap;">99 / 74 / 82</div>
                        <div class="stat-note">101 / 75 / 83 classes</div>
                    </div>
                    <div class="stat-cell">
                        <div class="stat-label">Validation</div>
                        <div class="stat-value mono">39</div>
                        <div class="stat-note">+ ValidationWindow &amp; CLI</div>
                    </div>
                    <div class="stat-cell">
                        <div class="stat-label">Customizer &amp; ToolBox</div>
                        <div class="stat-value mono">30 + 4</div>
                        <div class="stat-note">Guides &amp; Power Tools</div>
                    </div>
                    <div class="stat-cell">
                        <div class="stat-label">Automated tests</div>
                        <div class="stat-value mono">6,115</div>
                        <div class="stat-note">573 files · 3,275 methods</div>
                    </div>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="section-head">
                    <div>
                        <h2 class="section-title">Documentation modules</h2>
                        <p class="section-sub">Open any standalone reference manual below or jump straight to an attribute from the directory</p>
                    </div>
                    <a href="msultimate-license.html" class="btn btn-secondary btn-sm">Licensing &amp; EULA</a>
                </div>

                <div class="grid-4" style="margin-bottom: var(--space-10);">
                    <article class="card spotlight-card">
                        <div class="asset-meta-row" style="justify-content: space-between;">
                            <span class="tag tag-positive">Core</span>
                            <span class="mono" style="font-size: 12px;">156+ (161 classes)</span>
                        </div>
                        <h3 class="card-title">Core Framework</h3>
                        <p class="card-desc">14 attribute folders, custom serializers, extended data types, Core Systems Architecture, and Tutorials.</p>
                        <div class="card-footer">
                            <span class="mono">Free / $149.99</span>
                            <a href="msultimate-core-docs.html" class="link-arrow">Open docs</a>
                        </div>
                    </article>

                    <article class="card spotlight-card">
                        <div class="asset-meta-row" style="justify-content: space-between;">
                            <span class="tag tag-accent">Add-on</span>
                            <span class="mono" style="font-size: 12px;">99 (101 classes)</span>
                        </div>
                        <h3 class="card-title">Animated Attributes</h3>
                        <p class="card-desc">12 runtime categories covering combat HUDs, kinetic typography, sci-fi VFX, physics, and particle sims.</p>
                        <div class="card-footer">
                            <span class="mono">$29.99</span>
                            <a href="msultimate-animated-docs.html" class="link-arrow">Open docs</a>
                        </div>
                    </article>

                    <article class="card spotlight-card">
                        <div class="asset-meta-row" style="justify-content: space-between;">
                            <span class="tag">Add-on</span>
                            <span class="mono" style="font-size: 12px;">74 (75 classes)</span>
                        </div>
                        <h3 class="card-title">Component Designer</h3>
                        <p class="card-desc">7 categories of MonoBehaviour cards, atmospheric shaders/VFX, header controls, and genre themes.</p>
                        <div class="card-footer">
                            <span class="mono">$29.99</span>
                            <a href="msultimate-component-docs.html" class="link-arrow">Open docs</a>
                        </div>
                    </article>

                    <article class="card spotlight-card">
                        <div class="asset-meta-row" style="justify-content: space-between;">
                            <span class="tag">Add-on</span>
                            <span class="mono" style="font-size: 12px;">82 (83 classes)</span>
                        </div>
                        <h3 class="card-title">Hierarchy Designer</h3>
                        <p class="card-desc">8 categories of folders, tree branches, live component monitors, and draw-call/poly telemetry badges.</p>
                        <div class="card-footer">
                            <span class="mono">$29.99</span>
                            <a href="msultimate-hierarchy-docs.html" class="link-arrow">Open docs</a>
                        </div>
                    </article>

                    <article class="card spotlight-card">
                        <div class="asset-meta-row" style="justify-content: space-between;">
                            <span class="tag">Add-on</span>
                            <span class="mono" style="font-size: 12px;">39 attributes</span>
                        </div>
                        <h3 class="card-title">Validation Module</h3>
                        <p class="card-desc">39 field rules plus ValidationWindow, ValidationCLI, and custom IValidationRule pipelines.</p>
                        <div class="card-footer">
                            <span class="mono">$29.99</span>
                            <a href="msultimate-validation-docs.html" class="link-arrow">Open docs</a>
                        </div>
                    </article>

                    <article class="card spotlight-card">
                        <div class="asset-meta-row" style="justify-content: space-between;">
                            <span class="tag tag-accent">Add-on</span>
                            <span class="mono" style="font-size: 12px;">30 Guides</span>
                        </div>
                        <h3 class="card-title">Inspector Customizer</h3>
                        <p class="card-desc">Non-destructive InspectorProfile hydration, 30-node Makeover Graph, Multi-LLM AI Decorator, and AttributeCodeBaker.</p>
                        <div class="card-footer">
                            <span class="mono">$39.99</span>
                            <a href="msultimate-customizer-docs.html" class="link-arrow">Open docs</a>
                        </div>
                    </article>

                    <article class="card spotlight-card">
                        <div class="asset-meta-row" style="justify-content: space-between;">
                            <span class="tag tag-accent">Add-on</span>
                            <span class="mono" style="font-size: 12px;">4 Tools + 4 Attr</span>
                        </div>
                        <h3 class="card-title">ToolBox Vol. 1</h3>
                        <p class="card-desc">Advanced Console, History Track, Object Lifetime Tracker, Live Track, and their C# integration attributes.</p>
                        <div class="card-footer">
                            <span class="mono">$44.99</span>
                            <a href="msultimate-toolbox-docs.html" class="link-arrow">Open docs</a>
                        </div>
                    </article>

                    <article class="card spotlight-card">
                        <div class="asset-meta-row" style="justify-content: space-between;">
                            <span class="tag tag-positive">Legal</span>
                            <span class="mono" style="font-size: 12px;">Oct 2026 EULA</span>
                        </div>
                        <h3 class="card-title">Licensing &amp; EULA</h3>
                        <p class="card-desc">Community Edition EULA (&lt;$200,000 USD ceiling), Standard Unity Asset Store per-seat terms, and bundle matrix.</p>
                        <div class="card-footer">
                            <span class="mono">Terms</span>
                            <a href="msultimate-license.html" class="link-arrow">Read license</a>
                        </div>
                    </article>
                </div>

                <div class="section-head" id="comparison">
                    <div>
                        <h2 class="section-title">Master package comparison</h2>
                        <p class="section-sub">Exact counts, formats, and licensing tiers from MSUltimate_Ecosystem_Comparison_Guide.md</p>
                    </div>
                </div>

                <div class="doc-table-wrap" style="margin-bottom: var(--space-10);">
                    <table class="studio-table">
                        <thead>
                            <tr>
                                <th>Package Name</th>
                                <th>Price (USD)</th>
                                <th>Primary Domain</th>
                                <th>Attributes</th>
                                <th>Source Code</th>
                                <th>Tests Included</th>
                                <th>Scope</th>
                                <th>Licensing Tier</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>MSUltimate Core (Community)</strong></td>
                                <td class="mono" style="color: var(--positive);">FREE</td>
                                <td>Core Inspector &amp; Serializers</td>
                                <td class="mono">156+</td>
                                <td>Obfuscated DLL</td>
                                <td class="mono">—</td>
                                <td>Core</td>
                                <td><a href="msultimate-license.html#community-eula" class="link-arrow">Custom Free EULA (&lt;$200K Rev)</a></td>
                            </tr>
                            <tr>
                                <td><strong>MSUltimate Core (Pro)</strong></td>
                                <td class="mono">$149.99</td>
                                <td>Unrestricted Core Engine</td>
                                <td class="mono">156+</td>
                                <td>Full C# Source</td>
                                <td class="mono">—</td>
                                <td>Core</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr>
                                <td><strong>MSUltimate - Animated Attributes</strong></td>
                                <td class="mono">$29.99</td>
                                <td>Micro-Interactions &amp; VFX</td>
                                <td class="mono">99 (101 classes)</td>
                                <td>Full C# Source</td>
                                <td class="mono">—</td>
                                <td>Standalone</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr>
                                <td><strong>MSUltimate - Component Designer</strong></td>
                                <td class="mono">$29.99</td>
                                <td>Branded Inspector Cards</td>
                                <td class="mono">74 (75 classes)</td>
                                <td>Full C# Source</td>
                                <td class="mono">—</td>
                                <td>Standalone</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr>
                                <td><strong>MSUltimate - Hierarchy Designer</strong></td>
                                <td class="mono">$29.99</td>
                                <td>Scene Hierarchy Window</td>
                                <td class="mono">82 (83 classes)</td>
                                <td>Full C# Source</td>
                                <td class="mono">—</td>
                                <td>Standalone</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr>
                                <td><strong>MSUltimate - Validation Module</strong></td>
                                <td class="mono">$29.99</td>
                                <td>Project Scanning &amp; Fixes</td>
                                <td class="mono">39</td>
                                <td>Full C# Source</td>
                                <td class="mono">—</td>
                                <td>Standalone</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr>
                                <td><strong>MSUltimate - Inspector Customizer</strong></td>
                                <td class="mono">$39.99</td>
                                <td>Non-Destructive Styler &amp; Baker</td>
                                <td class="mono">Templates &amp; Graph</td>
                                <td>Full C# Source</td>
                                <td class="mono">—</td>
                                <td>Standalone</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr>
                                <td><strong>MSUltimate - ToolBox Vol. 1</strong></td>
                                <td class="mono">$44.99</td>
                                <td>4 Developer Power Tools</td>
                                <td class="mono">4 + Tools</td>
                                <td>Full C# Source</td>
                                <td class="mono">—</td>
                                <td>Standalone</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr class="row-highlight">
                                <td><strong>MSUltimate Pro (Full Collection)</strong></td>
                                <td class="mono"><strong>$299.99</strong></td>
                                <td>Complete Master Ecosystem</td>
                                <td class="mono"><strong>454+ (463 classes)</strong></td>
                                <td><strong>Full C# Source</strong></td>
                                <td class="mono"><strong>6,115 Cases</strong></td>
                                <td><strong>ALL 6 Addons</strong></td>
                                <td><strong>Standard Unity EULA (Per-Seat)</strong></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="section-head" id="directory">
                    <div>
                        <h2 class="section-title">Complete API &amp; guide index</h2>
                        <p class="section-sub">Click any category header or attribute below to jump straight to its documentation</p>
                    </div>
                </div>

                <div style="display: flex; flex-direction: column; gap: var(--space-5);">
                    {"".join(dir_cards)}
                </div>
            </div>
        </section>
    </main>

{render_footer()}
    <script src="js/studio.js"></script>
    <script src="js/msultimate-search-index.js"></script>
    <script src="js/msultimate-omnisearch.js"></script>
</body>

</html>
"""


def render_license_page() -> str:
    eula_md_text = EULA_MD.read_text(encoding="utf-8", errors="replace")
    eula_body = md_to_html(eula_md_text, EULA_MD, "msultimate-license.html", strip_first_h1=True)

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MSUltimate Licensing &amp; Community EULA — Maharaja Studio</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/studio.css">
</head>

<body>
{render_nav()}
{render_eco_subnav("msultimate-license.html")}

    <header class="hero" style="padding: var(--space-12) 0;">
        <canvas class="hero-canvas" data-glyph-mode="ecosystem" aria-hidden="true"></canvas>
        <div class="container">
            <div class="hero-breadcrumb">
                <a href="msultimate.html">MSUltimate</a>
                <span>/</span>
                <span class="mono" style="color: var(--accent-text);">Licensing &amp; EULA</span>
            </div>
            <h1 style="max-width: 24ch; margin-bottom: var(--space-4);">MSUltimate Licensing &amp; EULA</h1>
            <p class="hero-sub">
                Clear licensing for solo creators, commercial game studios, and enterprise pipelines across Community Edition and Standard Unity Asset Store Per-Seat Pro Editions.
            </p>
            <div class="hero-actions">
                <a href="#community-eula" class="btn btn-primary">Community EULA</a>
                <a href="#commercial-licensing" class="btn btn-secondary">Commercial Licensing</a>
            </div>
        </div>
    </header>

    <main>
        <section id="community-eula" class="section">
            <div class="container">
                <div class="grid-3" style="margin-bottom: var(--space-8);">
                    <div class="card">
                        <span class="tag tag-positive" style="align-self: flex-start;">Community Tier</span>
                        <h3 class="card-title">Free &lt;$200,000 USD</h3>
                        <p class="card-desc">Annual gross revenue and funding cap of $200,000 USD for commercial and non-commercial projects using the Core Community DLL.</p>
                    </div>
                    <div class="card">
                        <span class="tag tag-accent" style="align-self: flex-start;">Pro &amp; Addons</span>
                        <h3 class="card-title">Standard Unity EULA</h3>
                        <p class="card-desc">MSUltimate Core Pro ($149.99), all 6 standalone addons, and MSUltimate Pro Full Collection ($299.99) carry zero revenue caps.</p>
                    </div>
                    <div class="card">
                        <span class="tag" style="align-self: flex-start;">Per-Seat Basis</span>
                        <h3 class="card-title">1 License / Seat</h3>
                        <p class="card-desc">Commercial Pro packages and addons are licensed under the standard Unity Asset Store EULA (one license per active seat).</p>
                    </div>
                </div>

                <article class="doc-article" style="max-width: 92ch;">
                    <div class="doc-article-head">
                        <div class="doc-article-meta">
                            <span class="tag tag-positive">Legal Agreement</span>
                            <span>MSUltimate_Core_Community_EULA.md</span>
                        </div>
                        <h1>MSUltimate Core (Community Edition) EULA</h1>
                    </div>
                    {eula_body}
                </article>
            </div>
        </section>

        <section id="commercial-licensing" class="section section-surface">
            <div class="container">
                <div class="section-head">
                    <div>
                        <h2 class="section-title">Commercial Pro &amp; Addon Licensing</h2>
                        <p class="section-sub">Governed by the Standard Unity Asset Store End User License Agreement</p>
                    </div>
                </div>

                <div class="doc-table-wrap">
                    <table class="studio-table">
                        <thead>
                            <tr>
                                <th>Edition / Module</th>
                                <th>Price (USD)</th>
                                <th>Delivery Format</th>
                                <th>Revenue Ceiling</th>
                                <th>Governing License</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>MSUltimate Core (Community)</strong></td>
                                <td class="mono" style="color: var(--positive);">Free</td>
                                <td>Precompiled Obfuscated DLL</td>
                                <td class="mono">&lt;$200,000 USD / yr</td>
                                <td>Custom Free Community EULA</td>
                            </tr>
                            <tr>
                                <td><strong>MSUltimate Core (Pro)</strong></td>
                                <td class="mono">$149.99</td>
                                <td>100% Full C# Source Code</td>
                                <td class="mono">Unlimited</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr>
                                <td><strong>Animated Attributes / Component / Hierarchy / Validation</strong></td>
                                <td class="mono">$29.99 each</td>
                                <td>100% Full C# Source Code</td>
                                <td class="mono">Unlimited</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr>
                                <td><strong>Inspector Customizer</strong></td>
                                <td class="mono">$39.99</td>
                                <td>100% Full C# Source Code</td>
                                <td class="mono">Unlimited</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr>
                                <td><strong>ToolBox Vol. 1</strong></td>
                                <td class="mono">$44.99</td>
                                <td>100% Full C# Source Code</td>
                                <td class="mono">Unlimited</td>
                                <td>Standard Unity EULA (Per-Seat)</td>
                            </tr>
                            <tr class="row-highlight">
                                <td><strong>MSUltimate Pro (Full Collection)</strong></td>
                                <td class="mono"><strong>$299.99</strong></td>
                                <td><strong>Core + All 6 Addons + 6,115 Tests</strong></td>
                                <td class="mono"><strong>Unlimited</strong></td>
                                <td><strong>Standard Unity EULA (Per-Seat)</strong></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="cta-panel" style="margin-top: var(--space-8);">
                    <h2>Need multi-seat or custom enterprise terms</h2>
                    <p>Contact Maharaja Studio directly for bulk licensing inquiries or technical evaluation assistance.</p>
                    <div class="hero-actions" style="justify-content: center;">
                        <a href="mailto:maharajastudiocustomerservice@gmail.com" class="btn btn-primary">maharajastudiocustomerservice@gmail.com</a>
                        <a href="msultimate-docs.html" class="btn btn-secondary">Back to Docs Hub</a>
                    </div>
                </div>
            </div>
        </section>
    </main>

{render_footer()}
    <script src="js/studio.js"></script>
</body>

</html>
"""


def audit_generated_files(doc_files: list[str]) -> bool:
    file_ids: dict[str, set[str]] = {}
    ok = True
    for name in doc_files + ["msultimate.html"]:
        text = (WORKSPACE / name).read_text(encoding="utf-8")
        file_ids[name] = set(re.findall(r'id="([^"]+)"', text))

    for name in doc_files:
        text = (WORKSPACE / name).read_text(encoding="utf-8")
        ids = file_ids[name]
        missing_hashes = [h for h in re.findall(r'href="#([^"]+)"', text) if h not in ids]
        broken_cross = [
            f"{tgt}#{h}"
            for tgt, h in re.findall(r'href="(msultimate[^"]+\.html)#([^"]+)"', text)
            if tgt not in file_ids or h not in file_ids[tgt]
        ]
        md_leaks = re.findall(r'href="[^"]*\.md[^"]*"', text)
        if missing_hashes or broken_cross or md_leaks:
            ok = False
            print(f"[AUDIT FAIL] {name}: missing_hashes={missing_hashes[:5]}, broken_cross={broken_cross[:5]}, md_leaks={md_leaks[:5]}")
    if ok:
        print(f"Audit passed across all {len(doc_files)} generated HTML files (0 broken hashes, 0 unresolved .md links).")
    return ok


def main():
    packages = [
        {
            "pkg_name": "Core Framework",
            "page_title": "MSUltimate Core Documentation",
            "doc_page": "msultimate-core-docs.html",
            "badge": "156+ attributes",
            "summary": "14 documentation category folders covering layout groups, conditionals, custom serializers, extended data types, modular windows, and core architecture.",
            "data": collect_attribute_package("Core Framework", "msultimate-core-docs.html", DOCS_ROOT / "Documentation", CORE_CAT_ORDER),
        },
        {
            "pkg_name": "Animated Attributes",
            "page_title": "Animated Attributes Documentation",
            "doc_page": "msultimate-animated-docs.html",
            "badge": "99 (101 classes)",
            "summary": "Micro-interactions, combat HUD meters, kinetic typography, sci-fi VFX, data visualizers, and particle simulations.",
            "data": collect_attribute_package("Animated Attributes", "msultimate-animated-docs.html", DOCS_ROOT / "Addons" / "AnimatedAttributes" / "Documentation"),
        },
        {
            "pkg_name": "Component Designer",
            "page_title": "Component Designer Documentation",
            "doc_page": "msultimate-component-docs.html",
            "badge": "74 (75 classes)",
            "summary": "MonoBehaviour card frames, atmospheric backgrounds, header buttons, layout ergonomics, and genre theme shells.",
            "data": collect_attribute_package("Component Designer", "msultimate-component-docs.html", DOCS_ROOT / "Addons" / "ComponentDesigner" / "Documentation"),
        },
        {
            "pkg_name": "Hierarchy Designer",
            "page_title": "Hierarchy Designer Documentation",
            "doc_page": "msultimate-hierarchy-docs.html",
            "badge": "82 (83 classes)",
            "summary": "Virtual colored folders, tree branches, live telemetry monitors, inline buttons, and draw-call/poly badges.",
            "data": collect_attribute_package("Hierarchy Designer", "msultimate-hierarchy-docs.html", DOCS_ROOT / "Addons" / "HierarchyDesigner" / "Documentation"),
        },
        {
            "pkg_name": "Validation Module",
            "page_title": "Validation Module Documentation",
            "doc_page": "msultimate-validation-docs.html",
            "badge": "39 attributes + Engine",
            "summary": "Real-time field assertions, ValidationWindow deep project scanner with 1-click auto-fix, ValidationCLI, and custom rule APIs.",
            "data": collect_attribute_package("Validation Module", "msultimate-validation-docs.html", DOCS_ROOT / "Addons" / "ValidationModule" / "Documentation"),
        },
        {
            "pkg_name": "Inspector Customizer",
            "page_title": "Inspector Customizer Documentation",
            "doc_page": "msultimate-customizer-docs.html",
            "badge": "30 Manuals",
            "summary": "Non-destructive InspectorProfile hydration, 30-node Makeover Graph, Multi-LLM AI Decorator + Privacy Shield, Recipes, and AttributeCodeBaker.",
            "data": collect_customizer_package("msultimate-customizer-docs.html", DOCS_ROOT / "Addons" / "InspectorCustomizer" / "Documentation"),
        },
        {
            "pkg_name": "ToolBox Vol. 1",
            "page_title": "ToolBox Vol. 1 Documentation",
            "doc_page": "msultimate-toolbox-docs.html",
            "badge": "4 Tools + 4 Attr",
            "summary": "Manuals and integration guides for Advanced Console, History Track, Object Lifetime Tracker, Live Track, and their C# attributes.",
            "data": collect_toolbox_package("msultimate-toolbox-docs.html", DOCS_ROOT / "Addons" / "ToolBox_Vol1" / "Documentation"),
        },
    ]

    LINK_REGISTRY[os.path.normcase(os.path.normpath(str(EULA_MD.resolve())))] = (
        "msultimate-license.html",
        "community-eula",
        "MSUltimate Core (Community Edition) EULA",
    )
    LINK_REGISTRY[os.path.normcase(os.path.normpath(str(COMPARISON_MD.resolve())))] = (
        "msultimate-docs.html",
        "comparison",
        "MSUltimate Ecosystem Comparison Guide",
    )

    search_index = []
    for pm in packages:
        doc_page = pm["doc_page"]
        pkg_name = pm["pkg_name"]
        for entry, _ in iter_package_entries(pm):
            norm_key = os.path.normcase(os.path.normpath(str(entry["path"].resolve())))
            LINK_REGISTRY[norm_key] = (doc_page, entry["slug"], entry["title"])
            search_index.append({
                "name": entry["title"],
                "rawName": entry["raw_name"],
                "addon": pkg_name,
                "category": entry["category"],
                "docPage": doc_page,
                "hash": f"#{entry['slug']}",
                "status": "Index" if (entry["is_pkg_overview"] or entry["is_cat_index"]) else "Guide",
                "desc": entry["desc"] or f"{pkg_name} — {entry['category']}",
            })

    generated_docs = []
    for pm in packages:
        html_out = render_addon_doc_page(pm)
        (WORKSPACE / pm["doc_page"]).write_text(html_out, encoding="utf-8")
        generated_docs.append(pm["doc_page"])
        print(f"Wrote {pm['doc_page']} ({len(html_out):,} bytes)")

    hub_html = render_hub_page(packages)
    (WORKSPACE / "msultimate-docs.html").write_text(hub_html, encoding="utf-8")
    generated_docs.append("msultimate-docs.html")
    print(f"Wrote msultimate-docs.html ({len(hub_html):,} bytes)")

    lic_html = render_license_page()
    (WORKSPACE / "msultimate-license.html").write_text(lic_html, encoding="utf-8")
    generated_docs.append("msultimate-license.html")
    print(f"Wrote msultimate-license.html ({len(lic_html):,} bytes)")

    js_out = (
        "// Auto-generated from assets/Documentations/MSUltimate markdown documentation.\n"
        f"window.MSULTIMATE_ECOSYSTEM_INDEX = {json.dumps(search_index, ensure_ascii=False, indent=2)};\n"
    )
    (WORKSPACE / "js" / "msultimate-search-index.js").write_text(js_out, encoding="utf-8")
    print(f"Wrote js/msultimate-search-index.js ({len(search_index)} entries, {len(js_out):,} bytes)")

    if not audit_generated_files(generated_docs):
        sys.exit(1)


if __name__ == "__main__":
    main()
