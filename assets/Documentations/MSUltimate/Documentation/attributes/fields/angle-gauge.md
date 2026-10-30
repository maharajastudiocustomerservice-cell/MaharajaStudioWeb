# [AngleGauge]

> Renders a numeric field or rotation value as an interactive 2D radial dial gauge with angle snapping and compass directions.

---

## 1. Overview & Value Proposition

**What it does:**
Renders a visual circular dial or compass gauge with an interactive needle to intuitively rotate angles and directional vectors.

**The Problem:**
Tuning angular bearings, wind directions, or turret firing angles using raw numbers (`135.5°`, `270°`) forces developers to calculate trigonometry in their heads. Designers frequently enter reversed angles or miss quadrant boundaries because numbers alone lack spatial feedback.

**The Solution:**
Add `[AngleGauge]` to any numeric rotation field:
- **Interactive Radial Needle:** Click and drag the gauge needle to rotate angles with immediate visual feedback.
- **Cardinal Compass Markings:** Displays North (N), East (E), South (S), and West (W) compass directions.
- **Angle Snapping & Quick Buttons:** Snap to customizable increments (e.g. 15°, 45°, 90°) with one-click cardinal preset buttons.
- **Degrees or Radians:** Supports both standard Degrees (0–360°) and Radians ($0–2\pi$) with clockwise or counter-clockwise orientations.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class WindDirector : MonoBehaviour
{
    [AngleGauge(0, 360, snapAngle: 15f)]
    public float windDirectionDegrees = 45f;

    [AngleGauge(Radians = true, ShowQuickButtons = false)]
    public float steeringAngleRadians = 0f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `double` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AngleGaugeAttribute(float min = 0f, float max = 360f, float snapAngle = 0f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` | `0f` | Minimum angular limit bound. |
| `max` | `float` | `360f` | Maximum angular limit bound. |
| `snapAngle` | `float` | `0f` | Snapping increment in degrees (`0` disables snapping). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Min` | `float` | `0f` | Minimum angle limit. |
| `Max` | `float` | `360f` | Maximum angle limit. |
| `SnapAngle` | `float` | `0f` | Drag snap angle increment. |
| `ShowCompassDirections` | `bool` | `true` | Shows cardinal points (N, NE, E, SE, S, SW, W, NW). |
| `ShowQuickButtons` | `bool` | `true` | Shows quick 0°, 90°, 180°, 270° snap buttons. |
| `Radians` | `bool` | `false` | Stored and edited in Radians instead of Degrees. |
| `GaugeSize` | `float` | `84f` | Radial gauge diameter in pixels. |
| `Clockwise` | `bool` | `true` | Angle direction increases clockwise. |
| `ZeroOffset` | `float` | `90f` | Angular origin offset: 90 = North (top), 0 = East (right). |
| `NeedleColor` | `string` | `"#FF4757"` | Indicator needle hex color. |
| `ArcColor` | `string` | `"#2ED573"` | Active angle arc fill hex color. |
| `DialColor` | `string` | `"#3E4452"` | Dial bezel and tick mark hex color. |
| `BackgroundColor` | `string` | `"#1E1E28"` | Background container card hex color. |
| `BorderColor` | `string` | `"#323242"` | Border color for the widget container. |
| `BorderRadius` | `float` | `6f` | Corner radius of the widget card in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ArtilleryAim : MonoBehaviour
{
    [Header("Turret Horizontal Azimuth")]
    [AngleGauge(0, 360, snapAngle: 5f, GaugeSize = 96f, NeedleColor = "#e74c3c", ArcColor = "#3498db")]
    public float targetHeading = 180f;

    [Header("Elevation Arc")]
    [AngleGauge(min: -15f, max: 85f, ShowCompassDirections = false)]
    public float barrelElevation = 12f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Dial fits neatly inside group layouts and tabs. |
| `[SuffixLabel]` | Supported | Pairs with degree or radian suffix labels. |
| `[ReadOnly]` | Supported | Functions as a live visual rotation compass indicator. |
