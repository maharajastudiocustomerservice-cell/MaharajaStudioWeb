# How-To Guide

This guide covers common advanced use cases for the Advanced Console System.

## How to log Context Snapshots
When debugging complex AI or physics, knowing the state of specific variables at the moment of failure is critical.

```csharp
var context = new Dictionary<string, string>
{
    { "Velocity", currentVelocity.ToString() },
    { "Grounded", isGrounded.ToString() },
    { "Target", currentTarget ? currentTarget.name : "None" }
};

ConsoleLogManager.Log(
    ConsoleLogSeverity.Warning, 
    ConsoleLogSource.User,
    "Player missed jump threshold",
    channel: "Physics",
    contextSnapshot: context,
    target: this.gameObject // Links the log to this GameObject
);
```
*In the Console Window, click the log to see these values neatly formatted in the Detail Panel.*

## How to add Quick Actions to logs
Quick Actions are buttons embedded in a log's detail view. They are perfect for auto-fixing issues or teleporting to problem areas.

```csharp
var actions = new List<ConsoleAction>
{
    new ConsoleAction("Auto-Fix Prefab", () => {
        // Run code to fix the issue
        ResetPrefabState();
    }),
    new ConsoleAction("Teleport to Error", () => {
        SceneView.lastActiveSceneView.pivot = this.transform.position;
    })
};

ConsoleLogManager.Log(
    ConsoleLogSeverity.Error, 
    ConsoleLogSource.User,
    "Navigation Node is corrupted.",
    actions: actions
);
```

## How to search using regular expressions (Regex)
If you need to find specific patterns in your logs, use the Regex search.
1. In the Advanced Console Window, click the `.*` (Regex Search) button in the toolbar.
2. In the search box, enter your pattern. 
   - Example `^\[Player\]` finds logs that *start* with `[Player]`.
   - Example `Timeout|Disconnect` finds logs containing either word.

## How to add custom Runtime Console Commands
Ensure your method is `public static` and add the `[ConsoleCommand]` attribute.

```csharp
using MaharajaStudio.MSUltimate.Runtime;

public class CheatManager
{
    [ConsoleCommand("give_gold", "Gives the player a specific amount of gold")]
    public static void GiveGold(int amount)
    {
        Player.Inventory.Gold += amount;
        // The return value (or Debug.Log) will be printed in the overlay console.
        UnityEngine.Debug.Log($"Granted {amount} gold."); 
    }
}
```
*To use: open the runtime console ( ` ) and type `give_gold 500`.*

## How to Bookmark and Annotate Logs
During a playtest, you might notice odd behavior that doesn't trigger an error.
1. Find a log representing that moment.
2. Click the **Star (☆)** icon next to the log to **Bookmark** it.
3. Select the log and scroll down in the Detail Panel to the **Note:** text box. 
4. Type your observations (e.g., "Player clipped through floor here").
5. Use the Star icon in the main toolbar to filter *only* your bookmarked logs when you finish testing.
