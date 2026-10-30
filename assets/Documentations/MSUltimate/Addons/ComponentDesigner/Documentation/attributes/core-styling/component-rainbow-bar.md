# [ComponentRainbowBar]

> Renders an animated horizontal accent bar along the top or bottom border with a smoothly shifting full-spectrum rainbow gradient.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentRainbowBar]` adds a dynamic full-spectrum rainbow accent line along the boundary of the component card. Anchored to either the bottom or top border (`Edge = WaveEdge.Bottom` or `WaveEdge.Top`), it renders a continuous horizontal color bar (`Height = 3f`) whose colors cycle smoothly through the complete HSL chromatic wheel. Developers can customize the bar thickness (`Height`), color vibrancy (`Saturation`), cycle velocity (`Speed`), transparency (`Opacity`), and layering (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`).

**The Problem:**
Special milestone scripts, cosmetic skin handlers, prismatic energy shields, and celebratory seasonal event controllers look indistinguishable from ordinary logic in standard grayscale Unity inspector panels.

**The Solution:**
Decorating colorful systems with `[ComponentRainbowBar]`:
- **Shifting Full-Spectrum Gradient:** Animates a continuous moving rainbow spectrum across the card width.
- **Vibrant Color Saturation:** Fine-tune color intensity (`Saturation = 0.9f`) from pastel rainbow hues to vibrant neon prism strips.
- **Edge Anchoring:** Mounts along `WaveEdge.Top` to underline headers or `WaveEdge.Bottom` to crown footers.
- **Zero Click Interference:** Uses `PickingMode.Ignore`, ensuring all standard Unity input controls remain completely responsive.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentRainbowBar(Height = 4f, Speed = 1.5f, Edge = WaveEdge.Bottom, Saturation = 1.0f)]
public class PrismaticRainbowUnicornCosmetic : MonoBehaviour
{
    public string cosmeticSkinId = "SKIN_PRISMATIC_MYTHIC";
    public Color trailColorStart = Color.magenta;
    public Color trailColorEnd = Color.cyan;
    public bool emitGlitterParticles = true;
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
| **Component Slot** | `ContentOverlay` (if `Behind = true`) or `BodyOverlay` (if `Behind = false`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentRainbowBarAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Height` | `float` | `3f` | Vertical thickness of the rainbow bar in pixels. |
| `Edge` | `WaveEdge` | `WaveEdge.Bottom` | Edge placement (`WaveEdge.Bottom` or `WaveEdge.Top`). |
| `Speed` | `float` | `1f` | Gradient color shift cycle velocity multiplier. |
| `Opacity` | `float` | `0.7f` | Transparency alpha of the rainbow bar (0.0 to 1.0). |
| `Saturation` | `float` | `0.9f` | HSL saturation intensity of rainbow colors (0.0 to 1.0). |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#8B5CF6", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#110E1F", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("PRISMATIC SPECTRUM EMITTER", Subtitle = "Chromatographic Laser Dispersion Node", BackgroundColor = "#1C1733", TitleColor = "#EDE9FE")]
[ComponentRainbowBar(Height = 3.5f, Speed = 1.2f, Edge = WaveEdge.Bottom, Saturation = 0.95f, Opacity = 0.8f)]
public class PrismaticSpectrumEmitter : MonoBehaviour
{
    [Header("Optical Dispersion")]
    public float refractionIndex = 1.52f;
    public float wavelengthBandwidthNm = 380f;
    public bool enableTotalInternalReflection = true;

    [Header("Prism Modulation")]
    public float rotationMotorRpm = 45f;
    public int focalLengthMm = 85;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Placing at `WaveEdge.Top` provides an animated rainbow underline below header banners. |
| **`[ComponentBackground]`** | High | Dark backdrops allow rich rainbow hues to pop with high contrast. |
| **Inspector Controls** | High | Positioned with `PickingMode.Ignore`, ensuring all standard Unity input controls remain completely responsive. |
