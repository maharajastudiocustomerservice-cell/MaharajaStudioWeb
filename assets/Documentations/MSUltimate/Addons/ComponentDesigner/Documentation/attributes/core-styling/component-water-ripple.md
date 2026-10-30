# [ComponentWaterRipple]

> Renders animated expanding concentric water ripple rings from the component card center, creating aquatic wave motion or acoustic ping vibrations.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentWaterRipple]` projects animated liquid wave motion across the component inspector card. Operating via UI Toolkit vector rendering, it draws concentric circular rings (`Rings = 4`) that expand continuously outward from the center up to a maximum diameter (`MaxSize = 80f`) before fading out. Developers can customize ring stroke weight (`RingWidth = 1.5f`), ripple expansion speed (`Speed`), ring color (`Color`, defaulting to cyan `#4FC3F7`), transparency (`Opacity = 0.3f`), and layer positioning (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`).

**The Problem:**
Aquatic gameplay mechanics, ocean buoyant physics, sonar pulse detectors, and water simulation controllers look identical to rigid mechanical scripts in standard Unity inspector views. Developers miss the fluid, acoustic character of water-based systems.

**The Solution:**
Decorating liquid and wave systems with `[ComponentWaterRipple]`:
- **Concentric Expanding Waves:** Simulates realistic water ripples expanding outward from a central origin.
- **Configurable Ring Dynamics:** Adjust ring count (`Rings = 4`), stroke thickness (`RingWidth`), and maximum radius (`MaxSize = 80f`).
- **Smooth Opacity Falloff:** Fades rings gracefully as they expand, preventing harsh edge clipping.
- **Zero Click Interference:** Runs with `PickingMode.Ignore`, ensuring all standard Unity input controls remain completely responsive.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentWaterRipple(Color = "#06B6D4", Rings = 5, MaxSize = 90f, Speed = 1.2f, Opacity = 0.35f)]
public class OceanWaveBuoyancyPhysics : MonoBehaviour
{
    public float waterDensity = 1000f;
    public float waveAmplitude = 1.8f;
    public float dampingViscosity = 0.85f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `ContentOverlay` (if `Behind = true`) or `BodyOverlay` (if `Behind = false`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentWaterRippleAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#4FC3F7"` | Hex color string for the concentric ripple rings. |
| `Rings` | `int` | `4` | Total number of concurrent expanding ripple rings. |
| `MaxSize` | `float` | `80f` | Maximum expansion diameter in pixels before ring dissipation. |
| `RingWidth` | `float` | `1.5f` | Stroke thickness in pixels for each individual ripple ring. |
| `Speed` | `float` | `1f` | Expansion cycle velocity multiplier. |
| `Opacity` | `float` | `0.3f` | Transparency alpha of the ripple rings (0.0 to 1.0). |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#0891B2", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#061A22", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("SUB-SURFACE ACOUSTIC HYDROPHONE", Subtitle = "Sonar Echo Detection & Ping Engine", BackgroundColor = "#0A2936", TitleColor = "#CFFAFE")]
[ComponentWaterRipple(Color = "#22D3EE", Rings = 5, MaxSize = 100f, RingWidth = 2f, Speed = 1.3f, Opacity = 0.4f, Behind = true)]
public class SubsurfaceAcousticHydrophone : MonoBehaviour
{
    [Header("Sonar Ping Settings")]
    public float acousticPingFrequencyHz = 2500f;
    public float maxEchoListeningRangeMeters = 800f;
    public bool enableThermalLayerRefraction = true;

    [Header("Target Tracking")]
    public int maxTrackedVessels = 8;
    public float dopplerBearingCorrection = 1.4f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep aquatic blue or dark slate backgrounds highlight luminous cyan water rings. |
| **`[ComponentHeader]`** | High | Ripple circles emanate cleanly across the body below marine or sonar header bars. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures complete click-through transparency for all inspector controls. |
