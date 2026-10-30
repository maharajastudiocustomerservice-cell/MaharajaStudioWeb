# [ConfettiCannon]

> Launches a celebratory 2D physics-simulated confetti burst across the inspector on button clicks, method invocations, or value changes.

---

## 1. Overview & Value Proposition

**What it does:**
`[ConfettiCannon]` brings dopamine-rich celebratory feedback into the Unity editor by spawning a multi-colored fountain of fluttering 2D confetti particles. The simulation integrates realistic initial velocity (`InitialVelocity`), downward gravity (`Gravity`), rotational aerodynamic flutter, and a timed fadeout lifecycle (`BurstDuration`).

**The Problem:**
Completing long editor tasks—such as baking navmeshes, generating procedural dungeons, verifying level data, or leveling up test characters—often concludes with anti-climactic static console logs or silent field updates. This lacks emotional reward and makes verifying batch operations dull.

**The Solution:**
Decorating methods, buttons, or achievement fields with `[ConfettiCannon]`:
- **Celebratory 2D Physics:** Simulates authentic fluttering paper ribbon physics with gravity and drag right on the editor canvas.
- **Versatile Target Application:** Decorate inspector action methods (`[Button]`), numeric milestone fields, or property setters.
- **Fine-Tuned Particle Dynamics:** Control particle count (`ParticleCount`), launch arc (`InitialVelocity`), gravity pull (`Gravity`), and animation duration (`BurstDuration`).
- **High-Performance Vector Rendering:** Rendered directly using lightweight UI Toolkit custom draw commands, leaving zero residual gameobjects or memory leaks.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class QuestTracker : MonoBehaviour
{
    [ConfettiCannon(particleCount: 50, burstDuration: 1500f)]
    public int questsCompleted = 10;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serializable field, property, method, array (`T[]`), or list (`List<T>`) |
| **Collection Interfaces** | `ICollectionElementAttribute` (Element Cascading) & `ICollectionBatchAttribute` ("🎉" Celebration Header Action) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ConfettiCannonAttribute(int particleCount = 40, float burstDuration = 1200f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `particleCount` | `int` | `40` | Total number of fluttering confetti particles spawned during the burst. |
| `burstDuration` | `float` | `1200f` | Total lifetime of the confetti physics simulation in milliseconds. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ParticleCount` | `int` | `40` | Total count of confetti particles launched. |
| `BurstDuration` | `float` | `1200f` | Duration of the particle celebration simulation in milliseconds. |
| `Gravity` | `float` | `250f` | Downward gravitational acceleration constant applied to the confetti. |
| `InitialVelocity` | `float` | `120f` | Upward launch impulse velocity given to confetti fragments. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class LevelCompletionManager : MonoBehaviour
{
    [Header("Level Progress Milestones")]
    [ConfettiCannon(
        particleCount: 65, 
        burstDuration: 1600f, 
        Gravity = 300f, 
        InitialVelocity = 150f
    )]
    public int currentDungeonFloor = 50;

    [Header("Direct Collections Cascading & Batch Action")]
    [ConfettiCannon(particleCount: 35, burstDuration: 1000f)]
    public int[] milestoneTargetScores = new int[] { 1000, 2500, 5000, 10000 };

    [ConfettiCannon(particleCount: 40, burstDuration: 1200f)]
    public List<string> matchTrophies = new List<string> { "First Blood", "Pentakill" };

    [Header("Developer Actions")]
    [ConfettiCannon(particleCount: 80, burstDuration: 2000f)]
    public void GrantVictoryRewards()
    {
        Debug.Log("Rewards successfully awarded to party!");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Fires festive confetti cannons whenever the editor action button is clicked. |
| `[LevelUpSparkle]` | Stacking | Pairs with level-up stars for complete RPG milestone triumph displays. |
| `[BoxGroup]` | Supported | Particles burst freely across inspector container bounds without clipping artifacts. |

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `T[]` | ✅ Yes | Elements & Collection Header | Individual element edits launch bursts; header displays "🎉" action button. |
| `List<T>` | ✅ Yes | Elements & Collection Header | Interactive header action button triggers celebration across entire list. |
| `AdvancedList<T>` | ✅ Yes | Elements & Collection Header | Compatible with list reordering, adding, and removing items. |
| `SerializableDictionary<K, V>` | ✅ Yes | Dictionary Cells | Value edits trigger local particle fountain. |
| `SerializableNullable<T>` | ✅ Yes | Inner value | Cascades to nullable payload. |
| `SerializableTuple<...>` | ✅ Yes | Tuple cells | Fires particle effect from within tuple row. |

