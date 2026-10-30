# [SlotMachineReelText]

> Simulates a mechanical slot machine cylinder reel locking sequence with animated spinning status badges upon value modification.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit Transitions)`

---

## 1. Overview & Value Proposition

**What it does:**
`[SlotMachineReelText]` applies a tactile casino slot reel dynamic to enum, numeric, or string properties and collection element rows. Anchored to the top-right edge of the serialized field, it renders an animated mechanical reel status tag. At rest, it displays a dimmed `🎰 LOCKED` badge. Whenever the field value is changed—whether through a dropdown pick, slider drag, or procedural script modification—the badge springs into active motion, switching to `🎰 SPINNING...` in a warm amber glow (`HighlightColor`, defaulting to `#F59E0B`) for `SpinDuration` (defaulting to 450ms) before clicking firmly back into the locked state.

**The Problem:**
In RNG drop tables, loot box generators, procedural roll configurations, or random perk pickers, selecting a random value or enum feels mundane. Standard inspector fields lack the ceremonial suspense and physical weight of a mechanical slot reel click.

**The Solution:**
Decorating procedural or randomized values with `[SlotMachineReelText]`:
- **Mechanical Reel State Feedback:** Visually differentiates active spinning state (`🎰 SPINNING...`) from locked commitments (`🎰 LOCKED`).
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so each element row in `Enum[]`, `string[]`, or `List<T>` spins independently on value change.
- **Real-Time Property Tracking:** Automatically detects edits via `TrackPropertyValue` without requiring explicit method calls.
- **Vibrant Accent Highlight:** Illuminates in luminous amber (`HighlightColor`) during the active spin interval.
- **Non-Destructive Layout:** Maintains standard field alignment with an unobtrusive right-aligned status indicator.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CasinoLootBox : MonoBehaviour
{
    [SlotMachineReelText(spinDuration: 500f, HighlightColor = "#F59E0B")]
    public string rolledPrize = "Jackpot Diamond Ring";
}
```

---

## 3. Constructors & Parameters

```csharp
public SlotMachineReelTextAttribute(float spinDuration = 450f)
public SlotMachineReelTextAttribute(string[] options, float spinDuration = 450f)
public SlotMachineReelTextAttribute(params string[] options)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `spinDuration` | `float` | `450f` | Duration in milliseconds that the reel spins before locking into place. |
| `options` | `string[]` | `null` | Candidate symbols or reel items to cycle through during the spin sequence. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `SpinDuration` | `float` | `450f` | Total spin sequence duration in milliseconds. |
| `HighlightColor` | `string` | `"#F59E0B"` | Hex color string for the active spinning status badge and text highlight. |
| `Options` | `string[]` | `null` | Custom string array of symbols or states cycled across during the reel spin animation. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 5. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

namespace MaharajaStudio.MSUltimate.AnimatedAttributes.Sample
{
    public class SlotMachineReelTextExample : ModularMonoBehaviour
    {
        public enum GameDifficultyTier { Casual, Normal, Hardcore, Nightmare, Inferno }

        [System.Serializable]
        public class CasinoReelSlot
        {
            public string reelColumnId = "REEL_01";

            [SlotMachineReelText(spinDuration: 550f, HighlightColor = "#F59E0B")]
            public string jackpotSymbol = "CHERRY_TRIPLE";

            [Range(1, 100)]
            public int payoutMultiplier = 25;
        }

        [Title("SlotMachineReelText Attribute Showcase", "Mechanical cylinder drum spinning text")]
        [InfoBox("SlotMachineReelText imparts physical casino mechanical drum motion to fields.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Casino Drum Selectors")]
        [SlotMachineReelText(spinDuration: 500f, HighlightColor = "#F59E0B")]
        public GameDifficultyTier campaignDifficulty = GameDifficultyTier.Normal;

        [SlotMachineReelText(spinDuration: 400f, HighlightColor = "#10B981")]
        public string selectedHeroClass = "Sorcerer";

        [SlotMachineReelText(spinDuration: 650f, HighlightColor = "#FBBF24")]
        public string grandPrizeTier = "777 ROYAL DIAMOND JACKPOT";

        [BoxGroup("2. Inside Class Demonstration")]
        public CasinoReelSlot highRollerSlot = new CasinoReelSlot();

        [BoxGroup("3. Active 3-Reel Slot Bank")]
        [InfoBox("SlotMachineReelText cascades to collection elements, spinning mechanical drum options across individual list rows.", InspectorMessageType.Info)]
        [SlotMachineReelText(spinDuration: 500f, HighlightColor = "#F59E0B")]
        public GameDifficultyTier[] difficultyRoster = new GameDifficultyTier[]
        {
            GameDifficultyTier.Normal,
            GameDifficultyTier.Hardcore,
            GameDifficultyTier.Nightmare
        };

        public List<CasinoReelSlot> activeLootReels = new List<CasinoReelSlot>
        {
            new CasinoReelSlot { reelColumnId = "LEFT_REEL", jackpotSymbol = "BAR_DOUBLE", payoutMultiplier = 10 },
            new CasinoReelSlot { reelColumnId = "CENTER_REEL", jackpotSymbol = "BELL_GOLDEN", payoutMultiplier = 20 },
            new CasinoReelSlot { reelColumnId = "RIGHT_REEL", jackpotSymbol = "CROWN_ROYAL", payoutMultiplier = 50 }
        };

        [BoxGroup("4. High Roller Casino Playground")]
        [Button("Spin All Mechanical Reels", BackgroundColor = "#D97706", TextColor = "#FFFBEB")]
        public void SpinAllReels()
        {
            campaignDifficulty = (GameDifficultyTier)Random.Range(0, 5);
            Debug.Log("<color=#FBBF24>[SlotMachineReelText]</color> 🎰 All mechanical reels spinning across the payout payline!");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` / `[HorizontalGroup]` | Supported | Fits nicely inside reward chest cards and gacha configuration blocks. |
| `[ShowIf]` / `[EnableIf]` | Supported | Retains state smoothly across visibility toggles. |
| `[AnimatedOdometer]` | Stacking | Can be paired on separate fields within the same component. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`Enum[]`, `string[]`, `List<T>`), rendering individual spinning drum badges beside each element row. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Operates on direct enum arrays (`TEnum[]`), string arrays, and numeric lists. |
| **Nested Serializable Classes** | Supported | Fully spins and locks inside child classes and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions in `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
