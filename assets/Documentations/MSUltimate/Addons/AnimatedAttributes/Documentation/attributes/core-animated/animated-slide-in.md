# [AnimatedSlideIn]

> Smoothly slides an inspector element into view horizontally when the inspector panel loads or becomes visible.

---

## 1. Overview & Value Proposition

**What it does:**
Animates the entry transition of an inspector field. When the inspector window or GameObject selection initializes, the field smoothly slides into position from a specified horizontal offset (`SlideOffset`) with customizable duration (`SlideDuration`) and optional stagger delay (`Delay`).

**The Problem:**
Inspectors pop onto the screen abruptly with rigid static layouts, lacking the cinematic polish found in AAA game developer tooling and modern dashboard software.

**The Solution:**
Add `[AnimatedSlideIn]` to fields:
- **Cinematic Entry:** Gives tools and editors a modern, premium fluid feel.
- **Configurable Direction & Offset:** Slide in from the left (`-50px`) or right (`+50px`).
- **Cascading Stagger:** Stagger multiple fields using sequential `Delay` offsets (e.g. `0ms`, `50ms`, `100ms`).
- **Hardware Accelerated:** Uses UI Toolkit translate transforms for zero performance cost.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class WelcomeBanner : MonoBehaviour
{
    [AnimatedSlideIn(SlideOffset = -80f, SlideDuration = 350f)]
    public string welcomeMessage = "System Initialized";
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
public AnimatedSlideInAttribute()
```

*Attribute initializes with standard 50px left slide-in; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `SlideOffset` | `float` | `-50f` | Initial horizontal pixel offset to slide in from (negative = left, positive = right). |
| `SlideDuration` | `float` | `400f` | Animation duration in milliseconds. |
| `Delay` | `float` | `0f` | Stagger delay in milliseconds before slide animation begins. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class MissionBriefing : MonoBehaviour
{
    [Header("Cascading Mission Parameters")]
    [AnimatedSlideIn(SlideOffset = -60f, SlideDuration = 300f, Delay = 0f)]
    public string missionTitle = "Operation Red Dust";

    [AnimatedSlideIn(SlideOffset = -60f, SlideDuration = 300f, Delay = 60f)]
    public int operativeCount = 4;

    [AnimatedSlideIn(SlideOffset = -60f, SlideDuration = 300f, Delay = 120f)]
    public float timeLimitMinutes = 20f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Elements slide smoothly inside group containers without overflow clipping. |
| Sequential Stacking | Supported | Chain varying `Delay` values across adjacent fields for beautiful waterfall cascades. |
| Primary Drawers | Supported | Operates strictly on container translation, leaving controls interactable. |
