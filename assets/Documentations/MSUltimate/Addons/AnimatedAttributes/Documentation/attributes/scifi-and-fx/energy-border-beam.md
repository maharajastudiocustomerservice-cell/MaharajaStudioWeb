# [EnergyBorderBeam]

> Renders a high-energy laser beam traveling continuously along the perimeter border of the inspector field.

---

## 1. Overview & Value Proposition

**What it does:**
`[EnergyBorderBeam]` wraps inspector properties in an animated energy containment field. It renders a subtle base perimeter border (15% opacity), accompanied by an intense, luminous energy beam head (`BeamLength`, defaulting to 45px) rendered with increased stroke thickness (`BorderWidth + 1.5f`) in a vibrant neon hue (`BeamColor`). The beam circulates clockwise along all four edges of the container at an adjustable speed (`BeamSpeed`), giving the element an active power-line aura.

**The Problem:**
Special gameplay abilities, legendary inventory cards, activated forcefields, or dangerous overclocking options blend in with everyday inspector fields. Static borders fail to convey that an element is currently energized, active, or charged.

**The Solution:**
Decorating high-energy fields with `[EnergyBorderBeam]`:
- **Continuous Perimeter Circuit:** Calculates exact rectangular perimeter coordinates and sweeps a luminous beam seamlessly around corners.
- **Glowing Accent Hue:** Custom beam color (`BeamColor`, defaulting to `#38BDF8` sky blue) with configurable stroke width (`BorderWidth`).
- **Dynamic Speed Tuning:** Regulate circulation speed (`BeamSpeed`) for calm power loops or frantic high-voltage racing beams.
- **Built-In Container Padding:** Automatically wraps child fields in generous padding (`paddingTop/Bottom = 3, paddingLeft/Right = 4`) so borders do not overlap field content.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ForcefieldGenerator : MonoBehaviour
{
    [EnergyBorderBeam(beamColor: "#00F0FF", speed: 1.5f)]
    public float barrierIntegrity = 100f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public EnergyBorderBeamAttribute(string beamColor = "#38BDF8", float speed = 1.2f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `beamColor` | `string` | `"#38BDF8"` | Hex color string of the circulating energy beam head and base border. |
| `speed` | `float` | `1.2f` | Circulation speed multiplier along the border perimeter. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BeamColor` | `string` | `"#38BDF8"` | Hex color string for the circulating energy beam. |
| `BeamSpeed` | `float` | `1.2f` | Circulation speed multiplier. |
| `BeamLength` | `float` | `45f` | Length of the traveling energy beam head in pixels. |
| `BorderWidth` | `float` | `2f` | Base thickness of the border outline in pixels. |
| `BorderRadius` | `float` | `4f` | Corner radius of the border perimeter in pixels. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlasmaShieldSubsystem : MonoBehaviour
{
    [Header("Active Plasma Shielding")]
    [EnergyBorderBeam(
        beamColor: "#A855F7", 
        speed: 1.8f, 
        BeamLength = 60f, 
        BorderWidth = 2.5f
    )]
    public float shieldOutputGigawatts = 850f;

    [Header("Containment Magnetic Coil")]
    [EnergyBorderBeam(beamColor: "#F59E0B", speed: 1.0f)]
    public float magneticFluxDensity = 14.2f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Encloses grouped sub-fields inside a circulating high-energy border. |
| `[ElectricArcSparks]` | Stacking | Combines perimeter energy beams with branching lightning spark discharge. |
| `[ReadOnly]` | Supported | Frames critical status telemetry with prominent active energy beams. |
