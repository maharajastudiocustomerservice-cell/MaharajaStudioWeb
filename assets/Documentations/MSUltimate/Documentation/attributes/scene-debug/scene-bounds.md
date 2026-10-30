# [SceneBounds]

> Renders interactive 3D bounding box visualizations in the Scene view for Bounds, Rect, Vector3 extents, or Colliders with dimension readouts and interactive face drag handles.

---

## 1. Overview & Value Proposition

**What it does:**
Renders a 3D bounding volume directly in the Scene view representing a `Bounds`, `BoundsInt`, `Vector3` extent, or attached `Collider`. Features solid transparent face shading, wireframe boundary outlines, center crosshairs, dimension readouts (width × height × depth), and optional interactive resize handles (`Editable = true`) allowing developers to drag bounding faces directly in the Scene view.

**The Problem:**
Tweaking volume triggers, patrol areas, or collision bounding boxes via numeric `Vector3` center/size fields in the Inspector is cumbersome and disconnected from the spatial scene context.

**The Solution:**
Decorate any bounds or collider field with `[SceneBounds]`:
- **Immediate Spatial Awareness:** Instantly visualizes bounding box boundaries in real time.
- **Interactive Drag Resizing:** Set `Editable = true` to drag boundary faces directly in the Scene view with live Undo.
- **Dimensions & Center Mark:** Displays live dimension measurements and a center point crosshair.
- **Inspector Eye Toggle:** Includes a 1-click eye button beside the field in the Inspector to show or hide the gizmo at will.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class SpawnZone : MonoBehaviour
{
    [SceneBounds("#00FFFF", Editable = true, ShowDimensions = true, Label = "Spawn Area")]
    public Bounds spawnArea = new Bounds(Vector3.zero, new Vector3(10f, 4f, 10f));
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Bounds`, `BoundsInt`, `Vector3`, `Collider` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `SceneDebugGizmoDrawer` (Scene View) & `SceneGizmoFieldToggle` (Inspector) |

---

## 4. Constructors & Parameters

```csharp
public SceneBoundsAttribute()
public SceneBoundsAttribute(string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#00FFFF"` | Hex color code used for the bounding box faces and edges. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#00FFFF"` | Hex color of the bounding box lines and faces. |
| `FillAlpha` | `float` | `0.2f` | Alpha transparency for filled faces (`0` for wireframe only). |
| `ShowDimensions` | `bool` | `true` | Displays dimension text (`W × H × D`) above the bounding volume. |
| `ShowCenter` | `bool` | `true` | Draws a crosshair mark at the exact center of the bounding box. |
| `Label` | `string` | `""` | Custom label text displayed above the bounds. |
| `OnlyWhenSelected` | `bool` | `false` | Only renders when the GameObject is selected in the hierarchy. |
| `WireframeOnly` | `bool` | `false` | If true, suppresses solid face fill and renders wireframe edges only. |
| `Editable` | `bool` | `false` | Enables interactive face handles in the Scene view to resize the box by dragging. |
| `HandleColorHex` | `string` | `"#FFFFFF"` | Hex color of the interactive resize drag handles. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class AreaTriggerVolume : MonoBehaviour
{
    [Header("Interactive Patrol Boundary")]
    [SceneBounds("#2ecc71", 
        FillAlpha = 0.25f, 
        ShowDimensions = true, 
        ShowCenter = true, 
        Editable = true, 
        Label = "Patrol Bounds"
    )]
    public Bounds patrolBounds = new Bounds(Vector3.zero, new Vector3(20f, 5f, 20f));

    [Header("Restricted Zone (Wireframe Only)")]
    [SceneBounds("#e74c3c", WireframeOnly = true, Label = "Danger Zone")]
    public Bounds restrictedArea = new Bounds(new Vector3(0f, 0f, 10f), new Vector3(5f, 5f, 5f));
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders seamlessly inside group cards. |
| Multiple Allowed | Supported | Apply multiple `[SceneBounds]` tags to visualize different volumes on one component. |
| `ICollectionElement` | Supported | Renders bounding boxes for elements in `List<Bounds>` or `Bounds[]` collections. |
