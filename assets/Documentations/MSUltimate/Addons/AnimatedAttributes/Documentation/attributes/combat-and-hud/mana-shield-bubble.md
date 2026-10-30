# [ManaShieldBubble]

> Renders an undulating hexagonal forcefield shield with chromatic ripples around defensive or energy fields.

---

## 1. Overview & Value Proposition

**What it does:**
`[ManaShieldBubble]` wraps the decorated inspector field in an animated sci-fi or fantasy hexagonal energy barrier. The forcefield grid features undulating ambient luminescence and emits expanding ripples across its honeycomb cells whenever the user hovers or interacts with the control.

**The Problem:**
Magic shields, protective barriers, energy conduits, and sci-fi deflector fields look identical to standard health or armor stats in generic inspectors, obscuring the magical or technological nature of the mechanic.

**The Solution:**
Decorating protective stats with `[ManaShieldBubble]`:
- **Animated Honeycomb Grid:** Procedurally renders a glowing hexagonal tessellation directly behind and around the field.
- **Interactive Energy Ripples:** Clicking or modifying values propagates concentric wave ripples (`RippleSpeed`) through the shield lattice.
- **Customizable Barrier Palette:** Modify barrier theme color (`ShieldColor`) from cyan mana shields to amber kinetic barriers or purple void shields.
- **Adjustable Cell Geometry:** Scale individual hexagonal cell radius (`HexSize`) to fit narrow or wide inspector layouts.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ArcaneMage : MonoBehaviour
{
    [ManaShieldBubble(shieldColor: "#06B6D4", HexSize = 16f)]
    public float manaShieldAbsorption = 250f;
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
public ManaShieldBubbleAttribute(string shieldColor = "#06B6D4")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `shieldColor` | `string` | `"#06B6D4"` | Hex color string for the hexagonal shield grid lines and glow. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShieldColor` | `string` | `"#06B6D4"` | Hex color string for the forcefield honeycomb grid. |
| `HexSize` | `float` | `14f` | Radius size of individual hexagonal shield cells in pixels. |
| `RippleSpeed` | `float` | `2.5f` | Propagation speed multiplier of interactive ripple waves. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class StarshipDefenses : MonoBehaviour
{
    [Header("Deflector Array")]
    [ManaShieldBubble(shieldColor: "#38BDF8", HexSize = 18f, RippleSpeed = 3.0f)]
    public float forwardShieldCapacity = 1500f;

    [Header("Void Barrier Matrix")]
    [ManaShieldBubble(shieldColor: "#A855F7", HexSize = 12f)]
    public float voidBarrierRechargeRate = 45f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Forcefield grid seamlessly frames within group containers. |
| `[Range]` | Supported | Functions cleanly on slider bars; ripples propagate on slider drag. |
| `[AnimatedProgressBar]` | Supported | Combines progress bar fills with glowing hexagonal shield textures. |
