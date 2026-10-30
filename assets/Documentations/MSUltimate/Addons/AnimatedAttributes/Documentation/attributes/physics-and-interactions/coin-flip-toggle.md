# [CoinFlipToggle]

> Renders a boolean field as a flipping 3D coin with customizable heads/tails icons, physical spin animation, and collection cascading.

---

## 1. Overview & Value Proposition

**What it does:**
`[CoinFlipToggle]` replaces standard flat boolean checkboxes with an engaging 3D flipping coin token. When clicked, the coin flips along its horizontal axis with simulated rotational inertia over a configurable duration (`FlipDuration`), transitioning smoothly between its "heads" (true) state (`TrueColor`, `TrueIcon`) and "tails" (false) state (`FalseColor`, `FalseIcon`). It fully supports collection cascading via `ICollectionElementAttribute`.

**The Problem:**
Standard Unity boolean toggles are diminutive checkboxes that offer little visual flair or physical satisfaction. When toggling critical game state flags—such as PVP enabled, hardcore mode active, permadeath, or faction alignment—a plain checkbox lacks presence.

**The Solution:**
Decorating boolean fields with `[CoinFlipToggle]`:
- **Physical 3D Coin Rotation:** Simulates tactile rotational perspective and metallic shading during flips.
- **Custom Glyphs & Color Schemes:** Pick distinct icons (e.g., `★`, `✕`, `⚔`, `🛡`) and rich hex colors for both true and false faces.
- **Interactive or Read-Only:** Enable full interactive click flipping (`IsEditable = true`) or use as animated telemetry indicators.
- **Full Collection Cascading:** Implements `ICollectionElementAttribute` to effortlessly render lists and arrays of booleans as rows of flipping coins.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class GameSettings : MonoBehaviour
{
    [CoinFlipToggle(trueColor: "#F59E0B", falseColor: "#64748B", trueIcon: "★", falseIcon: "✕")]
    public bool isHardcoreModeActive = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `bool` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Collection Element Support** | Yes (`ICollectionElementAttribute`) |

---

## 4. Constructors & Parameters

```csharp
public CoinFlipToggleAttribute(string trueColor = "#F59E0B", string falseColor = "#64748B", string trueIcon = "★", string falseIcon = "✕")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `trueColor` | `string` | `"#F59E0B"` | Hex color string for the heads face (true state). |
| `falseColor` | `string` | `"#64748B"` | Hex color string for the tails face (false state). |
| `trueIcon` | `string` | `"★"` | Icon character or glyph displayed on the heads face. |
| `falseIcon` | `string` | `"✕"` | Icon character or glyph displayed on the tails face. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TrueColor` | `string` | `"#F59E0B"` | Hex color string for the true (heads) state. |
| `FalseColor` | `string` | `"#64748B"` | Hex color string for the false (tails) state. |
| `TrueIcon` | `string` | `"★"` | Display character on the true face. |
| `FalseIcon` | `string` | `"✕"` | Display character on the false face. |
| `FlipDuration` | `float` | `350f` | Duration of the 3D flip animation in milliseconds. |
| `IsEditable` | `bool` | `true` | Whether the coin can be interactively clicked to flip states. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class MatchmakingRules : MonoBehaviour
{
    [Header("Competitive Flags")]
    [CoinFlipToggle(
        trueColor: "#10B981", 
        falseColor: "#EF4444", 
        trueIcon: "✔", 
        falseIcon: "✖",
        FlipDuration = 400f
    )]
    public bool rankedQueueEnabled = true;

    [Header("Per-Team Readiness")]
    [CoinFlipToggle(trueColor: "#3B82F6", falseColor: "#475569", trueIcon: "⚔", falseIcon: "⚑")]
    public List<bool> teamReadyStates = new List<bool> { true, false, true, true };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Flips cleanly within compact box containers without boundary clipping. |
| Collections (`List<bool>`) | Supported | Implements `ICollectionElementAttribute` for multi-item list cascading. |
| `[ReadOnly]` | Supported | Displays coin state passively while disabling interactive flip clicks. |
