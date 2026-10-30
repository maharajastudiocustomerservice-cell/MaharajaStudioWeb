# [AudioReactivePulse]

> Pulses field scale and border glow dynamically in sync with live audio spectrum beats and bass frequencies.

---

## 1. Overview & Value Proposition

**What it does:**
`[AudioReactivePulse]` analyzes live game audio or editor preview playback and pulses the decorated field in real-time rhythm with low-frequency bass hits. When audio plays, the field scale expands up to `MaxScale` while radiating an energetic chromatic border glow (`BeatColor`), driven by an adjustable bass sensitivity factor (`BassSensitivity`).

**The Problem:**
Audio directors and sound designers frequently tune sound parameters—volume rolloff curves, DSP filter resonance, synth bass parameters—without visual cues on whether beats or drops are registering correctly in the engine.

**The Solution:**
Decorating audio-driven parameters with `[AudioReactivePulse]`:
- **Real-Time Spectrum Synchronization:** Binds inspector controls directly to active audio analysis channels.
- **Rhythmic Bass Detection:** Emphasizes kick drums, 808 subs, and low-frequency transients to create an organic, pulsing rhythm.
- **Customizable Beat Aesthetics:** Tailor the peak scale expansion (`MaxScale`) and glowing border shade (`BeatColor`).
- **Low-Overhead Analysis:** Reads shared fast-Fourier-transform (FFT) spectrum buffers with negligible CPU cost.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class RhythmTrackManager : MonoBehaviour
{
    [AudioReactivePulse(sensitivity: 1.8f, BeatColor = "#EC4899")]
    public float masterMusicVolume = 0.85f;
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
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AudioReactivePulseAttribute(float sensitivity = 1.5f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `sensitivity` | `float` | `1.5f` | Sensitivity multiplier for low-frequency bass beat triggers. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BassSensitivity` | `float` | `1.5f` | Sensitivity multiplier applied to bass spectrum frequency bands. |
| `MaxScale` | `float` | `1.06f` | Maximum scale multiplier reached during peak beat impacts. |
| `BeatColor` | `string` | `"#A855F7"` | Hex color string for the border glow and accent pulse on beat peaks. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class MusicBeatController : MonoBehaviour
{
    [Header("Audio Spectrum Reactivity")]
    [AudioReactivePulse(sensitivity: 2.0f, MaxScale = 1.08f, BeatColor = "#06B6D4")]
    public float bassDropIntensity = 1.0f;

    [Header("Synth Lead Settings")]
    [AudioReactivePulse(sensitivity: 1.2f, BeatColor = "#F59E0B")]
    public float synthPitchCutoff = 800f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Safely pulses within bounded inspector groups without overlapping borders. |
| `[LiveOscilloscopeWave]`| Stacking | Pairs with oscilloscope waveforms to provide both waveform tracing and rhythmic pulse. |
| `[Range]` | Supported | Functions cleanly on slider rows, pulsing both the handle and label during playback. |
