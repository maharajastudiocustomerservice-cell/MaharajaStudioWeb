# [SceneScaleHandle]

> Renders an interactive 3D scale gizmo (Handles.ScaleHandle) in the Scene view to directly scale Vector3 or float fields with mouse drag and live Undo support.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an interactive 3-axis scale handle directly in the Unity Scene view bound to a `Vector3` or `float` scale property. Allows designers to resize trigger bounds, visual multipliers, or collision shapes directly inside the Scene view using standard cube handle dragging.

**The Problem:**
Adjusting scale parameters like model scale multipliers, spawn box extents, or explosion scales by typing numbers into the Inspector requires repeatedly testing to see if the proportion matches surrounding props.

**The Solution:**
Add `[SceneScaleHandle]` to any scale vector or float:
- **Direct Scene Manipulation:** Click and drag scale axis cube handles directly in the 3D viewport.
- **Safety Clamp:** Enforces a configurable `MinScale` boundary to prevent accidental inverse or zero-scale issues.
- **Vector3 & Uniform Float:** Works identically on 3D vectors or uniform float scale factors.
- **Inspector Eye Toggle:** Includes a 1-click eye button beside the field in the Inspector to show or hide the gizmo.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class PropSpawner : MonoBehaviour
{
    [SceneScaleHandle("Spawn Extent", "#FF55AA")]
    public Vector3 spawnScale = Vector3.one;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Vector3`, `float` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SceneScaleHandleAttribute()
public SceneScaleHandleAttribute(string label)
public SceneScaleHandleAttribute(string label, string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `string` | `""` | Label text displayed near the scale gizmo. |
| `colorHex` | `string` | `"#FF55AA"` | Hex color code for the scale handle feedback. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | `""` | Optional label displayed at the scale handle. |
| `ColorHex` | `string` | `"#FF55AA"` | Hex color for the scale handle visual feedback. |
| `MinScale` | `float` | `0.01f` | Minimum allowed scale clamp value. |
| `OnlyWhenSelected` | `bool` | `true` | Only display handle when the GameObject is selected in the hierarchy. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class DestructibleObject : MonoBehaviour
{
    [Header("Debris Field Scale")]
    [SceneScaleHandle("Debris Volume", "#e74c3c", MinScale = 0.5f)]
    public Vector3 explosionVolume = new Vector3(2f, 2f, 2f);

    [Header("Uniform Shockwave Scale")]
    [SceneScaleHandle("Shockwave Multiplier", "#9b59b6")]
    public float shockwaveScale = 1.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| `[ScenePositionHandle]` | Supported | Stack position and scale handles together for comprehensive transform authoring. |
| `ICollectionElement` | Supported | Renders scale handles for elements inside collections. |
