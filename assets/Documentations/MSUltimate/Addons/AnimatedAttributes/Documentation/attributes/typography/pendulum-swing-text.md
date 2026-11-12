# PendulumSwingText

> `[PendulumSwingText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In pirate nautical games, western frontier saloons, medieval blacksmiths, or antique clockmaker workshops, static inspector labels look rigid and synthetic. Wood, rope, and clockwork pendulums naturally exhibit angular sway and momentum.

`[PendulumSwingText]` sways each character around its top-center pivot origin with harmonic angular momentum. Characters swing back and forth with customizable phase offsets, producing the unmistakable aesthetic of a creaking tavern sign in sea winds or an antique grandfather clock escapement.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PirateTavern : MonoBehaviour
{
    [PendulumSwingText(12f, 1.8f, 0.35f)]
    public string TavernSign = "THE_SALTY_SEADOG_TAVERN";
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (12 deg max angle, 1.8 Hz frequency, 0.35 phase shift)
public PendulumSwingTextAttribute();

// Parameterized constructor with custom angle, frequency, and phase shift
public PendulumSwingTextAttribute(float maxAngle, float swingFrequency = 1.8f, float phaseShift = 0.35f);
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `MaxAngle` | `float` | `12f` | Maximum angular swing amplitude in degrees. |
| `SwingFrequency` | `float` | `1.8f` | Oscillation swing frequency in hertz. |
| `PhaseShift` | `float` | `0.35f` | Phase shift offset between consecutive characters for snake/wave swaying. |
| `Continuous` | `bool` | `true` | When true, sways continuously; otherwise swings only on hover or value change. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PortHarborInspector : ModularMonoBehaviour
{
    [Title("Harbor Manifest", "Angular signboard sway and nautical pendulum telemetry", BackgroundColor = "#3e1f07", TextColor = "#FDBA74")]

    [BoxGroup("Harbor Telemetry")]
    [PendulumSwingText(12f, 1.8f, 0.35f)]
    public string TavernName = "THE_SALTY_SEADOG_TAVERN";

    [BoxGroup("Harbor Telemetry")]
    [PendulumSwingText(18f, 2.5f, 0.5f)]
    public float GaleWindKnots = 42.5f;

    [BoxGroup("Moored Vessels")]
    public List<VesselSlot> MooredShips = new List<VesselSlot>
    {
        new VesselSlot("HMS_BLACK_PEARL", 32),
        new VesselSlot("FLYING_DUTCHMAN", 48)
    };

    [Serializable]
    public class VesselSlot
    {
        [PendulumSwingText(14f, 2.0f, 0.4f)]
        public string VesselName;

        public int Cannons;

        public VesselSlot(string name, int cannons)
        {
            VesselName = name;
            Cannons = cannons;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[TabGroup]`** | Compatible | Angular rotation stays within standard line-height boundaries. |
| **`[ReadOnly]`** | Compatible | Continues to swing naturally on non-editable nautical text. |
| **Lists (`List<TClass>`)** | Compatible | Sibling container layout ensures row recycling causes zero assertion errors. |

---

## 7. Performance & Architecture

- **UI Toolkit Top-Center Pivot:** Sets `transformOrigin = new TransformOrigin(50%, 0%)` so rotation happens naturally around the top suspension point.
- **Pure Trigonometric Animation:** Single sinusoidal phase calculation per character with zero garbage collection allocations.

