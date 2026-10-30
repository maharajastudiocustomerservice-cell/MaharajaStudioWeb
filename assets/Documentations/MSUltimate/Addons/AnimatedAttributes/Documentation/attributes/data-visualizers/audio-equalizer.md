# [AudioEqualizer]

> Displays animated spectrum equalizer bars driven by numeric audio or volume properties, with peak cap markers and interactive scrubbing.

---

## 1. Overview & Value Proposition

**What it does:**
`[AudioEqualizer]` visualizes volume, decibel levels, or audio channel gains using an animated multi-column spectrum equalizer. Vertical bars fluctuate dynamically (`AnimationSpeed`) with decaying peak cap markers (`PeakColor`) that trace transient sound spikes. Users can scrub levels interactively by clicking and dragging anywhere across the equalizer container.

**The Problem:**
Audio volumes and channel gains represented by flat numeric floats or standard sliders feel clinical and disconnected from acoustic hardware. Sound designers cannot easily gauge whether a channel has high dynamic headroom or if levels are clipped.

**The Solution:**
Decorating volume or gain properties with `[AudioEqualizer]`:
- **Hardware-Style Spectrum Columns:** Renders a customizable bank of vertical VU bars (`BarCount`, `BarHeight`).
- **Peak Hold Indicators:** Decaying cap markers (`PeakColor`) visually capture maximum volume spikes.
- **Interactive Drag Scrubbing:** Drag anywhere on the equalizer widget (`IsEditable = true`) to adjust volumes fluidly.
- **Dynamic Cap Limits:** Bind `DynamicMaxValueMember` to adapt volume scaling to dynamic audio busses.
- **Collection Cascading:** Implements `ICollectionElementAttribute` for multi-channel audio mixer buses and soundbanks.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SoundManager : MonoBehaviour
{
    [AudioEqualizer(barCount: 10, barColor: "#10B981")]
    public float masterVolume = 85f;
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
public AudioEqualizerAttribute(int barCount = 8, string barColor = "#10B981")

public AudioEqualizerAttribute(
    string dynamicMaxValueMember, 
    int barCount = 8, 
    string barColor = "#10B981"
)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `barCount` | `int` | `8` | Number of vertical equalizer frequency columns rendered. |
| `barColor` | `string` | `"#10B981"` | Hex color string for the active equalizer bars. |
| `dynamicMaxValueMember` | `string` | — | Name of a member providing a dynamic max volume capacity. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BarCount` | `int` | `8` | Total number of equalizer spectrum columns. |
| `BarHeight` | `float` | `20f` | Maximum vertical height in pixels of the equalizer bars. |
| `BarColor` | `string` | `"#10B981"` | Hex color string for the active equalizer bars. |
| `PeakColor` | `string` | `"#FBBF24"` | Hex color string for the floating peak cap markers. |
| `AnimationSpeed` | `float` | `1.5f` | Oscillation speed multiplier for dynamic bar fluctuation. |
| `MinValue` | `float` | `0f` | Value mapped to completely empty equalizer bars. |
| `MaxValue` | `float` | `100f` | Value mapped to 100% full equalizer bars. |
| `DynamicMaxValueMember` | `string` | `null` | Name of a member returning dynamic upper bounds. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property field beside the equalizer. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether clicking/dragging on the equalizer scrubs the field value. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Optional label displayed beside the equalizer display. |
| `ShowValue` | `bool` | `true` | Whether to display numeric volume readout overlay. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AudioMixerBusController : MonoBehaviour
{
    [Header("Bus Gain Configuration")]
    public float maxBusGain = 120f;

    [Header("BGM Channel Gain")]
    [AudioEqualizer(
        nameof(maxBusGain), 
        barCount: 12, 
        barColor: "#06B6D4",
        BarHeight = 26f,
        PeakColor = "#F59E0B",
        AnimationSpeed = 2.0f,
        CustomLabel = "BGM MASTER"
    )]
    public float bgmGain = 92f;

    [Header("SFX Channel Gain")]
    [AudioEqualizer(barCount: 8, barColor: "#10B981", BarHeight = 22f)]
    public float sfxGain = 75f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Fits cleanly inside audio mixer consoles and audio channel strips. |
| `[EditorSoundEffect]` | Stacking | Pairs with sound effects to preview audio clicks when modifying channel gain. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` for multi-track audio bus lists. |
