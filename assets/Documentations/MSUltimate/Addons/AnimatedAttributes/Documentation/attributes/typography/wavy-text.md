# [WavyText]

> Animates characters in field labels with a fluid, undulating vertical sine wave oscillation.

---

## 1. Overview & Value Proposition

**What it does:**
`[WavyText]` converts static field labels into an undulating water wave ripple. It splits the label text into individual character elements and continuously oscillates them along the Y-axis using sinusoidal phase offsets ($y = \sin(\text{time} \cdot 2\pi \cdot \text{WaveFrequency} + i \cdot \text{CharacterPhaseShift}) \cdot \text{WaveAmplitude}$). With customizable vertical amplitude (`WaveAmplitude`, defaulting to 3.5px), frequency (`WaveFrequency`, defaulting to 2.5 Hz), and character phase spacing (`CharacterPhaseShift`, defaulting to 0.4 rad), it gives aquatic, psychedelic, or whimsical properties a floating motion. It also supports hover-only triggering (`Continuous = false`).

**The Problem:**
Aquatic systems, wind simulations, audio waveforms, or dreamlike fantasy mechanics often feel dry when presented through rigid, square inspector text. Static labels provide no visual hint that an underlying system is undulating or fluid.

**The Solution:**
Decorating liquid or oscillatory fields with `[WavyText]`:
- **Fluid Wave Motion:** Creates a rolling vertical sine wave across the text without layout jitter or text clipping.
- **Continuous or Hover-Only:** Set `Continuous = true` for ambient kinetic presence, or `false` for interactive hover-triggered ripples.
- **Adjustable Wave Dynamics:** Tune peak amplitude from gentle 1.5px water laps up to pronounced 6px tidal crests.
- **Independent Phase Offsets:** Staggers individual character delays via `CharacterPhaseShift` to maintain seamless wave continuity across strings of any length.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class OceanBuoyancyManager : MonoBehaviour
{
    [WavyText(amplitude: 4.0f, frequency: 2.2f)]
    public float oceanWaveHeight = 2.75f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **Collection Support** | Supported on fields in wrapper classes (`List<MyClass>`); Direct collection cascading is intentionally not supported. |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public WavyTextAttribute()

public WavyTextAttribute(float amplitude, float frequency)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `amplitude` | `float` | `3.5f` | Peak vertical amplitude displacement in pixels. |
| `frequency` | `float` | `2.5f` | Frequency of the sine wave in cycles per second. |

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `WaveAmplitude` | `float` | `3.5f` | Maximum vertical pixel displacement from baseline. |
| `WaveFrequency` | `float` | `2.5f` | Oscillation frequency in complete wave cycles per second. |
| `CharacterPhaseShift` | `float` | `0.4f` | Phase offset between consecutive characters in radians. |
| `Continuous` | `bool` | `true` | If true, ripples indefinitely; if false, ripples only while hovered by the cursor. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class LiquidBiomeController : MonoBehaviour
{
    [Header("Aquatic Simulation Parameters")]
    [WavyText(amplitude: 3.0f, frequency: 1.8f, CharacterPhaseShift = 0.35f)]
    public float fluidViscosity = 1.2f;

    [WavyText(amplitude: 4.5f, frequency: 3.0f, Continuous = true)]
    public string currentTideState = "HIGH_TIDE";

    [Header("Interactive Dream Properties")]
    [WavyText(amplitude: 5.0f, frequency: 2.5f, Continuous = false)]
    public float hallucinationStrength = 0.85f;

    [Header("Wrapper Classes in Lists")]
    public List<MarineSpecimen> marineSpecimens = new List<MarineSpecimen>
    {
        new MarineSpecimen { specimenName = "Bioluminescent Jellyfish", depthMeters = 1200f }
    };

    [Serializable]
    public class MarineSpecimen
    {
        [WavyText(amplitude: 3.5f, frequency: 2.2f)]
        public string specimenName = "Pelagic Leviathan";

        public float depthMeters = 3000f;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### 7.1 Layout & Conditional Stacking

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[BoxGroup]` / `[HorizontalGroup]`** | High | Works smoothly within grouped panels; preserves horizontal text alignments. |
| **`[ShowIf]` / `[EnableIf]`** | High | Seamlessly restarts or pauses wave oscillations during conditional visibility changes. |
| **`[BouncingText]` / `[GradientTextFlow]`** | Avoid | Only one text-mutation attribute should be applied to a single label at a time. |
| **Validation Attributes** | High | Fully compatible with `[Required]`, `[Range]`, and `[ValidateNotNull]`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Not Supported | Direct arrays are intentionally not cascaded. |
| **Generic Lists (`List<T>`)** | Not Supported | Direct lists are intentionally not cascaded. |
| **Wrapper Classes in Lists (`List<MyClass>`)** | Supported | Operates seamlessly on nested class fields when rendered inline or within collections. |
| **Unity UI Toolkit** | Supported | Integrates with UI Toolkit visual tree scheduler for smooth 60fps undulations. |
