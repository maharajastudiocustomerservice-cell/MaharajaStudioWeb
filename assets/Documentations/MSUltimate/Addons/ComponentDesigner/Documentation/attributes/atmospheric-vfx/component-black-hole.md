# [ComponentBlackHole]

> Renders an animated black hole accretion disk and gravitational vortex header card with rotating relativistic matter rings.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentBlackHole]` introduces astrophysics visuals to component inspectors. Injected into `ComponentSlot.BeforeContent` (`Order = 8`), it renders a dedicated 64px header banner displaying a black hole with a dark event horizon core (`EventHorizonRadius = 20f`) surrounded by an intensely glowing, rotating accretion disk (`AccretionDiskColor = "#F59E0B"`, `RotationSpeed = 1.0f`). Relativistic matter rings swirl and deform around the singularity with subtle gravitational lensing and customizable opacity (`Opacity = 0.28f`).

**The Problem:**
Gravitational physics solvers, spacetime singularity engines, void magic spells, and celestial mechanics feel dry when configured in plain text-based inspector panels. Developers lack immediate visual cues that convey immense gravitational force.

**The Solution:**
Decorating astrophysics and void systems with `[ComponentBlackHole]`:
- **Relativistic Accretion Swirl:** Animates rotating elliptical accretion matter bands around the dark event horizon core.
- **Gravitational Lensing Distortion:** Simulates light warping around the singularity boundary for cosmic visual fidelity.
- **Dedicated Header Card:** Anchors cleanly in `BeforeContent` with a fixed 64px height and contained overflow.
- **Zero Input Interruption:** Operates with `PickingMode.Ignore`, ensuring all standard Unity controls remain completely accessible.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBlackHole(accretionDiskColor: "#F59E0B", rotationSpeed: 1.2f, eventHorizonRadius: 22f)]
public class SingularityGravitationalWell : MonoBehaviour
{
    public float eventHorizonRadiusMeters = 15f;
    public float gravitationalPullForce = 2500f;
    public bool isSpacetimeHawkingRadiationEnabled = true;
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
| **Component Slot** | `BeforeContent` (`Order = 8`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentBlackHoleAttribute()
public ComponentBlackHoleAttribute(string accretionDiskColor = "#F59E0B", float rotationSpeed = 1.0f, float eventHorizonRadius = 20f)
```

- `accretionDiskColor`: Hex color string for the swirling accretion disk matter (e.g. `"#F59E0B"`).
- `rotationSpeed`: Accretion disk rotation velocity multiplier.
- `eventHorizonRadius`: Radius in pixels of the central dark event horizon.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `AccretionDiskColor` | `string` | `"#F59E0B"` | Hex color string for the glowing accretion disk. |
| `RotationSpeed` | `float` | `1.0f` | Rotational velocity multiplier for swirling matter rings. |
| `EventHorizonRadius` | `float` | `20f` | Radius in pixels of the dark central gravitational event horizon. |
| `Opacity` | `float` | `0.28f` | Transparency alpha of the accretion disk simulation (0.0 to 1.0). |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#D97706", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#140E06", BorderRadius = 6f, Padding = 10f)]
[ComponentBlackHole(AccretionDiskColor = "#F59E0B", RotationSpeed = 1.4f, EventHorizonRadius = 24f, Opacity = 0.35f)]
[ComponentHeader("SUPERMASSIVE SINGULARITY ENGINE", Subtitle = "General Relativistic Gravity Solver", BackgroundColor = "#1F1508", TitleColor = "#FEF3C7")]
public class SupermassiveSingularityEngine : MonoBehaviour
{
    [Header("Singularity Metric")]
    public float schwarzschildRadiusMeters = 3000f;
    public float kerrSpinParameterA = 0.98f;
    public float frameDraggingAngularVelocity = 0.15f;

    [Header("Tidal Forces")]
    public float spaghettificationTidalTensor = 9800f;
    public bool enableErgospherePenroseProcess = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Injected at `Order = 8` in `BeforeContent`, crowning header titles with an accretion disk banner. |
| **`[ComponentBackground]`** | High | Deep void black or cosmic brown backgrounds provide strong contrast for golden accretion matter rings. |
| **Inspector Controls** | High | Renders in a dedicated header element with `PickingMode.Ignore`, preserving responsiveness for all fields below. |
