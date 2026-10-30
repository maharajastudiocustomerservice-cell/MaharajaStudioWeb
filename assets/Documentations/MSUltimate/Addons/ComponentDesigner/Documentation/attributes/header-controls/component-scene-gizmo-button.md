# [ComponentSceneGizmoButton]

> Injects an interactive scene gizmo visibility toggle button directly inside the component header to declutter Scene view drawings.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentSceneGizmoButton]` gives level designers and scripters instant control over complex scene debug visualizations. Injected into `ComponentSlot.BeforeContent`, it displays an interactive toggle button (`GizmoLabel = "Gizmos"`, `Color = "#10B981"`) in the component header. Clicking the button toggles gizmo rendering on and off. It can either store visibility state in the editor session or bind directly to a boolean serialized field on the MonoBehaviour (`BoundPropertyName`).

**The Problem:**
Spawners, waypoints, cover nodes, raycast sensors, and AI patrol networks draw dense gizmo wireframes in the Scene view. When multiple systems overlap, the Scene view becomes an unreadable tangle of lines and icons, but opening Unity's global Gizmos menu mutes all gizmos across the entire project rather than isolating this specific component.

**The Solution:**
Decorating spatial and visualization systems with `[ComponentSceneGizmoButton]`:
- **Granular Per-Component Control:** Toggle gizmo overlays on or off specifically for the inspected component without touching global scene settings.
- **Two-Way Property Binding:** Optionally synchronize the toggle state directly with a `bool drawDebugGizmos` field on your script.
- **Visual Toggle Feedback:** The button dynamically illuminates in vibrant emerald green (`Color = "#10B981"`) when active and dims when muted.
- **Zero Scene View Clutter:** Keep your Scene view pristine during level design passes, enabling gizmo lines only when tuning the relevant parameters.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentSceneGizmoButton("drawSceneGizmos", gizmoLabel: "Vision Cones", defaultVisible: true)]
public class NpcSensorVisualizer : MonoBehaviour
{
    public bool drawSceneGizmos = true;
    public float sensorRangeMeters = 20f;
    public float fieldOfViewDegrees = 90f;

    private void OnDrawGizmos()
    {
        if (!drawSceneGizmos) return;
        Gizmos.color = Color.yellow;
        Gizmos.DrawWireSphere(transform.position, sensorRangeMeters);
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `BeforeContent` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentSceneGizmoButtonAttribute()
public ComponentSceneGizmoButtonAttribute(string boundPropertyName, string gizmoLabel = "Gizmos", bool defaultVisible = true)
```

- `boundPropertyName`: Name of the serialized boolean property on the MonoBehaviour bound to the toggle state.
- `gizmoLabel`: Text label displayed on the gizmo toggle button.
- `defaultVisible`: Initial visibility state if no serialized property or saved session preference exists.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GizmoLabel` | `string` | `"Gizmos"` | Button title displayed on the header toggle control. |
| `BoundPropertyName` | `string` | `""` | Name of the boolean field on the MonoBehaviour that controls gizmo drawing logic. |
| `DefaultVisible` | `bool` | `true` | Default visibility state upon first inspector initialization. |
| `Color` | `string` | `"#10B981"` | Hex accent color used when the gizmo toggle is in the enabled state. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#059669", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#031A11", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("TACTICAL PATROL WAYPOINT ROUTE", Subtitle = "Spline Navigation & Guard Sensor Nodes", BackgroundColor = "#093322", TitleColor = "#D1FAE5")]
[ComponentSceneGizmoButton("showPatrolGizmos", GizmoLabel = "Show Splines", Color = "#10B981", DefaultVisible = true)]
public class TacticalPatrolRouteDirector : MonoBehaviour
{
    [Header("Gizmo Visualization State")]
    public bool showPatrolGizmos = true;

    [Header("Patrol Network")]
    public Transform[] patrolWaypoints = new Transform[4];
    public float patrolSpeedMetersSec = 3.2f;
    public float nodeArrivalToleranceMeters = 0.5f;

    private void OnDrawGizmos()
    {
        if (!showPatrolGizmos || patrolWaypoints == null) return;

        Gizmos.color = Color.green;
        for (int i = 0; i < patrolWaypoints.Length; i++)
        {
            if (patrolWaypoints[i] == null) continue;
            Gizmos.DrawWireSphere(patrolWaypoints[i].position, nodeArrivalToleranceMeters);
            if (i < patrolWaypoints.Length - 1 && patrolWaypoints[i + 1] != null)
            {
                Gizmos.DrawLine(patrolWaypoints[i].position, patrolWaypoints[i + 1].position);
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Fits cleanly alongside the header title and status badges. |
| **`[ComponentHeaderButton]`** | High | Combines with action buttons (e.g. "Bake Path") on the opposite side of the header. |
| **Scene GUI Callbacks** | High | Integrates directly with `OnDrawGizmos`, `OnDrawGizmosSelected`, and `SceneView` callbacks. |
| **Inspector Controls** | High | Toggling the button immediately triggers a Scene view repaint to reflect the updated state. |
