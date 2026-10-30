# [SceneRotationHandle]

> Renders an interactive 3D rotation gizmo (Handles.RotationHandle) in the Scene view to directly rotate Quaternion or Vector3 Euler fields with live Undo support.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an interactive spherical 3-axis rotation gizmo directly in the Unity Scene view bound to a `Quaternion` or `Vector3` (Euler angles) field. Allows level designers and programmers to rotate spawn orientations, aim angles, or bone offsets visually using the mouse with full Undo/Redo integration.

**The Problem:**
Rotating objects or aim vectors by manually typing angle degrees into `(x, y, z)` fields in the Inspector involves guesswork and frequent gimble lock confusion, disrupting fluid level building.

**The Solution:**
Add `[SceneRotationHandle]` to any rotation vector or quaternion:
- **Interactive Scene Gizmo:** Drag standard rotation rings in the Scene view to orient values immediately.
- **Local / World Coordinates:** Support for local transform-relative orientation (`LocalSpace = true`) or absolute world coordinates.
- **Custom Pivot Offsets:** Offset handle position in 3D space (`OffsetX`, `OffsetY`, `OffsetZ`) to align with weapon barrels or character pivots.
- **Inspector Visibility Toggle:** Includes an eye button beside the field in the Inspector to show or hide the gizmo.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class TurretBase : MonoBehaviour
{
    [SceneRotationHandle("Turret Facing", "#00FFAA", LocalSpace = true)]
    public Vector3 initialEulerRotation = new Vector3(0f, 45f, 0f);
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Quaternion`, `Vector3` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SceneRotationHandleAttribute()
public SceneRotationHandleAttribute(string label)
public SceneRotationHandleAttribute(string label, string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `string` | `""` | Label text displayed near the rotation gizmo. |
| `colorHex` | `string` | `"#00FFAA"` | Hex color code for the rotation handle accent. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | `""` | Optional label displayed at the rotation handle. |
| `ColorHex` | `string` | `"#00FFAA"` | Hex color for the rotation handle visual feedback. |
| `LocalSpace` | `bool` | `true` | If true, rotates in local space relative to the GameObject transform. |
| `OnlyWhenSelected` | `bool` | `true` | Only display handle when the GameObject is selected in the hierarchy. |
| `OffsetX` | `float` | `0f` | Spatial offset along the X axis. |
| `OffsetY` | `float` | `0f` | Spatial offset along the Y axis. |
| `OffsetZ` | `float` | `0f` | Spatial offset along the Z axis. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class SearchLightController : MonoBehaviour
{
    [Header("Resting Light Orientation")]
    [SceneRotationHandle("Rest Angle", "#f1c40f", LocalSpace = true, OffsetY = 1.2f)]
    public Quaternion restingOrientation = Quaternion.identity;

    [Header("Patrol Sweep Limits")]
    [SceneRotationHandle("Max Sweep Euler", "#3498db", LocalSpace = true)]
    public Vector3 maxSweepAngle = new Vector3(0f, 90f, 0f);
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| `[ScenePositionHandle]` | Supported | Pair with `[ScenePositionHandle]` for simultaneous position and orientation editing. |
| `ICollectionElement` | Supported | Renders individual rotation handles for items in `List<Vector3>` or `Quaternion[]`. |
