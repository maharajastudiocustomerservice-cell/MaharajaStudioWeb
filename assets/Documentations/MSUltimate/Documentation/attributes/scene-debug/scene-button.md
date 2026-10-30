# [SceneButton]

> Renders interactive 3D clickable buttons floating in the Scene view to trigger methods or reset fields directly within the spatial viewport with live Undo support.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an interactive, clickable 3D button directly inside the Unity Scene view hovering above or offset from the GameObject. When clicked in the Scene view, it invokes the decorated method (or resets the decorated field/property) on the component with full Undo support.

**The Problem:**
Testing runtime behaviors, spawning actors, cycling animation states, or executing calibration routines requires constantly shifting focus between looking at the Scene view and scrolling through deep Inspector panels to locate utility buttons.

**The Solution:**
Add `[SceneButton]` directly onto any method, field, or property:
- **Spatial Clickable Action:** Execute component methods directly in the 3D viewport without ever leaving the Scene camera.
- **Customizable Positioning:** Position buttons in 3D space using `OffsetX`, `OffsetY`, `OffsetZ` or scale them with `Size`.
- **Theming & Color:** Customize button appearance using hex color codes (`ColorHex`).
- **Inspector Toggle:** Includes an eye visibility toggle beside the member in the Inspector to show or hide the 3D scene button.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class Spawner : MonoBehaviour
{
    [SceneButton("Spawn Enemy", "#00FF88", 2.0f)]
    public void Spawn()
    {
        Debug.Log("Enemy spawned from Scene view!");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Method | AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | Any method (zero parameters recommended), or field/property |
| **Collection Interface** | `ICollectionElementAttribute` |
| **Collection Cascading** | Full (`Vector3[]`, `List<Vector3>`, `Transform[]`, `List<GameObject>`) |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `SceneDebugGizmoDrawer` (Scene View) & `SceneGizmoFieldToggle` (Inspector) |

---

## 4. Constructors & Parameters

```csharp
public SceneButtonAttribute()
public SceneButtonAttribute(string text)
public SceneButtonAttribute(string text, string colorHex)
public SceneButtonAttribute(string text, float offsetY)
public SceneButtonAttribute(string text, string colorHex, float offsetY)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `text` | `string` | `"Execute"` | Text label displayed on the 3D button. |
| `colorHex` | `string` | `"#00FF88"` | Hex background color of the button. |
| `offsetY` | `float` | `1.5f` | Vertical offset in world units above the object. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | `"Execute"` | Label text displayed on the 3D scene button. |
| `OffsetX` | `float` | `0f` | Offset along the X axis from the object's transform. |
| `OffsetY` | `float` | `1.5f` | Offset along the Y axis from the object's transform. |
| `OffsetZ` | `float` | `0f` | Offset along the Z axis from the object's transform. |
| `ColorHex` | `string` | `"#00FF88"` | Hex background color for the button plate. |
| `Size` | `float` | `0.8f` | Scale size multiplier of the button in the Scene view. |
| `OnlyWhenSelected` | `bool` | `true` | Only renders when the GameObject is selected in the hierarchy. |
| `ShowToggleInInspector` | `bool` | `true` | Renders a visibility toggle eye button beside the member in the Inspector. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class LevelDoor : MonoBehaviour
{
    [Serializable]
    public class DefenseNode
    {
        public string nodeName = "Sector-Alpha";

        [SceneButton("Cycle Node", "#38BDF8", 1.0f)]
        public void ToggleNode() => Debug.Log($"Toggled {nodeName}");
    }

    [SerializeField] private bool isOpen = false;

    [SceneButton("Toggle Door", "#3498db", 2.2f, Size = 1.0f)]
    public void ToggleDoorState()
    {
        isOpen = !isOpen;
        transform.rotation = isOpen ? Quaternion.Euler(0, 90, 0) : Quaternion.identity;
    }

    [SceneButton("Reset Position", "#e74c3c", OffsetX = 1.5f, OffsetY = 2.2f)]
    public void ResetPosition()
    {
        transform.position = Vector3.zero;
        transform.rotation = Quaternion.identity;
    }

    [Header("Defense Node (Inside Class)")]
    public DefenseNode primaryNode = new DefenseNode();

    [Header("Direct Collection Cascading")]
    [SceneButton("Ping Waypoint", "#10B981", OffsetY = 1.0f)]
    public Vector3[] patrolWaypoints = new Vector3[] { new Vector3(2, 0, 2), new Vector3(6, 0, 2) };

    [SceneButton("Engage Extraction", "#38BDF8", OffsetY = 1.2f)]
    public List<Vector3> extractionZones = new List<Vector3> { new Vector3(-4, 0, 0), new Vector3(0, 0, 5) };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Pair with `[Button]` to have both an Inspector button and a 3D Scene View button on the same method. |
| Multiple Allowed | Supported | Stack multiple `[SceneButton]` tags with distinct offsets to create a floating in-scene action toolbar. |
| Method Invocation | Supported | Invokes methods safely within the editor lifecycle with Undo registration. |

### Collection Cascading Matrix

| Collection Type | Cascading Behavior | Presentation Mode |
| :--- | :---: | :--- |
| `Vector3[]`, `List<Vector3>` | **Supported** | Renders 3D clickable buttons hovering above each waypoint / coordinate slot. |
| `Transform[]`, `GameObject[]` | **Supported** | Renders interactive scene buttons directly anchored to referenced transform targets. |
| `AdvancedList<T>` | **Supported** | Full compatibility with advanced serialized collections and pagination. |
| `SerializableDictionary<K, V>` | **Supported** | Cascades to dictionary value element entries. |
| Nested `[Serializable]` Classes | **Supported** | Methods within class instances project 3D buttons into the scene view. |
