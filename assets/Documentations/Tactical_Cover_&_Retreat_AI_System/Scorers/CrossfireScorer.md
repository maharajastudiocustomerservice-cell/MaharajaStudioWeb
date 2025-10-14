# Scorer: Crossfire

`CrossfireScorerSO` evaluates hiding spots based on their potential to create a tactical crossfire with allied units. It rewards spots that provide a flanking angle on the player's position relative to the positions of other AI agents.

## How It Works

This scorer promotes intelligent squad behavior by moving beyond simple grouping. Instead of just huddling together, it encourages agents to spread out and attack from multiple angles.
For a given candidate spot, the scorer does the following:

1. It identifies the primary threat location (the player's last known or current position).
2. It iterates through all of the agent's allies.
3. For each ally, it calculates the angle formed at the player's position between the ally and the candidate spot (ally -> player -> candidate).
4. The scorer finds the maximum angle created among all allies.
5. The final score is based on how close this maximum angle is to the Optimal Angle defined in the asset. An angle of 90 degrees (a perfect "L" shape flank) would receive the highest score, while positions that are directly in line with an ally receive a low score.

## Setup

* Ensure your EnemyHider components have their allies list populated correctly.
* Create an instance of the CrossfireScorerSO asset.
* In the asset's Inspector, configure the Optimal Angle (90 is a good default) and Minimum Angle (e.g., 20, to ignore insignificant angles).
* Add this scorer asset to the Scorers list in your HidingSettingsSO and give it a moderate weight (e.g., 1.0 to 2.0). Its influence should be a significant factor in repositioning decisions.

Use Cases

*  **Advanced Squad Tactics:** The primary use case. Transform a group of AI from a simple mob into a coordinated squad that actively tries to flank and suppress the player.
*  **Making Combat More Challenging:** A crossfire is a difficult situation for a player to deal with. This scorer directly increases the tactical challenge of combat encounters.
*  **Dynamic Encounters:** The AI will dynamically create flanking maneuvers based on the current positions of all units, leading to less predictable and more engaging fights.