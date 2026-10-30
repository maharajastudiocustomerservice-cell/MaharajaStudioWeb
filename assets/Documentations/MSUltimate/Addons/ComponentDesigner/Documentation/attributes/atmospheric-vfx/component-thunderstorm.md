# [ComponentThunderstorm]

> Renders an atmospheric weather backdrop with animated diagonal rain streaks and ambient lightning flashes across the component card.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentThunderstorm]` immerses the component inspector in a tempestuous squall. Operating within `ComponentSlot.ContentOverlay`, it renders an animated deluge of angled rain streaks (`RainColor = "#93C5FD55"`, `RainIntensity = 1.2f`) slashing downward across the component card. Periodically, sudden atmospheric lightning strikes flash across the card face (`LightningColor = "#E0E7FF"`, `FlashInterval = 3.5f`), briefly illuminating fields before fading back into rain-drenched darkness.

**The Problem:**
Weather controllers, typhoon simulators, oceanic storm encounters, and thunder magic systems look calm and detached in flat gray inspector panels. Scripters tweaking hurricane gale forces or precipitation densities lack sensory feedback reflecting the intensity of the storm.

**The Solution:**
Decorating storm, oceanic, and tempest systems with `[ComponentThunderstorm]`:
- **High-Velocity Angled Rain Streaks:** Simulates heavy gale-force precipitation sweeping dynamically across inspector controls.
- **Dynamic Lightning Flash Strobe:** Timed stochastic lightning bursts illuminate background surfaces with brief, dramatic electric radiance.
- **Independent Color Customization:** Configure distinct tints for rain streaks (delicate blue or acid green) and electric lightning bolts (pure white, purple, or golden arc).
- **Zero Input Blockers:** Placed in `ContentOverlay` with `PickingMode.Ignore`, maintaining total click and hover transparency for all serialized fields.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentThunderstorm(flashInterval: 3.5f, rainIntensity: 1.2f, lightningColor: "#E0E7FF")]
public class HurricaneWeatherDirector : MonoBehaviour
{
    public float windSpeedMetersPerSec = 45f;
    public float rainPrecipitationRateMmHr = 120f;
    public float thunderClapDelaySec = 1.8f;
    public bool isSupercellFormed = true;
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
| **Component Slot** | `ContentOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentThunderstormAttribute()
public ComponentThunderstormAttribute(float flashInterval = 3.5f, float rainIntensity = 1.2f, string lightningColor = "#E0E7FF")
```

- `flashInterval`: Average delay in seconds between sudden lightning illumination flashes.
- `rainIntensity`: Speed and density multiplier for the falling rain streak particles.
- `lightningColor`: Hex color string for the sudden ambient flash illumination.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RainColor` | `string` | `"#93C5FD55"` | Hex color string (with alpha) for the falling rain streaks. |
| `LightningColor` | `string` | `"#E0E7FF"` | Hex color string for the brief lightning flash strobe. |
| `RainIntensity` | `float` | `1.2f` | Density and fall velocity multiplier governing the rainfall. |
| `FlashInterval` | `float` | `3.5f` | Average interval in seconds between lightning strikes. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#1D4ED8", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#0B132B", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("TEMPEST SHRINE ALTAR", Subtitle = "Maelstrom Weather & Lightning Conductor", BackgroundColor = "#1C2541", TitleColor = "#BFDBFE")]
[ComponentThunderstorm(FlashInterval = 2.8f, RainIntensity = 1.5f, LightningColor = "#C7D2FE", RainColor = "#60A5FA66")]
public class TempestShrineAltar : MonoBehaviour
{
    [Header("Storm Invocation")]
    public float atmosphericBarometricPressureHpa = 965f;
    public float electricChargePotentialKv = 850f;
    public int simultaneousLightningArcs = 6;

    [Header("Maelstrom Status")]
    public bool isSeaTideRising = true;
    public float seaSurgeHeightMeters = 8.4f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep oceanic indigo or dark stormcloud navy (`#0B132B`) maximizes lightning flash impact. |
| **`[ComponentHeader]`** | High | Header titles stand out sharply when illuminated by passing lightning bursts. |
| **`[ComponentSound]`** | High | Combine with rolling thunder audio clips on button clicks for intense atmospheric presence. |
| **Inspector Controls** | High | `PickingMode.Ignore` guarantees completely unhindered mouse events on all sliders, foldouts, and input fields. |
