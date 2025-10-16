# Core Engine API Documentation

This documentation covers the internal engine of the AI Hiding System. You will rarely call these APIs directly, as the `EnemyHider` component manages them for you. However, understanding how they work is crucial for deep customization, performance profiling, and debugging.

## The Core Data Flow

At its heart, every search follows this sequence:

1.  The `EnemyHider` gathers all relevant world data.
2.  It packages this data into a single, comprehensive `HidingContext` struct.
3.  This `HidingContext` is sent to one of the two core processors: `SynchronousHidingSystemCore` or `AsyncHidingSystemCore`.
4.  The core processor uses the context to run the **Generate -> Score -> Select** pipeline.
5.  The result, a `HidingSpot` struct, is returned to the `EnemyHider`, which then acts upon it.

---

## 1. Core Data Structures (The "Nouns")

These structs are the lifeblood of the system, carrying information between different stages.

### `HidingContext`

**What is it?**
The `HidingContext` is a comprehensive "snapshot" of the world at the exact moment a search is initiated. It contains all the information that providers and scorers need to make their decisions.

**Why is it important?**
It is the single source of truth for a search operation. By bundling all data together, the system ensures that every provider and scorer is working with the exact same information. It also makes the `Score` and `GenerateCandidates` methods clean and predictable, as they receive all their necessary data in one package.

**Key Properties:**
*   `enemyPosition` / `enemyTransform`: The agent's current location.
*   `players` / `allies`: Lists of all relevant friendly and enemy transforms.
*   `playerLastKnownPosition`: The AI's "memory" of where it last saw a threat.
*   `settings` / `lodSettings`: The configuration assets that define search parameters.
*   `visibilityService`: The service used for line-of-sight checks.
*   `activeProfile`: The temporary `SearchProfile` used for overrides.
*   **Helper Properties (`EffectiveSearchRadius`, etc.):** These automatically resolve whether to use a value from the `settings` or the override `profile`.

---

### `CandidateInfo`

**What is it?**
A `CandidateInfo` is the most basic representation of a potential hiding spot. It is the raw output from a `HideSpotProviderSO`.

**Why is it important?**
This simple, lightweight struct is the common language between all providers and the core system. Providers generate lists of these, and the core system feeds them one-by-one to the scorers for evaluation.

**Key Properties:**
*   `position`: The world-space position of the potential spot.
*   `coverNormal`: The direction pointing *away* from the surface of the cover object. It is `Vector3.zero` if the provider couldn't determine a cover direction (e.g., `NavMeshRingProviderSO`). This normal is crucial for scorers like `DirectionalCoverScorerSO`.

---

### `HidingSpot`

**What is it?**
A `HidingSpot` is the **final, actionable result** of a successful search. It's an enhanced `CandidateInfo` with additional tactical data calculated after the best spot has been chosen.

**Why is it important?**
This is the "mission plan" given back to the `EnemyHider`. It contains not just *where* to go, but *how* to get there safely and what the AI can do once it arrives.

**Key Properties:**
*   `position` & `coverNormal`: The position and cover direction of the winning spot.
*   `canPeekLeft` / `canPeekRight`: Booleans indicating if the AI can lean out from cover for a shot.
*   `peekLeftPosition` / `peekRightPosition`: The world-space positions to move to for peeking.
*   `safePath`: **(Crucial)** A pre-calculated `NavMeshPath`. The `PathSafetyScorerSO` evaluates this path to ensure it's safe. The `EnemyHider` then uses `agent.SetPath()` to follow this exact route, preventing the agent from taking a different, more dangerous route than the one that was scored.
*   `IsValid`: A boolean to check if the spot is valid (i.e., not `HidingSpot.Invalid`).

---

## 2. Core Interfaces & Services

### `IVisibilityService`

**What is it?**
An interface that defines the contract for how the system performs line-of-sight (LOS) checks. `DefaultVisibilityService` is the standard implementation, which uses `Physics.Raycast`.

