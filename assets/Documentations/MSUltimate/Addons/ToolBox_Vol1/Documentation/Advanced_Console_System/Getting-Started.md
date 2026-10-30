# Getting Started with Advanced Console

This guide will help you open, use, and integrate the **Advanced Console System** into your project.

## 1. Opening the Console Window
Inside the Unity Editor, open the Advanced Console Window from the top menu:
**`Window`** -> **`Maharaja Studio`** -> **`Advanced Console`**

*Tip: Dock this window alongside your standard Unity Console or Scene view. It serves as a superset of the built-in console for complex debugging.*

## 2. Your First Log
You can log to the Advanced Console from any script using the `ConsoleLogManager`. Ensure you include the namespace:

```csharp
using MaharajaStudio.MSUltimate.Editor.AdvancedConsole;

public class MyScript : MonoBehaviour 
{
    void Start() 
    {
#if UNITY_EDITOR
        ConsoleLogManager.LogInfo("System initialized successfully!", channel: "Core");
#endif
    }
}
```

*Note: The `ConsoleLogManager` is an Editor-only class. Wrap your calls in `#if UNITY_EDITOR`.*

## 3. Enabling the Runtime Overlay
To access the console during actual gameplay (in the Editor or in a build):
1. Create an empty GameObject in your first/boot scene.
2. Add the **`RuntimeConsoleOverlay`** component to it (`Add Component -> Maharaja Studio -> Runtime Console Overlay`).
3. Press **Play**.
4. Press the **Backtick key (\`)** (typically under the Escape key) to toggle the console open and closed.

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
