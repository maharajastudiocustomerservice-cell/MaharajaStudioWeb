# [ShimmerSweep]

> Sweeps a diagonal metallic light shine beam across the inspector field at periodic intervals to convey luxury and premium rarity.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit 2D Vector Meshes)`

---

## 1. Overview & Value Proposition

**What it does:**
`[ShimmerSweep]` casts a periodic metallic sheen across inspector properties and collection element rows. Using UI Toolkit's vector painter (`MeshGenerationContext.painter2D`), it creates an angled 45-degree translucent parallelogram beam (`ShimmerWidth`, defaulting to 40px) in a translucent tint (`ShimmerColor`, defaulting to 40% translucent white). The beam translates smoothly across the entire width of the container from left to right over `SweepDuration` ms, recurring every `Interval` seconds.

**The Problem:**
Premium game items—such as legendary loot tiers, rare trading cards, divine artifacts, or VIP memberships—often look indistinguishable from standard common inventory fields in the inspector. Without high-end visual polish, premium items feel ordinary during data authoring.

**The Solution:**
Decorating rare, mythical, or premium assets with `[ShimmerSweep]`:
- **Periodic Specular Glint:** Sweeps an angled metallic shine across the field at defined intervals (`Interval` in seconds).
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so every item in weapon catalogs or artifact lists receives its own periodic gleam.
- **Customizable Beam Dimensions:** Adjust shine beam width (`ShimmerWidth`) and sweep speed (`SweepDuration`).
- **Custom Hue & Transparency:** Configure gold foil shines (`#FBBF2466`), celestial silver (`#FFFFFF66`), or iridescent gemstone tints.
- **Zero-Allocation Translation:** Operates via horizontal style offsets (`style.left = currentX`) within an overflow-hidden wrapper, guaranteeing smooth editor frame rates.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class LegendaryItem : MonoBehaviour
{
    [ShimmerSweep(interval: 3.0f, shimmerColor: "#FBBF2466")]
    public string legendarySwordName = "Excalibur of the Dawn";
}
```

---

## 3. Constructors & Parameters

```csharp
public ShimmerSweepAttribute(float interval = 3.5f, string shimmerColor = "#FFFFFF66")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `interval` | `float` | `3.5f` | Cadence interval in seconds between consecutive shimmer sweeps. |
| `shimmerColor` | `string` | `"#FFFFFF66"` | Hex color string for the sweeping specular shine (translucent white). |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Interval` | `float` | `3.5f` | Time between consecutive sweeps in seconds. |
| `SweepDuration` | `float` | `600f` | Duration of a single shimmer sweep across the field in milliseconds. |
| `ShimmerColor` | `string` | `"#FFFFFF66"` | Hex color string for the specular shine beam. |
| `ShimmerWidth` | `float` | `40f` | Width of the angled specular light beam in pixels. |
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
    public class ShimmerSweepExample : ModularMonoBehaviour
    {
        [Title("ShimmerSweep Attribute Showcase", "Diagonal metallic light sweep gleam")]
        [InfoBox("ShimmerSweep animates an angled specular light shine across the surface of inspector fields at periodic intervals.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Metallic Gleams")]
        [ShimmerSweep(interval: 3.5f, shimmerColor: "#FFFFFF66", SweepDuration = 600f, ShimmerWidth = 45f)]
        public string platinumTrophyName = "SOVEREIGN CONQUEROR - PLATINUM 100%";

        [ShimmerSweep(interval: 2.5f, shimmerColor: "#FDE04788", SweepDuration = 500f, ShimmerWidth = 55f)]
        public float weaponCriticalRating = 385.5f;

        [BoxGroup("2. Inside Class Demonstration")]
        public RareLootEntry featuredItem = new RareLootEntry();

        [BoxGroup("3. Treasury Vault Trophy Manifest")]
        [InfoBox("ShimmerSweep cascades down to collections, rendering periodic specular light shines across individual element rows.", InspectorMessageType.Info)]
        [Title("Vault Relic Scepters (Metallic Shimmer Cascading)")]
        [ShimmerSweep(interval: 2.8f, shimmerColor: "#FDE04788", ShimmerWidth = 50f)]
        public string[] legendaryWeaponCodenames = new string[]
        {
            "SCEPTER_OF_SOLAR_FLAME",
            "HALBERD_OF_THE_VOID_EMPEROR",
            "AEGIS_OF_CELESTIAL_AURORA"
        };

        public List<RareLootEntry> royalVault = new List<RareLootEntry>
        {
            new RareLootEntry { itemName = "Aegis of the Sun God", itemGoldWorth = 48000 },
            new RareLootEntry { itemName = "Ring of Eternal Starlight", itemGoldWorth = 120000 }
        };

        [Serializable]
        public class RareLootEntry
        {
            public string itemName = "Crown of Celestial Monarchs";

            [ShimmerSweep(interval: 3.0f, shimmerColor: "#FBBF2488")]
            public int itemGoldWorth = 75000;
        }

        [BoxGroup("4. Treasury Vault Controls")]
        [Button("Polish All Artifacts (+5,000 Gold Worth)", BackgroundColor = "#EAB308", TextColor = "#1C1302")]
        public void PolishArtifacts()
        {
            featuredItem.itemGoldWorth += 5000;
            weaponCriticalRating += 12.5f;
            Debug.Log($"<color=#FDE047>[ShimmerSweep]</color> Relics polished! Crown value: {featuredItem.itemGoldWorth:N0} Gold.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Specular beam travels across the full width of grouped cards and boxes. |
| `[RPGRarityGlow]` | Stacking | Combines static rarity glowing borders with periodic metallic sweep passes. |
| `[ReadOnly]` | Supported | Accentuates luxury read-only asset names and balance sheets. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`string[]`, `float[]`, `List<T>`), sweeping an angled specular light shine across each row. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Operates on direct string arrays (`string[]`), numeric arrays, and asset lists. |
| **Nested Serializable Classes** | Supported | Fully functions inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions in `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
