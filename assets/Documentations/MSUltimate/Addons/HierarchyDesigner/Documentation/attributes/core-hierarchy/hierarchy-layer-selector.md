# [HierarchyLayerSelector]

> Draws an interactive layer selector widget directly on the hierarchy row to audit and reassign GameObject layers without opening the Inspector.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyLayerSelector]` brings direct layer auditing and switching right into the scene hierarchy. Managed by `HierarchyLayerSelectorRenderer`, it displays a compact layer badge widget (`Width = 70f`, `BadgeColor = "#1A2E1F"`, `TextColor = "#7EC89A"`) displaying the GameObject's current layer name. Clicking the widget opens Unity's layer selection popup menu, allowing instant reassignment. Developers can optionally hide the badge when the object is on the `Default` layer (`HideDefault = true`) to minimize clutter, and choose whether layer changes recursively apply to children (`ApplyToChildren = true`).

**The Problem:**
Layer mismatches are a leading cause of physics raycast failures, camera culling glitches, post-processing volume errors, and UI event blocking. Finding which entities are assigned to `Ignore Raycast`, `PostProcessing`, `Water`, or `UI` layers requires clicking through every object in the hierarchy and checking the top-right Inspector dropdown.

**The Solution:**
Decorating physics, camera, and lighting components with `[HierarchyLayerSelector]`:
- **At-a-Glance Layer Auditing:** Scan your hierarchy tree to immediately see which layer each entity belongs to.
- **Single-Click Layer Reassignment:** Click the badge to open the native layer popup menu and switch layers instantly.
- **Recursive Child Support:** Optionally propagate layer changes down entire child hierarchies (`ApplyToChildren = true`).
- **De-clutter with HideDefault:** Keep your hierarchy tidy by hiding the badge on standard unspecialized objects (`HideDefault = true`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyLayerSelector(Width = 75f, HideDefault = true)]
public class RaycastHitTarget : MonoBehaviour
{
    public float surfaceArmor = 50f;
    public bool isPenetrable = false;
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
| **Render Engine** | `HierarchyLayerSelectorRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyLayerSelectorAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HideDefault` | `bool` | `false` | When true, suppresses rendering when the GameObject is assigned to the `Default` layer. |
| `ApplyToChildren` | `bool` | `false` | When true, layer modifications recursively apply to all child GameObjects. |
| `BadgeColor` | `string` | `"#1A2E1F"` | Hex background color of the layer selector widget. |
| `TextColor` | `string` | `"#7EC89A"` | Hex text color of the active layer name. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels for the widget pill. |
| `Width` | `float` | `70f` | Width in pixels allocated to the layer badge widget. |
| `Height` | `float` | `0f` | Widget height in pixels, or `0f` to auto-match row height. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin. |
| `UndoLabel` | `string` | `"Change Layer"` | Transaction description registered with Unity Undo. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the layer selector widget remains active in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyLayerSelector(
    Width = 85f, 
    HideDefault = false, 
    ApplyToChildren = true, 
    BadgeColor = "#14532D", 
    TextColor = "#86EFAC", 
    XOffset = 6f)]
public class PostProcessVolumeTrigger : MonoBehaviour
{
    [Header("Volume Configuration")]
    public float blendDistanceMeters = 5.0f;
    public float volumeWeight = 1.0f;
    public bool isGlobalVolume = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyActiveButton]`**| High | Position the layer selector widget to the left of the power button using `XOffset = 26f`. |
| **`[HierarchyTagSelector]`** | High | Pairs naturally with tag selectors to manage both Tag and Layer directly in the hierarchy. |
| **Undo Stack** | High | Changes register with `Undo.RecordObject` and mark scenes dirty for seamless saving. |
| **Multi-Selection** | High | Changing the layer via the widget applies to the targeted GameObject cleanly without disrupting current selection. |
