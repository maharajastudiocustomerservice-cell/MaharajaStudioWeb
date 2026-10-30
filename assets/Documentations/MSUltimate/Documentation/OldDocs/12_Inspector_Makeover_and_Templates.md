# 12. Inspector Makeover & Template Engine

The **Inspector Makeover** system inside **MSUltimate Inspector Customizer** provides instant, 1-Click declarative visual transformations for any Unity component, MonoBehaviour, or ScriptableObject.

Rather than manually writing and configuring dozens of attributes by hand across thousands of lines of code, the Template Engine scans your component's fields, methods, and declarations, evaluates customizable rules, and applies rich layouts, progress bars, group boxes, foldouts, sliders, and interactive action buttons non-destructively in real time.

---

## 1. Core Architecture & Philosophy

```
  ┌─────────────────────────────────────────────────────────────┐
  │                    Target Component / Script                │
  │   (Raw C# fields, unadorned methods, zero hardcoded UI)     │
  └──────────────────────────────┬──────────────────────────────┘
                                 │ Scanned by Template Engine
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │                   Inspector Template Engine                 │
  │  • Scans: Class, Serialized Fields, Parameterless Methods  │
  │  • Evaluates: Scope, Data Type, Name, Attribute Filters     │
  │  • Expands: Dynamic Macro Tokens ({Name}, {Class}, etc.)   │
  │  • Resolves: Attribute Conflicts (Skip / Replace / Dup)    │
  └──────────────────────────────┬──────────────────────────────┘
                                 │ Generates Virtual Overrides
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │                  InspectorProfile Asset                     │
  │   • Non-destructive virtual attributes stored in assets     │
  │   • 1-Click Bake to Code converts directly to C# attributes│
  └─────────────────────────────────────────────────────────────┘
```

### Key Advantages:
- **Zero Source Code Pollution**: Experiment with layouts, themes, and groupings without touching or dirtying C# source files.
- **1-Click Makeovers**: Transform raw classes into studio-grade inspectors in a single click.
- **Undo/Redo Integrated**: Every makeover operation is fully registered in Unity's `Undo` stack.
- **Optional Code Baking**: When satisfied with your layout, bake virtual attributes directly into native C# attributes with the built-in Code Baker.

---

## 2. 1-Click Makeover Workflow

You can trigger an Inspector Makeover at any time via the Inspector Customizer editor tools:

### Step 1: Open the Makeover Dialog
1. Open the main **Inspector Customizer** window via:
   `Tools > Maharaja Studio > MSUltimate > Windows > Inspector Customizer`
2. Select any GameObject in your scene or inspect any component.
3. Click the **🎨 Makeover** button in the top toolbar, or choose **🎨 1-Click Makeover...** from the window context menu.

### Step 2: Choose a Preset Template
- Browse the left panel of the Makeover Modal to explore built-in or custom presets.
- Presets are categorized by domain (e.g. `General`, `RPG`, `Shooter`, `Vehicles`, `WorldGen`, `Audio`, `AI`, `UI`).

### Step 3: Inspect Live Match Preview & Conflict Resolution
- The right panel shows an instant **Live Match Preview** detailing:
  - Every field and method scanned on your component.
  - Which rules matched and what attributes will be applied.
  - Any potential attribute conflicts and how they will be resolved (Skip / Replace).

### Step 4: Apply Makeover
- Click **🎨 Apply Makeover**. The component's inspector is immediately transformed into a polished, grouped layout.

---

## 3. Built-in Curated Presets Catalog

MSUltimate includes 8 pre-configured, multi-condition presets tailored for standard game development domains:

