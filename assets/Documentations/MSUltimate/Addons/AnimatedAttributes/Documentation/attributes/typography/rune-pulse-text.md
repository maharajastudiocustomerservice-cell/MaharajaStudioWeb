# RunePulseText

> `[RunePulseText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In fantasy RPGs, magic systems, mythology games, or enchanted relic crafting, static text feels profane and mundane. Spell names, ancient runes, and divine relics require an aura of mystical power that static font styles cannot deliver.

`[RunePulseText]` simulates celestial or eldritch energy traveling through engraved stone runes. An illumination wave sweeps rhythmically across the characters, elevating energized letters with a graceful upward float and bathing them in luminous arcane violet or divine solar gold.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class MysticGrimoire : MonoBehaviour
{
    [RunePulseText(2.2f, 3.5f, "#C084FC")]
    public string Inscription = "EXCALIBUR_ETERNAL_SOVEREIGN";
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (2.2 Hz pulse speed, 3.5 character wave width, arcane violet glow)
public RunePulseTextAttribute();

// Parameterized constructor with custom speed, wave width, and rune color
public RunePulseTextAttribute(float pulseSpeed, float pulseWidth = 3.5f, string runeColor = "#C084FC");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `PulseSpeed` | `float` | `2.2f` | Wave progression speed in cycles per second. |
| `PulseWidth` | `float` | `3.5f` | Width of the illumination wave in character units. |
| `RuneColor` | `string` | `"#C084FC"` | Luminous rune glow color at the peak of the wave (hex code). |
| `BaseColor` | `string` | `""` | Optional inactive text color before energy passes through (hex code). |
| `LiftHeight` | `float` | `2.5f` | Upward floating displacement in pixels applied at the wave crest. |
| `Continuous` | `bool` | `true` | When true, animates continuously; otherwise pulses only on hover. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AncientSanctuaryInspector : ModularMonoBehaviour
{
    [Title("Eldritch Obelisk", "Ancient inscribed runes and divine celestial energy", BackgroundColor = "#2e1065", TextColor = "#D8B4FE")]

    [BoxGroup("Elder Inscriptions")]
    [RunePulseText(2.2f, 3.5f, "#C084FC")]
    public string MonolithInscription = "EXCALIBUR_ETERNAL_SOVEREIGN";

    [BoxGroup("Elder Inscriptions")]
    [RunePulseText(3.0f, 4.0f, "#FBBF24", LiftHeight = 3.5f)]
    public float HolyAuraMultiplier = 4.85f;

    [BoxGroup("Socketed Glyphs")]
    public List<GlyphSlot> ActiveGlyphs = new List<GlyphSlot>
    {
        new GlyphSlot("RUNE_OF_CELESTIAL_AEGIS", "EMPOWERED"),
        new GlyphSlot("SIGIL_OF_STARLIGHT_VOID", "CHARGING")
    };

    [Serializable]
    public class GlyphSlot
    {
        [RunePulseText(2.4f, 3.0f, "#FDE047")]
        public string GlyphTitle;

        public string Status;

        public GlyphSlot(string title, string status)
        {
            GlyphTitle = title;
            Status = status;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[AdvancedClass]`** | Compatible | Vertical character float respects parent group bounds. |
| **`[ReadOnly]`** | Compatible | Wave pulses normally on locked lore or non-editable narrative strings. |
| **Lists (`List<TClass>`)** | Compatible | Safe segmented container prevents visual corruption during list item re-ordering. |

---

## 7. Performance & Architecture

- **Distance-Based Hermite Interpolation:** Uses `SmoothStep` over normalized character distances for organic, non-linear bell curve illumination.
- **Single Pass State:** Evaluates both vertical translation and color lerp in a single 16ms pass per character.

