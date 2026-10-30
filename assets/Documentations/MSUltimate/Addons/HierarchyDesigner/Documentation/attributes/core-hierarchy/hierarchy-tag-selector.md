# [HierarchyTagSelector]

> Draws an interactive tag selector dropdown directly on the hierarchy row to modify GameObject tags with one click.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyTagSelector]` attaches to MonoBehaviour classes and renders a clickable tag badge directly on the hierarchy row. Driven by `HierarchyTagSelectorRenderer`, clicking the badge opens a native Unity `GenericMenu` populated with all project tags defined in `UnityEditorInternal.InternalEditorUtility.tags`. Selecting a new tag assigns `go.tag`, logs full Unity Undo operations (`Undo.RegisterCompleteObjectUndo`), and marks the scene dirty. It supports auto-hiding for untagged objects (`HideUntagged = true`) and fully customizable badge colors and borders.

**The Problem:**
Tagging GameObjects (e.g. `Player`, `Enemy`, `MainCamera`, `Finish`, `Hazard`) is essential for collision detection, AI perception, and camera framing. However, Unity requires selecting each object, moving to the Inspector, clicking the Tag dropdown, selecting the item, and repeating for every entity. Untagged mistakes are common and hard to spot until gameplay logic fails.

**The Solution:**
Decorating components with `[HierarchyTagSelector]`:
- **Instant Dropdown Picker:** Click directly on the hierarchy row to open a full popup menu of all project tags.
- **Fast Scene Auditing:** Immediately see which tag is assigned to each entity without selecting it.
- **Optional Clean Defaults:** Hide the badge when the object is `Untagged` to keep standard objects visual noise-free.
- **Full Undo Registration:** Supports standard `Ctrl+Z` rollbacks during Edit Mode editing sessions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTagSelector(BadgeColor = "#1E293B", TextColor = "#38BDF8")]
public class CombatTarget : MonoBehaviour
{
    public float targetPriority = 1.0f;
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
| **Render Engine** | `HierarchyTagSelectorRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyTagSelectorAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HideUntagged` | `bool` | `false` | Hides the widget when the GameObject's current tag is `Untagged`. |
| `BadgeColor` | `string` | `"#1E2D3D"` | Hex background color of the tag badge container. |
| `TextColor` | `string` | `"#7EB8D4"` | Hex color of the tag label text. |
| `BorderRadius` | `float` | `3f` | Corner radius of the tag badge in pixels. |
| `Width` | `float` | `70f` | Total width of the tag selector widget in pixels. |
| `Height` | `float` | `0f` | Height of the widget in pixels, or `0` for row-adjusted height (capped at 16px). |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `UndoLabel` | `string` | `"Change Tag"` | Undo transaction description registered in Edit Mode. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the tag selector remains visible and interactive in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyTagSelector(
    HideUntagged = false, 
    BadgeColor = "#1E1B4B", 
    TextColor = "#A5B4FC", 
    BorderRadius = 4f, 
    Width = 80f, 
    XOffset = 6f)]
public class SpawnableObstacle : MonoBehaviour
{
    [Header("Obstacle Properties")]
    public float damageOnImpact = 25f;
    public bool isDestructible = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyLayerSelector]`** | High | Combine with layer selector widgets for simultaneous tag and layer management in the hierarchy. |
| **`[HierarchyLayerTag]`** | High | Use `HierarchyTagSelector` for interactive tags and `HierarchyLayerTag` for layer labels. |
| **`[HierarchyHighlight]`** | High | Background highlights frame the tag badge clearly without visual conflict. |
| **Project Tags** | High | Automatically syncs with Unity's Project Tags settings; no manual string typing required. |
