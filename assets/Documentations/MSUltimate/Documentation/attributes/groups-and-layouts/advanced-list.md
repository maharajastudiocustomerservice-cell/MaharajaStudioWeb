# [AdvancedList]

> Supercharges Arrays and Lists with drag-and-drop reordering, instant search filtering, pagination, item counts, and lifecycle event callbacks.

---

## 1. Overview & Value Proposition

**What it does:**
Replaces Unity's standard `ReorderableList` with an advanced, feature-rich collection container. Adds live search filtering, pagination for long lists, expand/collapse controls, dynamic element labeling, and C# event hooks for add/remove operations.

**The Problem:**
Standard Unity lists become unwieldy when collections hold more than 10–20 elements. Finding specific items requires scrolling through dozens of rows, there are no search tools or pagination, reordering laggy elements is frustrating, and running logic when items are added or removed requires tedious `OnValidate` reflection.

**The Solution:**
Add `[AdvancedList]` to any array or list field:
- **Real-Time Search Bar:** Filter list elements on the fly by text, name, or properties.
- **Built-In Pagination:** Paginate large lists with customizable page sizes (`ItemsPerPage = 10`), keeping the inspector compact.
- **Dynamic Element Titles:** Name element headers using member properties (`OnTitleAttribute = "enemyName"`).
- **Expand / Collapse All:** 1-click toolbar buttons to expand or collapse all elements at once.
- **Lifecycle Callbacks:** Trigger custom methods when items are added or deleted (`OnItemAdded`, `OnItemRemoved`).

---

## 2. Quick Start

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class InventoryRoster : MonoBehaviour
{
    [AdvancedList(ShowSearch = true, ShowPagination = true, ItemsPerPage = 5)]
    public List<string> playerInventory = new List<string>
    {
        "Health Potion", "Iron Sword", "Mana Elixir", "Shield of Valor",
        "Torch", "Golden Key", "Leather Armor", "Boots of Speed"
    };
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field` |
| **Supported Types** | `List<T>`, `T[]` (Arrays and generic lists) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AdvancedListAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowHeader` | `bool` | `true` | Displays the collection header toolbar. |
| `Draggable` | `bool` | `true` | Allows dragging items to reorder them in the list. |
| `ShowAddRemove` | `bool` | `true` | Displays the `+` and `-` item management buttons. |
| `ShowSearch` | `bool` | `true` | Enables real-time text search filtering across elements. |
| `ShowPagination` | `bool` | `true` | Divides large collections into page views. |
| `ItemsPerPage` | `int` | `10` | Number of items shown per page when pagination is active. |
| `ShowItemCount` | `bool` | `true` | Displays count badge in the header (e.g. `"Enemies (24)"`). |
| `ShowAlternatingRowBackgrounds` | `bool` | `true` | Zebra-stripes rows with subtle alternating colors. |
| `ShowExpandCollapseControls` | `bool` | `true` | Shows Expand All and Collapse All buttons in header toolbar. |
| `HeaderLabel` | `string` | `""` | Custom header title override. |
| `EmptyMessage` | `string` | `"List is empty."` | Message displayed when collection contains 0 elements. |
| `OnTitleAttribute` | `string` | `""` | Property or method name inside element class used for dynamic foldout titles. |
| `OnItemAdded` | `string` | `""` | Method name in parent class called when an item is added. |
| `OnItemRemoved` | `string` | `""` | Method name in parent class called when an item is removed. |
| `MaxHeight` | `float` | `0f` | Max pixel height before enabling scrolling (`0` = unconstrained). |
| `BorderRadius` | `float` | `0f` | Corner radius of the list container. |
| `BorderColor` | `string` | `null` | Hex border color. |
| `HeaderBackgroundColor`| `string`| `null` | Hex color for the header toolbar. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[Serializable]
public class WaveEnemyData
{
    public string enemyIdentifier = "Goblin Archer";
    public int spawnCount = 5;
    public float spawnInterval = 1.5f;
}

public class WaveSpawnManager : MonoBehaviour
{
    [Header("Wave Configuration (Paginated & Searchable)")]
    [AdvancedList(
        HeaderLabel = "Enemy Wave Registry",
        ShowSearch = true,
        ShowPagination = true,
        ItemsPerPage = 3,
        OnTitleAttribute = nameof(WaveEnemyData.enemyIdentifier),
        OnItemAdded = nameof(OnEnemyAdded),
        OnItemRemoved = nameof(OnEnemyRemoved),
        BorderRadius = 4f
    )]
    public List<WaveEnemyData> waveEnemies = new List<WaveEnemyData>();

    private void OnEnemyAdded(int index)
    {
        Debug.Log($"Enemy wave profile added at index {index}");
    }

    private void OnEnemyRemoved(int index)
    {
        Debug.Log($"Enemy wave profile removed from index {index}");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Integrates cleanly inside outer tab or group containers. |
| `[ShowIf]` | Supported | Evaluates list visibility conditionally. |
| `[ReadOnly]` | Supported | Disables adding, removing, and reordering while maintaining list inspection. |
| Element Drawers | Supported | Elements inside the list fully support MSUltimate drawers (`[MinMaxSlider]`, `[SmartEnum]`). |
