# Getting Started: Your First Hiding AI

This guide will walk you through the entire process of setting up an AI that can intelligently hide from a player. We will cover the complete setup, from components to the final trigger script.

### Step 1: Scene Preparation

Before we begin, ensure your scene is ready:
1.  **NavMesh**: Your scene must have a baked NavMesh so the AI can navigate.
2.  **Layers**: Create a new Layer called `Obstacles` (or similar). Place all your static, cover-providing geometry (walls, crates, etc.) on this layer. We will use this to tell the system what blocks line of sight.

### Step 2: Create the AI's "Personality" Asset

The AI's behavior is stored in a `HidingSettings` ScriptableObject.
1.  In your Project window, right-click and go to **Create > HidingSystem > Hiding Settings**.
2.  Name it `StandardAI_Settings`.
3.  Select the new asset. In the Inspector, set the **Occluder Mask** to your `Obstacles` layer. This is critical for visibility checks.


### Step 3: Configure the `EnemyHider` Component

1.  Select your AI character GameObject. It must already have a `NavMeshAgent` component.
2.  Click **Add Component** and add the **`EnemyHider`**.
3.  Drag your `StandardAI_Settings` asset into the **Settings** slot on the `EnemyHider`.
4.  Drag the character's `NavMeshAgent` component into the **Agent** slot.

### Step 4: Define the Hiding Rules (Providers & Scorers)

Now, let's give our AI some basic rules. Select your `StandardAI_Settings` asset again.

1.  **Add Providers (Where to look for cover):**
    *   Under `Providers`, click `+` and add `BehindObstacleProviderSO`.
    *   Click `+` again and add `CurrentPositionProviderSO`. This is important, as it allows the AI to consider "staying put" if it's already in a good spot.

2.  **Add Scorers (How to decide which spot is best):**
    *   Under `Scorers`, click `+`. Add a `VisibilityScorerSO` and set its **Weight** to `2.0`. This makes being hidden very important.
    *   Add a `PathSafetyScorerSO` and set its **Weight** to `1.5`. This tells the AI to avoid running through open areas.
    *   Add a `DistanceScorerSO` with a **Weight** of `1.0`. This will make the AI prefer spots that are a reasonable distance away.

### Step 5: Triggering the AI with a Simple Controller

The `EnemyHider` needs to be told *when* to hide. Create a new script, `AIController.cs`, and add it to your AI character.

```csharp
using UnityEngine;
using MaharajaStudio.HidingSystem; // The Hiding System namespace

[RequireComponent(typeof(EnemyHider))]
public class AIController : MonoBehaviour
{
    // Assign your Player GameObject to this in the Inspector
    public Transform playerTarget;
    private EnemyHider hider;

    void Start()
    {
        hider = GetComponent<EnemyHider>();
        
        // Tell the hider who the enemy is
        hider.SetSinglePlayerTarget(playerTarget);
    }

    void Update()
    {
        // Check if we are exposed AND not already searching or moving to cover
        if (hider.IsThreatened && !hider.IsSearching && !hider.IsMoving)
        {
            Debug.Log("I'm exposed! Finding a place to hide.");
            hider.RetreatToHide();
        }
    }
}
```

Assign your Player object to the `Player Target` field on the `AIController`.

### You're Done!

Press Play! Move your player into the AI's line of sight. You should see the "I'm exposed!" debug log, and the AI will use your rules to find the best spot behind an obstacle and move there.

**➡️ Next: Learn the underlying principles in [Core Concepts](3-Core-Concepts.md)**
