# [ComponentPulseGlow]

> Adds an animated, radiating pulse glow that breathes rhythmically from the component card borders with customizable radius, speed, and hue.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentPulseGlow]` wraps the component card in a living ambient light emission. Injected into `ComponentSlot.BodyWrapper`, it renders a soft outer glow perimeter that expands and contracts rhythmically between minimum (`MinRadius`) and peak (`MaxRadius`) radii. Using harmonic sinusoidal interpolation, it oscillates illumination smoothly over time (`Speed`), supporting custom luminous hex colors (`Color`), peak transparency (`Opacity`), and corner rounding (`BorderRadius`) that conforms precisely to the host component's frame.

**The Problem:**
High-priority components—such as active boss controllers, game loop managers, mission-critical network relays, or selected development tools—look identical to inert utility components in long inspector lists. Developers lack an eye-catching way to highlight vital systems during testing and balancing.

**The Solution:**
Decorating critical components with `[ComponentPulseGlow]`:
- **Rhythmic Ambient Breathing:** Simulates an organic, breathing aura that immediately directs developer focus toward priority components.
- **Configurable Pulse Dynamics:** Adjust pulsation period (`Speed = 2f`), minimum core radius (`MinRadius = 2f`), and outer bloom spread (`MaxRadius = 8f`).
- **Precision Outer Alignment:** Matches the card's outer boundaries via `BorderRadius` so the glow blooms evenly from all edges.
- **Zero Control Obstruction:** Operates as a wrapper visual element outside the control hierarchy, ensuring controls receive uninterrupted mouse input.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentPulseGlow(Color = "#EF4444", MaxRadius = 10f, MinRadius = 2f, Speed = 1.5f, Opacity = 0.6f)]
public class BossEncounterPhaseManager : MonoBehaviour
{
    public int currentEncounterPhase = 3;
    public float enragedDamageMultiplier = 2.0f;
    public bool isEnrageTimerActive = true;
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
| **Component Slot** | `BodyWrapper` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentPulseGlowAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#4FC3F7"` | Hex color string for the radiating glow halo. |
| `MaxRadius` | `float` | `8f` | Maximum outward bloom spread in pixels at peak pulse expansion. |
| `MinRadius` | `float` | `2f` | Minimum glow thickness in pixels at pulse contraction trough. |
| `Speed` | `float` | `2f` | Full pulsation breath cycle duration in seconds. |
| `Opacity` | `float` | `0.5f` | Maximum glow opacity alpha at peak illumination (0.0 to 1.0). |
| `BorderRadius` | `float` | `6f` | Corner rounding radius in pixels of the glow contour. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#F59E0B", Width = 2f, Radius = 8f)]
[ComponentBackground("#1A1308", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("CRITICAL SYSTEM KERNEL", Subtitle = "Master Game State Authority", BackgroundColor = "#2A1D0B", TitleColor = "#FEF3C7")]
[ComponentPulseGlow(Color = "#FBBF24", MaxRadius = 12f, MinRadius = 3f, Speed = 1.8f, Opacity = 0.55f, BorderRadius = 8f)]
public class CriticalSystemKernel : MonoBehaviour
{
    [Header("Engine Loop")]
    public float targetFrameRate = 120f;
    public float physicsFixedDeltaTime = 0.02f;
    public bool isDeterministicTickEnabled = true;

    [Header("Telemetry")]
    public float allocatedMemoryMB = 450.2f;
    public int activeEntitiesCount = 1420;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBorder]`** | High | Matches `BorderRadius` with the border stroke so the glow radiates uniformly from the card frame. |
| **`[ComponentBackground]`** | High | Darker card background fills accentuate the luminous contrast of the radiating outer glow. |
| **Inspector Controls** | High | Injected into `BodyWrapper`, wrapping around the body container without interfering with inner UI events. |
