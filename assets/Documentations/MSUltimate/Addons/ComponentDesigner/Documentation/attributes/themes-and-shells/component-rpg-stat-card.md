# [ComponentRPGStatCard]

> Renders an RPG trading card header banner with rarity border glows, power level badges, class emblems, and rarity color palettes.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentRPGStatCard]` displays a collectible RPG character or item hero card above component fields. Operating in `ComponentSlot.BeforeContent`, it formats a card banner featuring an entity name (`Title`), level or power rating badge (`Level = 1`), subclass designation (`Subtitle = "Warrior"`), and class icon glyph (`ClassIcon = "🛡️"`). The banner dynamically illuminates across six item rarity tiers (`Rarity = Common`, `Uncommon`, `Rare`, `Epic`, `Legendary`, or `Mythic`), or allows custom tint overrides (`AccentColor`).

**The Problem:**
RPG character sheets, dungeon raid bosses, gacha heroes, and collectible card attributes blend into mundane property lists in Unity's standard editor. Designers tuning boss stats or hero archetypes lack immediate visual recognition of an entity's power bracket and archetype identity.

**The Solution:**
Decorating hero and equipment data with `[ComponentRPGStatCard]`:
- **Integrated Rarity Aesthetics:** Instantly sets border glows, level badge badges, and background highlights to match industry-standard rarity colors (from Common Gray to Mythic Magenta).
- **Hero Identity Block:** Displays character name, level badge, class title, and iconic role symbol in a compact header.
- **Custom Accent Override:** Allows developers to specify bespoke hex accents (`AccentColor`) when deviating from standard rarity palettes.
- **Clean Separation:** Operates in `BeforeContent`, keeping header art separate from the gameplay variables below.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentRPGStatCard("Grommash Ironbreaker", level: 60, subtitle: "Berserker Warlord", rarity: RPGCardRarity.Mythic, classIcon: "🪓")]
public class RaidBossEntity : MonoBehaviour
{
    public float maximumHitPoints = 125000f;
    public float ragePerSecond = 8.5f;
    public float cleaveDamageMultiplier = 2.4f;
    public bool isEnragePhaseActive = false;
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
public ComponentRPGStatCardAttribute(string title, int level = 1, string subtitle = "Warrior", RPGCardRarity rarity = RPGCardRarity.Legendary, string classIcon = "🛡️")
```

- `title`: Primary character, boss, or collectible hero card name.
- `level`: Level number or power rating score stamped into the card badge.
- `subtitle`: Subclass, role, or archetype string (e.g., `"Mage"`, `"Paladin"`, `"Rogue"`).
- `rarity`: Card tier governing visual glow and badge colors (`Common` through `Mythic`).
- `classIcon`: Unicode glyph or emoji representing class archetype.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | `"Character Card"` | Character, boss, or hero card title displayed prominently. |
| `Level` | `int` | `1` | Numeric level score displayed in the badge pill. |
| `Subtitle` | `string` | `"Warrior"` | Class archetype or category title. |
| `Rarity` | `RPGCardRarity` | `Legendary` | Rarity tier (`Common`, `Uncommon`, `Rare`, `Epic`, `Legendary`, `Mythic`). |
| `ClassIcon` | `string` | `"🛡️"` | Leading class archetype icon or emoji symbol. |
| `AccentColor` | `string` | `""` | Optional hex color string to override the standard rarity border glow palette. |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#E11D48", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#1A0B10", BorderRadius = 6f, Padding = 10f)]
[ComponentRPGStatCard(
    Title = "VALKYRIE QUEEN BRUNHILDE", 
    Level = 85, 
    Subtitle = "Divine Spear Vanguard", 
    Rarity = RPGCardRarity.Mythic, 
    ClassIcon = "⚡")]
public class DivineValkyrieHero : MonoBehaviour
{
    [Header("Hero Combat Scaling")]
    public float attackPower = 2840f;
    public float holyDamageBonusPercent = 45f;
    public float ultimateSkillCooldownSec = 35f;

    [Header("Ascension State")]
    public int ascensionRank = 5;
    public bool isDivineShieldActive = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep midnight obsidian cards allow the card rarity border glow to pop vibrantly. |
| **`[ComponentPresetManager]`** | High | Coexists underneath or above the card banner for character build presets. |
| **`[ComponentHeaderButton]`** | High | Place action buttons (e.g. "Level Up", "Reset Talents") alongside hero cards. |
| **Inspector Controls** | High | Cleanly sits in `BeforeContent`, keeping all serialized properties undisturbed underneath. |
