# ScanlineHoloText

> `[ScanlineHoloText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In sci-fi space combat, cyberpunk tactical consoles, avionics cockpits, or holographic head-up displays (HUD), static text lacks the flickering retro-futuristic charm of authentic cathode-ray tube (CRT) monitors or optical hologram projectors.

`[ScanlineHoloText]` animates a vertical phosphor scanline beam sweeping rhythmically across the field label. Characters illuminate with an electric beam highlight at the wave crest, while subtle transmission signal flutter creates the unmistakable aesthetic of a live tactical feed.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class StarshipHUD : MonoBehaviour
{
    [ScanlineHoloText(2.0f, "#06B6D4", "#E0F2FE")]
    public string RegistryId = "USS_PROMETHEUS_NX74913";
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (2.0 Hz scan speed, holographic cyan, electric white beam highlight)
public ScanlineHoloTextAttribute();

// Parameterized constructor with custom speed, holo color, and beam highlight color
public ScanlineHoloTextAttribute(float scanSpeed, string holoColor = "#06B6D4", string beamColor = "#E0F2FE");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `ScanSpeed` | `float` | `2.0f` | Vertical scanline beam sweep frequency in hertz. |
| `HoloColor` | `string` | `"#06B6D4"` | Base holographic phosphor text color (hex code). |
| `BeamColor` | `string` | `"#E0F2FE"` | Bright phosphor beam highlight color at the scan crest (hex code). |
| `TransmissionFlutter` | `bool` | `true` | Whether to simulate subtle CRT transmission signal flutter. |
| `Continuous` | `bool` | `true` | When true, sweeps continuously; otherwise sweeps only on hover. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class StarshipTacticalAvionics : ModularMonoBehaviour
{
    [Title("Avionics Console", "Holographic CRT telemetry and phosphor scanline sweep", BackgroundColor = "#083344", TextColor = "#38BDF8")]

    [BoxGroup("Bridge Telemetry")]
    [ScanlineHoloText(2.0f, "#06B6D4", "#E0F2FE")]
    public string VesselRegistry = "USS_ENTERPRISE_NCC1701";

    [BoxGroup("Bridge Telemetry")]
    [ScanlineHoloText(3.2f, "#10B981", "#D1FAE5", TransmissionFlutter = true)]
    public float WarpCoilHarmonicGhz = 47.85f;

    [BoxGroup("Tactical Sensor Array")]
    public List<SensorNode> ActiveSensors = new List<SensorNode>
    {
        new SensorNode("FORWARD_PHASED_ARRAY", 98.4f),
        new SensorNode("TACHYON_DETECT_GRID", 76.1f)
    };

    [Serializable]
    public class SensorNode
    {
        [ScanlineHoloText(2.5f, "#38BDF8", "#F0F9FF")]
        public string SensorDesignation;

        public float SignalStrength;

        public SensorNode(string name, float strength)
        {
            SensorDesignation = name;
            SignalStrength = strength;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[TabGroup]`** | Compatible | Holographic opacity sweeps smoothly within nested dark containers. |
| **`[Dropdown]` & `[TextField]`** | Compatible | Primary field controls retain full mouse responsiveness. |
| **Lists (`List<TClass>`)** | Compatible | Recycled list rows maintain precise scanline phase without visual tearing. |

---

## 7. Performance & Architecture

- **Zero Transform Mutation:** Only modifies `style.color` and `style.opacity`, avoiding any layout reflow or matrix transforms.
- **Throttled Noise Sampling:** Transmission flutter samples noise every 4 ticks (15 Hz) to maintain high performance across multiple fields.

