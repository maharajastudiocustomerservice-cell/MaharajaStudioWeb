# [ComponentBorder]

> Wraps the entire component inspector inside a customizable decorative border with corner rounding, margins, and optional glow bloom.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentBorder]` wraps the entire component inspector inside a polished border stroke frame. Operating through `ComponentSlot.BodyWrapper`, it frames the component body with customizable border color (`Color`, defaulting to cyan `#4FC3F7`), stroke thickness (`Width`), corner rounding (`Radius`), and internal padding. In addition, enabling `Glow = true` wraps an outer luminous ambient shadow (`GlowSpread`) around the perimeter, giving critical systems an elevated, floating presence in the inspector.

**The Problem:**
Inspectors packed with multiple MonoBehaviours run together into a continuous gray vertical list without visual separation. Designers cannot tell where one system ends and another begins without hunting for the tiny header foldout arrows.

**The Solution:**
Decorating classes with `[ComponentBorder]`:
- **Definitive Visual Boundaries:** Clearly distinguishes individual components with crisp border frames.
- **Ambient Luminous Glow:** Supports a secondary outer glow bloom (`Glow = true`) for legendary or mission-critical managers.
- **Full Geometry Control:** Configurable border radius, top/bottom/left/right margins, and internal padding.
- **BodyWrapper Slot Integration:** Encapsulates the entire component DOM without disturbing standard field alignment.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#3B82F6", Width = 2f, Radius = 8f, Glow = true)]
public class AudioManager : MonoBehaviour
{
    public float masterVolume = 1.0f;
    public bool muteOnFocusLost = true;
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
| **Component Slot** | `BodyWrapper` (`Order = 10`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentBorderAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#4FC3F7"` | Border stroke hex color code. |
| `Width` | `float` | `2f` | Border stroke width in pixels. |
| `Radius` | `float` | `8f` | Corner rounding radius in pixels. |
| `Glow` | `bool` | `false` | When true, renders an ambient soft outer glow wrapper around the border. |
| `GlowColor` | `string` | `""` | Custom glow hex color; if empty, automatically derived from `Color` with reduced opacity. |
| `GlowSpread` | `float` | `6f` | Outer glow spread distance in pixels. |
| `Padding` | `float` | `6f` | Internal padding space between border and content. |
| `MarginTop` | `float` | `4f` | Exterior top margin outside the border. |
| `MarginBottom` | `float` | `4f` | Exterior bottom margin outside the border. |
| `MarginLeft` | `float` | `0f` | Exterior left margin outside the border. |
| `MarginRight` | `float` | `0f` | Exterior right margin outside the border. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#10B981", Width = 2.5f, Radius = 10f, Glow = true, GlowColor = "#10B98133", GlowSpread = 8f, Padding = 8f)]
[ComponentBackground("#064E3B", BorderRadius = 10f, Padding = 10f)]
public class LifeSupportSystem : MonoBehaviour
{
    [Header("Life Support Telemetry")]
    public float oxygenReservePercentage = 94.5f;
    public float cabinPressureKPa = 101.3f;
    public bool scrubbingCycleActive = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Standard companion; provides matching corner radius fills inside the framed border. |
| **`[ComponentHeader]`** | High | Fits the entire component header and body cleanly within the border stroke. |
| **`[ComponentAnimatedBorder]`** | Avoid | Choose either static `[ComponentBorder]` or kinetic two-color `[ComponentAnimatedBorder]`. |
| **Child Field Layouts** | High | Transparently wraps around all MSUltimate layout groups (`[BoxGroup]`, `[TabGroup]`). |
