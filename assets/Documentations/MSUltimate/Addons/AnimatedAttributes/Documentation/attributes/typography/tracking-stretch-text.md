# TrackingStretchText

> `[TrackingStretchText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

Standard inspector labels feature fixed character kerning that remains static regardless of user interaction. In luxury, editorial, or prestige game interfaces (e.g. RPG item cards, boss title cards, achievements), subtle kinetic typography elevates developer ergonomics.

`[TrackingStretchText]` smoothly expands and contracts the horizontal spacing between letters with an elastic spring animation whenever the user hovers over the field. It also supports continuous breathing modes for hero parameters and title headings.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class RelicInspector : MonoBehaviour
{
    [TrackingStretchText(5f, 12f, "#38BDF8")]
    public string RelicTitle = "CHRONICLES OF AVALON";
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (4px stretch tracking, spring speed 12, sky blue highlight)
public TrackingStretchTextAttribute();

// Parameterized constructor with custom stretch spacing, spring speed, and highlight color
public TrackingStretchTextAttribute(float stretchTracking, float springSpeed = 12f, string highlightColor = "#38BDF8");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `StretchTracking` | `float` | `4f` | Maximum horizontal spacing in pixels added between characters when expanded. |
| `SpringSpeed` | `float` | `12f` | Spring lerp interpolation speed for expansion and contraction. |
| `HighlightColor` | `string` | `"#38BDF8"` | Accent color applied to text in the expanded hover state (hex code). |
| `Continuous` | `bool` | `false` | When true, continuously pulses tracking width in an idle breathing wave. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class HeroPrestigeInspector : ModularMonoBehaviour
{
    [Title("Editorial Showcase", "Kinetic kerning on inspector fields", BackgroundColor = "#082f49", TextColor = "#38BDF8")]

    [BoxGroup("Hero Attributes")]
    [TrackingStretchText(5f, 12f, "#38BDF8")]
    public string ChampionName = "VALERIUS THE UNVANQUISHED";

    [BoxGroup("Hero Attributes")]
    [TrackingStretchText(4f, 10f, "#FBBF24", Continuous = true)]
    public float PrestigeMultiplier = 3.5f;

    [BoxGroup("Equipped Titles")]
    public List<TitleCard> ActiveTitles = new List<TitleCard>
    {
        new TitleCard("DEFENDER OF SUNSPIRE", 1200),
        new TitleCard("VOID WALKER MASTER", 3500)
    };

    [Serializable]
    public class TitleCard
    {
        [TrackingStretchText(4.5f, 14f, "#F472B6")]
        public string TitleDesignation;

        public int HonorScore;

        public TitleCard(string designation, int score)
        {
            TitleDesignation = designation;
            HonorScore = score;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[AdvancedClass]`** | Compatible | Dynamic margin expands without overflowing parent card boundaries. |
| **`[ReadOnly]`** | Compatible | Text continues to stretch smoothly on hover even when editing is locked. |
| **Lists (`List<TClass>`)** | Compatible | Safely restores original margin during virtualized row recycling. |

---

## 7. Performance & Architecture

- **Sub-pixel Layout Safety:** Only adjusts `marginRight` on child letter elements, preventing layout recalculation on sibling controls.
- **Damped Spring Math:** Fast analytical lerp runs at 60 fps only during active transitions, sleeping when rest position is reached.

