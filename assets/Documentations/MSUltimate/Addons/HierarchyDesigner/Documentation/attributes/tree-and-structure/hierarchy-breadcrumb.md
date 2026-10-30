# [HierarchyBreadcrumb]

> Displays a compact ancestor hierarchy path breadcrumb next to the GameObject name.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyBreadcrumb]` traces the GameObject's parent hierarchy tree upwards and displays a compact ancestor breadcrumb trail (e.g. `Environment › Sector_A › Lights ›`) directly on the right side of the hierarchy row. Driven by `HierarchyBreadcrumbRenderer`, it formats ancestor names with a custom delimiter (`Delimiter = " › "`), limits traversal up to `MaxDepth` (default 3), and renders the path in subtle slate typography (`TextColor = "#718093"`).

**The Problem:**
In deeply nested scene trees (prefabs within prefabs, complex bone armatures, UI canvas hierarchies), finding out where an entity lives within the parent structure requires scrolling up to look for parent folder nodes or checking the Inspector's breadcrumb bar. When multiple objects share identical names (e.g., several objects named `Light`, `Collider`, or `Anchor`), confusion is common.

**The Solution:**
Decorating nested components with `[HierarchyBreadcrumb]`:
- **Contextual Parent Awareness:** See parent and grandparent container names at a glance without collapsing branches.
- **Disambiguate Identical Names:** Immediately tell apart identically named objects based on their parent path.
- **Configurable Ancestor Depth:** Cap depth (`MaxDepth = 3`) to keep breadcrumbs concise and uncluttered.
- **Custom Delimiters & Colors:** Choose symbols like `" › "`, `" / "`, or `" → "` with custom text colors.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBreadcrumb(MaxDepth = 2, Delimiter = " / ")]
public class PropDetailFixture : MonoBehaviour
{
    public int lodLevel = 0;
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
| **Render Engine** | `HierarchyBreadcrumbRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyBreadcrumbAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxDepth` | `int` | `3` | Maximum number of ancestor hierarchy levels to display. |
| `Delimiter` | `string` | `" › "` | Delimiter string separating ancestor names. |
| `TextColor` | `string` | `"#718093"` | Hex text color of the breadcrumb path label. |
| `ShowRoot` | `bool` | `true` | Whether to include the scene root GameObject in the breadcrumb path. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the breadcrumb path remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyBreadcrumb(
    MaxDepth = 3, 
    Delimiter = " › ", 
    TextColor = "#94A3B8", 
    XOffset = 6f)]
public class NestedUiWidget : MonoBehaviour
{
    [Header("UI Element")]
    public string widgetId = "BTN_CONFIRM_DIALOG";
    public bool isInteractable = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyChildCounter]`** | High | Use breadcrumbs on deeply nested children and child counters on top-level parent containers. |
| **`[HierarchyFolder]`** | High | Works alongside hierarchy folder headers to make organizational paths instantly readable. |
| **Root Objects** | High | Gracefully renders nothing if the GameObject has no parent (is already at root level). |
| **Repaint Hook** | High | Re-evaluates parent transform references during repaint; updates dynamically if reparented. |
