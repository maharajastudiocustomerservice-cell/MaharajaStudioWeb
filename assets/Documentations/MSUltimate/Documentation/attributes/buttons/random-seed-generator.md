# [RandomSeedGenerator]

> Attaches a 1-click randomize dice button and seed history tracker beside integer seed fields for procedural generation workflows.

---

## 1. Overview & Value Proposition

**What it does:**
Adds a 1-click randomize button (dice icon) and recent seed history chips next to integer seed fields.

**The Problem:**
Testing procedural worlds, dungeon layouts, or random loot requires changing seeds constantly. In standard Unity, you have to manually click the field, backspace, and mash random numbers on your keyboard over and over again. Plus, if you find a seed you liked, it's easy to accidentally overwrite and lose it forever.

**The Solution:**
Add `[RandomSeedGenerator]` to any `int`, `uint`, or `long` seed field:
- **1-Click Randomize:** Hit the dice button to instantly generate a new random seed.
- **Seed History Chips:** Keeps track of recently generated seeds so you can jump back to a great world layout anytime.
- **Customizable Random Source:** Choose between `UnityEngine.Random` and `System.Random`.
- **Fast Procedural Iteration:** Speeds up testing for terrain, noise generation, and roguelike level generators.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TerrainGenerator : MonoBehaviour
{
    [RandomSeedGenerator]
    public int worldSeed = 1337;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `int`, `uint`, `short`, `byte` |
| **Collection Interfaces** | `ICollectionElementAttribute`, `ICollectionBatchAttribute` (`"🎲"`) |
| **Collection Cascading** | Full (`List<int>`, `int[]`, `AdvancedList<int>`, `SerializableDictionary<K, int>`) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public RandomSeedGeneratorAttribute(int historySize = 5, string colorHex = "#2980b9", bool useUnityRandom = false)
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HistorySize` | `int` | `5` | Number of previous generated seeds remembered in the history chips. |
| `ColorHex` | `string` | `"#2980b9"` | Hex background color tint for the history chip buttons. |
| `UseUnityRandom` | `bool` | `false` | When `true`, uses `UnityEngine.Random`; otherwise uses `System.Random`. |
| `ShowHeaderButton` | `bool` | `true` | Surfaces a batch execution action button (`"🎲"`) in collection headers. |
| `HeaderButtonText` | `string` | `"🎲"` | Visual label displayed on the collection header action button. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ProceduralDungeonBuilder : MonoBehaviour
{
    [Serializable]
    public class BiomeProfile
    {
        public string biomeName = "Crystal Caverns";

        [RandomSeedGenerator(historySize: 4, colorHex: "#38BDF8")]
        public int biomeSeed = 1024;
    }

    [BoxGroup("World Generation Rules", Box = true)]
    [RandomSeedGenerator(historySize: 8, colorHex: "#8E44AD")]
    [Tooltip("Global generation seed determining room layout and enemy placements.")]
    public int dungeonSeed = 42;

    [BoxGroup("Biome Profile (Inside Class)")]
    public BiomeProfile primaryBiome = new BiomeProfile();

    [BoxGroup("Direct Collection Cascading")]
    [InfoBox("Click the collection header '🎲' button to reroll all array/list seeds at once, or roll elements individually.", InspectorMessageType.Info)]
    [RandomSeedGenerator(historySize: 3, colorHex: "#10B981")]
    public int[] chunkNoiseSeeds = new int[] { 10101, 20202, 30303, 40404 };

    [RandomSeedGenerator(historySize: 4, colorHex: "#38BDF8")]
    public List<int> worldGenPassSeeds = new List<int> { 55501, 55502, 55503 };
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Pairs seamlessly inside `[BoxGroup]` and `[VerticalGroup]`.
- **Callbacks:** When clicked, triggers property modification cascades, immediately executing any attached `[OnValueChanged]` callbacks.
- **Undo Integration:** Seed generation creates an undo point, allowing instant restoration via `Ctrl+Z`.

### Collection Cascading Matrix

| Collection Type | Cascading Behavior | Presentation Mode |
| :--- | :---: | :--- |
| `int[]` | **Supported** | Compact dice roller button + history chips per row + batch reroll header button (`"🎲"`). |
| `List<int>` | **Supported** | Seamless integration with reorderable lists; each element tracks independent history. |
| `AdvancedList<int>` | **Supported** | Full compatibility with advanced list pagination and reordering. |
| `SerializableDictionary<K, int>` | **Supported** | Cascades to dictionary value elements matching integer types. |
| Nested `[Serializable]` Classes | **Supported** | Preserves independent history storage keys per class member. |
