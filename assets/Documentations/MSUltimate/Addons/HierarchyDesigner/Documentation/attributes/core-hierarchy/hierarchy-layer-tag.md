# [HierarchyLayerTag]

> Displays the GameObject's assigned Unity layer as a clean label or colored badge directly on the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyLayerTag]` reads the GameObject's current layer (`LayerMask.LayerToName(go.layer)`) and renders it directly on the right edge of the hierarchy row. Driven by `HierarchyLayerTagRenderer`, it can display the layer either as a subtle italicized text label (`ShowAsBadge = false`) or as a rounded pill badge (`ShowAsBadge = true`). It supports auto-hiding for standard default objects (`HideDefault = true`), custom color themes, font overrides, and text prefixes (e.g., `"L: "`).

**The Problem:**
In complex game scenes (physics colliders, raycast targets, camera culling zones, post-processing triggers, lighting layers), knowing which layer an object belongs to is critical. Without hierarchy visibility, developers must select each GameObject and check the small dropdown in the top-right corner of the Inspector, slowing down scene audits and leading to accidental layer mismatch bugs.

**The Solution:**
Decorating components with `[HierarchyLayerTag]`:
- **Instant Layer Awareness:** Immediately identify layer assignments (e.g. `PostProcessing`, `Ignore Raycast`, `Water`, `Enemy`) at a glance.
- **Uncluttered Defaults:** Automatically hides when the object is assigned to layer `0` (`Default`), keeping standard hierarchy items clean.
- **Dual Display Modes:** Choose between lightweight italic text or stylized rounded badges with distinct background colors.
- **Zero Reflection Overhead:** Directly queries Unity's native `go.layer` integer without inspecting component fields or reflection caches.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyLayerTag(ShowAsBadge = true, BadgeColor = "#1E293B", BadgeTextColor = "#38BDF8")]
public class CullingVolume : MonoBehaviour
{
    public float cullingDistance = 150f;
    public LayerMask affectedLayers;
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
| **Render Engine** | `HierarchyLayerTagRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyLayerTagAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HideDefault` | `bool` | `true` | Whether to hide the tag when the GameObject is assigned to the `Default` layer (`0`). |
| `ShowAsBadge` | `bool` | `false` | Whether to render the layer as a rounded pill badge rather than plain text. |
| `LabelColor` | `string` | `"#667788"` | Hex color of the text when displayed in plain text mode. |
| `Italic` | `bool` | `true` | Whether to render label text with italic styling. |
| `FontSize` | `int` | `0` | Font size override in pixels, or `0` for default editor font size. |
| `BadgeColor` | `string` | `"#223344"` | Background hex color of the badge container when `ShowAsBadge` is `true`. |
| `BadgeTextColor` | `string` | `"#88BBCC"` | Text hex color inside the badge container. |
| `BorderRadius` | `float` | `3f` | Corner radius in pixels for the badge box. |
| `Prefix` | `string` | `""` | Optional string prepended before the layer name (e.g. `"Layer: "`). |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the layer tag remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyLayerTag(
    ShowAsBadge = true, 
    BadgeColor = "#312E81", 
    BadgeTextColor = "#A5B4FC", 
    Prefix = "LAYER: ", 
    BorderRadius = 4f, 
    XOffset = 6f)]
public class PostProcessVolumeTrigger : MonoBehaviour
{
    [Header("Volume Configuration")]
    public float blendDistance = 5.0f;
    public float weight = 1.0f;
    public int priority = 10;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTagSelector]`** | High | Pair `HierarchyLayerTag` with `HierarchyTagSelector` for complete Unity tag and layer auditing. |
| **`[HierarchyIcon]`** | High | Use custom icons on the left side of the row while layer tags occupy the right edge. |
| **`[HierarchySeparator]`** | High | Separator banners organize sections while individual child items show their specific layers. |
| **`[HierarchyHighlight]`** | High | Highlight backgrounds contrast smoothly behind dark badge containers. |
