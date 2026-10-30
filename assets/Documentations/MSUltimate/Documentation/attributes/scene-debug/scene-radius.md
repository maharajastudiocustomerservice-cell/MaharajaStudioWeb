# [SceneRadius]

> Renders interactive spherical, circular, or hemispherical radius visualizations in the Scene view for numeric range and distance fields with interactive drag handles.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an in-scene 3D or 2D radial boundary (sphere, circle disc, or hemisphere) directly around the GameObject representing numeric range, detection radius, explosion blast area, or sound falloff. Supports solid transparent face fills, wireframe circumference rings, segment customization, and interactive radial resize handles (`Editable = true`).

**The Problem:**
Tuning combat radii like melee attack ranges, aggro spheres, or audio attenuation ranges requires guessing floating-point numbers in the Inspector without immediate visual spatial feedback in the Scene camera.

**The Solution:**
Add `[SceneRadius]` to any numeric float or integer field:
- **Instant Radial Visualization:** See effective radii directly in the Scene view in real time.
- **Multiple Draw Modes:** Toggle between `Circle` (ground disc), `Sphere` (full 3D volume), and `Hemisphere` (dome/ceiling).
- **Interactive Drag Resizing:** Enable `Editable = true` to click and drag radius handles in the Scene view with live Undo.
- **Inspector Eye Toggle:** Includes a 1-click eye button beside the field in the Inspector to show or hide the gizmo.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class ExplosiveBarrel : MonoBehaviour
{
    [SceneRadius("#FF3300", DrawMode = SceneRadiusMode.Sphere, Editable = true, Label = "Blast Radius")]
    public float explosionRadius = 5.0f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `double`, `Vector3`, `Vector2` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SceneRadiusAttribute()
public SceneRadiusAttribute(string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#00FF00"` | Hex color code used for the circle, disc, or sphere visualization. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#00FF00"` | Hex color of the radius gizmo. |
| `FillAlpha` | `float` | `0.1f` | Alpha transparency for filled disc/sphere faces (`0` for wireframe). |
| `Segments` | `int` | `32` | Number of wireframe segments used to draw circles. |
| `DrawMode` | `SceneRadiusMode` | `SceneRadiusMode.Circle` | Shape mode: `Sphere`, `Circle`, or `Hemisphere`. |
| `ShowValue` | `bool` | `true` | Displays numeric radius value label above the shape. |
| `Label` | `string` | `""` | Custom text label displayed at the radius center. |
| `OnlyWhenSelected` | `bool` | `false` | Only renders when the GameObject is selected in the hierarchy. |
| `Editable` | `bool` | `false` | Renders interactive radius slider handles when selected for direct resizing. |
| `MinRadius` | `float` | `0.01f` | Minimum clamp limit for the radius drag handles. |
| `MaxRadius` | `float` | `float.MaxValue` | Maximum clamp limit for the radius drag handles. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class TurretDefenseZone : MonoBehaviour
{
    [Header("Targeting Outer Radius")]
    [SceneRadius("#00FF88", 
        DrawMode = SceneRadiusMode.Circle, 
        FillAlpha = 0.15f, 
        Editable = true, 
        Label = "Detection Range"
    )]
    public float detectionRange = 15f;

    [Header("Effective Minimum Range (Blind Spot)")]
    [SceneRadius("#FF4444", 
        DrawMode = SceneRadiusMode.Circle, 
        Editable = true, 
        Label = "Dead Zone"
    )]
    public float minRange = 3f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| Multiple Allowed | Supported | Stack multiple `[SceneRadius]` attributes on different fields to visualize nested ranges (e.g. inner vs outer aggro). |
| `ICollectionElement` | Supported | Renders radius visualizations for arrays or lists of numeric ranges. |
