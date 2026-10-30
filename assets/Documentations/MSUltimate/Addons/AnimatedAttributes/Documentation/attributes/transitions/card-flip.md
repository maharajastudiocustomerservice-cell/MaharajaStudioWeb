# [CardFlip]

> Animates a 3D card flip rotation around the Y-axis to alternate views or reveal advanced settings panels via button click.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit 3D Transforms)`

---

## 1. Overview & Value Proposition

**What it does:**
`[CardFlip]` introduces interactive 3D card rotation into inspector panels. It renders the property field alongside a stylized flip trigger button (`flipBtn`, styled with `"🔄 " + ButtonLabel`). When the developer clicks the button, the drawer triggers a 3D horizontal card flip rotation around the vertical Y-axis over a configurable duration (`FlipDuration`, defaulting to 350ms), compressing `scaleX` via a harmonic cosine curve (`Mathf.Abs(Mathf.Cos(progress * Mathf.PI))`) to simulate a double-sided card flip.

**The Problem:**
Complex inspector components often have two distinct viewing needs: a simple high-level summary for level designers, and deep granular settings for technical leads. Having both simultaneously visible clutters the UI, while tab bars consume precious vertical screen space.

**The Solution:**
Decorating dual-faceted configuration fields or list items with `[CardFlip]`:
- **Tactile 3D Flip Rotation:** Simulates a card turning over around its vertical spine using hardware-accelerated UI Toolkit scale transforms.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so array and collection item rows gain dedicated flip action buttons to inspect individual card details.
- **Dedicated Flip Action Button:** Renders a clean action button (`ButtonLabel`) right-aligned beside the property for instant flipping.
- **Configurable Flip Duration:** Tune rotation tempo (`FlipDuration`) for snappy 200ms flips or deliberate 500ms showcase turns.
- **Zero Layout Breakage:** Scale transforms modify visual rendering without altering layout flow or displacing adjacent controls.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class WeaponCard : MonoBehaviour
{
    [CardFlip(buttonLabel: "Flip for Calibration")]
    public float weaponOverheatThreshold = 85f;
}
```

---

## 3. Constructors & Parameters

```csharp
public CardFlipAttribute(string buttonLabel = "Flip for Advanced Settings")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `buttonLabel` | `string` | `"Flip for Advanced Settings"` | Label text rendered on the companion card flip trigger button. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ButtonLabel` | `string` | `"Flip for Advanced Settings"` | Label text for the flip action button. |
| `FlipDuration` | `float` | `350f` | Total duration of the 3D flip animation in milliseconds. |
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
    public class CardFlipExample : ModularMonoBehaviour
    {
        [Title("CardFlip Attribute Showcase", "Interactive 3D card flip rotation")]
        [InfoBox("CardFlip rotates fields or inspector panels 180 degrees in simulated 3D space around the Y-axis.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone 3D Flip Cards")]
        [CardFlip("Flip to Reveal Combat Passives", FlipDuration = 350f)]
        public string characterClassTitle = "Paladin Commander of the Sun";

        [CardFlip("Flip for Low-Level Socket Tuning", FlipDuration = 400f)]
        public string serverEndpointAddress = "cluster.mmo.galaxy.net:9900";

        [BoxGroup("2. Inside Class Demonstration")]
        public CollectibleFlipCard primaryCard = new CollectibleFlipCard();

        [BoxGroup("3. Collectible Card Deck Manifest")]
        [InfoBox("CardFlip cascades down to collections, rendering 3D flip trigger buttons beside each individual entry.", InspectorMessageType.Info)]
        [CardFlip("Flip Inscription")]
        public string[] runicScrollInscriptions = new string[]
        {
            "ANCIENT_FIRE_RITUAL",
            "VOID_CALL_INCANTATION",
            "CELESTIAL_AEGIS_MANTRA"
        };

        public List<CollectibleFlipCard> cardDeck = new List<CollectibleFlipCard>
        {
            new CollectibleFlipCard { cardTitle = "Seraphim Vanguard", holyResistanceScore = 92.0f },
            new CollectibleFlipCard { cardTitle = "Ophanim Wheel", holyResistanceScore = 85.0f }
        };

        [Serializable]
        public class CollectibleFlipCard
        {
            public string cardTitle = "Archangel Michael";

            [CardFlip("Flip to View Holy Resistances")]
            public float holyResistanceScore = 98.5f;
        }

        [BoxGroup("4. Card Flip Sandbox Controls")]
        [Button("Upgrade Paladin Class Tier", BackgroundColor = "#F59E0B", TextColor = "#1A0F02")]
        public void UpgradeClass()
        {
            characterClassTitle = "High Sovereign Paladin (Tier III)";
            primaryCard.holyResistanceScore = 100f;
            Debug.Log($"<color=#FBBF24>[CardFlip]</color> Class upgraded: {characterClassTitle}.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Flips cleanly within card or box containers without border overflow. |
| `[Tilt3DHover]` | Stacking | Combines interactive 3D cursor tilt with full button-triggered card flips. |
| `[RPGRarityGlow]` | Supported | Renders glowing rarity frames around flipping hero card profiles. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`string[]`, `List<T>`), adding individual flip trigger buttons to rotate row elements in 3D. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Operates on direct string arrays (`string[]`), numeric arrays, and object reference lists. |
| **Nested Serializable Classes** | Supported | Fully operates on fields inside child class items declared within lists. |
| **Custom Serializers** | Supported | Integrates cleanly with `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
