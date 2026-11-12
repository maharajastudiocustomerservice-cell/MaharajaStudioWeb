# Retro8BitBlink

> `[Retro8BitBlink]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

Smooth interpolations look out of place when building retro 8-bit / 16-bit games, arcade cabinets, or chunky CRT retro hardware consoles. Classic coin-op arcade machines used sharp, non-interpolated palette blinking to demand player attention (e.g. *"INSERT COIN"*, *"1P READY"*, *"GAME OVER"*).

`[Retro8BitBlink]` provides authentic discrete stepped color toggling between two high-contrast arcade color states without smooth fading or transitions. It delivers maximum nostalgic impact with virtually zero CPU overhead.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ArcadeMachine : MonoBehaviour
{
    [Retro8BitBlink(250f, "#EF4444", "#FACC15")]
    public string CoinPrompt = "INSERT COIN TO PLAY";
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (250ms interval, red/yellow arcade palette)
public Retro8BitBlinkAttribute();

// Parameterized constructor with custom interval, alert color, and normal color
public Retro8BitBlinkAttribute(float blinkIntervalMs, string alertColor = "#EF4444", string normalColor = "#FACC15");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `BlinkIntervalMs` | `float` | `250f` | Duration of each color state in milliseconds before snapping to the alternate color. |
| `AlertColor` | `string` | `"#EF4444"` | High-contrast alert state color (hex code). |
| `NormalColor` | `string` | `"#FACC15"` | Standard base state color (hex code). |
| `Continuous` | `bool` | `true` | When true, blinks continuously; otherwise blinks only on hover or value change. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ArcadeCabinetMaster : ModularMonoBehaviour
{
    [Title("Coin-Op Arcade Cabinet", "Retro 8-bit stepped strobe telemetry", BackgroundColor = "#422006", TextColor = "#FACC15")]

    [BoxGroup("Cabinet Telemetry")]
    [Retro8BitBlink(200f, "#EF4444", "#FACC15")]
    public string AttractModePrompt = "INSERT 25¢ FOR 2 CREDITS";

    [BoxGroup("Cabinet Telemetry")]
    [Retro8BitBlink(150f, "#3B82F6", "#FFFFFF")]
    public int AllTimeHighScore = 998850;

    [BoxGroup("Midway Units")]
    public List<CabinetSlot> MachineRow = new List<CabinetSlot>
    {
        new CabinetSlot("PACMAN_COINOP", 4),
        new CabinetSlot("SPACE_INVADERS_V2", 0)
    };

    [Serializable]
    public class CabinetSlot
    {
        [Retro8BitBlink(220f, "#EC4899", "#FBBF24")]
        public string MachineTitle;

        public int CreditsLoaded;

        public CabinetSlot(string title, int credits)
        {
            MachineTitle = title;
            CreditsLoaded = credits;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[AdvancedClass]`** | Compatible | Discrete color snap operates cleanly without layout recalculation. |
| **`[ReadOnly]`** | Compatible | Color flashing functions normally even when value inputs are locked. |
| **Lists (`List<TClass>`)** | Compatible | Safe segmented container cleanly preserves row indices during recycling. |

---

## 7. Performance & Architecture

- **Extreme Low-Cost:** Never modifies transforms, scales, or margins. Only toggles `style.color` on discrete timer ticks.
- **Zero Drift:** Timer accumulator resets precisely on every interval for steady arcade cadence.

