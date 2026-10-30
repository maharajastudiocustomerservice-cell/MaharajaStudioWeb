# [DiffHighlightFlash]

> Displays a breathing neon outline highlight whenever a field value differs from its initial or prefab state, aiding version control reviews.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware Accelerated UI Toolkit Border Transitions)`

---

## 1. Overview & Value Proposition

**What it does:**
`[DiffHighlightFlash]` provides instantaneous visual diff tracking inside the Unity Inspector. As soon as a serialized property's value deviates from its initial baseline (or prefab parent value), the attribute wraps the field in an animated, breathing outline glow (`DiffColor`) oscillating with configurable intensity (`PulseIntensity`). When reverted back to baseline, the highlight gracefully extinguishes.

**The Problem:**
During scene setup, balance passes, or prefab editing, developers often tweak dozens of properties. Before saving or committing, it is easy to forget which subtle sliders, toggles, or numbers were changed versus which ones remained at default values, leading to unintended git commits or forgotten test values.

**The Solution:**
Decorating mutable inspector properties with `[DiffHighlightFlash]`:
- **Unsaved Modification Radar:** Immediately flags any modified property with an eye-catching breathing border.
- **Collection Row Cascading:** Implements `ICollectionElementAttribute` to pinpoint the exact dirty or modified element row inside large arrays and tables.
- **Color-Coded Status Accent:** Choose custom diff outline colors (`DiffColor`), such as warm amber (`"#F59E0B"`), electric cyan, or git purple.
- **Configurable Pulse Breath:** Adjust the oscillation intensity (`PulseIntensity`) from a gentle ambient glow to an urgent flashing reminder.
- **Effortless Prefab & Git Audits:** Glance at complex inspector panels and instantly spot every altered value before committing.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class LevelTuningProfile : MonoBehaviour
{
    [DiffHighlightFlash(diffColor: "#F59E0B")]
    public float enemySpawnIntervalSeconds = 3.5f;
}
```

---

## 3. Constructors & Parameters

```csharp
public DiffHighlightFlashAttribute(string diffColor = "#F59E0B")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `diffColor` | `string` | `"#F59E0B"` | Hex color string for the modified value outline highlight (defaults to Amber). |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DiffColor` | `string` | `"#F59E0B"` | Hex color string of the breathing diff outline. |
| `PulseIntensity` | `float` | `1.0f` | Oscillation intensity multiplier for the breathing pulse glow. |
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
    public class DiffHighlightFlashExample : ModularMonoBehaviour
    {
        [Title("DiffHighlightFlash Attribute Showcase", "Visual dirty-state diff pulsing")]
        [InfoBox("DiffHighlightFlash projects a subtle breathing outline pulse onto any field whose value differs from its baseline.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Diff Trackers")]
        [DiffHighlightFlash(diffColor: "#F59E0B", PulseIntensity = 1.0f)]
        public string characterClassArchetype = "Shadow Assassin";

        [DiffHighlightFlash(diffColor: "#10B981", PulseIntensity = 1.2f)]
        public float baseAgilityScore = 48.5f;

        [BoxGroup("2. Inside Class Demonstration")]
        public CombatTuningNode combatParameters = new CombatTuningNode();

        [BoxGroup("3. Server Configuration Tuning Manifest")]
        [InfoBox("Direct float[] arrays decorated with [DiffHighlightFlash] display individual amber breathing diff highlights on modified elements.", InspectorMessageType.Info)]
        [DiffHighlightFlash(diffColor: "#F59E0B")]
        public float[] balancingStatMultipliers = new float[] { 1.0f, 1.25f, 1.5f, 2.0f };

        public List<CombatTuningNode> combatTuningProfiles = new List<CombatTuningNode>
        {
            new CombatTuningNode { damageFormula = "Physical Melee Standard", criticalDamageMultiplier = 2.0f },
            new CombatTuningNode { damageFormula = "Spell Magic Pierce", criticalDamageMultiplier = 1.75f }
        };

        [Serializable]
        public class CombatTuningNode
        {
            public string damageFormula = "BaseAtk * (1.0 + StatBonus)";

            [DiffHighlightFlash(diffColor: "#F43F5E", PulseIntensity = 1.3f)]
            public float criticalDamageMultiplier = 2.5f;
        }

        [BoxGroup("4. Interactive Balance Sandbox")]
        [Button("Tweak Balances (+10% Agility, +0.5x Crit)", BackgroundColor = "#F59E0B", TextColor = "#1C1102")]
        public void TweakBalancingValues()
        {
            baseAgilityScore += 5.0f;
            combatParameters.criticalDamageMultiplier += 0.5f;
            Debug.Log($"<color=#F59E0B>[DiffHighlightFlash]</color> Values tweaked. Diff highlights will illuminate.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Pulsing highlight frames the field cleanly without overflowing box layout borders. |
| `[ValueChangeFlash]` | Stacking | Combines momentary change flashes with persistent breathing diff highlights. |
| `[ReadOnly]` | Supported | Can be used on monitored status fields to highlight runtime overrides. |
| `[ShowIf]` / `[HideIf]` | Supported | Respects dynamic visibility states. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`float[]`, `string[]`, `List<T>`), highlighting altered rows with a breathing outline. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Functions on arrays and lists of numeric, string, vector, and object reference types. |
| **Nested Serializable Classes** | Supported | Fully functions inside child classes and structs declared within lists. |
| **Custom Serializers** | Supported | Compatible with `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
