# [SceneLabel]

> Renders world-space text labels and data readouts in the Scene view displaying field values, custom prefixes/suffixes, and background plates with billboarding.

---

## 1. Overview & Value Proposition

**What it does:**
Renders a world-space text plate directly in the Scene view displaying the current value of the decorated field or property. Features customizable font sizing, colors, background callout plates, 3D spatial offsets, prefix/suffix text, and automatic billboard camera-facing orientation.

**The Problem:**
Monitoring AI states, health values, patrol point numbers, or physics velocity readouts in large open scenes requires constantly glancing back and forth between the Inspector and Scene view or littering scripts with custom `OnDrawGizmos` GUI code.

**The Solution:**
Add `[SceneLabel]` to any field or property:
- **Instant World-Space Telemetry:** Live value updates visible directly above or beside objects in the Scene view.
- **Background Styling:** Crisp callout background plates (`BackgroundColorHex`) ensure readability against any background.
- **Billboarding:** Automatically rotates to face the Scene view camera at all times.
- **Collection Elements:** Decorate arrays or lists of waypoints to display index or coordinate labels for each point.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class EnemyHealth : MonoBehaviour
{
    [SceneLabel("HP: ", "#FF4444", OffsetY = 2.0f)]
    public int currentHealth = 100;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field (primitives, strings, vectors, enums) |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `SceneDebugGizmoDrawer` (Scene View) & `SceneGizmoFieldToggle` (Inspector) |

---

## 4. Constructors & Parameters

```csharp
public SceneLabelAttribute()
public SceneLabelAttribute(string prefix)
public SceneLabelAttribute(string prefix, string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `prefix` | `string` | `""` | Text prepended to the displayed field value. |
| `colorHex` | `string` | `"#FFFFFF"` | Hex color code for the text font. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `"#FFFFFF"` | Hex text color for the label. |
| `FontSize` | `int` | `12` | Font size in pixels. |
| `BackgroundColorHex` | `string` | `"#00000088"` | Hex color with alpha for the label background plate. |
| `OffsetX` | `float` | `0f` | Offset along the X axis from the object's transform. |
| `OffsetY` | `float` | `1f` | Offset along the Y axis from the object's transform. |
| `OffsetZ` | `float` | `0f` | Offset along the Z axis from the object's transform. |
| `Prefix` | `string` | `""` | Text prepended to the displayed value. |
| `Suffix` | `string` | `""` | Text appended to the displayed value. |
| `ShowFieldName` | `bool` | `false` | If true, automatically prefixes the label with the member name. |
| `BillboardMode` | `bool` | `true` | If true, rotates the label to always face the Scene camera. |
| `OnlyWhenSelected` | `bool` | `false` | Only renders when the GameObject is selected in the hierarchy. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class AIPatrolAgent : MonoBehaviour
{
    public enum AIState { Idle, Patrolling, Chasing, Alert }

    [Header("Agent State Telemetry")]
    [SceneLabel("State: ", "#f1c40f", OffsetY = 2.4f, FontSize = 14, BackgroundColorHex = "#1a1a1acc")]
    public AIState currentState = AIState.Patrolling;

    [Header("Detection Distance")]
    [SceneLabel("Radius: ", "#3498db", Suffix = " m", OffsetY = 1.8f)]
    public float detectionRadius = 15.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| `[ScenePositionHandle]` | Supported | Label updates and repositions dynamically as position handles are dragged. |
| `ICollectionElement` | Supported | Renders individual floating text labels for each element inside lists or arrays. |
