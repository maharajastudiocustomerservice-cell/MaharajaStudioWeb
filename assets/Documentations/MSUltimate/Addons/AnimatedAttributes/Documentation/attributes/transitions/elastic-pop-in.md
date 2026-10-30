# [ElasticPopIn]

> Pops inspector fields into view with an elastic overshoot spring scale animation upon initial mount or conditional reveal.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit Scale Transforms)`

---

## 1. Overview & Value Proposition

**What it does:**
`[ElasticPopIn]` introduces dynamic spring physics to inspector elements as they appear on screen. When an element or collection element row attaches to the panel, the drawer starts its scale at zero (`Vector3.zero`). After an optional stagger delay (`Delay`), the element scales up with an elastic overshoot trajectory ($s = \sin(p \cdot \frac{\pi}{2}) + \sin(p \cdot \pi) \cdot (\text{Overshoot} - 1)$), springing outward past 1.0 up to a customizable peak multiplier (`Overshoot`, defaulting to 1.2x) before settling elastically at 1.0 over a designated timeframe (`Duration`, defaulting to 400ms).

**The Problem:**
When toggling conditional properties, expanding new inventory slots, or switching tabs, newly revealed properties appear abruptly with static immediacy. Without dynamic motion, UI state changes feel stiff and lack the polished tactile feedback found in AAA games.

**The Solution:**
Decorating conditionally revealed fields, new components, or collection elements with `[ElasticPopIn]`:
- **Physical Spring Overshoot:** Scales outward past 100% up to `Overshoot` (e.g. 1.2x) before rebounding smoothly to rest.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so adding new slots or viewing collection elements pops each item in with spring physics.
- **Configurable Stagger Delays:** Chain multiple fields together with progressive `Delay` offsets (e.g. 0ms, 50ms, 100ms) for choreographed domino pop-in effects.
- **Hardware-Accelerated UI Scale:** Modifies `StyleScale` directly, keeping inspector performance fluid and smooth.
- **Graceful Lifecycle Cleanup:** Terminates scheduling automatically once `progress >= 1.0f` is reached, ensuring zero ongoing CPU usage.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SkillUnlockReward : MonoBehaviour
{
    [ElasticPopIn(duration: 400f, overshoot: 1.25f, delay: 0f)]
    public string newlyUnlockedSkill = "Meteor Swarm";
}
```

---

## 3. Constructors & Parameters

```csharp
public ElasticPopInAttribute(float duration = 400f, float overshoot = 1.2f, float delay = 0f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `duration` | `float` | `400f` | Total pop-in spring animation duration in milliseconds. |
| `overshoot` | `float` | `1.2f` | Peak scale multiplier reached during the outward spring rebound. |
| `delay` | `float` | `0f` | Stagger delay in milliseconds before the pop animation begins. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Duration` | `float` | `400f` | Total lifetime of the spring scale pop animation in milliseconds. |
| `Overshoot` | `float` | `1.2f` | Maximum scale multiplier reached during the outward elastic bounce. |
| `Delay` | `float` | `0f` | Wait time in milliseconds before triggering the pop animation. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

namespace MaharajaStudio.MSUltimate.AnimatedAttributes.Sample
{
    public class ElasticPopInExample : ModularMonoBehaviour
    {
        [Title("ElasticPopIn Attribute Showcase", "Joyful spring scale pop-in transition")]
        [InfoBox("ElasticPopIn applies a playful, tactile scale pop-in animation with an elastic overshoot.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Elastic Pop-In Fields")]
        [ElasticPopIn(duration: 400f, overshoot: 1.3f, delay: 0f)]
        public string victoryCrownBadge = "GRAND MASTER CHAMPION TROPHY";

        [ElasticPopIn(duration: 350f, overshoot: 1.25f, delay: 80f)]
        public float rewardGoldMultiplier = 3.5f;

        [BoxGroup("2. Inside Class Demonstration")]
        public AchievementCelebrationSlot primaryCelebration = new AchievementCelebrationSlot();

        [BoxGroup("3. Quest Rewards Manifest")]
        [InfoBox("ElasticPopIn cascades down to collections, applying spring scale pop-in animations with overshoot physics across each slot.", InspectorMessageType.Info)]
        [Title("Milestone Badges (Elastic Pop-In Cascading)")]
        [ElasticPopIn(duration: 380f, overshoot: 1.25f, delay: 50f)]
        public int[] milestoneLevelUnlocks = new int[] { 10, 25, 50, 75, 100 };

        public List<AchievementCelebrationSlot> questRewards = new List<AchievementCelebrationSlot>
        {
            new AchievementCelebrationSlot { achievementTitle = "Dungeon Delver Master", gemsAwarded = 100 },
            new AchievementCelebrationSlot { achievementTitle = "Flawless Boss Conqueror", gemsAwarded = 500 }
        };

        [Serializable]
        public class AchievementCelebrationSlot
        {
            public string achievementTitle = "Dragon Slayer Supreme";

            [ElasticPopIn(duration: 450f, overshoot: 1.35f, delay: 240f)]
            public int gemsAwarded = 250;
        }

        [BoxGroup("4. Pop-In Animation Controls")]
        [Button("Award Massive Celebration Bonus", BackgroundColor = "#F59E0B", TextColor = "#1C1102")]
        public void AwardBonus()
        {
            rewardGoldMultiplier += 0.5f;
            primaryCelebration.gemsAwarded += 50;
            Debug.Log($"<color=#FBBF24>[ElasticPopIn]</color> Celebration triggered! GoldMult: {rewardGoldMultiplier}x, Gems: {primaryCelebration.gemsAwarded}.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ShowIf]` | Supported | Pops elastically into view whenever conditional requirements become true. |
| `[BoxGroup]` | Supported | Scales smoothly within container boundaries without clipping parent frames. |
| `[SpringyBounce]` | Stacking | Combines initial elastic pop-in mount animations with subsequent click spring physics. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`int[]`, `string[]`, `List<T>`), animating newly mounted row elements with spring overshoot scaling. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Operates on direct primitive arrays (`int[]`, `float[]`), string arrays, and object lists. |
| **Nested Serializable Classes** | Supported | Fully animates fields inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions in `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
