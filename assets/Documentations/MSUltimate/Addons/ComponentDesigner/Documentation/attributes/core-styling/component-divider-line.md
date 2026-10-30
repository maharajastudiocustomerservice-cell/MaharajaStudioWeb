# [ComponentDividerLine]

> Adds a styled horizontal divider rule before or after the component body with customizable stroke thickness, margins, and gradient styling.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentDividerLine]` introduces clean visual demarcation between stacked component inspectors. Injecting into either `ComponentSlot.BeforeBody` (when `Position = ComponentPosition.Top`) or `ComponentSlot.AfterBody` (when `Position = ComponentPosition.Bottom`), it draws a crisp horizontal dividing rule. It supports customizable line color (`Color`, defaulting to slate `#444455`), stroke thickness (`Thickness`), horizontal and vertical margin spacing, and line styling presets (`Solid`, `Dashed`, or `Gradient` fading to `GradientEndColor`). Because `AllowMultiple = true`, it can be applied to both the top and bottom of a single component.

**The Problem:**
When multiple components reside on the same GameObject, standard Unity inspectors visually blend their boundaries. Without clear horizontal dividing rules, identifying where one script finishes and another starts requires scanning for foldout headers.

**The Solution:**
Decorating classes with `[ComponentDividerLine]`:
- **Definitive Boundary Separation:** Clearly partitions components with sleek horizontal rules.
- **Top or Bottom Positioning:** Place divider lines before the component (`Top`) or after it (`Bottom`) via `ComponentPosition`.
- **Styling Variations:** Switch between solid rules, dashed lines, or subtle gradient fades ($C_1 \to C_2$).
- **Support for Multiple Dividers:** Add distinct dividers above and below a single component.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentDividerLine(Position = ComponentPosition.Top, Color = "#3B82F6", Thickness = 2f)]
public class PlayerHealthManager : MonoBehaviour
{
    public float currentHealth = 100f;
    public float maxHealth = 100f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Component Slot** | `BeforeBody` (if `Top`) or `AfterBody` (if `Bottom`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentDividerLineAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Position` | `ComponentPosition` | `ComponentPosition.Top` | Placement of the divider rule (`Top` or `Bottom`). |
| `Color` | `string` | `"#444455"` | Hex color string for the divider stroke. |
| `Thickness` | `float` | `1f` | Stroke thickness in pixels. |
| `MarginHorizontal` | `float` | `0f` | Left and right margin spacing in pixels. |
| `MarginTop` | `float` | `4f` | Top margin spacing above the divider line. |
| `MarginBottom` | `float` | `4f` | Bottom margin spacing beneath the divider line. |
| `Style` | `ComponentDividerStyle` | `ComponentDividerStyle.Solid` | Visual style (`Solid`, `Dashed`, `Gradient`). |
| `GradientEndColor` | `string` | `"#00000000"` | Secondary color stop when `Style = Gradient`. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentDividerLine(Position = ComponentPosition.Top, Color = "#6366F1", Thickness = 2f, Style = ComponentDividerStyle.Gradient, GradientEndColor = "#A855F7")]
[ComponentDividerLine(Position = ComponentPosition.Bottom, Color = "#334155", Thickness = 1f, MarginTop = 8f)]
public class TelemetryLogger : MonoBehaviour
{
    [Header("Telemetry Configuration")]
    public string sessionID = "SESSION_8921";
    public bool logToFile = true;
    public float samplingIntervalSeconds = 0.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBorder]` / `[ComponentBackground]`** | High | Dividers sit outside the component card body, creating clean spacing between stacked cards. |
| **Multiple `[ComponentDividerLine]`** | High | Use one at `Top` and one at `Bottom` to cleanly sandwich important components. |
| **Field-Level Decorators** | High | Independent from internal field dividers like `[HorizontalLine]`. |
