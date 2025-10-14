# Scorer: Darkness

**`DarknessScorerSO`** is a very simple scorer that evaluates hiding spots based on the overall ambient light level of the scene. It rewards spots in environments that are generally darker.

## How It Works

This scorer operates on a very simple principle: it reads the scene's global ambient light intensity value from `RenderSettings.ambientIntensity`.

*   If the ambient intensity is high (a bright scene), it returns a low score.
*   If the ambient intensity is low (a dark scene), it returns a high score.

The score is calculated as `1.0f - ambientIntensity`, clamped between 0 and 1.

**Important Note:** This is a **global** scorer. At any given moment, it will return the exact same score for **every single candidate spot** regardless of their position. It does not check for dynamic lights or shadows cast by objects. Its purpose is to give a general "bias" towards darkness for the AI's decision-making process.

## Parameters

*   **Weight**: Determines how much the AI should care about the overall darkness of the scene when choosing a spot. If you want AI to strongly prefer hiding when the level is dark, give this a high weight.

## Use Cases

*   **Time of Day Behavior**: This scorer is perfect for influencing AI behavior based on a day/night cycle. If you change the ambient intensity at runtime to simulate the transition from day to night, this scorer will automatically make your AI more likely to hide during the night.
*   **General "Creature of the Dark" AI**: For AI that should be more active or more likely to take cover in dark levels (e.g., caves, nighttime scenes), this scorer provides a simple and extremely performant way to achieve that.

## Performance

The performance of this scorer is **excellent**. It is one of the fastest scorers available because it only involves reading a single float value from the render settings. Its impact on performance is negligible, making it safe to use in any configuration.