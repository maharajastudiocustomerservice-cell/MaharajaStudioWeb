# KaraokeWipeText

> `[KaraokeWipeText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In rhythm games, karaoke jukeboxes, dialogue subtitling, speech audio managers, or voiceover timing tools, developers need visual feedback showing how text timing correlates with audio playback. Static inspector text cannot express left-to-right temporal progression.

`[KaraokeWipeText]` animates a continuous or interactive horizontal sing-along lyric progression from left to right across field label characters. Text transitions smoothly from an inactive unread color into a vibrant active gold or custom highlight, delivering instantaneous rhythm game feedback.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class JukeboxChannel : MonoBehaviour
{
    [KaraokeWipeText(2.2f, "#FBBF24", "#64748B")]
    public string ChorusLyric = "DONT_STOP_BELIEVIN_HOLD_ON";
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (2.0s wipe duration, warm gold active, slate inactive)
public KaraokeWipeTextAttribute();

// Parameterized constructor with custom wipe duration, active color, and inactive color
public KaraokeWipeTextAttribute(float wipeDuration, string activeColor = "#FBBF24", string inactiveColor = "#64748B");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `WipeDuration` | `float` | `2.0f` | Duration of a complete left-to-right lyric wipe in seconds. |
| `ActiveColor` | `string` | `"#FBBF24"` | Active sung lyric highlight color (hex code). |
| `InactiveColor` | `string` | `"#64748B"` | Inactive unplayed lyric color (hex code). |
| `LoopDelay` | `float` | `0.6f` | Pause delay in seconds before looping the wipe. |
| `Continuous` | `bool` | `true` | When true, animates continuously; otherwise wipes only on hover. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class KaraokeStageInspector : ModularMonoBehaviour
{
    [Title("Rhythm Stage", "Lyric progression and karaoke vocal timing", BackgroundColor = "#451a03", TextColor = "#FCD34D")]

    [BoxGroup("Vocal Channels")]
    [KaraokeWipeText(2.2f, "#FBBF24", "#64748B")]
    public string ActiveChorusLine = "DONT_STOP_BELIEVIN_HOLD_ON";

    [BoxGroup("Vocal Channels")]
    [KaraokeWipeText(1.5f, "#EC4899", "#334155", LoopDelay = 0.4f)]
    public float TrackTempoBpm = 128.0f;

    [BoxGroup("Track Queue")]
    public List<SongItem> SongQueue = new List<SongItem>
    {
        new SongItem("BOHEMIAN_RHAPSODY", "PERFECT_SCORE"),
        new SongItem("STAIRWAY_TO_HEAVEN", "QUEUED")
    };

    [Serializable]
    public class SongItem
    {
        [KaraokeWipeText(2.5f, "#34D399", "#64748B")]
        public string Title;

        public string Status;

        public SongItem(string title, string status)
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
| **`[BoxGroup]` & `[AdvancedClass]`** | Compatible | Linear color transition operates cleanly without layout recalculation. |
| **`[Slider]` & `[ProgressBar]`** | Compatible | Excellent partner for track scrubbers and progress bars. |
| **Lists (`List<TClass>`)** | Compatible | Safe segmented container prevents visual artifacts in virtualized rows. |

---

## 7. Performance & Architecture

- **Sub-character Boundary Antialiasing:** Interpolates colors smoothly between adjacent characters at the sweep boundary (`blend = wipeHead - index`).
- **Zero Transform Impact:** Only mutates `style.color`, ensuring $0\text{ ms}$ layout reflow cost.

