# Scorer: Defensive Position Bonus

**`DefensivePositionScorerSO`** is a powerful scorer that provides "inertia" or a defensive bonus. It evaluates the agent's **current position** to determine if it's safe, making the AI less likely to abandon a good spot and more likely to flee a compromised one.

## How It Works

This scorer is unique because it only cares about one specific candidate: the one that represents the agent's current location. For all other candidate spots, it returns a score of 0.

When it evaluates the agent's current position, it performs a critical check:

1.  **Is the agent currently visible to any player?** It uses the `IVisibilityService` to check if the agent can be seen from its current spot.

2.  The result of this check leads to one of two extreme outcomes:
    *   **If VISIBLE:** The agent's cover is blown. The scorer returns `float.NegativeInfinity`. This is a powerful penalty that effectively disqualifies the current position, forcing the AI to choose a different hiding spot. It creates a strong "get to cover!" instinct.
    *   **If NOT VISIBLE:** The agent is safe. The scorer returns the small, positive `inertiaBonus`. This gives a slight advantage to staying put, ensuring the AI won't move to a new spot unless it's significantly better than the one it's already in. This prevents fidgety, unnecessary movement.

## Parameters

*   **Weight**: Determines the influence of this scorer. Because it can return `NegativeInfinity`, its penalty effect is absolute regardless of weight. The weight primarily affects how influential the `inertiaBonus` is when compared to scores from other active scorers.
*   **Acceptance Radius**: A small radius to determine if a candidate point is close enough to be considered the agent's current position.
*   **Inertia Bonus**: The small score bonus (e.g., 0.1 or 0.2) applied if the agent is currently safe. This value should be kept relatively low.

## Use Cases

*   **Creating Stable AI**: This is the primary solution for preventing AI from constantly shuffling between two or more hiding spots that have very similar scores. The inertia bonus makes them "prefer" to stay still.
*   **Intelligent Cover Response**: This scorer is essential for creating AI that reacts believably to being discovered. The moment it becomes visible, its top priority will be to move to a new, safer location.
*   **Establishing a Defensive Baseline**: It should be included in most configurations to create a base level of intelligent self-preservation.

## Note

* Chose the parameters value and weight in the HidingSetting for this scorer very carefully because it's very sencitive one and a wrong weight for this scorer may cause the agent will never move. so try to give it's weight as low as possible like 0.1 or less than 0.1


## Performance and Dependencies

This scorer's performance is excellent. It only performs its main logic (the visibility check) for a single candidate spot per evaluation cycle.

*   It is highly dependent on a correctly configured **`IVisibilityService`**.
*   It is designed to be used with the **`CurrentPositionProviderSO`**, which ensures that the agent's current position is always included in the list of candidates to be evaluated. Without this provider, the `DefensivePositionScorer` will do nothing.