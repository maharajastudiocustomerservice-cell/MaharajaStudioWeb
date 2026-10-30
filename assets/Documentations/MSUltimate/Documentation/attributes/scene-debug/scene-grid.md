# [SceneGrid]

> Renders a customizable reference coordinate grid in the Scene view on any cardinal plane (XZ, XY, YZ) for level editing, tile alignment, and spatial measurements.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an interactive reference ground or wall grid directly in the Scene view centered on the GameObject or origin. Supports custom cell sizes, grid dimensions, plane orientation (`XZ`, `XY`, `YZ`), axis highlight colors, and center anchoring.

**The Problem:**
Placing props, aligning modular level pieces, configuring tilemaps, or verifying character spawn spacing against world measurements requires guessing distances or relying on Unity's global Scene grid, which is locked to world origin and cannot easily follow individual objects or orient along custom axes.

**The Solution:**
Add `[SceneGrid]` to any transform, vector, or numeric field:
- **Object-Centric Grid:** The grid moves and anchors directly to the decorated object's position.
- **Multi-Plane Alignment:** Switch effortlessly between horizontal ground (`XZ`), 2D/vertical wall (`XY`), or side profile (`YZ`) planes.
- **Configurable Spacing:** Set exact `CellSize`, `GridWidth`, and `GridDepth` to match level tiles or modular asset footprints.
- **Origin Axis Highlighting:** Highlights primary center axes for rapid visual alignment.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class LevelBuilder : MonoBehaviour
{
    [SceneGrid("#3498db", CellSize = 2f, GridWidth = 10, GridDepth = 10, Plane = SceneGridPlane.XZ)]
    public Vector3 placementCenter = Vector3.zero;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Vector3`, `Vector2`, `int`, `float`, `Transform` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `SceneDebugGizmoDrawer` (Scene View) & `SceneGizmoFieldToggle` (Inspector) |

---

## 4. Constructors & Parameters

```csharp
public SceneGridAttribute()
public SceneGridAttribute(string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `"#555555"` | Hex color code used for the grid lines. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#555555"` | Hex color of the grid lines. |
| `CellSize` | `float` | `1.0f` | Size of each grid cell in world units. |
| `GridWidth` | `int` | `10` | Number of cells along the primary axis. |
| `GridDepth` | `int` | `10` | Number of cells along the secondary axis. |
| `ShowAxes` | `bool` | `true` | Whether to draw highlighted center origin axes. |
| `AxesColorHex` | `string` | `"#FFFFFF"` | Hex color for the center origin axes. |
| `Plane` | `SceneGridPlane` | `SceneGridPlane.XZ` | Orientation plane of the grid (`XZ`, `XY`, or `YZ`). |
| `CenterOnObject` | `bool` | `true` | If true, centers the grid on the object transform rather than starting from origin. |
| `Label` | `string` | `""` | Optional descriptive label displayed at the grid origin. |
| `OnlyWhenSelected` | `bool` | `false` | Only renders when the GameObject is selected in the hierarchy. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class ModularBuildingSystem : MonoBehaviour
{
    [Header("Foundation Ground Grid (XZ)")]
    [SceneGrid("#4a90e2", 
        CellSize = 4f, 
        GridWidth = 12, 
        GridDepth = 12, 
        Plane = SceneGridPlane.XZ, 
        ShowAxes = true, 
        Label = "Foundation Grid"
    )]
    public Vector3 buildingPivot = Vector3.zero;

    [Header("Elevation Wall Grid (XY)")]
    [SceneGrid("#2ecc71", 
        CellSize = 2f, 
        GridWidth = 8, 
        GridDepth = 6, 
        Plane = SceneGridPlane.XY, 
        OnlyWhenSelected = true,
        Label = "Façade Grid"
    )]
    public Vector3 wallOffset = new Vector3(0f, 0f, 0f);
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| `[ScenePositionHandle]` | Supported | Combine with `[ScenePositionHandle]` to move the grid anchor point interactively. |
| Multiple Allowed | Supported | Stack multiple `[SceneGrid]` attributes to render perpendicular reference planes (e.g., floor + wall). |
