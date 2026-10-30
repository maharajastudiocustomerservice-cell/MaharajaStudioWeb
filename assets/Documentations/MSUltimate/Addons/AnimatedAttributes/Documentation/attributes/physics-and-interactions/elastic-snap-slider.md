# [ElasticSnapSlider]

> Renders a slider with magnetic snap notches and elastic spring bounce when snapping to step intervals, with dynamic bounds and collection support.

---

## 1. Overview & Value Proposition

**What it does:**
`[ElasticSnapSlider]` elevates standard numeric sliders into tactile, magnetic controls. As the user scrubs the slider, the thumb handle exhibits magnetic pull toward defined step intervals (`SnapStep`). When entering the magnetic zone (`SnapThreshold`), the handle snaps firmly into place with a subtle harmonic spring bounce. It supports dynamic bounds, companion numeric field input, and collection cascading.

**The Problem:**
Standard Unity sliders (`[Range]`) move linearly without tactile stops. When tuning discrete intervals—such as audio volume increments (0%, 25%, 50%, 75%, 100%), grid tile subdivisions, or weapons fire rates—designers frequently struggle to hit exact target increments using mouse drags.

**The Solution:**
Decorating numeric fields with `[ElasticSnapSlider]`:
- **Magnetic Step Snapping:** Pulls the slider handle magnetically to specified step intervals (`SnapStep`) within range (`SnapThreshold`).
- **Tactile Elastic Rebound:** Produces an elastic spring overshoot and settle effect upon snapping.
- **Dynamic Limits Binding:** Bind maximums dynamically via `dynamicMaxValueMember` or `DynamicMinValueMember`.
- **Integrated Precision Input Field:** Includes a companion numeric text field (`DrawInputField = true`) for direct manual typing.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for arrays and lists of numeric values.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AudioMixerSettings : MonoBehaviour
{
    [ElasticSnapSlider(min: 0f, max: 100f, step: 25f)]
    public float masterVolumePercent = 75f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `int`, `float`, `double`, `long`, `short`, `byte` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public ElasticSnapSliderAttribute(float min, float max, float step = 25f)

public ElasticSnapSliderAttribute(string dynamicMaxValueMember, float step = 25f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` | — | Minimum slider value range limit. |
| `max` | `float` | — | Maximum slider value range limit. |
| `dynamicMaxValueMember` | `string` | — | Name of a member providing dynamic upper range capacity. |
| `step` | `float` | `25f` | Step interval between magnetic snap points. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum slider value. |
| `MaxValue` | `float` | `100f` | Maximum slider value. |
| `DynamicMaxValueMember` | `string` | `null` | Name of a member providing dynamic maximum bound. |
| `DynamicMinValueMember` | `string` | `null` | Name of a member providing dynamic minimum bound. |
| `SnapStep` | `float` | `25f` | Step interval between magnetic snap points. |
| `SnapThreshold` | `float` | `5f` | Distance threshold in units to trigger magnetic snapping. |
| `DrawInputField` | `bool` | `true` | Whether to draw companion numeric text field for precise typing. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether the slider is interactive. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Custom label prefix displayed beside the slider. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AudioMasterBus : MonoBehaviour
{
    [Header("Dynamic Channel Limit")]
    public float maxBusDecibels = 120f;

    [Header("Master Bus Limiter")]
    [ElasticSnapSlider(
        nameof(maxBusDecibels), 
        step: 20f, 
        SnapThreshold = 8f, 
        CustomLabel = "Master DB"
    )]
    public float currentBusOutput = 60f;

    [Header("Octave Equalizer Bands")]
    [ElasticSnapSlider(0f, 100f, step: 10f)]
    public List<float> equalizerBands = new List<float> { 50f, 60f, 70f, 40f };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Integrates neatly into audio panels, graphics sliders, and modular groups. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` for multiple stepped sliders. |
| `[ThresholdSpikeFlash]` | Stacking | Triggers threshold flashes when scrubbing past designated limits. |