| Preset Name | Category | Icon | Target Domain & Mechanics | Key Visual Features |
|---|---|:---:|---|---|
| **Clean & Modern Polish** | General | ✨ | Universal MonoBehaviours, managers, logic components | Smart foldouts for ID/Setup, vitals boxes, audio boxes, physics boxes, 0–100 sliders for rates/speeds, method buttons. |
| **RPG Character & Combat** | RPG | ⚔️ | Player heroes, enemy champions, bosses, stats systems | Color-coded gauges (Health 💚, Mana 💙, Stamina 💛, Shield 🩵, Rage ❤️), Combat Attributes box, Equipment foldout, Combat action buttons. |
| **Sci-Fi Weapon & Ballistics Suite** | Shooter | 🚀 | Guns, blasters, plasma cannons, projectile weapons | Ammo gauge, Overheat bar, Ballistics & Recoil box, Ergonomics box, Visuals/Audio foldout, Fire/Reload action buttons. |
| **Vehicle Physics & Engine Dynamics** | Vehicles | 🏎️ | Cars, tanks, flight rigs, physics chassis | Tachometer RPM bar (8000 max), Speedometer gauge (300 max), Powertrain box, Suspension/Steering box, Aero/Brakes foldout, Cockpit action buttons. |
| **Procedural World & Biome Generator** | WorldGen | 🌍 | Terrain engines, voxel builders, dungeon generators | Noise & Elevation box, Atmospheric palette box, Foliage/Chunk topology foldouts, 0–1 probability sliders, Generator action buttons. |
| **Audio Director & Soundscape Mixer** | Audio | 🎧 | Audio managers, spatial emitters, ambient soundscapes | Normalized 0–1 volume faders, Pitch controls, 3D Spatialization box, Stem playlists foldout, Playback preview buttons. |
| **AI Agent & Behavior Controller** | AI | 🧠 | Enemy bots, companion AI, state machines | Aggro & Threat gauge, Morale bar, Perception & Senses box, Navigation box, Combat tactics box, Waypoints foldout, AI state triggers. |
| **UI View & Screen Layout Suite** | UI | 🖥️ | Canvases, screen presenters, widget controllers | Screen rect bounds box, Spacing & Padding box, Color palette foldout, Motion & Animation timings, UI testing buttons. |

---

## 4. Declarative Rule Engine Specification

Each `InspectorTemplate` consists of an ordered sequence of declarative rules (`InspectorTemplateRule`).

### Target Scope
Controls which member types are evaluated:
- **`Field`**: Serialized instance fields only.
- **`Method`**: Public parameterless methods (eligible for action buttons).
- **`Class`**: Component-level declarations (for ComponentStyle or Header decorators).
- **`Any`**: All scanned members.

### Type Filter
Filters members based on their data type:
- **`Any`**: Matches any data type.
- **`Numeric`**: Matches `int`, `float`, `double`, `short`, `byte`, `long`, `uint`, etc.
- **`Text`**: Matches `string` or `char`.
- **`Boolean`**: Matches `bool`.
- **`Color`**: Matches `Color` and `Color32`.
- **`Enum`**: Matches any enum type.
- **`ArrayOrList`**: Matches any array (`T[]`) or `List<T>`.
- **`SubclassOf`**: Matches types inheriting from or implementing the name specified in `TypeFilterArgument`.
- **`ExactType`**: Matches exact type name specified in `TypeFilterArgument`.

### Name Filter & Multi-Pattern Lists
Matches member variable or method names:
- **`Wildcard`**: Glob matching with `*` and `?`. Supports multiple patterns separated by `|` or `,` (e.g. `*health*|*mana*|*stamina*|*shield*`).
- **`Contains`**: Substring matching (case-insensitive). Supports multiple keywords separated by `|` or `,`.
- **`StartsWith`**: Prefix matching (e.g. `m_` or `On`).
- **`EndsWith`**: Suffix matching (e.g. `Duration` or `Vfx`).
- **`RegexPattern`**: Full Regular Expression matching.
- **`Any`**: Matches any member name.

### Attribute Filter
Checks whether the member already has existing attributes:
- **`Any`**: No attribute requirements.
- **`HasAttribute`**: Only matches if the member already has the specified attribute (e.g. `Range` or `SerializeField`).
- **`LacksAttribute`**: Only matches if the member does NOT have the specified attribute.

