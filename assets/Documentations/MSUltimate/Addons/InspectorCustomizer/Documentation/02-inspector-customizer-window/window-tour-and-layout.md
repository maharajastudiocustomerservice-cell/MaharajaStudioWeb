# Inspector Customizer Window Tour & Layout

> **Module:** MSUltimate Inspector Customizer — Editor Windows  
> **Topic:** User Interface Layout, Toolbar Anatomy, Filter Controls, Scope Menus, and Member Context Actions

---

## 1. Visual Workspace Architecture

The `InspectorCustomizerWindow` (`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Inspector Customizer`) is a responsive, dual-column workspace built entirely with Unity UI Toolkit:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│  [Target Object: HeroController] [🔍 TypePicker] [Mode: Both ▼] [Ping Profile] [💾 Save] [Bake]   │
├─────────────────────────────────────────────┬────────────────────────────────────────────────────┤
│  🔍 Search members...                       │  Selected: currentHealth (float)                   │
│  [Scope: Standard ▼]                        │  [Collapse All] [Copy Stack] [Paste] [MemberMenu ▼]│
│  [All] [Overridden] [Comp] [Fields] [Props] │  ────────────────────────────────────────────────  │
│  ────────────────────────────────────────── │  ┌──────────────────────────────────────────────┐  │
│  ▼ Component (1 override)                   │  │ ☰ [ComponentHeader]                     [⋮][✕]│  │
│    • HeroController [Header]                │  │   Title: "WARRIOR HERO"   Color: #FF3344     │  │
│  ▼ Fields (5 overrides)                     │  └──────────────────────────────────────────────┘  │
│    • currentHealth [Bar]                    │  ┌──────────────────────────────────────────────┐  │
│    • maxHealth [ReadOnly]                   │  │ ☰ [ProgressBar]                         [⋮][✕]│  │
│    • moveSpeed [Range]                      │  │   Min: 0   Max: 100   Color: #33CC66         │  │
│    • isGrounded [Toggle]                    │  └──────────────────────────────────────────────┘  │
│  ▼ Methods (2 overrides)                    │  ┌──────────────────────────────────────────────┐  │
│    • Respawn() [Button]                     │  │ ☰ [Tooltip]                             [⋮][✕]│  │
│    • LevelUp() [Button]                     │  │   Text: "Current character hit points"       │  │
│                                             │  └──────────────────────────────────────────────┘  │
│                                             │  [ + Add Attribute ]      [ ⚡ AI Decorator ]      │
└─────────────────────────────────────────────┴────────────────────────────────────────────────────┘
```

---

## 2. Top Toolbar Controls & Indicators

| Toolbar Control | Internal Identifier | Functionality & Interaction |
| :--- | :--- | :--- |
| **Target Object Slot** | `_targetField` | `ObjectField` accepting any `GameObject`, `Component`, or `ScriptableObject`. Dragging an object automatically resolves its type and opens its active `InspectorProfile`. |
| **Type Picker Button** | `_typePickerBtn` | Launches `TypePickerWindow` allowing developers to inspect C# classes, POCO data structs, or EditorWindows without needing an active scene instance. |
| **Target Type Badge** | `_targetTypeBadge` | Displays the assembly-qualified type name and declaring assembly (e.g. `Game.Characters.HeroController [Assembly-CSharp]`). Click to ping or select the target script. |
| **Override Mode Dropdown** | `_modeDropdown` | Toggles between `Both` (hybrid), `EditorOverride` (profile only), and `CodeOnly` (source code only). |
| **Ping Profile Button** | `_pingBtn` | Pings and highlights the active `InspectorProfile` ScriptableObject in Unity's Project browser. |
| **Save Profile Button** | `_saveBtn` | Forces an immediate disk write of the active profile asset and marks it clean. |
| **Reset Profile Button** | `ic-reset-btn` | Clears all overrides on the current target component entry with confirmation and Undo tracking. |
| **Undo / Redo Buttons** | `_undoBtn` / `_redoBtn` | Navigates the Undo history stack. Also triggered via `Ctrl+Z`, `Ctrl+Y`, or `Ctrl+Shift+Z`. |
| **Explore Code Button** | `ic-import-btn` | Scans the target C# script and imports all code-defined attributes into the visual profile deck. |
| **Sync Selection Button** | `ic-sync-sel-btn` | Instantly synchronizes the customizer target with the currently selected scene GameObject or Project asset. |
| **Recipe Menu Button** | `_recipeBtn` | Opens a quick-access dropdown of installed attribute recipes to apply directly to the component. |
| **Refresh Button** | `ic-refresh-btn` | Invalidates reflection and hydration caches and forces a full redraw of member lists and cards. |
| **Settings Hub Button** | `ic-settings-btn` | Launches `InspectorCustomizerSettingsWindow` for project-wide preferences, AI configurations, and ignore rules. |
| **Bake Code Button** | `_bakeBtn` | Launches `BakeCodePreviewWindow` to permanently inject configured attributes into C# source code. |
| **Makeover Wizard Button** | `_makeoverBtn` | Launches `InspectorMakeoverModalWindow` for 1-click procedural layout generation. |
| **AI Assistant Button** | `_aiBtn` | Launches `AIDecoratorModalWindow` to prompt Large Language Models for automated inspector styling. |

---

## 3. Left Column: Member Discovery & Scope Filtering

The left column indexes all inspectable members discovered on the target type through reflection.

### 3.1 Category Filter Buttons
Quickly filter the member list by clicking one of the top filter buttons:
- **`All`:** Displays all discovered members across the component.
- **`Overridden`:** Filters the view to only show members that have at least one active profile override.
- **`Component`:** Focuses on class/component declaration styling attributes (`[ComponentHeader]`, `[ComponentBorder]`).
- **`Fields`:** Restricts the list to serialized, private backing, and inherited fields.
- **`Properties`:** Displays C# properties (getters/setters).
- **`Methods`:** Restricts the list to candidate action methods.

### 3.2 The Scope Filter Menu (`[Scope ▼]`)
Clicking the **Scope** dropdown opens a configuration menu controlling member discovery depth:

```
[Scope Filter Menu]
├── Presets
│   ├── Standard (Clean - Default)          ◄── Recommended for standard game scripts
│   └── Power User (Full Discovery)         ◄── Exposes compiler internals & private members
├── Fields
│   ├── [✓] Serialized Fields
│   ├── [ ] Private Fields
│   └── [ ] Compiler Backing Fields (<Prop>k__BackingField)
├── Properties
│   ├── [✓] Show C# Properties
│   └── [ ] Only Decorated Properties [ShowInInspector]
├── Methods
│   ├── [✓] Public Methods
│   ├── [ ] Private Methods
│   └── [ ] Methods with Parameters
├── Inheritance & Statics
│   ├── [ ] Static Members
│   └── [✓] Inherited Members
└── ⚙ Open Settings Window...
```

- **`Standard Preset`:** Displays public/serialized fields, public parameterless methods, and inherited members. Keeps the workspace clean and free of noise.
- **`Power User Preset`:** Enables discovery of private backing fields, private debug methods, static variables, and parameterized methods. Ideal for technical directors and systems programmers.

---

## 4. Member Context Menu (`[MemberMenu ▼]`)

Right-clicking any member in the left list or clicking the `[MemberMenu ▼]` button in the right column header opens a comprehensive utility menu:

### 4.1 Stack Clipboard Actions
- **`📋 Copy Attribute Stack`:** Copies all applied attributes, their parameter keys, and serialized values on this member to the internal clipboard.
- **`📄 Copy C# Attributes`:** Generates formatted C# attribute declaration code and copies it to the system clipboard.
- **`📋 Paste Stack (Append)`:** Appends all copied attributes to the selected member's existing stack.
- **`📋 Paste Stack (Replace)`:** Clears existing attributes on the selected member and replaces them with the clipboard stack.

