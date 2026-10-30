# [AnimatedRainbowText]

> Continuously cycles the field label text through the RGB/HSV color spectrum with customizable cycle speeds, saturation, and lightness.

---

## 1. Overview & Value Proposition

**What it does:**
Animates the label text of any field or property with a smooth, continuous chromatic RGB/HSV color cycle. Perfect for highlighting god-tier items, developer cheat flags, Easter eggs, or supercharged gameplay variables.

**The Problem:**
Standard inspector text is monochrome and static, failing to give high-tier cosmetic or developer-exclusive settings an immediate distinctive appearance.

**The Solution:**
Add `[AnimatedRainbowText]` to any field:
- **Vibrant Chromatic Motion:** Label smoothly cycles through vivid rainbow hues in real time.
- **HSV Palette Tuning:** Adjust color saturation (`Saturation = 0.8f`) and lightness (`Lightness = 0.6f`).
- **Speed Control:** Speed up or slow down the rainbow cycle frequency (`CycleSpeed`).
- **Zero Allocation:** Color animation is evaluated efficiently via hardware-accelerated style ticks.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CheatManager : MonoBehaviour
{
    [AnimatedRainbowText(CycleSpeed = 1.5f, Saturation = 1f, Lightness = 0.6f)]
    public bool godModeActive = false;
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
public AnimatedRainbowTextAttribute()
```

*Attribute initializes with standard 1Hz rainbow cycle; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CycleSpeed` | `float` | `1f` | Speed of the rainbow chromatic color cycle in Hz. |
| `Saturation` | `float` | `1f` | HSV color saturation (0 = grayscale, 1 = maximum vibrance). |
| `Lightness` | `float` | `0.5f` | HSV lightness/value (0 = dark, 1 = bright). |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class MythicItemDefinition : MonoBehaviour
{
    [Header("Cosmetic Mythic Weapon Configuration")]
    [AnimatedRainbowText(CycleSpeed = 2f, Saturation = 0.9f, Lightness = 0.65f)]
    public string weaponTitle = "Prismatic Core Destroyer";

    [AnimatedRainbowText(CycleSpeed = 0.8f)]
    public float rainbowAuraIntensity = 5.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Rainbow text renders inside group containers. |
| `[AnimatedHover]` | Supported | Composes with hover scale effects. |
| Primary Drawers | Supported | Applies strictly to the label element, keeping input controls standard. |