### Action Types
Defines the visual modification applied when criteria match:
- **`AddAttribute`**: Injects an attribute override with configured constructor arguments and property values.
- **`ApplyRecipe`**: Applies a reusable multi-attribute recipe.
- **`WrapInGroup`**: Wraps the member in a visual container (`BoxGroup`, `Foldout`, `TabGroup`, `HorizontalGroup`, etc.).

### Conflict Handling
Controls what happens if the attribute already exists on the member:
- **`Skip`**: If already present, skips adding to preserve existing configuration.
- **`Replace`**: Overwrites existing values with template values.
- **`Duplicate`**: Adds a duplicate attribute override (useful for stacking headers or decorators).

---

## 5. Dynamic Macro Tokens

When defining attribute arguments, labels, or group names, you can use **dynamic macro tokens** that are resolved per member at evaluation time:

| Macro Token | Expanded Output | Example Usage | Evaluated Result |
|---|---|---|---|
| `{Name}` | Nicified member name | `Button(Text = "⚔️ {Name}")` on `CastSpell()` | `⚔️ Cast Spell` |
| `{RawName}` | Exact C# identifier | `Foldout(Name = "{RawName}_Settings")` on `audioSource` | `audioSource_Settings` |
| `{Type}` | CLR type name | `Note(Text = "Type: {Type}")` on `float health` | `Type: Single` |
| `{Class}` | Target class name | `BoxGroup(Name = "{Class} Vitals")` on `PlayerHero` | `PlayerHero Vitals` |
| `{Category}` | Recipe or group category | `Title(Title = "{Category}")` | `Stats` |

---

## 6. Compound Attribute Recipes

An **Inspector Attribute Recipe** (`InspectorAttributeRecipe`) is a reusable collection of pre-composed attribute configurations designed to be applied to individual members or referenced by templates.

### Built-in Recipes:
1. **`Polished Health Bar`**: Green ProgressBar (`#10B981`) with 100 max value.
2. **`Mana Energy Bar`**: Electric blue ProgressBar (`#3B82F6`) with 100 max value.
3. **`Stamina Gauge Bar`**: Golden amber ProgressBar (`#F59E0B`) with 100 max value.
4. **`Shield Barrier Bar`**: Cyan ProgressBar (`#06B6D4`) with 100 max value.
5. **`Overheat Warning Bar`**: Crimson ProgressBar (`#EF4444`) with 100 max value.
6. **`Action Trigger Button`**: Elevated 32px Button with `{Name}` dynamic macro label.
7. **`Audio Normalized Slider`**: CustomRange (0 to 1) for volume and gain faders.
8. **`Collapsible Section`**: Dynamic Foldout group named `{Category}`.

---

## 7. Template & Recipe Manager Window

To author, modify, duplicate, or test your custom templates and recipes:
1. Open the manager via:
   `Tools > Maharaja Studio > MSUltimate > Windows > Template & Recipe Manager`
2. **Left Panel**: Search and select templates or recipes. Use **+ New Template** or **+ New Recipe** to create custom presets.
3. **Rule Builder**: Visually configure rule criteria (Scope, Types, Names, Actions, Groups, and Overrides).
4. **Interactive Test Sandbox**: Drag any `MonoScript` into the test field to preview rule evaluation in real time without modifying any scene objects.

---

## 8. Resetting & Rebuilding Presets

If you wish to reset all built-in templates and recipes to studio defaults:
- Run: `Tools > Maharaja Studio > MSUltimate > Rebuild Built-in Presets & Recipes`

---

## 9. Sample Scripts Testbed

Eight comprehensive sample scripts are provided in `Assets/MSUltimate/Addons/MSUltimate-InspectorCustomizer/Sample/Scripts/` to easily test the Makeover system:

