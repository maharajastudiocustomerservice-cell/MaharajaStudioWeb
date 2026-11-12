# Unity Context Menus & Editor Shortcuts

> **Module:** MSUltimate Inspector Customizer — Workflows & Menus  
> **Topic:** Complete Directory of Context Menus across Components, GameObjects, Assets, and Windows

---

## 1. Component Header Context Menu

Right-clicking the header bar of any MonoBehaviour or ScriptableObject in the Unity Inspector surfaces the **`MSUltimate`** context submenu:

```
[Component Header Right-Click]
├── Reset
├── Remove Component
├── Move Up / Down
└── MSUltimate
    ├── ⚡ Magic Makeover (1-Click Auto-Detect)
    ├── 🎨 Open Inspector Makeover Wizard...
    ├── 🪟 Live Compare (Before vs After)...
    ├── 📋 Apply Preset >
    │   ├── Clean & Modern Polish
    │   ├── RPG Character & Combat HUD
    │   ├── Sci-Fi Blaster & Weapon System
    │   ├── Vehicle Physics Rig & Engine
    │   ├── Procedural Biome & World Generator
    │   ├── Audio Ambience & Soundscape Synthesizer
    │   ├── AI Agent & Behavior Blackboard
    │   ├── Game Canvas & Adaptive UI Theme
    │   └── Layout Archetypes >
    │       ├── Split-Pane Master Detail Workspace
    │       ├── Hybrid Split-Pane & Tabs Workspace
    │       ├── Multi-Tab Workspace
    │       └── Game Dashboard
    └── 🗑️ Clear Customizer Overrides
```

### 1.1 Action Details
| Menu Command | Priority | Action Performed |
| :--- | :---: | :--- |
| **`⚡ Magic Makeover`** | `100` | Scans the component, scores all installed templates, executes the highest-scoring template, and repaints the inspector in real time. |
| **`🎨 Open Makeover Wizard...`** | `101` | Launches `InspectorMakeoverModalWindow` for visual preset browsing, scoring explanations, and selective rule toggling. |
| **`🪟 Live Compare...`** | `102` | Launches `InspectorMakeoverCompareWindow` showing an interactive side-by-side comparison (Before vs. After). |
| **`📋 Apply Preset >`** | `120-133`| 1-Click application of specific curated templates without auto-detection. |
| **`🗑️ Clear Overrides`** | `140` | Deletes all customizer overrides for this component from the profile, restoring the default inspector. |

---

## 2. GameObject Hierarchy Context Menu

Right-clicking any GameObject in the Scene Hierarchy window:
- **Path:** **`GameObject > Maharaja Studio > MSUltimate > Customize Inspector...`** *(Priority 20)*
- **Behavior:** Automatically resolves the GameObject, identifies its primary inspectable component, and launches `InspectorCustomizerWindow` targeted to that component.

---

## 3. Project Window Asset Context Menu

Right-clicking any file in the Unity Project browser:
- **Path:** **`Assets > Maharaja Studio > MSUltimate > Customize Inspector...`** *(Priority 30)*
- **Supported Assets:**
  - C# Scripts (`.cs`): Resolves the declared class type.
  - ScriptableObjects (`.asset`): Resolves the data model and opens its profile.
  - Prefabs (`.prefab`): Resolves the root component.

---

## 4. MonoScript Header Context Menu

Right-clicking the header bar of a `.cs` script asset in the Inspector window:
- **Path:** **`CONTEXT > MonoScript > MSUltimate > Customize Inspector...`** *(Priority 500)*
- **Behavior:** Opens the customizer targeted directly to that script type without needing to instantiate it on a scene GameObject.

---

## 5. EditorWindow Context Menu

Right-clicking the tab or header of any custom `EditorWindow`:
- **Path:** **`CONTEXT > EditorWindow > MSUltimate > Customize Window...`** *(Priority 500)*
- **Behavior:** Opens `InspectorCustomizerWindow` targeted to the `EditorWindow` type, allowing visual customization of developer tool windows.

---

## 6. Top Tools Menu Commands

The suite registers menu items under the Unity top menu bar:

| Menu Item Path | Priority | Action Performed |
| :--- | :---: | :--- |
| **`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Inspector Customizer`** | `200` | Opens the main visual customizer dual-pane editor window. |
| **`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Makeover Graph Editor`** | `201` | Launches the visual node graph editor for authoring procedural templates and macros. |
| **`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Template & Recipe Manager`** | `202` | Opens the template and compound recipe management hub. |
| **`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Inspector Customizer Settings`** | `203` | Opens the 8-category split-view project preferences and AI settings window. |
| **`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Component Defaults & Rules`** | `204` | Opens the global component defaults and ignore rules configuration window. |
| **`Tools > Maharaja Studio > MSUltimate > Rebuild Built-in Presets & Recipes`** | `1010` | Restores and refreshes all factory templates, archetypes, and recipes into the project. |
