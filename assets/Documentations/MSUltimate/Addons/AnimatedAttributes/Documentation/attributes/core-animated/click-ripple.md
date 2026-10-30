# [ClickRipple]

> Applies a tactile scale bump depression and color flash animation whenever an inspector field is clicked.

---

## 1. Overview & Value Proposition

**What it does:**
Injects rich tactile micro-interaction feedback upon clicking. When the user clicks or presses the field, the control briefly depresses (`BumpScale = 0.95x`) and flashes an overlay tint (`FlashColor`), simulating a responsive physical button or touchscreen push.

**The Problem:**
Inspector fields and custom buttons often give no visual confirmation of click registration, leaving developers unsure if their click was registered during busy editor operations.

**The Solution:**
Add `[ClickRipple]` to any field:
- **Instant Physical Tactility:** Subtle scale compression gives an authentic physical button feel.
- **Visual Click Flash:** High-speed flash ripple (`BumpDuration = 100ms`) provides instant acknowledgment.
- **Customizable Theming:** Choose custom flash hex tints (e.g. white, neon cyan, gold).
- **Zero Overhead:** Managed purely via transient UI Toolkit visual state triggers.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class TriggerPad : MonoBehaviour
{
    [ClickRipple(BumpScale = 0.93f, BumpDuration = 80f, FlashColor = "#00FFFF77")]
    public bool triggerAction = false;
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
public ClickRippleAttribute()
```

*Attribute initializes with standard 0.95x bump scaling; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BumpScale` | `float` | `0.95f` | Target scale factor during click depression. |
| `BumpDuration` | `float` | `100f` | Total duration in milliseconds for the bump animation. |
| `FlashColor` | `string` | `"#ffffff55"` | Hex color string for flash overlay during click. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CombatActionPad : MonoBehaviour
{
    [Header("Tactile Combat Actions")]
    [ClickRipple(BumpScale = 0.92f, BumpDuration = 90f, FlashColor = "#f1c40f88")]
    public bool executePrimaryAttack;

    [ClickRipple(BumpScale = 0.95f, FlashColor = "#e74c3c66")]
    public bool executeUltimateSkill;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[AnimatedHover]` | Supported | Pairs perfectly with hover animations for end-to-end interactive polish. |
| `[BoxGroup]` | Supported | Functions cleanly inside group containers. |
| Buttons & Toggles | Supported | Enhances custom button drawers and toggles. |
