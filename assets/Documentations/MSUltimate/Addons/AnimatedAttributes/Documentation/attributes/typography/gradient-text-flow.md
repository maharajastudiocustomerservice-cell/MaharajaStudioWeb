# [GradientTextFlow]

> Animates field label typography with a smooth, continuously shifting multi-stop iridescent color gradient flow.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit StyleColor Transitions)`

---

## 1. Overview & Value Proposition

**What it does:**
`[GradientTextFlow]` transforms static field labels into dynamic iridescent typographic headers. It cycles the label's text color continuously through a 3-stop harmonic gradient spectrum (`Color1` $\to$ `Color2` $\to$ `Color3` $\to$ `Color2` $\to$ `Color1`) driven by sinusoidal time modulation ($t = \frac{\sin(\text{time} \cdot \text{Speed}) + 1}{2}$). Operating at a customizable cycle frequency (`Speed`, defaulting to 1.2x), it brings vibrant, fluid visual energy to legendary attributes, elemental damage headers, or collection element rows.

**The Problem:**
Highlighting elite game tiers—such as Mythic rarity, Celestial blessings, or Prismatic elements—typically requires bulky banners or custom info boxes that take up valuable vertical screen real estate in already crowded inspectors.

**The Solution:**
Decorating elite fields or collection items with `[GradientTextFlow]`:
- **Fluid Color Transition:** Interpolates across three distinct color stops with zero perceptible color banding.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so every string or socket slot in collections cycles through shimmering chromatic gradients.
- **Ultra-Lightweight:** Directly mutates `label.style.color` without reconstructing text elements or causing layout reflows.
- **Customizable Palettes:** Supports fully custom hex codes to match game aesthetics (e.g. Synthwave pink/cyan/yellow, Holy gold/white/blue, or Toxic green/lime/cyan).
- **Adjustable Wave Cadence:** Fine-tune oscillation velocity from slow ethereal drifting to fast vibrant pulses.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class MythicItemDefinition : MonoBehaviour
{
    [GradientTextFlow("#FF007F", "#00D2FF", "#FFE600", speed: 1.5f)]
    public string mythicRelicName = "Crown of the Sun King";
}
```

---

## 3. Constructors & Parameters

```csharp
public GradientTextFlowAttribute()

public GradientTextFlowAttribute(string color1, string color2, string color3 = "#FFE600", float speed = 1.2f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color1` | `string` | `"#FF007F"` | Starting primary color stop of the gradient cycle. |
| `color2` | `string` | `"#00D2FF"` | Secondary middle color stop of the gradient wave. |
| `color3` | `string` | `"#FFE600"` | Third color stop of the shifting gradient flow. |
| `speed` | `float` | `1.2f` | Modulation frequency speed multiplier. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color1` | `string` | `"#FF007F"` | Hex color string for the first chromatic stop. |
| `Color2` | `string` | `"#00D2FF"` | Hex color string for the secondary middle stop. |
| `Color3` | `string` | `"#FFE600"` | Hex color string for the final third stop. |
| `Speed` | `float` | `1.2f` | Speed of gradient shifting cycles per second. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

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
    public class GradientTextFlowExample : ModularMonoBehaviour
    {
        [Title("GradientTextFlow Attribute Showcase", "Continuous multi-stop animated gradient shifting")]
        [InfoBox("GradientTextFlow continuously animates the color of field labels using a multi-stop color gradient wave.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Prismatic Lore & Affinities")]
        [GradientTextFlow("#FF007F", "#7F00FF", "#00F0FF", speed: 1.5f)]
        public string astralBladeInscription = "Excalibur of the Shifting Void — 12th Cycle";

        [GradientTextFlow("#F59E0B", "#EF4444", "#EC4899", speed: 2.0f)]
        public float plasmaCoreTemperature = 10450.5f;

        [BoxGroup("2. Inside Class Demonstration")]
        public PrismaticSocket primarySocket = new PrismaticSocket();

        [BoxGroup("3. Socketed Relic Catalog")]
        [InfoBox("Demonstrates that [GradientTextFlow] operates cleanly on fields declared inside wrapper classes inside lists (List<MyClass>).", InspectorMessageType.Info)]
        public List<PrismaticSocket> relicSocketBank = new List<PrismaticSocket>
        {
            new PrismaticSocket { socketId = "SOCKET_BETA", runeTitle = "Glacial Frost Nova Inscription", amplificationFactor = 1.85f },
            new PrismaticSocket { socketId = "SOCKET_GAMMA", runeTitle = "Nether Vortex Graviton Cipher", amplificationFactor = 3.20f }
        };

        [Serializable]
        public class PrismaticSocket
        {
            public string socketId = "SOCKET_01";

            [GradientTextFlow("#FFE600", "#FF007F", "#00D2FF", speed: 1.8f)]
            public string runeTitle = "Prismatic Core Rune";

            public float amplificationFactor = 1.5f;
        }

        [BoxGroup("4. Prismatic Matrix Controls")]
        [Button("Attune Astral Prism", BackgroundColor = "#A21CAF", TextColor = "#FDF4FF")]
        public void AttunePrism()
        {
            plasmaCoreTemperature = UnityEngine.Random.Range(8500f, 15000f);
            Debug.Log($"<color=#EC4899>[GradientTextFlow]</color> Prismatic resonance attuned! Plasma Core: {plasmaCoreTemperature:F1}K.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` / `[HorizontalGroup]` | Supported | Fits cleanly into any layout; color flows continuously regardless of nesting depth. |
| `[ShowIf]` / `[EnableIf]` | Supported | Color modulation continues smoothly when revealed. |
| `[BouncingText]` / `[WavyText]` | Avoid | Text manipulation attributes targeting the same label element will conflict; use one per property. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Direct Collections (`string[]`, `List<T>`)** | Not Supported | Direct collections are intentionally not cascaded. |
| **Wrapper Classes in Lists (`List<MyClass>`)** | Supported | Fully animates fields inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions on fields within custom serialized wrappers. |
