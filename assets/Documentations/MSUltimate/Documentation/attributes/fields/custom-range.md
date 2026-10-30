# [CustomRange]

> Renders a numeric field as an enhanced slider with custom limits, dynamic member bounds, step snapping, and styling.

---

## 1. Overview & Value Proposition

**What it does:**
Upgrades standard numeric range sliders with step snapping, dynamic min/max bounds, decimal precision, and custom colors.

**The Problem:**
Unity's built-in `[Range]` attribute is static: min and max values must be compile-time constants. You cannot bind limits dynamically to another property (like `maxAmmo`), cannot snap slider dragging to discrete steps (like `0.25`), and cannot style track colors.

**The Solution:**
Add `[CustomRange]` to any numeric field:
- **Dynamic Min/Max Limits:** Bind limits dynamically to float/int member fields or methods (e.g. `minLevel`, `maxLevel`).
- **Step Snapping:** Snap values to exact increments (e.g. `Step = 0.5f` or `Step = 5f`).
- **Decimal Precision Control:** Enforce exact decimal rounding (e.g. `Decimals = 2`).
- **Integrated Number Box:** Displays an editable numeric field alongside the slider track.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class WeaponStats : MonoBehaviour
{
    [CustomRange(0f, 100f)]
    public float damage = 25f;

    [CustomRange(0f, 10f, Step = 0.25f)]
    public float reloadTime = 2.5f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `double`, `long`, `short`, `byte` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public CustomRangeAttribute(float min, float max)
public CustomRangeAttribute(int min, int max)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` / `int` | *(Required)* | Static minimum allowed value. |
| `max` | `float` / `int` | *(Required)* | Static maximum allowed value. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Min` | `float` | *(Required)* | Minimum numeric bound. |
| `Max` | `float` | *(Required)* | Maximum numeric bound. |
| `Step` | `float` | `0f` | Step snapping increment (`0f` is continuous). |
| `MinMember` | `string` | `null` | Member name returning dynamic min bound. |
| `MaxMember` | `string` | `null` | Member name returning dynamic max bound. |
| `Decimals` | `int` | `-1` | Decimal places to round to (`-1` for default). |
| `ShowInputField` | `bool` | `true` | Renders editable numeric input next to slider. |
| `SliderColor` | `string` | `null` | Hex track fill color. |
| `SliderThumbColor` | `string` | `null` | Hex slider handle/thumb color. |
| `CustomLabel` | `string` | `null` | Custom field display label override. |
| `InputWidth` | `float` | `0f` | Custom width of the numeric input box (0 uses default). |
| `Height` | `float` | `0f` | Custom slider row height in pixels (0 uses default). |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TurretCalibrator : MonoBehaviour
{
    public float maxElevationAngle = 85f;

    [Header("Elevation Control")]
    [CustomRange(-10f, 90f, MaxMember = nameof(maxElevationAngle), Step = 1f, SliderColor = "#3498db")]
    public float currentPitch = 15f;

    [Header("Burst Fire Timing")]
    [CustomRange(0.05f, 2.0f, Step = 0.05f, Decimals = 2, SliderColor = "#e67e22")]
    public float burstDelaySeconds = 0.15f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[SuffixLabel]` | Supported | Suffix measurement unit docks cleanly to the right of the slider. |
| `[BoxGroup]` | Supported | Adapts cleanly within nested groups and tabs. |
| `[ReadOnly]` | Supported | Locks slider and number input from user edits. |
