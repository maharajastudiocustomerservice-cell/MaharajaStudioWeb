# EqualizerText

> `[EqualizerText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In audio management, rhythm games, soundtrack mixing, or combat intensity systems, static text fails to convey acoustic energy. Standard Unity inspectors require opening specialized audio profiler windows just to verify if sound parameters are active.

`[EqualizerText]` converts each character in the field label into an individual frequency band on a graphic equalizer. Characters bounce vertically with multi-octave acoustic harmonics and peak color accents, instantly conveying rhythmic pulse and audio energy directly on mixer buses and volume parameters.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AudioBuses : MonoBehaviour
{
    [EqualizerText(6f, 3.5f, "#EC4899")]
    public float BassHeavyMixer = -2.5f;
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (6px max height, 3.2 Hz tempo, pink peak color)
public EqualizerTextAttribute();

// Parameterized constructor with custom height, tempo, and peak color
public EqualizerTextAttribute(float maxBounceHeight, float beatFrequency = 3.2f, string peakColor = "#EC4899");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `MaxBounceHeight` | `float` | `6f` | Maximum vertical displacement reached by peak frequency characters. |
| `BeatFrequency` | `float` | `3.2f` | Beat rhythm tempo and oscillation speed in hertz. |
| `CenterBias` | `bool` | `true` | When true, center characters achieve higher peak amplitudes than edges (bell curve EQ). |
| `PeakColor` | `string` | `"#EC4899"` | Color accent applied to characters at the top of their bounce (hex code). |
| `Continuous` | `bool` | `true` | When true, animates continuously; otherwise animates only on hover. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SoundboardMaster : ModularMonoBehaviour
{
    [Title("Mixer Console", "Live audio bus telemetry and equalizer readouts", BackgroundColor = "#3b0764", TextColor = "#F472B6")]

    [BoxGroup("Master Channels")]
    [EqualizerText(6f, 3.5f, "#EC4899")]
    public string MainThemeTrack = "SYNTHWAVE_NEON_CRUISE";

    [BoxGroup("Master Channels")]
    [EqualizerText(8f, 5f, "#A855F7", CenterBias = true)]
    public float SubwooferGain = 6.2f;

    [BoxGroup("Track Playlist")]
    public List<AudioTrack> Playlist = new List<AudioTrack>
    {
        new AudioTrack("CYBER_CHASE_OST", "PLAYING"),
        new AudioTrack("BOSS_FIGHT_ORCHESTRAL", "PAUSED")
    };

    [Serializable]
    public class AudioTrack
    {
        [EqualizerText(5f, 3f, "#38BDF8")]
        public string Title;

        public string Status;

        public AudioTrack(string title, string status)
        {
            Title = title;
            Status = status;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[TabGroup]`** | Compatible | Vertical translation respects overflow boundaries. |
| **`[Slider]` & `[ProgressBar]`** | Compatible | Decorates label independently while value sliders operate smoothly. |
| **Lists (`List<TClass>`)** | Compatible | Sibling container architecture guarantees zero assertion errors in list rows. |

---

## 7. Performance & Architecture

- **Harmonic Wave Synthesis:** Uses closed-form trigonometric combinations (`Sin(t) + Cos(1.6t) * 0.5f`) rather than costly runtime FFT analysis.
- **Zero Allocations:** Evaluates all displacements inline without memory allocations per tick.

