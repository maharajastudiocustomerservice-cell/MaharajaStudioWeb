# FlameText

> `[FlameText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In fantasy RPGs, blacksmith forge systems, volcanic survival games, or fiery combat spells, static text feels cold and clinical. Standard Unity inspectors cannot express incinerator heat, molten temperatures, or elemental danger.

`[FlameText]` animates text characters with erratic vertical Perlin turbulence and a shifting fire color spectrum. Characters flicker upward like tongues of flame, shifting seamlessly from deep crimson ember bases through vivid orange fire bodies to luminous yellow sparks.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class VolcanoFurnace : MonoBehaviour
{
    [FlameText(4.5f, 4f)]
    public float CrucibleTemperature = 1650.0f;
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (4.0 turbulence speed, 3.5px flame height)
public FlameTextAttribute();

// Parameterized constructor with custom turbulence speed and flame height
public FlameTextAttribute(float turbulenceSpeed, float flameHeight = 3.5f);
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `TurbulenceSpeed` | `float` | `4f` | Speed of heat turbulence and flame convection currents. |
| `FlameHeight` | `float` | `3.5f` | Maximum vertical displacement reached by flicking flame tips in pixels. |
| `FlameBaseColor` | `string` | `"#DC2626"` | Crimson base ember color at the root of the flame (hex code). |
| `FlameMidColor` | `string` | `"#F97316"` | Vibrant orange color at the core of the flame body (hex code). |
| `FlameTipColor` | `string` | `"#FDE047"` | Luminous electric yellow color at the tip of the flame (hex code). |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class VolcanicFoundryCore : ModularMonoBehaviour
{
    [Title("Crucible Foundry", "Volcanic heat and forge telemetry", BackgroundColor = "#450a0a", TextColor = "#F87171")]

    [BoxGroup("Core Thermal Subsystem")]
    [FlameText(4.5f, 4f)]
    public float MagmaChamberHeat = 2100.5f;

    [BoxGroup("Core Thermal Subsystem")]
    [FlameText(6f, 5f, FlameBaseColor = "#991B1B", FlameMidColor = "#EA580C", FlameTipColor = "#FEF08A")]
    public string DragonBreathStatus = "PYROCLASTIC_OVERCHARGE";

    [BoxGroup("Smelting Kilns")]
    public List<KilnSlot> SmeltingSlots = new List<KilnSlot>
    {
        new KilnSlot("CRUCIBLE_ALPHA", 1850),
        new KilnSlot("OBSIDIAN_HEARTH", 2400)
    };

    [Serializable]
    public class KilnSlot
    {
        [FlameText(5f, 3.8f)]
        public string HearthName;

        public int HeatJoules;

        public KilnSlot(string name, int joules)
        {
            HearthName = name;
            HeatJoules = joules;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[AdvancedClass]`** | Compatible | Retains stable visual card framing during continuous thermal flickers. |
| **`[Slider]` & `[MinMaxSlider]`** | Compatible | Pairs perfectly with temperature and pressure sliders. |
| **Lists (`List<TClass>`)** | Compatible | Operates cleanly inside virtualized list rows without label duplication. |

---

## 7. Performance & Architecture

- **Perlin Turbulence Convection:** Uses multi-octave 2D `Mathf.PerlinNoise` sampling for natural non-repeating flame tongue motion.
- **Micro-Jitter Harmonics:** Blends subtle high-frequency sinusoids with noise to prevent repetitive synthetic looping.

