# [ComponentTheme]

> Applies a comprehensive, cohesive design theme preset across the component inspector in a single attribute declaration.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentTheme]` is the master aesthetic styling shortcut for MSUltimate-ComponentDesigner. Injected into `ComponentSlot.BodyWrapper`, it transforms the entire inspector presentation using ten professionally curated visual themes (`Theme = Cyberpunk`, `DarkSciFi`, `RPGParchedScroll`, `Synthwave80s`, `CleanMinimal`, `RetroArcade`, `NordicDark`, `Glassmorphism`, `MidnightGold`, or `CrimsonNeon`). Developers can customize the themed header title (`Title`), descriptive subtitle (`Subtitle`), icon glyph (`Icon`), and corner radius (`Radius`), harmonizing colors, borders, and typography instantly.

**The Problem:**
Individually configuring borders, backgrounds, headers, and color palettes across dozens of script files requires repetitive attribute stacks (`[ComponentBorder]`, `[ComponentBackground]`, `[ComponentHeader]`). Teams want a unified, consistent art direction for all components without duplicating long attribute declarations.

**The Solution:**
Standardizing component styling with `[ComponentTheme]`:
- **Ten Curated Design Systems:** Instantly toggle between Sci-Fi, RPG, Cyberpunk, Synthwave, Minimalist, or Glassmorphic styles.
- **Single-Line Implementation:** Replaces 4–5 individual styling attributes with a single, expressive declaration.
- **Integrated Header System:** Embeds titles, subtitles, and category icons configured specifically for the active theme preset.
- **Unified Team Ergonomics:** Establishes visual consistency across entire engineering teams with effortless maintenance.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentTheme(ComponentThemePreset.Cyberpunk, "CYBER DECK OVERDRIVE", "Neural Interface Bus", "⚡")]
public class CyberDeckNeuralBus : MonoBehaviour
{
    public float synopticBandwidthGhz = 128.5f;
    public float neuralFeedbackDamping = 0.85f;
    public bool isCortexLinkSecured = true;
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
public ComponentThemeAttribute(ComponentThemePreset theme)
public ComponentThemeAttribute(ComponentThemePreset theme, string title, string subtitle = "", string icon = "")
```

- `theme`: Pre-packaged aesthetic preset (`Cyberpunk`, `DarkSciFi`, `RPGParchedScroll`, `Synthwave80s`, `CleanMinimal`, `RetroArcade`, `NordicDark`, `Glassmorphism`, `MidnightGold`, `CrimsonNeon`).
- `title`: Primary component header title override.
- `subtitle`: Explanatory subtitle text displayed underneath the title.
- `icon`: Unicode glyph or emoji representing the component category.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Theme` | `ComponentThemePreset` | `Cyberpunk` | Complete visual theme preset applied across the component inspector. |
| `Title` | `string` | `""` | Themed header title text override. If empty, uses class name. |
| `Subtitle` | `string` | `""` | Themed header subtitle text describing subsystem purpose. |
| `Icon` | `string` | `""` | Leading icon glyph or emoji displayed in the themed header. |
| `Radius` | `float` | `-1f` | Corner rounding radius override in pixels (`-1` uses theme preset default). |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentTheme(
    ComponentThemePreset.MidnightGold, 
    Title = "ROYAL TREASURY VAULT", 
    Subtitle = "Kingdom Sovereign Asset Reserve", 
    Icon = "👑", 
    Radius = 8f)]
public class RoyalTreasuryVaultManager : MonoBehaviour
{
    [Header("Vault Reserves")]
    public int totalGoldBullionBars = 15000;
    public float royalInterestYieldPerMonth = 0.045f;
    public int sovereignDiamondCount = 350;

    [Header("Security Guards")]
    public int eliteImperialGuardsStationed = 24;
    public bool isMagicalVaultWardIntact = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeaderButton]`** | High | Buttons integrate cleanly into themed header bars across all presets. |
| **`[ComponentPresetManager]`** | High | Adds preset snapshot capabilities directly beneath the themed header. |
| **`[ComponentLock]`** | High | Protects themed component variables from accidental edits with a single lock switch. |
| **Inspector Controls** | High | Wraps the entire visual presentation in `BodyWrapper` without modifying field draw logic. |
