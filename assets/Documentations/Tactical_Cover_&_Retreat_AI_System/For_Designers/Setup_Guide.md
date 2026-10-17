# Setup Guide for Designers

Welcome! This guide will walk you through setting up the Tactical Cover & Retreat AI System in your Unity project. The entire system is designed to be configured from the editor without writing code, though a programmer will need to trigger the hiding action.

## Goal

Our goal is to give an AI character the ability to intelligently hide from its enemies. We will achieve this by:
1.  Adding and configuring the main `EnemyHider` component.
2.  Creating a "Rulebook" (`HidingSettings`) that defines what makes a good hiding spot.
3.  Hooking into the `EnemyHider`'s events to see the results.

---

### Step 1: Add the `EnemyHider` Component

This component is the "brain" of the hiding system for a single AI.

1.  Select your AI character's GameObject.
2.  In the Inspector, click **Add Component** and add **`EnemyHider`**.

You will see several fields on this component. Let's configure the most important ones.

*   **Execution Mode**: Choose `Asynchronous` for the best performance, or `Synchronous` for easier debugging.
*   **Allow Desperate Retreat**: Check this box if you want the AI to find the "least bad" spot if no perfectly safe spot is available. This prevents the AI from getting stuck when surrounded.

![Add EnemyHider Component](https://i.imgur.com/your-image-placeholder.png)
*(Note: Images are placeholders. They will be replaced with actual screenshots of the interface)*

---

### Step 2: Create the AI's "Rulebook" (Hiding Settings)

Next, we create an asset to hold all our rules for hiding.

1.  In your `Project` window (e.g., in an `AI/Settings` folder), right-click.
2.  Go to **Create > HidingSystem > Hiding Settings**.
3.  Name it something descriptive, like `AggressiveAI_Rules` or `StealthyAI_Settings`.

Now, go back to your `EnemyHider` component. Drag your new `HidingSettings` asset from the Project window into the **Settings** slot. Also, make sure to assign the **Agent** field with the `NavMeshAgent` from your character.

![Assign Hiding Settings](https://i.imgur.com/your-image-placeholder.png)

---

### Step 3: Define "What is a Good Hiding Spot?"

Select your `HidingSettings` asset in the Project window to see its properties in the Inspector. This is where you define the AI's personality using **Providers** and **Scorers**.

*   **Providers**: These *find* potential hiding spots. Think of them as the AI's "eyes" looking for places to go.
*   **Scorers**: These *rate* the spots found by the providers. They help the AI "decide" which spot is the best.

**Example Setup for a Tactical AI:**

1.  **Add Providers**: Under the `Providers` list, click the `+` icon. Add `BehindObstacleProviderSO` to find spots behind walls and `CurrentPositionProviderSO` to make the AI stable.
2.  **Add Scorers**: Under the `Scorers` list, click `+`. Add scorers to define the behavior.
    *   **`VisibilityScorerSO`**: To make the AI prefer spots the enemy can't see.
    *   **`PathSafetyScorerSO`**: To make the AI avoid running through the open.
    *   For each scorer, you can set a **Weight**. This tells the system how important that rule is. For a tactical AI, `Visibility` and `PathSafety` should have the highest weights.

![Configure Providers and Scorers](https://i.imgur.com/your-image-placeholder.png)

---

### Step 4: Hooking into Events (Optional)

The `EnemyHider` has UnityEvents that let you know what's happening. You can use these to trigger animations, sounds, or other effects without any code.

*   **On Search Started**: Triggers when the AI begins looking for a spot.
*   **On Search Success**: Triggers when a spot is found.
*   **On Search Failed**: Triggers when no spot could be found.

You can drag other components or GameObjects into these event slots and call their public methods, just like a UI Button's `OnClick()` event.

### Step 5: Triggering the Action

The `EnemyHider` needs to be told *when* to hide. A programmer must call the `RetreatToHide()` function from another script. Work with your team's programmer to decide on the right conditions to trigger this action (e.g., when the AI's health is low, when it's being aimed at, etc.). The AI will then use the rules you've designed to find the perfect spot!

---

### Step 6: Validate Your Setup (No Programmer Needed!)

You don't need to ask a programmer if your scene or layers are configured properly. Open the **Environment & Agent Validator**:

* Go to **Tools > Maharaja Studio > Tactical AI > Windows > Environment & Agent Validator** (or click **"Inspect in Validator"** on the agent component in your Inspector).
* Click **Scan Scene**.
* The validator will check your NavMesh, ensure your agents aren't accidentally occluding themselves, check that all placed cover nodes and zones are valid, and catch dead scorers.
* If any issues show up, simply click **Auto-Fix All** to fix them automatically.

📖 **Learn More**: Read the complete **[Scene Validator Guide](../SceneValidatorGuide.md)** for a full list of checks and tips.