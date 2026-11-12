# Live Before-vs-After Comparison Window

> **Module:** MSUltimate Inspector Customizer — Workflows & Menus  
> **Topic:** Side-by-Side Inspector Diffing, Score Badges, Evaluation Modes, and Live Application

---

## 1. Overview of `InspectorMakeoverCompareWindow`

Visualizing how an inspector will look before applying a makeover is critical for maintaining high UI standards across a project.

The **Live Compare Window** (`InspectorMakeoverCompareWindow`) renders an interactive, side-by-side split screen showing the component in its raw state versus its transformed MSUltimate state:

- **How to invoke:** Right-click any Component header $\rightarrow$ **`MSUltimate > 🪟 Live Compare (Before vs After)...`**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Live Makeover Compare: HeroController                                                 │
│  Template: [ RPG Character & Combat HUD ▼ ]  [ 94% Match ★ ]  [ 6 Fields Styled ]       │
├──────────────────────────────────────────┬─────────────────────────────────────────────┤
│  BEFORE (Default Unity Inspector)        │  AFTER (MSUltimate Makeover)                │
│  Mode: [ Default Unity ▼ ]               │  Template: RPG Character & Combat HUD       │
│  ──────────────────────────────────────  │  ─────────────────────────────────────────  │
│  Script: [HeroController]                │  ┌────────────────────────────────────────┐ │
│  Current Health: [80]                    │  │ ⚔️ WARRIOR HERO [Combat Controller]    │ │
│  Max Health:     [100]                   │  ├────────────────────────────────────────┤ │
│  Min Damage:     [10]                    │  │ ▼ Vitality Telemetry                   │ │
│  Max Damage:     [50]                    │  │   Health: [■■■■■■■■□□ 80 / 100]        │ │
│  Move Speed:     [6.5]                   │  │   Damage: [ 10 ────●───●── 50 ]         │ │
│  Respawn (hidden - method)               │  ├────────────────────────────────────────┤ │
│                                          │  │ [ ⚔️ Attack ] [ 🛡️ Shield ] [ 💥 Ultimate]│ │
│                                          │  └────────────────────────────────────────┘ │
├──────────────────────────────────────────┴─────────────────────────────────────────────┤
│  Comparing: Default Unity ➔ RPG Character (8 members evaluated)      [ Apply Makeover ]│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Top Toolbar & Metric Badges

| Control / Indicator | Purpose & Visual Feedback |
| :--- | :--- |
| **Template Selector Dropdown** | Cycle through all installed templates (e.g. *Clean & Modern*, *RPG Combat*, *Sci-Fi Weapon*, *Vehicle Physics*). The **AFTER** column repaints instantly with the selected template's layout. |
| **Score Badge (`94% Match`)** | Calculates the percentage of inspected fields and methods successfully transformed by the active template. Scores above 80% highlight with an emerald green badge. |
| **Diff Pill (`6 Fields Styled`)** | Real-time summary tallying how many fields received decorators, how many layout groups were created, and how many methods were turned into buttons. |
| **Target Object Slot** | Allows dragging another GameObject into the window to compare different scene instances on the fly. |

---

## 3. The Three "Before" Comparison Modes

The left column can compare against three different baseline representations:

1. **`DefaultUnity`:**
   - Strips all MSUltimate drawers and renders the raw, unadorned Unity Inspector.
   - Ideal for seeing the dramatic contrast between standard flat Unity fields and MSUltimate's UI Toolkit styling.
2. **`CurrentInspector`:**
   - Renders the component exactly as it currently looks in your active Inspector window (including any profile overrides already applied).
   - Ideal for comparing incremental tweaks when experimenting with a new template on an already-customized component.
3. **`CodeOnly`:**
   - Evaluates only attributes declared directly in C# code, ignoring profile overrides.
   - Ideal for verifying whether your code-defined attributes are preserved properly.

---

## 4. Live Synchronization & 1-Click Application

- **Live Parameter Editing:** Tweak values inside the active `InspectorCustomizerWindow` or `MakeoverGraphWindow`; the **AFTER** column in the compare window updates in real-time.
- **Selective Action Review:** Scroll through the diff list to see which fields matched which rules.
- **Commit Layout:** Clicking **`Apply Makeover`** records a Unity Undo state, saves the generated overrides into the component's `InspectorProfile` asset, and closes the window.
