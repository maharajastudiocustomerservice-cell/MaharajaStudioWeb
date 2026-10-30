# [ComponentEqualizer]

> Renders an animated audio spectrum analyzer equalizer along the top or bottom border of the component card with bouncing vertical frequency bars.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentEqualizer]` introduces real-time audio spectrum visualization aesthetics to Unity component cards. Docked to either the top or bottom edge (`WaveEdge.Top` or `WaveEdge.Bottom`), it animates a row of rhythmic frequency bars bouncing smoothly between min and peak heights (`MaxHeight`). It supports two-tone gradient bar coloring (`Color` and `SecondaryColor`), customizable bar counts (`Bars`), inter-bar spacing (`Gap`), oscillation tempo (`Speed`), transparency (`Opacity`), and layering (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`).

**The Problem:**
Audio managers, dynamic music controllers, sound synthesizer modules, and VO soundboards appear identical to non-acoustic gameplay scripts in standard Unity inspectors. Developers and sound designers lack instant visual cues that a component handles audio frequencies.

**The Solution:**
Decorating sound systems with `[ComponentEqualizer]`:
- **Dynamic Frequency Bar Animation:** Simulates real-time multi-band EQ analysis using sine-based harmonics and pseudo-random frequency heights.
- **Dual-Color Gradient Spectrum:** Blends smoothly from primary low-frequency tones (`Color`) to secondary treble-frequency highlights (`SecondaryColor`).
- **Edge-Docked Precision:** Neatly anchors along either card edge without encroaching upon or distorting serialized inspector fields.
- **Zero-Friction Interaction:** Operates with `PickingMode.Ignore`, ensuring sliders, volume curves, and audio clip slots remain fully clickable.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentEqualizer(Color = "#00E676", SecondaryColor = "#FFD600", Bars = 16, MaxHeight = 22f, Speed = 2f)]
public class AdaptiveAudioEngine : MonoBehaviour
{
    public float masterVolumeDb = -3.5f;
    public float combatIntensity = 0.75f;
    public bool isSpatialAudioEnabled = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `ContentOverlay` (if `Behind = true`) or `BodyOverlay` (if `Behind = false`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentEqualizerAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#4FC3F7"` | Hex color string for base frequency bars. |
| `SecondaryColor` | `string` | `"#FF4081"` | Hex color string for high-frequency bar peaks or gradient tint. |
| `Bars` | `int` | `12` | Total number of vertical equalizer bars rendered across the edge. |
| `MaxHeight` | `float` | `20f` | Maximum vertical height in pixels for active frequency bars. |
| `Gap` | `float` | `2f` | Spacing gap in pixels between adjacent equalizer bars. |
| `Speed` | `float` | `1.5f` | Oscillation and bounce tempo multiplier. |
| `Opacity` | `float` | `0.5f` | Transparency alpha of the equalizer elements (0.0 to 1.0). |
| `Edge` | `WaveEdge` | `WaveEdge.Bottom` | Edge placement (`WaveEdge.Bottom` or `WaveEdge.Top`). |
| `Behind` | `bool` | `false` | When true, renders behind inspector fields; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#8B5CF6", Width = 2f, Radius = 8f)]
[ComponentBackground("#130E26", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("SYNTHESIZER CORE", Subtitle = "Dynamic DSP & Filter Matrix", BackgroundColor = "#1F1538", TitleColor = "#EDE9FE")]
[ComponentEqualizer(Color = "#A78BFA", SecondaryColor = "#F472B6", Bars = 18, MaxHeight = 24f, Gap = 3f, Speed = 1.8f, Opacity = 0.6f, Edge = WaveEdge.Bottom, Behind = true)]
public class SynthesizerCore : MonoBehaviour
{
    [Header("Oscillator Settings")]
    public float baseFrequencyHz = 440f;
    [Range(0f, 1f)]
    public float lowPassCutoff = 0.65f;
    [Range(0f, 1f)]
    public float resonanceQ = 0.3f;

    [Header("Reverb & Modulation")]
    public float reverbRoomSize = 0.5f;
    public float lfoModulationRateHz = 2.4f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Dark backdrops allow colorful equalizer bars to glow vividly. |
| **`[ComponentHeader]`** | High | Works well when docked to `WaveEdge.Bottom` opposite a prominent header bar. |
| **Inspector Controls** | High | Transparent mouse input enables immediate interaction with audio sliders and volume meters. |
