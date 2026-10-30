# [ComponentGradientOverlay]

> Renders a smooth two-stop gradient backdrop overlay across the component card with support for multi-directional angles and transparency.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentGradientOverlay]` washes the component inspector card in a customizable linear two-color gradient. Injected into `ComponentSlot.ContentOverlay`, it renders behind serialized fields without obstructing text clarity or control interactions. Developers can specify starting and ending hex colors (`StartColor`, `EndColor`), directional orientation (`Direction` $\to$ `Vertical`, `Horizontal`, `DiagonalTopLeft`, `DiagonalTopRight`), subtle overlay opacity (`Opacity`), and edge clipping radius (`BorderRadius`). Furthermore, `AllowMultiple = true` allows stacking multiple complementary gradient passes for advanced artistic blending.

**The Problem:**
Flat solid backgrounds can make complex inspector hierarchies feel flat, sterile, and uninspired. Developers wishing to visually distinguish distinct sub-systems often find solid colors too harsh or distracting behind serialized controls.

**The Solution:**
Decorating components with `[ComponentGradientOverlay]`:
- **Directional Gradients:** Choose between vertical top-to-bottom shading, horizontal flows, or angled diagonals for dynamic lighting feels.
- **Subtle Ambient Opacity:** Defaults to `0.15f` opacity, delivering sophisticated color tints that preserve high text contrast and readability.
- **Corner Radius Conformity:** Clips gradient corners via `BorderRadius` to match enclosing card borders seamlessly.
- **Multi-Stacking Support:** Stack secondary diagonal gradients over primary vertical washes to create rich multi-point ambient lighting.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentGradientOverlay("#4F46E5", "#06B6D4", Direction = GradientDirection.DiagonalTopLeft, Opacity = 0.2f)]
public class CyberpunkWeatherController : MonoBehaviour
{
    public float acidRainIntensity = 0.6f;
    public float neonFogDensity = 0.35f;
    public Color skyAmbientTint = Color.cyan;
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
| **Component Slot** | `ContentOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentGradientOverlayAttribute(string startColor, string endColor)
```

- `startColor`: Hex string for the gradient starting color (e.g. `"#3B82F6"`).
- `endColor`: Hex string for the gradient destination color (e.g. `"#10B981"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `StartColor` | `string` | *(Constructor)* | Hex color string for the gradient origin. |
| `EndColor` | `string` | *(Constructor)* | Hex color string for the gradient destination. |
| `Direction` | `GradientDirection` | `GradientDirection.Vertical` | Directional orientation (`Vertical`, `Horizontal`, `DiagonalTopLeft`, `DiagonalTopRight`). |
| `Opacity` | `float` | `0.15f` | Transparency alpha of the gradient overlay (0.0 to 1.0). |
| `BorderRadius` | `float` | `0f` | Corner rounding radius in pixels for clipping gradient edges. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#8B5CF6", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#0F0C20", BorderRadius = 8f, Padding = 10f)]
[ComponentGradientOverlay("#7C3AED", "#EC4899", Direction = GradientDirection.DiagonalTopLeft, Opacity = 0.18f, BorderRadius = 8f)]
[ComponentHeader("DIMENSIONAL RIFT ANCHOR", Subtitle = "Spacetime Distortion Field Generator", BackgroundColor = "#191438", TitleColor = "#F5F3FF")]
public class DimensionalRiftAnchor : MonoBehaviour
{
    [Header("Field Parameters")]
    public float spatialDistortionRadius = 45f;
    public float gravitationalPull = 9.81f;
    public bool stabilizeSingularityCore = true;

    [Header("Energy Feeds")]
    public float zeroPointEnergyInput = 750f;
    public int containmentFieldEmitters = 4;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Gradients overlay over solid background colors for nuanced lighting and chromatic depth. |
| **`[ComponentParticles]`** | High | Gradients set in `ContentOverlay` provide an atmospheric backdrop for floating particle effects. |
| **Inspector Controls** | High | Placed in `ContentOverlay` with `PickingMode.Ignore`, ensuring all standard Unity controls receive full pointer input. |
