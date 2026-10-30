# [RPGRarityGlow]

> Wraps an inspector field in an animated RPG rarity aura with floating particle sparks and decorative corner badges.

---

## 1. Overview & Value Proposition

**What it does:**
`[RPGRarityGlow]` encloses the decorated field within an animated, color-coded rarity border aura that reflects classic RPG loot tiers—from `Common` grey to `Legendary` gold and `Mythic` cosmic violet. It features floating ambient particle motes and optional corner insignia badges (`ShowCornerBadges`).

**The Problem:**
In loot-heavy games, inventory ScriptableObjects and item prefabs are difficult to distinguish at a glance when inspecting data folders. Common consumables and ultra-rare artifacts look identical in standard grey inspector panels.

**The Solution:**
Applying `[RPGRarityGlow]` to item data:
- **Instant Tier Recognition:** Instantly visually communicates item rarity using standard industry color conventions.
- **6 Built-In Rarity Tiers:** Out-of-the-box support for `Common`, `Uncommon`, `Rare`, `Epic`, `Legendary`, and `Mythic`.
- **Floating Ambient Sparks:** Gentle particle sparks drift upward along the aura borders for high-tier items.
- **Corner Badges & Scalable Intensity:** Toggle ornate corner gems (`ShowCornerBadges`) and fine-tune `AuraIntensity`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class LootItem : MonoBehaviour
{
    [RPGRarityGlow(RPGRarityTier.Legendary, AuraIntensity = 1.2f)]
    public string weaponName = "Excalibur of the Sun";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field, property, or collection element (`T[]`, `List<T>`) |
| **Collection Cascading** | Yes (`ICollectionElementAttribute`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public RPGRarityGlowAttribute(RPGRarityTier rarity = RPGRarityTier.Legendary)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `rarity` | `RPGRarityTier` | `RPGRarityTier.Legendary` | Rarity tier determining aura palette and particle effects. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Rarity` | `RPGRarityTier` | `Legendary` | Item rarity tier enum value. |
| `AuraIntensity` | `float` | `1.0f` | Brightness and glow bloom multiplier for the aura. |
| `ShowCornerBadges` | `bool` | `true` | Whether to render decorative corner gem badges around the element. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

### `RPGRarityTier` Enumeration

| Tier | Aura Color | Theme & Visuals |
| :--- | :--- | :--- |
| `Common` | `#94A3B8` (Slate Grey) | Subtle muted border with no particle emissions. |
| `Uncommon` | `#22C55E` (Emerald Green) | Fresh forest glow with gentle shimmer. |
| `Rare` | `#3B82F6` (Cobalt Blue) | Crisp sapphire glow with drifting energy motes. |
| `Epic` | `#A855F7` (Arcane Purple) | Vibrant violet aura with swirling magical sparkles. |
| `Legendary` | `#F59E0B` (Radiant Gold) | Intense golden sunburst glow with ascending sparks. |
| `Mythic` | `#EC4899` (Cosmic Crimson) | Pulsing magenta-red cosmic vortex aura with dual particle streams. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class EquipmentItemDefinition : ScriptableObject
{
    [Header("Loot Configuration")]
    [RPGRarityGlow(RPGRarityTier.Mythic, AuraIntensity = 1.3f, ShowCornerBadges = true)]
    public string artifactTitle = "Heart of the Void God";

    [RPGRarityGlow(RPGRarityTier.Epic)]
    public int spellPowerBonus = 350;

    [RPGRarityGlow(RPGRarityTier.Rare)]
    public float criticalStrikeChance = 14.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Encloses neatly inside or outside inspector group frames. |
| `[ParticleBurst]` | Stacking | Combines ambient rarity sparks with explosive click burst celebrations. |
| `[Asset3DPreview]` | Supported | Frames 3D item asset previews in ornate rarity auras. |
| Direct Collections | Supported | Cascades animated rarity auras and glowing borders to each element card in collections via `ICollectionElementAttribute`. |