| Script Name | Recommended Preset | Tested Features |
|---|---|---|
| `Sample_RPGHeroCharacter.cs` | RPG Character & Combat | Health/Mana/Stamina/Shield/Rage progress bars, Combat Stats box, Equipment foldout, Combat action buttons. |
| `Sample_SciFiWeaponBlaster.cs` | Sci-Fi Weapon & Ballistics Suite | Ammo gauge, Overheat bar, Ballistics box, Handling box, Visuals foldout, Weapon action buttons. |
| `Sample_VehiclePhysicsRig.cs` | Vehicle Physics & Engine Dynamics | Tachometer RPM bar, Speedometer gauge, Powertrain box, Suspension box, Aero foldout, Cockpit action buttons. |
| `Sample_ProceduralBiomeGenerator.cs` | Procedural World & Biome Generator | Noise & Elevation box, Atmosphere palette box, Chunk/Foliage foldouts, 0–1 probability sliders, Generation action buttons. |
| `Sample_AudioEnvironmentDirector.cs` | Audio Director & Soundscape Mixer | Normalized volume sliders, Pitch sliders, 3D Spatialization box, Stem playlists, Playback action buttons. |
| `Sample_AIEnemyController.cs` | AI Agent & Behavior Controller | Aggro & Threat gauge, Morale bar, Perception box, Navigation box, Tactics box, Waypoints foldout, AI state buttons. |
| `Sample_UIViewScreenLayout.cs` | UI View & Screen Layout Suite | Screen rect bounds box, Layout padding box, Color palette foldout, Animation timings, UI testing buttons. |
| `Sample_ComprehensiveMakeoverShowcase.cs` | Clean & Modern Polish / All | Master testbed covering all primitives, vectors, curves, gradients, arrays, lists, enums, child structs, and multi-signature action methods. |

---

## 10. Intelligent Makeover Analysis Passes

In addition to static declarative rules, the Makeover Engine features five sequential intelligent analysis passes that dynamically reason about your component's member relationships, naming conventions, and domain mechanics.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       INTELLIGENT MAKEOVER PIPELINE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Declarative Rule Pass    → Scope, type, and name-based attribute matching│
│ 2. Dynamic Companion Binding→ health binds to maxHealth (DynamicMaxValue)   │
│ 3. Relational Field Pairing → min/max & start/end paired into HorizontalRow │
│ 4. Smart Toggle Cascades    → hasShield collapses shieldHealth, shieldRegen │
│ 5. Action Toolbar Pass      → Parameterless methods clustered into Buttons  │
│ 6. Magic Match Scoring      → 0-100% compatibility score + 1-Click Apply   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1. Relational Field Pairing
Detects companion fields that represent ranges, limits, or dimensions and automatically formats them:
- **Companion Pairs (`min*`/`max*`, `start*`/`end*`, `width`/`height`)**:
  - Automatically identifies paired fields such as `minDamage` & `maxDamage`, `minPitch` & `maxPitch`, `minSlope` & `maxSlope`, or `startTime` & `endTime`.
  - Wraps them in side-by-side `[HorizontalGroup("{Stem} (Range)", Gap = 6)]` so they render on the same line, saving valuable vertical inspector real estate.
- **Range Vectors (`Vector2` / `Vector2Int`)**:
  - Detects vectors representing ranges (`pitchRange`, `damageLimits`, `zoomBounds`).
  - Injects `[MinMaxSlider(0f, 100f)]` for intuitive dual-thumb slider control.

### 2. Dynamic Companion Binding
Traditional inspectors hardcode progress bars to a static maximum (e.g. `100f`). When an RPG character levels up or equips gear increasing `maxHealth` to `450`, static bars display distorted values.
- **Automatic Max Detection**:
  - Scans for companion numeric fields:
    - `currentHealth` / `health` → `maxHealth`, `maximumHealth`, `hpMax`
    - `currentMana` / `mana` → `maxMana`, `maximumMana`, `mpMax`
    - `currentAmmo` / `ammo` → `clipSize`, `maxAmmo`, `magazineCapacity`
    - `fuel` → `maxFuel`, `fuelCapacity`
    - `currentXp` / `experience` → `xpToNextLevel`, `maxXp`
