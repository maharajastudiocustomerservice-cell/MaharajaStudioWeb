# [LiveOscilloscopeWave]

> Renders a real-time retro CRT phosphor waveform reacting dynamically to value mutations, featuring interactive dragging and dynamic amplitude scaling.

---

## 1. Overview & Value Proposition

**What it does:**
`[LiveOscilloscopeWave]` transforms standard numeric properties into a live retro cathode-ray tube (CRT) oscilloscope display. A vibrant phosphor trace oscillates horizontally across a customizable canvas, with its amplitude directly driven by the decorated field's value. Users can interactively scrub values by clicking and dragging vertically on the CRT display.

**The Problem:**
Audio synthesizer parameters, pitch modulations, vibration frequencies, and recoil offsets are hard to conceptualize through simple numeric textboxes. Designers need visual wave representations to grasp how adjustments alter waveforms.

**The Solution:**
Decorating numeric fields with `[LiveOscilloscopeWave]`:
- **Real-Time CRT Wave Simulation:** Renders an authentic glowing phosphor trace with configurable harmonics and speed.
- **Interactive Drag Scrubbing:** Drag directly on the CRT display (`IsEditable = true`) to scrub amplitudes intuitively.
- **Dynamic Upper Bounds:** Bind `DynamicMaxValueMember` to adapt peak wave scaling to runtime equipment or audio limits.
- **Collection Cascading:** Implements `ICollectionElementAttribute` to visualize harmonic lists or audio frequencies inside lists and arrays.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SynthesizerVoice : MonoBehaviour
{
    [LiveOscilloscopeWave(waveHeight: 50f, phosphorColor: "#39FF14", maxValue: 5f)]
    public float oscillatorFrequency = 2.4f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `double`, `int`, `long` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public LiveOscilloscopeWaveAttribute(
    float waveHeight = 40f, 
    string phosphorColor = "#39FF14", 
    float maxValue = 2.0f
)

public LiveOscilloscopeWaveAttribute(
    string dynamicMaxValueMember, 
    float waveHeight = 40f, 
    string phosphorColor = "#39FF14"
)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `waveHeight` | `float` | `40f` | Height of the CRT oscilloscope canvas in pixels. |
| `phosphorColor` | `string` | `"#39FF14"` | Hex color string for the glowing phosphor trace. |
| `maxValue` | `float` | `2.0f` | Maximum amplitude value mapped to the top of the display. |
| `dynamicMaxValueMember` | `string` | — | Name of a member (field/property/method) returning dynamic max amplitude. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `WaveHeight` | `float` | `40f` | Vertical display height in pixels. |
| `PhosphorColor` | `string` | `"#39FF14"` | Hex color string for the CRT beam trace. |
| `WaveSpeed` | `float` | `2.0f` | Speed multiplier of the horizontal waveform scrolling motion. |
| `WaveComplexity` | `float` | `3.0f` | Harmonic frequency complexity and ripple count of the wave simulation. |
| `MinValue` | `float` | `0.0f` | Minimum amplitude value mapped to the flat baseline. |
| `MaxValue` | `float` | `2.0f` | Maximum amplitude mapped to the peak display boundary. |
| `DynamicMaxValueMember` | `string` | `null` | Member name returning dynamic upper bounds. |
| `DrawInputField` | `bool` | `true` | Whether to draw the standard serialized property field above the CRT trace. |
| `ShowInputField` | `bool` | `true` | Alias for `DrawInputField`. |
| `IsEditable` | `bool` | `true` | Whether dragging vertically on the CRT display scrub modifies the amplitude. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `CustomLabel` | `string` | `null` | Optional custom label prefix rendered beside the oscilloscope display. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AudioDspFilter : MonoBehaviour
{
    [Header("Oscillator Resonance")]
    [LiveOscilloscopeWave(
        waveHeight: 55f, 
        phosphorColor: "#00E5FF", 
        maxValue: 10f, 
        WaveSpeed = 3.5f, 
        WaveComplexity = 4.0f,
        CustomLabel = "LFO Resonance"
    )]
    public float filterResonance = 4.2f;

    [Header("Dynamic Waveform with Member Bound")]
    [LiveOscilloscopeWave(nameof(GetMaxAmplitude), waveHeight: 45f, phosphorColor: "#39FF14")]
    public float modulationAmplitude = 1.8f;

    private float GetMaxAmplitude() => 5.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | CRT displays frame cleanly inside box groups and collapsible sections. |
| `[AudioReactivePulse]` | Stacking | Pairs seamlessly to add rhythmic pulses to the oscilloscope row during audio playback. |
| Arrays & Lists | Supported | Implements `ICollectionElementAttribute` to render CRT waveforms inside serialized lists. |
