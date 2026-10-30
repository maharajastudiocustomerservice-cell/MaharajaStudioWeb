# [ComponentVaporwaveSun]

> Renders a synthwave aesthetic header banner with a segmented neon setting sun rising over an animated scrolling perspective grid.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentVaporwaveSun]` infuses the component inspector with an unmistakable 1980s retro-futuristic Outrun aesthetic. Injected into `ComponentSlot.BeforeContent`, it generates a stylized graphic banner (`Height = 70f`) featuring a glowing segmented horizon sun (`SunColor = "#FF007F"`) sinking into a neon perspective wireframe floor (`GridColor = "#7928CA"`). The perspective grid rolls continuously towards the viewer (`ScrollSpeed = 1.0f`), evoking high-speed cruising down an infinite digital highway.

**The Problem:**
Synthwave rhythm games, retro arcade racers, neon cyberpunk vehicles, and 80s cassette music tools lose their distinctive visual identity when displayed inside standard flat gray inspector cards. Developers miss the stylish neon swagger of their game's art direction during editor workflows.

**The Solution:**
Decorating synthwave, neon, and retro arcade components with `[ComponentVaporwaveSun]`:
- **Segmented Neon Sun:** Renders the classic horizontal-striped setting sun with vibrant magenta-to-gold gradient hues.
- **Scrolling Wireframe Grid:** True 3D perspective floor grid lines roll continuously towards the viewer to simulate infinite forward motion.
- **Dedicated Header Banner:** Embedded as a `BeforeContent` visual card directly above inspector fields, preserving clean organization below.
- **Vibrant Color Customization:** Freely tweak neon sun and grid wireframe hues to suit dark synth, outrun, or retro aesthetic palettes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentVaporwaveSun(sunColor: "#FF007F", gridColor: "#7928CA", scrollSpeed: 1.0f)]
public class OutrunTurboVehicleController : MonoBehaviour
{
    public float topSpeedMph = 185f;
    public float turboBoostMultiplier = 1.5f;
    public string activeRadioTrack = "Kavinsky - Nightcall";
    public bool isNitrousPurgeReady = true;
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
| **Component Slot** | `BeforeContent` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentVaporwaveSunAttribute()
public ComponentVaporwaveSunAttribute(string sunColor = "#FF007F", string gridColor = "#7928CA", float scrollSpeed = 1.0f)
```

- `sunColor`: Hex color string representing the segmented setting sun glow.
- `gridColor`: Hex color string representing the perspective wireframe floor grid.
- `scrollSpeed`: Animation velocity multiplier governing the forward-scrolling floor grid.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `SunColor` | `string` | `"#FF007F"` | Hex color string for the glowing segmented neon sun. |
| `GridColor` | `string` | `"#7928CA"` | Hex color string for the perspective wireframe grid lines. |
| `ScrollSpeed` | `float` | `1.0f` | Rate multiplier governing the animated forward grid motion. |
| `Height` | `float` | `70f` | Total pixel height of the synthwave header banner element. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#C026D3", Width = 2f, Radius = 8f)]
[ComponentBackground("#180B2B", BorderRadius = 8f, Padding = 12f)]
[ComponentVaporwaveSun(SunColor = "#FF007F", GridColor = "#9333EA", ScrollSpeed = 1.25f, Height = 80f)]
public class SynthwaveArcadeGameDirector : MonoBehaviour
{
    [Header("Retro Gameplay")]
    public int currentHighScore = 198400;
    public float roadCurvature = 0.35f;
    public int palmTreeDensity = 24;

    [Header("Synthesizer Audio")]
    public float basslineSidechainCompression = 0.82f;
    public bool isArpeggiatorSynchronized = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep midnight purple or obsidian backgrounds (`#180B2B`) frame the neon sun perfectly. |
| **`[ComponentBorder]`** | High | Pair with neon magenta or electric violet borders for a complete retro arcade cabinet finish. |
| **`[ComponentSound]`** | High | Add retro 8-bit or synth chord audio triggers on inspector interaction. |
| **Inspector Controls** | High | Cleanly sits in `BeforeContent`, keeping all serialized properties undisturbed underneath. |
