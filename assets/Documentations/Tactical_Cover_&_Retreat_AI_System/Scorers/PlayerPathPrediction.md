# Scorer: Player Path Prediction

PlayerPathPredictionScorerSO is a highly intelligent scorer that allows an AI to ambush the player by predicting their future position based on their current movement velocity.

## How It Works

This scorer elevates the AmbushScorer from reacting to the player's past position to anticipating their future actions. It leverages a new PlayerTrackerService to get the player's current velocity.
The scoring logic follows two critical ambush principles:
* Stay Hidden Now: The candidate spot must be hidden from the player's current position. If the AI can be seen while moving into its ambush spot, the ambush fails. This check receives a score of 0.
* See Them Later: The candidate spot must have a clear line of sight to the player's predicted future position. This position is calculated by projecting the player's current velocity forward in time by a set amount (Prediction Time).
* If both conditions are met, the candidate is a perfect ambush spot and receives a high score (1.0). Otherwise, it receives a score of 0.0.

## Setup

* Crucial Step: In the EnemyHider.cs script, you must add one line to the CreateHidingContext method: PlayerTrackerService.Update(players);. This is required to feed the tracker the data it needs. The updated script is provided below.
1. Create an instance of the PlayerPathPredictionScorerSO asset.
2. In the asset's Inspector, set the Prediction Time (e.g., 1.0 to 2.0 seconds, depending on how fast your players move).
3. Add this scorer asset to the Scorers list in your HidingSettingsSO. It works well with a moderate to high weight.

## Use Cases

*  **Creating "Smart" AI:** This is a hallmark of intelligent-feeling AI. It gives the impression that the AI is thinking ahead and outsmarting the player.
*  **Effective Ambushes:** Perfect for stealth games or for AI archetypes like assassins or trappers. The AI will correctly lead its target, hiding behind a corner and preparing to engage as the player sprints past.
*  **Punishing Predictable Player Behavior:** This scorer naturally punishes players who run in straight lines without checking corners, as the AI will be waiting for them.