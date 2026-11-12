# Template & Recipe Manager Overview

> **Module:** MSUltimate Inspector Customizer — Templates & Recipes  
> **Topic:** Managing, Authoring, and Testing Templates and Recipes

---

## 1. What Are Templates & Recipes?

- **Inspector Template (`InspectorTemplate`):** A project asset containing an ordered list of pattern-matching rules and visual graph pipelines. When applied to a component, the template evaluates every field and method, styling matched members automatically.
- **Attribute Recipe (`InspectorAttributeRecipe`):** A reusable compound bundle of multiple attributes with pre-configured parameters and dynamic string tokens (e.g. `{Name}`, `{Type}`). Recipes can be stamped onto any field via the Customizer, Makeover Graph, or Context Menu.

The **Template & Recipe Manager** (`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Template & Recipe Manager`) provides a unified workspace for managing these assets.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Template & Recipe Manager                                [ Templates ]  [ Recipes ]   │
├──────────────────────┬─────────────────────────────────────────────────────────────────┤
│  🔍 Search assets... │  Inspector Template: RPG Character & Combat                     │
│  ─────────────────── │  Category: RPG | Icon: ⚔️                                        │
│  TEMPLATES (14)      │  ─────────────────────────────────────────────────────────────  │
│  • Clean & Modern    │  Intelligent Makeover Passes:                                   │
│  • RPG Character ◄── │  [✓] Relational Companion Pairing   [✓] Dynamic Companion Bind  │
│  • Sci-Fi Ballistics │  [✓] Progressive Toggle Cascades    [✓] Action Toolbar Synthesis│
│  • Vehicle Physics   │  ─────────────────────────────────────────────────────────────  │
│  • Procedural Biome  │  Declarative Rules (15 rules):                                  │
│  • Audio Director    │  1. Match: *health* (Numeric) -> Apply: [ProgressBar]           │
│  • AI Agent          │  2. Match: min*, max* (Numeric) -> Pair in: [HorizontalGroup]   │
│  • UI View Layout    │  3. GroupPath: Combat/Vitals -> Hierarchical Tab + Box Container│
│  • Game Dashboard    │  ─────────────────────────────────────────────────────────────  │
│  • Multi-Tab Pro     │  [ Open in Makeover Graph ]   [ Duplicate ]   [ Test on Script ]│
│  ─────────────────── │                                                                 │
│  [ + New Template ]  │                                                                 │
└──────────────────────┴─────────────────────────────────────────────────────────────────┘
```

---

## 2. Managing Inspector Templates

In the **Templates** tab:
- **Browse & Filter:** Search templates by name or category tag (`General`, `RPG`, `Shooter`, `Vehicles`, `WorldGen`, `Audio`, `AI`, `UI`, `Layouts`, `Master Suite`).
- **Inspect Configuration:** View description, category badges, intelligent makeover passes, and declarative rules.
- **Hierarchical Layout Paths (`GroupPath`):** Rules support slash-separated group paths (e.g. `Combat/Vitals` for Tab + Box, or `Combat/Vitals/Row` for Tab + Box + Row) to construct sophisticated multi-level nested layouts automatically.
- **Short-Circuit Control (`StopProcessingIfMatched`):** Individual rules can be set to stop evaluating subsequent rules on a member once matched, preventing conflicting attribute applications.
- **Open in Makeover Graph:** Click to open the template's visual node graph in `MakeoverGraphWindow` for advanced visual wiring.
- **Duplicate Template:** Quickly clone an existing template to create studio-specific variations.

### Built-in Production Templates Directory (14 Templates)

| Template Name | Category | Badge | Core Architectural Theme |
| :--- | :---: | :---: | :--- |
| **`Clean & Modern Polish`** | `General` | ✨ | Universal starter template: status lights, required validation, asset previews, auto-sliders. |
| **`RPG Character & Combat`** | `RPG` | ⚔️ | Dual-bar health/mana gauges, cooldown timers, attribute stats, combat action buttons. |
| **`Sci-Fi Weapon & Ballistics Suite`**| `Shooter` | 🚀 | Ammo counters, overheat bars, fire rates, spread sliders, reload triggers. |
| **`Vehicle Physics & Engine Dynamics`**| `Vehicles`| 🏎️ | RPM/torque gauges, gear ratios, suspension travel, tire friction sliders. |
| **`Procedural World & Biome Generator`**| `WorldGen`| 🌍 | Seed generators, octave noise sliders, terrain curve pickers, map generation buttons. |
| **`Audio Director & Soundscape Mixer`**| `Audio` | 🎧 | Decibel sliders, audio clip previews, spatial blend rings, bus routing controls. |
| **`AI Agent & Behavior Controller`** | `AI` | 🧠 | State indicators, perception radii, threat meters, blackboard debug actions. |
| **`UI View & Screen Layout Suite`** | `UI` | 🖥️ | Screen anchors, canvas bounds, animation timing, transition triggers. |
| **`Layout Archetype: Game Dashboard`** | `Layouts` | 📊 | Metric cards, telemetry status bars, split overview panels. |
| **`Layout Archetype: Multi-Tab Workspace`**| `Layouts`| 📑 | Clean multi-tab navigation separating Core, Physics, Audio, and Advanced sections. |
| **`Layout Archetype: Split-Pane Master/Detail`**| `Layouts`| ✂️ | Vertical resizable split pane for master navigation and detail properties. |
| **`Layout Archetype: Hybrid Split-Pane & Tabs`**| `Layouts`| 🗂️ | Combines horizontal tabs with resizable split pane inspector panels. |
| **`Cyberpunk Neon & Animated FX`** | `Addons Showcase` | ⚡ | Animated pulsing glows, cybernetic borders, chromatic shift cards. |
| **`AAA Production Suite (Core & Addons Master)`**| `Master Suite`| 👑 | Exhaustive master layout combining class framing, telemetry gauges, and validation. |

---

## 3. The Interactive Test Engine

At the bottom of the Template & Recipe Manager:
- Drag any `MonoScript` or GameObject into the **Test Script** slot.
- The manager simulates the template or recipe against the target without saving changes.
- A results summary shows exactly which members matched, what attributes would be applied, and any conflict warnings.

---

## 4. Rebuilding Built-in Assets

If built-in templates or recipes are accidentally deleted or corrupted:
- Go to the Unity menu:  
  **`Tools > Maharaja Studio > MSUltimate > Rebuild Built-in Presets & Recipes`**.
- The factory automatically restores all default templates and recipes into `Assets/MSUltimate/Addons/MSUltimate-InspectorCustomizer/Templates/`.