**Why is it important?**
It centralizes all visibility logic. By using an interface, you could theoretically replace the default physics-based system with something else (e.g., a custom voxel-based visibility grid, a portal-based system) without having to change any of the scorers. The scorers simply ask the service, "Is this point visible?" and get a `true`/`false` answer.

**Key Methods:**
*   `AnyPlayerHasLineOfSight(ctx, point)`: The most common method. Returns `true` if *any* player can see the given point.
*   `InAnyPlayerFOVAndVisible(ctx, point)`: A stricter check that also ensures the point is within a player's Field of View cone.

---

## 3. Core Processors (The "Verbs")

These are the static classes that contain the main logic loop. `EnemyHider` chooses which one to call based on the `ExecutionMode`.

### `SynchronousHidingSystemCore`

**What is it?**
This processor runs the entire **Generate -> Score -> Select** pipeline on the main thread in a single frame.

**How does it work?**
1.  It receives the `HidingContext`.
2.  It loops through all `EffectiveProviders` and collects all `CandidateInfo`s into a single, pooled list.
3.  It then iterates through every candidate. For each candidate, it iterates through every scorer in the `settings`, calculates the raw score, applies the weight, and sums them up.
4.  If a scorer returns `NegativeInfinity`, the candidate is immediately disqualified.
5.  It keeps track of the candidate with the highest score.
6.  Finally, it converts the winning `CandidateInfo` into a `HidingSpot` by calculating the path and peek points.

**API:**
*   `TryFindBestSpot(in HidingContext, out HidingSpot, out float)`: Finds the single best spot.
*   `TryFindTopSpots(in HidingContext, int count, out List<HidingSpot>)`: Finds the top `N` spots, sorted by score.

**When to use it:**
This mode is used by `EnemyHider` for the `Synchronous` `ExecutionMode` and for quick, non-blocking queries like `CanFindHidingSpot()`. It's simpler and easier to debug, but can cause performance issues with many AIs.

---

### `AsyncHidingSystemCore`

**What is it?**
This is the high-performance processor that offloads the most expensive parts of the search (raycasting and scoring) to background worker threads using Unity's C# Job System and Burst Compiler.

**How does it work?**
The process is more complex but significantly faster:

1.  **(Main Thread) Preparation:**
    *   It receives the `HidingContext`.
    *   It generates all `CandidateInfo`s from providers, just like the synchronous core.
    *   **Crucially, it deconstructs all complex objects (like `Transform`) into simple, "blittable" data types (`Vector3`, `float`) and copies them into `NativeArray`s.** This is a requirement for the Job System.
    *   It prepares huge batches of `RaycastCommand`s for every visibility check needed by the scorers (e.g., 3 body points per candidate vs. every player).

2.  **(Worker Threads) Execution:**
    *   It schedules all the `RaycastCommand`s to run in parallel.
    *   It then schedules a custom `ScoreCandidatesJob`. This job receives all the `NativeArray`s of data and the raycast results.
    *   Inside the job, each core of the CPU processes a chunk of the candidates. The scoring logic (for scorers marked with `IMultiThreadedScorer`) is executed here. This code is often Burst-compiled into highly optimized machine code.

3.  **(Main Thread) Finalization:**
    *   The main thread `await`s the completion of the jobs.
    *   Once the jobs are done, it retrieves the raw scores from the `ScoreCandidatesJob`.
    *   It then runs any scorers that were **not** marked as `IMultiThreadedScorer` (like those requiring NavMesh APIs).
    *   Finally, it finds the best score and calculates the final `HidingSpot`, just like the synchronous version.

**API:**
*   `FindBestSpotAsync(HidingContext, CancellationToken)`: Asynchronously finds the single best spot. Returns a `Task` or `UniTask`.
*   `FindTopSpotsAsync(HidingContext, int, CancellationToken)`: Asynchronously finds and returns a list of the top `N` spots.

**When to use it:**
This is the default and recommended mode for production. It ensures that the heavy calculations of the AI have minimal impact on your game's frame rate, allowing for more agents and more complex environments.