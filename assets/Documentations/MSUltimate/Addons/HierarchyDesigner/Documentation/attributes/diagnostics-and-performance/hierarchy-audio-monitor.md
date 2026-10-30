# [HierarchyAudioMonitor]

> Displays an animated VU volume meter and interactive play/mute toggle button in the hierarchy for AudioSource components.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyAudioMonitor]` embeds live audio telemetry and control directly into the hierarchy row for GameObjects with `AudioSource` components. Driven by `HierarchyAudioMonitorRenderer`, it displays 3 live animated VU meter equalizer bars (`MeterColor = "#2ED573"`) whenever audio is actively playing. When paused or muted, it switches to a clean status icon (`"♫"` or `"✕"` in `MutedColor = "#747D8C"`). Clicking the button immediately toggles `audio.mute` with full Unity Undo registration in Edit Mode and instant muting during Play Mode.

**The Problem:**
Diagnosing audio issues (e.g., sound effects failing to play, runaway audio sources blowing out the master mix, looping ambient sounds playing in the wrong scene) often requires opening the Audio Profiler window or clicking through multiple AudioSource objects in the hierarchy to check playback flags and volume sliders.

**The Solution:**
Decorating audio managers or sound triggers with `[HierarchyAudioMonitor]`:
- **Animated Equalizer Feedback:** Instantly see which AudioSources in the scene are actively emitting sound via animated VU meter bars.
- **One-Click Muting:** Click the hierarchy widget to instantly mute or unmute specific audio sources without deselecting current objects.
- **Full Undo Support:** Audio mute toggles record to the Unity Undo stack (`Undo.RecordObject`).
- **Play Mode & Edit Mode Support:** Visualizes audio previews during both editor testing and runtime gameplay.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[RequireComponent(typeof(AudioSource))]
[HierarchyAudioMonitor(MeterColor = "#10B981", MutedColor = "#64748B")]
public class AmbienceZone : MonoBehaviour
{
    public AudioClip forestAmbience;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class`, `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyAudioMonitorRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyAudioMonitorAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowVuMeter` | `bool` | `true` | Whether to render the live animated volume VU meter bars during active playback. |
| `MeterColor` | `string` | `"#2ED573"` | Hex color of the active VU meter bars. |
| `MutedColor` | `string` | `"#747D8C"` | Hex color used when the audio source is muted or paused. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the audio monitor remains visible and active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[RequireComponent(typeof(AudioSource))]
[HierarchyAudioMonitor(
    ShowVuMeter = true, 
    MeterColor = "#06B6D4", 
    MutedColor = "#94A3B8", 
    XOffset = 6f)]
public class CombatSoundEmitter : MonoBehaviour
{
    private AudioSource _source;

    [Header("Clips")]
    public AudioClip swordSlash;
    public AudioClip shieldImpact;

    private void Awake()
    {
        _source = GetComponent<AudioSource>();
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`AudioSource` Component** | Required | Queries `go.GetComponent<AudioSource>()`; gracefully hides if no `AudioSource` is present. |
| **`[HierarchyToggle]`** | High | Pair with boolean toggles to control other audio system flags (e.g. `loop`, `spatialAudio`). |
| **`[HierarchyIcon]`** | High | Use speaker or music note icons on the left while the interactive VU meter sits on the right. |
| **Undo Stack** | High | Fully integrated with Unity's undo manager; edits register `Undo.RecordObject(audio, "Toggle Audio Mute")`. |
