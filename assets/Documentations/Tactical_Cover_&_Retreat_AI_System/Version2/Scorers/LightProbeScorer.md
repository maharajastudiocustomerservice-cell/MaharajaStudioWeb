# Scorer: Light Probe (Shadows)

**`LightProbeScorerSO`** is a stealth-oriented scorer that leverages Unity's baked or dynamic Global Illumination (GI) data. It allows agents to detect and prioritize dark areas, such as shadows cast by static geometry.

## How It Works

This scorer queries the scene's lighting data directly.

1.  **Probe Query:** It calls `LightProbes.GetInterpolatedProbe` at the candidate position. This returns the lighting information (Spherical Harmonics) for that specific point in space.
2.  **Luminance Calculation:** It estimates the average brightness (Luminance) from the probe data.
3.  **Score:**
    * **1.0 (Stealthy):** If the brightness is 0 (Pitch Black).
    * **0.0 (Exposed):** If the brightness exceeds the `Darkness Threshold`.
    * **Gradient:** Scores linearly between 0 and the threshold.

## Parameters

* **Darkness Threshold**: The brightness value (approx 0.0 to 1.0+) above which a spot is considered "too bright" and receives 0 score.

## Use Cases

* **Stealth Games**: AI can hide in the shadows of buildings or trees.
* **Night Missions**: AI will stick to unlit alleyways rather than walking under streetlights.

## Performance and Dependencies

* **Thread Safety:** **Main Thread Only**. `LightProbes` API is not thread-safe.
* **Cost:** Low. Interpolating a light probe is very fast compared to raycasting.