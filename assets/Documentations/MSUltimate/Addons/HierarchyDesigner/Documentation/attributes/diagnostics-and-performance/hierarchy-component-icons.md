# [HierarchyComponentIcons]

> Renders a horizontal strip of mini component icons directly on the hierarchy row with type tooltips.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyComponentIcons]` scans all components attached to a GameObject and renders a compact horizontal strip of mini native Unity component icons (`IconSize = 12f`, `Spacing = 2f`) on the hierarchy row. Driven by `HierarchyComponentIconsRenderer`, it queries `EditorGUIUtility.ObjectContent(comp, comp.GetType())` to resolve accurate Unity editor icons (e.g., BoxCollider, Rigidbody, NavMeshAgent, Light, AudioSource, Animator), ignoring redundant Transform components and capping display count at `MaxIcons` (default 5). Hovering over any icon reveals a tooltip showing the exact component class name.

**The Problem:**
In dense scene hierarchies, determining what components are attached to a GameObject requires selecting each entity one by one and scrolling through the Inspector. Developers frequently misplace colliders, miss unassigned animators, or forget whether an object has a Rigidbody, resulting in tedious manual audits.

**The Solution:**
Decorating components with `[HierarchyComponentIcons]`:
- **Immediate Architectural Inspection:** See all functional components attached to an entity at a glance in the Hierarchy.
- **Accurate Unity Native Iconography:** Uses official icons matched by Unity EditorGUIUtility for instant visual recognition.
- **Hover Inspection Tooltips:** Hover over any icon to verify the exact type name without opening foldouts.
- **Configurable Caps & Spacing:** Keep hierarchy rows clean and uncluttered by bounding icon count (`MaxIcons`) and adjusting padding.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyComponentIcons(MaxIcons = 4, IconSize = 12f)]
public class CharacterEntity : MonoBehaviour
{
    public float movementSpeed = 6.0f;
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
| **Render Engine** | `HierarchyComponentIconsRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyComponentIconsAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxIcons` | `int` | `5` | Maximum number of attached component icons to render in the strip. |
| `IconSize` | `float` | `12f` | Width and height in pixels of each rendered component icon. |
| `Spacing` | `float` | `2f` | Spacing in pixels between adjacent component icons. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the component icon strip remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[RequireComponent(typeof(Rigidbody), typeof(CapsuleCollider), typeof(AudioSource))]
[HierarchyComponentIcons(
    MaxIcons = 6, 
    IconSize = 13f, 
    Spacing = 3f, 
    XOffset = 6f)]
public class PhysicalProp : MonoBehaviour
{
    [Header("Prop Physics")]
    public float massKg = 45f;
    public bool breakable = true;
    public float impactThreshold = 12f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyComponentCount]`** | High | Use `HierarchyComponentCount` for a numerical badge counter and `HierarchyComponentIcons` for visual type icons. |
| **`[HierarchyActiveButton]`** | High | Place active buttons on the far right while the component icon strip sits beside it. |
| **Automatic Transform Filter** | Built-in | Always excludes the standard `Transform` or `RectTransform` component to prevent unnecessary visual noise. |
| **Custom Script Icons** | High | Custom MonoBehaviours with custom script icons configured in Unity will display their assigned icons. |
