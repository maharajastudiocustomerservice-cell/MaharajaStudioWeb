# [TrackLifetime]

> Tracks instantiate, destroy, and object pooling lifecycle events for components to identify memory leaks and allocation spikes.

---

## 1. Overview & Value Proposition

**What it does:**
`[TrackLifetime]` instruments component classes to automatically record lifecycle telemetry: instantiation timestamps, active duration, destruction events, and object pool recycle cycles (`OnEnable`/`OnDisable`). All tracked instances are monitored in real-time within the Lifetime Track window, with alerts for leaked long-lived instances (`LongLifespanThreshold`) and excessive concurrent population spikes (`PeakAlertThreshold`).

**The Problem:**
Object pooling bugs, lingering references, and runaway `GameObject.Instantiate()` loops are among the most common sources of memory fragmentation and garbage collection stutters in Unity. Standard Unity profilers show generic memory counters without correlating which game subsystem, spawning script, or pooling manager created the unreleased instances.

**The Solution:**
Decorating classes with `[TrackLifetime]`:
- **Automated Lifecycle Profiling:** Measures instance lifetimes from birth to death without writing manual profiling hooks.
- **Pooling & Recycle Metrics:** Toggle `IsPooled = true` to measure spawn/recycle frequencies through `OnEnable` and `OnDisable` rather than standard garbage creation.
- **Spawn Source Stack Tracing:** Captures exact C# call stacks at the moment of creation (`TrackSpawnSource = true`), pinning down exactly which spawner created each object.
- **Peak Population & Leak Guards:** Triggers immediate alerts when concurrent instances exceed limits (`PeakAlertThreshold = 100`) or linger beyond intended lifespans (`LongLifespanThreshold = 30f`).
- **Visual Grouping & Category Tints:** Organize types into distinct categories (`Category = "Enemies"`, `Category = "Projectiles"`) with custom color coding (`ColorHex`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.LifetimeTracker;

[TrackLifetime("Projectiles", "#E74C3C")]
public class PlasmaBolt : MonoBehaviour
{
    public float projectileSpeed = 25f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ToolBox-Vol1 Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Lifetime Track Window & Scene Profiler |
| **Tracking Engine** | `LifetimeTrackManager` |

---

## 4. Constructors & Parameters

```csharp
public TrackLifetimeAttribute()
public TrackLifetimeAttribute(string category)
public TrackLifetimeAttribute(string category, string colorHex)
```

- **`category`** (`string`, optional): Display category name used for grouping types inside the Lifetime Track dashboard.
- **`colorHex`** (`string`, optional): Hex color code applied to graphs, tables, and telemetry pills representing this type.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `string` | `"Uncategorized"` | Grouping category displayed in the Lifetime Track window. |
| `ColorHex` | `string` | `"#7B9FD4"` | Hex color string used to tint this type in tables, sparklines, and timeline charts. |
| `MaxHistory` | `int` | `2000` | Maximum circular buffer size of retained lifecycle events per type. |
| `LogToConsole` | `bool` | `false` | When true, forwards lifecycle threshold anomalies directly to the Unity console. |
| `LongLifespanThreshold` | `float` | `0f` | Lifespan threshold in seconds; instances surviving longer are flagged as potential leaks (0 disables). |
| `PeakAlertThreshold` | `int` | `0` | Peak concurrent instance count threshold; fires an alert if exceeded (0 disables). |
| `TrackSpawnSource` | `bool` | `true` | When true, captures C# stack traces at instantiation to identify spawn originators. |
| `IsPooled` | `bool` | `false` | When true, tracks lifecycle via `OnEnable`/`OnDisable` activation instead of `Instantiate`/`Destroy`. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.LifetimeTracker;

namespace ProjectZero.Weapons
{
    // High-frequency pooled projectile monitored for pool leaks and allocation surges
    [TrackLifetime("Projectiles", "#3498DB",
        IsPooled = true,
        MaxHistory = 5000,
        LongLifespanThreshold = 10.0f,    // Flag projectile if it survives > 10 seconds without despawning
        PeakAlertThreshold = 300,         // Alert if active projectile count breaches 300
        TrackSpawnSource = true,
        LogToConsole = true)]
    public class KineticBullet : MonoBehaviour
    {
        public float damage = 15f;
        public float lifetime = 3.0f;

        private float _aliveTimer;

        private void OnEnable()
        {
            _aliveTimer = 0f;
        }

        private void Update()
        {
            _aliveTimer += Time.deltaTime;
            if (_aliveTimer >= lifetime)
            {
                gameObject.SetActive(false); // Return to pool
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| System / Addon | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[LiveTrack]`** | High | Pair class lifecycle tracking with field-level live telemetry graphs on spawners. |
| **`[ConsoleCommand]`** | High | Use console commands to trigger mass spawning or pool clearance during performance profiling. |
| **Lifetime Track Window** | Native | Automatically populates tables, active entity counts, and lifetime distribution histograms. |
| **Object Pooling Systems** | High | Compatible with Unity 6 `UnityEngine.Pool` and custom studio pooling managers via `IsPooled = true`. |
