# [AnimatedHover]

> Smoothly transitions scale, rotation, background color, text color, and margins when the mouse cursor hovers over an inspector field.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms standard static inspector rows into tactile, responsive UI elements. When the user hovers their mouse over the field, it triggers smooth hardware-accelerated transitions adjusting scale (`ScaleOnHover`), background highlight (`BackgroundColorOnHover`), text color, slight tilt rotations, and margin offsets.

**The Problem:**
Standard Unity inspectors feel completely static and unresponsive, offering no visual feedback that an element is interactive until clicked.

**The Solution:**
Add `[AnimatedHover]` to any field or property:
- **Tactile Responsiveness:** Subtle scale lifts (`1.02x`) and color shifts reward user interaction.
- **Micro-Interaction Polish:** Create high-end modern tools that feel alive and responsive.
- **Configurable Transitions:** Tune duration (`TransitionDuration = 150ms`) and UI Toolkit easing modes (`EaseInOut`, `EaseOut`, `Linear`).
- **Granular Styling:** Control individual margin shifts and background tones.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class GameSettings : MonoBehaviour
{
    [AnimatedHover(ScaleOnHover = 1.03f, BackgroundColorOnHover = "#4a69bd", TransitionDuration = 120f)]
    public float masterVolume = 1.0f;
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
public AnimatedHoverAttribute()
```

*Attribute initializes with standard subtle hover scaling; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ScaleOnHover` | `float` | `1.02f` | Scale factor applied to the element while hovered. |
| `BackgroundColorOnHover` | `string` | `"#3E3E3E"` | Hex color string for the background on hover. |
| `TextColorOnHover` | `string` | `"#FFFFFF"` | Hex color string for text on hover. |
| `RotateOnHover` | `float` | `0f` | Rotation angle in degrees on hover. |
| `MarginTopOnHover` | `float` | `-1f` | Top margin in pixels on hover (`-1` leaves unchanged). |
| `MarginBottomOnHover` | `float` | `-1f` | Bottom margin in pixels on hover (`-1` leaves unchanged). |
| `MarginLeftOnHover` | `float` | `-1f` | Left margin in pixels on hover (`-1` leaves unchanged). |
| `MarginRightOnHover` | `float` | `-1f` | Right margin in pixels on hover (`-1` leaves unchanged). |
| `TransitionDuration` | `float` | `150f` | Transition duration in milliseconds. |
| `EasingMode` | `EasingMode` | `EasingMode.EaseInOut` | Transition easing curve (e.g. `EaseInOut`, `EaseOut`, `Linear`). |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using UnityEngine.UIElements;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlayerAbilityConfig : MonoBehaviour
{
    [Header("Primary Combat Action (Hover to Inspect)")]
    [AnimatedHover(
        ScaleOnHover = 1.04f, 
        BackgroundColorOnHover = "#2c3e50", 
        TextColorOnHover = "#f1c40f", 
        TransitionDuration = 140f, 
        EasingMode = EasingMode.EaseOut
    )]
    public float fireballDamage = 120f;

    [AnimatedHover(ScaleOnHover = 1.02f, BackgroundColorOnHover = "#16a085")]
    public float manaCost = 25f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Hover scaling expands cleanly inside group containers. |
| `[ClickRipple]` | Supported | Pair with `[ClickRipple]` for complete hover-and-click tactile feedback. |
| Primary Drawers | Supported | Enhances native and custom field drawers without interrupting data edits. |
