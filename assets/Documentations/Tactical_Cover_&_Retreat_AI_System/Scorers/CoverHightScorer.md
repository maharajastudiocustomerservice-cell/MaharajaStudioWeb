# Scorer: Cover Height

`CoverHeightScorerSO` evaluates a candidate spot based on the height of the cover in front of it, ensuring the AI does not try to hide behind objects that are too short to conceal it properly.

## How It Works
This scorer adds a layer of intelligence to cover selection by checking not just if there is cover, but if that cover is tall enough. It operates only on candidates that have a coverNormal provided by their generator (like AutomaticCoverProviderSO or BehindObstacleProviderSO).

For a given `candidate spot`, the scorer simulates the agent's head position. It then casts a short ray from just in front of the agent's head directly towards the primary threat (`the player's last known position or current position`).
* If the ray hits an `occluder`, it means there is a solid object at head-level between the agent and the threat. The spot receives a high score (1.0), indicating good, tall cover.
* If the ray does not hit anything, it implies the cover is too low (e.g., a waist-high crate), and the agent's head would be exposed. The spot receives a low score (0.0).
* If a candidate has no coverNormal, the scorer returns a neutral score (0.5) so as not to penalize providers that don't generate this data.

## Parameters
*  **Check Offset:** How far in front of the agent's head to start the raycast. This should be a small value to ensure the check is close to the agent.
*  **Check Distance:** The maximum length of the raycast. This should be short, as it's only meant to verify the immediate cover, not see across the map.

## Use Cases
Realistic Cover Selection: This is a crucial scorer for preventing silly AI behavior, like crouching behind a small rock or a low railing while thinking it's completely hidden.
Enhancing Tactical Realism: In shooters or tactical games, this ensures that AI agents prioritize cover that offers full protection, leading to more believable and challenging encounters.

## Performance
The performance impact of this scorer is very low. It performs a single, very short Physics.Raycast for each candidate that has cover information. In most scenarios, its cost is negligible.