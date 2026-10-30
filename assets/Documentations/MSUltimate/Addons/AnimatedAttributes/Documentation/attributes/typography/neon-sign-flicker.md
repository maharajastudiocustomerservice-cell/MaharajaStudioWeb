# [NeonSignFlicker]

> Recreates vintage neon sign typography with vivid gas-tube luminescence and intermittent sputtering flickers.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit StyleColor Transitions)`

---

## 1. Overview & Value Proposition

**What it does:**
`[NeonSignFlicker]` replicates the imperfect, retro aesthetic of electrical neon gas tubes in the Unity Inspector. It applies bold typographic weight to the primary field label and washes it in a radiant neon hue (`NeonColor`, defaulting to hot magenta `#FF007F`). Periodically, evaluated on a 32ms cadence, erratic voltage dips are simulated: if a random check falls below `FlickerRate` (defaulting to 0.25), the label momentarily sputters to a dim, erratic transparency (`alpha` between 0.2 and 0.6) before flashing back to full brightness.

**The Problem:**
Cyberpunk, 80s retro, horror, or noir projects frequently lack atmospheric flavor in editor tools. Static magenta or cyan text labels feel like plain flat UI elements rather than glowing electrical signs buzzing in a dark alley.

**The Solution:**
Decorating themed parameters or collection items with `[NeonSignFlicker]`:
- **Authentic Voltage Sputter:** Delivers organic, non-uniform flickers modeled after dying gas-discharge lamps.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so every street sign or signboard slot in string collections flickers with independent voltage instability.
- **Bold Tube Typography:** Automatically applies `FontStyle.Bold` to emulate thick glass neon tube filaments.
- **Adjustable Voltage Instability:** Tune `FlickerRate` from a rock-steady hum (0.05) to a dying, erratic strobe (0.50).
- **Vibrant Spectrum:** Supports any neon hex color—from hot pink and radioactive green to amber and cobalt blue.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CyberpunkDiner : MonoBehaviour
{
    [NeonSignFlicker(neonColor: "#FF007F", FlickerRate = 0.2f)]
    public string dinerSignboardName = "NEON DREAMS DINER";
}
```

---

## 3. Constructors & Parameters

```csharp
public NeonSignFlickerAttribute(string neonColor = "#FF007F")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `neonColor` | `string` | `"#FF007F"` | Hex color string for the illuminated neon gas tube text. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `NeonColor` | `string` | `"#FF007F"` | Hex color code applied to the bold neon typography. |
| `FlickerRate` | `float` | `0.25f` | Probability (0.0 to 1.0) of a sputtering voltage drop occurring on each tick. |
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
    public class NeonSignFlickerExample : ModularMonoBehaviour
    {
        [Title("NeonSignFlicker Attribute Showcase", "Vintage gas tube neon glow")]
        [InfoBox("NeonSignFlicker simulates authentic vintage illuminated neon signage with rich gas-tube bloom.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Neon District Signage")]
        [NeonSignFlicker("#FF007F", FlickerRate = 0.25f)]
        public string mainNightclubMarquee = "NEO-TOKYO NIGHTCLUB 2099 — VIP LOUNGE";

        [NeonSignFlicker("#00F0FF", FlickerRate = 0.15f)]
        public string open24HoursNotice = "OPEN 24/7 SYNTH-WAVE & COCKTAILS";

        [BoxGroup("2. Inside Class Demonstration")]
        public NeonSignboardConfig rooftopBillboard = new NeonSignboardConfig();

        [BoxGroup("3. District Signboard Power Grid Manifest")]
        [InfoBox("Demonstrates that [NeonSignFlicker] operates cleanly on fields declared inside wrapper classes inside lists (List<MyClass>).", InspectorMessageType.Info)]
        public List<NeonSignboardConfig> districtSignboardNetwork = new List<NeonSignboardConfig>
        {
            new NeonSignboardConfig { districtZone = "ALLEYWAY_SOUTH", signboardLabel = "RAMEN & NOODLE BAR" },
            new NeonSignboardConfig { districtZone = "INDUSTRIAL_DOCKS", signboardLabel = "SYNTHETIC FUEL DEPOT" }
        };

        [Serializable]
        public class NeonSignboardConfig
        {
            public string districtZone = "DOWNTOWN_PLAZA";

            [NeonSignFlicker("#E11D48", FlickerRate = 0.30f)]
            public string signboardLabel = "NEON CASINO ARCADE";
        }

        [BoxGroup("4. District Power Grid Telemetry & Controls")]
        [Button("Trigger Transformer Voltage Surge", BackgroundColor = "#C026D3", TextColor = "#FDF4FF")]
        public void TriggerSurge()
        {
            Debug.LogWarning("<color=#F472B6>[NeonSignFlicker]</color> High-voltage power surge injected! Neon gas tubes flickering.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` / `[HorizontalGroup]` | Supported | Looks striking on dark container backgrounds and cyberpunk card layouts. |
| `[ShowIf]` / `[EnableIf]` | Supported | Flickering pauses cleanly when hidden and resumes seamlessly on reveal. |
| `[NeonPulseGlow]` | Supported | Perfect visual pairing: `[NeonPulseGlow]` illuminates the container borders while `[NeonSignFlicker]` animates the text. |
| `[GradientTextFlow]` | Avoid | Multiple text coloring attributes targeting the same label will fight over `style.color`. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Direct Collections (`string[]`, `List<string>`)** | Not Supported | Direct arrays and lists are intentionally not cascaded. |
| **Wrapper Classes in Lists (`List<MyClass>`)** | Supported | Fully animates fields inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions on fields within custom serialized wrappers. |
