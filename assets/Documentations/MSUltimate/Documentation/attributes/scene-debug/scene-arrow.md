# [SceneArrow]

> Renders interactive directional 3D arrows in the Scene view to visualize heading vectors, velocities, and ray directions with draggable tip handles.

---

## 1. Overview & Value Proposition

**What it does:**
Draws a 3D directional arrow directly in the Unity Scene view representing a `Vector3` direction, velocity, or `Transform` orientation. Features live magnitude readouts, solid/dashed/double styling, and an optional draggable tip handle (`Editable = true`) to aim the vector directly inside the Scene view with live Undo.

**The Problem:**
Tweaking directional vectors (like wind direction, projectile launch angles, or raycast offsets) by typing `(x, y, z)` values in the Inspector requires guessing angles and repeatedly testing play mode to verify direction.

**The Solution:**
Add `[SceneArrow]` to any vector or transform field:
- **Instant 3D Visualization:** See vectors immediately in world or local space in the Scene view.
- **Interactive Drag Handle:** Enable `Editable = true` to click and drag the arrow tip directly in SceneView.
- **Length & Magnitude Display:** Live distance/magnitude label displayed alongside the arrow shaft.
- **Inspector Visibility Toggle:** Includes a 1-click eye button beside the field in the Inspector to show or hide the gizmo.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class TurretAim : MonoBehaviour
{
    [SceneArrow("#00FF88", Editable = true, ShowMagnitude = true)]
    public Vector3 fireDirection = Vector3.forward * 5f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Vector3`, `Quaternion`, `Transform`, `Rigidbody` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `SceneDebugGizmoDrawer` (Scene View) & `SceneGizmoFieldToggle` (Inspector) |

---

## 4. Constructors & Parameters

```csharp
public SceneArrowAttribute()
public SceneArrowAttribute(string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#FF00FF"` | Hex color code for the arrow shaft and cone. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#FF00FF"` | Hex color for the arrow. |
| `ArrowHeadSize` | `float` | `0.2f` | Size scaling of the arrow cone tip. |
| `Thickness` | `float` | `2.0f` | Line thickness of the arrow shaft. |
| `Length` | `float` | `1.0f` | Fixed length or length multiplier for the arrow. |
| `Normalize` | `bool` | `false` | Normalizes the vector before drawing. |
| `ShowMagnitude` | `bool` | `true` | Displays floating text readout showing vector magnitude. |
| `Label` | `string` | `""` | Custom descriptive label displayed next to the arrow. |
| `OnlyWhenSelected` | `bool` | `false` | Only renders when the GameObject is selected in hierarchy. |
| `ArrowStyle` | `SceneArrowStyle`| `SceneArrowStyle.Solid` | Line style (`Solid`, `Dashed`, `Double`). |
| `Editable` | `bool` | `false` | Renders a draggable move handle at the arrow tip. |
| `LockLength` | `bool` | `false` | Preserves original length when dragging the tip handle. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class ProjectileLauncher : MonoBehaviour
{
    [Header("Launch Velocity Vector (Draggable Tip Handle)")]
    [SceneArrow("#3498db", 
        ArrowStyle = SceneArrowStyle.Solid, 
        Thickness = 3f, 
        ShowMagnitude = true, 
        Editable = true, 
        Label = "Launch Velocity"
    )]
    public Vector3 launchVelocity = new Vector3(0f, 8f, 15f);

    [Header("Wind Drift Force")]
    [SceneArrow("#f39c12", ArrowStyle = SceneArrowStyle.Dashed, Thickness = 2f)]
    public Vector3 environmentalWind = new Vector3(2f, 0f, 0f);
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| Multiple Allowed | Supported | Apply multiple `[SceneArrow]` tags to visualize multiple directional vectors. |
| `ICollectionElement` | Supported | Renders arrows for all vectors inside `List<Vector3>` collections. |
