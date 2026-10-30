# [ImpactRecoil]

> Snaps the inspector field backward with physical recoil kick displacement upon value changes, recovering smoothly via simulated spring physics.

---

## 1. Overview & Value Proposition

**What it does:**
`[ImpactRecoil]` delivers punchy physical feedback inside the Unity Inspector whenever a field's value changes. It simulates a mechanical or ballistic recoil kick by displacing the entire field horizontally (`RecoilPixels`) instantly upon value mutation, then smoothly interpolating back to rest over a configurable recovery duration (`RecoveryDuration`) using damped kinetic restitution.

**The Problem:**
Tweaking combat weapon stats, ammunition counters, impact forces, or damage multipliers in the default Unity Inspector feels passive and disconnected from physical impact. Designers cannot easily perceive when rapid mutations or automated gameplay balance scripts fire during Play Mode tests.

**The Solution:**
Decorating numeric or state fields with `[ImpactRecoil]`:
- **Tactile Kinematic Feedback:** Visually "kicks" the UI field backward upon each value delta, mimicking weapon slide cycles and heavy mechanical switches.
- **Directional Recoil Control:** Choose leftward (`RecoilLeft = true`) or rightward kick directions to match visual layout semantics and HUD alignments.
- **Customizable Restitution Curve:** Adjust recovery duration (`RecoveryDuration`) and displacement distance (`RecoilPixels`) for anything from subtle micro-kicks to violent shotgun blasts.
- **Zero Runtime Overhead:** Implemented via hardware-accelerated UI Toolkit transforms and tween scheduling that idles at 0% CPU when values are resting.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class WeaponMechanics : MonoBehaviour
{
    [ImpactRecoil(recoilPixels: 10f, recoveryDuration: 200f)]
    public int currentAmmoCount = 30;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property (`int`, `float`, `Vector3`, `bool`, etc.) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ImpactRecoilAttribute(float recoilPixels = 8f, float recoveryDuration = 250f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `recoilPixels` | `float` | `8f` | Displacement distance in pixels for the initial recoil kick. |
| `recoveryDuration` | `float` | `250f` | Duration in milliseconds to recover smoothly from the recoil displacement. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RecoilPixels` | `float` | `8f` | Peak displacement distance in pixels during the initial kick. |
| `RecoveryDuration` | `float` | `250f` | Recovery transition duration in milliseconds back to the resting position. |
| `RecoilLeft` | `bool` | `true` | Direction of recoil; kicks left if `true`, or right if `false`. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class HeavyArtilleryTurret : MonoBehaviour
{
    [Header("Ballistic Weapon State")]
    [ImpactRecoil(
        recoilPixels: 14f, 
        recoveryDuration: 300f, 
        RecoilLeft = true
    )]
    public int chamberedRounds = 6;

    [Header("Impulse Force")]
    [ImpactRecoil(recoilPixels: 8f, recoveryDuration: 180f, RecoilLeft = false)]
    public float kineticImpulseNewtons = 4500f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Recoil translates the internal visual element smoothly within bounded group containers. |
| `[FloatUpDeltaNumber]` | Stacking | Pairs with floating numbers to show numeric deltas while the field physically recoils. |
| `[ValueChangeFlash]` | Stacking | Combines chromatic border flashing with kinematic kickback for intense feedback. |
