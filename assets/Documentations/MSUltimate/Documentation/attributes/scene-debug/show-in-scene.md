# [ShowInScene]

> Renders a 3D waypoint marker shape and text label at a position in the Scene view for Vector3, Vector2, and Transform fields with optional interactive translation handles.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an in-scene 3D waypoint marker (Sphere, Cube, Cross, Diamond, or built-in Unity icon) and floating label at any `Vector3`, `Vector2`, or `Transform` coordinate. Supports camera distance readouts, custom spatial offsets, and an interactive position handle (`Editable = true`) with grid snapping.

**The Problem:**
Keeping track of spawn locations, patrol targets, or object focal points in a complex scene requires either selecting each GameObject individually or writing repetitive gizmo drawing code in `OnDrawGizmos`.

**The Solution:**
Add `[ShowInScene]` to any position field:
- **Instant Marker Rendering:** See points marked clearly in the Scene view even when not actively selecting the object.
- **Multiple Shapes & Icons:** Choose between `Sphere`, `Cube`, `Cross`, `Diamond`, or built-in Unity icon names.
- **Interactive Move Handles:** Set `Editable = true` to click and drag the marker directly in the Scene view with live Undo.
- **Camera Distance Readout:** Enable `ShowDistanceToCamera = true` to see distance measurements in real time.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class SpawnBeacon : MonoBehaviour
{
    [ShowInScene("Spawn Anchor", "#00FFFF", Shape = SceneGizmoShape.Diamond, Editable = true)]
    public Vector3 spawnPosition = new Vector3(0f, 1f, 5f);
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Vector3`, `Vector2`, `Transform`, `GameObject`, `Component` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ShowInSceneAttribute()
public ShowInSceneAttribute(string label)
public ShowInSceneAttribute(string label, string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `string` | `""` | Text label displayed above the marker. |
| `colorHex` | `string` | `"#FFFFFF"` | Hex color code for the marker shape and text. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | `""` | Custom label displayed above the marker. |
| `ColorHex` | `string` | `"#FFFFFF"` | Hex color of the marker shape and label. |
| `Size` | `float` | `0.5f` | Scale size of the marker shape in world units. |
| `Shape` | `SceneGizmoShape` | `SceneGizmoShape.Sphere` | Marker shape (`Sphere`, `Cube`, `Cross`, `Diamond`). |
| `ShowLabel` | `bool` | `true` | Whether to render the text label above the marker. |
| `OffsetX` | `float` | `0f` | Spatial offset along the X axis. |
| `OffsetY` | `float` | `0.5f` | Spatial offset along the Y axis. |
| `OffsetZ` | `float` | `0f` | Spatial offset along the Z axis. |
| `ShowDistanceToCamera` | `bool` | `false` | Displays live distance from the Scene camera to this marker. |
| `OnlyWhenSelected` | `bool` | `false` | Only renders when the GameObject is selected in the hierarchy. |
| `IconName` | `string` | `""` | Built-in Unity icon name to draw at the position. |
| `Editable` | `bool` | `false` | Renders an interactive position handle when selected for direct Scene translation. |
| `LocalSpace` | `bool` | `false` | Treats the position as local space relative to the parent transform. |
| `Snap` | `float` | `0f` | Grid snapping increment when dragging the handle (`0` = smooth continuous). |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class TacticalWaypoint : MonoBehaviour
{
    [Header("Primary Rally Point")]
    [ShowInScene("Rally Point", "#2ecc71", 
        Shape = SceneGizmoShape.Cross, 
        Size = 0.8f, 
        Editable = true, 
        Snap = 0.5f,
        ShowDistanceToCamera = true
    )]
    public Vector3 rallyPoint = new Vector3(5f, 0f, 10f);

    [Header("Cover Target Position")]
    [ShowInScene("Cover Spot", "#e67e22", Shape = SceneGizmoShape.Cube, LocalSpace = true)]
    public Vector3 coverOffset = new Vector3(-2f, 0f, 3f);
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| Multiple Allowed | Supported | Stack multiple `[ShowInScene]` attributes across different points on the same component. |
| `ICollectionElement` | Supported | Renders markers for every element in `List<Vector3>` or `Transform[]` collections. |
