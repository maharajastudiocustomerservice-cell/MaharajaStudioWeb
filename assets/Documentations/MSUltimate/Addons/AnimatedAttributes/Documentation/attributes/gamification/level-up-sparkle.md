# [LevelUpSparkle]

> Spawns glittering golden stars and sparkles that drift upward whenever a property or field value increases.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (GPU Painter2D + MeshGenerationContext)`

---

## 1. Overview & Value Proposition

**What it does:**
`[LevelUpSparkle]` delivers gratifying RPG progression feedback inside the Unity Inspector. When the assigned field or property is modified and its numeric value increases, the attribute spawns a cluster of glittering golden micro-stars (`StarCount`) in a custom color (`SparkleColor`) that shimmer and drift upward (`FloatDistance`) over an animated duration (`Duration`).

**The Problem:**
Progression values—such as character levels, skill ranks, mastery points, or enhancement tiers—should feel rewarding when upgraded during playtesting or design tuning. In the default inspector, increasing a character level from 1 to 50 provides identical sensory feedback to modifying an arbitrary debug index.

**The Solution:**
Decorating growth metrics with `[LevelUpSparkle]`:
- **Unidirectional Positive Trigger:** Only triggers when the value actually increases, remaining silent during resets or decreases.
- **Glittering Micro-Particle Trail:** Radiates twinkling 4-point stars that float upward and spin gently, mirroring classic JRPG leveling sequences.
- **Direct Collection Cascading:** Implements `ICollectionElementAttribute` to cascade upward golden sparkle bursts to individual collection element rows in numeric arrays and lists.
- **Customizable Star Canopy:** Adjust the number of stars (`StarCount`), their upward climb distance (`FloatDistance`), and color scheme (`SparkleColor`).
- **Clean UI Lifecycle:** Automatically recycles and disposes UI elements without adding allocations to your editor loop.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class HeroProgress : MonoBehaviour
{
    [LevelUpSparkle(starCount: 16, sparkleColor: "#FBBF24")]
    public int characterLevel = 1;
}
```

---

## 3. Constructors & Parameters

```csharp
public LevelUpSparkleAttribute(int starCount = 12, string sparkleColor = "#FBBF24")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `starCount` | `int` | `12` | Total number of twinkling sparkle stars spawned during the level-up sequence. |
| `sparkleColor` | `string` | `"#FBBF24"` | Hex color string for the glittering star particles (defaults to Gold). |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `StarCount` | `int` | `12` | Number of animated sparkle stars emitted upon value increment. |
| `SparkleColor` | `string` | `"#FBBF24"` | Hex color string for the glittering stars. |
| `FloatDistance` | `float` | `30f` | Vertical upward drift distance in pixels. |
| `Duration` | `float` | `800f` | Duration of the sparkle animation in milliseconds. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

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
    public class LevelUpSparkleExample : ModularMonoBehaviour
    {
        [Title("LevelUpSparkle Attribute Showcase", "Twinkling golden star particle physics drifting upward on progression")]
        [InfoBox("LevelUpSparkle spawns glittering starburst particles that drift upward and twinkle whenever an integer or float value increases.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Progression Sparkles")]
        [LevelUpSparkle(starCount: 16, sparkleColor: "#FBBF24")]
        public int characterLevel = 45;

        [LevelUpSparkle(starCount: 14, sparkleColor: "#38BDF8")]
        public int weaponRefinementTier = 7;

        [BoxGroup("2. Inside Class Demonstration")]
        public HeroStatNode primaryAttribute = new HeroStatNode();

        [BoxGroup("3. Character Core Stat Manifest")]
        [InfoBox("Direct numeric collections decorated with [LevelUpSparkle] automatically cascade star bursts to individual elements when edited.", InspectorMessageType.Info)]
        [LevelUpSparkle(starCount: 14, sparkleColor: "#FBBF24")]
        public int[] heroSkillRanks = new int[] { 10, 25, 40, 55 };

        public List<HeroStatNode> companionStats = new List<HeroStatNode>
        {
            new HeroStatNode { attributeName = "Vitality & Resilience", statRankPoints = 42 },
            new HeroStatNode { attributeName = "Arcane Intelligence", statRankPoints = 50 }
        };

        [Serializable]
        public class HeroStatNode
        {
            public string attributeName = "Agility & Reflexes";

            [LevelUpSparkle(starCount: 15, sparkleColor: "#10B981")]
            public int statRankPoints = 35;
        }

        [BoxGroup("4. Character Progression Controls")]
        [Button("Level Up Hero! (+1 Level)", BackgroundColor = "#F59E0B", TextColor = "#1C1003")]
        public void LevelUpHero()
        {
            characterLevel++;
            Debug.Log($"<color=#FBBF24>[LevelUpSparkle]</color> LEVEL UP! Hero reached Level {characterLevel}.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ConfettiCannon]` | Stacking | Combines rising golden stars with festive confetti fountains for major milestones. |
| `[FloatUpDeltaNumber]` | Stacking | Displays `+1` green delta badges alongside rising golden star sparkles. |
| `[BoxGroup]` | Supported | Floats elegantly over boxed groups and card headers. |
| `[ShowIf]` / `[HideIf]` | Supported | Seamlessly manages visibility of sparkling progression fields. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Decorating `int[]`, `float[]`, or `List<int>` cascades sparkling star bursts directly onto the edited element row. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Numeric Collections** | Supported | Operates seamlessly on `int[]`, `float[]`, `double[]`, `long[]`, `short[]`, `byte[]`, etc. |
| **Nested Serializable Classes** | Supported | Fully functions on numeric fields inside serializable structs and classes within lists. |
| **Custom Serializers** | Supported | Fully compatible with `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
