# [RotaryKnob]

> Replaces numeric fields with an interactive circular rotary dial knob operated via angular drag gestures, with dynamic bounds and magnetic snapping.

---

## 1. Overview & Value Proposition

**What it does:**
`[RotaryKnob]` transforms standard linear numeric inputs into hardware-style analog rotary dials. Operated via angular circular mouse drags, the dial updates numeric values between `MinValue` and `MaxValue` (or dynamic bounds via `DynamicMaxValueMember`). It renders a visual value arc (`ArcColor`), directional pointer needle (`PointerColor`), optional magnetic step snapping (`SnapInterval`), and configurable numeric readout formatting (`ValueFormat`). It also implements `ICollectionElementAttribute` for multi-item list cascading.

**The Problem:**
Audio synthesizers, volume attenuators, radial dials, steer angles, or vintage hardware consoles are intrinsically circular controls. Tuning rotational values using flat horizontal sliders feels counter-intuitive and clutters complex audio/physics panels.

**The Solution:**
Decorating numeric fields with `[RotaryKnob]`:
- **Hardware Dial Ergonomics:** Circular mouse dragging around the dial center provides natural rotational torque feedback.
- **Magnetic Snap Intervals:** Snap to discrete steps (e.g., 5°, 10°, 45°) via `SnapInterval`, or set to `0f` for smooth analog rotation.
- **Dynamic Limits Binding:** Bind maximums dynamically via `dynamicMaxValueMember` or `DynamicMinValueMember`.
- **Integrated Precision Input Field:** Includes a companion numeric text field (`DrawInputField = true`) for direct manual entry.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for synthesizer arrays and mixer channels.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SynthesizerChannel : MonoBehaviour
{
    [RotaryKnob(min: 0f, max: 100f, size: 48f)]
    public float lowPassFilterCutoff = 65f;
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
public RotaryKnobAttribute(float min = 0f, float max = 100f, float size = 42f)

public RotaryKnobAttribute(string dynamicMaxValueMember, float size = 42f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` | `float` | `0f` | Minimum numeric value at counter-clockwise limit. |
| `max` | `float` | `100f` | Maximum numeric value at clockwise limit. |
| `dynamicMaxValueMember` | `string` | — | Name of a member providing dynamic upper range capacity. |
| `size` | `float` | `42f` | Diameter in pixels of the rotary knob dial. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinValue` | `float` | `0f` | Minimum dial value bound. |
| `MaxValue` | `float` | `100f` | Maximum dial value bound. |
| `DynamicMaxValueMember` | `string` | `null` | Name of a member providing dynamic maximum bound. |
| `DynamicMinValueMember` | `string` | `null` | Name of a member providing dynamic minimum bound. |
| `KnobSize` | `float` | `42f` | Diameter of the circular dial in pixels. |
| `ArcColor` | `string` | `"#3B82F6"` | Hex color string for the active circular value arc indicator. |
| `PointerColor` | `string` | `"#FFFFFF"` | Hex color string for the directional needle pointer line. |
| `SnapInterval` | `float` | `0f` | Magnetic snap interval step (`0f` for smooth continuous rotation). |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property companion input field. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether the rotary knob dial can be interactively rotated by dragging. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `ShowValue` | `bool` | `true` | Whether to display the numeric value readout beside the knob. |
| `ValueFormat` | `string` | `"{0:F1}"` | Format string applied to the numeric value readout text. |
| `CustomLabel` | `string` | `null` | Custom label prefix displayed beside the knob. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AudioMasterConsole : MonoBehaviour
{
    [Header("Master Channel Gain")]
    public float maximumBusGainDB = 24f;

    [RotaryKnob(
        nameof(maximumBusGainDB), 
        size: 52f, 
        ArcColor = "#10B981", 
        ValueFormat = "{0:F2} dB", 
        CustomLabel = "Pre-Amp Gain"
    )]
    public float preAmpGain = 12.5f;

    [Header("Parametric EQ Knobs")]
    [RotaryKnob(0f, 100f, size: 38f, ArcColor = "#F59E0B")]
    public List<float> parametricEqualizerPots = new List<float> { 20f, 50f, 80f };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Arranges side-by-side inside horizontal layouts or compact mixer cards. |
| Collections (`List<float>`) | Supported | Implements `ICollectionElementAttribute` for multiple stepped rotary pots. |
| `[ReadOnly]` | Supported | Locks interactive mouse dragging while displaying passive rotational telemetry. |
