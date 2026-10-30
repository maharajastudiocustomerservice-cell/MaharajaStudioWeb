# [ComponentCompactMode]

> Condenses the component inspector layout with reduced margins, padding, and row heights to maximize visible information density.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentCompactMode]` optimizes component layouts for high-density editing. Injected into `ComponentSlot.BodyWrapper`, it tightens vertical field margins, compresses row spacing (`CompactRowHeight = 18f`), and subtly scales font size (`FontScale = 0.9f`). It optionally equips the component header with a toggle switch (`ShowHeaderToggle = true`) allowing developers to dynamically alternate between expansive standard spacing and condensed compact density on the fly.

**The Problem:**
Extensive game managers, RPG database tables, state machines, and weapon asset definitions contain dozens of serialized fields. Default Unity inspector padding forces massive vertical scrolling, making it tedious to compare values across different sections of the same component.

**The Solution:**
Applying `[ComponentCompactMode]` to data-rich components:
- **High Information Density:** Reduces vertical height per property by up to 35%, fitting more fields into view simultaneously.
- **Interactive Header Mode Switch:** Let developers toggle between compact density and standard comfortable spacing with a single click.
- **Subtle Font Scaling:** Proportionally shrinks labels and values (`FontScale = 0.9f`) to prevent text clipping while preserving readability.
- **Zero Loss of Control Functionality:** Every field, slider, object picker, and foldout remains completely functional with pixel-precise touch targets.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentCompactMode(defaultCompact: true, showHeaderToggle: true)]
public class CombatStatisticsTable : MonoBehaviour
{
    public float basePhysicalDamage = 55f;
    public float baseMagicalDamage = 32f;
    public float criticalStrikeChance = 0.15f;
    public float criticalDamageMultiplier = 2.0f;
    public float armorPenetrationFlat = 10f;
    public float lifeStealPercentage = 0.05f;
    public float attackSpeedRating = 1.25f;
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
public ComponentCompactModeAttribute()
public ComponentCompactModeAttribute(bool defaultCompact, bool showHeaderToggle = true)
```

- `defaultCompact`: Whether compact mode is active upon inspector load (`true` by default).
- `showHeaderToggle`: Whether to display an interactive compact toggle switch in the component header.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DefaultCompact` | `bool` | `true` | When true, initial inspector layout starts in condensed compact mode. |
| `ShowHeaderToggle` | `bool` | `true` | When true, renders an interactive compact switch in the component header. |
| `CompactRowHeight` | `float` | `18f` | Height in pixels allocated to each serialized property row in compact mode. |
| `FontScale` | `float` | `0.9f` | Scale multiplier applied to label and value typography in compact mode. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#3B82F6", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#0B132B", BorderRadius = 6f, Padding = 8f)]
[ComponentHeader("RPG CHARACTER ATTRIBUTE MATRIX", Subtitle = "Master Stat Sheet & Combat Derivatives", BackgroundColor = "#121F42", TitleColor = "#BFDBFE")]
[ComponentCompactMode(DefaultCompact = true, ShowHeaderToggle = true, CompactRowHeight = 18f, FontScale = 0.88f)]
public class RPGCharacterAttributeMatrix : MonoBehaviour
{
    [Header("Core Attributes")]
    public int strength = 24;
    public int agility = 18;
    public int intelligence = 14;
    public int vitality = 30;

    [Header("Defenses & Resistances")]
    public float physicalArmor = 150f;
    public float fireResistancePercent = 25f;
    public float frostResistancePercent = 10f;
    public float lightningResistancePercent = 15f;
    public float poisonResistancePercent = 40f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Places the compact toggle switch neatly inside the header navigation bar. |
| **`[ComponentBackground]`** | High | Adjusts container padding seamlessly to match condensed inner child margins. |
| **Tabbed Layouts** | High | Works alongside tab groups and accordion foldouts to maximize screen efficiency. |
| **Inspector Controls** | High | Modifies UI Toolkit USS style rules directly without disrupting property draw cycles. |
