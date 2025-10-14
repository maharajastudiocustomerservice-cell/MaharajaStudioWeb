# Quick Start Guide

This guide provides the minimum setup required to get the Tactical Cover & Retreat AI System working in your project. It assumes you have an existing AI controller script (like a state machine or behavior tree) that will decide *when* the AI should hide.

## Step 1: Add and Configure `EnemyHider`

1.  Select your AI character's GameObject in the scene.
2.  Click **Add Component** and add the **`EnemyHider`** component.
3.  This component is the main interface for the system. You will see several fields in the Inspector.

## Step 2: Create Hiding Settings

The behavior of your AI is defined in a `HidingSettings` ScriptableObject.

1.  In your `Project` window, right-click to open the context menu.
2.  Navigate to **Create > HidingSystem > Hiding Settings**.
3.  Give the new asset a descriptive name (e.g., `TacticalAI_Settings`).

## Step 3: Assign Settings and Dependencies

Go back to the `EnemyHider` component on your AI character.

1.  **Assign Settings**: Drag your new `HidingSettings` asset into the **Settings** field.
2.  **Assign Nav Mesh Agent**: Drag the `NavMeshAgent` component from your AI character into the **Agent** field.
3.  **Configure Providers & Scorers**: Select your `HidingSettings` asset to configure it. Add at least one **Provider** (e.g., `BehindObstacleProviderSO`) to find spots and at least one **Scorer** (e.g., `VisibilityScorerSO`) to evaluate them. For even more intelligent behavior, you can tag objects in your scene with helper components like CoverNode, TacticalZone and etc...

## Step 4: Call the API from Your Controller

The `EnemyHider` component will not do anything on its own. You must call its public methods from your own AI logic scripts.

Here is a minimal example of how to trigger a search for a hiding spot.

```csharp
// In your existing AI controller script (e.g., EnemyMind.cs, AISateMachine.cs)

using UnityEngine;
using MaharajaStudio.HidingSystem; // Make sure to include the namespace

public class MyAIController : MonoBehaviour
{
    public Transform playerTarget; // Assign the player in the inspector
    private EnemyHider hider;

    void Start()
    {
        // Get the EnemyHider component
        hider = GetComponent<EnemyHider>();
        if (hider == null)
        {
            Debug.LogError("EnemyHider component not found!");
            this.enabled = false;
        }
    }

    void Update()
    {
        // This is your custom logic. For example, hide when health is low.
        if (ShouldStartHiding())
        {
            // First, tell the hider who to hide from
            hider.SetSinglePlayerTarget(playerTarget);

            // Then, command it to start the search
            hider.RetreatToHide();
        }
    }

    private bool ShouldStartHiding()
    {
        // Replace this with your own game's logic!
        // e.g., return currentHealth < maxHealth * 0.5f;
        // e.g., return playerIsAimingAtMe;
        return true;
    }
}
```

With this setup, when your `ShouldStartHiding()` condition becomes true, the `EnemyHider` will use your configured settings to find the best hiding spot and automatically move the NavMeshAgent there. You can subscribe to its `OnSearchSuccess` and `OnSearchFailed` events to be notified of the result.