# [ParticleBurst]

> Spawns an animated 2D canvas particle burst explosion (confetti or sparks) with physics gravity and velocity spread when a field is clicked or modified.

---

## 1. Overview & Value Proposition

**What it does:**
Spawns a delightful, celebratory mini-particle simulation directly inside the Inspector window whenever the decorated field is clicked or changed. Particles erupt outward with customizable velocity (`Spread`), gravity acceleration (`Gravity`), color (`ParticleColor`), count (`ParticleCount`), and lifetime (`BurstDuration`).

**The Problem:**
Completing major milestones, clicking critical build buttons, or discovering rare items in inspector data tables feels mundane without visual celebration.

**The Solution:**
Add `[ParticleBurst]` to any field or button:
- **Celebratory Feedback:** Rewarding particle sparks / confetti explosions celebrate crucial interactions.
- **2D Canvas Physics:** Particles simulate genuine 2D ballistic physics with velocity dispersion and downward gravity.
- **Particle Customization:** Configure particle count (e.g. `25`), spread radius, and spark color (`#FFD700` gold).
- **Transient Zero-Leak Simulation:** Canvas particles automatically destroy upon expiry with zero memory allocation.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class QuestReward : MonoBehaviour
{
    [ParticleBurst(ParticleColor = "#FFD700", ParticleCount = 20, Spread = 60f)]
    public int bonusGoldReward = 500;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | Any serializable field or property |
| **Collection Interfaces** | `ICollectionElementAttribute`, `ICollectionBatchAttribute` (`"✨"`) |
| **Collection Cascading** | Full (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ParticleBurstAttribute()
```

*Attribute initializes with golden spark particle settings; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ParticleColor` | `string` | `"#FFD700"` | Hex color string for spawned particles. |
| `ParticleCount` | `int` | `15` | Number of particles spawned in each burst. |
| `BurstDuration` | `float` | `1000f` | Lifetime of the particle burst animation in milliseconds. |
| `Gravity` | `float` | `9.8f` | Downward gravity acceleration applied to particles. |
| `Spread` | `float` | `50f` | Initial velocity and dispersion spread of particles in pixels. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |
| `ShowHeaderButton` | `bool` | `true` | Surfaces a batch execution action button (`"✨"`) in collection headers. |
| `HeaderButtonText` | `string` | `"✨"` | Visual label displayed on the collection header action button. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class AchievementDefinition : MonoBehaviour
{
    [Serializable]
    public class WeaponProfile
    {
        public string weaponName = "Excalibur";

        [ParticleBurst(ParticleColor = "#8B5CF6", ParticleCount = 20)]
        public int forgeLevel = 5;
    }

    [Header("Milestone Achievement Unlock")]
    [ParticleBurst(
        ParticleColor = "#f39c12", 
        ParticleCount = 30, 
        BurstDuration = 1200f, 
        Spread = 80f, 
        Gravity = 12f
    )]
    public bool isAchievementUnlocked = false;

    [Header("Prestige Level Rank")]
    [ParticleBurst(ParticleColor = "#9b59b6", ParticleCount = 20)]
    public int prestigeRank = 1;

    [Header("Weapon Profile (Inside Class)")]
    public WeaponProfile activeWeapon = new WeaponProfile();

    [Header("Direct Collections Cascading")]
    [ParticleBurst(ParticleColor = "#F59E0B", ParticleCount = 25)]
    public int[] runePowerTiers = new int[] { 100, 250, 500, 1000 };

    [ParticleBurst(ParticleColor = "#38BDF8", ParticleCount = 15)]
    public List<float> elementalMultipliers = new List<float> { 1.25f, 1.75f, 2.5f };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Particle explosions burst cleanly across container boundaries. |
| `[ClickRipple]` | Supported | Can be combined with click ripples for maximum tactile celebration. |
| Primary Drawers | Supported | Operates on a transient overlay layer without interfering with data values. |

### Collection Cascading Matrix

| Collection Type | Cascading Behavior | Presentation Mode |
| :--- | :---: | :--- |
| `int[]`, `float[]` | **Supported** | Triggers reactive sparks on item change + batch `"✨"` celebration header button. |
| `List<string>` | **Supported** | Cascades to string entries; editing any entry triggers spark burst. |
| `AdvancedList<T>` | **Supported** | Full compatibility with reorderable list animations. |
| `SerializableDictionary<K, V>` | **Supported** | Cascades to dictionary value elements. |
| Nested `[Serializable]` Classes | **Supported** | Members inside serialized structures trigger independent spark bursts. |
