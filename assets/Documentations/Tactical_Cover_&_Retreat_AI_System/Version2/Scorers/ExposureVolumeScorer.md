# Scorer: Exposure Volume

**`ExposureVolumeScorerSO`** calculates how "exposed" a candidate spot is to the open world. Unlike visibility checks (which check against specific enemies), this checks against empty space. It prevents the AI from choosing spots that are technically hidden from the current enemy but are otherwise wide open (e.g., the middle of a courtyard).

## How It Works

This scorer creates a 360-degree "safety profile" of the spot.

1.  **Radial Sampling:** It casts a specified number of rays (`Samples`) in a circle around the candidate spot at waist height.
2.  **Open Space Detection:** For each ray, it checks if it hits any geometry within `Check Distance`.
    * **Hit:** The direction is "Closed/Safe."
    * **No Hit:** The direction is "Open/Exposed."
3.  **Ratio Calculation:** It calculates the ratio of Open rays to Total rays.
    * A spot in an open field (0 hits) gets a high exposure ratio -> **Low Score**.
    * A spot in a tight alley (many hits) gets a low exposure ratio -> **High Score**.

## Parameters

* **Samples**: The number of rays to cast (e.g., 8 or 16). Higher values are more accurate but more expensive.
* **Check Distance**: How far the ray must travel without hitting anything to be considered "Open."

## Use Cases

* **General Survival**: The most robust "default" behavior for avoiding open areas.
* **Corridors vs. Halls**: Biases the AI towards tighter spaces where they are less likely to be sniped from unknown angles.
* **Avoiding "Skylining"**: Prevents AI from standing on top of ridges or hills where they are visible against the sky.

## Performance

**Scalable.** The cost is directly proportional to the `Samples` parameter. 8 samples is usually sufficient for good results without heavy performance impact.