# [DrawCollection]

> Renders arrays, lists, queues, and 2D/3D matrix data structures with advanced reordering, search filtering, pagination, and order badges.

---

## 1. Overview & Value Proposition

**What it does:**
Upgrades standard Unity arrays and lists with a search bar, paging controls, clean row numbers, and smooth drag-and-drop reordering.

**The Problem:**
Standard Unity lists become completely unmanageable when managing large game datasets (e.g. 50+ enemy spawn waves, inventory items, or dialogue nodes). Finding a single item requires endless scrolling, reordering items is awkward, and multi-dimensional matrices cannot be rendered in the Inspector at all.

**The Solution:**
Add `[DrawCollection]` above any list, array, or matrix:
- **Instant Search & Filter:** Type to filter list elements immediately without lag.
- **Fast Pagination:** Page through large arrays with next/previous controls and configurable items-per-page.
- **Index Order Badges:** Clean visual number badges (`#01`, `#02`) indicate exact order at a glance.
- **Matrix 2D/3D Grid Support:** Visualizes multi-dimensional arrays and grids directly as interactive cell tables.

---

## 2. Quick Start

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.Runtime.Collections;

public class WaveManager : MonoBehaviour
{
    [DrawCollection(ShowSearch = true, ShowPagination = true, ItemsPerPage = 5)]
    public List<GameObject> waveEnemyPrefabs = new List<GameObject>();
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Arrays (`T[]`), `List<T>`, `HashSet<T>`, `Queue<T>`, `Stack<T>`, `Matrix2D<T>`, `Matrix3D<T>` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public DrawCollectionAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ElementLabel` | `string` | `null` | Custom title prefix for child element headers (e.g. "Wave Element"). |
| `ShowOrderBadges` | `bool` | `true` | Displays numeric index chips (`#01`, `#02`) beside each element. |
| `MatrixCellSize` | `float` | `48f` | Pixel cell size when rendering 2D/3D matrix collections. |
| `ShowSearch` | `bool` | `true` | Enables real-time keyword search filtering. |
| `ShowPagination` | `bool` | `false` | Enables pagination controls. |
| `ItemsPerPage` | `int` | `15` | Maximum items displayed per page. |
| `ShowItemCount` | `bool` | `true` | Displays total element count badge in the header. |
| `AllowClipboard` | `bool` | `true` | Enables copy/paste buttons for array transfer. |
| `EmptyMessage` | `string` | `"Collection is empty."` | Text shown when the collection is empty. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.Runtime.Collections;

public class SkillTreeController : MonoBehaviour
{
    [System.Serializable]
    public struct SkillNode
    {
        public string skillName;
        public int requiredLevel;
        public Sprite skillIcon;
    }

    [Header("Player Skill Progression")]
    [DrawCollection(
        ElementLabel = "Skill Node",
        ShowSearch = true,
        ShowPagination = true,
        ItemsPerPage = 6,
        ShowOrderBadges = true,
        HeaderBackgroundColor = "#2C3E50",
        BorderRadius = 4f
    )]
    public List<SkillNode> availableSkills = new List<SkillNode>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Nests cleanly inside box containers and collapsible foldouts. |
| `[ShowIf]` | Supported | Dynamically display the entire collection based on conditions. |
| `[Searchable]` | Supported | Integrates with overall class-level inspection filters. |
