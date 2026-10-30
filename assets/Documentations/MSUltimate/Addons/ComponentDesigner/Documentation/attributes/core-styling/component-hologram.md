# [ComponentHologram]

> Applies an animated sci-fi holographic overlay across the component card with scrolling scanlines, subtle CRT flickers, and chromatic tinting.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentHologram]` envelops the component card in a futuristic holographic projector aesthetic. Operating via UI Toolkit custom vector rendering, it draws a lattice of horizontal scanlines (`Scanlines`) that scroll steadily across the card surface (`Speed`). It applies dynamic illumination flickering (`FlickerIntensity`), customizable holographic tinting (`Color`, defaulting to neon cyan `#00FFCC`), controllable transparency (`Opacity`), and front/back layer routing (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`).

**The Problem:**
Cyberpunk consoles, holographic UI projectors, AI interfaces, and telecommunications transmitters look mundane when edited in standard static Unity inspector panels, failing to reflect their high-tech, futuristic in-game presentation.

**The Solution:**
Decorating sci-fi modules with `[ComponentHologram]`:
- **Scrolling CRT Scanlines:** Simulates raster scan displays by shifting illuminated horizontal bands across the vertical coordinate axis over time.
- **Micro-Voltage Flicker:** Uses subtle noise-driven opacity oscillations to create realistic projector instability without jarring the user's eyes.
- **Custom Futuristic Tints:** Tailor hues between neon cyan, tactical amber, matrix green, or synthwave violet.
- **Full Click-Through Ergonomics:** Absolutely positioned with `PickingMode.Ignore`, ensuring all inspector input fields, toggles, and buttons operate unimpeded.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentHologram(Color = "#00E5FF", Scanlines = 8, Speed = 2f, FlickerIntensity = 0.2f, Opacity = 0.25f)]
public class HolographicHUDProjector : MonoBehaviour
{
    public float projectionDistanceMeters = 2.5f;
    public float opticalResolutionDpi = 300f;
    public bool isInterferenceFilteringEnabled = true;
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
public ComponentHologramAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#00FFCC"` | Hex color string for holographic tinting and scanlines. |
| `Scanlines` | `int` | `6` | Total count of scrolling horizontal scanline bands visible on the card. |
| `Speed` | `float` | `1.5f` | Scanline vertical scrolling velocity multiplier. |
| `FlickerIntensity` | `float` | `0.15f` | Magnitude of rapid CRT brightness/opacity flicker (0.0 to 1.0). |
| `Opacity` | `float` | `0.2f` | Global transparency alpha of the holographic effect (0.0 to 1.0). |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#06B6D4", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#081D24", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("TACTICAL HOLO-MAP TRANSMITTER", Subtitle = "Orbital Uplink & Beacon Synchronizer", BackgroundColor = "#0C2E38", TitleColor = "#CFFAFE")]
[ComponentHologram(Color = "#22D3EE", Scanlines = 10, Speed = 1.8f, FlickerIntensity = 0.12f, Opacity = 0.22f, Behind = true)]
public class TacticalHoloMapTransmitter : MonoBehaviour
{
    [Header("Transmitter Frequency")]
    public float uplinkFrequencyGHz = 14.25f;
    public int connectedSquadNodes = 6;
    public float beaconRefreshIntervalSeconds = 0.5f;

    [Header("Optics Calibration")]
    public float distortionCorrectionFactor = 0.98f;
    public bool enableVolumetricDepthOcclusion = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Dark teal or charcoal backdrops accentuate neon cyan hologram scanlines. |
| **`[ComponentHeader]`** | High | Creates a cohesive sci-fi terminal appearance when combined with tech headers. |
| **Inspector Controls** | High | Zero mouse interception ensures smooth workflow when modifying serialized variables. |
