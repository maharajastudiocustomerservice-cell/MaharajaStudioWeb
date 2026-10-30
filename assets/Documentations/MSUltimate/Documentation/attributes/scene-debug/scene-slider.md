# [SceneSlider]

> Renders a constrained 1D linear slider handle in the Scene view to adjust float or int values directly along a specified cardinal or directional axis with mouse drag.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an in-scene 1D linear track and slider cap directly in the Scene view aligned along a selected axis (`X`, `Y`, `Z`, `Forward`, `Up`, `Right`). Allows level designers and technical artists to drag a scalar float or int parameter (like door open percent, platform lift height, or laser beam length) intuitively along its spatial direction of movement.

**The Problem:**
Tuning directional scalar offsets—such as how high an elevator should travel or how far forward a spiked trap should extend—requires guessing numbers in an Inspector field and observing if the distance looks right.

**The Solution:**
Add `[SceneSlider]` to any scalar float or integer:
- **Constrained 1D Dragging:** Move values smoothly between `Min` and `Max` along the object's local or cardinal axes.
- **Directional Axes:** Choose from `X`, `Y`, `Z`, `Forward`, `Up`, or `Right` to match physical movement directions.
- **Visual Track & Cap:** Renders a clean guide line, slider track, and draggable disc cap.
- **Inspector Toggle:** Includes an eye visibility toggle beside the field in the Inspector.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class ElevatorPlatform : MonoBehaviour
{
    [SceneSlider("Lift Height", SceneSliderAxis.Up, min: 0f, max: 25f)]
    public float targetHeight = 10f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `double` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SceneSliderAttribute()
public SceneSliderAttribute(SceneSliderAxis axis, float min = 0f, float max = 100f)
public SceneSliderAttribute(string label, SceneSliderAxis axis, float min = 0f, float max = 100f)
public SceneSliderAttribute(string label, SceneSliderAxis axis, float min, float max, string colorHex)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `string` | `""` | Label text displayed near the slider handle. |
| `axis` | `SceneSliderAxis` | `SceneSliderAxis.Y` | Directional axis (`X`, `Y`, `Z`, `Forward`, `Up`, `Right`). |
| `min` | `float` | `0f` | Minimum slider boundary value. |
| `max` | `float` | `100f` | Maximum slider boundary value. |
| `colorHex` | `string` | `"#FFCC00"` | Hex color code for the slider track and cap. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Axis` | `SceneSliderAxis` | `SceneSliderAxis.Y` | Movement axis along which the slider travels. |
| `Min` | `float` | `0f` | Minimum slider clamp value. |
| `Max` | `float` | `100f` | Maximum slider clamp value. |
| `HandleSize` | `float` | `0.3f` | Scale size of the 3D slider handle cap. |
| `ColorHex` | `string` | `"#FFCC00"` | Hex color for the slider bar and handle cap. |
| `Label` | `string` | `""` | Optional label displayed at the slider position. |
| `OnlyWhenSelected` | `bool` | `true` | Only display when the GameObject is selected in the hierarchy. |
| `ShowToggleInInspector` | `bool` | `true` | Shows an eye visibility toggle button beside the field in the Inspector. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.SceneDebug;

public class LaserObstacle : MonoBehaviour
{
    [Header("Laser Beam Extension Length")]
    [SceneSlider("Beam Distance", SceneSliderAxis.Forward, 1f, 50f, "#e74c3c")]
    public float beamLength = 15f;

    [Header("Vertical Elevation Offset")]
    [SceneSlider("Elevation", SceneSliderAxis.Up, 0f, 10f, "#3498db")]
    public float mountElevation = 2f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Eye toggle button renders cleanly inside group cards. |
| Multiple Allowed | Supported | Stack multiple sliders on different axes to control 2D or 3D scalar components. |
| `ICollectionElement` | Supported | Renders sliders for numeric elements inside collections. |
