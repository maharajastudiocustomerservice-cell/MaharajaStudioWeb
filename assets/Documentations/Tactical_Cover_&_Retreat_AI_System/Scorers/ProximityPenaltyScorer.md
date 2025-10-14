# Scorer: Proximity Penalty

ProximityPenaltyScorerSO scores a candidate based on its raw proximity to the nearest player. It creates a "danger zone" around players, heavily penalizing or disqualifying spots that are too close, regardless of visibility.

## How It Works

This scorer enforces a critical self-preservation behavior by ensuring the AI maintains a safe distance from threats. It doesn't care about cover or line of sight; its only concern is raw distance.
*  **Finds Nearest Threat:** It first calculates the distance from the candidate hiding spot to every player. It only considers the distance to the closest player for its evaluation.
*  **Disqualification Check:** It checks if this distance is within the disqualificationRadius. If it is, the spot is considered suicidally close. The scorer returns float.NegativeInfinity, which instantly removes the spot from consideration, no matter how good other scorers think it is.
*  **Penalty Calculation:** If the spot is outside the disqualification zone but inside the larger dangerRadius, it is considered hazardous. The scorer calculates a penalty that scales linearly.
A spot right on the edge of the dangerRadius will get a score of 1.0 (no penalty).
A spot right on the edge of the disqualificationRadius will get a score of 0.0 (maximum penalty).
*  **Safe Zone:** If the spot is outside of the dangerRadius, this scorer considers it perfectly safe and gives it a full score of 1.0.

## Parameters

*  **Disqualification Radius:** The absolute "no-go" zone. Any candidate spot within this distance of a player will be instantly rejected. This should be a small value representing the agent's immediate personal space (e.g., 2-3 meters).
*  **Danger Radius:** A larger warning zone. Spots within this radius will be penalized. This should be a larger value representing the distance at which the agent starts to feel threatened (e.g., 7-10 meters).

## Use Cases

*  **Essential Self-Preservation:** This is a highly recommended scorer for nearly every configuration. It prevents the AI from making the naive mistake of hiding right next to an enemy.
*  **Enforcing Engagement Ranges:** It stops the AI from retreating to a "hidden" spot that is still within melee or shotgun range of a player.
*  **Creating Skittish AI:** By using a large dangerRadius, you can create AI characters that are more cautious and prefer to keep their distance.

## Performance

This scorer is extremely high-performance. It involves a simple loop and distance calculations (Vector3.SqrMagnitude). Its impact on performance is negligible, and the behavioral improvement it provides is immense.
