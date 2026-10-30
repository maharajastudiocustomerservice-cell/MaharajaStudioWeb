# [VaporizeDisintegrate]

> Spawns a disintegration particle dissolve effect when a field is reset, cleared, modified, or executed via button.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property | Method` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit 2D Particle Meshes)`

---

## 1. Overview & Value Proposition

**What it does:**
`[VaporizeDisintegrate]` delivers a sci-fi or dark fantasy dissolution effect inside the Unity Inspector. When an attached field or collection element row is modified, cleared, or an action method is triggered, the element dissolves into a cloud of disintegrating ash or ember particles (`ParticleCount`) that float away and fade over a designated duration (`Duration`) in a chosen vaporize tint (`DisintegrateColor`).

**The Problem:**
Destructive or irreversible editor operations—such as clearing save game caches, deleting local high scores, resetting tuning profiles to defaults, or purging unlinked assets—often execute abruptly without visual weight. Designers can inadvertently clear data without a clear visual consequence.

**The Solution:**
Decorating destructive fields, reset properties, or collection items with `[VaporizeDisintegrate]`:
- **Visceral Dissolution FX:** Renders high-tech digital de-rezzing or burning ash disintegration directly across the field frame.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so clearing, modifying, or deleting individual items in collections (`float[]`, `List<T>`) triggers ash dissolution on that exact row.
- **Visual Impact for Resets:** Gives clear, satisfying visual confirmation when purging, clearing, or overwriting critical data.
- **Customizable Disintegration Color:** Style dissolution particles as glowing amber embers (`"#F59E0B"`), digital plasma cyan (`"#06B6D4"`), or void purple (`"#9333EA"`).
- **Universal Decorator Support:** Easily attaches to fields, properties, or clickable buttons (`[Button]`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SaveSlotManager : MonoBehaviour
{
    [VaporizeDisintegrate(count: 45, duration: 700f)]
    public int currentSaveIndex = 0;
}
```

---

## 3. Constructors & Parameters

```csharp
public VaporizeDisintegrateAttribute(int count = 40, float duration = 600f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `count` | `int` | `40` | Total number of dissolving ash particles spawned upon trigger. |
| `duration` | `float` | `600f` | Total lifetime of the disintegration dissolve sequence in milliseconds. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ParticleCount` | `int` | `40` | Total count of dissolve ash or vapor particles emitted. |
| `Duration` | `float` | `600f` | Total disintegration animation duration in milliseconds. |
| `DisintegrateColor` | `string` | `"#F59E0B"` | Hex color string for the dissolving ash particles (defaults to Amber). |
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
    public class VaporizeDisintegrateExample : ModularMonoBehaviour
    {
        [Title("VaporizeDisintegrate Attribute Showcase", "Disintegration particle dissolve physics")]
        [InfoBox("VaporizeDisintegrate spawns animated disintegration particles that dissolve into ash and vapor.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Disintegration Fields")]
        [VaporizeDisintegrate(count: 45, duration: 700f, DisintegrateColor = "#F59E0B")]
        public string contrabandItemTag = "Unstable Dark Matter Core";

        [VaporizeDisintegrate(count: 35, duration: 500f, DisintegrateColor = "#EF4444")]
        public float incineratorCoreCelsius = 1850f;

        [BoxGroup("2. Inside Class Demonstration")]
        public WasteDisposalBay primaryIncineratorBay = new WasteDisposalBay();

        [BoxGroup("3. Facility Incineration Matrix")]
        [InfoBox("VaporizeDisintegrate cascades down to collections, spawning disintegration ash particles per element row.", InspectorMessageType.Info)]
        [VaporizeDisintegrate(count: 30, duration: 500f, DisintegrateColor = "#F59E0B")]
        public float[] fuelCanisterResidues = new float[] { 45.5f, 80.0f, 12.5f, 95.0f };

        public List<WasteDisposalBay> disposalChambers = new List<WasteDisposalBay>
        {
            new WasteDisposalBay { bayIdentifier = "Slag Recycler Chamber A", payloadMassKg = 150.0f },
            new WasteDisposalBay { bayIdentifier = "Bio-Ash Smelter Chamber B", payloadMassKg = 210.0f }
        };

        [Serializable]
        public class WasteDisposalBay
        {
            public string bayIdentifier = "Hazardous Plasma Crucible 07";

            [VaporizeDisintegrate(count: 40, duration: 650f, DisintegrateColor = "#F97316")]
            public float payloadMassKg = 320.0f;
        }

        [BoxGroup("4. Disintegration Beam Controls")]
        [VaporizeDisintegrate(count: 65, duration: 900f, DisintegrateColor = "#EF4444")]
        [Button("Vaporize All Contraband! (Incinerate)", BackgroundColor = "#EF4444", TextColor = "#FFFFFF")]
        public void VaporizeContraband()
        {
            contrabandItemTag = "<DISINTEGRATED INTO ASH>";
            incineratorCoreCelsius = 3200f;
            primaryIncineratorBay.payloadMassKg = 0f;
            Debug.LogWarning("<color=#F87171>[VaporizeDisintegrate]</color> DISINTEGRATION COMPLETE! Ash particles vaporized.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Triggers dramatic vaporize dissolve effects upon button invocation. |
| `[HoldToConfirmButton]` | Stacking | Pairs with hold-to-confirm buttons to vaporize irreversible action controls upon release. |
| `[BoxGroup]` | Supported | Disintegration particles float freely across group bounds before fading. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`float[]`, `string[]`, `List<T>`), spawning particle dissolution ash specifically on modified/cleared element rows. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Operates on direct numeric arrays (`float[]`), string arrays, and object lists. |
| **Nested Serializable Classes** | Supported | Fully functions inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions in `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
