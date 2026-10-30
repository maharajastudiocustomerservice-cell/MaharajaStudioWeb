# [ParticleSnowfall]

> Spawns falling weather particles with lateral wind drift and gentle oscillation across the field or container background.

---

## 1. Overview & Value Proposition

**What it does:**
`[ParticleSnowfall]` introduces serene winter weather aesthetics to the Unity Inspector. It generates a continuous cascade of falling snowflakes (`ParticleCount`) drifting downward at a customizable velocity (`FallSpeed`), while applying sinusoidal lateral wind turbulence (`WindSway`) and customized snowflake pigmentation (`ParticleColor`).

**The Problem:**
Winter environments, alpine level configurations, holiday event content, or ice magic properties often blend into standard inspector containers without conveying a frosty or wintry theme. Designers tweaking winter balance lack visual thematic context.

**The Solution:**
Decorating winter, blizzard, or ice variables with `[ParticleSnowfall]`:
- **Organic Wind Turbulence:** Snowflakes sway side-to-side dynamically with harmonic wind oscillation (`WindSway`).
- **Configurable Weather Intensity:** Scale from light flurries (`ParticleCount = 15`) to blizzard cascades (`ParticleCount = 60`) with faster falling velocity (`FallSpeed`).
- **Color Customization:** Render pristine white snow (`"#FFFFFF"`), ethereal icy cyan (`"#E0F2FE"`), or ash fall for volcanic winter settings.
- **Seamless Recycling:** Snowflakes loop infinitely by wrapping from bottom to top bounds, maintaining steady frame rates without garbage collection.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class WinterBiomeConfig : MonoBehaviour
{
    [ParticleSnowfall(count: 35, fallSpeed: 45f)]
    public float ambientFrostIntensity = 0.85f;
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
public ParticleSnowfallAttribute(int count = 30, float fallSpeed = 40f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `count` | `int` | `30` | Total number of simultaneous active snowfall particles. |
| `fallSpeed` | `float` | `40f` | Downward falling velocity in pixels per second. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ParticleCount` | `int` | `30` | Active snowflake particle count rendered in the field background. |
| `FallSpeed` | `float` | `40f` | Vertical descent rate in pixels per second. |
| `WindSway` | `float` | `15f` | Horizontal sway oscillation amplitude simulating wind draft. |
| `ParticleColor` | `string` | `"#FFFFFF"` | Hex color string for the falling snow particles. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class GlacierSurvivalTelemetry : MonoBehaviour
{
    [Header("Severe Blizzard Parameters")]
    [ParticleSnowfall(
        count: 50, 
        fallSpeed: 60f, 
        WindSway = 25f, 
        ParticleColor = "#F0F9FF"
    )]
    public float blizzardWindSpeedKPH = 85f;

    [Header("Glacier Core Temperature")]
    [ParticleSnowfall(count: 20, fallSpeed: 30f, ParticleColor = "#BAE6FD")]
    public float permafrostDepthMeters = 340f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Snow particles cascade within the boundaries of the group or card container. |
| `[AnimatedProgressBar]` | Supported | Pairs with chilling frost progress bars to visualize temperature drops. |
| `[ReadOnly]` | Supported | Beautifully decorates read-only environment telemetry readouts. |
