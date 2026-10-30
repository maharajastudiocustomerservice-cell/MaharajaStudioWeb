# [BouncingText]

> Applies a springy letter-by-letter staggered bounce animation to field labels on hover or click.

---

## 1. Overview & Value Proposition

**What it does:**
`[BouncingText]` brings tactile feedback to inspector typography by segmenting field labels into individual character glyphs. When the user hovers over the field (`MouseEnterEvent`) or clicks to focus (`PointerDownEvent`), it triggers a choreographed wave bounce across the letters. Each consecutive character begins its bounce after a brief offset (`StaggerDelay`, defaulting to 35ms), ascending upward by `BounceHeight` (defaulting to 4px) along a sinusoidal trajectory ($y = -\sin(\text{progress} \cdot \pi) \cdot \text{BounceHeight}$) while temporarily shifting to a warm accent color (`BounceColor`, defaulting to amber `#F59E0B`).

**The Problem:**
Inspectors packed with dozens of monotonous text labels feel static and uninviting. Important fields—such as easter eggs, critical alerts, or promotional rewards—blend seamlessly into generic inspector panels without any subtle visual personality.

**The Solution:**
Decorating prominent properties with `[BouncingText]`:
- **Interactive Micro-Animation:** Rewards user interaction with immediate, springy kinetic feedback on mouse hover or click.
- **Sinusoidal Wave Trajectory:** Produces a fluid Mexican-wave hop across the text without jagged frame steps.
- **Dynamic Color Accents:** Characters temporarily adopt a vibrant highlight hue (`BounceColor`) at peak bounce height.
- **Graceful Lifecycle Management:** Executes only during active bounces; automatically shuts down animation scheduling when all letters return to rest.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SpecialRewardChest : MonoBehaviour
{
    [BouncingText(bounceHeight: 5f, staggerDelay: 30f, BounceColor = "#FBBF24")]
    public string legendaryItemDrop = "Excalibur";
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
| **Collection Support** | Supported on fields in wrapper classes (`List<MyClass>`); Direct collection cascading is intentionally not supported. |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public BouncingTextAttribute()

public BouncingTextAttribute(float bounceHeight, float staggerDelay = 35f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `bounceHeight` | `float` | `4f` | Peak height in pixels each character bounces upward. |
| `staggerDelay` | `float` | `35f` | Delay between each consecutive character's bounce in milliseconds. |

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BounceHeight` | `float` | `4f` | Maximum upward pixel displacement during the hop. |
| `StaggerDelay` | `float` | `35f` | Stagger offset in milliseconds between adjacent letter animations. |
| `BounceDuration` | `float` | `280f` | Total duration of a single character's bounce hop in milliseconds. |
| `BounceColor` | `string` | `"#F59E0B"` | Hex color string applied to each character while at peak bounce height. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ArcadeScoreBoard : MonoBehaviour
{
    [Header("Hero Text Banners")]
    [BouncingText(bounceHeight: 6f, staggerDelay: 40f, BounceColor = "#EC4899", BounceDuration = 320f)]
    public string topPlayerName = "PLAYER_ONE";

    [BouncingText(bounceHeight: 4f, staggerDelay: 25f, BounceColor = "#10B981")]
    public int highStreakCount = 99;

    [BouncingText(bounceHeight: 5f, staggerDelay: 35f, BounceColor = "#3B82F6")]
    public float comboMultiplier = 4.5f;

    [Header("Wrapper Classes in Lists")]
    [Tooltip("Fields inside custom wrapper classes inside lists animate cleanly without disrupting inspector layout.")]
    public List<ArcadeMarqueeSlot> marqueeSlots = new List<ArcadeMarqueeSlot>
    {
        new ArcadeMarqueeSlot { cabinetLocation = "Main Floor", marqueeText = "STEP RIGHT UP & WIN!" }
    };

    [Serializable]
    public class ArcadeMarqueeSlot
    {
        public string cabinetLocation = "Main Midway";

        [BouncingText(bounceHeight: 4f, staggerDelay: 30f, BounceColor = "#F59E0B")]
        public string marqueeText = "HIGH SCORE RECORD!";
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### 7.1 Layout & Conditional Stacking

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[BoxGroup]` / `[HorizontalGroup]`** | High | Fits cleanly inside any container; retains full label layout alignment. |
| **`[ShowIf]` / `[EnableIf]`** | High | Safely rebinds and triggers smoothly when conditionally revealed. |
| **`[WavyText]` / `[GradientTextFlow]`** | Avoid | Multiple text-manipulation attributes targeting the same label will conflict over child character elements; choose one per field. |
| **Validation Attributes** | High | Fully compatible with `[Required]`, `[Range]`, and `[ValidateNotNull]`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Not Supported | Direct arrays are intentionally not cascaded. |
| **Generic Lists (`List<T>`)** | Not Supported | Direct lists are intentionally not cascaded. |
| **Wrapper Classes in Lists (`List<MyClass>`)** | Supported | Operates seamlessly on fields declared inside wrapper classes rendered inline or within collections. |
| **Unity UI Toolkit** | Supported | Attaches lifecycle callbacks (`MouseEnterEvent`, `PointerDownEvent`) directly to the generated `Label` element. |
