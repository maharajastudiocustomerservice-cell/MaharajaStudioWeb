# Scorer: Sensory Stimulus Filter Scorer

**`SensoryTypeScorerSO`** evaluates candidate spots based on their proximity to specific categorized sensory disturbances (`StimulusType`) recorded in the `StimulusRegistry`. It supports both **investigation mode** (seeking noise) and **evasion mode** (fleeing loud gunfire/explosions).

---

## How It Works

1. **Category Filtering:** Uses a bitmask (`targetStimuli`) to isolate specific disturbances (e.g. `Gunshot | Explosion` while ignoring `Footstep`).
2. **Temporal Decay:** Automatically ignores stimuli older than `maxMemoryAge`.
3. **Distance Falloff:** Normalizes the distance from candidate spots to the disturbance within `hearingRange`.
4. **Investigation vs. Evasion:**
   * `investigateMode = true`: Closer spots receive higher scores (useful for guards investigating suspicious noise).
   * `investigateMode = false`: Farther spots receive higher scores (useful for civilians, wounded units, or stealth agents escaping combat).

---

## Inspector Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `targetStimuli` | `StimulusType` | `Gunshot \| Explosion` | Sensory categories to react to. |
| `hearingRange` | `float` | `40f` | Maximum distance to react to sounds. |
| `maxMemoryAge` | `float` | `6f` | Forget disturbances older than this (in seconds). |
| `investigateMode` | `bool` | `true` | True = attracted to noise; False = flees from noise. |
| `minimumIntensity` | `float` (0-1) | `0.15f` | Minimum disturbance volume required to provoke a score change. |
| `neutralScore` | `float` (0-1) | `0.5f` | Baseline score returned when no matching stimuli exist. |

---

## Archetype Presets

### Combat Third-Party / Noise Hunter
* `targetStimuli`: `Gunshot | Explosion`
* `investigateMode`: `true`
* `hearingRange`: `60f`

### Stealth Guard (Patrol)
* `targetStimuli`: `Footstep | Distraction`
* `investigateMode`: `true`
* `hearingRange`: `20f`

### Civilian / Non-Combatant
* `targetStimuli`: `Gunshot | Explosion`
* `investigateMode`: `false` (Evasion Mode)
* `hearingRange`: `50f`
