#!/usr/bin/env python3
"""
Ultimate Quick Inspector Documentation Builder
Reads markdown source from assets/Documentations/UltimateQuickInspector/Readme.md
and assets/Descriptions/UltimateQuickInspector_Description.txt,
converts them into Graphite+Amber HTML with scoped anchors, copyable code blocks,
tables, and callouts, and writes ultimate-quick-inspector-docs.html.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from build_product_docs import (
    WORKSPACE,
    SVG_CHEVRON,
    SVG_COPY,
    SVG_ALERT_INFO,
    SVG_ALERT_WARN,
    strip_emoji,
    slugify,
    render_nav,
    render_mobile_drawer,
    render_footer,
    render_pager,
    md_to_html,
)

UQI_README = WORKSPACE / "assets" / "Documentations" / "UltimateQuickInspector" / "Readme.md"
UQI_DESC = WORKSPACE / "assets" / "Descriptions" / "UltimateQuickInspector_Description.txt"


def split_uqi_readme(raw_md: str) -> dict[str, str]:
    chunks: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []

    for line in raw_md.splitlines():
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            if current_key:
                chunks[current_key] = "\n".join(current_lines).strip()
            h2 = m.group(1).strip()
            if "Table of Contents" in h2:
                current_key = None
                current_lines = []
                continue
            elif "Feature" in h2:
                current_key = "features"
            elif "How to Use" in h2:
                current_key = "how-to-use"
            elif "Component" in h2:
                current_key = "components"
            elif "Data Storage" in h2:
                current_key = "data-storage"
            elif "Troubleshoot" in h2:
                current_key = "troubleshooting"
            elif "Contact" in h2:
                current_key = "contact"
            elif "Thank" in h2:
                # Append to contact
                pass
            current_lines = [line]
        else:
            if current_key:
                current_lines.append(line)

    if current_key:
        chunks[current_key] = "\n".join(current_lines).strip()

    return chunks


def build_uqi_overview_section() -> str:
    return (
        '<section id="overview" class="docs-section" data-doc-title="Overview & Architecture">\n'
        '    <article class="doc-article">\n'
        '        <div class="doc-article-head">\n'
        '            <div class="doc-article-meta">\n'
        '                <span>Ultimate Quick Inspector</span>\n'
        '                <span>/</span>\n'
        '                <span>Documentation Hub</span>\n'
        '                <span class="mono" style="margin-left:auto;">v1.0 Pro</span>\n'
        '            </div>\n'
        '            <h1>Ultimate Quick Inspector Documentation</h1>\n'
        '        </div>\n\n'
        '        <p class="doc-lead">\n'
        '            A lightweight, zero-overhead Unity Editor extension for pinning, organizing across multi-page tabs, and instantly selecting frequently accessed scene objects, prefabs, materials, and scripts.\n'
        '        </p>\n\n'
        '        <div class="doc-card-grid">\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>Pin Anything</h4>\n'
        '                <p>Pin scene GameObjects (active or disabled), project prefabs, script assets, and materials with one drag-and-drop motion.</p>\n'
        '            </div>\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>Persistent GUID Tracking</h4>\n'
        '                <p>Automatic <code>GuidComponent</code> maintains persistent object identity even after scene reloads, project restarts, or GameObject renames.</p>\n'
        '            </div>\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>Multi-Page Drawer</h4>\n'
        '                <p>Organize items into feature-scoped pages like <em>UI Elements</em>, <em>Player Systems</em>, or <em>Level Design</em> for clean workspaces.</p>\n'
        '            </div>\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>Zero Performance Cost</h4>\n'
        '                <p>Data is stored in a clean <code>QuickInspectorData.asset</code> ScriptableObject. Zero runtime allocations or frame overhead.</p>\n'
        '            </div>\n'
        '        </div>\n\n'
        '        <h3>Quick Start &amp; Access</h3>\n'
        '        <div class="doc-table-wrap">\n'
        '            <table class="doc-table">\n'
        '                <thead>\n'
        '                    <tr><th>Workflow</th><th>Action</th><th>Notes</th></tr>\n'
        '                </thead>\n'
        '                <tbody>\n'
        '                    <tr><td><strong>Open Tool</strong></td><td><span class="mono">Window &gt; Ultimate Quick Inspector</span></td><td>Dock anywhere in your editor layout (next to Inspector or Hierarchy)</td></tr>\n'
        '                    <tr><td><strong>Add Items</strong></td><td>Drag &amp; drop from Project or Hierarchy</td><td>Supports single or multi-selection drop into the active page</td></tr>\n'
        '                    <tr><td><strong>Add Page</strong></td><td>Click <span class="mono">+</span> in page toolbar</td><td>Create unlimited categorized pages</td></tr>\n'
        '                    <tr><td><strong>Rename Page</strong></td><td>Click Settings icon (gear)</td><td>Edit current page name to reflect game subsystem</td></tr>\n'
        '                    <tr><td><strong>Select Item</strong></td><td>Click row or ping icon</td><td>Focuses and pings the object in Hierarchy/Project immediately</td></tr>\n'
        '                    <tr><td><strong>Remove Item</strong></td><td>Click <span class="mono">&times;</span> or &ldquo;Remove All&rdquo;</td><td>Unpins reference without deleting the underlying asset</td></tr>\n'
        '                </tbody>\n'
        '            </table>\n'
        '        </div>\n\n'
        '        <h3>Documentation Chapters</h3>\n'
        '        <div class="doc-table-wrap">\n'
        '            <table class="doc-table">\n'
        '                <thead>\n'
        '                    <tr><th>Chapter</th><th>Category</th><th>Description</th><th>Anchor</th></tr>\n'
        '                </thead>\n'
        '                <tbody>\n'
        '                    <tr><td><strong>Features</strong></td><td>Core Concepts</td><td>Feature overview: drag-and-drop, persistent data, and multi-page drawer</td><td><a href="#features">Read Section &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>How to Use</strong></td><td>Workflow</td><td>Opening window, adding/managing objects, page workflows, and search</td><td><a href="#how-to-use">Read Section &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Components Explained</strong></td><td>Architecture</td><td>Deep dive into <code>GuidComponent</code> and why persistent IDs matter</td><td><a href="#components">Read Section &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Data Storage</strong></td><td>Architecture</td><td><code>QuickInspectorData.asset</code> ScriptableObject and version control practices</td><td><a href="#data-storage">Read Section &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Troubleshooting</strong></td><td>Maintenance</td><td>Cross-scene warnings, missing reference cleanup, and reset options</td><td><a href="#troubleshooting">Read Section &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Support &amp; Contact</strong></td><td>Support</td><td>Customer service email, Discord community, and Asset Store feedback</td><td><a href="#contact">Read Section &rarr;</a></td></tr>\n'
        '                </tbody>\n'
        '            </table>\n'
        '        </div>\n'
        '    </article>\n'
        '</section>\n'
    )


def build_ultimate_quick_inspector_docs() -> None:
    raw_md = UQI_README.read_text(encoding="utf-8")
    chunks = split_uqi_readme(raw_md)

    uqi_meta = [
        ("start", "Getting Started", "features", "Key Features", "Features & Capabilities"),
        ("start", "Getting Started", "how-to-use", "How to Use", "How to Use & Window Layout"),
        ("arch", "Architecture & Data", "components", "Components Explained", "Components: GuidComponent"),
        ("arch", "Architecture & Data", "data-storage", "Data Storage", "Data Storage & ScriptableObject"),
        ("maint", "Support & Maintenance", "troubleshooting", "Troubleshooting", "Troubleshooting & Best Practices"),
        ("maint", "Support & Maintenance", "contact", "Support & Contact", "Customer Support & Contact"),
    ]

    link_map: dict[str, str] = {
        "overview": "overview",
        "features": "features",
        "how-to-use": "how-to-use",
        "components": "components",
        "guidcomponent": "components",
        "data-storage": "data-storage",
        "troubleshooting": "troubleshooting",
        "troubleshooting--best-practices": "troubleshooting",
        "contact": "contact",
    }

    cat_order: list[tuple[str, str]] = []
    grouped: dict[str, list[tuple[str, str, str]]] = {}
    for ckey, clabel, sec_id, nav_label, full_title in uqi_meta:
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

    sections_html = [build_uqi_overview_section()]
    for _ck, clabel, sec_id, _nl, full_title in uqi_meta:
        chunk_md = chunks.get(sec_id, "")
        body_html = md_to_html(chunk_md, UQI_README, link_map, sec_id, strip_first_h1=False)
        sections_html.append(
            f'<section id="{sec_id}" class="docs-section" data-doc-title="{html.escape(full_title, quote=True)}">\n'
            '    <article class="doc-article">\n'
            '        <div class="doc-article-head">\n'
            '            <div class="doc-article-meta">\n'
            '                <a href="#overview" class="doc-crumb-link">Ultimate Quick Inspector</a>\n'
            '                <span>/</span>\n'
            f'                <span>{html.escape(clabel)}</span>\n'
            '                <span class="mono" style="margin-left:auto;">Readme.md</span>\n'
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
        '    <title>Ultimate Quick Inspector — Documentation · Maharaja Studio</title>\n'
        '    <meta name="description" content="Complete documentation for Ultimate Quick Inspector: Pin assets and scene objects, multi-page drawer organization, persistent GUID scene tracking, and data storage.">\n'
        '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
        '    <link rel="stylesheet" href="css/studio.css">\n'
        '</head>\n\n'
        '<body class="docs-workspace docs-no-subnav">\n'
        + render_nav("uqi", "ultimate-quick-inspector.html", "Asset overview")
        + render_mobile_drawer("Ultimate Quick Inspector", [
            ("ultimate-quick-inspector.html", "Ultimate Quick Inspector Overview"),
            ("#overview", "Docs Hub & Quick Start"),
            ("#features", "Key Features"),
            ("#how-to-use", "How to Use & Layout"),
            ("#components", "GuidComponent Architecture"),
            ("#data-storage", "ScriptableObject Storage"),
            ("#troubleshooting", "Troubleshooting"),
            ("#contact", "Support & Contact"),
        ])
        + '\n    <main>\n'
        '        <div class="container">\n'
        '            <div class="docs-shell">\n'
        '                <aside class="docs-sidebar" aria-label="Ultimate Quick Inspector documentation navigation">\n'
        '                    <div class="docs-sidebar-head">\n'
        '                        <div class="docs-sidebar-title-row">\n'
        '                            <span class="docs-sidebar-title">Quick Inspector</span>\n'
        '                            <span style="display:inline-flex;align-items:center;gap:8px;">\n'
        '                                <span class="mono" style="font-size: 11px; color: var(--text-muted);">7 guides</span>\n'
        '                                <button type="button" class="docs-sidebar-close" data-doc-sidebar-close aria-label="Close sections drawer">\n'
        '                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>\n'
        '                                </button>\n'
        '                            </span>\n'
        '                        </div>\n'
        '                        <div class="docs-search-wrap">\n'
        '                            <svg class="docs-search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>\n'
        '                            <input type="search" id="doc-search" class="docs-search-input" style="padding-right:12px;" placeholder="Filter sections..." aria-label="Filter Ultimate Quick Inspector documentation" autocomplete="off">\n'
        '                        </div>\n'
        '                    </div>\n'
        '                    <div class="docs-sidebar-body">\n'
        '                        <div class="docs-pinned-group">\n'
        '                            <div class="docs-pinned-label">Start Here</div>\n'
        '                            <a href="#overview" class="docs-nav-link"><span>Overview &amp; Quick Start</span><span class="eco-pill-count">v1.0</span></a>\n'
        '                        </div>\n'
        + "\n".join(sidebar_groups_html)
        + '\n                    </div>\n'
        '                </aside>\n\n'
        '                <div class="docs-main">\n'
        '                    <div class="docs-mobile-toolbar">\n'
        '                        <button type="button" id="doc-sidebar-toggle" class="btn btn-secondary btn-sm" aria-expanded="false">\n'
        '                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="7" y2="7"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="17" y2="17"/></svg>\n'
        '                            Sections (7)\n'
        '                        </button>\n'
        '                        <a class="btn btn-secondary btn-sm" href="ultimate-quick-inspector.html">Asset Overview</a>\n'
        '                    </div>\n\n'
        + "\n".join(sections_html)
        + render_pager()
        + '                </div>\n'
        '            </div>\n'
        '        </div>\n'
        '    </main>\n\n'
        + render_footer("ultimate-quick-inspector.html", "Ultimate Quick Inspector")
        + '    <script src="js/studio.js"></script>\n'
        '</body>\n\n'
        '</html>\n'
    )

    out_path = WORKSPACE / "ultimate-quick-inspector-docs.html"
    out_path.write_text(page_html, encoding="utf-8")
    print(f"Wrote {out_path.relative_to(WORKSPACE)} (7 sections)")


if __name__ == "__main__":
    build_ultimate_quick_inspector_docs()
