# [HierarchyChildCounter]

> Displays a badge of active and total direct or recursive child GameObjects directly on the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyChildCounter]` inspects a GameObject's transform hierarchy and renders a badge showing active versus total child counts (e.g. `"3/5"`, `"12/20"`). Driven by `HierarchyChildCounterRenderer`, it supports direct child counting (`Recursive = false`) or recursive descendant counting across all sub-branches (`Recursive = true`). It allows hiding the badge when empty (`OnlyIfChildrenExist = true`), customizable string templates (`Format = "{active}/{total}"`), and empty warning badge alerts (`WarnIfEmpty = true`, `EmptyWarningColor = "#E71C23"`).

**The Problem:**
When organizing object pools, waypoint networks, patrol paths, spawn groups, or UI lists, collapsed parent objects hide how many children are inside and whether any are currently active. Developers must repeatedly expand and collapse foldouts just to check child counts.

**The Solution:**
Decorating parent container components with `[HierarchyChildCounter]`:
- **Active / Total Child Telemetry:** See exactly how many children exist and how many are currently active (e.g., spawned vs unspawned).
- **Direct vs Recursive Modes:** Count immediate children or full subtree descendants across all nested depths.
- **Empty Group Alerts:** Flashes a red warning badge when an object expected to have children is empty (`WarnIfEmpty = true`).
- **Custom Badge Formatting:** Customize background colors, text colors, and format strings (e.g. `"{active} Active"`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyChildCounter]
public class WaypointGroup : MonoBehaviour
{
    public bool isLooping = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyChildCounterRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyChildCounterAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Recursive` | `bool` | `false` | Whether to count descendants recursively through all nested child branches. |
| `OnlyIfChildrenExist` | `bool` | `true` | Whether to hide the badge when the GameObject has zero children. |
| `Format` | `string` | `"{active}/{total}"` | Text format string with placeholders `{active}` and `{total}`. |
| `BadgeColor` | `string` | `"#2C3A47"` | Hex background color of the child counter badge. |
| `TextColor` | `string` | `"#CAD3C8"` | Hex text color of the counter numbers. |
| `EmptyWarningColor` | `string` | `"#E71C23"` | Hex warning badge color when the GameObject has no children and `WarnIfEmpty` is true. |
| `WarnIfEmpty` | `bool` | `false` | Whether to display an alert badge when the child count is zero. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the child counter badge remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyChildCounter(
    Recursive = true, 
    Format = "Spawned: {active}/{total}", 
    BadgeColor = "#1E293B", 
    TextColor = "#38BDF8", 
    WarnIfEmpty = true, 
    EmptyWarningColor = "#DC2626", 
    XOffset = 6f)]
public class EnemySpawnPool : MonoBehaviour
{
    [Header("Pool Configuration")]
    public GameObject enemyPrefab;
    public int maxPoolSize = 30;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyFolder]`** | High | Place child counters on folder headers to see the total number of items organized within each folder. |
| **`[HierarchyBreadcrumb]`** | High | Use child counters on parents and breadcrumbs on children for complete two-way hierarchy awareness. |
| **`[HierarchyComponentCount]`** | Complementary | Use `HierarchyComponentCount` for attached components and `HierarchyChildCounter` for child GameObjects. |
| **Dynamic Spawning** | High | Accurately tracks children instantiated or destroyed at runtime in Play Mode. |
