# [EndTabGroup]

> Closes an active tab group scope started by [BeginTabGroup], restoring subsequent inspector members to standard full-width layout flow.

---

## 1. Overview & Value Proposition

**What it does:**
Acts as the closing scope delimiter for multi-tab layout groups opened with `[BeginTabGroup]`. Decorating the final member of a tab with `[EndTabGroup]` seals the tab container after rendering that member; all subsequent members in the script render outside the tab container across the full width of the inspector.

**The Problem:**
Without an explicit tab delimiter, any field added to a MonoBehaviour would automatically be trapped inside the very last tab declared in the script. Placing global fields, master action buttons, or status banners below the tab view would be impossible.

**The Solution:**
Decorate the last member of the final tab with `[EndTabGroup]`:
- **Clean Scope Closure:** Seals the tab container cleanly and resets layout state.
- **Global Footer Support:** Allows adding full-width controls, reset buttons, and telemetry below the tab view.
- **Defensive Layout Recovery:** Prevents GUI tree corruptions even if tab indices are mismatched.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterRig : MonoBehaviour
{
    // Tab 1: Stats
    [BeginTabGroup("Stats")]
    public int health = 100;

    // Tab 2: Audio
    [BeginTabGroup("Audio")]
    [EndTabGroup] // Closes the tab container after rendering footstepClip
    public AudioClip footstepClip;

    // Renders full-width below the tabs
    public bool isInitialized = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any member closing a tab group scope |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | Handled natively by MSUltimate Inspector layout engine |

---

## 4. Constructors & Parameters

```csharp
public EndTabGroupAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `AttributeCategory`| `LayoutGroup` | Categorizes this attribute as a structural layout delimiter. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameAudioDirector : MonoBehaviour
{
    // Tab 1: Music
    [BeginTabGroup("Music", GroupName = "AudioTabs", TabIcon = "d_AudioSource Icon")]
    public AudioSource musicSource;
    public float musicVolume = 0.8f;

    // Tab 2: Sound FX
    [BeginTabGroup("Sound FX", GroupName = "AudioTabs", TabIcon = "d_SpeakerIcon")]
    public AudioSource sfxSource;
    public float sfxVolume = 1.0f;

    // Tab 3: Voice
    [BeginTabGroup("Voice", GroupName = "AudioTabs", TabIcon = "d_Microphone")]
    public AudioSource voiceSource;
    [EndTabGroup] // Closes the AudioTabs group after rendering voiceVolume
    public float voiceVolume = 0.9f;

    // Full-width controls outside the tab system
    [Header("Master Controls (Global Below Tabs)")]
    [Range(0f, 1f)]
    public float masterVolume = 1.0f;

    [Button("Stop All Audio Channels")]
    public void StopAllAudio()
    {
        Debug.Log("All audio playback stopped.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BeginTabGroup]` | Mandatory Pair | Must follow a preceding `[BeginTabGroup]` declaration. |
| `[Button]` | Supported | Can decorate a method button to finish the tab and trigger an action simultaneously. |
| `[BoxGroup]` | Supported | New box groups can be started immediately after `[EndTabGroup]`. |
