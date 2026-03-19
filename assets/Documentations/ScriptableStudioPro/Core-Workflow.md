# Core Workflow

This document covers the primary interface and workflows of **Scriptable Studio Pro**.

---

## The Main Interface

The window is divided into three main areas:

1. **Sidebar (Left)** — Lists all `ScriptableObject` types found in your project.
2. **Grid Area (Right, Center)** — The main workspace where you view and edit data.
3. **Toolbar (Top)** — Mode selection and global tools.

Additionally in v3.0, a **Pill Strip** appears at the top of the right pane when multiple types are selected, enabling instant type navigation.

---

## Working with the Grid

The grid is the heart of the tool. It displays your assets in a spreadsheet-like view.

### Sorting & Filtering

- **Sort**: Click any column header to sort ascending/descending.
- **Filter**: Use the instance search bar to filter rows.
  - **Simple Text**: `Sword` matches any instance with "Sword" in the name.
  - **Advanced Syntax**:
    - **Logical**: `&&` (AND), `||` (OR). Example: `[Cost] < 50 && [Type] == "Fire"`.
    - **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`, `:` (contains).
    - **Nested Fields**: `[Stats.Health] > 100` or `[Inventory[0]] == "Potion"`.
    - **Null Check**: `[Model] == {null}` to find missing references.

### Reordering

Drag rows by their index number (far-left column) to reorder them. Works in both Create and Edit modes.

### Bulk Editing

1. Select multiple rows (`Ctrl/Cmd + Click` or `Shift + Click`).
2. Edit a value in **any** selected row.
3. The change applies to **all** selected rows simultaneously.

---

## Pill Navigation *(New in v3.0)*

When you check multiple types in the sidebar (for Batch Mode), a **Pill Strip** appears above the grid.

| Action | Result |
|:---|:---|
| **Left-click** a pill | Immediately switches the grid to show that type's data |
| **Right-click + drag** a pill | Reorders the pill to your preferred position |
| **▼ / ▲ button** (far right) | Collapses or expands the pill strip |

The pill strip height is configurable in **Settings › Visuals › Pill Height**.

---

## Context Menu Actions

Right-click on any row or index number to access:

| Action | Description |
|:---|:---|
| **Ping Asset** | Highlights the file in the Project window |
| **Copy / Paste Values** | Copy all field values from one row and paste them into another |
| **Duplicate Row** | Creates an exact copy of the selected instance |
| **Smart Rename** | *(Edit Mode)* Renames the asset file based on a string field |
| **Insert Row Above / Below** | Adds a blank row at a specific position |
| **Delete** | Removes the selected instance |

---

## Detail Panel

Accessible via **Open Details** in the main toolbar. The Detail Panel shows all fields of a single instance in a vertical, scrollable layout.

### Native Drawing System *(New in v3.0)*

In v3.0, the Detail Panel uses a **native drawing pipeline** for field types. The system works as follows:

1. At startup, the tool scans all loaded assemblies for `CustomPropertyDrawer` attributes and builds a fast type-to-drawer cache.
2. When rendering a field in the Detail Panel, the tool checks if the field's type is **native-drawn**. A type is native-drawn if:
   - It has a Unity `CustomPropertyDrawer` registered in any loaded assembly.
   - Its fully-qualified name (or its generic type definition) is listed in **Settings › Native Drawn Types**.
   - Its name contains "SerializableDictionary" (auto-supported).
   - It is a `LocalizedString`, `LocalizedAsset`, or any `UnityEngine.Localization.*` type.
3. If native-drawn → rendered via `IMGUIContainer` + Unity's built-in inspector.
4. Otherwise → rendered via the tool's own recursive field builder.

This means you **never need to configure anything** for types like `SerializableDictionary`, localization fields, or any type your team provides a custom drawer for.

### Supported Attributes in the Detail Panel

The Detail Panel respects these Unity field attributes:
- `[Header]` — renders a bold section label above the field.
- `[Tooltip]` — surface as hover tooltip on the label.
- `[TextArea]` / `[Multiline]` — renders a multi-line text box with configurable minimum height.
- `[Range]` — renders a **slider + numeric input** side-by-side.
- `[HideInInspector]` — field is hidden, matching standard Inspector behavior.

### Searching Fields

Use the **search bar** at the top of the Detail Panel to filter visible fields by name.

---

## Create Mode vs. Edit Mode

### Create Mode

| Property | Detail |
|:---|:---|
| **Purpose** | Rapidly creating *new* assets |
| **Behavior** | Data exists only in memory until explicitly saved |
| **Save** | Click **Create Assets** to write `.asset` files to disk |
| **Naming** | Files are named based on the **Naming Pattern** (e.g., `{TYPE}_{ii}`) |
| **Drag & Drop** | Drag existing `.asset` files onto the window to import their values |

### Edit Mode

| Property | Detail |
|:---|:---|
| **Purpose** | Managing *existing* assets |
| **Behavior** | Grid operates on the actual asset files |
| **Import** | **Import All** or **Import Selected** to load assets into the grid |
| **Save** | Click **Update Linked Assets** to write changes to disk |

---

## Drag & Drop

You can drag any `ScriptableObject` file from the **Project Window** into the Scriptable Studio Pro window:

- In **Edit Mode**: Adds the asset as a linked row.
- In **Create Mode** with **Link Dragged Assets** enabled: Adds a linked copy. Duplicate prevention ensures no asset is added twice.
- Object fields inside the **Detail Panel** also accept individual asset drags.

---

## Undo / Redo

The tool uses a **custom undo stack** independent of Unity's standard undo system.

| Shortcut | Action |
|:---|:---|
| `Ctrl + Z` / `Cmd + Z` | Undo |
| `Ctrl + Y` / `Cmd + Shift + Z` | Redo |

The undo stack tracks:
- Individual cell value changes (including localization fields and native-drawn types)
- Row additions and removals
- Reordering
- Bulk operations and drag-and-drop batches
- Naming pattern changes
