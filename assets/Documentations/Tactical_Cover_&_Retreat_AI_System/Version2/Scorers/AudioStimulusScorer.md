# Scorer: Audio Stimulus

**`AudioStimulusScorerSO`** is a strategic scorer that influences the AI to investigate or move toward interesting events (Stimuli) in the world, such as gunshots, explosions, or footsteps.

## How It Works

This scorer connects the hiding system to a global event system (`StimulusRegistry`).

1.  **Fetch Stimuli:** It retrieves a list of recent events from the `StimulusRegistry`.
2.  **Filter:** It ignores any stimuli that are "stale" (older than 5 seconds) or outside the agent's `Hearing Range`.
3.  **Evaluate:** For the candidate spot, it calculates the distance to the relevant sound.
4.  **Score:**
    * It calculates a score based on proximity: `1.0 - (Distance / HearingRange)`.
    * Closer spots get higher scores, effectively pulling the agent toward the source of the noise.
    * It returns the highest score found among all valid stimuli.

## Parameters

* **Hearing Range**: The maximum distance (in meters) at which the agent can "hear" or care about a stimulus.

## Use Cases

* **"Third Partying"**: In a battle royale or free-for-all scenario, this draws AI agents toward ongoing firefights.
* **Investigating**: If a player knocks over a physics object, this scorer can override standard cover logic to make the AI move toward the noise source to investigate.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. It accesses the static `StimulusRegistry` and `Time.time`, which are generally not safe or accessible within Burst jobs.
* **Requirement:** Requires an external system populating `StimulusRegistry.RecentStimuli`.