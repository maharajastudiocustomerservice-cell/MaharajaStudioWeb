# [ComponentScanline]

> Renders a continuous scrolling horizontal scanline across the component card, creating an authentic retro CRT monitor refresh sweep.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentScanline]` introduces subtle vintage display hardware aesthetics to component inspector windows. It simulates an authentic cathode-ray tube (CRT) monitor beam sweep by continuously scrolling a thin horizontal beam (`Height = 2f`) vertically from top to bottom across the card surface (`Speed = 3f` seconds per pass). Featuring customizable beam color (`Color`, defaulting to white `#FFFFFF`), delicate ambient opacity (`Opacity = 0.08f`), and layer ordering (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`), it imparts a retro terminal or radar scope feel without hindering text clarity.

**The Problem:**
Retro arcade games, terminal consoles, cyberdecks, flight instrumentation, and analog surveillance systems feel disjointed when presented in standard flat Unity inspector forms. Developers miss the nostalgic analog vibe of real hardware monitors.

**The Solution:**
Decorating retro systems with `[ComponentScanline]`:
- **Continuous CRT Vertical Sweep:** Sweeps a luminous horizontal electron beam continuously across the card.
- **Ultra-Subtle Default Opacity:** Defaults to `0.08f` opacity, ensuring all text labels and values remain crisp and readable.
- **Custom Hardware Colors:** Switch between classic monochrome white, amber phosphors (`#FFB000`), or terminal green (`#33FF33`).
- **Complete Input Transparency:** Runs with `PickingMode.Ignore`, guaranteeing that text inputs, toggles, and sliders operate without lag or obstruction.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentScanline(Color = "#33FF33", Height = 2.5f, Speed = 2.5f, Opacity = 0.12f)]
public class RetroArcadeCabinetLogic : MonoBehaviour
{
    public int hiScoreRecord = 99990;
    public int currentCreditCount = 3;
    public bool enableAttractMode = true;
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
public ComponentScanlineAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#FFFFFF"` | Hex color string for the scrolling CRT beam. |
| `Height` | `float` | `2f` | Vertical thickness in pixels of the scanline beam. |
| `Opacity` | `float` | `0.08f` | Transparency alpha of the scanline beam (0.0 to 1.0). |
| `Speed` | `float` | `3f` | Duration in seconds required for one full vertical screen pass. |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#22C55E", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#071A0E", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("TERMINAL MAINFRAME CONSOLE", Subtitle = "VT100 Emulation & Telemetry Log", BackgroundColor = "#0D2E1A", TitleColor = "#DCFCE7")]
[ComponentScanline(Color = "#4ADE80", Height = 3f, Speed = 3.2f, Opacity = 0.14f, Behind = true)]
public class TerminalMainframeConsole : MonoBehaviour
{
    [Header("Baud Rate & I/O")]
    public int baudRateBps = 9600;
    public int bufferLineCapacity = 256;
    public bool enableHardwareFlowControl = true;

    [Header("Telemetry Log")]
    public string activeSessionToken = "TTY_AUTH_OK_771";
    public float memoryUsageBytes = 65536f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Dark backdrops maximize the vintage CRT monitor feel. |
| **`[ComponentHeader]`** | High | Sweeps gracefully across the body below retro terminal title cards. |
| **Inspector Controls** | High | Zero mouse event interception ensures normal input interaction. |
