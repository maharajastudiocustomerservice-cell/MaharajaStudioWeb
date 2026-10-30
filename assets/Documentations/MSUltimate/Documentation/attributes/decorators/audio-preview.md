# [AudioPreview]

> Renders an interactive waveform player with Play, Pause, Scrubbing, and Volume controls directly beneath AudioClip fields.

---

## 1. Overview & Value Proposition

**What it does:**
Embeds a playable sound preview card with an audio waveform directly in the Inspector so you can audition audio clips without entering Play Mode.

**The Problem:**
In standard Unity, auditioning an assigned `AudioClip` requires finding the asset in the Project window and pressing play in the tiny preview strip at the bottom of the screen. When configuring dozens of weapon blasts, footsteps, or UI clicks, this back-and-forth clicking breaks your rhythm.

**The Solution:**
Add `[AudioPreview]` above any `AudioClip` field:
- **1-Click In-Inspector Audio:** Play and pause sound clips right inside the component inspector.
- **Visual Waveform Display:** View peak loudness, duration, and silence gaps on a clean waveform graph.
- **Interactive Scrubber:** Click anywhere along the waveform or progress bar to scrub playback.
- **Volume & Loop Toggles:** Test sound levels and looping seams without writing sound test rigs.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class FootstepAudio : MonoBehaviour
{
    [AudioPreview(WaveformHeight = 40f, WaveformColor = "#2ECC71")]
    public AudioClip grassStepSound;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `AudioClip` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AudioPreviewAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowWaveform` | `bool` | `true` | Renders the audio frequency waveform graphic. |
| `WaveformHeight` | `float` | `60f` | Height in pixels of the waveform display canvas. |
| `WaveformColor` | `string` | `"#4FC3F7"` | Hex color string for the active waveform lines. |
| `WaveformBackgroundColor` | `string` | `"#1A1A2E"` | Background hex color of the waveform box. |
| `PlayheadColor` | `string` | `"#FF5722"` | Hex color of the moving playback scrubber needle. |
| `ShowVolumeSlider` | `bool` | `true` | Displays an inline volume slider control. |
| `DefaultVolume` | `float` | `0.8f` | Initial preview playback volume (`0.0f` to `1.0f`). |
| `ShowLoopToggle` | `bool` | `true` | Displays a toggle button to test looping audio clips. |
| `Loop` | `bool` | `false` | Default loop state for playback. |
| `ShowTimestamp` | `bool` | `true` | Shows current elapsed time and total duration readouts. |
| `AutoPlay` | `bool` | `false` | Automatically starts playback when a new clip is assigned. |
| `PlaylistMode` | `bool` | `true` | When decorating a list of clips, renders a Jukebox playlist player instead of separate cards. |
| `BorderRadius` | `float` | `6f` | Corner rounding radius of the player card. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class WeaponAudioPlayer : MonoBehaviour
{
    [Header("Weapon Sound Effects")]
    [AudioPreview(
        WaveformHeight = 50f,
        WaveformColor = "#E74C3C",
        WaveformBackgroundColor = "#11111E",
        ShowVolumeSlider = true,
        DefaultVolume = 0.9f
    )]
    public AudioClip gunFireSound;

    [AudioPreview(ShowWaveform = false, ShowLoopToggle = true)]
    public AudioClip reloadLoopSound;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Integrates cleanly inside audio categories or tab sections. |
| `[ShowIf]` | Supported | Conditionally reveals sound previews when sound options are enabled. |
| `[DrawCollection]` | Supported | Functions smoothly inside serialized lists of sound variations. |
