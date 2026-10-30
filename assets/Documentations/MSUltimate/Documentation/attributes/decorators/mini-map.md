# [MiniMap]

> Renders an interactive 2D radar/minimap canvas for Vector2 or Vector3 position fields with live spatial dragging.

---

## 1. Overview & Value Proposition

**What it does:**
Embeds a visual 2D radar grid next to a Vector position field, allowing designers to see and drag spatial coordinates directly inside the Inspector.

**The Problem:**
Tuning 2D spawn coordinates, patrol waypoints, or UI anchor offsets using raw numbers (`X: 14.2, Y: -8.7`) requires abstract mental mapping. Designers must repeatedly switch to the Scene view or play mode just to see where an offset lands in relation to boundaries.

**The Solution:**
Add `[MiniMap]` to any Vector2 or Vector3 field:
- **Interactive Spatial Dragging:** Click and drag the position indicator dot directly on the radar grid to update coordinates in real time.
- **Configurable Coordinate Range:** Set grid boundaries (`range`) to match world room sizes, UI boundaries, or arena extents.
- **Coordinate Overlay:** Displays clear numeric coordinate readouts directly below the radar canvas.
- **Styling Customization:** Customize canvas dimensions, indicator dot colors, and background radar grid colors.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SpawnerPoint : MonoBehaviour
{
    [MiniMap(mapSize: 90f, range: 25f)]
    public Vector2 localSpawnOffset;

    [MiniMap(range: 100f, dotColorHex: "#2ecc71")]
    public Vector3 patrolTargetPosition;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Vector2`, `Vector2Int`, `Vector3`, `Vector3Int`, `Vector2[]`, `List<Vector2>`, `Vector3[]`, `List<Vector3>` |
| **Collection Cascading** | Yes (`ICollectionElementAttribute`) |
| **Collection Presentation** | Yes (`ICollectionPresentationAttribute` - Unified Multi-Point Radar Mode) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public MiniMapAttribute(
    float mapSize = 80f, 
    float range = 50f, 
    string dotColorHex = "#e74c3c", 
    string gridColorHex = "#333333", 
    bool showCoordinates = true)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `mapSize` | `float` | `80f` | Width and height of the square minimap canvas in pixels. |
| `range` | `float` | `50f` | Half-extent coordinate distance from the center origin. |
| `dotColorHex` | `string` | `"#e74c3c"` | Hex color string for the draggable position indicator dot. |
| `gridColorHex` | `string` | `"#333333"` | Hex background color of the radar grid canvas. |
| `showCoordinates` | `bool` | `true` | Toggles numeric readout text below the canvas. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MapSize` | `float` | `80f` | Radar canvas pixel dimensions. |
| `Range` | `float` | `50f` | Spatial coordinate range represented on the grid. |
| `DotColorHex` | `string` | `"#e74c3c"` | Indicator point color. |
| `GridColorHex` | `string` | `"#333333"` | Canvas background grid color. |
| `ShowCoordinates` | `bool` | `true` | Shows or hides coordinate label. |
| `EnableCustomPresentation`| `bool` | `true` | Toggles multi-waypoint unified radar presentation mode for collection containers. |
| `ConnectWaypoints` | `bool` | `true` | Whether consecutive waypoints on collection radar displays are linked with trajectory lines. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class BossArenaDirector : MonoBehaviour
{
    [Header("Artillery Target")]
    [MiniMap(mapSize: 100f, range: 40f, dotColorHex: "#e74c3c", gridColorHex: "#1e272e")]
    public Vector2 orbitalStrikeTarget;

    [Header("Air Drop Location")]
    [MiniMap(mapSize: 80f, range: 100f, dotColorHex: "#3498db")]
    public Vector3 supplyCrateDropPoint;

    [Header("Patrol Waypoint Network")]
    [MiniMap(mapSize: 90f, range: 80f, dotColorHex: "#10b981", ConnectWaypoints = true)]
    public Vector2[] patrolWaypoints;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Minimap scales neatly inside boxed layout groups. |
| `[ShowIf]` | Supported | Conditionally displays the radar canvas when spatial modes are enabled. |
| `[ReadOnly]` | Supported | Displays position on radar canvas without allowing dragging. |
| `ICollectionPresentationAttribute` | Supported | Renders a unified multi-point radar view plotting all coordinates as numbered waypoints on a single radar screen. |
| `ICollectionElementAttribute` | Supported | In standard list mode, cascades compact interactive 2D radar widgets to each element slot across `Vector2[]` and `List<Vector3>`. |
