# RubberBandText

> `[RubberBandText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In hyper-casual mobile games, cartoon platformers, match-3 titles, or tactile toy mechanics, standard inspector interfaces feel rigid and utilitarian. Developers crafting juicy mechanics benefit from having the same playful squash-and-stretch feedback present in their tooling.

`[RubberBandText]` applies volume-preserving cartoon squash-and-stretch wobble physics to field labels on hover or click. Characters expand horizontally while compressing vertically (`scale.x = 1.35, scale.y = 0.74`), snapping back with an organic damped spring oscillation that feels deliciously tactile.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class JellySlimeSpawner : MonoBehaviour
{
    [RubberBandText(1.35f, 16f, "#EC4899")]
    public float SlimeBounciness = 1.85f;
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (1.35x stretch factor, 16 Hz wobble speed, bubblegum pink)
public RubberBandTextAttribute();

// Parameterized constructor with custom stretch factor, wobble speed, and stretch color
public RubberBandTextAttribute(float stretchFactor, float wobbleSpeed = 16f, string stretchColor = "#EC4899");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `StretchFactor` | `float` | `1.35f` | Horizontal stretch ratio at peak elastic expansion. |
| `WobbleSpeed` | `float` | `16f` | Damped spring wobble oscillation speed in hertz. |
| `StretchColor` | `string` | `"#EC4899"` | Accent color applied during peak stretch (hex code). |
| `TriggerOnHover` | `bool` | `true` | Whether hovering the mouse over the field triggers the rubber band stretch. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CartoonToyInspector : ModularMonoBehaviour
{
    [Title("Toy Factory", "Volume-preserving cartoon squash-and-stretch physics", BackgroundColor = "#500724", TextColor = "#F472B6")]

    [BoxGroup("Juicy Gameplay Fields")]
    [RubberBandText(1.35f, 16f, "#EC4899")]
    public int CandyMatchCombo = 12;

    [BoxGroup("Juicy Gameplay Fields")]
    [RubberBandText(1.5f, 22f, "#38BDF8")]
    public float JellySlimeBounceFactor = 1.85f;

    [BoxGroup("Toy Manifest")]
    public List<ToySlot> ActiveToys = new List<ToySlot>
    {
        new ToySlot("SPRING_POGO_STICK", "READY"),
        new ToySlot("RUBBER_DUCKY_SUPER", "ARMED")
    };

    [Serializable]
    public class ToySlot
    {
        [RubberBandText(1.35f, 16f, "#F472B6")]
        public string ToyName;

        public string Status;

        public ToySlot(string name, string status)
        {
            ToyName = name;
            Status = status;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[AdvancedClass]`** | Compatible | Container scale transforms cleanly without disturbing parent grid layouts. |
| **`[Button]` Actions** | Compatible | Ideal pairing for interactive gameplay triggers and reward claims. |
| **Lists (`List<TClass>`)** | Compatible | Sibling container layout ensures row recycling causes zero assertion errors. |

---

## 7. Performance & Architecture

- **Volume Conservation:** Computes `scaleY = 1.0f / scaleX` to preserve optical mass throughout the squash and stretch.
- **Exponential Decay Spring:** `Mathf.Exp(-norm * 4.5f)` ensures natural physical settling without infinite micro-jitter.

