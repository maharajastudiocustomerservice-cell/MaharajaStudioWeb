# [ComponentMatrixRain]

> Renders a classic cyberpunk digital rain effect with falling character streams cascading in vertical trails across the component background.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentMatrixRain]` transforms the component inspector into a cyberpunk terminal. Operating via UI Toolkit vector and text rendering, it generates vertical columns of descending digital characters (`Columns`, `TrailLength`). Characters descend steadily (`Speed`) with luminance falloff towards the tail end of each trail before recycling at the top. It features iconic phosphor green by default (`Color = "#00FF41"`), selectable font scale (`FontSize`), custom glyph character dictionaries (`Characters = "01アイウエオカキクケコ"`), fine-tuned ambient transparency (`Opacity = 0.3f`), and default background layer positioning (`Behind = true` $\to$ `ComponentSlot.ContentOverlay`).

**The Problem:**
Hacking mechanics, terminal shells, cryptographic decipherers, and cyberspace network protocols look identical to regular combat or inventory scripts in standard Unity editors. Without unmistakable visual identity, developers miss the hacker/data fantasy during configuration.

**The Solution:**
Decorating cybersecurity and terminal components with `[ComponentMatrixRain]`:
- **Iconic Digital Stream Cascade:** Animates asynchronous vertical cascades of descending code symbols.
- **Custom Character Glyphs:** Supply any custom alphabet or hexadecimal strings (`Characters = "0123456789ABCDEF"` or Japanese Katakana).
- **Luminance Trail Falloff:** Automatically illuminates leading glyphs with bright highlights while softly fading trailing characters.
- **Background Default Layering:** Defaults to `Behind = true` with `PickingMode.Ignore`, guaranteeing that text inputs, toggles, and dropdowns remain 100% readable and accessible.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentMatrixRain(Color = "#00FF66", Columns = 14, Speed = 1.2f, Opacity = 0.35f)]
public class CyberdeckTerminalHacker : MonoBehaviour
{
    public string targetNodeIp = "192.168.42.105";
    public int bypassCyclesRemaining = 3;
    public float iceBreakerPenetration = 0.85f;
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
public ComponentMatrixRainAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#00FF41"` | Hex color string for falling characters (classic phosphor green). |
| `Columns` | `int` | `12` | Total number of vertical falling character columns. |
| `TrailLength` | `int` | `6` | Number of glyphs rendered per falling column stream. |
| `Speed` | `float` | `1f` | Fall rate velocity multiplier. |
| `FontSize` | `int` | `10` | Font size in points for digital glyph characters. |
| `Opacity` | `float` | `0.3f` | Global transparency alpha of the falling rain layer (0.0 to 1.0). |
| `Characters` | `string` | `"01アイウエオカキクケコ"` | Glyph pool string sampled randomly by descending columns. |
| `Behind` | `bool` | `true` | When true (default), renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#10B981", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#05160E", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("CYBERNETIC FIREWALL INTRUDER", Subtitle = "Neural Interface Subversion Node", BackgroundColor = "#0A281A", TitleColor = "#D1FAE5")]
[ComponentMatrixRain(Color = "#34D399", Columns = 16, TrailLength = 8, Speed = 1.4f, Opacity = 0.28f, Characters = "01010110ABCDEF", Behind = true)]
public class CyberneticFirewallIntruder : MonoBehaviour
{
    [Header("Network Intrusion")]
    public string targetSubnetGateway = "10.0.88.1";
    public float memoryBufferOverflowPercent = 74.2f;
    public bool isTraceEvaded = true;

    [Header("Exploit Modules")]
    public int activeZeroDayPayloads = 2;
    public float decryptionBandwidthMbps = 1200f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Midnight black or dark emerald backgrounds maximize the luminosity of descending characters. |
| **`[ComponentHeader]`** | High | Anchoring the rain behind inspector controls below a cyberpunk title creates a cohesive terminal theme. |
| **Inspector Controls** | High | `Behind = true` combined with `PickingMode.Ignore` ensures complete click-through transparency for all inspector fields. |
