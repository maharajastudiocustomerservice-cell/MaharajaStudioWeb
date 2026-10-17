# Service: StimulusRegistry

The **`StimulusRegistry`** is a high-speed, zero-allocation global sensory registry for game events such as Gunshots, Footsteps, Explosions, and Distractions. AI agents and scorers query this registry to investigate noise, take cover from explosions, or react to stealth disturbances.

---

## Why Use It?

* **Stealth & Hearing System:** Allows AI to distinguish between subtle footsteps (`StimulusType.Footstep`) and loud gunfire (`StimulusType.Gunshot`).
* **Distance Attenuation:** Automatically calculates acoustic falloff so agents perceive intensity based on proximity to the disturbance.
* **Filter Queries:** Fast bitmask filtering (`TryGetLoudestStimulus`) lets guards only react to high-threat stimuli during combat while listening for subtle noises in patrol mode.
* **Auto-Decay:** Expired disturbances automatically prune from memory after 10 seconds.

---

## Stimulus Categories

```csharp
[System.Flags]
public enum StimulusType
{
    None = 0,
    Footstep = 1 << 0,
    Gunshot = 1 << 1,
    Explosion = 1 << 2,
    Distraction = 1 << 3,
    VoiceCallout = 1 << 4,
    FoliageRustle = 1 << 5,
    All = ~0
}
```

---

## Public API Reference

```csharp
namespace MaharajaStudio.TacticalAI.Helper
```

### Methods

#### `RegisterStimulus`
Registers a new disturbance in the world with category, travel radius, and intensity.

```csharp
public static void RegisterStimulus(
    StimulusType type, 
    Vector3 position, 
    float radius = 20f, 
    Transform instigator = null, 
    float intensity = 1.0f
)
```

#### `TryGetLoudestStimulus`
Queries the highest intensity stimulus perceived at a given listener coordinate with distance falloff.

```csharp
public static bool TryGetLoudestStimulus(
    Vector3 listenerPosition, 
    float hearingThreshold, 
    out StimulusEvent stimulus, 
    StimulusType filter = StimulusType.All
)
```
* **Returns:** `true` if any disturbance in range exceeds `hearingThreshold`; otherwise `false`.

#### `GetStimuliInRadius`
Populates a caller-provided list with all active stimuli inside a specified sphere.

```csharp
public static void GetStimuliInRadius(
    Vector3 center, 
    float radius, 
    List<StimulusEvent> results, 
    StimulusType filter = StimulusType.All
)
```

#### `Clear`
Purges all recorded disturbances.

---

## Example: Registering Sounds from Player Actions

```csharp
using UnityEngine;
using MaharajaStudio.TacticalAI.Helper;

public class PlayerMovementSound : MonoBehaviour
{
    public void OnFootstepLanded(Vector3 groundPos, bool isSprinting)
    {
        float audibleRadius = isSprinting ? 18f : 6f;
        float intensity = isSprinting ? 0.8f : 0.3f;

        StimulusRegistry.RegisterStimulus(
            StimulusType.Footstep, 
            groundPos, 
            audibleRadius, 
            transform, 
            intensity
        );
    }
}
```
