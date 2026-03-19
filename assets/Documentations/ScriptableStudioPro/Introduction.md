# Introduction

**Scriptable Studio Pro** is the ultimate asset management platform for Unity. It transforms the way you create, edit, and manage `ScriptableObject` data, giving you the speed of a spreadsheet, the depth of a full inspector, and the creative power of Generative AI — all inside a single, cohesive editor window.

Designed for **professional studios and solo developers** alike, version 3.0 marks a major leap forward in type compatibility, navigation ergonomics, and workflow depth.

---

## Key Features

### 📊 The Grid Editor
Forget the default Inspector. View and edit hundreds of assets simultaneously in a high-performance, multi-column grid.
- **Sort & Filter**: Find assets instantly by name, type, or field values — including advanced query syntax with `&&`, `||`, comparison operators, and nested field access.
- **Bulk Editing**: Select multiple rows and edit them simultaneously.
- **Reorder**: Drag and drop rows to organize your list instantly.

### 🎨 Native Drawing System *(New in 3.0)*
Any field type is now rendered correctly in the **Detail Panel**, without workarounds or exclusions.
- Types with a Unity `CustomPropertyDrawer` are **detected automatically** at startup and rendered natively.
- Register additional types in **Settings › Native Drawn Types** to give them first-class treatment.
- This covers `SerializableDictionary`, third-party framework types, any custom generic wrapper, and any type your team builds with a property drawer.

### 🔬 Next-Generation Type Parser *(New in 3.0)*
The internal type-reading and writing engine has been completely rebuilt from the ground up.
- Handles **every C# primitive** including `uint`, `byte`, `sbyte`, `short`, `ushort`, `ulong`, `char`, and `decimal`.
- Handles **all Unity types**: math structs, `Gradient`, `AnimationCurve`, `LayerMask`, `Quaternion`, `Bounds`, and more.
- **Generic types and custom serializers** (e.g., `SerializableDictionary<TKey, TValue>`) are parsed using a multi-strategy engine that respects `ISerializationCallbackReceiver`, ensuring the exact same state as runtime.
- Previously, many of these types showed empty or broken values. They now work universally across the Grid, Detail Panel, Undo/Redo, Smart Fill, and AI generation.

### 🏷️ Pill Navigation System *(New in 3.0)*
When working with multiple selected types in Batch Mode, a row of **interactive pills** appears above the grid, one per selected type.
- **One-click navigation** between any checked type — no sidebar scrolling.
- **Drag-to-reorder** pills to set your preferred workflow order.
- The container auto-collapses to save space and expands on demand.

### 🌐 Localization Support *(New in 3.0)*
Fields using **Unity Localization** (`LocalizedString`, `LocalizedAsset`, and any type in the `UnityEngine.Localization` namespace) are now fully supported.
- Values are correctly read, written, and cloned without breaking internal table references.

### 🛠️ Dual Workflow Modes
- **Create Mode**: Rapidly prototype data in memory. Create 100 items, tweak them, save only when ready.
- **Edit Mode**: Load existing assets from your project and modify them in place with bulk tools.

### ⚡ Power Tools
- **Formulas**: Use math directly in fields (`=[Level] * 100`, `=[Strength] + [Agility]`).
- **Smart Fill**: Select a range and auto-complete sequences, gradients, patterns, and GUIDs.
- **Smart Rename**: Rename hundreds of files based on their internal data in one click.
- **Find & Replace**: Search across all fields and replace text or values instantly.
- **Validator**: Advanced rule-based validation with built-in rules, formula expressions, and Regex.

### 🧠 AI Asset Architect *(Optional)*
Integrated directly into the workflow is a world-class AI assistant.
- **Generate**: Create production-ready assets from text prompts.
- **Refine**: Use natural language to tweak existing data (*"Make all boss enemies 20% stronger"*).
- **Context-Aware**: Understands your game's name, theme, lore, and custom field types.
- [Read the full AI Documentation](./AI-System.md)

### 🛡️ Professional Grade
- **Undo/Redo**: A custom system tracks every change — including bulk operations, localization fields, and native-drawn types.
- **Import/Export**: JSON, CSV, SQL, and Google Sheets support.
- **Full Type Safety**: No special-casing needed. Every serializable C# and Unity type works out of the box.

---

## Why Scriptable Studio Pro?

Unity's default ScriptableObject workflow is slow: create one file, rename it, select it, edit the inspector, repeat. Complex field types like dictionaries or localization references require workarounds or custom editors.

**Scriptable Studio Pro** removes all of that friction. Whether you are balancing an RPG item database, managing NPC dialogue lines with localization, or configuring level data with complex custom serializers — this tool saves hours of manual work every day.
