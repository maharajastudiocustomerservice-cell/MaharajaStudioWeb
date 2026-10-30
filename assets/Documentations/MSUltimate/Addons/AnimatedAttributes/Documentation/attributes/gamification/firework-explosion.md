# [FireworkExplosion]

> Spawns a radial firework shell burst that sparkles, shimmers, and glitters across the inspector upon completion triggers or clicks.

---

## 1. Overview & Value Proposition

**What it does:**
`[FireworkExplosion]` transforms button presses, field completions, and state changes into celebratory visual fireworks. It simulates an aerial shell detonation that blooms outward in a circular radius (`ExplosionRadius`) with glittering particle trails (`ParticleCount`), styled in radiant primary hues (`PrimaryColor`) that dissipate gracefully over a defined timeframe (`Duration`).

**The Problem:**
Highlighting high-value milestones—such as unlocking achievements, beating campaign bosses, or completing asset validation checks—feels underwhelming when only conveyed by static checkboxes or small notification text.

**The Solution:**
Decorating critical triggers and methods with `[FireworkExplosion]`:
- **Radiant Shell Bloom:** Launches a 360-degree fireworks burst with randomized trail velocities and twinkle decay.
- **Customizable Color Scheme:** Pick signature celebratory colors (`PrimaryColor`), such as hot magenta, neon gold, or electric cyan.
- **Adjustable Blast Radius:** Scale burst spread (`ExplosionRadius`) to fit compact inspector panels or expansive inspector headers.
- **Multi-Target Support:** Attach to fields, properties, or clickable methods (`[Button]`) to celebrate automated or manual actions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class PlayerMilestone : MonoBehaviour
{
    [FireworkExplosion(primaryColor: "#F59E0B", radius: 75f)]
    public int totalStarsEarned = 100;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serializable field, property, collection item, or button method |
| **Collection Cascading** | Supported (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>` via `ICollectionElementAttribute`) |
| **Collection Batch Processing**| Supported (`ICollectionBatchAttribute`, `ICollectionBatchDrawer` with `"🎆"` header celebration button) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public FireworkExplosionAttribute(string primaryColor = "#EC4899", float radius = 60f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `primaryColor` | `string` | `"#EC4899"` | Primary hex color of the firework explosion flash and sparkles. |
| `radius` | `float` | `60f` | Radial spread distance in pixels of the exploding shell sparks. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PrimaryColor` | `string` | `"#EC4899"` | Hex color string for the firework flash and glittering sparks. |
| `ExplosionRadius` | `float` | `60f` | Radial spread distance in pixels for the firework particles. |
| `ParticleCount` | `int` | `35` | Total number of spark particles emitted during the burst. |
| `Duration` | `float` | `900f` | Total lifetime of the firework animation in milliseconds. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

namespace MaharajaStudio.MSUltimate.AnimatedAttributes.Sample
{
    [AddComponentMenu("Maharaja Studio/MSUltimate/Samples/Animated Attributes/Gamification/Firework Explosion Example")]
    public class FireworkExplosionExample : ModularMonoBehaviour
    {
        // ─── 1. Standalone Fields ────────────────────────────────────────────────
        [BoxGroup("1. Standalone Firework Shell Bursts", BackgroundColor = "#1F0718", BorderColor = "#DB2777", BorderRadius = 6, MarginBottom = 8)]
        [FireworkExplosion(primaryColor: "#EC4899", radius: 75f)]
        public string bossDefeatedAchievement = "DRAGON SLAYER (Unlocked)";

        [FireworkExplosion(primaryColor: "#F59E0B", radius: 80f)]
        public int playerMilestoneLevel = 50;

        // ─── 2. Inside Class Demonstration ───────────────────────────────────────
        [BoxGroup("2. Inside Class Demonstration", BackgroundColor = "#26091E", BorderColor = "#BE185D", BorderRadius = 6, MarginBottom = 8)]
        public FestivalRocketSlot finaleRocketSlot = new FestivalRocketSlot();

        [System.Serializable]
        public class FestivalRocketSlot
        {
            public string rocketName = "Supernova Comet Shell";
            [FireworkExplosion(primaryColor: "#A855F7", radius: 70f)]
            public int shellCaliberMm = 120;
        }

        // ─── 3. Direct Collections Cascading & Batch Action ──────────────────────
        [BoxGroup("3. Direct Collections Cascading & Batch Action", BackgroundColor = "#170512", BorderColor = "#9D174D", BorderRadius = 6, MarginBottom = 8)]
        [InfoBox("Direct collection cascading: [FireworkExplosion] implements ICollectionElementAttribute to spawn localized firework bursts on individual array/list rows, and ICollectionBatchAttribute to surface a '🎆' batch celebration header button.", InspectorMessageType.Info)]

        [FireworkExplosion(primaryColor: "#A855F7", radius: 70f)]
        public int[] shellSalvoCalibersMm = new int[] { 75, 100, 125, 150 };

        [FireworkExplosion(primaryColor: "#38BDF8", radius: 65f)]
        public List<string> celebratoryStageCues = new List<string>
        {
            "Opener: Crimson Peony",
            "Mid-Show: Golden Willow Cascade",
            "Finale: Titanium Salvo Burst"
        };

        // ─── 4. Interactive Playground ───────────────────────────────────────────
        [BoxGroup("4. Pyrotechnic Launch Controls", BackgroundColor = "#2D0C24", BorderColor = "#F472B6", BorderRadius = 6)]
        [FireworkExplosion(primaryColor: "#38BDF8", radius: 90f)]
        [Button("Launch Grand Finale Firework! (Cyan 90px)", BackgroundColor = "#DB2777", TextColor = "#FFFFFF")]
        public void LaunchGrandFinale()
        {
            Debug.Log("[FireworkExplosion] WHOOSH... BOOM! Grand finale firework shell detonated.");
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### Attribute Stacking

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Detonates fireworks directly from inspector action buttons upon execution. |
| `[ConfettiCannon]` | Stacking | Combines fireworks shell bursts with falling confetti for festival-grade celebrations. |
| `[CardGroup]` | Supported | Renders smoothly over cards and groups without clipping adjacent inspector rows. |

### Collection Cascading Matrix

| Collection Type | Element Type | Supported | Notes |
| :--- | :--- | :---: | :--- |
| `T[]` (Array) | `int[]`, `string[]`, any type | Yes | Detonates radial firework shell bursts from each individual array element. |
| `List<T>` | `List<int>`, `List<string>`, `List<T>` | Yes | Cascades down to individual list elements automatically. |
| `AdvancedList<T>` | Any element type | Yes | Fully supported in reorderable list items. |
| `SerializableDictionary<K, V>` | Key or Value elements | Yes | Fires celebratory spark bursts on interacting with dictionary items. |
| `[Serializable] class/struct` | Nested properties | Yes | Plays spark animations on editing fields inside nested classes. |
| **Collection Batch Header** | `"🎆"` Header Button | Yes | Launches fireworks simultaneously across all collection rows via `ICollectionBatchAttribute`. |

