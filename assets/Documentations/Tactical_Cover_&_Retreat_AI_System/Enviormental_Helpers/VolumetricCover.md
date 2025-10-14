# Feature Guide: VolumetricCover

The `VolumetricCover` component designates a volume of space (like a smoke cloud, dense fog, or thick foliage) as "soft cover." This type of cover provides concealment and can block an AI's line of sight, but it does not physically stop movement or projectiles.

## Why Use It?

*  **Dynamic Gameplay:** Allows the AI to intelligently use temporary cover like smoke grenades.
*  **Richer Environments:** Makes natural environments more tactically interesting by allowing AI to hide in thick bushes or foggy areas.
*  **Enhanced Stealth:** Provides more opportunities for both players and AI to break line of sight and reposition, leading to more dynamic stealth and combat encounters.

## Setup Guide

1. Select the GameObject that represents your soft cover (e.g., a smoke grenade particle effect, a large bush model).
2. Add a Collider component to it (BoxCollider, SphereCollider, etc.) to define its boundaries.
Crucially, check the Is Trigger box on the Collider. This ensures it provides concealment without physically blocking characters.
3. Click Add Component and add the VolumetricCover script.
4. A semi-transparent gray gizmo will be drawn in the Scene View, showing the volume of the soft cover.

## How It Works

This component is used by the VolumetricCoverScorerSO. This scorer has special logic:
* It first checks if a potential hiding spot is visible to any player based on normal, solid geometry.
* If the spot is visible, the scorer then performs another check: it casts a ray from the player to the hiding spot.
* If this ray intersects with the collider of any active VolumetricCover object, the scorer considers the line of sight to be blocked.
* It then returns a high score, effectively turning an otherwise exposed position into a viable hiding spot.