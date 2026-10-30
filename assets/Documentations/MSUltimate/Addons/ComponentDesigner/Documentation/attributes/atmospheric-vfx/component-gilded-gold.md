# [ComponentGildedGold]

> Wraps the component card in a luxury gilded metallic border with animated specular gleam sweeps and customizable alloy tones.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentGildedGold]` elevates component cards into prestigious museum-grade artifacts. Functioning as a `BodyWrapper` in `ComponentSlot.BodyWrapper`, it frames the inspector with an ornate precious metal border (`FrameWidth = 2f`, `Radius = 6f`) rendered across three refined alloy styles (`Tone = GoldTone.RoyalGold`, `RoseGold`, or `AntiqueBronze`). Periodically, an animated high-specularity gleam ray sweeps gracefully along the metallic rim (`GlintSpeed = 2.2f`, `GlintInterval = 3.5f`), catching the eye and establishing high item rarity.

**The Problem:**
Legendary weapons, divine relics, royal crown currencies, and prestige game passes look indistinguishable from standard common gray utility components in Unity's default inspector. Level designers and economy tuners lack visual feedback for items intended to feel truly mythical and valuable.

**The Solution:**
Decorating legendary and royal assets with `[ComponentGildedGold]`:
- **Precious Alloy Tones:** Choose between vibrant 24K Royal Gold, romantic copper-infused Rose Gold, or weathered Antique Bronze.
- **Specular Gleam Sweeps:** A high-speed light glint travels along the border perimeter at timed intervals to simulate light reflecting off polished bullion.
- **Precision Beveled Framing:** Integrates with rounded corner bounds (`Radius = 6f`) to create a bespoke jewelry bezel around the component.
- **Zero Input Interference:** Operates within `BodyWrapper` while delegating pointer events directly to child elements, maintaining smooth slider drags and field edits.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentGildedGold(tone: GoldTone.RoyalGold, frameWidth: 2.5f, glintInterval: 3f)]
public class ExcaliburHolyRelic : MonoBehaviour
{
    public string relicName = "Sword of Promised Victory";
    public int holyDamage = 9500;
    public float divineAuraRadius = 12f;
    public bool isAttunedToChampion = true;
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
public ComponentGildedGoldAttribute()
public ComponentGildedGoldAttribute(GoldTone tone = GoldTone.RoyalGold, float frameWidth = 2f, float glintInterval = 3.5f)
```

- `tone`: Metallic alloy preset (`GoldTone.RoyalGold`, `GoldTone.RoseGold`, or `GoldTone.AntiqueBronze`).
- `frameWidth`: Border line thickness in pixels.
- `glintInterval`: Time delay in seconds between specular gleam sweep flashes.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Tone` | `GoldTone` | `GoldTone.RoyalGold` | Precious metal alloy styling (`RoyalGold`, `RoseGold`, `AntiqueBronze`). |
| `FrameWidth` | `float` | `2f` | Thickness in pixels of the gilded outer border frame. |
| `Radius` | `float` | `6f` | Corner rounding radius in pixels for the gilded bezel. |
| `GlintSpeed` | `float` | `2.2f` | Travel speed multiplier of the specular glint flash across the perimeter. |
| `GlintInterval` | `float` | `3.5f` | Cooldown interval in seconds between periodic glint sweeps. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBackground("#1A1408", BorderRadius = 8f, Padding = 12f)]
[ComponentHeader("ARCHANGEL'S SANCTIFIED CHALICE", Subtitle = "Tier 7 Mythic Divine Regalia", BackgroundColor = "#2A1E0B", TitleColor = "#FEF08A")]
[ComponentGildedGold(Tone = GoldTone.RoyalGold, FrameWidth = 2.5f, Radius = 8f, GlintSpeed = 2.5f, GlintInterval = 4.0f)]
public class MythicRegaliaItemDefinition : MonoBehaviour
{
    [Header("Divine Economy & Power")]
    public int goldValue = 250000;
    public float graceBlessingMultiplier = 2.5f;

    [Header("Enchantment Slots")]
    public int maximumSocketCount = 5;
    public bool requiresSacredConsecration = true;

    [Header("Telemetry")]
    public string originalCreatorMonarch = "King Aurelius IV";
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep velvet black, royal purple, or obsidian cards make the golden foil gleam dramatically. |
| **`[ComponentHeader]`** | High | Crowns headers with matching gilded gold accents for royal palace inventories. |
| **`[ComponentBadge]`** | High | Pair with "MYTHIC" or "LEGENDARY" badges to immediately communicate item rarity. |
| **Inspector Controls** | High | Native wrapper layout leaves all serialized property fields completely interactable. |