### 4.2 Stack Management & Optimization
- **`🔇 Mute All Attributes`:** Sets `IsDisabled = true` across all attributes on this member, temporarily bypassing them during drawing.
- **`🔊 Unmute All Attributes`:** Re-enables all attributes on this member.
- **`⊞ Collapse All Parameters` / `⊟ Expand All Parameters`:** Toggles parameter foldout cards to save vertical screen space.
- **`🔀 Reverse Stack Order`:** Reverses the top-to-bottom execution order of attributes on this member.
- **`🔄 Reset Parameters to Defaults`:** Resets all attributes on this member to factory default values.
- **`🧹 Deduplicate Stack`:** Automatically removes redundant identical attribute definitions on the member.
- **`🔍 Re-import from C# Code`:** Re-scans the target C# script and imports any code-defined attributes on this specific member.

### 4.3 Quick Combos & Presets
One-click shortcuts to apply popular attribute combinations:
- **For Classes:** `Component Header & Box`, `Hierarchy Designer Row`.
- **For Methods:** `Action Button + HelpBox`, `Button Group Header`.
- **For Fields:** `BoxGroup + Title`, `Foldout Group`, `ReadOnly + InfoBox`, `Custom Range Slider`, `Conditional (ShowIf)`, `Add to Field Bookmark`.

### 4.4 Custom Recipes
- **`💾 Save Stack as Custom Recipe...`:** Saves the selected member's attribute stack as a new reusable `InspectorAttributeRecipe` ScriptableObject in your project.
- **`⚡ Apply Recipe >`:** Displays a categorized flyout menu of all installed attribute recipes to stamp onto the member.

### 4.5 Clear
- **`✕ Clear All Attributes for this Member`:** Deletes all overrides on this member from the profile.
