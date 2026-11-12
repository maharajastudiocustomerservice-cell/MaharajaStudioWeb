#!/usr/bin/env python3
"""
Documentation Hub Builder (documentation.html)
Generates the central documentation directory portal in the Graphite+Amber
design system with real-time search filtering across all 6 asset packages.
"""

from __future__ import annotations

import html
from pathlib import Path

from build_product_docs import (
    WORKSPACE,
    render_nav,
    render_mobile_drawer,
    render_footer,
)


def build_documentation_hub() -> None:
    cards = [
        {
            "id": "msultimate",
            "title": "MSUltimate Ecosystem",
            "badge": "Ecosystem · 454+ Attributes",
            "badge_cls": "badge-amber",
            "img": "assets/Images/MSUltimate_Logo.png",
            "docs_href": "msultimate-docs.html",
            "asset_href": "msultimate.html",
            "license_href": "msultimate-license.html",
            "summary": "Enterprise-grade Unity 6+ editor enhancement suite. Decorate fields with kinetic animations, transform inspector panels with node-based makeovers, validate scene constraints, and curate hierarchy structures.",
            "guides_count": "454+ Guides",
            "modules": ["Community & Pro Core", "Animated Attributes", "Component Designer", "Hierarchy Designer", "Validation Module", "Inspector Customizer", "ToolBox Vol. 1", "License & EULA"],
            "keywords": "msultimate attributes editor ui styling inspector hierarchy validation customizer toolbox license eula community pro",
        },
        {
            "id": "ms-motion",
            "title": "MSMotion v2.0",
            "badge": "v2.0 · Multi-Actor & FX",
            "badge_cls": "badge-amber",
            "img": "assets/Images/MSMotion_Logo.png",
            "docs_href": "ms-motion-docs.html",
            "asset_href": "ms-motion.html",
            "summary": "Multi-actor interaction choreography and animation engine. Orchestrate synchronized combat moves, dynamic summons, motion warping, 8 FX event channels, and zero-allocation PlayableGraph blending.",
            "guides_count": "51 Guides",
            "modules": ["Animation Editor (10)", "Composition Editor (26)", "Runtime Framework (10)", "Troubleshooting (4)"],
            "keywords": "msmotion motion animation choreography fx visual effects dynamic summons playablegraph warping",
        },
        {
            "id": "tactical",
            "title": "Tactical Cover & Retreat AI",
            "badge": "v3.0 · Spatial AI & Squads",
            "badge_cls": "badge-amber",
            "img": "assets/Images/Tactical_Cover_&_Retreat_AI_System_Logo.png",
            "docs_href": "tactical-cover-retreat-ai-system-docs.html",
            "asset_href": "tactical-cover-retreat-ai-system.html",
            "summary": "Enterprise spatial intelligence framework. Pair high-performance Burst cover evaluation with combat locomotion, synchronized squad choreography, real-time ballistic suppression, and automated scene validation.",
            "guides_count": "99 Guides",
            "modules": ["Environmental Helpers (8)", "Spatial Providers (21)", "Tactical Scorers (47)", "API Reference (3)", "Use Cases (3)", "What's New & Upgrades (6)"],
            "keywords": "tactical cover retreat ai combat squads burst suppression providers scorers navigation",
        },
        {
            "id": "ssp",
            "title": "Scriptable Studio Pro",
            "badge": "v4.5 · Bulk Grid & Prefabs",
            "badge_cls": "badge-amber",
            "img": "assets/Images/ScriptableStudioPro_Logo.png",
            "docs_href": "scriptable-studio-pro-docs.html",
            "asset_href": "scriptable-studio-pro.html",
            "summary": "Excel-grade bulk data grid editor. Rapidly edit thousands of ScriptableObjects and Prefab components with formula expressions, native property drawers, AI Asset Architect, and offline Docker grammar checking.",
            "guides_count": "14 Guides",
            "modules": ["Bulk Data Grid", "Prefab Studio Pro", "Formula Engine", "Native Drawers", "AI Architect", "MT & Grammar"],
            "keywords": "scriptable studio pro grid editor prefab bulk excel formula localization translation grammar ai",
        },
        {
            "id": "ofp",
            "title": "Object Finder Pro",
            "badge": "v2.0 · Multithreaded Search",
            "badge_cls": "badge-amber",
            "img": "assets/Images/ObjectFinderPro_Logo.png",
            "docs_href": "object-finder-pro-docs.html",
            "asset_href": "object-finder-pro.html",
            "summary": "Lightning-fast project and scene query engine. Features Smart Search query language (t:, m:, p:, b:), 5 search scopes, multi-component filters, component signature queries, and extensible CustomFilterBase API.",
            "guides_count": "12 Guides",
            "modules": ["Smart Search Query Syntax", "Core & Advanced Filters", "5 Search Scopes", "Find All References", "CustomFilterBase API"],
            "keywords": "object finder pro search query smart search filter references scenes assets hierarchy",
        },
        {
            "id": "uqi",
            "title": "Ultimate Quick Inspector",
            "badge": "v1.0 Pro · GUID Pin Drawer",
            "badge_cls": "badge-amber",
            "img": "assets/Images/UltimateQuickInspector_Logo.png",
            "docs_href": "ultimate-quick-inspector-docs.html",
            "asset_href": "ultimate-quick-inspector.html",
            "summary": "Lightweight productivity extension for pinning and grouping frequently accessed assets and scene objects across customizable pages with persistent GUID scene tracking and zero runtime overhead.",
            "guides_count": "7 Guides",
            "modules": ["Drag & Drop Simplicity", "Multi-Page Organization", "GuidComponent Tracking", "ScriptableObject Storage"],
            "keywords": "ultimate quick inspector pin drawer guid persistent scene objects hierarchy favorites",
        },
    ]

    cards_html = []
    for c in cards:
        tags_html = " ".join(f'<span class="mono" style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: var(--bg-deep); border: 1px solid var(--hairline); color: var(--text-secondary);">{html.escape(m)}</span>' for m in c["modules"])
        extra_btn = f'\n                    <a href="{c["license_href"]}" class="btn btn-secondary btn-sm" style="color: var(--text-secondary);">License &amp; EULA</a>' if c.get("license_href") else ''
        cards_html.append(
            f'            <div class="card asset-card" data-hub-card="{html.escape(c["keywords"])}" style="display: flex; flex-direction: column; background: var(--bg-card); border: 1px solid var(--hairline); border-radius: var(--radius-lg); padding: 24px; transition: border-color 140ms ease, transform 140ms ease;">\n'
            f'                <div style="display: flex; align-items: flex-start; gap: 16px; margin-bottom: 16px;">\n'
            f'                    <img src="{c["img"]}" alt="{html.escape(c["title"])}" style="width: 52px; height: 52px; border-radius: var(--radius-md); object-fit: contain; background: var(--bg-deep); border: 1px solid var(--hairline); padding: 4px;">\n'
            f'                    <div style="flex: 1; min-width: 0;">\n'
            f'                        <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 4px; flex-wrap: wrap;">\n'
            f'                            <h3 style="margin: 0; font-size: 18px; font-weight: 600; color: var(--text-primary);">{html.escape(c["title"])}</h3>\n'
            f'                            <span class="mono" style="font-size: 11px; padding: 2px 8px; border-radius: 999px; background: var(--accent-soft); border: 1px solid var(--accent-line); color: var(--accent-text); font-weight: 500;">{html.escape(c["badge"])}</span>\n'
            f'                        </div>\n'
            f'                        <span class="mono" style="font-size: 12px; color: var(--text-muted);">{html.escape(c["guides_count"])}</span>\n'
            f'                    </div>\n'
            f'                </div>\n\n'
            f'                <p style="font-size: 14px; line-height: 1.55; color: var(--text-secondary); margin-bottom: 20px; flex: 1;">\n'
            f'                    {html.escape(c["summary"])}\n'
            f'                </p>\n\n'
            f'                <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 24px;">\n'
            f'                    {tags_html}\n'
            f'                </div>\n\n'
            f'                <div style="display: flex; align-items: center; gap: 12px; margin-top: auto; padding-top: 16px; border-top: 1px solid var(--hairline-strong); flex-wrap: wrap;">\n'
            f'                    <a href="{c["docs_href"]}" class="btn btn-primary btn-sm" style="flex: 1; min-width: 140px; text-align: center;">Explore Docs &rarr;</a>\n'
            f'                    <a href="{c["asset_href"]}" class="btn btn-secondary btn-sm">Asset Page</a>{extra_btn}\n'
            f'                </div>\n'
            f'            </div>'
        )

    page_html = (
        '<!DOCTYPE html>\n'
        '<html lang="en" data-theme="dark">\n\n'
        '<head>\n'
        '    <meta charset="UTF-8">\n'
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '    <title>Documentation Hub — Maharaja Studio</title>\n'
        '    <meta name="description" content="Central documentation portal for Maharaja Studio Unity assets: MSUltimate Ecosystem, MSMotion v2.0, Tactical AI v3.0, Scriptable Studio Pro, Object Finder Pro, and Ultimate Quick Inspector.">\n'
        '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
        '    <link rel="stylesheet" href="css/studio.css">\n'
        '</head>\n\n'
        '<body>\n'
        + render_nav("documentation", "index.html", "Studio Home")
        + render_mobile_drawer("Documentation Hub", [
            ("index.html", "Home"),
            ("msultimate-docs.html", "MSUltimate Ecosystem (454+)"),
            ("msultimate-license.html", "MSUltimate License & EULA"),
            ("ms-motion-docs.html", "MSMotion v2.0 (51)"),
            ("tactical-cover-retreat-ai-system-docs.html", "Tactical Cover & Retreat AI (99)"),
            ("scriptable-studio-pro-docs.html", "Scriptable Studio Pro (14)"),
            ("object-finder-pro-docs.html", "Object Finder Pro (12)"),
            ("ultimate-quick-inspector-docs.html", "Ultimate Quick Inspector (7)"),
        ])
        + '\n    <header class="hero">\n'
        '        <canvas class="hero-canvas" data-glyph-mode="grid" aria-hidden="true"></canvas>\n'
        '        <div class="container text-center" style="position: relative; z-index: 1;">\n'
        '            <div class="hero-breadcrumb" style="justify-content: center; margin-bottom: 12px;">\n'
        '                <a href="index.html">Home</a>\n'
        '                <span>/</span>\n'
        '                <span class="mono" style="color: var(--accent-text);">Documentation Portal</span>\n'
        '            </div>\n'
        '            <h1 style="font-size: clamp(32px, 5vw, 48px); margin-bottom: 16px;">Maharaja Studio Documentation</h1>\n'
        '            <p class="hero-sub" style="max-width: 720px; margin: 0 auto 28px;">\n'
        '                Official architecture guides, API references, cookbooks, and workflow manuals for the Maharaja Studio Unity product suite.\n'
        '            </p>\n'
        '            <div class="hub-search-box" style="margin: 0 auto; max-width: 600px;">\n'
        '                <svg style="position: absolute; left: 16px; top: 50%; transform: translateY(-50%); color: var(--text-muted);" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>\n'
        '                <input type="search" id="doc-hub-search" class="hub-search-input" placeholder="Filter documentation by package, keyword, or feature..." aria-label="Filter documentation packages" autocomplete="off">\n'
        '            </div>\n'
        '        </div>\n'
        '    </header>\n\n'
        '    <main class="page-content" style="padding: 60px 0 100px;">\n'
        '        <div class="container">\n'
        '            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 32px; flex-wrap: wrap; gap: 16px;">\n'
        '                <div>\n'
        '                    <h2 style="font-size: 22px; font-weight: 600; margin: 0 0 4px; color: var(--text-primary);">Unity Packages &amp; Toolkits</h2>\n'
        '                    <span class="mono" style="font-size: 13px; color: var(--text-muted);">6 Active Products &middot; 640+ Authored Guides</span>\n'
        '                </div>\n'
        '                <div class="mono" style="font-size: 12px; color: var(--text-secondary); background: var(--bg-card); padding: 6px 14px; border-radius: var(--radius-sm); border: 1px solid var(--hairline);">\n'
        '                    Unity 2021.3 LTS through Unity 6+\n'
        '                </div>\n'
        '            </div>\n\n'
        '            <div id="hub-cards-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 24px;">\n'
        + "\n".join(cards_html)
        + '\n            </div>\n\n'
        '            <div id="hub-empty-state" style="display: none; text-align: center; padding: 60px 20px; background: var(--bg-card); border: 1px dashed var(--hairline-strong); border-radius: var(--radius-lg); margin-top: 24px;">\n'
        '                <h3 style="margin-bottom: 8px; font-size: 18px; color: var(--text-primary);">No documentation matching your filter</h3>\n'
        '                <p style="color: var(--text-secondary); font-size: 14px; margin-bottom: 16px;">Try searching for generic terms like &ldquo;attributes&rdquo;, &ldquo;motion&rdquo;, &ldquo;squad&rdquo;, &ldquo;grid&rdquo;, or &ldquo;search&rdquo;.</p>\n'
        '                <button type="button" class="btn btn-secondary btn-sm" id="hub-reset-btn">Reset Search Filter</button>\n'
        '            </div>\n'
        '        </div>\n'
        '    </main>\n\n'
        + render_footer("index.html", "Studio Overview")
        + '    <script src="js/studio.js"></script>\n'
        '    <script>\n'
        '    (function() {\n'
        '        const searchInput = document.getElementById("doc-hub-search");\n'
        '        const cards = document.querySelectorAll("[data-hub-card]");\n'
        '        const emptyState = document.getElementById("hub-empty-state");\n'
        '        const resetBtn = document.getElementById("hub-reset-btn");\n\n'
        '        if (!searchInput) return;\n\n'
        '        function filter() {\n'
        '            const q = searchInput.value.trim().toLowerCase();\n'
        '            let visible = 0;\n'
        '            cards.forEach(card => {\n'
        '                const hay = (card.getAttribute("data-hub-card") + " " + card.textContent).toLowerCase();\n'
        '                const match = !q || hay.includes(q);\n'
        '                card.style.display = match ? "flex" : "none";\n'
        '                if (match) visible++;\n'
        '            });\n'
        '            if (emptyState) emptyState.style.display = visible === 0 ? "block" : "none";\n'
        '        }\n\n'
        '        searchInput.addEventListener("input", filter);\n'
        '        if (resetBtn) {\n'
        '            resetBtn.addEventListener("click", () => {\n'
        '                searchInput.value = "";\n'
        '                filter();\n'
        '                searchInput.focus();\n'
        '            });\n'
        '        }\n'
        '    })();\n'
        '    </script>\n'
        '</body>\n\n'
        '</html>\n'
    )

    out_path = WORKSPACE / "documentation.html"
    out_path.write_text(page_html, encoding="utf-8")
    print(f"Wrote {out_path.relative_to(WORKSPACE)}")


if __name__ == "__main__":
    build_documentation_hub()

