# Scorer: Stalemate Breaker

**`StalemateBreakerScorerSO`** is a behavioral scorer designed to prevent "camping." It detects if an agent has been sitting in one spot for too long and dynamically increases the value of flanking positions to force movement.

## How It Works

This scorer introduces the concept of "Boredom" to the AI.

1.  **Check Boredom:** It checks the `TimeInCover` property of the agent.
    * If the time is less than `Boredom Threshold`, the agent is "content," and the scorer returns a neutral **0.5**.
2.  **Calculate Flank Urgency:** If the agent is "bored" (time > threshold), the scorer aggressively seeks movement.
3.  **Geometric Analysis:** It compares the direction to the Enemy vs. the direction to the Candidate Spot.
    * It uses the **Dot Product** to determine the angle.
    * **High Reward:** Lateral movements (moving sideways relative to the enemy). This is a "Flank".
    * **Low Reward:** Moving directly forward (aggressive) or backward (retreat) is rewarded less than flanking in this specific scorer.
4.  **Scaling:** The score is multiplied by a `Boredom Factor`. The longer the agent sits, the higher the score for flanking becomes, eventually overriding safety concerns to force a move.

## Parameters

* **Boredom Threshold**: The time (in seconds) the agent must sit in cover before this scorer activates.
* **Flank Urgency**: A multiplier that determines how desperately the agent wants to flank once bored. Higher values create more aggressive, restless AI.

## Use Cases

* **Anti-Camping**: Prevents AI from finding one "perfect" spot and staying there forever, which is boring for the player.
* **Dynamic Flow**: Creates a rhythm to combat where AI takes cover, shoots for a while, and then naturally decides to rotate to a new angle.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. It relies on accessing the `TimeInCover` property from the `TacticalAgent` instance provided in the context.