- **Dynamic Property Binding**:
  - Automatically configures `ProgressBarAttribute.DynamicMaxValueMember = companionField.Name`.
  - As stats scale dynamically during gameplay, the inspector gauge dynamically updates its denominator without custom editor code!

### 3. Smart Toggle Cascades
Eliminates clutter through automated **progressive disclosure**:
- **Feature Switch Detection**:
  - Scans for boolean toggles starting with `has`, `use`, `enable`, `allow`, `can`, or `show` (e.g. `hasShield`, `useGravity`, `enableAudio`, `enableSuspension`, `hasHeadlights`, `useTurbo`).
- **Child Parameter Identification**:
  - Identifies related child properties using stem matching:
    - `hasShield` → controls `shieldHealth`, `shieldRegenRate`, `shieldBreakSound`, `shieldColor`.
    - `useGravity` → controls `gravityScale`, `gravityDirection`.
    - `enableAudio` → controls `audioVolume`, `audioPitch`, `audioClips`.
    - `hasHeadlights` → controls `headlightIntensity`, `headlightColor`, `headlightAngle`.
- **Conditional Visibility Wiring**:
  - Injects `[ConditionalField("{toggleName}")]` onto all child parameters.
  - When the feature switch is unchecked, all associated child fields instantly collapse out of view.

### 4. Action Toolbar & Method Buttons Pass
In Unity's default inspector, methods cannot be triggered without entering Play Mode or executing custom editor GUI code.
- **Method Discovery**:
  - Scans all public and decorated parameterless candidate methods on the target component (e.g. `FireWeapon()`, `Reload()`, `PerformStunt()`, `GenerateWorld()`).
- **Action Button Clustering**:
  - Injects `[Button("⚡ {Name}")]` with automatically nicified labels.
  - Groups them together inside a shared `[ButtonGroup("Actions")]` toolbar rendered at the bottom of the inspector.
- **Zero Boilerplate**:
  - Developers instantly gain one-click debug and test triggers directly from the inspector without writing custom buttons in C#.

### 5. 1-Click Smart Auto-Detect & Match Scoring ("Magic Makeover")
Eliminates guesswork when selecting presets for unfamiliar components:
- **Compatibility Scoring (0–100%)**:
  - Computes a weighted match score evaluating:
    - **Member Coverage (50%)**: Proportion of serialized fields and methods enhanced by the preset.
    - **Domain Keyword Affinity (35%)**: Alignment between component type name/fields and domain mechanics (RPG, Shooter, Vehicle, Biome, Audio, UI).
    - **Intelligence Bonus (15%)**: Bonus points for successfully wired dynamic bars, paired rows, toggle cascades, and action buttons.
- **⚡ Magic Makeover Recommendation Banner**:
  - Displayed prominently at the top of the modal window:
    ```
    ⚡ Magic Recommendation: RPG Character & Combat [96% Match]
    Matched 14/16 fields (88%) • 2 dynamic progress bars • 2 companion pairs • 1 toggle cascade • 3 action buttons
    [ ⚡ Apply Magic Makeover ]
    ```
  - Clicking **Apply Magic Makeover** applies the highest-ranked preset with all intelligence passes in **1-Click** and registers complete Undo history.
- **Match Badges & Sorting**:
  - Every preset card in the catalog displays its compatibility percentage (`96%`, `78%`, `45%`).
  - Presets are automatically sorted by compatibility rank so the most relevant preset is always selected first.
- **Granular Control**:
  - Developers can toggle individual intelligence passes (`🔗 Pairing`, `⚡ Dynamic Max`, `✨ Cascades`, `⚡ Action Toolbar`) live in the preview toolbar, or uncheck individual preview actions prior to application.

