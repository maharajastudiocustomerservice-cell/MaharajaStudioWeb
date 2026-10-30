# [MagneticHover]

> Applies a spring-based magnetic pull physics effect that smoothly attracts the inspector element toward the mouse cursor on hover.

---

## 1. Overview & Value Proposition

**What it does:**
Introduces playful, organic physics interactions into the Inspector. When the mouse cursor moves within `MagneticRadius` (in pixels) of the field, the element is drawn magnetically toward the cursor up to `MaxPullDistance`, springing back into place (`SpringForce`) when the mouse leaves.

**The Problem:**
Standard UI elements feel dead and completely disconnected from the mouse cursor, making the editor experience rigid and dry.

**The Solution:**
Add `[MagneticHover]` to key fields or buttons:
- **Organic Physics Micro-Interaction:** High-polish spring magnetic pull responds dynamically to cursor proximity.
- **Configurable Magnetic Field:** Tune attraction radius (`MagneticRadius = 150px`) and maximum displacement pull.
- **Natural Spring Snapback:** Damped spring return restores element alignment instantly upon cursor departure.
- **Ideal for Action Buttons & Sliders:** Makes key interactive settings feel magnetic and enticing.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SpecialAction : MonoBehaviour
{
    [MagneticHover(MagneticRadius = 120f, MaxPullDistance = 12f, SpringForce = 0.25f)]
    public bool triggerSpecialEvent = false;
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
public MagneticHoverAttribute()
```

*Attribute initializes with standard 150px radius and 15px max pull; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MagneticRadius` | `float` | `150f` | Maximum distance in pixels from cursor before magnetic attraction triggers. |
| `MaxPullDistance` | `float` | `15f` | Maximum displacement in pixels the element can be pulled toward the cursor. |
| `SpringForce` | `float` | `0.2f` | Spring stiffness factor controlling attraction responsiveness and snapback. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class MagicSpellDefinition : MonoBehaviour
{
    [Header("Ultimate Spell Trigger")]
    [MagneticHover(MagneticRadius = 180f, MaxPullDistance = 20f, SpringForce = 0.3f)]
    public bool castUltimateSkill = false;

    [Header("Mana Overdrive Amplification")]
    [MagneticHover(MaxPullDistance = 10f)]
    public float manaOverdriveMultiplier = 2.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ClickRipple]` | Supported | Pairs with click ripples for delightful magnetic button feel. |
| `[BoxGroup]` | Supported | Contained cleanly inside layout cards. |
| Primary Drawers | Supported | Operates via transform translation without interrupting mouse click events. |
