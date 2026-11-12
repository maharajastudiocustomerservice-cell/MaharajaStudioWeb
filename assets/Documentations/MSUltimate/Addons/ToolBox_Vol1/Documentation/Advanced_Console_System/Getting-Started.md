# Getting Started with Advanced Console

This guide will help you open, use, and integrate the **Advanced Console System** into your project.

## 1. Opening the Console Window
Inside the Unity Editor, open the Advanced Console Window from the top menu:
**`Tools`** -> **`Maharaja Studio`** -> **`MSUltimate`** -> **`ToolBox Vol 1`** -> **`Advanced Console`**

*Tip: Dock this window alongside your standard Unity Console or Scene view. It serves as a superset of the built-in console for complex debugging.*

## 2. Your First Log
You can log to the Advanced Console from any script using `MSConsole` (safe in both Editor and player builds with no `#if UNITY_EDITOR` required) or `RuntimeConsoleLogManager`:

```csharp
using MaharajaStudio.MSUltimate.Runtime;
using UnityEngine;

public class MyScript : MonoBehaviour 
{
    void Start() 
    {
        MSConsole.Log("System initialized successfully!", channel: "Core", target: this);
    }
}
```

## 3. Enabling the Runtime Overlay
During gameplay (in Play Mode or in a build), `RuntimeAdvancedConsoleUI` loads automatically via `RuntimeInitializeOnLoadMethod`:
1. Press **Play** (or run a build).
2. Press the **Backtick key (\`)** (typically under the Escape key) to toggle the UI Toolkit console open and closed.
*(Note: The legacy IMGUI `RuntimeConsoleOverlay` component is deprecated in favor of `RuntimeAdvancedConsoleUI`.)*

## 4. Registering a Console Command
Console commands allow you to trigger methods from within the in-game runtime console.

```csharp
using MaharajaStudio.MSUltimate.Runtime;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public static float PlayerHealth = 100f;

    [ConsoleCommand("heal", "Restores the player's health to 100")]
    public static void HealPlayer()
    {
        PlayerHealth = 100f;
        Debug.Log("Player health restored!");
    }

    [ConsoleCommand("set_speed", "Sets the player's movement speed")]
    public static void SetSpeed(float speed)
    {
        // Add logic to set speed
        Debug.Log($"Speed set to {speed}");
    }
}
```
Open the runtime console ( ` ) and type `heal` or `set_speed 15.5`.

---
**Next Step:** Dive deeper into the architecture in [Core Concepts](Core-Concepts.md).