---

## 11. Component Context Menu Quick-Makeover

To streamline developer workflows without cluttering the Inspector UI, all Makeover functionality is accessible via the **Component Context Menu**:

1. In the Unity Inspector, **Right-Click** the header of any `MonoBehaviour` component.
2. Navigate to the `Maharaja Studio` submenu:

```
Right-Click Component Header
└── Maharaja Studio
    ├── ⚡ Magic Makeover (1-Click Auto-Detect)
    ├── 🎨 Open Inspector Makeover Wizard...
    ├── 🪟 Live Compare (Before vs After)...
    ├─────────────────────────────────────────
    ├── 📋 Apply Preset
    │   ├── Clean & Modern Polish
    │   ├── RPG Character & Combat HUD
    │   ├── Sci-Fi Blaster & Weapon System
    │   ├── Vehicle Physics Rig & Engine
    │   ├── Procedural Biome & World Generator
    │   ├── Audio Ambience & Soundscape Synthesizer
    │   ├── AI Agent & Behavior Blackboard
    │   └── Game Canvas & Adaptive UI Theme
    ├─────────────────────────────────────────
    └── 🗑️ Clear Customizer Overrides
```

### Key Advantages:
- **Zero Inspector Drawing Pollution**: No custom GUI controls or buttons are injected into your normal inspector drawing loop.
- **1-Click Magic Application**: Selecting `⚡ Magic Makeover` instantly detects the best matching preset, runs all five intelligent passes, updates the active `InspectorProfile`, and repaints the inspector in ~0.05 ms.
- **Non-Destructive Reset**: Selecting `🗑️ Clear Customizer Overrides` safely wipes overrides for that component from the profile with full `Undo` support.

---

## 12. Interactive Live "Before vs. After" Side-by-Side Preview Window

When evaluating templates, developers can open the dedicated **Makeover Compare Window** (`InspectorMakeoverCompareWindow`) to see the exact before-and-after transformation in real time:

- **How to Open**:
  - Click the **🪟 Live Side-by-Side Preview** button in the Makeover Modal Window footer or toolbar.
  - Or click **🪟 Live Preview** on the Magic Recommendation banner.
  - Or right-click any MonoBehaviour header and select `Maharaja Studio > 🪟 Live Compare (Before vs After)...`.

### Dual-Column Layout:
```
┌──────────────────────────────────────┬──────────────────────────────────────┐
│  ⚪ BEFORE: Default Unity Inspector   │    ✨ AFTER: MSUltimate Makeover      │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ Script: Sample_RPGHeroCharacter      │ 🎨 RPG Character & Combat HUD        │
│                                      │                                      │
│ currentHealth           [ 100.0 ]    │ ⚡ Current Health       75 / [maxHealth]│
│ maxHealth               [ 100.0 ]    │ [███████████████████░░░░░] (Emerald) │
│                                      │                                      │
│ minDamage               [  15.0 ]    │ 🔗 Horizontal Companion Pair         │
│ maxDamage               [  45.0 ]    │ [Min Damage: 15.0] [Max Damage: 45.0]│
│                                      │                                      │
│ hasShield               [  ✔  ]      │ ✔ Has Shield                         │
│ shieldHealth            [  50.0 ]    │ ↳ Shield Health          [+Conditional]│
│                                      │                                      │
│ (Hidden by Unity Default Inspector)  │ ⚡ Action Toolbar                    │
│                                      │ [ ⚡ Cast Spell ]  [ ⚡ Drink Potion ]│
└──────────────────────────────────────┴──────────────────────────────────────┘
```

