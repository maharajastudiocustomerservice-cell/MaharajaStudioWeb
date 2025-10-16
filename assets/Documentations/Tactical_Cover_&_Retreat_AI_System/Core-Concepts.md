# Core Concepts: How the System Thinks

Understanding the core architecture will empower you to create truly unique and intelligent AI. The entire system is built on a simple but powerful pipeline.

### The Generate -> Score -> Select Pipeline

Every time you call `RetreatToHide()`, the system performs three main steps:

1.  **GENERATE**: **Providers** scan the world and generate a list of potential hiding spots (`CandidateInfo`). They don't know if a spot is "good" or "bad"; they only know how to find possibilities.
2.  **SCORE**: Each candidate spot is then shown to a list of **Scorers**. Each scorer evaluates the spot based on one specific criterion (e.g., "How visible is it?") and gives it a score.
3.  **SELECT**: The system multiplies each score by its user-defined **Weight** and adds them all up. The candidate with the highest total score is the winner.

This pipeline is what allows for such modular and data-driven behavior.

```mermaid
graph TD
    A[Start Search: RetreatToHide()] --> B{HidingContext Assembled};
    B --> C[1. GENERATE Candidates];
    C --> D(BehindObstacleProvider);
    C --> E(CoverNodeProvider);
    C --> F(...);
    D & E & F --> G[Master List of Candidates];
    G --> H[2. SCORE Each Candidate];
    H -- Candidate 1 --> I{For each Scorer...};
    I -- VisibilityScorer --> J(Score: 0.0 * Weight: 2.0);
    I -- DistanceScorer --> K(Score: 0.8 * Weight: 1.0);
    I -- PathSafetyScorer --> L(Score: 1.0 * Weight: 1.5);
    J & K & L --> M[Total Score for Candidate 1 = 2.3];
    H -- Candidate 2... --> N[...];
    M & N --> O[3. SELECT Candidate with Highest Score];
    O --> P[Return Best HidingSpot];
```

### AI Personality: `HidingSettings` vs. `SearchProfile`

You have two ways to define an AI's behavior:

*   **`HidingSettingsSO` (The Rulebook)**: This is the AI's default "personality." It's a static asset that defines the complete set of providers and scorers the AI uses. You might have a `SniperSettings` asset that prefers high ground and long distances, and a `GruntSettings` asset that prefers staying close to allies.

*   **`SearchProfile` (The "Mood")**: This is a temporary, code-driven override for a single search. It allows you to dynamically change the AI's priorities. For example, when an AI's health is low, you can use a `SearchProfile` to temporarily crank up the weight of the `DistanceScorer` and `PathSafetyScorer`, making it act more desperately and cautiously without changing its base personality asset.

### The Facade Pattern: Keeping Your Code Clean

The `EnemyHider` component acts as a **Facade**. It provides a simple, clean API (`RetreatToHide()`, `IsThreatened`, etc.) that hides the complex machinery underneath. Your AI controller only ever needs to talk to the `EnemyHider`, keeping your game logic decoupled and easy to manage.

**➡️ Next: See practical examples in the [How-To Guides (Cookbook)](4-How-To-Guides.md)**
