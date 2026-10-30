# [ProbabilityPie]

> Renders collections of weighted items as an interactive Donut/Pie distribution chart and segmented percentage ribbon with 1-click normalization tools.

---

## 1. Overview & Value Proposition

**What it does:**
Turns arrays or lists of weighted items into an interactive Pie/Donut chart with a percentage breakdown and 1-click normalization tools.

**The Problem:**
Balancing loot tables, enemy spawn rates, or procedural generation weights by staring at a raw list of numbers is confusing. You have to do mental math or open a calculator to figure out what a weight of "35" actually means when total weights add up to 215. This makes tuning drops slow and prone to balance errors.

**The Solution:**
Add `[ProbabilityPie]` above any array or list containing weight values:
- **Instant Visual Pie Chart:** See the exact percentage distribution of every item as a color-coded pie/donut chart.
- **Percentage Ribbon & Legend:** Displays clear percentages (e.g. `Common: 65%`, `Rare: 10%`) right on screen.
- **1-Click "Normalize to 100%" & "Equalize" Buttons:** Instantly scales all weights so they cleanly add up to 100%, or distributes weights equally across elements.
- **Zero Lag:** Charts update in real time as you adjust numbers in the list.

---

## 2. Quick Start

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class DropManager : MonoBehaviour
{
    [Serializable]
    public struct DropItem
    {
        public string itemName;
        public float weight;
    }

    [ProbabilityPie("weight", "itemName")]
    public DropItem[] drops;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | Arrays (`T[]`), Lists (`List<T>`), primitive arrays (`float[]`, `int[]`) |
| **Collection Presentation** | Supported (`ICollectionPresentationAttribute`) |
| **Collection Batch Processing** | Supported (`ICollectionBatchAttribute`, `ICollectionBatchDrawer`) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public ProbabilityPieAttribute(string weightMember = "weight", string labelMember = "name")
```
- **`weightMember`**: Name of the numerical field/property in child items representing probability weight. Default is `"weight"`.
- **`labelMember`**: Name of the string/object field in child items representing the item name in tooltips/legend. Default is `"name"`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `EnableCustomPresentation` | `bool` | `true` | Enables rich Donut/Pie presentation mode for the collection container. |
| `BatchTriggers` | `CollectionBatchTriggers` | `None` | Automated lifecycle events that trigger weight recalculation/batch actions. |
| `ShowHeaderButton` | `bool` | `true` | Renders the 1-click batch normalize button in the collection container header. |
| `HeaderButtonText` | `string` | `"⚖️"` | Icon or text displayed on the collection header action button. |
| `WeightMember` | `string` | `"weight"` | Field or property name for the numerical weight. |
| `LabelMember` | `string` | `"name"` | Field or property name for the item label/title. |
| `ShowPieChart` | `bool` | `true` | Renders the circular vector donut/pie chart graphic. |
| `ShowPercentageBar` | `bool` | `true` | Renders the horizontal segmented percentage bar beneath the chart. |
| `ShowLegend` | `bool` | `true` | Displays color-coded legend badges with computed percentage values. |
| `ShowActionButtons` | `bool` | `true` | Displays the 1-click 'Normalize to 100%' and 'Equalize' action buttons. |
| `ChartRadius` | `float` | `55f` | Outer radius of the vector pie/donut chart in pixels. |
| `DonutHoleRatio` | `float` | `0.5f` | Inner donut hole ratio (`0.0` for solid pie, `0.5` for donut ring). |
| `CustomPalette` | `string[]` | `null` | Optional array of hex color strings to theme each slice sequentially. |
| `BackgroundColor` | `string` | `"#1E1E28"` | Background container card hex color. |
| `BorderColor` | `string` | `"#323242"` | Border outline hex color of the container card. |
| `BorderRadius` | `float` | `6f` | Corner rounding radius of the container card in pixels. |
| `MarginTop` | `float` | `4f` | Top margin in pixels. |
| `MarginBottom` | `float` | `8f` | Bottom margin in pixels. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MonsterSpawner : MonoBehaviour
{
    [Serializable]
    public class SpawnEntry
    {
        public string monsterName;
        public GameObject prefab;
        [Range(0, 100)] public float spawnChance = 20f;
    }

    [BoxGroup("Encounter Probability Matrix", Box = true)]
    [ProbabilityPie(
        weightMember: nameof(SpawnEntry.spawnChance),
        labelMember: nameof(SpawnEntry.monsterName),
        ChartRadius = 65f,
        DonutHoleRatio = 0.55f,
        ShowActionButtons = true
    )]
    [Tooltip("Weighted distribution of monsters spawned during night phases.")]
    public List<SpawnEntry> nightEncounters = new List<SpawnEntry>();
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Works cleanly inside `[BoxGroup]` and `[CardGroup]`.
- **Zero Allocations:** Recalculates slice angles only when underlying property values are edited, maintaining responsive 60 FPS repaints.
- **Defensive Handling:** Safely handles empty lists, zero-weight sums, or invalid member names with clean inline guidance messages without throwing GUI exceptions.
