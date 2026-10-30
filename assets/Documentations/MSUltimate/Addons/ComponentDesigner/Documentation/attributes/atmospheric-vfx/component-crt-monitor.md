# [ComponentCRTMonitor]

> Wraps the component inspector in a retro cathode-ray tube (CRT) display with rolling scanlines, phosphor glow, and barrel curvature.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentCRTMonitor]` transforms the component inspector into an authentic vintage computing terminal. Injected into `ComponentSlot.BodyWrapper`, it wraps the entire component card in a curved monitor enclosure featuring rolling horizontal raster scanlines (`ScanlineOpacity = 0.25f`, `ScanSpeed = 1.0f`), an evocative monochrome or amber phosphor tint (`PhosphorTint = "#33FF77"`), and a subtle optical vignette curvature distortion (`Curvature = 0.05f`).

**The Problem:**
Cyberpunk decker terminals, Cold War radar computers, retro terminal emulators, and military diagnostic systems lose their tactile charm when rendered on clean modern flat gray panels. Artists and scripters miss the nostalgic tactile grit of glowing cathode phosphor and rolling electron beams.

**The Solution:**
Decorating terminal and diagnostic components with `[ComponentCRTMonitor]`:
- **Animated Raster Scanlines:** Continuous rolling horizontal beam sweep simulates vintage 50Hz/60Hz cathode television screens.
- **Phosphor Electron Bloom:** Imbues text labels and value fields with an authentic nostalgic green (P1 phosphor), amber (P3 phosphor), or icy blue hue.
- **Convex Barrel Curvature:** Simulates the curved glass tube faceplate with subtle corner shading and edge darkening.
- **Native Wrapper Architecture:** Operates as a `BodyWrapper` that encases all inspector controls within a cohesive retro television frame while preserving total input reactivity.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentCRTMonitor(phosphorTint: "#33FF77", curvature: 0.05f, scanlineOpacity: 0.25f)]
public class CyberTerminalMainframe : MonoBehaviour
{
    public string terminalNodeId = "NORAD-DEFCON-01";
    public int baudRate = 9600;
    public bool isModemCarrierDetected = true;
    public float memoryBufferParity = 0.98f;
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
| **Component Slot** | `BodyWrapper` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentCRTMonitorAttribute()
public ComponentCRTMonitorAttribute(string phosphorTint = "#33FF77", float curvature = 0.05f, float scanlineOpacity = 0.25f)
```

- `phosphorTint`: Hex color string representing the CRT phosphor emission (e.g., `#33FF77` for P1 Green, `#F59E0B` for P3 Amber).
- `curvature`: Strength multiplier for the barrel screen edge curvature and vignette corner darkening.
- `scanlineOpacity`: Alpha intensity of the rolling horizontal electron raster scanlines.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PhosphorTint` | `string` | `"#33FF77"` | Hex color string for the CRT phosphor tinting and ambient bloom. |
| `Curvature` | `float` | `0.05f` | Strength of the spherical glass tube curvature and corner vignette shading. |
| `ScanSpeed` | `float` | `1.0f` | Rate multiplier governing the downward rolling raster line animation. |
| `ScanlineOpacity` | `float` | `0.25f` | Visibility opacity of the animated horizontal cathode scanlines. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#15803D", Width = 2f, Radius = 8f)]
[ComponentBackground("#05160A", BorderRadius = 8f, Padding = 12f)]
[ComponentHeader("MAINFRAME RADAR TELEMETRY", Subtitle = "Tactical Cold War Air-Defense Matrix", BackgroundColor = "#082512", TitleColor = "#86EFAC")]
[ComponentCRTMonitor(PhosphorTint = "#22C55E", Curvature = 0.06f, ScanSpeed = 1.2f, ScanlineOpacity = 0.3f)]
public class RadarInterceptionTerminal : MonoBehaviour
{
    [Header("Antenna & Frequency")]
    public float sweepFrequencyGhz = 2.45f;
    public float antennaAzimuthDegrees = 142.5f;
    public int detectedBogeys = 3;

    [Header("Cathode Screen Calibration")]
    [Range(0f, 100f)]
    public float beamIntensityLux = 85f;
    public bool isPhosphorPersistenceHigh = true;
    public string activeSectorGrid = "SECTOR-BRAVO-NINER";
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep obsidian or dark forest green backgrounds (`#05160A`) heighten the luminous CRT phosphor contrast. |
| **`[ComponentHeader]`** | High | Header titles appear as if displayed inside the monitor glass when placed within the component. |
| **Monochrome Fields** | High | Pair with green or amber field label styling to complete the 1980s terminal experience. |
| **Inspector Controls** | High | Sliders, object selectors, and string fields remain fully responsive beneath the scanline overlay. |
