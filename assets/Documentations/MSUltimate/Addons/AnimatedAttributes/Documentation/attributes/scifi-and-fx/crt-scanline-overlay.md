# [CRTScanlineOverlay]

> Overlays retro CRT monitor raster scanlines rolling vertically across the inspector field to evoke vintage arcade and terminal aesthetics.

---

## 1. Overview & Value Proposition

**What it does:**
`[CRTScanlineOverlay]` applies an authentic retro cathode-ray tube (CRT) monitor effect directly across inspector properties. Using UI Toolkit's 2D vector painter (`MeshGenerationContext.painter2D`), it draws horizontal raster scanlines with customizable spacing (`LineSpacing`, defaulting to 4px) and opacity (`ScanlineAlpha`, defaulting to 0.2). The scanlines roll continuously downward at a designated velocity (`ScrollSpeed` in px/sec), creating a convincing vintage display aesthetic without obstructing input readability.

**The Problem:**
Retro arcade games, cyberpunk terminals, fallout-style wasteland computers, or analog security monitors often feature rich in-game CRT shaders. However, inside the Unity Editor, data configurations for these systems look modern and generic, breaking the retro immersion during development and tuning.

**The Solution:**
Decorating vintage or terminal parameters with `[CRTScanlineOverlay]`:
- **Rolling Raster Lines:** Continuously scrolls horizontal scanlines downward at a configurable velocity (`ScrollSpeed`), simulating 60Hz cathode ray scanning.
- **Subtle, Non-Intrusive Alpha:** Fine-tune scanline transparency (`ScanlineAlpha`) and spacing (`LineSpacing`) so text and numbers remain fully legible.
- **Hardware-Accelerated Vector Strokes:** Renders via lightweight `painter2D.LineTo` paths with zero texture asset dependencies.
- **Non-Blocking Pointer Input:** Configured with `PickingMode.Ignore`, allowing clicks, drags, and text editing to pass straight through to the underlying field.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ArcadeTerminal : MonoBehaviour
{
    [CRTScanlineOverlay(scrollSpeed: 30f, lineSpacing: 4f)]
    public string terminalBootSequence = "INIT_SYSTEM_V_1984";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public CRTScanlineOverlayAttribute(float scrollSpeed = 25f, float lineSpacing = 4f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `scrollSpeed` | `float` | `25f` | Vertical rolling speed of scanlines in pixels per second. |
| `lineSpacing` | `float` | `4f` | Vertical distance between adjacent scanline stripes in pixels. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ScrollSpeed` | `float` | `25f` | Vertical downward roll velocity in pixels per second. |
| `LineSpacing` | `float` | `4f` | Spacing distance in pixels between scanline raster lines. |
| `ScanlineAlpha` | `float` | `0.2f` | Opacity alpha (from `0f` to `1f`) of the raster lines. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class RetroHackingTerminal : MonoBehaviour
{
    [Header("Mainframe Cipher")]
    [CRTScanlineOverlay(
        scrollSpeed: 35f, 
        lineSpacing: 5f, 
        ScanlineAlpha = 0.28f
    )]
    public string encryptionKey = "HEX_4F_A2_90_FF";

    [Header("Terminal Baud Rate")]
    [CRTScanlineOverlay(scrollSpeed: 20f, lineSpacing: 3f)]
    public int modemBaudRate = 9600;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Scanline overlay clips neatly within group boundaries. |
| `[HologramFlicker]` | Stacking | Combines CRT scanlines with holographic opacity flicker for vintage monitors. |
| `[PasswordMask]` | Supported | Pairs with password masks to create classified terminal login inputs. |
