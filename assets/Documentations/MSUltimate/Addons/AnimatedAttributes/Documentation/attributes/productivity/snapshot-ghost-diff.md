# [SnapshotGhostDiff]

> Overlays a smooth fading ghost highlight across the field background whenever modifying or undoing property values.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Zero Idle Tick Allocations)`

---

## 1. Overview & Value Proposition

**What it does:**
`[SnapshotGhostDiff]` tracks serialized property mutations in real time via UI Toolkit's `TrackPropertyValue`. Whenever the monitored field's value changes or an Undo/Redo operation occurs, the attribute triggers a soft background highlight in a designated tint (`GhostColorAdd` / `GhostColorRemove`). The highlight then gracefully interpolates its alpha transparency back to zero over a customizable decay duration (`FadeDuration`), visually confirming that a mutation took place.

**The Problem:**
When scrubbing sliders, modifying values via hotkeys, or performing bulk Undo/Redo cycles, developers often lose track of which specific field just mutated on a crowded inspector screen. Without transient visual confirmation, it is easy to miss subtle numerical shifts.

**The Solution:**
Decorating monitored fields with `[SnapshotGhostDiff]`:
- **Instant Change Confirmation:** Illuminates the property field background the moment a value delta or Undo action happens.
- **Collection Row Cascading:** Implements `ICollectionElementAttribute` to overlay ghost highlights specifically on the mutated element row inside arrays and lists.
- **Graceful Linear Fadeout:** Fades out smoothly from 0.4 opacity over a configurable interval (`FadeDuration` in milliseconds).
- **Customizable Color Accents:** Select distinct color tints (`GhostColorAdd`, `GhostColorRemove`) to convey increments or decrements.
- **Zero Idle Computation:** The drawer registers a transient schedule timer that sleeps completely once the fade progress reaches 100%.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlayerInventory : MonoBehaviour
{
    [SnapshotGhostDiff(fadeDuration: 1000f)]
    public int inventoryCapacity = 40;
}
```

---

## 3. Constructors & Parameters

```csharp
public SnapshotGhostDiffAttribute(float fadeDuration = 1200f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `fadeDuration` | `float` | `1200f` | Ghost highlight fade duration in milliseconds before returning to transparent. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `FadeDuration` | `float` | `1200f` | Total duration of the ghost highlight fadeout animation in milliseconds. |
| `GhostColorAdd` | `string` | `"#10B981"` | Hex color string for newly added or increased values (defaults to Emerald). |
| `GhostColorRemove` | `string` | `"#EF4444"` | Hex color string for removed or decreased values (defaults to Red). |
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
    public class SnapshotGhostDiffExample : ModularMonoBehaviour
    {
        [Title("SnapshotGhostDiff Attribute Showcase", "Fading ghost trail overlay displaying previous serialized states")]
        [InfoBox("SnapshotGhostDiff captures the previous state of a serialized property whenever it is changed or undone.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Snapshot Ghost Outlines")]
        [SnapshotGhostDiff(fadeDuration: 1200f)]
        public float characterJumpImpulse = 14.5f;

        [SnapshotGhostDiff(fadeDuration: 1800f, GhostColorAdd = "#10B981", GhostColorRemove = "#EF4444")]
        public float sprintVelocityMultiplier = 1.85f;

        [BoxGroup("2. Inside Class Demonstration")]
        public BallisticsTuningNode ballisticsConfig = new BallisticsTuningNode();

        [BoxGroup("3. Armory Ballistics Manifest")]
        [InfoBox("SnapshotGhostDiff cascades down to array slots, capturing ephemeral dissolved ghost trails when values are tuned.", InspectorMessageType.Info)]
        [SnapshotGhostDiff(fadeDuration: 1200f)]
        public float[] projectileSpeedTiers = new float[] { 120f, 240f, 480f };

        public List<BallisticsTuningNode> weaponArmory = new List<BallisticsTuningNode>
        {
            new BallisticsTuningNode { caliberName = "7.62x51mm NATO Subsonic", muzzleVelocityMps = 320f },
            new BallisticsTuningNode { caliberName = "5.56x45mm High Velocity", muzzleVelocityMps = 940f }
        };

        [Serializable]
        public class BallisticsTuningNode
        {
            public string caliberName = ".50 BMG Armor Piercing";

            [SnapshotGhostDiff(fadeDuration: 1400f)]
            public float muzzleVelocityMps = 880f;
        }

        [BoxGroup("4. Interactive Physics Playground")]
        [Button("Boost Jump (+5.0)", BackgroundColor = "#10B981", TextColor = "#022C22")]
        public void BoostJumpImpulse()
        {
            characterJumpImpulse += 5.0f;
            Debug.Log($"<color=#10B981>[SnapshotGhostDiff]</color> Jump impulse boosted to {characterJumpImpulse}!");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Fades within the property element boundary without bleeding into neighboring fields. |
| `[FloatUpDeltaNumber]` | Stacking | Pairs background ghost color fades with floating RPG numeric deltas. |
| `[DiffHighlightFlash]` | Stacking | Combines ephemeral ghost background fades with persistent breathing outline borders. |
| `[ShowIf]` / `[HideIf]` | Supported | Operates seamlessly with conditional visibility filters. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`float[]`, `string[]`, `List<T>`), overlaying fading ghost backgrounds onto modified element rows. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Functions on arrays and lists of numeric, string, vector, and object reference types. |
| **Nested Serializable Classes** | Supported | Fully functions inside child classes and structs declared within lists. |
| **Custom Serializers** | Supported | Compatible with `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