- **Left (Before)**: Accurately reproduces default Unity inspector rendering (flat monochrome rows, un-nicified variable names, and hidden methods).
- **Right (After)**: Live visual simulation of the MSUltimate layout with colored gauges, companion flex rows, conditional disclosure tags, and action buttons.
- **Interactive Preset Switcher**: Switch between templates live using the top dropdown menu to immediately evaluate different themes before applying.
- **Isolated Preview Sandbox**: Editing values or interacting with controls inside the compare window operates on an isolated in-memory preview instance (`HideFlags.HideAndDontSave`). GameObjects in the scene or project are never modified or dirtied by testing values in the comparison window.
- **1-Click Apply**: Click **⚡ Apply This Makeover** directly in the compare window to commit changes with complete Undo support.

---

## 13. Hierarchical Visual Architecture & Layout Engine (GroupPaths)

Previous inspector makeover systems were limited to flat single-level boxes or foldouts. Complex game systems (such as hero controllers, vehicle physics rigs, or inventory managers) quickly overflow a single-tier layout, causing visual clutter and excessive vertical scrolling.

MSUltimate introduces a **Hierarchical Layout Engine** that allows authoring complex multi-tier layouts using an intuitive **"Folder Path" Mental Model**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MULTI-TIER VISUAL ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ [Hero Identity Overview] (Top Header)                                       │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ 🗂️ [ Overview ]    🗂️ [ Combat ]    🗂️ [ Dynamics ]    🗂️ [ Media & FX ]│ │
│ ├─────────────────────────────────────────────────────────────────────────┤ │
│ │ 📦 [ BoxGroup: Vitals & Core Resources ]                                │ │
│ │  • Health:  [████████████████████████████░░░░░] 75 / 100                │ │
│ │  • Mana:    [████████████████░░░░░░░░░░░░░░░░░] 40 / 100                │ │
│ │  • 🔗 Horizontal Row: [ Min Damage: 12 ] [ Max Damage: 36 ]            │ │
│ │                                                                         │ │
│ │ 📂 [ Foldout: Advanced Multipliers ]                                    │ │
│ │  • Crit Chance: 0.25                                                    │ │
│ │  • Crit Multiplier: 2.0                                                 │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│ ⚡ [ Bottom Action Dock ]                                                   │ │
│ [ ⚡ Cast Spell ]   [ ⚡ Take Damage ]   [ ⚡ Reset Stats ]                │ │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1. Intuitive "Folder Path" Syntax
Any rule's `GroupPath` can now specify nested layout tiers using forward slashes (`/`) or explicit prefixes:

| Format | Syntax Example | Synthesized Inspector Layout |
|---|---|---|
| **Flat Box** | `Vitals` | Standalone `[BoxGroup("Vitals")]` (100% backward-compatible). |
| **2-Tier Tab/Box** | `Combat/Vitals` | `[BeginTabGroup("Combat")]` → `[BoxGroup("Vitals")]`. |
| **3-Tier Tab/Box/Row** | `Combat/Stats/Row1` | Tab `Combat` → Box `Stats` → `[HorizontalGroup("Stats_Row1")]`. |
| **Explicit Prefixes** | `Tab:Audio/Foldout:Advanced FX` | Tab `Audio` → Nested collapsible `[Foldout("Advanced FX")]`. |
| **Hero / Header** | `Hero/Identity Overview` | Top-level summary header pinned above main tab navigation. |

### 2. Intelligent Layout Synthesizer
Under the hood, the engine compiles hierarchical paths into Unity-safe visual attributes:
1. **Deterministic Tab Grouping**:
   - `[BeginTabGroup]` is injected **strictly onto the first member** of each tab, preventing broken duplicate tab bars.
   - `[EndTabGroup]` is synthesized cleanly on the terminal boundary of the tab collection.
2. **Deterministic Monotonic `PropertyOrder`**:
   - Groups items in 1,000-point bands (Tab 1 = `1000..1999`, Tab 2 = `2000..2999`, etc.), boxes within tabs in 100-point sub-bands, and items within boxes in sequential steps (`+1`, `+2`...).
   - Guarantees that members belonging to the same visual box are contiguous, completely preventing Unity declaration-order fragmentation.
