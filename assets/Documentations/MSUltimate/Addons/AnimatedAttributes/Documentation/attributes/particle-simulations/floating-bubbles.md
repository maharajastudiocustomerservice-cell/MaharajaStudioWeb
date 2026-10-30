# [FloatingBubbles]

> Spawns gentle rising soap bubbles that wobble with fluid buoyancy and pop into tiny droplets upon cursor hover or interaction.

---

## 1. Overview & Value Proposition

**What it does:**
`[FloatingBubbles]` imbues inspector fields with relaxing, organic ambiance by rendering buoyant translucent bubbles. The simulation spawns a steady flow of rising spherical bubbles (`BubbleCount`) floating upward at a configurable speed (`RiseSpeed`) with chromatic iridescence (`BubbleTint`). When the developer moves their mouse cursor over an active bubble, it wobbles elastically and pops into mist droplets.

**The Problem:**
Aquatic gameplay parameters, potion brewing mechanics, underwater vehicle stats, or playful casual games often look clinical when presented in standard dark-grey inspector palettes. There is no atmospheric ambient movement to convey fluid immersion or lighthearted design.

**The Solution:**
Decorating fluid, aquatic, or potion variables with `[FloatingBubbles]`:
- **Interactive Cursor Popping:** Moving your mouse over active bubbles triggers a playful wobble-and-pop particle splash.
- **Buoyancy & Fluid Dynamics:** Simulates authentic micro-wobble and sinusoidal lateral drift as bubbles rise through the container.
- **Atmospheric Visual Polish:** Adjust bubble count (`BubbleCount`), upward buoyancy velocity (`RiseSpeed`), and iridescent color tint (`BubbleTint`).
- **GPU-Friendly Drawing:** Employs low-cost vector primitives that sleep when the inspector tab is defocused.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PotionBrewingStation : MonoBehaviour
{
    [FloatingBubbles(count: 20, riseSpeed: 30f)]
    public float elixirBoilingTemperature = 85f;
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
public FloatingBubblesAttribute(int count = 15, float riseSpeed = 25f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `count` | `int` | `15` | Total number of simultaneous floating bubbles spawned in the field backdrop. |
| `riseSpeed` | `float` | `25f` | Upward buoyancy speed in pixels per second. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BubbleCount` | `int` | `15` | Maximum active bubble particles circulating across the field. |
| `RiseSpeed` | `float` | `25f` | Vertical float rate in pixels per second. |
| `BubbleTint` | `string` | `"#38BDF8"` | Hex tint color applied to the translucent bubble skins (defaults to Sky Blue). |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SubmarineDepthControls : MonoBehaviour
{
    [Header("Ballast Tank Saturation")]
    [FloatingBubbles(
        count: 25, 
        riseSpeed: 35f, 
        BubbleTint = "#2DD4BF"
    )]
    public float ballastTankFillPercent = 72.5f;

    [Header("Life Support Dissolved Oxygen")]
    [FloatingBubbles(count: 12, riseSpeed: 20f, BubbleTint = "#93C5FD")]
    public float dissolvedOxygenPPM = 98f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Bubbles float seamlessly behind child fields inside bounded box groups. |
| `[LiquidDragSlider]` | Stacking | Combines floating background bubbles with elastic liquid slider handles for maximum aquatic aesthetic. |
| `[AnimatedProgressBar]` | Supported | Enhances fluid bars with background effervescent bubble animations. |
