# [ConstellationStarfield]

> Renders a cosmic space starfield with drifting, twinkling celestial particles across the inspector field background.

---

## 1. Overview & Value Proposition

**What it does:**
`[ConstellationStarfield]` turns the background of inspector fields into a deep space viewport. It renders a dark cosmic backdrop (`#0A0A14` at 0.85 opacity) filled with procedural stars (`StarCount`). Powered by UI Toolkit's 2D vector painter (`MeshGenerationContext.painter2D`), stars drift horizontally across the canvas at a configurable velocity (`DriftSpeed`), wrapping smoothly at border edges while oscillating their brightness (`alpha = (Mathf.Sin(Twinkle) + 1f) * 0.4f + 0.2f`) with sinusoidal twinkling.

**The Problem:**
Space simulators, celestial navigation systems, galactic trade economies, or sci-fi procedural generators feel grounded and dull when presented over default dark-grey editor panels. The lack of cosmic ambiance detaches developers from the space-themed game world they are constructing.

**The Solution:**
Decorating interstellar or astronomical properties with `[ConstellationStarfield]`:
- **Vector-Painted Starfield:** Procedurally renders circular stars with randomized sizes (1.0 to 2.5px) and drift speeds using GPU-accelerated UI Toolkit 2D vector arcs.
- **Harmonic Celestial Twinkling:** Each star maintains an independent sine wave phase offset for organic, non-uniform twinkling.
- **Continuous Edge Wrapping:** Stars wrap seamlessly from right to left borders as they drift, keeping memory allocations at zero.
- **Seamless Field Stacking:** Draws behind standard `PropertyField` inputs, keeping numbers and labels sharp and interactively accessible.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class StarshipNavigation : MonoBehaviour
{
    [ConstellationStarfield(starCount: 30, driftSpeed: 20f)]
    public Vector3 warpDestinationCoordinates = new Vector3(104.5f, -42.8f, 902.1f);
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
public ConstellationStarfieldAttribute(int starCount = 25, float driftSpeed = 15f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `starCount` | `int` | `25` | Number of procedural background stars simulated across the canvas. |
| `driftSpeed` | `float` | `15f` | Horizontal drift velocity of stars in pixels per second. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `StarCount` | `int` | `25` | Total count of background stars spawned. |
| `DriftSpeed` | `float` | `15f` | Horizontal drift rate in pixels per second. |
| `StarColor` | `string` | `"#FFFFFF"` | Hex color string for the background stars (defaults to White). |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class GalaxySectorRegistry : MonoBehaviour
{
    [Header("Sector Telemetry")]
    [ConstellationStarfield(
        starCount: 40, 
        driftSpeed: 25f, 
        StarColor = "#E0F2FE"
    )]
    public string primaryConstellationName = "Orion-Cygnus Arm";

    [Header("Hyperspace Jump Readiness")]
    [ConstellationStarfield(starCount: 15, driftSpeed: 10f)]
    public float jumpDriveCoherence = 98.4f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Starfield canvas fills the rectangular background inside box groups cleanly. |
| `[NeonPulseGlow]` | Stacking | Pairs with neon border glow to frame cosmic starfields in high-tech sci-fi consoles. |
| `[ReadOnly]` | Supported | Decorates read-only galactic coordinates and sector names with celestial motion. |
