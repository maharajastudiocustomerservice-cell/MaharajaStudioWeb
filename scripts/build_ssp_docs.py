#!/usr/bin/env python3
"""
Scriptable Studio Pro v4.5 Documentation Builder
Reads markdown sources from assets/Documentations/ScriptableStudioPro/,
converts them into Graphite+Amber HTML with scoped anchors, copyable code
blocks, tables, and callouts, and writes scriptable-studio-pro-docs.html.
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

SSP_ROOT = WORKSPACE / "assets" / "Documentations" / "ScriptableStudioPro"


DETAIL_PANEL_MD = """# Detail Panel & Native Drawing Pipeline

Accessible via **Open Details** in the main toolbar, or by double-clicking any instance in the grid. The Detail Panel shows all fields of a single instance in a focused vertical, scrollable layout with real-time property bindings.

## Native Drawing System (v3.0+)

In v3.0+, the Detail Panel uses a **native drawing pipeline** for all field types, bypassing generic string reflection:

1. **Assembly Scan at Startup:** The system scans all loaded project assemblies for `CustomPropertyDrawer` attributes and builds an in-memory type-to-drawer cache.
2. **Type Detection:** When rendering a field, the tool checks whether the field's type is marked as native-drawn. A type qualifies if:
   - It has a custom Unity `PropertyDrawer` registered in any loaded assembly.
   - Its fully-qualified name appears in the **Native Drawn Types** list under General Settings.
   - It is an engine primitive, vector, color, gradient, animation curve, or bounds.
3. **Hardware-Accelerated UI:** Where UI Toolkit drawers are detected, elements are rendered directly via visual element binding; IMGUI drawers fall back safely to a sandboxed GUI clipping scope without layout breaking.

## Prefab & Model Card

When a `GameObject` or Prefab asset is assigned or inspected:
- **Real-Time AssetPreview:** Generates a crisp thumbnail with LOD preview.
- **Component Badges:** Displays attached components with quick-jump links.
- **Spawn in Scene:** Instantiates the prefab at `Vector3.zero` or current scene camera focal point.
- **Embedded Inspector:** Toggle an inline full Unity Inspector for child components directly inside the panel.

## Toolbar Controls

| Control | Action | Shortcut |
|:---|:---|:---|
| **Search Filter** | Filters visible fields by name or property path | `Ctrl+F` |
| **Prev / Next** | Switches active instance without closing drawer | `[` / `]` |
| **Undo / Redo** | Full multi-step undo stack targeting only this asset | `Ctrl+Z` / `Ctrl+Y` |
| **Dock Placement** | Switch between Right Dock (default) and Bottom Dock | Settings |
"""

CREATE_EDIT_MODES_MD = """# Create Mode vs. Edit Mode & Prefab Overrides

Scriptable Studio Pro offers two distinct operating modes designed to separate rapid draft generation from live project asset maintenance.

## Mode Comparison

| Capability | Create Mode | Edit Mode |
|:---|:---|:---|
| **Target Purpose** | Rapid generation of *new* ScriptableObjects or Prefab variants | Batch editing existing project assets on disk |
| **Memory State** | In-memory draft instances; no disk writes until confirmed | Directly bound to assets on disk; auto-saves or manual flush |
| **Save Action** | Click **Create Assets** to write `.asset` files to target folder | Click **Update Linked Assets** or press `Ctrl+S` |
| **Naming Engine** | Evaluates Naming Patterns (e.g. `{TYPE}_{ii}`, `{NAME}_{ID:000}`) | Retains existing file names; rename via F2 or batch renamer |
| **Drag & Drop** | Dropping files sets reference properties or loads archetype templates | Dropping files imports them directly into the current grid |
| **Count Selector** | Set initial batch size (e.g. create 50 item configs at once) | Grid row count matches imported file count |

## Prefab Studio Pro Mode (New in v4.0)

When targeting Prefab components instead of ScriptableObjects:
- **Delta-Safe Property Overrides:** Modifying values records standard Unity Prefab property modifications without breaking inheritance or dirtying unchanged fields.
- **Variant Creation:** In Create Mode, generating from a Prefab creates clean **Prefab Variants** parented to the source asset.
- **Component Filtering:** Filter by component type (e.g. `CharacterStats`, `WeaponData`, `AudioEmitter`) across hundreds of nested prefabs in a single unified table.

