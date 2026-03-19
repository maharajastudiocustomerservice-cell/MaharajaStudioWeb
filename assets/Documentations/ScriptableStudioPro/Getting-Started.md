# Getting Started

Welcome to **Scriptable Studio Pro v3.0**. This guide will get you set up and creating your first database in minutes.

---

## Installation

1. Import the **Scriptable Studio Pro** package via the Unity Package Manager.
2. The tool compiles automatically and registers menu items.

---

## Opening the Window

Go to **`Assets › Scriptable Studio Pro`** or **`Tools › Maharaja Studio › Scriptable Studio Pro › Open Window`**  
Keyboard shortcut: **`Ctrl + M`** / **`Cmd + M`**

---

## Your First Workflow

### 1. Select a Type

The left sidebar lists every `ScriptableObject` class in your project.

- Type in the **Search Bar** to filter types instantly.
- Click a type (e.g., `ItemData`, `EnemyStats`) to load its grid.

If you don't have any custom `ScriptableObject` types yet, create a simple C# script and compile:

```csharp
using UnityEngine;

[CreateAssetMenu(fileName = "NewItem", menuName = "Game/Item")]
public class ItemData : ScriptableObject
{
    public string ItemName;
    public int Cost;
    public float Damage;
    public bool IsRare;
}
```

You can use any field type — primitives, Unity structs, enums, custom serializers, `LocalizedString`, `List<T>`, or any type with a `CustomPropertyDrawer`. The v3.0 parser handles all of them.

---

### 2. Choose a Mode

Use the **Mode Selector** in the top-left toolbar:

| Mode | Purpose |
|:---|:---|
| **Create Mode** | Prototype data in memory. Instances are virtual until you click **Create Assets**. |
| **Edit Mode** | Load existing `.asset` files and modify them. Changes are applied when you click **Update Linked Assets**. |

---

### 3. Add Data

1. Ensure you are in **Create Mode**.
2. Click **➕ (Add)** to add a row.
3. Fill values directly in the grid cells.
4. Use **Duplicate** (right-click context menu) to clone rows quickly.

For fields that are complex types (custom structs, dictionaries, localized strings), click **Open Details** in the toolbar to open the **Detail Panel** for that instance. The Detail Panel uses the **Native Drawing System** to render every field correctly, including types with custom property drawers.

---

### 4. Navigate with Pills *(New in v3.0)*

When you check multiple types in the sidebar (for batch creation), a row of **Pills** appears above the grid — one pill per selected type.

- **Left-click** a pill to jump to that type's grid instantly.
- **Right-click + drag** a pill to reorder it.
- Click **▼** at the right of the pill strip to expand/collapse it.

---

### 5. Save Assets

1. When satisfied with your data, check the **Folder Settings** at the bottom of the window.
2. Choose a **Subfolder Mode** (Default, Single Subfolder, or Subfolder Per Type).
3. Click **Create Assets**.
4. The tool generates `.asset` files in your project at the chosen location.

---

## Working with Custom & Localization Types

### Custom Types (Serializers, Dictionaries, Wrappers)

If your `ScriptableObject` has a field like `SerializableDictionary<int, string>` or any third-party wrapper type:

1. **Grid**: The tool automatically detects if a type has a `CustomPropertyDrawer` and renders it natively. No extra configuration is usually needed.
2. **Detail Panel**: The field appears with its proper drawer UI.
3. If a type is *not* auto-detected, go to **Settings › Native Drawn Types** and add its fully-qualified class name manually.

### Localization Fields (`LocalizedString`, `LocalizedAsset`)

Fields using **Unity Localization** are handled automatically:
- Values are correctly read from and written to the Localization tables without breaking references.
- No manual configuration required.

---

## Next Steps

| Guide | Description |
|:---|:---|
| [Core Workflow](Core-Workflow.md) | Master the grid, sorting, bulk editing, and context menus. |
| [Power Features](Power-Features.md) | Formulas, Smart Fill, Import/Export, and Undo/Redo. |
| [User Interface](UserInterface.md) | Detailed reference for every button, field, and panel. |
| [AI Assistant](AI-System.md) | Use AI to generate and refine data at scale. |
| [Configuration](Configuration.md) | Settings, shortcuts, assembly filtering, and more. |
