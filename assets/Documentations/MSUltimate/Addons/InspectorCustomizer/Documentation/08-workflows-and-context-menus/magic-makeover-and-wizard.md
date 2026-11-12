# Magic Makeover & Inspector Makeover Wizard

> **Module:** MSUltimate Inspector Customizer — Workflows & Menus  
> **Topic:** 1-Click Auto-Detection Heuristics, Suitability Scoring, and the Makeover Wizard Modal

---

## 1. 1-Click Magic Makeover (`⚡ Magic Makeover`)

The fastest way to transform an unstyled inspector is the **1-Click Magic Makeover**:

- **How to invoke:** Right-click any Component header in the Unity Inspector $\rightarrow$ **`MSUltimate > ⚡ Magic Makeover (1-Click Auto-Detect)`**.

```
[Component Header Right-Click]
├── Reset
├── Remove Component
└── MSUltimate
    ├── ⚡ Magic Makeover (1-Click Auto-Detect)   ◄── CLICK HERE
    ├── 🎨 Open Inspector Makeover Wizard...
    ├── 🪟 Live Compare (Before vs After)...
    └── 📋 Apply Preset >
```

### 1.1 The Auto-Detection Scoring Algorithm
When clicked, the engine executes an instant evaluation pass:
1. **Reflection Scan:** Discovers all serialized fields, properties, and methods on the component.
2. **Heuristic Pattern Scoring:** Evaluates all installed templates against the component's member profile:
   - **Combat & RPG Keywords:** Terms like `health`, `mana`, `stamina`, `damage`, `shield`, `cooldown`, `xp` score highly for the **RPG Character & Combat** template.
   - **Physics & Engine Keywords:** Terms like `torque`, `rpm`, `gear`, `horsepower`, `suspension`, `tire` score highly for the **Vehicle Physics Rig** template.
   - **Audio & Soundscape Keywords:** Terms like `reverb`, `volume`, `pitch`, `bus`, `spatial`, `occlusion` score highly for the **Audio Director** template.
   - **Procedural Keywords:** Terms like `seed`, `octave`, `perlin`, `noise`, `biome`, `moisture` score highly for the **Procedural Biome** template.
3. **Winner Selection:** The highest-scoring template is chosen.
4. **Relational Passes Executed:** Companion pairs (`min*`/`max*`) are joined into `[HorizontalGroup]`, progress bars are bound to max fields, and methods are turned into action buttons.
5. **Applied to Profile:** Overrides are saved into the component's `InspectorProfile` and the inspector repaints immediately.

---

## 2. The Inspector Makeover Wizard

For cases where you want to preview templates, review recommendation scores, and selectively toggle rules before applying, open the **Makeover Wizard**:

- **How to invoke:** Right-click Component header $\rightarrow$ **`MSUltimate > 🎨 Open Inspector Makeover Wizard...`**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  Inspector Makeover Wizard: HeroController                                             │
│  Recommended Template: [ RPG Character & Combat HUD (Score: 94) ★ ]                    │
├──────────────────────┬─────────────────────────────────────────────────────────────────┤
│  CATEGORY FILTER     │  TEMPLATE DETAILS & LIVE PREVIEW                                │
│  [All] [RPG] [Audio] │  RPG Character & Combat HUD                                     │
│  [Physics] [UI]      │  Recommendation Reason: "Component features health, mana, and   │
│  ─────────────────── │  combat cooldown variables with matching companion max limits." │
│  TEMPLATES           │  ─────────────────────────────────────────────────────────────  │
│  • RPG Character ★   │  Intelligence Passes:                                           │
│  • Clean & Modern    │  [✓] Enable Relational Pairing        [✓] Enable Toggle Cascades│
│  • Sci-Fi Ballistics │  [✓] Enable Dynamic Companion Binding  [✓] Enable Action Toolbar│
│  • UI View Layout    │  ─────────────────────────────────────────────────────────────  │
│  • Vehicle Physics   │  Matched Rules to Apply:                                        │
│                      │  [✓] Rule 1: currentHealth -> [ProgressBar] (Color: #33CC66)    │
│                      │  [✓] Rule 2: currentMana   -> [ProgressBar] (Color: #3388FF)    │
│                      │  [✓] Rule 3: minDamage, maxDamage -> [HorizontalGroup]          │
│                      │  [✓] Rule 4: RespawnPlayer() -> [Button("Respawn Player")]      │
├──────────────────────┴─────────────────────────────────────────────────────────────────┤
│  [ Cancel ]                                                            [ Apply Makeover]│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Recommendation Scoring & Explanations
The Wizard displays:
- **Numerical Match Score (0–100):** Visual percentage indicating how well the template matches the component.
- **Natural Language Reason:** Explains why the template was recommended (e.g. *"Detected vehicle drivetrain variables: rpm, gearRatio, engineTorque"*).

### 2.2 Intelligence Feature Toggles
Before applying, you can toggle individual heuristic passes:
- **Relational Pairing:** Pairs companion fields into side-by-side rows.
- **Dynamic Companion Binding:** Connects progress bar ceilings to companion fields.
- **Toggle Cascades:** Wires boolean flags to conditionally hide child parameters.
- **Action Toolbar:** Gathers methods into interactive button bars.

### 2.3 Selective Rule Checkboxes
The Wizard lists every individual field and method that matched a rule. You can uncheck individual items if you want certain variables left unstyled.

### 2.4 One-Click Application
Clicking **`Apply Makeover`** commits the customized layout to the component's `InspectorProfile` asset with full Undo support.
