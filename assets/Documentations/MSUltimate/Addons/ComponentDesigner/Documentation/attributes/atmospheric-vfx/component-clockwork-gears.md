# [ComponentClockworkGears]

> Renders animated interlocking clockwork brass gears rotating in synchronized motion across the component background.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentClockworkGears]` wraps the component inspector in an animated steampunk mechanical aesthetic. Driven by UI Toolkit vector painters in `ComponentSlot.ContentOverlay`, it renders an ensemble of precision-meshed brass gears (`GearCount = 4`, supporting 2 to 5 interlocking cogs) rotating at continuous synchronized velocity (`RotationSpeed = 0.6f`). The gears counter-rotate relative to their adjoining cogs with configurable warm brass or bronze hues (`GearColor = "#D97706"`) and subtle translucency (`Opacity = 0.18f`), ensuring technical readability remains paramount.

**The Problem:**
Steampunk chronometers, clockwork automatons, dwarven excavation machinery, and time-loop artifacts feel visually disconnected when represented by plain, static Unity inspector fields. Developers lack visual context when tuning intricate gear ratios, escapement timings, or steam pressure tolerances.

**The Solution:**
Decorating mechanical and automaton components with `[ComponentClockworkGears]`:
- **Interlocking Gear Kinematics:** Procedurally meshes cogs with accurate alternating rotational directions and tooth pitch ratios.
- **Atmospheric Mechanical Ambiance:** Soft vector alpha blending (`Opacity = 0.18f`) adds immersive steampunk flavor without competing with field readability.
- **Configurable Cog Assemblies:** Fine-tune tooth profiles, gear counts (2–5 cogs), and rotation rates to reflect the machine's speed.
- **Click-Through Transparency:** Injected into `ContentOverlay` with `PickingMode.Ignore`, guaranteeing that text boxes, curve editors, and buttons remain 100% interactive.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentClockworkGears(gearColor: "#D97706", rotationSpeed: 0.6f, gearCount: 4)]
public class ChronoEscapementMechanism : MonoBehaviour
{
    public float gearRatio = 3.75f;
    public float pendulumFrequencyHz = 1.0f;
    public int mainspringTensionJoules = 450;
    public bool isClockworkTicking = true;
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
public ComponentClockworkGearsAttribute()
public ComponentClockworkGearsAttribute(string gearColor = "#D97706", float rotationSpeed = 0.6f, int gearCount = 4)
```

- `gearColor`: Hex color string representing the brass or bronze gear wheel tint.
- `rotationSpeed`: Angular velocity multiplier governing gear rotation.
- `gearCount`: Number of interlocking cog wheels to render (clamped between 2 and 5).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GearColor` | `string` | `"#D97706"` | Hex color string for the brass or copper gear teeth and body. |
| `RotationSpeed` | `float` | `0.6f` | Angular velocity multiplier governing gear rotation. |
| `GearCount` | `int` | `4` | Number of interlocking cog wheels to render (supported range 2–5). |
| `Opacity` | `float` | `0.18f` | Overall background opacity multiplier of the vector gears. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#B45309", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#1A1208", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("DWARVEN GYROSCOPIC CORE", Subtitle = "Sector 4 Automated Clockwork Assembly", BackgroundColor = "#26190C", TitleColor = "#FDE68A")]
[ComponentClockworkGears(GearColor = "#D97706", RotationSpeed = 0.75f, GearCount = 5, Opacity = 0.22f)]
public class DwarvenClockworkAutomaton : MonoBehaviour
{
    [Header("Escapement & Dynamics")]
    [Tooltip("Primary mainspring torque output in Newton-meters.")]
    public float mainspringTorqueNm = 840f;

    [Tooltip("Secondary differential gear backlash tolerance.")]
    public float gearBacklashToleranceMm = 0.04f;

    [Tooltip("Steam pressure fed into the clockwork escapement manifold.")]
    public float steamPressurePsi = 120f;

    [Header("Overheat & Lubrication")]
    [Range(0f, 1f)]
    public float syntheticOilViscosity = 0.85f;
    public bool isSteamGovernorEngaged = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep bronze, charcoal, or dark mahogany backgrounds (`#1A1208`) make warm amber gears glow elegantly. |
| **`[ComponentHeader]`** | High | Place steampunk brass headers above the rotating cogs for a museum-grade gadget inspector. |
| **`[ComponentGildedGold]`** | High | Pairs seamlessly with gold leaf borders for royal and clockwork fantasy artefacts. |
| **Inspector Controls** | High | `PickingMode.Ignore` guarantees completely unhindered mouse events on all sliders, foldouts, and input fields. |
