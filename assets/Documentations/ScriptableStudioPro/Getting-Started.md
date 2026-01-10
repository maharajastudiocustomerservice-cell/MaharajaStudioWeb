# Getting Started

Welcome to **Scriptable Studio Pro**. This guide will help you set up the tool and create your first database.

## Installation

1. Import the **Scriptable Studio Pro** package into your Unity project.
2. The tool will automatically compile and appear in the menu bar.

## Opening the Window

Go to `Asset > Scriptable Studio Pro` or `Tools > Maharaja Studio > Scriptable Studio Pro > Open Window` (or press `Ctrl+M` / `Cmd+M`).

## Your First Workflow

### 1. Select a Type
The left sidebar lists every `ScriptableObject` class in your project.
- Click on a type (e.g., `ItemData`, `EnemyStats`) to load the grid.
- If you don't have any custom ScriptableObjects yet, create a simple C# script:

```csharp
using UnityEngine;

[CreateAssetMenu(fileName = "NewItem", menuName = "Game/Item")]
public class ItemData : ScriptableObject
{
    public string ItemName;
    public int Cost;
    public float Damage;
}
```

### 2. Create Mode vs. Edit Mode
Use the dropdown in the top-left toolbar to switch modes:

- **Create Mode**: Start with a blank slate. Add "Virtual Instances" to the list. These exist only in the window until you click "Create Assets".
- **Edit Mode**: Loads all existing `.asset` files of the selected type from your project. Changes are applied directly to the files when you press "Update Linked Assets".

### 3. Adding Data
1. Ensure you are in **Create Mode**.
2. Click the **➕ (Add)** button in the toolbar to add a row.
3. Type values into the grid cells.
4. Use **Duplicate** to copy rows quickly.

### 4. Saving Assets
1. When you are happy with your data, check the **Folder Settings** at the bottom of the window.
2. Choose a **Subfolder Name** (e.g., "Items").
3. Click **Create Assets**.
4. The tool will generate the `.asset` files in your project.

---

## Next Steps

- Learn about the [Core Workflow](Core-Workflow.md) to master the grid and bulk editing.
- Explore [Power Features](Power-Features.md) like Formulas and Smart Fill.
- Set up the [AI Assistant](AI-Assistant.md) to generate content for you.
