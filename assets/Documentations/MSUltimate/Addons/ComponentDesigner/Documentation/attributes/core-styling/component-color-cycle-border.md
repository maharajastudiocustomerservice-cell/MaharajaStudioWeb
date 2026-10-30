# [ComponentColorCycleBorder]

> Wraps the component in a full rainbow spectrum border that continuously cycles through the HSL hue wheel with zero extra DOM overhead.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentColorCycleBorder]` provides a smooth, full-spectrum rainbow border around the component inspector. Driven by `EditorApplication.update`, it smoothly cycles the border color through the complete 360° HSL hue wheel (`Color.HSVToRGB(hue, Saturation, Lightness)`), taking `Speed` seconds (defaulting to 5.0s) per full rotation. Unlike heavy multi-element rainbow shaders, it mutates the existing border style colors directly with zero extra visual tree elements, ensuring buttery smooth inspector performance.

**The Problem:**
Highlighting legendary items, prism generators, or Easter egg debug tools with static colors fails to reflect their rainbow or prismatic nature. Furthermore, custom shader effects often add heavy rendering overhead to the editor window.

**The Solution:**
Decorating prismatic components with `[ComponentColorCycleBorder]`:
- **Continuous 360° Hue Rotation:** Traverses smoothly through the entire color spectrum (red $\to$ yellow $\to$ green $\to$ cyan $\to$ blue $\to$ magenta $\to$ red).
- **Zero Additional DOM Elements:** Directly updates container border color styles without spawning additional elements.
- **Configurable HSL Parameters:** Fine-tune `Saturation`, `Lightness`, `Opacity`, and rotation duration (`Speed`).
- **BodyWrapper Slot Integration:** Encapsulates the entire component body without distorting internal field margins.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentColorCycleBorder(Width = 2.5f, Radius = 8f, Speed = 4f)]
public class PrismaticCoreManager : MonoBehaviour
{
    public float prismaticEnergy = 100f;
    public bool isOvercharged = false;
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
| **Component Slot** | `BodyWrapper` (`Order = 5`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentColorCycleBorderAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Width` | `float` | `2f` | Border stroke width in pixels. |
| `Radius` | `float` | `6f` | Corner rounding radius in pixels. |
| `Saturation` | `float` | `0.7f` | Color saturation clamped between `0.0` (grayscale) and `1.0` (vivid). |
| `Lightness` | `float` | `0.6f` | Color lightness clamped between `0.0` (dark) and `1.0` (bright). |
| `Speed` | `float` | `5f` | Duration in seconds for a full 360° hue cycle rotation. |
| `Opacity` | `float` | `0.8f` | Border alpha opacity clamped between `0.0` and `1.0`. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentColorCycleBorder(Width = 3f, Radius = 10f, Speed = 3.5f, Saturation = 0.85f, Lightness = 0.65f, Opacity = 0.9f)]
[ComponentBackground("#111827", BorderRadius = 10f, Padding = 12f)]
public class GodModeCheatController : MonoBehaviour
{
    [Header("Developer Privileges")]
    public bool unlimitedHealth = true;
    public bool infiniteAmmo = true;
    public float walkSpeedMultiplier = 2.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Recommended companion; dark backgrounds make the cycling rainbow border colors pop vividly. |
| **`[ComponentHeader]`** | High | The rainbow border encompasses both header cards and inner controls seamlessly. |
| **`[ComponentBorder]` / `[ComponentAnimatedBorder]`** | Avoid | Only one border wrapper should be applied per component to prevent conflicting stroke borders. |
| **`[ComponentBadge]`** | High | Floating corner tags sit gracefully atop the cycling border frame. |
