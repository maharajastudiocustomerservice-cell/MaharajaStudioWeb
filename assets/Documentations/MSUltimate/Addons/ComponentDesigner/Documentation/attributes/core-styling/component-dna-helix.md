# [ComponentDNAHelix]

> Renders an animated rotating DNA double-helix along the top or bottom edge of the component card with two interleaving sinusoidal strands.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentDNAHelix]` brings biological and scientific motion into the component inspector. Operating as an overlay or background layer (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`), it renders an animated double-helix ribbon along either the top or bottom edge (`WaveEdge`). Two opposing sinusoidal particle strands (`Color1` and `Color2`, defaulting to cyan `#4FC3F7` and hot pink `#FF4081`) rotate continuously with customizable node count (`Nodes`), node diameter (`Size`), wave height (`Amplitude`), rotation velocity (`Speed`), and opacity.

**The Problem:**
Genetics engines, procedural mutation managers, biological crafting cauldrons, or bio-tech implants lack visceral scientific identity when viewed through plain inspector tables.

**The Solution:**
Decorating biological components with `[ComponentDNAHelix]`:
- **Interleaving Double Helix Motion:** Simulates genuine 3D double-strand rotation with phased sine waves ($y = \pm\sin(\text{time} \cdot \text{Speed} + i \cdot \text{phase}) \cdot \text{Amplitude}$).
- **Dual Strand Color Coding:** Independently style both nucleotide strands with distinct signature hues.
- **Top or Bottom Edge Anchoring:** Crown headers or ground footers via `WaveEdge.Top` or `WaveEdge.Bottom`.
- **Zero Input Blocking:** Set to `PickingMode.Ignore`, guaranteeing uninterrupted access to underlying fields.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentDNAHelix(Color1 = "#00E5FF", Color2 = "#FF1744", Amplitude = 14f, Speed = 1.2f)]
public class MutationGeneSequencer : MonoBehaviour
{
    public float mutationChancePercentage = 15.5f;
    public string primaryGeneMarker = "GENE_CRYO_RESIST";
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
public ComponentDNAHelixAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color1` | `string` | `"#4FC3F7"` | Hex color string for the first nucleotide strand. |
| `Color2` | `string` | `"#FF4081"` | Hex color string for the second nucleotide strand. |
| `Nodes` | `int` | `10` | Number of node markers rendered per strand. |
| `Size` | `float` | `4f` | Diameter in pixels for each individual strand node dot. |
| `Amplitude` | `float` | `12f` | Peak vertical amplitude displacement of the helix wave in pixels. |
| `Speed` | `float` | `1f` | Helix rotation speed multiplier. |
| `Opacity` | `float` | `0.5f` | Global transparency alpha of the helix container (0.0 to 1.0). |
| `Edge` | `WaveEdge` | `WaveEdge.Bottom` | Edge placement (`WaveEdge.Bottom` or `WaveEdge.Top`). |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#10B981", Width = 2f, Radius = 8f)]
[ComponentBackground("#0A1914", BorderRadius = 8f, Padding = 12f)]
[ComponentDNAHelix(Color1 = "#34D399", Color2 = "#A7F3D0", Nodes = 12, Amplitude = 10f, Speed = 1.5f, Opacity = 0.6f, Edge = WaveEdge.Bottom, Behind = true)]
public class BioSyntheticOrganism : MonoBehaviour
{
    [Header("Genetic Traits")]
    public string specimenSpecies = "Chimeric Flora IV";
    public float cellularRegenerationRate = 4.2f;
    public int chromosomePairs = 24;
    public bool isGeneticallyStable = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Dark backdrops allow the glowing double-helix strands to stand out with high contrast. |
| **`[ComponentBadge]`** | High | Floating corner tags (e.g. `"BIOLOGY"` or `"CRISPR"`) pair naturally with the helix animation. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures full mouse click-through to buttons and sliders. |
