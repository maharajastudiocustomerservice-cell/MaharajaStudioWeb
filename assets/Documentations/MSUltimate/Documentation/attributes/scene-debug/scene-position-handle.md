# [ScenePositionHandle]

> Renders an interactive 3D translation gizmo in the Scene view to directly drag, manipulate, and assign Vector3 or Vector2 coordinates with live Undo support and grid snapping.

---

## 1. Overview & Value Proposition

**What it does:**
Renders a full 3D interactive translation handle (`Handles.PositionHandle`) directly in the Scene view attached to any `Vector3` or `Vector2` field. Allows developers to drag the position directly in the 3D viewport, automatically serializing and writing the changes back to the component with full Undo support.

**The Problem:**
Placing offset targets, spawn positions, interaction anchors, or look-at targets by manually typing numbers into `Vector3 (x, y, z)` fields in the Inspector is tedious, trial-and-error work that disrupts level design workflow.

**The Solution:**
Add `[ScenePositionHandle]` to any position vector:
- **Direct Viewport Manipulation:** Drag vectors directly in 3D space using standard XYZ axis handles.
- **Guide Line to Origin:** Renders a visual guide line (`DrawLineToOrigin = true`) from the handle back to the object's origin.
- **Grid Snapping:** Configure grid snapping increments (`Snap = 0.5f`) for clean unit alignment.
- **Local / World Coordinates:** Toggle `LocalSpace = true` to manipulate coordinates relative to the object's transform rotation and scale.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class TurretTargeting : MonoBehaviour
{
    [ScenePositionHandle("Target Point", "#FFAA00", LocalSpace = true)]
    public Vector3 targetOffset = new Vector3(0f, 2f, 10f);
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Vector3`, `Vector2`, `Transform` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `SceneDebugGizmoDrawer` (Scene View) & `SceneGizmoFieldToggle` (Inspector) |

---

## 4. Constructors & Parameters

```csharp
public ScenePositionHandleAttribute()
public ScenePositionHandleAttribute(string label)
public ScenePositionHandleAttribute(string label, string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `string` | `""` | Label text displayed near the translation gizmo. |
| `colorHex` | `string` | `"#FFAA00"` | Hex color code for the guide line and handle cap disc. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | `""` | Optional label displayed at the handle position. |
| `ColorHex` | `string` | `"#FFAA00"` | Hex color for connecting line and cap visualization. |
| `LocalSpace` | `bool` | `false` | If true, manipulates position in local space relative to the GameObject. |
| `Snap` | `float` | `0f` | Grid snap increment for position movement (`0` = smooth movement). |
| `OnlyWhenSelected` | `bool` | `true` | Only display handles when the GameObject is selected in the hierarchy. |
| `DrawLineToOrigin` | `bool` | `true` | Draws a guide line connecting the handle position back to the object's transform origin. |
| `CapSize` | `float` | `0.25f` | Size scaling of the handle cap disc. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class WeaponAttachmentPoint : MonoBehaviour
{
    [Header("Muzzle Flash Spawn Position")]
    [ScenePositionHandle("Muzzle Pivot", "#e67e22", LocalSpace = true, Snap = 0.1f)]
    public Vector3 muzzleOffset = new Vector3(0f, 0.2f, 1.5f);

    [Header("Shell Ejection Point")]
    [ScenePositionHandle("Ejector Pivot", "#f1c40f", LocalSpace = true)]
    public Vector3 ejectorOffset = new Vector3(0.2f, 0.1f, -0.3f);
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| `[SceneLabel]` | Supported | Pair with `[SceneLabel]` to show floating coordinate or state readouts directly beside the handle. |
| `ICollectionElement` | Supported | Renders individual translation gizmos for each point inside lists or arrays. |
