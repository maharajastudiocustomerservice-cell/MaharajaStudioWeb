# Scorer: Flank Exposure Risk (360° Open Angles)

**`FlankExposureRiskScorerSO`** is a defensive and survival scorer that measures how exposed a spot is to ambient sightlines from all 360 degrees. It rewards spots safely tucked into deep corners and wall recesses while penalizing spots out in the open that could be flanked from unmonitored angles.

```
       [ Deep Corner Spot ]                     [ Open Field Spot ]
       ═══════════════════                      
       ║  ● (3 angles blocked)                         ● (8 angles open)
       ║                                        
       Score: 0.88 (High Security)              Score: 0.00 (High Risk)
```

## How It Works

1. Casts a series of radial rays in a full circle around the candidate position at `heightOffset` (waist/chest level).
2. For each angle, checks if a solid occluding wall is present within `scanRadius` (`EffectiveOccluderMask`).
3. Counts the number of open angles where the ray cast found no solid obstacle.
4. **Scoring Calculation:**
   $$\text{Exposure Ratio} = \frac{\text{Open Angles}}{\text{Ray Count}}$$
   $$\text{Score} = 1.0 - \text{Exposure Ratio}$$
   * A spot in the open with all rays unblocked receives `0.0`.
   * A spot with walls blocking multiple sides receives high values (e.g. `0.75` - `1.0`).

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `scanRadius` | `float` | `10.0` | Distance in meters to scan for protecting walls or barriers. |
| `rayCount` | `int` | `8` | Number of radial rays cast around the 360° circle (e.g. 8 rays = 45° intervals). |
| `heightOffset` | `float` | `1.0` | Vertical offset above the candidate ground point (simulating torso/eye level). |

## Use Cases

* **Corner Hugging & Room Clearing:** Encourages AI to clear rooms and tuck themselves into corners with minimal exposed flanks.
* **Open Map Navigation:** Prevents AI from taking "cover" behind a single skinny pole in the middle of a wide open field.
* **Stealth & Defensive Anchors:** Essential for defensive roles, guards holding strongpoints, and survivalist behaviors.

## Performance & Optimization

* **Computational Cost:** **Moderate**. Performs `rayCount` (default: 8) short raycasts per candidate.
* **LOD Awareness:** Automatically scales well when paired with LOD settings that lower candidate counts at greater distances from the player.
