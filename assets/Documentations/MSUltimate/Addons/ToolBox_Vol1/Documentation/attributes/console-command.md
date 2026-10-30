# [ConsoleCommand]

> Registers static C# methods as invokable developer console commands within the Advanced Runtime Console overlay.

---

## 1. Overview & Value Proposition

**What it does:**
`[ConsoleCommand]` automatically discovers and registers static C# methods into the runtime Advanced Console system. By decorating any static method with `[ConsoleCommand]`, developers, QA testers, and designers can invoke gameplay cheats, toggle debug visualization modes, manipulate game speed, or spawn items directly by typing commands into the runtime HUD console.

**The Problem:**
Building an in-game developer console usually involves creating complex custom command dictionaries, maintaining fragile string-to-method dispatchers, parsing arguments manually, and hardcoding autocomplete tables. When code is refactored, these bespoke dispatch tables fall out of sync, leading to broken cheats and frustrating debugging sessions during QA passes.

**The Solution:**
Decorating static methods with `[ConsoleCommand]`:
- **Zero-Boilerplate Registration:** Automatically indexes methods via reflection without any central registry or manager script setup.
- **Categorization & Autocomplete:** Organizes commands into clean categories (`Category = "Combat"`, `Category = "Cheats"`) with fuzzy autocomplete in the console GUI.
- **Usage Syntax Hints:** Supply clear syntax guides (`Usage = "give_gold <amount>"`) rendered in the console help menu.
- **Automatic Parameter Conversion:** Console parser automatically deserializes string arguments into primitive types (`int`, `float`, `bool`, `string`, `Vector3`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public static class DebugCommands
{
    [ConsoleCommand("heal_player", "Restores the local player to full health.", Category = "Player")]
    public static void HealPlayer()
    {
        Debug.Log("Player restored to full health.");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ToolBox-Vol1 Addon |
| **Attribute Target** | `Method` (Must be `static`) |
| **Inherited** | No |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Runtime Console Overlay / ToolBox Window |
| **Command System** | `AdvancedConsoleManager` |

---

## 4. Constructors & Parameters

```csharp
public ConsoleCommandAttribute(string command, string description = "")
```

- **`command`** (`string`): The keyword or command identifier typed by the user in the console (e.g. `"noclip"`, `"spawn_item"`).
- **`description`** (`string`, optional): Human-readable explanation of what the command does, displayed in the console help list.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Command` | `string` | Assigned in constructor | Primary keyword used to invoke this command. |
| `Description` | `string` | `""` | Descriptive summary displayed when running `help` or hovering the command. |
| `Usage` | `string` | `""` | Syntax signature hint explaining parameter requirements (e.g. `"<item_id> [count]"`). |
| `Category` | `string` | `"General"` | Organizational category used to group related commands in help listings. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

namespace ProjectZero.DebugTools
{
    public static class GameplayConsoleCommands
    {
        [ConsoleCommand("godmode", "Toggles invulnerability for the player character.", Category = "Cheats")]
        public static void ToggleGodMode()
        {
            // Toggle invulnerability flag
            Debug.Log("[Console] God mode toggled.");
        }

        [ConsoleCommand("set_timescale", "Changes the global simulation timescale.", 
            Usage = "set_timescale <scale:float>", Category = "Time")]
        public static void SetTimeScale(float scale)
        {
            Time.timeScale = Mathf.Clamp(scale, 0f, 10f);
            Debug.Log($"[Console] TimeScale adjusted to: {Time.timeScale}");
        }

        [ConsoleCommand("give_currency", "Adds credits to the player's wallet.", 
            Usage = "give_currency <currencyId:string> <amount:int>", Category = "Economy")]
        public static void GiveCurrency(string currencyId, int amount)
        {
            Debug.Log($"[Console] Granted {amount} units of '{currencyId}'.");
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| System / Addon | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[LiveTrack]`** | High | Use console commands to trigger state changes that are visualized live via `[LiveTrack]` graphs. |
| **`[HistoryTrack]`** | High | Value modifications executed via console commands are recorded into the `[HistoryTrack]` timeline. |
| **`[TrackLifetime]`** | High | Invoke spawn/despawn console commands to stress-test lifecycle tracking buffers. |
| **Advanced Console UI** | Native | Commands appear immediately in search, fuzzy autocomplete, and the categorized `help` list. |
