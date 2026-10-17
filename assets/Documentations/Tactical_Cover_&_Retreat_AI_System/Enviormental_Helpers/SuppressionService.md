# Service: Suppression Service

**`SuppressionService`** is a runtime helper service and central manager that tracks active bullet trajectories, ballistic streams, and suppressive fire cones in real-time. It enables Tactical AI agents to perceive incoming gunfire and avoid pathing into dangerous lines of fire.

```
 Muzzle Origin
      ▲
      │═══════════════════════════════════════════════════► Direction (length: 50m)
      │ ◄─── radius (1.5m) ───►
      (Active for duration: e.g. 0.8s)
```

## How It Works

* **Singleton Architecture:** Exposes `SuppressionService.Instance` for high-speed, zero-allocation registration from any weapon or projectile script.
* **Temporal Buffer with Auto-Decay:** Stores active suppression cones with expiration timestamps (`Time.time + duration`). Automatically cleans expired cones during its `Update()` cycle.
* **Fast Geometric Cylinder Queries:** `IsPointSuppressed(Vector3 point)` uses vector projection and square-magnitude calculations to test whether a coordinate lies within any active fire cylinder without physics queries or allocations.
* **Editor Debugging Gizmos:** Renders transparent red suppression danger cylinders and wire-spheres in the Scene View when running in the Editor.

---

## Public API Reference

```csharp
namespace MaharajaStudio.TacticalAI.Helper
```

### Methods

#### `RegisterSuppressiveFire`
Registers an active stream of gunfire or incoming bullet trajectory.

```csharp
public void RegisterSuppressiveFire(
    Vector3 origin, 
    Vector3 direction, 
    float length, 
    float radius, 
    float duration
)
```

* **`origin`**: The starting world point of the gunfire (e.g., muzzle position).
* **`direction`**: The normalized aim or firing direction vector.
* **`length`**: The maximum range in meters that the gunfire travels.
* **`radius`**: The danger radius around the bullet stream (spread/threat width).
* **`duration`**: How long (in seconds) the danger zone persists (e.g., `0.3s` for a single shot, `1.5s` for sustained machine-gun fire).

#### `IsPointSuppressed`
Checks if a world position is currently inside any active gunfire cone, explosion, or continuous stream.

```csharp
public bool IsPointSuppressed(Vector3 point)
```
* **Returns:** `true` if the point is within range and within radius of an active fire trajectory; otherwise `false`.

#### `GetSuppressionIntensity`
Calculates aggregated suppression intensity (0.0 to 1.0) and the primary incoming vector bullets are arriving from.

```csharp
public float GetSuppressionIntensity(Vector3 point, out Vector3 incomingFireDirection)
```
* **`incomingFireDirection`**: Out parameter with normalized vector pointing back toward the source of fire, allowing AI to duck behind the safe side of cover.
* **Returns:** Normalized 0.0 to 1.0 suppression intensity with distance falloff.

#### `RegisterExplosiveSuppression`
Registers a spherical blast/shockwave from grenades, mortars, or artillery.

```csharp
public void RegisterExplosiveSuppression(Vector3 epicenter, float radius, float duration, float intensity = 1.0f)
```

#### `RegisterContinuousSuppression`
Registers sustained machine-gun fire from a live weapon muzzle (e.g. mounted turret).

```csharp
public int RegisterContinuousSuppression(Transform muzzleTransform, float length, float radius, float intensity = 1.0f)
public void StopContinuousSuppression(int handle)
```
* **Returns:** An integer handle used to stop the stream when firing ceases.

#### `ClearAll`
Clears all active cones, explosive spheres, and continuous streams.

---

## Integration Example

Call `RegisterSuppressiveFire` whenever weapons fire in your project:

### 1. Raycast Weapons (Instant Hit)
```csharp
using UnityEngine;
using MaharajaStudio.TacticalAI.Helper;

public class HitscanRifle : MonoBehaviour
{
    [SerializeField] private Transform muzzle;
    [SerializeField] private float range = 60f;
    [SerializeField] private float suppressionRadius = 1.5f;
    [SerializeField] private float suppressionDuration = 0.5f;

    public void Shoot()
    {
        // 1. Your weapon logic (Raycast, effects, audio)
        Ray ray = new Ray(muzzle.position, muzzle.forward);
        if (Physics.Raycast(ray, out RaycastHit hit, range))
        {
            // Apply damage...
        }

        // 2. Alert the Tactical AI system of the bullet stream
        if (SuppressionService.Instance != null)
        {
            SuppressionService.Instance.RegisterSuppressiveFire(
                muzzle.position, 
                muzzle.forward, 
                range, 
                suppressionRadius, 
                suppressionDuration
            );
        }
    }
}
```

### 2. Projectile / Physical Bullet Weapons
```csharp
public class HeavyTurret : MonoBehaviour
{
    public void OnBurstFired(Vector3 barrelPos, Vector3 fireDir)
    {
        SuppressionService.Instance?.RegisterSuppressiveFire(
            barrelPos, 
            fireDir, 
            length: 80f, 
            radius: 2.5f, 
            duration: 1.2f
        );
    }
}
```
