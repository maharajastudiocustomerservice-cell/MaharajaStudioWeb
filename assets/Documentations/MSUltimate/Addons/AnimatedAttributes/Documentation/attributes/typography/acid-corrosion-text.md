# AcidCorrosionText

> `[AcidCorrosionText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In toxic wastelands, alien bio-threats, chemical manufacturing, or weapon durability systems, standard inspector fields feel detached from the hazardous materials they represent. Static hazard text does not communicate volatile chemical corrosiveness.

`[AcidCorrosionText]` renders text in radioactive lime-green and sulfur-yellow hues, animating individual characters with an asymmetrical downward acid droplet droop and caustic horizontal micro-sizzles. Letters stretch viscously before snapping back, giving the visceral impression of boiling acid.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ChemicalReservoir : MonoBehaviour
{
    [AcidCorrosionText(4.5f, 3.0f, "#84CC16")]
    public float FluoroantimonicMolarity = 18.5f;
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (4.5px drip distance, 3.0 drip speed, toxic lime color)
public AcidCorrosionTextAttribute();

// Parameterized constructor with custom drip distance, speed, and acid color
public AcidCorrosionTextAttribute(float dripDistance, float dripSpeed = 3.0f, string acidColor = "#84CC16");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `DripDistance` | `float` | `4.5f` | Maximum downward droplet droop distance in pixels. |
| `DripSpeed` | `float` | `3.0f` | Speed of the viscous droplet ooze and snap-back cycle. |
| `AcidColor` | `string` | `"#84CC16"` | Base radioactive toxic lime text color (hex code). |
| `SizzleColor` | `string` | `"#FACC15"` | Sulfur yellow caustic sizzle highlight color (hex code). |
| `SizzleJitter` | `bool` | `true` | Whether to apply horizontal caustic micro-sizzling during the ooze cycle. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class BiohazardLabInspector : ModularMonoBehaviour
{
    [Title("Biohazard Containment", "Chemical volatility and acid drip telemetry", BackgroundColor = "#1a2e05", TextColor = "#A3E635")]

    [BoxGroup("Caustic Telemetry")]
    [AcidCorrosionText(4.5f, 3.0f, "#84CC16")]
    public float AcidAcidityMolar = 18.5f;

    [BoxGroup("Caustic Telemetry")]
    [AcidCorrosionText(6f, 4.5f, "#65A30D", SizzleColor = "#FEF08A", SizzleJitter = true)]
    public string XenomorphSalivaStatus = "CONCENTRATED_HYPER_ACID";

    [BoxGroup("Waste Conduits")]
    public List<ConduitSlot> DrainagePipes = new List<ConduitSlot>
    {
        new ConduitSlot("DRAIN_SECTOR_7B", "CORROSION_SEEPAGE"),
        new ConduitSlot("VALVE_ALPHA_LEAK", "NEUTRALIZING")
    };

    [Serializable]
    public class ConduitSlot
    {
        [AcidCorrosionText(4f, 2.8f, "#84CC16")]
        public string ConduitTag;

        public string State;

        public ConduitSlot(string tag, string state)
        {
            ConduitTag = tag;
            State = state;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[TabGroup]`** | Compatible | Vertical droop remains safely within standard label margins. |
| **`[MinMaxSlider]` & `[ProgressBar]`** | Compatible | Pairs cleanly with toxic pool depth and pH level sliders. |
| **Lists (`List<TClass>`)** | Compatible | Dynamic translate resets gracefully during virtualized list row cycling. |

---

## 7. Performance & Architecture

- **Asymmetrical Quadratic Easing:** Employs polynomial acceleration (`t^2`) for downward stretch paired with fast quadratic deceleration for snap recoil, avoiding expensive physics solvers.
- **Micro-Jitter Throttling:** Sizzle vibration evaluates only when characters exceed the 40% threshold, minimizing style updates.

