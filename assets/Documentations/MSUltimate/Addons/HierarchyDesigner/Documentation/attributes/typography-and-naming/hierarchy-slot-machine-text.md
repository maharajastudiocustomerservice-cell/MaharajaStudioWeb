# [HierarchySlotMachineText]

> Animates hierarchy label characters rolling vertically into position like slot machine reels.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchySlotMachineText]` animates the characters of a GameObject's name as if spinning on a casino slot machine reel. Characters rapidly roll vertically across a blur of alphanumeric characters before snapping into position sequentially from left to right.

**The Problem:**
In casino games, loot box systems, randomized item spawners, or gacha mechanics, developers need an unmistakable visual cue in the editor that a system represents an RNG or prize-rolling component. Standard text gives no indication of randomness.

**The Solution:**
Decorating RNG components with `[HierarchySlotMachineText]`:
- **Casino Reel Spin Animation:** Renders vertical tumbling reel motion (`ReelSpeed = 4.0f`) that settles into the final text name over a configured duration (`Duration = 1.5f`).
- **Looping & Re-Spin Timing:** Configurable automatic re-spin loop (`Loop = true`, `LoopInterval = 5.0f`) creates continuous casino excitement in the Editor window.
- **Custom Reel Colors:** Style characters with lucky gold, amber, or neon pink (`TextColor = "#F39C12"`).
- **Bold Typography:** Enhances reel character legibility during rapid spin phases.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySlotMachineText(TextColor = "#F39C12", ReelSpeed = 4.5f, Duration = 1.2f, Loop = true)]
public class LuckyWheelRewardManager : MonoBehaviour
{
    public int jackpotMultiplier = 50;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` \| `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchySlotMachineTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchySlotMachineTextAttribute()
```

- Standard parameterless constructor. Reel dynamics, looping, and colors are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TextColor` | `string` | `"#F39C12"` | Hex color string applied to the rolling and settled reel characters. |
| `ReelSpeed` | `float` | `4.0f` | Vertical rolling velocity multiplier of the characters. |
| `Duration` | `float` | `1.5f` | Duration in seconds of the active spinning/rolling phase. |
| `Loop` | `bool` | `true` | Whether to periodically repeat the slot machine rolling animation. |
| `LoopInterval` | `float` | `5.0f` | Time delay in seconds between repeat spin cycles. |
| `Bold` | `bool` | `true` | Whether to render the characters with bold font weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the rolling animation continues during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchySlotMachineText(
    TextColor = "#EAB308", 
    ReelSpeed = 5.0f, 
    Duration = 1.8f, 
    Loop = true, 
    LoopInterval = 6.0f, 
    Bold = true)]
public class GachaLootBoxChest : MonoBehaviour
{
    [Header("Loot Configuration")]
    public string lootTableId = "EPIC_SEASON_01";
    public float legendaryDropChance = 0.025f;
    public bool isOpened = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyTooltip]`** | High | Display drop chance percentages and item table IDs on hover. |
| **`[HierarchyIcon]`** | High | Pair with custom dice, chest, or coin icons for an unmistakable casino appearance. |
| **`[HierarchyGlow]`** | High | Add golden or purple ambient glow around high-tier rolling containers. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with static color attributes as the slot machine renderer actively drives text color. |
