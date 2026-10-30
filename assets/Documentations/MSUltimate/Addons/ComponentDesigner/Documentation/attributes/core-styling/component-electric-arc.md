# [ComponentElectricArc]

> Renders animated electric arcs and lightning bolt discharges along the top or bottom border of the component card with high-frequency flicker and glow.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentElectricArc]` injects procedural electrical lightning discharge animations directly onto component cards. Operating via UI Toolkit vector painters, it calculates multi-segment jagged electrical bolts anchored along a chosen edge (`Edge = WaveEdge.Bottom` or `WaveEdge.Top`). It features customizable discharge coloration (`Color`), segment density (`SegmentCount`), line weight (`Thickness`), jaggedness variance (`MaxDisplacement`), animation flicker frequency (`Speed`), soft outer bloom (`Glow`), and layer ordering (`Behind = false` $\to$ `BodyOverlay`, `Behind = true` $\to$ `ContentOverlay`).

**The Problem:**
High-voltage sci-fi machinery, lightning spells, energy shields, and plasma generators feel inert when configured in generic gray Unity inspector panels. Static text headers fail to communicate that a script governs hazardous high-voltage logic.

**The Solution:**
Decorating electrifying scripts with `[ComponentElectricArc]`:
- **Dynamic Jagged Bolt Generation:** Procedurally subdivides edge segments into erratic electrical pathways with randomized mid-point displacement ($y \pm \text{Random} \cdot \text{MaxDisplacement}$).
- **High-Frequency Discharge Flicker:** Animates spark re-routing and intensity oscillations at lightning speeds (`Speed = 3f` by default).
- **Subtle Ambient Glow:** Draws soft, double-width luminous outer halos around arcs when `Glow = true`.
- **Non-Intrusive Layout:** Positioned absolutely with `PickingMode.Ignore`, ensuring controls remain completely responsive.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentElectricArc(Color = "#00E5FF", SegmentCount = 10, MaxDisplacement = 14f, Speed = 4f, Glow = true)]
public class PlasmaConduitCore : MonoBehaviour
{
    public float voltageOutputKV = 240.5f;
    public float capacitorCharge = 98.2f;
    public bool isDischargeSafetyEngaged = false;
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
public ComponentElectricArcAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#88CCFF"` | Hex color string for electrical lightning discharges. |
| `SegmentCount` | `int` | `8` | Total number of jagged lightning segments rendered across the border. |
| `Thickness` | `float` | `2f` | Stroke width in pixels for arc discharge lines. |
| `MaxDisplacement` | `float` | `12f` | Peak vertical displacement away from the border edge in pixels. |
| `Speed` | `float` | `3f` | Flicker and spark mutation velocity multiplier. |
| `Opacity` | `float` | `0.7f` | Global transparency alpha of the electrical layer (0.0 to 1.0). |
| `Glow` | `bool` | `true` | When true, renders a wider soft luminous halo around lightning bolts. |
| `Edge` | `WaveEdge` | `WaveEdge.Bottom` | Edge placement (`WaveEdge.Bottom` or `WaveEdge.Top`). |
| `Behind` | `bool` | `false` | When true, renders behind inspector fields; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#3B82F6", Width = 2f, Radius = 6f)]
[ComponentBackground("#0A1128", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("TESLA COIL GENERATOR", Subtitle = "High-Voltage Overdrive Module", BackgroundColor = "#101D42", TitleColor = "#E0F2FE")]
[ComponentElectricArc(Color = "#67E8F9", SegmentCount = 12, Thickness = 2.5f, MaxDisplacement = 10f, Speed = 3.5f, Glow = true, Edge = WaveEdge.Bottom, Behind = true)]
public class TeslaCoilGenerator : MonoBehaviour
{
    [Header("Generator Specs")]
    public float resonantFrequencyKHz = 142.8f;
    public int sparkGapSpacingMm = 18;
    public float secondaryCoilTurns = 1200f;

    [Header("Safety Controls")]
    public bool autoGroundOnFault = true;
    public float thermalShutdownCelsius = 85f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep navy or charcoal backgrounds maximize the contrast and brilliance of blue-cyan electric arcs. |
| **`[ComponentHeader]`** | High | Anchoring the arc to `WaveEdge.Top` provides an electrified neon underline below header titles. |
| **Inspector Controls** | High | Transparent overlay does not intercept pointer hover, drag, or click events. |
