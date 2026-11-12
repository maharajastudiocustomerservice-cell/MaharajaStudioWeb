# GravityDropText

> `[GravityDropText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In arcade cabinets, pinball machines, platformer games, or physics-driven puzzlers, standard text displays lack physical weight. When a player achieves a jackpot or unlocks a rare item, static text fails to deliver the celebratory impact of a physical drop.

`[GravityDropText]` simulates authentic Newtonian gravity physics. When triggered, characters drop down from above the baseline with gravitational acceleration ($9.8\text{ m/s}^2$), bouncing and settling to rest with realistic coefficient-of-restitution damping and impact color flashes.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PinballScoreboard : MonoBehaviour
{
    [GravityDropText(14f, 9.8f, 0.45f)]
    public int JackpotScore = 1500000;
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (14px drop height, 9.8 gravity, 0.45 bounciness)
public GravityDropTextAttribute();

// Parameterized constructor with custom drop height, gravity acceleration, and bounciness
public GravityDropTextAttribute(float dropHeight, float gravity = 9.8f, float bounciness = 0.45f);
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `DropHeight` | `float` | `14f` | Initial vertical drop displacement in pixels above the baseline. |
| `Gravity` | `float` | `9.8f` | Downward gravitational acceleration factor. |
| `Bounciness` | `float` | `0.45f` | Coefficient of restitution (0.0 to 1.0) governing bounce height decay. |
| `StaggerDelay` | `float` | `35f` | Stagger delay in milliseconds between consecutive falling characters. |
| `ImpactColor` | `string` | `"#F59E0B"` | Flash highlight color applied upon ground contact (hex code). |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ArcadeScoreMachine : ModularMonoBehaviour
{
    [Title("Pinball Arcade", "Newtonian falling text and ground impact bounce", BackgroundColor = "#451a03", TextColor = "#FBBF24")]

    [BoxGroup("Arcade Scores")]
    [GravityDropText(14f, 9.8f, 0.45f)]
    public int JackpotPoints = 1250000;

    [BoxGroup("Arcade Scores")]
    [GravityDropText(20f, 14f, 0.6f, StaggerDelay = 45f, ImpactColor = "#EC4899")]
    public string BossLootBanner = "LEGENDARY_RELIC_ACQUIRED";

    [BoxGroup("Leaderboard")]
    public List<ScoreSlot> HighScorers = new List<ScoreSlot>
    {
        new ScoreSlot("ACE_GUNNER_X", "GRANDMASTER"),
        new ScoreSlot("SHADOW_VIPER_99", "DIAMOND")
    };

    [Serializable]
    public class ScoreSlot
    {
        [GravityDropText(14f, 9.8f, 0.45f)]
        public string PilotCallsign;

        public string RankTier;

        public ScoreSlot(string callsign, string tier)
        {
            PilotCallsign = callsign;
            RankTier = tier;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[TabGroup]`** | Compatible | Vertical drop displacement respects parent container margins. |
| **`[Button]` Actions** | Compatible | Excellent trigger partner for simulation test buttons. |
| **Lists (`List<TClass>`)** | Compatible | Sibling container architecture guarantees clean row recycling. |

---

## 7. Performance & Architecture

- **Euler Physics Integration:** Calculates velocity, acceleration, and bounce damping numerically without running Unity's PhysX engine.
- **Sleep on Rest:** Animation loop halts automatically once all letters reach velocity threshold $< 1.5\text{ px/s}$.

