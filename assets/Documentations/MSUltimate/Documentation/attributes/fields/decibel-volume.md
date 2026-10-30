# [DecibelVolume]

> Transforms a volume field into a logarithmic Audio Decibel (dB) slider with a VU meter, mute toggle, and linear readouts.

---

## 1. Overview & Value Proposition

**What it does:**
Converts standard linear volume floats into a professional audio mixer slider measured in Decibels (dB) with a live VU meter and mute toggle.

**The Problem:**
Human hearing perceives loudness logarithmically, not linearly. Setting volumes with simple 0.0 to 1.0 sliders makes subtle adjustments at lower volumes impossible and requires tedious manual `20 * log10(volume)` calculations when interfacing with Unity's AudioMixer.

**The Solution:**
Add `[DecibelVolume]` to any audio volume field:
- **True Logarithmic Audio Slider:** Scales naturally from silence (`-80 dB`) up to unity gain (`0 dB`) and boosted gain (`+6 dB`).
- **Visual LED / VU Level Meter:** Renders an authentic multi-colored audio level meter bar beside the slider.
- **One-Click Mute Speaker:** Quickly mute and unmute audio channels during play testing.
- **Dual Serialization Modes:** Store as standard Linear amplitude ($0.0-1.0$) or directly as raw Decibels for `AudioMixer.SetFloat`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioChannel : MonoBehaviour
{
    [DecibelVolume(-80f, 6f)]
    public float busVolumeLinear = 1f;

    [DecibelVolume(-80f, 0f, storeAsDecibels: true)]
    public float mixerChannelDecibels = 0f;
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
public DecibelVolumeAttribute(float minDb = -80f, float maxDb = 6f, bool storeAsDecibels = false)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `minDb` | `float` | `-80f` | Minimum decibel value (representing complete silence). |
| `maxDb` | `float` | `6f` | Maximum decibel value (`0 dB` is unity gain, `>0 dB` is boosted). |
| `storeAsDecibels` | `bool` | `false` | If `true`, serializes raw dB; if `false`, stores linear amplitude ($0.0-1.0$). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinDb` | `float` | `-80f` | Lower bound decibel value. |
| `MaxDb` | `float` | `6f` | Upper bound decibel value. |
| `StoreAsDecibels` | `bool` | `false` | Serialization storage mode toggle. |
| `ShowVuMeter` | `bool` | `true` | Displays visual LED / VU meter bar. |
| `ShowLinearPercentage` | `bool` | `true` | Shows linear percentage text (e.g. "75.4%"). |
| `ShowPresets` | `bool` | `true` | Displays quick jump buttons (Mute, -12dB, -6dB, 0dB, +3dB). |
| `ShowMuteToggle` | `bool` | `true` | Displays 1-click speaker mute button. |
| `BackgroundColor` | `string` | `"#1E1E28"` | Background container card hex color. |
| `BorderColor` | `string` | `"#323242"` | Border card outline hex color. |
| `BorderRadius` | `float` | `6f` | Corner radius of the widget card in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using UnityEngine.Audio;
using MaharajaStudio.MSUltimate.Runtime;

public class MasterAudioMixerController : MonoBehaviour
{
    [Header("Audio Mixer Binding")]
    public AudioMixer masterMixer;

    [Header("Buses (Stored As Raw dB)")]
    [DecibelVolume(-80f, 0f, storeAsDecibels: true, ShowPresets = true)]
    public float masterBusVolume = 0f;

    [DecibelVolume(-60f, 6f, storeAsDecibels: true)]
    public float sfxBusVolume = -3f;

    [Header("Music Bus (Linear 0.0 - 1.0)")]
    [DecibelVolume(-80f, 0f, storeAsDecibels: false, ShowLinearPercentage = true)]
    public float musicLinearGain = 0.85f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Functions cleanly inside grouped mixer racks. |
| `[ReadOnly]` | Supported | Mute and presets are locked; functions as a visual decibel monitor. |
| `[ShowIf]` | Supported | Dynamically display advanced channel strips only when mixer buses are active. |
