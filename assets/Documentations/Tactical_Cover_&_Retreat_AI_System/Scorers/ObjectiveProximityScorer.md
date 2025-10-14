# Scorer: Objective Proximity

`ObjectiveProximityScorerSO` scores candidate spots based on their distance and relevance to a mission objective. This makes the AI "mission-aware," preventing it from abandoning a critical location it's supposed to be defending.

## How It Works

This scorer relies on a new static service called ObjectiveService. Your game's own mission scripts are responsible for registering and unregistering objective locations with this service.
The ObjectiveProximityScorerSO asset is configured to care about a specific ObjectiveType (e.g., Defend, Attack).
When scoring a candidate, it finds the nearest objective of the matching type. The scoring logic then rewards proximity:
A spot very close to the objective receives a high score (1.0).
As the distance to the objective increases, the score decreases linearly.
If the distance exceeds the Max Distance setting on the scorer, the score becomes 0.0.
This creates a powerful incentive for the AI to choose cover that keeps it relevant to the mission, adding a crucial layer of tactical intelligence.

## Setup

From your game logic scripts (e.g., a "King of the Hill" manager, a "Bomb Defusal" script), get a reference to the objective's position.
When the objective becomes active, call `ObjectiveService.RegisterObjective(...)`, passing in its position and type.
When the objective is completed or moves, call `ObjectiveService.UnregisterObjective(...)` or `ClearObjectives()`.
Create an instance of the `ObjectiveProximityScorerSO` asset.
Configure its Target Type, Optimal Distance, and Max Distance in the Inspector.
Add this scorer asset to the Scorers list in your HidingSettingsSO and give it an appropriate weight.

## Use Cases

Defensive Scenarios: Essential for AI that needs to guard a flag, control point, or VIP. This scorer will force them to hide near the objective instead of running away.
Offensive Scenarios: By setting the type to Attack, you can encourage AI to select hiding spots that move them progressively closer to their target.
Dynamic Objectives: Works perfectly for objectives that move, as long as your game logic continually updates the objective's position in the ObjectiveService.