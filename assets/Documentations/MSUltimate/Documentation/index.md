# MSUltimate Documentation Hub

> **The Ultimate AAA Inspector & Tooling Architecture for Unity.**  
> Built for Unity 6 (6000.x)+.

---

## Welcome to MSUltimate
MSUltimate elevates the Unity Inspector from a plain serialization window into a responsive, beautiful, high-efficiency authoring environment. Designed for enterprise production pipelines, MSUltimate delivers zero-boilerplate attributes, dynamic layout groups, scene debug overlays, and deep editor tooling.

👉 **New to the ecosystem?** Read the [**Ecosystem & Edition Comparison Guide**](packages-comparison.md) for a comprehensive breakdown of Community, Pro, and Addon packages.

---

## Modules in this Suite
- **MSUltimate Core** — 156 concrete attributes (161 documented attribute classes including base contracts), custom collection serializers, extended types, and modular windowing framework.
- [**Animated Attributes**](../Addons/MSUltimate-AnimatedAttributes/Documentation/index.md) — 99 concrete reactive visual feedback, VFX, and kinetic motion attributes (101 attribute classes).
- [**Component Designer**](../Addons/MSUltimate-ComponentDesigner/Documentation/index.md) — 74 concrete header cards, themes, and aesthetic styling attributes (75 attribute classes).
- [**Hierarchy Designer**](../Addons/MSUltimate-HierarchyDesigner/Documentation/index.md) — 82 concrete hierarchy enhancement and telemetry attributes (83 attribute classes).
- [**ToolBox Vol. 1**](../Addons/MSUltimate-ToolBox-Vol1/Documentation/index.md) — Advanced Console, History Track, Lifetime Track, and Live Track (+ 4 attributes).
- [**Validation Module**](../Addons/MSUltimate-ValidationModule/Documentation/index.md) — 39 real-time validation attributes and project scan window.
- [**Inspector Customizer**](../Addons/MSUltimate-InspectorCustomizer/Documentation/index.md) — Non-destructive virtual attribute engine, Makeover Graph, AI Decorator, templates/recipes, and AST code baking.

---

## Editor Windows & Tools Directory
Core & Validation windows are under `Tools > Maharaja Studio > MSUltimate > Windows`, while Addon tools use dedicated submenus under `Tools > Maharaja Studio > MSUltimate`:

| Window Name | Menu Path | Module | Purpose |
| :--- | :--- | :--- | :--- |
| **Example & Attribute Explorer** | `Tools > Maharaja Studio > MSUltimate > Windows > Example & Attribute Explorer` | Core | Interactive browser for attribute examples and documentation. |
| **Setup & Compatibility Wizard** | `Tools > Maharaja Studio > MSUltimate > Windows > Setup & Compatibility Wizard` | Core | First-run setup, global integration, custom type baking, and conflict checks. |
| **Inspector Layout Settings** | `Tools > Maharaja Studio > MSUltimate > Windows > Inspector Layout Settings` | Core | Global label layout, responsive breakpoints, and collection defaults in Preferences. |
| **Asset Manager** | `Tools > Maharaja Studio > MSUltimate > Windows > Asset Manager` | Core | Centralized catalog for `[ManageableAsset]` ScriptableObjects. |
| **Scene Debug Overlay** | `Tools > Maharaja Studio > MSUltimate > Windows > Scene Debug Overlay` | Core | Master control panel for scene view gizmo and handle overlays. |
| **Validation Window** | `Tools > Maharaja Studio > MSUltimate > Windows > Validation Window` | Validation | Project-wide batch validation scanner and 1-click auto-fix tools. |
| **Inspector Customizer** | `Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Inspector Customizer` | Customizer | Main non-destructive visual inspector customization workbench. |
| **Makeover Graph Editor** | `Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Makeover Graph Editor` | Customizer | 30-node visual graph editor for compound inspector makeovers. |
| **Template & Recipe Manager** | `Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Template & Recipe Manager` | Customizer | Author and manage reusable makeover templates and recipes. |
| **Component Defaults & Rules** | `Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Component Defaults & Rules` | Customizer | Project-wide default component attributes and granular ignore rules. |
| **Inspector Customizer Settings** | `Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Inspector Customizer Settings` | Customizer | Customizer engine preferences, AI providers, catalog, and baking options. |
| **Advanced Console** | `Tools > Maharaja Studio > MSUltimate > ToolBox Vol 1 > Advanced Console` | ToolBox Vol. 1 | High-throughput structured log analyzer, rules, and runtime console commands. |
| **HistoryTrack Window** | `Tools > Maharaja Studio > MSUltimate > ToolBox Vol 1 > HistoryTrack Window` | ToolBox Vol. 1 | Visual Undo/Redo timeline and variable change diffs (`Play Mode Tweaks` also available). |
| **Object Lifetime Tracker** | `Tools > Maharaja Studio > MSUltimate > ToolBox Vol 1 > Object Lifetime Tracker` | ToolBox Vol. 1 | Allocation tracker, dangling-reference hunter, and scene teardown leak detector. |
| **LiveTrack Dashboard** | `Tools > Maharaja Studio > MSUltimate > ToolBox Vol 1 > LiveTrack Dashboard` | ToolBox Vol. 1 | Real-time variable telemetry HUD and multi-scale oscilloscope graphs. |

---

## Core Attribute Categories
| Category | Attribute Count | Index Link |
| :--- | :---: | :--- |
| **Advanced** | 12 | [Browse Advanced Attributes](attributes/advanced/index.md) |
| **Buttons & Actions** | 7 | [Browse Button Attributes](attributes/buttons/index.md) |
| **Lifecycle & Callbacks** | 11 | [Browse Callback Attributes](attributes/callbacks/index.md) |
| **Collections & Lists** | 3 *(2 concrete + `BaseCollection`)* | [Browse Collection Attributes](attributes/collections/index.md) |
| **Conditionals & Visibility** | 7 | [Browse Conditional Attributes](attributes/conditional/index.md) |
| **Decorators & Banners** | 37 | [Browse Decorator Attributes](attributes/decorators/index.md) |
| **Field Drawers & Sliders** | 37 | [Browse Field Attributes](attributes/fields/index.md) |
| **Groups & Layouts** | 16 | [Browse Group Attributes](attributes/groups-and-layouts/index.md) |
| **Scene Debug & Handles** | 12 | [Browse Scene Debug Attributes](attributes/scene-debug/index.md) |
| **Types & Presets** | 4 | [Browse Type Attributes](attributes/types/index.md) |
| **Validation (Core)** | 8 | [Browse Validation Attributes](attributes/validation/index.md) |
| **Core & Engine Directives** | 4 *(abstract base contracts)* | [Browse Core Directives](attributes/core/index.md) |
| **Windowing & Preferences** | 2 | [Browse Windowing Attributes](attributes/windowing/index.md) |
| **Others** | 1 | [Browse Other Attributes](attributes/others/index.md) |
