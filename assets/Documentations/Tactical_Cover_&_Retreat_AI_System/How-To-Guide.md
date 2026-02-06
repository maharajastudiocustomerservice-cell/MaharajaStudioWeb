# How-To Guides (The Cookbook)

This section provides practical, goal-oriented recipes for creating common AI behaviors.

### Recipe: The Cautious Marksman

**Goal**: An AI that tries to stay as far away from the player as possible and heavily prioritizes safety.

**Ingredients**:
*   A `HidingSettings` asset named `Marksman_Settings`.
*   Providers: `BehindObstacleProviderSO`, `CurrentPositionProviderSO`.
*   Scorers: `DistanceScorerSO`, `VisibilityScorerSO`, `PathSafetyScorerSO`.

**Method**:
1.  In your `Marksman_Settings` asset, add the providers listed above.
2.  Add the scorers with the following weights:
    *   **`DistanceScorerSO`**: `Weight: 3.0` (This is the highest priority. The AI desperately wants to be far away).
    *   **`VisibilityScorerSO`**: `Weight: 2.0` (Being unseen is very important).
    *   **`PathSafetyScorerSO`**: `Weight: 2.0` (The path to the safe spot must also be safe).

**Result**: When this AI hides, it will consistently choose valid cover points near the maximum edge of its search radius.

---

### Recipe: The Aggressive Flanker

**Goal**: An AI that prefers to hide in locations that create a crossfire angle with its allies, getting into an advantageous flanking position.

**Ingredients**:
*   A `HidingSettings` asset named `Flanker_Settings`.
*   Providers: `NavMeshRingProviderSO`, `BehindObstacleProviderSO`.
*   Scorers: `CrossfireScorerSO`, `VisibilityScorerSO`, `ProximityPenaltyScorerSO`.

**Method**:
1.  Configure the `Flanker_Settings` asset.
2.  Set up the scorer weights:
    *   **`CrossfireScorerSO`**: `Weight: 3.0` (The absolute main priority is getting a good angle).
    *   **`VisibilityScorerSO`**: `Weight: 1.5` (The spot should still be hidden).
    *   **`ProximityPenaltyScorerSO`**: `Weight: 1.0` (Ensure it doesn't try to flank from a position that is suicidally close).

**Result**: This AI will ignore spots directly behind it, instead favoring cover that puts it at a 90-degree angle to its allies, relative to the player's position. Make sure to populate the `allies` list on the `EnemyHider` for this to work

**➡️ Next: [Providers Reference](Providers-Reference.md)**
