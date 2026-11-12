#!/usr/bin/env python3
"""
MSMotion v2.0 & Object Finder Pro v2.0 Documentation Builder
Reads markdown sources from assets/Documentations/MSMotion/ and
assets/Documentations/ObjectFinderPro/ (plus ObjectFinderPro_Description.txt),
resolves relative .md cross-links to single-page hash sections, embeds verified
editor screenshots, and outputs Graphite+Amber HTML pages aligned with
css/studio.css and js/studio.js.

Usage:
    python scripts/build_product_docs.py
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
MSMOTION_ROOT = WORKSPACE / "assets" / "Documentations" / "MSMotion"
OFP_README = WORKSPACE / "assets" / "Documentations" / "ObjectFinderPro" / "README.md"
OFP_DESC = WORKSPACE / "assets" / "Descriptions" / "ObjectFinderPro_Description.txt"

EMOJI_RE = re.compile(
    r"[\U0001F300-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+",
    flags=re.UNICODE,
)

# Preserve UI icons inside preformatted diagrams while stripping pictographs from prose/headings.
EXTRA_PICTOGRAM_CHARS = ("\ufe0f", "\u200d", "✅", "❌", "⭐", "➔", "➜", "➤", "⚙")

SVG_CHEVRON = (
    '<svg class="docs-cat-chevron" width="13" height="13" viewBox="0 0 24 24" '
    'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" '
    'stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
)

SVG_COPY = (
    '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<rect width="14" height="14" x="8" y="8" rx="2"/>'
    '<path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>'
)

SVG_ALERT_INFO = (
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>'
)

SVG_ALERT_WARN = (
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/>'
    '<path d="M12 9v4"/><path d="M12 17h.01"/></svg>'
)


def strip_emoji(text: str, strip_edges: bool = True) -> str:
    cleaned = text
    # Clean parenthesized/bracketed pictographs cleanly without leaving empty "()" or "[]"
    cleaned = re.sub(r"\(\s*[\U0001F300-\U0001FAFF\u2600-\u26FF\u2700-\u27BF\ufe0f\u200d]+\s*\)", "", cleaned)
    cleaned = re.sub(r"\[\s*[\U0001F300-\U0001FAFF\u2600-\u26FF\u2700-\u27BF\ufe0f\u200d]+\s*\]", "", cleaned)
    cleaned = EMOJI_RE.sub("", cleaned)
    for ch in EXTRA_PICTOGRAM_CHARS:
        cleaned = cleaned.replace(ch, "")
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    cleaned = re.sub(r"\[\s+", "[", cleaned)
    cleaned = re.sub(r"\(\s+", "(", cleaned)
    return cleaned.strip() if strip_edges else cleaned


def slugify(name: str) -> str:
    s = strip_emoji(name).lower().strip()
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "section"


def human_title_from_md(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        m = re.match(r"^\s*#\s+(.+?)\s*$", line)
        if m:
            t = strip_emoji(m.group(1)).replace("`", "").strip()
            if t:
                return t
    return fallback


# ==============================================================================
# Shared Chrome (Matches css/studio.css across site)
# ==============================================================================

def render_nav(current_asset: str, cta_href: str, cta_label: str = "Asset overview") -> str:
    assets = [
        ("msultimate", "msultimate.html", "assets/Images/MSUltimate_Logo.png", "MSUltimate Ecosystem", "454+ attributes · Core & 6 addons"),
        ("ms-motion", "ms-motion.html", "assets/Images/MSMotion_Logo.png", "MSMotion v2.0", "Multi-actor choreography & FX"),
        ("scriptable-studio-pro", "scriptable-studio-pro.html", "assets/Images/ScriptableStudioPro_Logo.png", "Scriptable Studio Pro v4.5", "Grid editor & Prefab Studio"),
        ("tactical", "tactical-cover-retreat-ai-system.html", "assets/Images/Tactical_Cover_&_Retreat_AI_System_Logo.png", "Tactical Cover & Retreat AI", "v3.0 squad maneuvers & cover"),
        ("object-finder-pro", "object-finder-pro.html", "assets/Images/ObjectFinderPro_Logo.png", "Object Finder Pro", "Async query & reference search"),
        ("uqi", "ultimate-quick-inspector.html", "assets/Images/UltimateQuickInspector_Logo.png", "Ultimate Quick Inspector", "Multi-page GUID pin drawer"),
    ]
    dropdown_items = []
    for key, href, img, title, meta in assets:
        cur_cls = " is-current" if key == current_asset else ""
        dropdown_items.append(
            f'                        <a class="nav-dropdown-item{cur_cls}" href="{href}" role="menuitem">\n'
            f'                            <span class="nav-dropdown-thumb"><img src="{img}" alt=""></span>\n'
            '                            <span>\n'
            f'                                <span class="nav-dropdown-title">{html.escape(title)}</span>\n'
            f'                                <span class="nav-dropdown-meta">{html.escape(meta)}</span>\n'
            '                            </span>\n'
            '                        </a>'
        )
    return (
        '    <nav class="site-nav" aria-label="Main navigation">\n'
        '        <div class="container nav-inner">\n'
        '            <a class="brand" href="index.html">\n'
        '                <span class="brand-mark" aria-hidden="true">MS</span>\n'
        '                <span>Maharaja Studio</span>\n'
        '            </a>\n\n'
        '            <ul class="nav-menu">\n'
        '                <li><a class="nav-link" href="index.html">Home</a></li>\n'
        '                <li class="nav-dropdown">\n'
        '                    <button type="button" class="nav-link" data-dropdown-trigger aria-expanded="false" aria-haspopup="true">\n'
        '                        Assets\n'
        '                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>\n'
        '                    </button>\n'
        '                    <div class="nav-dropdown-panel" role="menu">\n'
        + "\n".join(dropdown_items)
        + "\n                    </div>\n"
        '                </li>\n'
        '                <li><a class="nav-link active" href="documentation.html">Documentation</a></li>\n'
        '                <li><a class="nav-link" href="support.html">Support</a></li>\n'
        '                <li><a class="nav-link" href="contact.html">Contact</a></li>\n'
        '            </ul>\n\n'
        '            <div class="nav-actions">\n'
        '                <button type="button" class="theme-btn" data-theme-toggle aria-label="Switch theme">\n'
        '                    <svg class="icon-moon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>\n'
        '                    <svg class="icon-sun" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>\n'
        '                </button>\n'
        f'                <a class="btn btn-primary btn-sm" href="{html.escape(cta_href, quote=True)}">{html.escape(cta_label)}</a>\n'
        '                <button type="button" class="mobile-menu-btn" data-mobile-menu-toggle aria-label="Toggle navigation menu" aria-expanded="false">\n'
        '                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="7" y2="7"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="17" y2="17"/></svg>\n'
        '                </button>\n'
        '            </div>\n'
        '        </div>\n'
        '    </nav>\n'
    )


def render_mobile_drawer(group_title: str, quick_links: list[tuple[str, str]]) -> str:
    links_html = "\n            ".join(
        f'<a href="{html.escape(href, quote=True)}">{html.escape(label)}</a>'
        for href, label in quick_links
    )
    return (
        '    <div class="mobile-drawer" aria-label="Mobile navigation">\n'
        '        <div class="mobile-drawer-group">\n'
        '            <span class="mobile-drawer-label">Navigation</span>\n'
        '            <a href="index.html">Home</a>\n'
        '            <a href="documentation.html" class="active">Documentation</a>\n'
        '            <a href="support.html">Support</a>\n'
        '            <a href="contact.html">Contact</a>\n'
        '        </div>\n'
        '        <div class="mobile-drawer-group">\n'
        f'            <span class="mobile-drawer-label">{html.escape(group_title)}</span>\n'
        f'            {links_html}\n'
        '        </div>\n'
        '    </div>\n'
    )


def render_footer(product_href: str, product_label: str) -> str:
    return (
        '    <footer class="site-footer">\n'
        '        <div class="container footer-inner">\n'
        '            <div>\n'
        '                <span>&copy; 2026 Maharaja Studio. All rights reserved.</span>\n'
        '                <span style="margin: 0 8px;">·</span>\n'
        f'                <a href="{html.escape(product_href, quote=True)}" style="color: var(--text-secondary);">{html.escape(product_label)}</a>\n'
        '                <span style="margin: 0 8px;">·</span>\n'
        '                <a href="documentation.html" style="color: var(--text-secondary);">All Docs</a>\n'
        '                <span style="margin: 0 8px;">·</span>\n'
        '                <a href="legal.html" style="color: var(--text-secondary);">Legal Notice</a>\n'
        '            </div>\n'
        '            <div class="footer-links">\n'
        '                <a href="https://youtube.com/@king_of_games-l9e?si=EleZSFthz6ZBPPao" target="_blank" rel="noopener">YouTube</a>\n'
        '                <a href="https://discord.gg/GamF5bez3h" target="_blank" rel="noopener">Discord</a>\n'
        '                <a href="mailto:maharajastudiocustomerservice@gmail.com">Email</a>\n'
        '            </div>\n'
        '        </div>\n'
        '    </footer>\n'
    )


def render_pager() -> str:
    return (
        '                    <nav class="docs-pager" aria-label="Page pagination">\n'
        '                        <button type="button" id="prev-doc" class="docs-pager-btn">\n'
        '                            <span class="docs-pager-dir">Previous</span>\n'
        '                            <span class="docs-pager-title">Start of guide</span>\n'
        '                        </button>\n'
        '                        <button type="button" id="next-doc" class="docs-pager-btn is-next">\n'
        '                            <span class="docs-pager-dir">Next</span>\n'
        '                            <span class="docs-pager-title">Next guide</span>\n'
        '                        </button>\n'
        '                    </nav>\n'
    )


def render_code_block(code_str: str, lang: str = "csharp") -> str:
    lang_label = html.escape(lang.upper() if len(lang) <= 5 else lang, quote=False)
    escaped_code = html.escape(code_str, quote=False)
    return (
        '<div class="code-block-wrapper">'
        '<div class="code-block-bar">'
        f"<span>{lang_label}</span>"
        '<button type="button" class="copy-code-btn" aria-label="Copy code">'
        f"{SVG_COPY}"
        '<span class="copy-label">Copy</span></button></div>'
        f"<pre><code>{escaped_code}</code></pre></div>"
    )


# ==============================================================================
# Markdown Conversion Engine
# ==============================================================================

def clean_latex_expr(expr: str) -> tuple[str, bool]:
    raw = expr.strip()
    simple = {
        r"\rightarrow": "→",
        r"\to": "→",
        r"\leftarrow": "←",
        r"\leftrightarrow": "↔",
        r"\le": "≤",
        r"\leq": "≤",
        r"\ge": "≥",
        r"\geq": "≥",
        r"\times": "×",
        r"\Delta": "Δ",
    }
    if raw in simple:
        return simple[raw], False
    s = raw
    s = re.sub(r"\\text\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\frac\{([^}]*)\}\{([^}]*)\}", r"(\1) / (\2)", s)
    s = s.replace(r"\rightarrow", "→").replace(r"\to", "→").replace(r"\leftarrow", "←")
    s = s.replace(r"\cdot", "·").replace(r"\times", "×").replace(r"\Delta", "Δ")
    s = s.replace(r"\le", "≤").replace(r"\ge", "≥").replace(r"\infty", "∞")
    s = re.sub(r"\s+", " ", s).strip()
    return s, any(c in s for c in ("=", "/", "sin", "cos", "²", "³", "+", "(", "m/s", "ms"))


def resolve_href(raw_href: str, src_path: Path, link_map: dict[str, str], local_sec_id: str) -> tuple[str, bool]:
    href = raw_href.strip()
    if href.startswith(("http://", "https://", "mailto:")):
        return href, True
    if href.startswith("#"):
        # Local anchor inside same section or known section
        target_cand = href[1:]
        if target_cand in link_map.values():
            return href, False
        return f"#{local_sec_id}__{slugify(target_cand)}", False

    def format_target(raw_target: str) -> str:
        if raw_target.startswith("#") or ".html" in raw_target:
            return raw_target
        return f"#{raw_target}"

    path_part, _, _ = href.partition("#")
    if path_part:
        clean_part = path_part.replace("\\", "/").lower().strip()
        if clean_part in link_map:
            return format_target(link_map[clean_part]), False

        p_obj = Path(path_part)
        name_key = p_obj.name.lower()
        stem_key = p_obj.stem.lower()
        if name_key in link_map:
            return format_target(link_map[name_key]), False
        if stem_key in link_map:
            return format_target(link_map[stem_key]), False

        # Common documentation cross-reference aliases
        alias_map = {
            "scenevalidatorguide.md": "SceneValidator",
            "scenevalidator.md": "SceneValidator",
            "whatsnew_v3.0.md": "whats-new-v3",
            "whatsnew_v2.5.md": "whats-new-v25",
            "4-how-to-guides.md": "for-designers",
            "ai-assistant.md": "ai-asset-architect",
            "getting-started.md": "quick-start",
            "zonecontrolstatescorer.md": "ZoneControlStateScorerSO",
            "vaultopportunityscorer.md": "VaultOpportunityScorerSO",
            "sensorytypescorer.md": "SensoryTypeScorerSO",
        }
        if name_key in alias_map:
            target = alias_map[name_key]
            if target in link_map.values():
                return format_target(target), False
            elif target in link_map:
                return format_target(link_map[target]), False

        resolved = (src_path.parent / path_part).resolve()
        res_name = resolved.name.lower()
        res_stem = resolved.stem.lower()
        if res_name in link_map:
            return format_target(link_map[res_name]), False
        if res_stem in link_map:
            return format_target(link_map[res_stem]), False

        for root_cand in [MSMOTION_ROOT.resolve(), (WORKSPACE / "assets" / "Documentations").resolve()]:
            try:
                rel_key = resolved.relative_to(root_cand).as_posix().lower()
                if rel_key in link_map:
                    return format_target(link_map[rel_key]), False
            except ValueError:
                pass
    return href, False


def format_inline(text: str, src_path: Path, link_map: dict[str, str], local_sec_id: str) -> str:
    tokens: list[str] = []

    def stash(snippet: str) -> str:
        idx = len(tokens)
        tokens.append(snippet)
        return f"\x00TOK{idx}\x00"

    def finalize_string(chunk: str) -> str:
        cleaned = strip_emoji(chunk, strip_edges=False)
        escaped = html.escape(cleaned, quote=False)
        # Allow literal <br> inside Markdown table cells to break lines cleanly
        escaped = escaped.replace("&lt;br&gt;", "<br>").replace("&lt;br/&gt;", "<br>")
        escaped = re.sub(r"\*\*([^\n*]+?)\*\*", r"<strong>\1</strong>", escaped)
        escaped = re.sub(
            r"(?<![A-Za-z0-9])\*([^\s*][^*\n]*?[^\s*]|\S)\*(?![A-Za-z0-9])",
            r"<em>\1</em>",
            escaped,
        )
        return re.sub(r"\x00TOK(\d+)\x00", lambda mt: tokens[int(mt.group(1))], escaped)

    def repl_code(m: re.Match) -> str:
        inner = strip_emoji(m.group(1), strip_edges=True)
        if not inner:
            return ""
        return stash(f"<code>{html.escape(inner, quote=False)}</code>")

    s = re.sub(r"`([^`]+)`", repl_code, text)

    def repl_math(m: re.Match) -> str:
        txt, is_formula = clean_latex_expr(m.group(1))
        esc = html.escape(strip_emoji(txt), quote=False)
        return stash(f'<code class="math-expr">{esc}</code>' if is_formula else esc)

    s = re.sub(r"\$([^$\n]+)\$", repl_math, s)

    def repl_link(m: re.Match) -> str:
        label_raw = m.group(1)
        href_raw = m.group(2)
        resolved, is_ext = resolve_href(href_raw, src_path, link_map, local_sec_id)
        label_html = finalize_string(label_raw)
        attrs = ' target="_blank" rel="noopener"' if is_ext else ""
        return stash(f'<a href="{html.escape(resolved, quote=True)}"{attrs}>{label_html}</a>')

    s = re.sub(r"\[((?:[^\[\]]|\[[^\[\]]*\])+)\]\(([^)]+)\)", repl_link, s)
    return finalize_string(s)


def parse_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [c.strip() for c in stripped.split("|")]


MERMAID_REPLACEMENTS = {
    "rt-intro": (
        "+-----------------------------------------------------------------------------------+\n"
        "|                                  Gameplay Code                                    |\n"
        "|     (Triggers Play, CrossFade, Stops, or MSMotionInteraction Choreography)        |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "             |                                                  |\n"
        "             v                                                  v\n"
        "+------------------------------------+         +------------------------------------+\n"
        "|         MSMotionAnimator           |         |       MSMotionInteraction          |\n"
        "| (Drives PlayableGraph & Mixers)    |         | (Multi-Actor Orchestration Engine) |\n"
        "+------------------------------------+         +------------------------------------+\n"
        "       /          |          \\                          |                    \\\n"
        "      v           v           v                         v                     v\n"
        "+------------+ +------------+ +------------+   +-------------------+  +-------------------+\n"
        "|  FXPlayer  | |  Stretch   | |    Rig     |   | Dynamic Summons & |  |    Interaction    |\n"
        "| (Audio/VFX | | Applicator | | Controller |   | Actor Object Pool |  | Overrides Presets |\n"
        "|   Pool)    | | (Scaling)  | |   (IK)     |   | (MSMotionActorPool)| | (Body Spacing/Gait)|\n"
        "+------------+ +------------+ +------------+   +-------------------+  +-------------------+"
    ),
    "rt-interaction-overrides": (
        "+-----------------------------------+      +----------------------------------------+\n"
        "| MSMotionInteractionConfig         |      | MSMotionInteractionOverrides           |\n"
        "| (Authored Choreography Baseline)  |      | (Non-Destructive Designer Preset)      |\n"
        "+-----------------------------------+      +----------------------------------------+\n"
        "                  |                                            |\n"
        "                  +---------------------+----------------------+\n"
        "                                        v\n"
        "                   +-----------------------------------------+\n"
        "                   | MSMotionInteractionSession              |\n"
        "                   | (Resolved Clamps, Offsets, Gaits & FX)  |\n"
        "                   +-----------------------------------------+\n"
        "                     /                  |                  \\\n"
        "                    v                   v                   v\n"
        "       [Lead Actor Graph]      [Partner Actor Graph]     [Dynamic Summons]"
    ),
}


def md_to_html(
    md_text: str,
    src_path: Path,
    link_map: dict[str, str],
    sec_id: str,
    strip_first_h1: bool = True,
    post_heading_injections: dict[str, str] | None = None,
    omit_lines_containing: tuple[str, ...] = (),
) -> str:
    """Convert CommonMark/GFM markdown into Studio doc HTML."""
    lines = md_text.splitlines()
    out: list[str] = []
    i = 0
    n = len(lines)
    removed_h1 = False
    injections_used: set[str] = set()

    def is_table_start(idx: int) -> bool:
        if idx + 1 >= n:
            return False
        l1 = lines[idx].strip()
        l2 = lines[idx + 1].strip()
        return ("|" in l1 and "|" in l2 and bool(re.match(r"^\|?[\s:\-|]+\|?$", l2)) and "-" in l2)

    def render_blockquote_html(bq_lines: list[str]) -> str:
        alert_match = re.match(r"^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*)$", bq_lines[0], flags=re.IGNORECASE) if bq_lines else None
        if alert_match:
            kind = alert_match.group(1).upper()
            tail = alert_match.group(2).strip()
            body_lines = ([tail] if tail else []) + bq_lines[1:]
            cls_map = {
                "NOTE": ("is-info", "Note", SVG_ALERT_INFO),
                "TIP": ("is-success", "Tip", SVG_ALERT_INFO),
                "IMPORTANT": ("is-warning", "Important", SVG_ALERT_WARN),
                "WARNING": ("is-warning", "Warning", SVG_ALERT_WARN),
                "CAUTION": ("is-danger", "Caution", SVG_ALERT_WARN),
            }
            cls_name, label_txt, svg_ico = cls_map.get(kind, ("is-info", kind.title(), SVG_ALERT_INFO))
            p_groups: list[list[str]] = [[]]
            for bl in body_lines:
                if not bl:
                    if p_groups[-1]:
                        p_groups.append([])
                else:
                    p_groups[-1].append(bl)
            inner = "".join(
                f"<p>{'<br>'.join(format_inline(g, src_path, link_map, sec_id) for g in grp)}</p>"
                for grp in p_groups
                if grp
            )
            return (
                f'<div class="doc-callout {cls_name}">'
                f'<div class="doc-callout-label">{svg_ico}<span>{label_txt}</span></div>'
                f"{inner}</div>"
            )
        p_groups = [[]]
        for bl in bq_lines:
            if not bl:
                if p_groups[-1]:
                    p_groups.append([])
            else:
                p_groups[-1].append(bl)
        inner = "".join(
            f"<p>{'<br>'.join(format_inline(g, src_path, link_map, sec_id) for g in grp)}</p>"
            for grp in p_groups
            if grp
        )
        return f"<blockquote>{inner}</blockquote>"

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if any(tok in stripped for tok in omit_lines_containing):
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
            if lang.lower() == "mermaid" and sec_id in MERMAID_REPLACEMENTS:
                out.append(render_code_block(MERMAID_REPLACEMENTS[sec_id], "architecture"))
            else:
                code_body = "\n".join(code_lines)
                effective_lang = "layout" if (lang == "text" and ("+---" in code_body or "| " in code_body)) else lang
                out.append(render_code_block(code_body, effective_lang))
            continue

        if re.match(r"^(\-{3,}|\*{3,}|_{3,})$", stripped):
            out.append("<hr>")
            i += 1
            continue

        hm = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if hm:
            lvl = len(hm.group(1))
            heading_txt = hm.group(2).strip()
            if lvl == 1 and strip_first_h1 and not removed_h1:
                removed_h1 = True
                if post_heading_injections and "__TOP__" in post_heading_injections:
                    out.append(post_heading_injections["__TOP__"])
                    injections_used.add("__TOP__")
                i += 1
                continue
            h_clean = strip_emoji(heading_txt)
            h_slug = f"{sec_id}__{slugify(h_clean)}"
            out.append(f'<h{lvl} id="{h_slug}">{format_inline(heading_txt, src_path, link_map, sec_id)}</h{lvl}>')
            if post_heading_injections:
                for key, html_frag in post_heading_injections.items():
                    if key != "__TOP__" and key not in injections_used and key.lower() in h_clean.lower():
                        out.append(html_frag)
                        injections_used.add(key)
            i += 1
            continue

        if stripped.startswith(">"):
            bq_lines = []
            while i < n and lines[i].strip().startswith(">"):
                bq_lines.append(lines[i].strip()[1:].lstrip())
                i += 1
            out.append(render_blockquote_html(bq_lines))
            continue

        if is_table_start(i):
            headers = parse_table_row(lines[i])
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(parse_table_row(lines[i]))
                i += 1
            th_html = "".join(f"<th>{format_inline(h, src_path, link_map, sec_id)}</th>" for h in headers)
            tr_html = []
            for r in rows:
                padded = r + [""] * (len(headers) - len(r))
                tds = [f"<td>{format_inline(cell, src_path, link_map, sec_id)}</td>" for cell in padded[: len(headers)]]
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
                        if k < n and (
                            re.match(r"^(\s*)([-*+]|\d+\.)\s+", lines[k])
                            or (lines[k].strip().startswith(">") and len(lines[k]) - len(lines[k].lstrip()) > base_indent)
                        ):
                            j = k
                            continue
                        break
                    if cur.strip().startswith(">"):
                        ind_bq = len(cur.replace("\t", "  ")) - len(cur.replace("\t", "  ").lstrip())
                        if ind_bq < base_indent:
                            break
                        bq_lines = []
                        while j < n and lines[j].strip().startswith(">"):
                            bq_lines.append(lines[j].strip()[1:].lstrip())
                            j += 1
                        bq_html = render_blockquote_html(bq_lines)
                        if items:
                            items[-1] = items[-1][:-5] + bq_html + "</li>"
                        else:
                            items.append(f"<li>{bq_html}</li>")
                        continue
                    m_cur = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.+)$", cur)
                    if not m_cur:
                        break
                    ind = len(m_cur.group(1).replace("\t", "  "))
                    cur_tag = "ol" if m_cur.group(2).endswith(".") else "ul"
                    if m_cur.group(3).lstrip().startswith(">") and ind >= base_indent:
                        bq_lines = []
                        while j < n:
                            m_bq = re.match(r"^(\s*)([-*+]|\d+\.)\s+>\s*(.*)$", lines[j])
                            if not m_bq or len(m_bq.group(1).replace("\t", "  ")) < ind:
                                break
                            bq_lines.append(m_bq.group(3))
                            j += 1
                        bq_html = render_blockquote_html(bq_lines)
                        if items:
                            items[-1] = items[-1][:-5] + bq_html + "</li>"
                        else:
                            items.append(f"<li>{bq_html}</li>")
                        continue
                    if ind < base_indent or (ind == base_indent and cur_tag != tag):
                        break
                    if ind > base_indent:
                        sub_html, j = render_list(j, ind)
                        if items:
                            items[-1] = items[-1][:-5] + sub_html + "</li>"
                        else:
                            items.append(f"<li>{sub_html}</li>")
                        continue
                    item_html = format_inline(m_cur.group(3), src_path, link_map, sec_id)
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
            if any(tok in cur_s for tok in omit_lines_containing):
                i += 1
                continue
            p_lines.append(cur_s)
            i += 1
        if p_lines:
            out.append(f"<p>{' '.join(format_inline(p, src_path, link_map, sec_id) for p in p_lines)}</p>")

    if post_heading_injections:
        for key, html_frag in post_heading_injections.items():
            if key not in injections_used and key != "__TOP__":
                out.insert(0, html_frag)

    return "\n".join(out)


def render_figure(src: str, alt: str, caption: str) -> str:
    return (
        '<figure class="doc-figure">'
        f'<img src="{html.escape(src, quote=True)}" alt="{html.escape(alt, quote=True)}" loading="lazy">'
        f'<figcaption class="doc-figcaption">{html.escape(caption)}</figcaption>'
        "</figure>"
    )


def render_fx_cards_grid() -> str:
    cards = [
        ("#ce-audio-fx-node", "Audio FX", "Frame-accurate sound playback with pitch variance, 3D spatialization, and pooling."),
        ("#ce-camera-shake-node", "Camera Shake FX", "Cinemachine impulse triggers, procedural noise profiles, and directional trauma shakes."),
        ("#ce-particle-fx-node", "Particle FX", "Pooled Shuriken particle systems with bone sockets, spline flight, and emission bursts."),
        ("#ce-vfx-graph-node", "VFX Graph FX", "Unity Visual Effect Graph instances with dynamic property drives and GPU particle simulation."),
        ("#ce-decal-fx-node", "Decal FX", "Directional raycast surface decals (blood, dirt, runes, skid marks) with slope angle culling."),
        ("#ce-spawn-fx-node", "Spawn FX", "Instantiates custom prefabs at bone sockets with zero runtime GC spikes and handover support."),
        ("#ce-script-event-node", "Script Event FX", "Dispatches typed C# callbacks via MSMotionScriptEventBus (float, int, bool, string, GameObject)."),
        ("#ce-transform-fx-node", "Transform FX", "Dynamic bone/socket offsets with 3D Bezier spline flight paths and easing transitions."),
    ]
    items = "".join(
        f'<a href="{href}" class="doc-mini-card" style="text-decoration:none;display:block;">'
        f'<h6>{html.escape(title)}</h6><p>{html.escape(desc)}</p></a>'
        for href, title, desc in cards
    )
    return f'<div class="doc-card-grid">{items}</div>'


# ==============================================================================
# MSMotion Documentation Builder
# ==============================================================================

MSMOTION_SECTIONS = [
    # (category_key, category_label, section_id, nav_label, md_rel_path, module_key)
    ("animation-editor", "Animation Editor", "ae-intro", "Overview", "EditorTool/AnimationEditor/index.md", "ae"),
    ("animation-editor", "Animation Editor", "ae-getting-started", "Getting Started", "EditorTool/AnimationEditor/getting-started.md", "ae"),
    ("animation-editor", "Animation Editor", "ae-timeline", "Timeline & Range Operations", "EditorTool/AnimationEditor/timeline-and-range-operations.md", "ae"),
    ("animation-editor", "Animation Editor", "ae-keyframe", "Curve & Keyframe Editing", "EditorTool/AnimationEditor/keyframe-editing.md", "ae"),
    ("animation-editor", "Animation Editor", "ae-events", "Animation Events", "EditorTool/AnimationEditor/animation-events.md", "ae"),
    ("animation-editor", "Animation Editor", "ae-bone-ik", "Bone Overlay & IK/FK Solver", "EditorTool/AnimationEditor/bone-overlay-and-ik.md", "ae"),
    ("animation-editor", "Animation Editor", "ae-transition", "Transition & Bridging", "EditorTool/AnimationEditor/transition-and-bridging.md", "ae"),
    ("animation-editor", "Animation Editor", "ae-advanced-tools", "Advanced Editorial Tools", "EditorTool/AnimationEditor/advanced-editorial-tools.md", "ae"),
    ("animation-editor", "Animation Editor", "ae-clip-management", "Clip & Asset Management", "EditorTool/AnimationEditor/clip-asset-management.md", "ae"),
    ("animation-editor", "Animation Editor", "ae-changelog", "Changelog (v4.5 – v4.6)", "EditorTool/AnimationEditor/changelog.md", "ae"),

    ("composition-core", "Composition Editor", "ce-intro", "Composition Overview", "EditorTool/CompositionEditor/index.md", "ce"),
    ("composition-core", "Composition Editor", "ce-settings", "Editor Settings", "EditorTool/CompositionEditor/editor-settings.md", "ce"),
    ("composition-core", "Composition Editor", "ce-clip-node", "Animation Clip Node", "EditorTool/CompositionEditor/animation-clip-node.md", "ce"),
    ("composition-core", "Composition Editor", "ce-pose-node", "Pose Node", "EditorTool/CompositionEditor/pose-node.md", "ce"),

    ("composition-solvers", "Modifiers & Solvers", "ce-foot-ik-node", "Foot IK Node", "EditorTool/CompositionEditor/foot-ik-node.md", "ce"),
    ("composition-solvers", "Modifiers & Solvers", "ce-ik-override-node", "IK Override Node", "EditorTool/CompositionEditor/ik-override-node.md", "ce"),
    ("composition-solvers", "Modifiers & Solvers", "ce-ik-rig-config", "IK Rig Configuration", "EditorTool/CompositionEditor/ik-rig-configuration.md", "ce"),
    ("composition-solvers", "Modifiers & Solvers", "ce-look-at-node", "Look-At Constraint Node", "EditorTool/CompositionEditor/look-at-node.md", "ce"),
    ("composition-solvers", "Modifiers & Solvers", "ce-jiggle-node", "Jiggle Physics Node", "EditorTool/CompositionEditor/jiggle-physics-node.md", "ce"),
    ("composition-solvers", "Modifiers & Solvers", "ce-trajectory-node", "Trajectory Override Node", "EditorTool/CompositionEditor/trajectory-override-node.md", "ce"),
    ("composition-solvers", "Modifiers & Solvers", "ce-bone-subdivision-node", "Bone Subdivision Node (Exp)", "EditorTool/CompositionEditor/bone-subdivision-node.md", "ce"),

    ("composition-fx", "FX & Gameplay Events", "ce-fx-overview", "FX Nodes Overview", "EditorTool/CompositionEditor/fx-nodes-overview.md", "ce"),
    ("composition-fx", "FX & Gameplay Events", "ce-audio-fx-node", "Audio FX Node", "EditorTool/CompositionEditor/audio-fx-node.md", "ce"),
    ("composition-fx", "FX & Gameplay Events", "ce-camera-shake-node", "Camera Shake FX Node", "EditorTool/CompositionEditor/camera-shake-fx-node.md", "ce"),
    ("composition-fx", "FX & Gameplay Events", "ce-particle-fx-node", "Particle FX Node", "EditorTool/CompositionEditor/particle-fx-node.md", "ce"),
    ("composition-fx", "FX & Gameplay Events", "ce-vfx-graph-node", "VFX Graph FX Node", "EditorTool/CompositionEditor/vfx-graph-fx-node.md", "ce"),
    ("composition-fx", "FX & Gameplay Events", "ce-decal-fx-node", "Decal FX Node", "EditorTool/CompositionEditor/decal-fx-node.md", "ce"),
    ("composition-fx", "FX & Gameplay Events", "ce-spawn-fx-node", "Spawn FX Node", "EditorTool/CompositionEditor/spawn-fx-node.md", "ce"),
    ("composition-fx", "FX & Gameplay Events", "ce-script-event-node", "Script Event FX Node", "EditorTool/CompositionEditor/script-event-fx-node.md", "ce"),
    ("composition-fx", "FX & Gameplay Events", "ce-transform-fx-node", "Transform FX Node", "EditorTool/CompositionEditor/transform-fx-node.md", "ce"),

    ("composition-choreo", "Multi-Actor Choreography", "ce-actor-roster-window", "Actor Roster & Alignment", "EditorTool/CompositionEditor/actor-roster-window.md", "ce"),
    ("composition-choreo", "Multi-Actor Choreography", "ce-actor-lifecycle-nodes", "Actor Lifecycle Nodes", "EditorTool/CompositionEditor/actor-lifecycle-nodes.md", "ce"),
    ("composition-choreo", "Multi-Actor Choreography", "ce-interaction-overrides-inspector", "Interaction Overrides Inspector", "EditorTool/CompositionEditor/interaction-overrides-inspector.md", "ce"),

    ("composition-export", "Baking & Pipelines", "ce-export-options", "Export Options", "EditorTool/CompositionEditor/export-options.md", "ce"),
    ("composition-export", "Baking & Pipelines", "ce-batch-export", "Batch Export Queue", "EditorTool/CompositionEditor/batch-export.md", "ce"),
    ("composition-export", "Baking & Pipelines", "ce-metadata-manager", "Metadata Manager", "EditorTool/CompositionEditor/metadata-manager.md", "ce"),

    ("runtime", "Runtime Framework", "rt-intro", "Runtime Overview", "RuntimeSystem/index.md", "rt"),
    ("runtime", "Runtime Framework", "rt-quick-start", "Quick Start Guide", "RuntimeSystem/quick-start.md", "rt"),
    ("runtime", "Runtime Framework", "rt-core-animation", "Core Animation System", "RuntimeSystem/core-animation-system.md", "rt"),
    ("runtime", "Runtime Framework", "rt-multi-actor-interaction", "Multi-Actor Interaction", "RuntimeSystem/multi-actor-interaction.md", "rt"),
    ("runtime", "Runtime Framework", "rt-interaction-overrides", "Interaction Overrides System", "RuntimeSystem/interaction-overrides.md", "rt"),
    ("runtime", "Runtime Framework", "rt-rigging-ik", "Rigging & IK System", "RuntimeSystem/rigging-and-ik-system.md", "rt"),
    ("runtime", "Runtime Framework", "rt-stretch-scale", "Stretch & Scale System", "RuntimeSystem/stretch-and-scale-system.md", "rt"),
    ("runtime", "Runtime Framework", "rt-dynamic-bone-subdivision", "Dynamic Bone Subdivision", "RuntimeSystem/dynamic-bone-subdivision.md", "rt"),
    ("runtime", "Runtime Framework", "rt-fx-event", "FX & Event System", "RuntimeSystem/fx-event-system.md", "rt"),
    ("runtime", "Runtime Framework", "rt-optimization", "Optimization & Best Practices", "RuntimeSystem/optimization-and-best-practices.md", "rt"),

    ("troubleshooting", "Troubleshooting", "tb-foot-ik-forced", "Foot IK Forced on All Animations", "Troubleshooting/Troubleshooting_Foot_IK.md", "tb"),
    ("troubleshooting", "Troubleshooting", "tb-roll-flip-glitch", "Roll & Flip Rotation Glitches", "Troubleshooting/Troubleshooting_Roll_Animations.md", "tb"),
    ("troubleshooting", "Troubleshooting", "tb-composition-troubleshooting", "Composition Editor Troubleshooting", "EditorTool/CompositionEditor/troubleshooting.md", "tb"),
    ("troubleshooting", "Troubleshooting", "tb-animation-troubleshooting", "Animation Editor Troubleshooting", "EditorTool/AnimationEditor/troubleshooting.md", "tb"),
]

MSMOTION_FIGURES = {
    "ae-intro": {"Editor Interface Layout": render_figure("assets/Images/MSMotion/ae-layout.png", "MSMotion Animation Editor Layout", "Figure: Animation Editor workspace — Top Toolbar, Left Sidebar Accordion, Timeline Ruler, and Scrubber Tracks")},
    "ae-events": {"__TOP__": render_figure("assets/Images/MSMotion/ce-event-management.png", "Animation Events Management", "Figure: Animation Events timeline markers and inspector panel")},
    "ce-intro": {"Editor Window Layout": render_figure("assets/Images/MSMotion/ce-layout.png", "Composition Editor Layout", "Figure: Composition Editor workspace — Top Toolbar, Breadcrumb Bar, Layer Stack, Timeline View, and Inspector")},
    "ce-settings": {"__TOP__": render_figure("assets/Images/MSMotion/setting.png", "MSMotion Settings Panel", "Figure: MSMotion Settings window for General, Timeline, Appearance, and Snapping configuration")},
    "ce-ik-rig-config": {"__TOP__": render_figure("assets/Images/MSMotion/ce-rig-config.png", "IK Rig Configuration Window", "Figure: IK Rig Configuration Editor Window")},
    "ce-jiggle-node": {"Colliders": render_figure("assets/Images/MSMotion/ce-jiggle-colliders.png", "Jiggle Physics Colliders", "Figure: Jiggle Physics Scene View colliders and chain preview")},
    "ce-trajectory-node": {"__TOP__": render_figure("assets/Images/MSMotion/ce-trajectory-spline.png", "Trajectory Spline Override", "Figure: Trajectory Override Bezier spline editing inside Unity Scene View")},
    "ce-fx-overview": {
        "__TOP__": render_fx_cards_grid(),
        "Property Overrides": render_figure("assets/Images/MSMotion/ce-property-overrides.png", "Property Overrides Workflow", "Figure: Property Overrides workflow driving runtime component fields and method calls per FX slot"),
    },
    "ce-export-options": {"__TOP__": render_figure("assets/Images/MSMotion/ce-export-window.png", "Export Options Window", "Figure: Export Options Window for baking compositions to AnimationClips and companion Configs")},
    "ce-batch-export": {"__TOP__": render_figure("assets/Images/MSMotion/ce-batch-queue.png", "Batch Export Queue Window", "Figure: Batch Export Queue window")},
    "ce-metadata-manager": {"__TOP__": render_figure("assets/Images/MSMotion/ce-metadata-manager.png", "Metadata Manager Window", "Figure: Metadata Manager window")},
}


def build_msmotion_overview_section() -> str:
    module_cards = [
        ("Animation Editor", "#ae-intro", "10 chapters", "Direct edit-mode authoring on native .anim assets: 1-click FBX clip extraction, range ops, curve smoothing filters, Time Warper, Remove Root Motion, and Scene View Live Link."),
        ("Composition Editor", "#ce-intro", "26 chapters", "PSD-like multi-layer animation mixer, 19 Slot Types, Foot IK & IK Overrides, Jiggle Physics, Trajectory Splines, 8 FX node types, Multi-Actor Roster, and batch baking."),
        ("Runtime Framework", "#rt-intro", "10 chapters", "PlayableGraph API core (MSMotionAnimator), synchronized multi-actor orchestration (MSMotionInteraction), Interaction Overrides presets, FX pooling, and Rig/Stretch controllers."),
        ("Troubleshooting", "#tb-foot-ik-forced", "4 chapters", "Diagnostics for Unity Foot IK bubbling on PlayableGraph base layers, Roll & Flip gimbal spikes (1-3 frame glitches), composition export checks, and editor warnings."),
    ]
    cards_html = "\n".join(
        '<div class="doc-index-card">'
        '<div class="doc-index-card-head">'
        f'<a href="{href}" class="doc-index-card-title">{html.escape(title)}</a>'
        f'<span class="eco-pill-count">{html.escape(cnt)}</span>'
        '</div>'
        f'<p class="doc-index-card-desc">{html.escape(desc)}</p>'
        f'<div class="doc-index-chips"><a href="{href}" class="doc-index-chip">Open guide</a></div>'
        '</div>'
        for title, href, cnt, desc in module_cards
    )

    explorer_rows = []
    for _ck, cat_label, sec_id, nav_label, rel_path, mod in MSMOTION_SECTIONS:
        mod_tag = {"ae": "Animation Editor", "ce": "Composition Editor", "rt": "Runtime Framework", "tb": "Troubleshooting"}[mod]
        search_txt = html.escape(f"{nav_label} {cat_label} {mod_tag} {rel_path}".lower(), quote=True)
        explorer_rows.append(
            f'<tr data-cat-row data-cat-targets="{mod}" data-cat-search="{search_txt}">'
            f'<td><a href="#{sec_id}"><code>{html.escape(nav_label)}</code></a></td>'
            f'<td><span class="tag">{html.escape(cat_label)}</span></td>'
            f'<td><span class="mono" style="font-size:12px;color:var(--text-muted);">{html.escape(rel_path)}</span></td>'
            '</tr>'
        )

    return (
        '<section id="overview" class="docs-section" data-doc-title="MSMotion v2.0 Documentation Hub">\n'
        '    <article class="doc-article">\n'
        '        <div class="doc-article-head">\n'
        '            <div class="doc-article-meta">\n'
        '                <span class="mono" style="color:var(--accent-text);">MSMotion v2.0</span>\n'
        '                <span>/</span>\n'
        '                <span>Tools &gt; Maharaja Studio &gt; MsMotion</span>\n'
        '                <span class="tag" style="margin-left:auto;">50 chapters</span>\n'
        '            </div>\n'
        '            <h1>MSMotion v2.0 Documentation</h1>\n'
        '        </div>\n'
        '        <p class="doc-lead">MSMotion is an edit-mode animation authoring workspace, multi-actor choreography director, and PlayableGraph runtime framework for Unity 6+. Edit native <code>.anim</code> clips, layer 19 timeline slot types, trigger 8 pooled FX channels, and coordinate Humanoid &amp; Generic multi-actor sequences with 0ms frame drift.</p>\n'
        '        <div class="doc-callout is-info">\n'
        '            <div class="doc-callout-label">'
        f'{SVG_ALERT_INFO}<span>Workspace Entry Points &amp; Demo Build</span></div>\n'
        '            <p>Open inside Unity via <strong>Tools &gt; Maharaja Studio &gt; MsMotion</strong>. A standalone <a href="https://github.com/maharajastudiocustomerservice-cell/MSMotion-Demo-Build-win/releases/tag/Demo" target="_blank" rel="noopener">Windows Demo Build</a> is also available on GitHub Releases.</p>\n'
        '        </div>\n'
        '        <h2>Documentation Modules</h2>\n'
        f'        <div class="doc-index-grid">{cards_html}</div>\n'
        '        <h2>Interactive Chapter Directory</h2>\n'
        '        <div data-cat-explorer>\n'
        '            <div class="cat-filter-bar">\n'
        '                <input type="search" class="cat-filter-input" placeholder="Filter all 50 chapters by topic, node, or file..." aria-label="Filter MSMotion chapters">\n'
        '                <div class="cat-target-pills" role="group" aria-label="Module filter">\n'
        '                    <button type="button" class="cat-target-pill is-active" data-target-filter="all">All</button>\n'
        '                    <button type="button" class="cat-target-pill" data-target-filter="ae">Animation</button>\n'
        '                    <button type="button" class="cat-target-pill" data-target-filter="ce">Composition</button>\n'
        '                    <button type="button" class="cat-target-pill" data-target-filter="rt">Runtime</button>\n'
        '                    <button type="button" class="cat-target-pill" data-target-filter="tb">Troubleshooting</button>\n'
        '                </div>\n'
        '                <span class="cat-filter-count">Showing 50 of 50</span>\n'
        '            </div>\n'
        '            <div class="doc-table-wrap">\n'
        '                <table class="studio-table">\n'
        '                    <thead><tr><th>Chapter</th><th>Category</th><th>Source File</th></tr></thead>\n'
        f'                    <tbody>{"".join(explorer_rows)}</tbody>\n'
        '                </table>\n'
        '            </div>\n'
        '        </div>\n'
        '    </article>\n'
        '</section>\n'
    )


def build_msmotion_docs() -> None:
    link_map: dict[str, str] = {}
    for _ck, _cl, sec_id, _nav, rel_path, _mod in MSMOTION_SECTIONS:
        link_map[rel_path.lower()] = sec_id

    # Build sidebar groups in order
    cat_order: list[tuple[str, str]] = []
    grouped: dict[str, list[tuple[str, str, str, str]]] = {}
    for cat_key, cat_label, sec_id, nav_label, rel_path, mod in MSMOTION_SECTIONS:
        if cat_key not in grouped:
            cat_order.append((cat_key, cat_label))
            grouped[cat_key] = []
        grouped[cat_key].append((sec_id, nav_label, rel_path, mod))

    sidebar_groups_html = []
    for idx, (cat_key, cat_label) in enumerate(cat_order):
        items = grouped[cat_key]
        collapsed_cls = " is-collapsed" if idx > 1 else ""
        expanded_attr = "false" if idx > 1 else "true"
        li_html = "".join(
            f'<li><a href="#{sec_id}" class="docs-nav-link">{html.escape(nav_label)}</a></li>'
            for sec_id, nav_label, _rp, _m in items
        )
        sidebar_groups_html.append(
            f'<div class="docs-cat-group{collapsed_cls}">'
            f'<button type="button" class="docs-cat-btn" aria-expanded="{expanded_attr}">'
            f'<span>{html.escape(cat_label)}</span>'
            f'<span style="display:inline-flex;align-items:center;gap:6px;">'
            f'<span class="docs-cat-count">{len(items)}</span>{SVG_CHEVRON}</span>'
            '</button>'
            f'<ul class="docs-nav-menu">{li_html}</ul>'
            '</div>'
        )

    sections_html = [build_msmotion_overview_section()]
    mod_names = {"ae": "Animation Editor", "ce": "Composition Editor", "rt": "Runtime Framework", "tb": "Troubleshooting"}
    mod_start = {"ae": "ae-intro", "ce": "ce-intro", "rt": "rt-intro", "tb": "tb-foot-ik-forced"}

    for _ck, cat_label, sec_id, nav_label, rel_path, mod in MSMOTION_SECTIONS:
        md_path = MSMOTION_ROOT / rel_path
        if not md_path.exists():
            raise FileNotFoundError(f"Missing MSMotion markdown file: {md_path}")
        md_text = md_path.read_text(encoding="utf-8")
        title = human_title_from_md(md_text, nav_label)
        injections = MSMOTION_FIGURES.get(sec_id)
        body_html = md_to_html(
            md_text,
            md_path,
            link_map,
            sec_id,
            strip_first_h1=True,
            post_heading_injections=injections,
        )
        crumb_tail = (
            f'<a href="#overview" class="doc-crumb-link">MSMotion v2.0</a>'
            '                <span>/</span>\n'
            f'                <span>{html.escape(mod_names[mod])}</span>'
            if cat_label == mod_names[mod]
            else (
                f'<a href="#{mod_start[mod]}" class="doc-crumb-link">{html.escape(mod_names[mod])}</a>\n'
                '                <span>/</span>\n'
                f'                <span>{html.escape(cat_label)}</span>'
            )
        )
        sections_html.append(
            f'<section id="{sec_id}" class="docs-section" data-doc-title="{html.escape(title, quote=True)}">\n'
            '    <article class="doc-article">\n'
            '        <div class="doc-article-head">\n'
            '            <div class="doc-article-meta">\n'
            f'                {crumb_tail}\n'
            f'                <span class="mono" style="margin-left:auto;">{html.escape(rel_path)}</span>\n'
            '            </div>\n'
            f'            <h1>{html.escape(title)}</h1>\n'
            '        </div>\n'
            f'{body_html}\n'
            '    </article>\n'
            '</section>\n'
        )

    subnav_html = (
        '    <div class="eco-subnav" aria-label="MSMotion documentation modules">\n'
        '        <div class="container">\n'
        '            <div class="eco-subnav-inner">'
        '<a href="#overview" class="eco-pill" data-doc-prefixes="overview"><span>Overview</span><span class="eco-pill-count">Start</span></a>'
        '<a href="#ae-intro" class="eco-pill" data-doc-prefixes="ae-"><span>Animation Editor</span><span class="eco-pill-count">10</span></a>'
        '<a href="#ce-intro" class="eco-pill" data-doc-prefixes="ce-"><span>Composition Editor</span><span class="eco-pill-count">26</span></a>'
        '<a href="#rt-intro" class="eco-pill" data-doc-prefixes="rt-"><span>Runtime Framework</span><span class="eco-pill-count">10</span></a>'
        '<a href="#tb-foot-ik-forced" class="eco-pill" data-doc-prefixes="tb-"><span>Troubleshooting</span><span class="eco-pill-count">4</span></a>'
        '</div>\n'
        '        </div>\n'
        '    </div>\n'
    )

    page_html = (
        '<!DOCTYPE html>\n'
        '<html lang="en" data-theme="dark">\n\n'
        '<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '    <title>MSMotion v2.0 — Documentation · Maharaja Studio</title>\n'
        '    <meta name="description" content="Complete reference manual for MaharajaStudio MSMotion v2.0: Animation Editor, Composition Editor, Multi-Actor Choreography, Modifiers, 8 FX Event Nodes, and PlayableGraph Runtime API.">\n'
        '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
        '    <link rel="stylesheet" href="css/studio.css">\n'
        '</head>\n\n'
        '<body class="docs-workspace">\n'
        + render_nav("ms-motion", "ms-motion.html", "Asset overview")
        + render_mobile_drawer("MSMotion Modules", [
            ("ms-motion.html", "MSMotion Overview"),
            ("#overview", "Documentation Hub"),
            ("#ae-intro", "Animation Editor (10)"),
            ("#ce-intro", "Composition Editor (26)"),
            ("#rt-intro", "Runtime Framework (10)"),
            ("#tb-foot-ik-forced", "Troubleshooting (4)"),
        ])
        + subnav_html
        + '\n    <main>\n'
        '        <div class="container">\n'
        '            <div class="docs-shell">\n'
        '                <aside class="docs-sidebar" aria-label="MSMotion documentation navigation">\n'
        '                    <div class="docs-sidebar-head">\n'
        '                        <div class="docs-sidebar-title-row">\n'
        '                            <span class="docs-sidebar-title">MSMotion Docs</span>\n'
        '                            <span style="display:inline-flex;align-items:center;gap:8px;">\n'
        f'                                <span class="mono" style="font-size: 11px; color: var(--text-muted);">{len(MSMOTION_SECTIONS) + 1} guides</span>\n'
        '                                <button type="button" class="docs-sidebar-close" data-doc-sidebar-close aria-label="Close chapters drawer">\n'
        '                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>\n'
        '                                </button>\n'
        '                            </span>\n'
        '                        </div>\n'
        '                        <div class="docs-search-wrap">\n'
        '                            <svg class="docs-search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>\n'
        '                            <input type="search" id="doc-search" class="docs-search-input" style="padding-right:12px;" placeholder="Filter all 50 chapters..." aria-label="Filter MSMotion chapters" autocomplete="off">\n'
        '                        </div>\n'
        '                    </div>\n'
        '                    <div class="docs-sidebar-body">\n'
        '                        <div class="docs-pinned-group">\n'
        '                            <div class="docs-pinned-label">Start Here</div>\n'
        '                            <a href="#overview" class="docs-nav-link"><span>MSMotion Documentation Hub</span><span class="eco-pill-count">Index</span></a>\n'
        '                        </div>\n'
        + "\n".join(sidebar_groups_html)
        + '\n                    </div>\n'
        '                </aside>\n\n'
        '                <div class="docs-main">\n'
        '                    <div class="docs-mobile-toolbar">\n'
        '                        <button type="button" id="doc-sidebar-toggle" class="btn btn-secondary btn-sm" aria-expanded="false">\n'
        '                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="7" y2="7"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="17" y2="17"/></svg>\n'
        '                            Chapters (50)\n'
        '                        </button>\n'
        '                        <a class="btn btn-secondary btn-sm" href="ms-motion.html">MSMotion Overview</a>\n'
        '                    </div>\n\n'
        + "\n".join(sections_html)
        + render_pager()
        + '                </div>\n'
        '            </div>\n'
        '        </div>\n'
        '    </main>\n\n'
        + render_footer("ms-motion.html", "MSMotion v2.0")
        + '    <script src="js/studio.js"></script>\n'
        '</body>\n\n'
        '</html>\n'
    )

    out_path = WORKSPACE / "ms-motion-docs.html"
    out_path.write_text(page_html, encoding="utf-8")
    print(f"Wrote {out_path.relative_to(WORKSPACE)} ({len(MSMOTION_SECTIONS) + 1} sections)")


# ==============================================================================
# Object Finder Pro Documentation Builder
# ==============================================================================

def split_ofp_readme(readme_text: str) -> dict[str, str]:
    """Slice assets/Documentations/ObjectFinderPro/README.md cleanly by heading boundaries."""
    markers = [
        ("main-window", "# Object Finder Tool", "### Smart Search"),
        ("smart-search", "### Smart Search", "### 2. Core Filter Options"),
        ("core-filters", "### 2. Core Filter Options", "### 3. Search Behavior & Performance"),
        ("search-behavior", "### 3. Search Behavior & Performance", "### 4. Results Area"),
        ("results-area", "### 4. Results Area", "### 5. Other Controls & Features"),
        ("other-controls", "### 5. Other Controls & Features", "### 6. Multi-Component Filter"),
        ("multi-component-filter", "### 6. Multi-Component Filter", "## Folder Selection Window"),
        ("folder-selection", "## Folder Selection Window", "### 7. Advanced: Filter by Component Signature"),
        ("advanced-filters", "### 7. Advanced: Filter by Component Signature", "## Settings Window"),
        ("settings-window", "## Settings Window", None),
    ]
    out: dict[str, str] = {}
    for sec_id, start_tok, end_tok in markers:
        s_idx = readme_text.find(start_tok)
        if s_idx == -1:
            raise ValueError(f"Marker {start_tok!r} not found in ObjectFinderPro README.md")
        e_idx = readme_text.find(end_tok, s_idx) if end_tok else len(readme_text)
        if e_idx == -1:
            raise ValueError(f"End marker {end_tok!r} not found in ObjectFinderPro README.md")
        chunk = readme_text[s_idx:e_idx].strip()
        # Drop duplicate first heading line from sliced chunk since article header provides <h1>
        lines = chunk.splitlines()
        if lines and lines[0].startswith("#"):
            lines = lines[1:]
        # Clean stray leading separator
        while lines and lines[0].strip() in ("", "---"):
            lines.pop(0)
        out[sec_id] = "\n".join(lines).strip()
    return out


def build_ofp_overview_section() -> str:
    query_examples = (
        "comp(BoxCollider).isTrigger:true\n"
        "comp(Light).intensity:>5\n"
        "comp(Rigidbody).mass:>=10\n"
        "memsize:>=5mb\n"
        "tag:Player,Enemy\n"
        'tag:"UI Element"\n'
        "tag:Enemy -layer:Water\n"
        "vehicle -car\n"
        "t:Material\n"
        "script:PlayerController active:true"
    )
    cards = [
        ("Main Window & Search Modes", "#main-window", "Core UI", "Auto Search, Fuzzy Search (typo-tolerant & relevance sorted), Exact Match, and Smart Search modes."),
        ("Smart Search Query Language", "#smart-search", "Syntax", "Filter by component properties (comp(...).prop:value), numeric metrics (polycount, memsize, texwidth, childcount), tags, layers, hyphens, and acronyms."),
        ("5 Search Scopes & Core Filters", "#core-filters", "Filters", "Scope searches across Both, Scene, Project, Unloaded Scene, or In Root GameObject with type, active state, tag, layer, and script filters."),
        ("Component Signature & Find References", "#advanced-filters", "Advanced", "Match exact component signatures on templates or trace every direct reference across Scenes, Prefabs, and ScriptableObjects."),
        ("Custom Filter API (CustomFilterBase)", "#custom-filters", "Extensible", "Inherit ScriptableObject base class CustomFilterBase to write custom rules alongside 35+ included ready-to-use filters with source code."),
        ("Settings, Presets & Folder Scope", "#settings-window", "Config", "Configure default presets, favorite renaming, feature visibility toggles, folder scoping, and full keyboard navigation."),
    ]
    cards_html = "\n".join(
        '<div class="doc-index-card">'
        '<div class="doc-index-card-head">'
        f'<a href="{href}" class="doc-index-card-title">{html.escape(title)}</a>'
        f'<span class="eco-pill-count">{html.escape(badge)}</span>'
        '</div>'
        f'<p class="doc-index-card-desc">{html.escape(desc)}</p>'
        f'<div class="doc-index-chips"><a href="{href}" class="doc-index-chip">Open section</a></div>'
        '</div>'
        for title, href, badge, desc in cards
    )

    return (
        '<section id="overview" class="docs-section" data-doc-title="Object Finder Pro v2.0 Overview">\n'
        '    <article class="doc-article">\n'
        '        <div class="doc-article-head">\n'
        '            <div class="doc-article-meta">\n'
        '                <span class="mono" style="color:var(--accent-text);">Object Finder Pro v2.0</span>\n'
        '                <span>/</span>\n'
        '                <span>Tools &gt; Maharaja Studio &gt; Object Finder Pro</span>\n'
        '                <span class="tag" style="margin-left:auto;">12 sections</span>\n'
        '            </div>\n'
        '            <h1>Object Finder Pro Documentation</h1>\n'
        '        </div>\n'
        '        <p class="doc-lead">Object Finder Pro turns your Unity project into an asynchronous, non-blocking searchable database for Scene GameObjects, Prefabs, ScriptableObjects, unloaded scenes, and assets—complete with real-time streaming results and extensible ScriptableObject filters.</p>\n'
        '        <h2>What\'s New in Version 2.0</h2>\n'
        '        <ul>\n'
        '            <li><strong>Fuzzy Search &amp; Exact Match Modes:</strong> Typo-tolerant, relevance-sorted lookups (e.g. <code>plyr</code> matches <code>Player</code>) alongside strict case-insensitive exact matching.</li>\n'
        '            <li><strong>In Root GameObject Scope:</strong> Confine searches inside a specific GameObject hierarchy—ideal for locating skeleton bones or nested prefab parts.</li>\n'
        '            <li><strong>Dedicated Settings Window:</strong> Configure default startup presets, load-last-preset behavior, history cap, highlight colors, feature visibility, and renameable favorites.</li>\n'
        '            <li><strong>Real-Time Streaming &amp; Keyboard Navigation:</strong> Results stream in live as they are discovered, with keyboard navigation across Folder Selector, Component Selector, and Filter windows.</li>\n'
        '        </ul>\n'
        '        <h2>Smart Search Query Cheat Sheet</h2>\n'
        '        <p>Verified Smart Search queries supported when <strong>Use Smart Search</strong> is enabled:</p>\n'
        + render_code_block(query_examples, "query")
        + '\n        <h2>Documentation Map</h2>\n'
        f'        <div class="doc-index-grid">{cards_html}</div>\n'
        '    </article>\n'
        '</section>\n'
    )


def build_ofp_custom_filters_section() -> str:
    return (
        '<section id="custom-filters" class="docs-section" data-doc-title="Custom Filter API (CustomFilterBase)">\n'
        '    <article class="doc-article">\n'
        '        <div class="doc-article-head">\n'
        '            <div class="doc-article-meta">\n'
        '                <span class="mono" style="color:var(--accent-text);">Extensibility</span>\n'
        '                <span>/</span>\n'
        '                <span>ObjectFinderPro_Description</span>\n'
        '            </div>\n'
        '            <h1>Custom Filter API &amp; Pre-Built Filters</h1>\n'
        '        </div>\n'
        '        <p class="doc-lead">Beyond the built-in query parser, Multi-Component Filter, and Signature Filter, Object Finder Pro provides an extensible ScriptableObject filter API designed for studio pipeline rules and project validation.</p>\n'
        '        <h2>ScriptableObject Filter Architecture</h2>\n'
        '        <ul>\n'
        '            <li><strong>Write Custom Filter Logic:</strong> Create a new C# script inheriting from the <code>CustomFilterBase</code> class to implement custom validation or scene inspection queries.</li>\n'
        '            <li><strong>Reusable Filter Assets:</strong> Because each custom filter is a <code>ScriptableObject</code>, teams can create, configure, and save multiple filter asset instances for recurring checks.</li>\n'
        '            <li><strong>35+ Pre-Built Filters Included:</strong> Ships with over 35 ready-to-use filters with full C# source code serving as practical examples and turnkey diagnostics (such as locating animators without controllers or static GameObjects with rigidbodies).</li>\n'
        '            <li><strong>Toggle Section Visibility:</strong> Show or hide the Custom Filters section inside the main window at any time via <strong>Settings Window &gt; Features Tab</strong>.</li>\n'
        '        </ul>\n'
        '    </article>\n'
        '</section>\n'
    )


def build_object_finder_pro_docs() -> None:
    readme_text = OFP_README.read_text(encoding="utf-8")
    # Clean typo in Folder Selection keyboard shortcut text while preserving accuracy
    readme_text = readme_text.replace("UpArrow/DownArror", "UpArrow / DownArrow")
    readme_text = readme_text.replace("Collaps folder", "Collapse folder")
    # Also note negative hyphen exclusion in Smart Search if helpful while keeping 100% factual
    chunks = split_ofp_readme(readme_text)

    ofp_meta = [
        ("search-filtering", "Search & Filtering", "main-window", "Main Window & Modes", "Main Window: Object Finder Pro"),
        ("search-filtering", "Search & Filtering", "smart-search", "Smart Search Syntax", "Smart Search Query Language"),
        ("search-filtering", "Search & Filtering", "core-filters", "Core Filter Options", "Core Filter Options & Scopes"),
        ("search-filtering", "Search & Filtering", "search-behavior", "Behavior & Performance", "Search Behavior & Performance"),
        ("search-filtering", "Search & Filtering", "results-area", "Results & Filter Bar", "Results Area & Live Filter Bar"),

        ("workflows-scopes", "Workflows & Scopes", "other-controls", "Sorting, Stats & Presets", "Sorting, Performance & Presets"),
        ("workflows-scopes", "Workflows & Scopes", "multi-component-filter", "Multi-Component Filter", "Multi-Component Filter & Selector"),
        ("workflows-scopes", "Workflows & Scopes", "folder-selection", "Folder Selection Window", "Folder Selection Window"),
        ("workflows-scopes", "Workflows & Scopes", "advanced-filters", "Signature & References", "Component Signature & Find References"),

        ("extensibility", "Extensibility & Settings", "custom-filters", "Custom Filter API", "Custom Filter API (CustomFilterBase)"),
        ("extensibility", "Extensibility & Settings", "settings-window", "Settings Window", "Settings Window"),
    ]

    link_map = {"readme.md": "overview"}
    smart_search_extra = {
        "Undo/Redo": (
            '<div class="doc-callout is-info">'
            '<div class="doc-callout-label">' + SVG_ALERT_INFO + '<span>Query Logic Extensions</span></div>'
            '<p>Smart Search also supports hyphen (<code>-</code>) negative exclusion on terms or keywords (for example, <code>tag:Enemy -layer:Water</code> or <code>vehicle -car</code>) alongside comma-separated <code>OR</code> lists such as <code>tag:Player,Enemy</code>.</p>'
            '</div>'
        )
    }

    cat_order: list[tuple[str, str]] = []
    grouped: dict[str, list[tuple[str, str, str]]] = {}
    for ckey, clabel, sec_id, nav_label, full_title in ofp_meta:
        if ckey not in grouped:
            cat_order.append((ckey, clabel))
            grouped[ckey] = []
        grouped[ckey].append((sec_id, nav_label, full_title))

    sidebar_groups_html = []
    for ckey, clabel in cat_order:
        items = grouped[ckey]
        li_html = "".join(f'<li><a href="#{sid}" class="docs-nav-link">{html.escape(nl)}</a></li>' for sid, nl, _ft in items)
        sidebar_groups_html.append(
            '<div class="docs-cat-group">'
            '<button type="button" class="docs-cat-btn" aria-expanded="true">'
            f'<span>{html.escape(clabel)}</span>'
            f'<span style="display:inline-flex;align-items:center;gap:6px;">'
            f'<span class="docs-cat-count">{len(items)}</span>{SVG_CHEVRON}</span>'
            '</button>'
            f'<ul class="docs-nav-menu">{li_html}</ul>'
            '</div>'
        )

    sections_html = [build_ofp_overview_section()]
    for _ck, clabel, sec_id, _nl, full_title in ofp_meta:
        if sec_id == "custom-filters":
            sections_html.append(build_ofp_custom_filters_section())
            continue

        raw_md = chunks[sec_id]
        inject = smart_search_extra if sec_id == "smart-search" else None
        body_html = md_to_html(
            raw_md,
            OFP_README,
            link_map,
            sec_id,
            strip_first_h1=False,
            post_heading_injections=inject,
            omit_lines_containing=("[GIF/Screenshot showing",),
        )
        sections_html.append(
            f'<section id="{sec_id}" class="docs-section" data-doc-title="{html.escape(full_title, quote=True)}">\n'
            '    <article class="doc-article">\n'
            '        <div class="doc-article-head">\n'
            '            <div class="doc-article-meta">\n'
            '                <a href="#overview" class="doc-crumb-link">Object Finder Pro</a>\n'
            '                <span>/</span>\n'
            f'                <span>{html.escape(clabel)}</span>\n'
            '                <span class="mono" style="margin-left:auto;">README.md</span>\n'
            '            </div>\n'
            f'            <h1>{html.escape(full_title)}</h1>\n'
            '        </div>\n'
            f'{body_html}\n'
            '    </article>\n'
            '</section>\n'
        )

    page_html = (
        '<!DOCTYPE html>\n'
        '<html lang="en" data-theme="dark">\n\n'
        '<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '    <title>Object Finder Pro v2.0 — Documentation · Maharaja Studio</title>\n'
        '    <meta name="description" content="Complete guide to Object Finder Pro v2.0: Smart Search query syntax, Fuzzy & Exact modes, 5 search scopes, Multi-Component & Signature filters, Find All References, CustomFilterBase API, and Settings.">\n'
        '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
        '    <link rel="stylesheet" href="css/studio.css">\n'
        '</head>\n\n'
        '<body class="docs-workspace docs-no-subnav">\n'
        + render_nav("object-finder-pro", "object-finder-pro.html", "Asset overview")
        + render_mobile_drawer("Object Finder Pro", [
            ("object-finder-pro.html", "Object Finder Pro Overview"),
            ("#overview", "Docs Hub & Query Sheet"),
            ("#main-window", "Main Window & Modes"),
            ("#smart-search", "Smart Search Syntax"),
            ("#core-filters", "Core Filters & Scopes"),
            ("#advanced-filters", "Signature & References"),
            ("#custom-filters", "Custom Filter API"),
            ("#settings-window", "Settings Window"),
        ])
        + '\n    <main>\n'
        '        <div class="container">\n'
        '            <div class="docs-shell">\n'
        '                <aside class="docs-sidebar" aria-label="Object Finder Pro documentation navigation">\n'
        '                    <div class="docs-sidebar-head">\n'
        '                        <div class="docs-sidebar-title-row">\n'
        '                            <span class="docs-sidebar-title">Object Finder Pro</span>\n'
        '                            <span style="display:inline-flex;align-items:center;gap:8px;">\n'
        '                                <span class="mono" style="font-size: 11px; color: var(--text-muted);">12 guides</span>\n'
        '                                <button type="button" class="docs-sidebar-close" data-doc-sidebar-close aria-label="Close sections drawer">\n'
        '                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>\n'
        '                                </button>\n'
        '                            </span>\n'
        '                        </div>\n'
        '                        <div class="docs-search-wrap">\n'
        '                            <svg class="docs-search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>\n'
        '                            <input type="search" id="doc-search" class="docs-search-input" style="padding-right:12px;" placeholder="Filter sections..." aria-label="Filter Object Finder Pro documentation" autocomplete="off">\n'
        '                        </div>\n'
        '                    </div>\n'
        '                    <div class="docs-sidebar-body">\n'
        '                        <div class="docs-pinned-group">\n'
        '                            <div class="docs-pinned-label">Start Here</div>\n'
        '                            <a href="#overview" class="docs-nav-link"><span>Overview &amp; Query Sheet</span><span class="eco-pill-count">v2.0</span></a>\n'
        '                        </div>\n'
        + "\n".join(sidebar_groups_html)
        + '\n                    </div>\n'
        '                </aside>\n\n'
        '                <div class="docs-main">\n'
        '                    <div class="docs-mobile-toolbar">\n'
        '                        <button type="button" id="doc-sidebar-toggle" class="btn btn-secondary btn-sm" aria-expanded="false">\n'
        '                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="7" y2="7"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="17" y2="17"/></svg>\n'
        '                            Sections (12)\n'
        '                        </button>\n'
        '                        <a class="btn btn-secondary btn-sm" href="object-finder-pro.html">Asset Overview</a>\n'
        '                    </div>\n\n'
        + "\n".join(sections_html)
        + render_pager()
        + '                </div>\n'
        '            </div>\n'
        '        </div>\n'
        '    </main>\n\n'
        + render_footer("object-finder-pro.html", "Object Finder Pro v2.0")
        + '    <script src="js/studio.js"></script>\n'
        '</body>\n\n'
        '</html>\n'
    )

    out_path = WORKSPACE / "object-finder-pro-docs.html"
    out_path.write_text(page_html, encoding="utf-8")
    print(f"Wrote {out_path.relative_to(WORKSPACE)} (12 sections)")


def main() -> int:
    build_msmotion_docs()
    build_object_finder_pro_docs()

    from build_ssp_docs import build_scriptable_studio_pro_docs
    from build_uqi_docs import build_ultimate_quick_inspector_docs
    from build_tactical_docs import build_tactical_ai_docs, build_tactical_ai_whats_new
    from build_hub_docs import build_documentation_hub

    build_scriptable_studio_pro_docs()
    build_ultimate_quick_inspector_docs()
    build_tactical_ai_docs()
    build_tactical_ai_whats_new()
    build_documentation_hub()
    return 0


if __name__ == "__main__":
    sys.exit(main())
