# Provider: Advance Cover

**`AdvanceCoverProviderSO`** is an offensive provider designed to generate hiding or cover points that facilitate forward movement towards a specific target or direction. It is the core component for "leapfrogging" or aggressive territory claiming behaviors.

## How It Works

This provider calculates a "Forward" vector using the following priority logic:
1.  **Direction to Last Known Enemy Position:** If the AI remembers where the player was, it prioritizes moving towards that memory.
2.  **Agent Forward:** If no target data exists, it uses the agent's current forward facing direction.

Once the direction is established, the provider generates candidate points within a defined cone (the `Search Angle`) along that vector. Unlike simple movement providers, this system explicitly checks for local cover availability:

1.  **Cone Sampling:** It casts random rays within the search angle.
2.  **Distance Randomization:** It selects a point between 50% and 100% of the `Advance Distance`. This ensures the AI makes significant progress and doesn't pick a spot just 1 meter away.
3.  **Obstacle Validation:** After sampling a valid NavMesh position, it performs a `Physics.CheckSphere` at that location. It only accepts the point if an obstacle is detected nearby (simulating "wall hugging" logic). This ensures the agent moves *to cover*, not just into the open.

## Parameters

* **Advance Distance**: The maximum distance forward the provider will search. The AI will try to move at least 50% of this distance.
* **Search Angle**: The width of the cone in degrees. A narrower angle forces a direct approach; a wider angle allows for diagonal advancement.

## Use Cases

* **Closing the Gap**: Ideal for melee units or shotgun wielders who need to move safely from cover to cover to get into effective range.
* **Leapfrogging**: When used by a squad, agents can take turns suppressing the enemy while others use this provider to advance to the next barricade.
* **Aggressive Patrols**: Allows an AI to push through a level while sticking to walls and obstacles rather than walking down the center of a corridor.

## Performance

**Moderate.** While the math for cone generation is cheap, this provider performs a `Physics.CheckSphere` for every generated candidate to ensure cover exists at the destination. While efficient for standard candidate counts (e.g., 10-20), setting the `Candidates Per Provider` count extremely high in your LOD settings may impact performance.