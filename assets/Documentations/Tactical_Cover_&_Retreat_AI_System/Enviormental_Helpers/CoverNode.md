# Feature Guide: CoverNode

The `CoverNode` component provides precise, designer-placed cover positions in the world. It guarantees high-priority tactical spots, supports stance tagging (Low/High/Both), edge points, vaultability, destructible health degradation, weapon mounting, and blind-fire points.

## Why Use It?

* **Designer Control:** Guarantees specific strategic locations are evaluated as potential cover, overriding purely procedural generation.
* **Tactical Posture & Stance:** Flags low (crouch) vs. high (stand) cover for animation alignment.
* **Destructible Barriers:** Supports health tracking and damage callbacks; automatically unregisters when destroyed so AI doesn't hide behind rubble.
* **Weapon Mounting:** Exposes exact barrier rest points for bipod or weapon bracing.
* **Blind Fire Offsets:** Computes left, right, and overhead blind-fire offsets for combat systems.

## Setup Guide

1. Create a GameObject at the exact position where the AI should take cover.
2. Add the `CoverNode` script.
3. Align the **Cover Direction** vector (visualized as a cyan arrow in Scene View). The arrow points outwards, away from the protective barrier surface.
4. Select the **Stance** (`Low`, `High`, or `Both`).
5. (Optional) Check **Is Vaultable** if agents can mantle over it, or **Is Destructible** with configured health.

## Parameters & Properties

| Parameter | Type | Description |
|---|---|---|
| `coverDirection` | `Vector3` | Facing normal away from the obstacle. Visualized by cyan gizmo arrow. |
| `stance` | `CoverStance` | Stance requirement: `Low` (crouch), `High` (stand), or `Both`. |
| `isEdgePoint` | `bool` | Flags this point as a corner or edge (ideal for peeking). |
| `isVaultable` | `bool` | Allows AI to vault/mantle over this low obstacle. |
| `isDestructible` | `bool` | Enables health tracking; cover is destroyed when health hits zero. |
| `maxHealth` / `currentHealth` | `float` | Current barrier durability before being compromised. |
| `IsDestroyed` | `bool` | True if destructible and current health <= 0. |

## Public API Reference

```csharp
namespace MaharajaStudio.TacticalAI.Helper
```

### Methods
* **`TakeDamage(float damageAmount)`**: Applies damage to destructible cover. When health reaches zero, fires `OnCoverDestroyed` and automatically unregisters from `CoverNodeRegistry`.
* **`Repair(float amount)`**: Restores cover durability up to `maxHealth` and re-registers the node if repaired above zero.
* **`GetMountingPosition(float eyeHeight = 1.6f)`**: Returns the world coordinates along the top ridge of the barrier to brace or mount a weapon.
* **`GetBlindFirePosition(PeekDirection direction, float lateralOffset = 0.6f)`**: Calculates lateral (Left/Right) or overhead blind-fire positions without exposing the AI's core body.

### Events
* **`OnCoverDestroyed (Action<CoverNode>)`**: Triggered when damage reduces the cover's health to zero.

## Example: Damaging Cover from Gunfire

```csharp
using UnityEngine;
using MaharajaStudio.TacticalAI.Helper;

public class BulletImpact : MonoBehaviour
{
    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.TryGetComponent<CoverNode>(out var cover))
        {
            cover.TakeDamage(25f);
        }
    }
}
```