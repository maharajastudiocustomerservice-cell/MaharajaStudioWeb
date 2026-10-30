# [NeonPulseGlow]

> Renders a rhythmic breathing neon glow and pulsating border frame around the inspector field container.

---

## 1. Overview & Value Proposition

**What it does:**
`[NeonPulseGlow]` wraps inspector properties in an illuminated, breathing neon frame. The drawer styles the element with rounded border corners (radius 4px) and continuously modulates the border width between `MinSpread` (default 1px) and `MaxSpread` (default 3.5px), while harmonically pulsing the alpha color intensity from 0.3 to 0.85 in a vivid neon tint (`GlowColor`, defaulting to hot magenta `#EC4899`). The pulse frequency is calibrated via `PulseSpeed` in radians per second.

**The Problem:**
Cyberpunk titles, arcade mini-games, neon synthwave themes, or night club management games look out of place when configured using dull default unity controls. Key attributes—such as neon lighting colors, nightclub popularity, or cyberdeck battery life—lack vibrant atmospheric presence.

**The Solution:**
Decorating themed properties with `[NeonPulseGlow]`:
- **Breathing Border Spread:** Dynamically interpolates border stroke thickness between `MinSpread` and `MaxSpread`, creating a convincing light bloom.
- **Harmonic Sinusoidal Fading:** Calculates alpha glow oscillation smoothly (`pulse = (sin(time) + 1) * 0.5`) without abrupt cuts.
- **Vibrant Custom Colors:** Supports any signature neon hex tone (`GlowColor`), from neon pink to laser cyan or radioactive lime.
- **Direct Element Integration:** Discovered via `AnimationTargetHelper`, eliminating unnecessary container nesting.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CyberpunkSign : MonoBehaviour
{
    [NeonPulseGlow(glowColor: "#EC4899", pulseSpeed: 1.5f)]
    public float neonSignLuminance = 1500f;
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
public NeonPulseGlowAttribute(string glowColor = "#EC4899", float pulseSpeed = 1.2f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `glowColor` | `string` | `"#EC4899"` | Hex color string for the breathing neon pulse border. |
| `pulseSpeed` | `float` | `1.2f` | Breathing pulse frequency multiplier. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GlowColor` | `string` | `"#EC4899"` | Hex color string of the neon glow (defaults to Hot Magenta). |
| `MinSpread` | `float` | `1f` | Minimum glow border width in pixels. |
| `MaxSpread` | `float` | `3.5f` | Maximum glow border width in pixels during peak expansion. |
| `PulseSpeed` | `float` | `1.2f` | Breathing oscillation tempo multiplier. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class NightclubSoundConsole : MonoBehaviour
{
    [Header("Synthwave Soundstage")]
    [NeonPulseGlow(
        glowColor: "#06B6D4", 
        pulseSpeed: 2.0f, 
        MinSpread = 1.5f, 
        MaxSpread = 4.5f
    )]
    public float audioBassBoostDecibels = 18f;

    [Header("Laser Array Strobe")]
    [NeonPulseGlow(glowColor: "#F43F5E", pulseSpeed: 1.0f)]
    public Color laserPrimaryTint = Color.magenta;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Pulsing neon border accents fields nestled within grouped card containers. |
| `[ShimmerSweep]` | Stacking | Combines breathing neon borders with periodic metallic specular sweeps. |
| `[ColorPicker]` | Supported | Enhances color fields with real-time breathing visual borders matching the theme. |
