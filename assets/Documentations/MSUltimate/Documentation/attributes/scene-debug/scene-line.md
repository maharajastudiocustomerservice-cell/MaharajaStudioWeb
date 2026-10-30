# [SceneLine]

> Renders connected line paths and waypoint routes in the Scene view for point collections with closed-loop toggling, distance measurements, and interactive vertex drag handles.

---

## 1. Overview & Value Proposition

**What it does:**
Renders connected 3D lines and path segments directly in the Scene view for collections of `Vector3`, `Vector2`, or `Transform` objects. Supports custom line thickness, dashed styling, closed loops, vertex dots, segment distance readouts, and interactive vertex dragging (`Editable = true`).

**The Problem:**
Authoring patrol paths, camera rails, or boundary polygons by manually inputting coordinate lists into Inspector arrays is blind work, forcing developers to rely on guessing coordinates without seeing the actual route in context.

**The Solution:**
Add `[SceneLine]` to any waypoint collection or vector array:
- **Spatial Path Visualization:** Instantly visualizes the entire path connecting waypoints in the Scene view.
- **Interactive Waypoint Handles:** With `Editable = true`, drag individual path vertices directly inside the Scene view with live Undo.
- **Distance & Loop Support:** Measure distances between waypoints (`ShowDistances = true`) and create closed patrol loops (`ClosedLoop = true`).
- **Local / World Space:** Switch between absolute world coordinates and local transform-relative offsets (`LocalSpace = true`).

---

## 2. Quick Start

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class PatrolRoute : MonoBehaviour
{
    [SceneLine("#FFFF00", Editable = true, ClosedLoop = true, ShowDistances = true)]
    public List<Vector3> waypoints = new List<Vector3>
    {
        new Vector3(0, 0, 0),
        new Vector3(5, 0, 0),
        new Vector3(5, 0, 5),
        new Vector3(0, 0, 5)
    };
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `List<Vector3>`, `Vector3[]`, `List<Vector2>`, `Vector2[]`, `Transform[]`, `List<Transform>` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `SceneDebugGizmoDrawer` (Scene View) & `SceneGizmoFieldToggle` (Inspector) |

---

## 4. Constructors & Parameters

```csharp
public SceneLineAttribute()
public SceneLineAttribute(string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#FFFF00"` | Hex color code used for drawing the line segments and vertex spheres. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#FFFF00"` | Hex color of the path line. |
| `Thickness` | `float` | `2.0f` | Line thickness in pixels. |
| `DashLength` | `float` | `0f` | Dash spacing for dotted/dashed lines (`0` for solid line). |
| `ClosedLoop` | `bool` | `false` | Connects the last waypoint back to the first. |
| `ShowVertexDots` | `bool` | `true` | Renders small spheres at each path vertex. |
| `VertexDotSize` | `float` | `0.1f` | Radius of the vertex indicator spheres. |
| `ShowDistances` | `bool` | `false` | Displays segment distance measurement labels along each line segment. |
| `Label` | `string` | `""` | Custom descriptive label displayed along the path. |
| `OnlyWhenSelected` | `bool` | `false` | Only renders when the GameObject is selected in the hierarchy. |
| `Editable` | `bool` | `false` | Renders interactive drag handles at each waypoint to reshape the path directly in the Scene view. |
| `LocalSpace` | `bool` | `false` | Treats point coordinates relative to the object's transform instead of world space. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class CameraRailPath : MonoBehaviour
{
    [Header("Cinematic Camera Rail (Interactive Drag Vertices)")]
    [SceneLine("#9b59b6", 
        Thickness = 3f, 
        ClosedLoop = false, 
        ShowDistances = true, 
        Editable = true, 
        LocalSpace = true,
        Label = "Camera Track"
    )]
    public List<Vector3> cameraTrackPoints = new List<Vector3>
    {
        new Vector3(0, 2, 0),
        new Vector3(10, 4, 15),
        new Vector3(20, 6, 30)
    };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| Multiple Allowed | Supported | Stack multiple `[SceneLine]` tags to draw multiple connected routes (e.g., ground route vs air route). |
| Collection Integration | Supported | Fully compatible with lists and arrays; handles dynamically re-evaluate upon adding or removing items. |
