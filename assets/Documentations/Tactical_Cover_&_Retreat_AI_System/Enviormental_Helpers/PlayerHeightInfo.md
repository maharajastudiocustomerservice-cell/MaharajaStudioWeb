# Feature Guide: PlayerHeightInfo

The PlayerHeightInfo component is a simple but powerful tool that allows you to specify the `eye height` of individual player characters. This is essential for creating varied gameplay scenarios where players might have different character models, stances (`crouching`, `prone`), or even be children or large monsters.
The AI system will use this information to perform highly accurate line-of-sight (LOS) checks, making it smarter and more reactive to the actual tactical situation.

## Why Use It?

*  **Accurate Visibility:** If a player is crouching, the AI will correctly understand that they can't see over certain obstacles.
*  **Support for Different Characters:** Allows for players of different sizes (e.g., a tall robot vs. a small goblin) to be evaluated correctly.
*  **Dynamic Stances:** Works perfectly with player controllers that allow crouching or going prone. By changing the currentEyeHeight value at runtime, you can make the AI's perception dynamically adapt to the player's actions.

## Setup Guide

1. Select your Player Prefab or the player character GameObject in your scene.
2. Click Add Component and search for PlayerHeightInfo. Add the script.
3. That's it! The AI system will now automatically detect and use this component.

## Parameters

*  **currentEyeHeight (float):** The most important field. This value represents the height of the player's "eyes" or camera, measured in meters from the GameObject's transform origin (pivot).
*  **Default Value:** 1.7 (a reasonable height for an average standing adult).
*  **Runtime Changes:** If you have a player controller script, it can get a reference to this component and change this value when the player crouches or stands up. The AI will immediately use the new value in its next calculation.

## Example: Integrating with a Player Controller

Here is a small code snippet showing how a player's script might update this value.

```CSharp
// In your PlayerController.cs or similar script

public PlayerHeightInfo playerHeight; // Assign this in the Inspector
public float standingHeight = 1.7f;
public float crouchingHeight = 0.9f;

void OnCrouch()
{
    // When the player crouches, update the height info.
    playerHeight.currentEyeHeight = crouchingHeight;
}

void OnStandUp()
{
    // When the player stands up, set it back.
    playerHeight.currentEyeHeight = standingHeight;
}
```

If a player GameObject does not have this component, the AI will gracefully fall back to using the default playerEyeHeight value defined in your HidingSettingsSO asset for that player.