> [!NOTE]
> Create Mode never touches your disk until you click **Create Assets**. If you close the window with unsaved drafts, Scriptable Studio Pro prompts you to preserve or discard the temporary session cache.
"""


def build_ssp_overview_section() -> str:
    return (
        '<section id="overview" class="docs-section" data-doc-title="Overview & Architecture">\n'
        '    <article class="doc-article">\n'
        '        <div class="doc-article-head">\n'
        '            <div class="doc-article-meta">\n'
        '                <span>Scriptable Studio Pro</span>\n'
        '                <span>/</span>\n'
        '                <span>Documentation Hub</span>\n'
        '                <span class="mono" style="margin-left:auto;">v4.5 Enterprise</span>\n'
        '            </div>\n'
        '            <h1>Scriptable Studio Pro v4.5 Documentation</h1>\n'
        '        </div>\n\n'
        '        <p class="doc-lead">\n'
        '            High-speed bulk data editing for Unity: manipulate hundreds of ScriptableObjects and Prefab components in an Excel-grade grid with formulas, native property drawers, machine translation, grammar validation, and bidirectional CSV/JSON/SQL sync.\n'
        '        </p>\n\n'
        '        <div class="doc-card-grid">\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>Bulk Data Grid</h4>\n'
        '                <p>Virtual row rendering handles 10,000+ objects without UI stutter. Multi-column sorting, frozen columns, and column reordering.</p>\n'
        '            </div>\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>Prefab Studio Pro</h4>\n'
        '                <p>Inspect and edit component fields across prefabs and models. Delta-safe overrides preserve prefab variant inheritance.</p>\n'
        '            </div>\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>Formula Engine</h4>\n'
        '                <p>Run mathematical operations across columns with syntax like <code>=[BaseHP] * 1.15 + 20</code>, alias variables, and batch mutations.</p>\n'
        '            </div>\n'
        '            <div class="doc-mini-card">\n'
        '                <h4>AI &amp; Localization (v4.5)</h4>\n'
        '                <p>DeepL, Google, Azure, and LibreTranslate integration paired with local Docker LanguageTool for zero-cost offline grammar checks.</p>\n'
        '            </div>\n'
        '        </div>\n\n'
        '        <h3>Essential Shortcuts &amp; Operations</h3>\n'
        '        <div class="doc-table-wrap">\n'
        '            <table class="doc-table">\n'
        '                <thead>\n'
        '                    <tr><th>Action</th><th>Shortcut</th><th>Context</th><th>Description</th></tr>\n'
        '                </thead>\n'
        '                <tbody>\n'
        '                    <tr><td><strong>Open Grid Editor</strong></td><td><span class="kbd">Ctrl+M</span> / <span class="kbd">Cmd+M</span></td><td>Editor Global</td><td>Opens Scriptable Studio Pro main grid window</td></tr>\n'
        '                    <tr><td><strong>Edit Cell</strong></td><td><span class="kbd">F2</span> or Double Click</td><td>Grid Cell</td><td>Enters inline edit mode for strings, numbers, or enum dropdowns</td></tr>\n'
        '                    <tr><td><strong>Commit &amp; Next</strong></td><td><span class="kbd">Enter</span> / <span class="kbd">Tab</span></td><td>Inline Cell</td><td>Commits current cell value and moves to the next row/column</td></tr>\n'
        '                    <tr><td><strong>Open Detail Panel</strong></td><td><span class="kbd">Space</span> or Toolbar</td><td>Row Selection</td><td>Opens focused inspector panel with native property drawers</td></tr>\n'
        '                    <tr><td><strong>Save Linked Assets</strong></td><td><span class="kbd">Ctrl+S</span> / <span class="kbd">Cmd+S</span></td><td>Grid Focus</td><td>Flushes all modified in-memory records to disk asset files</td></tr>\n'
        '                    <tr><td><strong>Formula Mode</strong></td><td>Type <code>=</code> in Cell</td><td>Numeric Cell</td><td>Initiates cross-column formula evaluation for selected row</td></tr>\n'
        '                </tbody>\n'
        '            </table>\n'
        '        </div>\n\n'
        '        <h3>Complete Documentation Chapters</h3>\n'
        '        <div class="doc-table-wrap">\n'
        '            <table class="doc-table">\n'
        '                <thead>\n'
        '                    <tr><th>Section</th><th>Category</th><th>Scope</th><th>Link</th></tr>\n'
        '                </thead>\n'
        '                <tbody>\n'
        '                    <tr><td><strong>Introduction</strong></td><td>Getting Started</td><td>Architectural overview, v4.5 features, and requirements</td><td><a href="#introduction">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Getting Started</strong></td><td>Getting Started</td><td>Installation, first workflow walkthrough, opening windows</td><td><a href="#getting-started">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Configuration</strong></td><td>Getting Started</td><td>General settings, folder rules, naming patterns, import/export</td><td><a href="#configuration">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>User Interface</strong></td><td>Core Editing</td><td>Main toolbar, left sidebar, center grid, detail panel, status bar</td><td><a href="#user-interface">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Core Workflow</strong></td><td>Core Editing</td><td>Grid editing, sorting, filtering, and Prefab Studio workflows</td><td><a href="#core-workflow">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Detail Panel</strong></td><td>Core Editing</td><td>Native Drawing System (v3.0), property drawers, model cards</td><td><a href="#detail-panel">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Create vs. Edit Mode</strong></td><td>Core Editing</td><td>In-memory generation, naming templates, delta-safe overrides</td><td><a href="#create-edit-modes">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Power Features</strong></td><td>Power &amp; AI</td><td>Formula syntax, aliases, formula mode, batch transformations</td><td><a href="#power-features">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>AI Asset Architect</strong></td><td>Power &amp; AI</td><td>Prompt-based ScriptableObject creation with OpenAI &amp; Gemini</td><td><a href="#ai-asset-architect">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Grammar Checking</strong></td><td>Localization</td><td>Quality assurance scanning, spelling correction, review pane</td><td><a href="#grammar-checking">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Grammar Providers</strong></td><td>Localization</td><td>Local Docker LanguageTool setup (free, offline) and cloud APIs</td><td><a href="#setup-grammar-providers">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>Machine Translation</strong></td><td>Localization</td><td>Automated batch translation across Unity Localization tables</td><td><a href="#machine-translation">Read Guide &rarr;</a></td></tr>\n'
        '                    <tr><td><strong>MT Providers Setup</strong></td><td>Localization</td><td>DeepL, Google Cloud V2, Azure Translator, and LibreTranslate</td><td><a href="#setup-mt-providers">Read Guide &rarr;</a></td></tr>\n'
        '                </tbody>\n'
        '            </table>\n'
        '        </div>\n'
        '    </article>\n'
        '</section>\n'
    )


def build_scriptable_studio_pro_docs() -> None:
    ssp_meta = [
        ("start", "Getting Started", "introduction", "Introduction", "Introduction & Architecture", "Introduction.md"),
        ("start", "Getting Started", "getting-started", "Getting Started", "Installation & First Workflow", "Getting-Started.md"),
        ("start", "Getting Started", "configuration", "Configuration", "Configuration & Patterns", "Configuration.md"),
        ("core", "Core Editing & UI", "user-interface", "User Interface", "User Interface Reference", "UserInterface.md"),
        ("core", "Core Editing & UI", "core-workflow", "Core Workflow", "Core Workflow & Prefabs", "Core-Workflow.md"),
        ("core", "Core Editing & UI", "detail-panel", "Detail Panel", "Detail Panel & Native Drawers", None),
        ("core", "Core Editing & UI", "create-edit-modes", "Create vs. Edit Mode", "Create vs. Edit Mode", None),
        ("power", "Power Tools & Formulas", "power-features", "Power Features", "Formulas & Search Aliases", "Power-Features.md"),
        ("power", "Power Tools & Formulas", "ai-asset-architect", "AI Asset Architect", "AI Asset Architect", "AI-System.md"),
        ("ai", "Localization & AI Setup", "grammar-checking", "Grammar Checking", "Grammar Checking (v4.5)", "grammar-checking.md"),
        ("ai", "Localization & AI Setup", "setup-grammar-providers", "Grammar Providers", "Grammar Providers (Docker & Cloud)", "SetupGuide/setup-grammar-providers.md"),
        ("ai", "Localization & AI Setup", "machine-translation", "Machine Translation", "Machine Translation Engine (v4.5)", "machine-translation.md"),
        ("ai", "Localization & AI Setup", "setup-mt-providers", "MT Providers Setup", "MT Providers (DeepL, Google, Azure)", "SetupGuide/setup-mt-providers.md"),
    ]

    link_map: dict[str, str] = {
        "overview": "overview",
        "detail-panel": "detail-panel",
        "create-edit-modes": "create-edit-modes",
    }
    for _ck, _cl, sec_id, _nl, _ft, rel_md in ssp_meta:
        if rel_md:
            link_map[rel_md.lower()] = sec_id
            link_map[Path(rel_md).name.lower()] = sec_id
            link_map[sec_id] = sec_id

    cat_order: list[tuple[str, str]] = []
    grouped: dict[str, list[tuple[str, str, str]]] = {}
    for ckey, clabel, sec_id, nav_label, full_title, _rm in ssp_meta:
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

    sections_html = [build_ssp_overview_section()]
    for _ck, clabel, sec_id, _nl, full_title, rel_md in ssp_meta:
        if sec_id == "detail-panel":
            raw_md = DETAIL_PANEL_MD
            src_file = SSP_ROOT / "UserInterface.md"
        elif sec_id == "create-edit-modes":
            raw_md = CREATE_EDIT_MODES_MD
            src_file = SSP_ROOT / "UserInterface.md"
        else:
            src_file = SSP_ROOT / rel_md
            raw_md = src_file.read_text(encoding="utf-8")

        body_html = md_to_html(raw_md, src_file, link_map, sec_id, strip_first_h1=False)
        sections_html.append(
            f'<section id="{sec_id}" class="docs-section" data-doc-title="{html.escape(full_title, quote=True)}">\n'
            '    <article class="doc-article">\n'
            '        <div class="doc-article-head">\n'
            '            <div class="doc-article-meta">\n'
            '                <a href="#overview" class="doc-crumb-link">Scriptable Studio Pro</a>\n'
            '                <span>/</span>\n'
            f'                <span>{html.escape(clabel)}</span>\n'
            f'                <span class="mono" style="margin-left:auto;">{html.escape(Path(rel_md or "UserInterface.md").name)}</span>\n'
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
        '    <title>Scriptable Studio Pro v4.5 — Documentation · Maharaja Studio</title>\n'
        '    <meta name="description" content="Complete documentation for Scriptable Studio Pro v4.5: Bulk grid editor, Prefab Studio Pro, native property drawers, formula engine, machine translation, and grammar checking.">\n'
        '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
        '    <link rel="stylesheet" href="css/studio.css">\n'
        '</head>\n\n'
        '<body class="docs-workspace docs-no-subnav">\n'
        + render_nav("scriptable-studio-pro", "scriptable-studio-pro.html", "Asset overview")
        + render_mobile_drawer("Scriptable Studio Pro", [
            ("scriptable-studio-pro.html", "Scriptable Studio Pro Overview"),
            ("#overview", "Docs Hub & Shortcuts"),
            ("#getting-started", "Installation & Workflow"),
            ("#core-workflow", "Grid & Prefab Studio"),
            ("#detail-panel", "Native Drawing System"),
            ("#create-edit-modes", "Create vs. Edit Modes"),
            ("#power-features", "Formula Engine"),
            ("#ai-asset-architect", "AI Asset Architect"),
            ("#grammar-checking", "Grammar Checking"),
            ("#machine-translation", "Machine Translation"),
        ])
        + '\n    <main>\n'
        '        <div class="container">\n'
        '            <div class="docs-shell">\n'
        '                <aside class="docs-sidebar" aria-label="Scriptable Studio Pro documentation navigation">\n'
        '                    <div class="docs-sidebar-head">\n'
        '                        <div class="docs-sidebar-title-row">\n'
        '                            <span class="docs-sidebar-title">Scriptable Studio Pro</span>\n'
        '                            <span style="display:inline-flex;align-items:center;gap:8px;">\n'
        '                                <span class="mono" style="font-size: 11px; color: var(--text-muted);">14 guides</span>\n'
        '                                <button type="button" class="docs-sidebar-close" data-doc-sidebar-close aria-label="Close sections drawer">\n'
        '                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>\n'
        '                                </button>\n'
        '                            </span>\n'
        '                        </div>\n'
        '                        <div class="docs-search-wrap">\n'
        '                            <svg class="docs-search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>\n'
        '                            <input type="search" id="doc-search" class="docs-search-input" style="padding-right:12px;" placeholder="Filter sections..." aria-label="Filter Scriptable Studio Pro documentation" autocomplete="off">\n'
        '                        </div>\n'
        '                    </div>\n'
        '                    <div class="docs-sidebar-body">\n'
        '                        <div class="docs-pinned-group">\n'
        '                            <div class="docs-pinned-label">Start Here</div>\n'
        '                            <a href="#overview" class="docs-nav-link"><span>Overview &amp; Shortcuts</span><span class="eco-pill-count">v4.5</span></a>\n'
        '                        </div>\n'
        + "\n".join(sidebar_groups_html)
        + '\n                    </div>\n'
        '                </aside>\n\n'
        '                <div class="docs-main">\n'
        '                    <div class="docs-mobile-toolbar">\n'
        '                        <button type="button" id="doc-sidebar-toggle" class="btn btn-secondary btn-sm" aria-expanded="false">\n'
        '                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="7" y2="7"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="17" y2="17"/></svg>\n'
        '                            Sections (14)\n'
        '                        </button>\n'
        '                        <a class="btn btn-secondary btn-sm" href="scriptable-studio-pro.html">Asset Overview</a>\n'
        '                    </div>\n\n'
        + "\n".join(sections_html)
        + render_pager()
        + '                </div>\n'
        '            </div>\n'
        '        </div>\n'
        '    </main>\n\n'
        + render_footer("scriptable-studio-pro.html", "Scriptable Studio Pro v4.5")
        + '    <script src="js/studio.js"></script>\n'
        '</body>\n\n'
        '</html>\n'
    )

    out_path = WORKSPACE / "scriptable-studio-pro-docs.html"
    out_path.write_text(page_html, encoding="utf-8")
    print(f"Wrote {out_path.relative_to(WORKSPACE)} (14 sections)")


if __name__ == "__main__":
    build_scriptable_studio_pro_docs()

