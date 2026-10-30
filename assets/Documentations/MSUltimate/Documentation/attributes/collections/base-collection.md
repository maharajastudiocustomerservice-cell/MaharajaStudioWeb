# [BaseCollection]

> Base configuration attribute for MSUltimate advanced collection and dictionary drawers providing pagination, real-time search, clipboard tools, and custom themes.

---

## 1. Overview & Value Proposition

**What it does:**
Provides advanced search, pagination, copy/paste, and visual styling options for lists, arrays, and custom collections.

**The Problem:**
Unity's default `ReorderableList` is basic and clunky. Once a list grows beyond 20 items, the Inspector scrolls forever, lag spikes occur during repaint, there is no way to search for specific items, and copying entries between lists is impossible.

**The Solution:**
Add collection styling attributes inherited from `[BaseCollection]`:
- **Instant Search Bar:** Filter lists with hundreds of elements instantly by typing keywords.
- **Smart Pagination:** Break massive lists into clean pages (e.g. 10 or 15 items per page) to eliminate Inspector scroll lag.
- **Clipboard & Batch Operations:** 1-click copy/paste array items, clear collections, or duplicate entries with full Undo support.
- **Custom Visual Styling:** Set alternating row colors, rounded borders, custom header banners, and empty placeholder labels.

---

## 2. Quick Start

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.Runtime.Collections;

public class InventoryData : MonoBehaviour
{
    [DrawCollection(ShowSearch = true, ShowPagination = true, ItemsPerPage = 10)]
    public List<string> itemNames = new List<string>();
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Arrays (`T[]`), `List<T>`, `HashSet<T>`, `Queue<T>`, `Stack<T>`, `SerializableDictionary<K, V>` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public BaseCollectionAttribute()
```

*Note: `BaseCollectionAttribute` is an abstract class serving as the foundation for concrete collection attributes like `[DrawCollection]` and `[DrawDictionary]`.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowSearch` | `bool` | `true` | Displays an interactive search filter field at the top of the collection. |
| `ShowPagination` | `bool` | `false` | Enables page-by-page navigation for large datasets. |
| `ItemsPerPage` | `int` | `15` | Maximum number of rows rendered per page when pagination is active. |
| `ShowItemCount` | `bool` | `true` | Displays a badge indicator with the total number of elements. |
| `MaxHeight` | `float` | `0f` | Maximum pixel height for the scroll container (`0` = no limit). |
| `AllowClipboard` | `bool` | `true` | Enables copy/paste buttons for transferring array elements. |
| `AllowClear` | `bool` | `true` | Enables a 1-click "Clear All" action in the collection header menu. |
| `EmptyMessage` | `string` | `"Collection is empty."` | Placeholder text rendered when the list has zero elements. |
| `ShowMenuButton` | `bool` | `true` | Shows the action menu button (⋮) with advanced list actions. |
| `HeaderLabel` | `string` | `null` | Custom title text rendered above the collection header. |
| `HeaderBackgroundColor` | `string` | `null` | Hex color string for the collection header bar. |
| `HeaderTextColor` | `string` | `null` | Hex color string for header text. |
| `RowBackgroundColor` | `string` | `null` | Hex color string for standard rows. |
| `AlternatingRowBackgroundColor` | `string` | `null` | Hex color string for zebra-striped alternating rows. |
| `BorderColor` | `string` | `null` | Hex color string for the container boundary border. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels. |
| `BorderWidth` | `float` | `1f` | Border stroke width in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.Runtime.Collections;

public class LootDropTable : MonoBehaviour
{
    [System.Serializable]
    public struct DropItem
    {
        public string itemId;
        public float weight;
        public int minQuantity;
        public int maxQuantity;
    }

    [Header("Drop Configuration")]
    [DrawCollection(
        HeaderLabel = "Enemy Loot Drops",
        ShowSearch = true,
        ShowPagination = true,
        ItemsPerPage = 8,
        EmptyMessage = "No drop items configured yet.",
        BorderRadius = 6f
    )]
    public List<DropItem> lootDrops = new List<DropItem>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Searchable]` | Supported | Pairs seamlessly with root class search filters. |
| `[BoxGroup]` | Supported | Embeds cleanly inside collapsible boxes and tabs. |
| `[ShowIf]` | Supported | Can be conditionally shown or hidden based on game settings. |
