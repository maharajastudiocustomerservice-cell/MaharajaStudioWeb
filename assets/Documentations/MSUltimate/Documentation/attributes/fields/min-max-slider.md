# [MinMaxSlider]

> Renders Vector2 and Vector2Int fields as a dual-thumb range slider with visual bounds, numeric input boxes, and snapping increments.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms standard `Vector2` or `Vector2Int` fields into an ergonomic dual-handle horizontal range slider with minimum and maximum draggable thumbs, flanked by optional editable numeric input fields.

**The Problem:**
Specifying numerical ranges (e.g. enemy spawn delays between 2.5s and 8.0s, audio pitch randomizers from 0.8 to 1.2) using standard `Vector2 (x, y)` fields in Unity is visually unintuitive. Designers have to guess which component is the minimum and can easily type inverted values where `x > y`.

**The Solution:**
Applying `[MinMaxSlider]` delivers:
- **Visual Dual Thumbs:** Drag the lower and upper bounds directly across an interactive track.
- **Input Field Integration:** Dual numerical text boxes flanking the slider allow exact precision typing.
- **Auto Clamping & Inversion Prevention:** Automatically prevents the minimum handle from exceeding the maximum handle.
- **Dynamic Limits & Stepping:** Support for dynamic member limits (`MinMember`, `MaxMember`) and step snapping (e.g. `Step = 0.5f`).
- **Collection Support:** Full support for `List<Vector2>` and collection elements via `ICollectionElementAttribute`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class EnemySpawner : MonoBehaviour
{
    [MinMaxSlider(1f, 15f)]
    public Vector2 spawnDelayRange = new Vector2(3f, 7f);
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Vector2`, `Vector2Int`, `SerializableRange` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public MinMaxSliderAttribute(float min, float max)
public MinMaxSliderAttribute(int min, int max)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` / `int` | *(Required)* | Lower boundary limit of the slider track. |
| `max` | `float` / `int` | *(Required)* | Upper boundary limit of the slider track. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Min` | `float` | *(Set in constructor)* | Lower numerical limit of the slider. |
| `Max` | `float` | *(Set in constructor)* | Upper numerical limit of the slider. |
| `ShowFields` | `bool` | `true` | Toggles visibility of the min/max numerical input boxes. |
| `ShowMinField` | `bool` | `true` | Toggles visibility of the lower bound text input box. |
| `ShowMaxField` | `bool` | `true` | Toggles visibility of the upper bound text input box. |
| `InputWidth` | `float` | `45f` | Width in pixels allocated for each numeric input field. |
| `Step` | `float` | `0f` | Snap step increment (e.g. `0.25f` or `1f`). `0` = continuous. |
| `Decimals` | `int` | `-1` | Number of decimal places to display (`-1` = unconstrained). |
| `MinMember` | `string` | `null` | Name of a field, property, or method dynamically providing the lower limit. |
| `MaxMember` | `string` | `null` | Name of a field, property, or method dynamically providing the upper limit. |
| `StepMember` | `string` | `null` | Dynamic member providing step increments. |
| `SliderColor` | `string` | `null` | Hex color styling for the active range between thumbs. |
| `SliderThumbColor` | `string` | `null` | Hex color styling for both slider thumbs. |
| `MinThumbColor` | `string` | `null` | Hex color override specifically for the minimum thumb. |
| `MaxThumbColor` | `string` | `null` | Hex color override specifically for the maximum thumb. |
| `TrackBackgroundColor` | `string` | `null` | Hex background track color behind the thumbs. |
| `CustomLabel` | `string` | `null` | Override text for the field label. |
| `LabelWidth` | `float` | `0f` | Explicit label width override in pixels. |
| `Height` | `float` | `0f` | Explicit control height override in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioAmbienceZone : MonoBehaviour
{
    [Header("Pitch Variation Bounds")]
    [MinMaxSlider(0.5f, 2.0f, Step = 0.05f, SliderColor = "#2ecc71")]
    public Vector2 pitchRandomRange = new Vector2(0.9f, 1.15f);

    [Header("Int Volume Delay (Seconds)")]
    [MinMaxSlider(0, 60, ShowFields = true, InputWidth = 50f)]
    public Vector2Int fadeIntervalSeconds = new Vector2Int(5, 20);

    [Header("Dynamic Boss Spawn Waves")]
    public float dynamicMinDelay = 10f;
    public float dynamicMaxDelay = 120f;

    [MinMaxSlider(0f, 150f, MinMember = nameof(dynamicMinDelay), MaxMember = nameof(dynamicMaxDelay))]
    public Vector2 bossWaveTriggerTimes = new Vector2(15f, 90f);
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Adapts width cleanly inside nested containers and foldouts. |
| `[ShowIf]` | Supported | Hides or displays the dual slider based on condition states. |
| `[ReadOnly]` | Supported | Renders the track and handle positions while disabling drag operations. |
| `ICollectionElement` | Supported | Works seamlessly inside `List<Vector2>` or `Vector2[]` collections. |
