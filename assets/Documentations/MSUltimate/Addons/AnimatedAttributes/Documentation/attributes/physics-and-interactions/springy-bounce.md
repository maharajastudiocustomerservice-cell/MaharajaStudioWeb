# [SpringyBounce]

> Applies damped harmonic oscillator spring physics on click, hover, or value change events across inspector fields.

---

## 1. Overview & Value Proposition

**What it does:**
`[SpringyBounce]` applies organic squash-and-stretch spring dynamics to inspector elements. Powered by a damped harmonic oscillator model with customizable spring stiffness ($k$, `Stiffness`) and friction damping ($c$, `Damping`), the element reacts with a tactile scale impulse (`TriggerScaleBump`) whenever clicked, hovered, or modified, bouncing and settling realistically back to rest.

**The Problem:**
Standard editor controls are static and visually stiff. Clicking a button, toggling an option, or entering a new value produces zero physical response, creating an interface that feels lifeless and unresponsive compared to modern desktop operating systems and games.

**The Solution:**
Decorating interactive fields and controls with `[SpringyBounce]`:
- **Damped Harmonic Physics:** Simulates true Hooke's law spring oscillation with second-order differential dynamics.
- **Micro-Scale Impulse:** Triggers a momentary scale punch (`TriggerScaleBump`), stretching and compressing the UI frame before settling.
- **Tuning Versatility:** Adjust spring stiffness (`Stiffness`) and damping ratio (`Damping`) to achieve anything from stiff mechanical clicks to jelly-like wobbles.
- **Universal Field Compatibility:** Decorate fields or properties to breathe life into everyday data entry.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class BouncyUI : MonoBehaviour
{
    [SpringyBounce(stiffness: 180f, damping: 14f)]
    public float bouncyTension = 1.0f;
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
public SpringyBounceAttribute(float stiffness = 160f, float damping = 12f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `stiffness` | `float` | `160f` | Spring stiffness coefficient $k$ controlling oscillation frequency. |
| `damping` | `float` | `12f` | Spring damping coefficient $c$ controlling decay rate and friction. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Stiffness` | `float` | `160f` | Spring stiffness constant $k$. |
| `Damping` | `float` | `12f` | Spring damping friction constant $c$. |
| `TriggerScaleBump` | `float` | `0.12f` | Scale impulse magnitude applied to the element upon trigger. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlatformerCharacterMotor : MonoBehaviour
{
    [Header("Trampoline Jump Impulse")]
    [SpringyBounce(
        stiffness: 220f, 
        damping: 10f, 
        TriggerScaleBump = 0.18f
    )]
    public float jumpBounceForce = 850f;

    [Header("Squash and Stretch Multiplier")]
    [SpringyBounce(stiffness: 140f, damping: 8f, TriggerScaleBump = 0.15f)]
    public float squashFactor = 1.25f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Spring oscillation applies to the property frame without jittering parent box containers. |
| `[Tilt3DHover]` | Stacking | Combines pseudo-3D perspective tilt with springy scale bounce for ultra-tactile cards. |
| `[FloatUpDeltaNumber]` | Stacking | Bounces the field elastically while numbers float upward on value adjustments. |
