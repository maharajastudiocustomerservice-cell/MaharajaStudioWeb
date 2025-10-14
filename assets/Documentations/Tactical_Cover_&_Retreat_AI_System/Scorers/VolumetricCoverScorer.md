# Scorer: Volumetric Cover

VolumetricCoverScorerSO scores candidate spots based on their concealment inside "soft cover" volumes like smoke clouds, dense fog, or magical darkness. This teaches the AI to use visual obstruction to its advantage.

## How It Works

This system is designed to complement the standard visibility system, which only understands solid objects. It uses a VolumetricCover component, which should be placed on objects like smoke cloud prefabs. These components register themselves with a VolumetricCoverRegistry.
The VolumetricCoverScorer evaluates a candidate spot that the normal visibility system considers "exposed." For each such spot, it performs its own line-of-sight check. It casts a ray from the player's eyes to the candidate spot. Then, it checks if that ray intersects with any active VolumetricCover collider.

* If the spot is exposed to the normal system, but the line of sight is blocked by a volumetric cover, it means the AI can use that smoke cloud to hide. The spot receives a high score (1.0).
* If the spot is exposed and not blocked by any soft cover, it is truly a bad spot and receives a low score (0.0).
* If the spot is already hidden behind a solid wall (according to the normal system), this scorer returns a neutral score (0.5), as it doesn't need to add its own input.

## Setup

* On your smoke grenade prefab, fog effect, etc., add a collider (e.g., SphereCollider or BoxCollider) that approximates its volume. Mark it as a Trigger.
* Add the new VolumetricCover component to this GameObject.
* Create an instance of the VolumetricCoverScorerSO asset.
* Add this scorer asset to the Scorers list in your HidingSettingsSO and give it a positive weight (e.g., 1.0 - 1.5).

## Use Cases

*  **Tactical Gameplay:** Allows AI to intelligently use smoke grenades (either its own or the player's) to break line of sight and maneuver.
*  **Environmental Storytelling:** You can fill a swamp with VolumetricCover fog volumes, and the AI will naturally understand that it can use the fog to hide and ambush the player.
*  **Magic Systems:** Perfect for spells that create fields of magical darkness or obscuring mist.