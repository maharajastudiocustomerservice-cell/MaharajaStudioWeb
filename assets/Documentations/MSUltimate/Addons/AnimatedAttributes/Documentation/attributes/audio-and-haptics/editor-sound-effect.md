# [EditorSoundEffect]

> Plays synthesized auditory cues directly in the Unity Editor when interacting with buttons, toggles, or serializable fields.

---

## 1. Overview & Value Proposition

**What it does:**
`[EditorSoundEffect]` brings tactile sound design into the Unity Inspector by playing subtle audio synthesizers or chime presets when a field, property, or method button is clicked or modified. Built-in presets include mechanical clicks, futuristic blips, success chimes, and warning alerts.

**The Problem:**
Editor tooling is overwhelmingly visual. Pressing utility buttons, executing builds, or adjusting mission-critical flags provides no auditory confirmation, leading to accidental double-clicks or uncertainty about whether an action executed.

**The Solution:**
Decorating buttons or fields with `[EditorSoundEffect]`:
- **Auditory Affirmation:** Confirms interactions with crisp, satisfying audio feedback.
- **5 Built-In Presets:** Choose from `Click`, `Tick`, `SciFiBlip`, `SuccessChime`, and `WarningBeep`.
- **Pitch Modulation:** Fine-tune playback `Pitch` to differentiate actions across a single panel.
- **Method & Button Support:** Applies to both fields/properties and `[Button]` / `Method` invokers.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class BuildUtility : MonoBehaviour
{
    [EditorSoundEffect(EditorSoundPreset.SuccessChime, Pitch = 1.1f)]
    public void BakeLightingAndNavMesh()
    {
        Debug.Log("Baking completed successfully!");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serializable field, property, collection item, or button method |
| **Collection Cascading** | Supported (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>` via `ICollectionElementAttribute`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public EditorSoundEffectAttribute(EditorSoundPreset sound = EditorSoundPreset.Click)
public EditorSoundEffectAttribute(EditorSoundPreset sound, float pitch)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `sound` | `EditorSoundPreset` | `EditorSoundPreset.Click` | Preset sound effect played on interaction. |
| `pitch` | `float` | `1.0f` | Playback pitch multiplier for the sound effect. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `SoundPreset` | `EditorSoundPreset` | `Click` | Audio preset enum (`Click`, `Tick`, `SciFiBlip`, `SuccessChime`, `WarningBeep`). |
| `Pitch` | `float` | `1.0f` | Playback pitch multiplier for the sound effect. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

### `EditorSoundPreset` Enumeration

| Enum Value | Description |
| :--- | :--- |
| `Click` | Subtle tactile mechanical switch click. |
| `Tick` | Light high-frequency tick for stepper adjustments. |
| `SciFiBlip` | High-tech electronic chirp for sci-fi controls. |
| `SuccessChime` | Uplifting melodic bell chime for build or bake completions. |
| `WarningBeep` | Urgent alert tone for destructive or dangerous actions. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

namespace MaharajaStudio.MSUltimate.AnimatedAttributes.Sample
{
    [AddComponentMenu("Maharaja Studio/MSUltimate/Samples/Animated Attributes/Audio And Haptics/Editor Sound Effect Example")]
    public class EditorSoundEffectExample : ModularMonoBehaviour
    {
        // ─── 1. Standalone Tactile Audio Fields ──────────────────────────────────
        [BoxGroup("1. Standalone Tactile Audio Fields", BackgroundColor = "#0F172A", BorderColor = "#2563EB", BorderRadius = 6, MarginBottom = 8)]
        [EditorSoundEffect(EditorSoundPreset.WarningBeep, Pitch = 1.2f)]
        public int emergencyThreatLevel = 3;

        [EditorSoundEffect(EditorSoundPreset.SciFiBlip, Pitch = 0.95f)]
        public string primaryWeaponStatus = "PHOTON-TORPEDOES-ARMED";

        // ─── 2. Inside Class Demonstration ───────────────────────────────────────
        [BoxGroup("2. Inside Class Demonstration", BackgroundColor = "#0D1E36", BorderColor = "#0284C7", BorderRadius = 6, MarginBottom = 8)]
        public AvionicsSwitchModule primaryAvionicsSwitch = new AvionicsSwitchModule();

        [System.Serializable]
        public class AvionicsSwitchModule
        {
            [EditorSoundEffect(EditorSoundPreset.Click, Pitch = 1.1f)]
            public string subsystemName = "Auxiliary Core Coolant";

            [EditorSoundEffect(EditorSoundPreset.Tick, Pitch = 1.3f)]
            public float pressureBar = 14.8f;
        }

        // ─── 3. Direct Collections Cascading Showcase ────────────────────────────
        [BoxGroup("3. Direct Collections Cascading Showcase", BackgroundColor = "#0B182B", BorderColor = "#1D4ED8", BorderRadius = 6, MarginBottom = 8)]
        [InfoBox("Direct collection cascading: [EditorSoundEffect] implements ICollectionElementAttribute to automatically play synthesized tactile sound feedback when modifying individual items in arrays and lists.", InspectorMessageType.Info)]

        [EditorSoundEffect(EditorSoundPreset.Click, 1.2f)]
        public string[] subsystemCallsigns = new string[] { "ALPHA-01", "BRAVO-02", "CHARLIE-03" };

        [EditorSoundEffect(EditorSoundPreset.Tick, 0.9f)]
        public List<float> calibrationFrequencies = new List<float> { 142.5f, 285.0f, 427.5f };

        // ─── 4. Interactive Soundboard Playground ─────────────────────────────────
        [BoxGroup("4. Interactive Soundboard Playground", BackgroundColor = "#13233D", BorderColor = "#38BDF8", BorderRadius = 6)]
        [EditorSoundEffect(EditorSoundPreset.SuccessChime, Pitch = 1.0f)]
        [Button("Deploy Landing Clamps", BackgroundColor = "#10B981", TextColor = "#FFFFFF")]
        public void DeployLandingClamps()
        {
            Debug.Log("[EditorSoundEffect] Deployed landing clamps with audio feedback!");
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### Attribute Stacking

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Fires sound feedback each time the inspector button is triggered. |
| `[ClickRipple]` | Supported | Pairs visual ripple feedback with crisp auditory clicks for complete tactile response. |
| `[ParticleBurst]` | Supported | Delivers both celebratory audio chimes and visual particle sparks. |

### Collection Cascading Matrix

| Collection Type | Element Type | Supported | Notes |
| :--- | :--- | :---: | :--- |
| `T[]` (Array) | `string[]`, `float[]`, `int[]`, objects | Yes | Synthesizes tactile sound feedback on interacting with individual array elements. |
| `List<T>` | `List<string>`, `List<float>`, `List<T>` | Yes | Cascades down to individual list elements automatically. |
| `AdvancedList<T>` | Any element type | Yes | Fully supported in reorderable list items. |
| `SerializableDictionary<K, V>` | Key or Value elements | Yes | Triggers audio feedback on interacting with dictionary items. |
| `[Serializable] class/struct` | Nested properties | Yes | Plays sound effects when modifying fields inside nested classes. |
| `Method / [Button]` | Methods | Yes | Plays configured audio preset upon method button invocation. |

