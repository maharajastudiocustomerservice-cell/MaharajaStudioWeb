# [Tilt3DHover]

> Tilts the inspector element in pseudo-3D perspective toward the cursor with dynamic specular lighting glare on mouse movement.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit 3D Transforms)`

---

## 1. Overview & Value Proposition

**What it does:**
`[Tilt3DHover]` replicates modern interactive holographic card ergonomics inside the Unity Inspector. As the mouse cursor hovers across the decorated field, card, or collection element row, the element tilts smoothly in 3D perspective along the X and Y axes up to a configurable maximum tilt angle (`MaxTiltAngle`). Simultaneously, a subtle specular glare gradient moves dynamically across the surface (`ShowSpecularGlare = true`), creating a tangible illusion of depth.

**The Problem:**
Standard 2D flat editor layouts lack visual hierarchy and feel static. Important hero cards, primary configuration panels, or inventory item profiles look identical to ordinary raw data fields.

**The Solution:**
Decorating hero fields or collection cards with `[Tilt3DHover]`:
- **Parallax 3D Card Tilt:** Calculates mouse offset from element center to calculate realistic yaw and pitch rotations.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so trading cards and collection rows tilt independently under the user's cursor.
- **Dynamic Specular Light Glare:** Moves a glossy light reflection across the surface to mimic physical acrylic or trading cards.
- **Configurable Perspective:** Control depth intensity (`PerspectiveDepth`) and maximum tilt rotation (`MaxTiltAngle`).
- **Smooth Recovery Tweening:** Gently springs back to flat alignment as soon as the mouse exits the element rect.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class InventoryItemCard : MonoBehaviour
{
    [Tilt3DHover(maxTilt: 10f)]
    public string itemLoreDescription = "Ancient Dragon Scale";
}
```

---

## 3. Constructors & Parameters

```csharp
public Tilt3DHoverAttribute(float maxTilt = 8f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `maxTilt` | `float` | `8f` | Maximum rotation tilt angle in degrees along X and Y axes. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxTiltAngle` | `float` | `8f` | Maximum angular tilt rotation in degrees. |
| `PerspectiveDepth` | `float` | `300f` | Simulated 3D perspective projection depth factor. |
| `ShowSpecularGlare` | `bool` | `true` | Whether to render the dynamic moving specular highlight reflection. |
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
    public class Tilt3DHoverExample : ModularMonoBehaviour
    {
        [Title("Tilt3DHover Attribute Showcase", "Interactive 3D perspective tilt tracking")]
        [InfoBox("Tilt3DHover tracks the cursor position relative to the element, applying smooth pseudo-3D rotation.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Holographic Cards")]
        [Tilt3DHover(maxTilt: 14f, PerspectiveDepth = 350f, ShowSpecularGlare = true)]
        public string tradingCardName = "Celestial Phoenix - Prismatic Rare";

        [Tilt3DHover(maxTilt: 8f, ShowSpecularGlare = false)]
        public int attackRatingPoints = 8800;

        [BoxGroup("2. Inside Class Demonstration")]
        public CollectibleDeckSlot featuredCard = new CollectibleDeckSlot();

        [BoxGroup("3. Collectible Deck Showcase Gallery")]
        [InfoBox("Tilt3DHover cascades down to collections, rendering 3D perspective hover tilts across individual element rows.", InspectorMessageType.Info)]
        [Title("Foil Card Inscription Array (3D Tilt Cascading)")]
        [Tilt3DHover(maxTilt: 10f, ShowSpecularGlare = true)]
        public string[] holographicCardTitles = new string[]
        {
            "ASTRAL_LEVIATHAN_MYTHIC",
            "SOLAR_ARCHON_RADIANT",
            "CHRONO_WEAVER_ETERNAL"
        };

        public List<CollectibleDeckSlot> activeDeckBinder = new List<CollectibleDeckSlot>
        {
            new CollectibleDeckSlot { editionSerial = "STAR-VOID-01", foilFinishType = "Cosmic Obsidian Sheen" },
            new CollectibleDeckSlot { editionSerial = "DRAGON-GLOW-02", foilFinishType = "Gold Leaf Emboss" }
        };

        [Serializable]
        public class CollectibleDeckSlot
        {
            public string editionSerial = "1ST-EDITION-FOIL-042";

            [Tilt3DHover(maxTilt: 12f, ShowSpecularGlare = true)]
            public string foilFinishType = "Rainbow Prismatic Starlight";
        }

        [BoxGroup("4. Interactive Card Controls")]
        [Button("Draw Next Rare Card", BackgroundColor = "#A855F7", TextColor = "#1E0B36")]
        public void DrawRareCard()
        {
            attackRatingPoints += 250;
            Debug.Log($"<color=#C084FC>[Tilt3DHover]</color> New card drawn! Attack rating: {attackRatingPoints}.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Turns ordinary box groups into tactile, interactive 3D hero cards. |
| `[SpringyBounce]` | Stacking | Combines dynamic 3D tilt tracking with spring scale bounce upon clicks. |
| `[RPGRarityGlow]` | Stacking | Pairs holographic tilt with colored rarity auras for premium trading cards. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`string[]`, `List<T>`), applying smooth 3D cursor tilt to each row element or card. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Operates on direct string arrays (`string[]`), object lists, and serializable card arrays. |
| **Nested Serializable Classes** | Supported | Fully animates fields inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions in `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
