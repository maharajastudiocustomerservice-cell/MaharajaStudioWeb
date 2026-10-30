# [TableList]

> Renders lists and arrays as a spreadsheet-style interactive table where object properties map directly to horizontal columns.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms standard serialized lists or arrays of custom classes/structs into a structured data grid. Instead of repetitive nested foldouts for each element, each serialized field becomes a table column, and each list item becomes a compact row.

**The Problem:**
Managing collections of structured data (like weapon inventories, loot drop tables, or enemy spawn waves) using Unity's default list view is tedious. Every element has its own foldout that must be clicked open, wasting screen real estate and making side-by-side data comparison impossible.

**The Solution:**
Add `[TableList]` to any list or array field:
- **Spreadsheet-Style Grid:** View all items and compare their stats side-by-side in clean horizontal rows.
- **Column Header Row:** Auto-generates column headers matching member property names.
- **Zebra Striping:** Alternating row background colors for effortless horizontal eye tracking.
- **Scroll Capping:** Set `MaxHeight` to constrain massive lists inside a scrollable table pane.

---

## 2. Quick Start

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[Serializable]
public class ItemDrop
{
    public string itemId;
    [Range(0f, 1f)]
    public float dropRate;
    public int minQuantity;
    public int maxQuantity;
}

public class LootTable : MonoBehaviour
{
    [TableList]
    public List<ItemDrop> drops = new List<ItemDrop>();
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `List<T>`, `T[]`, `AdvancedList<T>` where `T` is a serializable class or struct |
| **Interface Implemented** | `ICollectionPresentationAttribute` (Tabular data presentation layout) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `TableListDrawer` (registered in `DrawerDatabase`) |

---

## 4. Constructors & Parameters

```csharp
public TableListAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `EnableCustomPresentation` | `bool` | `true` | Whether custom tabular collection presentation is enabled. |
| `ShowHeader` | `bool` | `true` | Whether to display the table column headers row. |
| `ExpandChildCollections`| `bool` | `false` | Whether nested collections inside cells start expanded. |
| `HeaderBackgroundColor`| `string`| `null` | Hex background color for the column header row. |
| `HeaderTextColor` | `string` | `null` | Hex text color for the column header labels. |
| `HeaderFontSize` | `int` | `0` | Header font size in pixels (`0` = default). |
| `RowBackgroundColor` | `string` | `null` | Hex background color for table rows. |
| `AlternatingRowBackgroundColor`| `string`| `null`| Hex color for alternating rows (zebra-striping). |
| `BorderColor` | `string` | `null` | Hex color code for the table outer border. |
| `BorderWidth` | `float` | `1f` | Table border thickness in pixels. |
| `BorderRadius` | `float` | `3f` | Corner radius for the table container. |
| `Padding` | `float` | `5f` | Internal cell padding in pixels. |
| `MarginTop` | `float` | `5f` | Spacing above the table in pixels. |
| `MarginBottom` | `float` | `5f` | Spacing below the table in pixels. |
| `MinHeight` | `float` | `150f` | Minimum pixel height for the table area. |
| `MaxHeight` | `float` | `0f` | Maximum pixel height before enabling scrolling (`0` = unconstrained). |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[Serializable]
public class EnemySpawnWave
{
    public string waveName = "Wave 1";
    public GameObject enemyPrefab;
    public int count = 5;
    public float spawnInterval = 1.2f;
    public bool isBossWave = false;
}

public class WaveManager : MonoBehaviour
{
    [Header("Encounter Waves Grid")]
    [TableList(
        HeaderBackgroundColor = "#2c3e50", 
        HeaderTextColor = "#ecf0f1", 
        AlternatingRowBackgroundColor = "#1a252f",
        MaxHeight = 280f,
        BorderRadius = 4f
    )]
    public List<EnemySpawnWave> campaignWaves = new List<EnemySpawnWave>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :--- | :--- |
| `[BoxGroup]` | Supported | Tables nest cleanly inside outer box or tab groups. |
| `[ShowIf]` | Supported | Evaluates conditional visibility on the entire table. |
| `[ReadOnly]` | Supported | Disables in-cell edits while preserving grid data inspection. |
| Inner Drawers | Supported | Cells respect nested attributes (`[Range]`, `[ColorHex]`, `[TagSelector]`). |
| `Collections (Arrays & Lists)` | **Supported (`ICollectionPresentationAttribute`)** | Transforms collection rendering into a structured tabular data grid with column headers and zebra striping. |