3. **Dedicated Bottom Action Dock**:
   - Parameterless methods with `[Button]` overrides are assigned `PropertyOrder >= 9000`, anchoring action toolbars neatly at the bottom of the inspector beneath all tabs and data fields.
4. **Top Header Protection**:
   - Un-tabbed summary fields are ordered between `100` and `999`, establishing clear "Hero Cards" that remain visible regardless of which tab is active.

### 3. Built-in Layout Archetypes
MSUltimate includes high-level architectural templates:
- **`Layout Archetype: Game Dashboard`**:
  - Top Hero Identity card (`id`, `name`, `level`, `rank`).
  - Core vs. Advanced tabs for balanced parameter management.
  - Dedicated Prefab & Asset References tab (filters by `UnityObject`).
  - Collapsible Diagnostic / Cheat foldouts.
  - Docked Action button toolbar.
- **`Layout Archetype: Multi-Tab Workspace`**:
  - Full studio 4-tab workspace layout: `General`, `Gameplay`, `Media & FX`, and `Diagnostics`.
  - Automatically sorts any complex monolithic script into clean, focused domains.
- **`Layout Archetype: Split-Pane Master/Detail Workspace`** (Phase 2):
  - TwoPaneSplitView resizable workspace layout.
  - Top Hero Header identity overview.
  - Left Column for Character Profile & Level progression.
  - Right Column for Dynamic Progress Gauges (Health, Mana, Stamina) & Combat Attributes.
  - Docked bottom Action button toolbar.

---

## 14. Resizable Two-Column Split Panes (`TwoPaneSplitView`)

MSUltimate's Inspector Makeover engine natively supports Unity UIElements' `TwoPaneSplitView` through simple declarative GroupPaths. You can divide any component inspector into two resizable columns without writing a single line of custom editor code.

### 1. GroupPath Split Syntax
Split panes can be declared using either keyword prefixes or positional tokens:

| Syntax Pattern | Meaning | Example |
| :--- | :--- | :--- |
| `Split:Name/Left/Box:Title` | Pane 0 (Left / Master) | `Split:Workspace/Left/Box:Profile Details` |
| `Split:Name/Right/Box:Title` | Pane 1 (Right / Detail) | `Split:Workspace/Right/Box:Combat Stats` |
| `Split/Left/BoxName` | Positional Pane 0 | `Split/Left/Stats` |
| `Split/Right/BoxName` | Positional Pane 1 | `Split/Right/Equipment` |
| `Tab:X/Split:Y/Left/Box:Z` | Split nested inside a Tab | `Tab:Combat/Split:Vitals/Left/Box:Health` |
| `Top:Title` / `Bottom:Title` | Vertical Split orientation | `Split:Logs/Top:Console` & `Split:Logs/Bottom:Filter` |

### 2. Automatic Attribute Synthesis
The layout engine synthesizes the exact attribute sequence required by `ModularMonoBehaviourEditor`:
1. **`[BeginSplitPane("NAME", Direction = Horizontal, Height = 220, InitialSplitterPosition = 200)]`** is synthesized on the first member of Pane 0.
2. **`[BeginSplitPane("NAME")]`** is synthesized on the first member of Pane 1 (triggering the pane switch).
3. **`[EndSplitPane]`** is synthesized on the terminal member of Pane 1 (cleanly popping the split container).

### 3. Monotonic Ordering Across Split Panes
To prevent Unity's C# field declaration order from interleaving left and right fields, the engine assigns strict monotonic `PropertyOrder` bands:
- **Left Pane Members**: Ordered in band `BaseOrder + 10..49`
- **Right Pane Members**: Ordered in band `BaseOrder + 50..99`
- **Root Header Members**: Ordered in band `100..999`
- **Action Buttons**: Docked at `9000+`

This guarantees that Pane 1 fields are never rendered before Pane 0 fields have completed, producing a clean, resizable side-by-side layout every time.



