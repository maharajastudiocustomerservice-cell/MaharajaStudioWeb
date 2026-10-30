# [ComponentFireworks]

> Renders periodic animated firework bursts with radiating colorful sparks and festive particle explosions across the component card.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentFireworks]` brings celebratory motion and particle flair to Unity components. It renders cyclic radial firework explosions across the inspector card body. Sparks explode outward from randomized origin coordinates, expanding up to a maximum blast radius (`BurstRadius`) before fading away and triggering the next sequence. Developers can tailor the tri-color palette (`Color1`, `Color2`, `Color3`), particle count (`Particles`), spark dot diameter (`Size`), burst cadence in seconds (`Speed`), transparency (`Opacity`), and layering (`Behind = true` $\to$ `ContentOverlay`, `Behind = false` $\to$ `BodyOverlay`).

**The Problem:**
Achievement managers, reward distribution systems, victory sequences, and seasonal festive events appear dry and bureaucratic in standard grayscale inspector views. Developers configuring joyful, milestone-driven features lack visual celebration.

**The Solution:**
Decorating festive systems with `[ComponentFireworks]`:
- **Periodic Radial Explosions:** Simulates expanding pyrotechnic bursts ($r = t \cdot \text{BurstRadius}$) that disperse particles evenly in 360-degree radial patterns.
- **Tri-Color Spark Distribution:** Alternates between gold, ember orange, and vivid pink (or customized festive hex colors) for multidimensional visual depth.
- **Configurable Cadence & Size:** Fine-tune interval frequency (`Speed`) and particle diameter (`Size`) from subtle celebratory sparkles to grand pyrotechnic displays.
- **Zero Click Interference:** Runs with `PickingMode.Ignore`, ensuring all reward thresholds and serialized values are effortlessly editable.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentFireworks(Color1 = "#FFD700", Color2 = "#FF1493", Color3 = "#00E5FF", Particles = 16, BurstRadius = 45f)]
public class AchievementRewardManager : MonoBehaviour
{
    public string achievementId = "ACH_MASTER_EXPLORER";
    public int bonusGemsAwarded = 500;
    public bool triggerConfettiOnUnlock = true;
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
public ComponentFireworksAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color1` | `string` | `"#FFD700"` | Hex color string for the primary burst spark color (gold). |
| `Color2` | `string` | `"#FF4500"` | Hex color string for secondary burst sparks (orange-red). |
| `Color3` | `string` | `"#FF69B4"` | Hex color string for tertiary burst sparks (hot pink). |
| `Particles` | `int` | `12` | Total number of particle sparks emitted per burst explosion. |
| `BurstRadius` | `float` | `40f` | Maximum outward radial expansion distance in pixels. |
| `Size` | `float` | `3f` | Diameter in pixels for each individual spark dot. |
| `Speed` | `float` | `3f` | Burst cycle duration (approximate interval between explosions in seconds). |
| `Opacity` | `float` | `0.6f` | Transparency alpha of the fireworks animation (0.0 to 1.0). |
| `Behind` | `bool` | `false` | When true, renders behind inspector controls; when false, renders on top. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#F59E0B", Width = 2f, Radius = 8f)]
[ComponentBackground("#1A1408", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("VICTORY EVENT DISPATCHER", Subtitle = "Season End Trophy & Celebration Handler", BackgroundColor = "#2A1E0B", TitleColor = "#FEF3C7")]
[ComponentFireworks(Color1 = "#FBBF24", Color2 = "#F87171", Color3 = "#60A5FA", Particles = 18, BurstRadius = 50f, Size = 3.5f, Speed = 2.5f, Opacity = 0.7f, Behind = true)]
public class VictoryEventDispatcher : MonoBehaviour
{
    [Header("Celebration Parameters")]
    public string tournamentSeasonName = "Championship Series 2026";
    public int topLeaderboardRankThreshold = 10;
    public float celebrationMusicFadeDuration = 3.5f;

    [Header("Payout Multipliers")]
    public float goldMultiplier = 2.5f;
    public bool grantExclusiveSkinBadge = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep dark backgrounds give expanding firework sparks theatrical pop and high contrast. |
| **`[ComponentHeader]`** | High | Fireworks burst gracefully across the body below golden celebratory headers. |
| **Inspector Controls** | High | UI Toolkit absolute positioning with `PickingMode.Ignore` guarantees completely transparent mouse events. |
