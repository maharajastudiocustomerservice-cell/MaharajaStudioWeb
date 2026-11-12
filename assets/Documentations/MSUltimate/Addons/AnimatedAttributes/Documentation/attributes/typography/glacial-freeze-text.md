# GlacialFreezeText

> `[GlacialFreezeText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In arctic survival games, cryo weapon systems, cryogenic chambers, or sub-zero blizzard environments, static typography fails to communicate freezing danger. Developers frequently resort to static blue color tints that lack physical tactile urgency.

`[GlacialFreezeText]` applies an icy crystalline color sheen to field labels, causing characters to shudder with authentic high-frequency micro-tremors (cryo shiver) like teeth chattering in extreme sub-zero cold. It supports both continuous cryo-containment cycles and interactive hover triggers.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CryoChamber : MonoBehaviour
{
    [GlacialFreezeText(1.2f, 32f, "#A5F3FC")]
    public float CoreTemperatureKelvin = 4.2f;
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (1.2px shiver intensity, 32 Hz frequency, glacial ice cyan)
public GlacialFreezeTextAttribute();

// Parameterized constructor with custom shiver intensity, vibration frequency, and frost color
public GlacialFreezeTextAttribute(float shiverIntensity, float shiverFrequency = 32f, string frostColor = "#A5F3FC");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `ShiverIntensity` | `float` | `1.2f` | Micro-tremor shivering amplitude in pixels. |
| `ShiverFrequency` | `float` | `32f` | Vibration shivering frequency in hertz. |
| `FrostColor` | `string` | `"#A5F3FC"` | Glacial ice cyan base crystalline text color (hex code). |
| `FreezeGlowColor` | `string` | `"#38BDF8"` | Deep cryo blue tint applied during peak shivering (hex code). |
| `Continuous` | `bool` | `false` | When true, shivers continuously; otherwise shivers only on hover or value change. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CryoContainmentInspector : ModularMonoBehaviour
{
    [Title("Cryogenic Containment", "Sub-zero telemetry and thermal shivering", BackgroundColor = "#083344", TextColor = "#67E8F9")]

    [BoxGroup("Thermal Telemetry")]
    [GlacialFreezeText(1.2f, 32f, "#A5F3FC")]
    public float LiquidHeliumTemperature = 4.2f;

    [BoxGroup("Thermal Telemetry")]
    [GlacialFreezeText(1.8f, 40f, "#E0F2FE", FreezeGlowColor = "#0284C7", Continuous = true)]
    public string ContainmentStatus = "SUPERCONDUCTING_STABLE";

    [BoxGroup("Storage Capsules")]
    public List<CapsuleSlot> SpecimenSlots = new List<CapsuleSlot>
    {
        new CapsuleSlot("SPECIMEN_FROST_ALPHA", -196.5f),
        new CapsuleSlot("CRYOPOD_SECTOR_4", -220.0f)
    };

    [Serializable]
    public class CapsuleSlot
    {
        [GlacialFreezeText(1.4f, 35f, "#CFFAFE")]
        public string SpecimenName;

        public float CelsiusTemp;

        public CapsuleSlot(string name, float temp)
        {
            SpecimenName = name;
            CelsiusTemp = temp;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[AdvancedClass]`** | Compatible | Micro-vibrations stay within element bounds without clipping card borders. |
| **`[Slider]` & `[ProgressBar]`** | Compatible | Operates harmoniously above or alongside cold-temperature sliders. |
| **Lists (`List<TClass>`)** | Compatible | Sibling container layout ensures row recycling causes zero assertion errors. |

---

## 7. Performance & Architecture

- **Harmonic Sinusoid Synthesis:** Employs twin high-frequency sinusoids (`Sin(t * 1.7) * intensity`) for natural biological shivering cadence without random noise allocations.
- **Defensive Sibling Tree:** Fully compatible with Unity 6 UIR, never modifying `Label` children directly.

