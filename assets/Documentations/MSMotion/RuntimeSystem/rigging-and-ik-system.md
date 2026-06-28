# Rigging & IK System

MSMotion integrates procedural skeletal control with Unity's modern **Animation Rigging package** via the `MSMotionRigController` component. By mapping rigging constraints to abstract string identifiers, the system completely decouples runtime targeting logic from individual character bone structures.

---

## The Decoupling Pattern

Standard IK setups bind gameplay targets directly to specific skeletal transforms, making it difficult to reuse animations across characters with different bone hierarchies. MSMotion solves this with a **Slot-Based Decoupling Pattern**:

1.  **Named Constraints**: In the Inspector, the developer maps a string `Id` (e.g. `"LeftFoot"`, `"LookAtTarget"`) to a specific `IRigConstraint` component on the character (such as a `TwoBoneIKConstraint` or `MultiAimConstraint`).
2.  **Asset Configuration**: The `MSMotionAnimationConfig` defines constraint behaviors by referencing the string `Id` inside its `IKOverrides` list.
3.  **Dynamic Execution**: When the animator plays the config, it requests `MSMotionRigController` to activate the slot. The controller resolves the mapping and drives the target weight, leaving gameplay code to only manage target positions.

This means **the exact same `MSMotionAnimationConfig` asset can play on a giant, a goblin, or a standard hero**, provided each character has registered the correct constraint slots.

---

## Blending & Timing Rules

Each IK override entry (`MSMotionIKEntry`) specifies custom timing parameters:
*   **Target Weight**: The target weight `[0, 1]` to apply to the constraint.
*   **Delay Start**: Number of seconds to wait after the animation starts before starting to blend the IK constraint in.
*   **Delay End**: Number of seconds before the animation ends to start blending the IK constraint out.
*   **Fade In / Fade Out**: Speeds to ramp the constraint weight (falls back to animation fade speeds if set to `0`).
*   **Blend Mode**:
    *   `Override`: Linearly blends towards the target weight, overriding lower layers.
    *   `Additive`: Adds weight on top of lower active solvers (clamped to a max of `1.0`).

---

## Pole Vector Stabilization (Hint Math)

For limbs using a `TwoBoneIKConstraint` (such as arms and legs), rapid movement of the target can cause joints (like knees or elbows) to flip violently. 

`MSMotionRigController` includes a built-in mathematical stabilization solver. If an IK constraint target is set and an IK hint (pole vector) transform is registered:
*   The controller evaluates the bone geometry of the limb (`root`, `mid`, `tip`) every frame.
*   It computes a stable bend normal vector relative to the target's position.
*   It applies a spherical interpolation (Slerp) blending toward the limb's natural rest bend direction.
*   The result is applied directly to the IK hint target, guaranteeing a smooth and natural joint bend direction even near singularity configurations.

---

## Cross-Layer Suppression

If multiple override layers are active simultaneously (for example, a character running while executing a dynamic sword slash), the IK solvers on lower layers should not distort the active upper-body action.

If `_enableCrossLayerSuppression` is enabled:
*   The controller checks the weight of higher layers.
*   If a higher layer is active (weight `> 0.001f`), non-additive, and has an `AvatarMask` that covers the bone driven by a lower layer's IK constraint, the controller reduces the effective blend weight of that lower IK solver proportionally.
*   This prevents lower-layer foot planting or aiming solvers from fighting with upper-body attack clips.

---

## MSMotionRigController API Reference

`MaharajaStudio.MSMotion.Runtime.MSMotionRigController` : `MonoBehaviour`

*Compiles automatically when the `com.unity.animation.rigging` package is present in the project.*

### Methods

#### SetTarget
```csharp
public void SetTarget(string constraintId, Transform target);
```
Assigns a world-space `Transform` target to the specified constraint slot. The target is tracked dynamically every frame.

#### ClearTarget
```csharp
public void ClearTarget(string constraintId);
```
Clears the active target, disabling the constraint.

#### RegisterConstraint
```csharp
public void RegisterConstraint(string id, IRigConstraint constraint);
```
Registers an IK constraint programmatically (useful for procedurally spawned rigs or modular characters). Replaces any existing slot with the same ID.

#### UnregisterConstraint
```csharp
public void UnregisterConstraint(string id);
```
Removes the slot mapping from the lookup table.

#### PauseIK
```csharp
public void PauseIK();
```
Pauses all IK evaluations, locking the current weight levels in place.

#### ResumeIK
```csharp
public void ResumeIK();
```
Resumes dynamic weight and target evaluations.

#### SetCrossLayerSuppression
```csharp
public void SetCrossLayerSuppression(bool enable);
```
Enables or disables automatic weight culling based on higher active layers' masks.

#### GetConstraintWeight
```csharp
public float GetConstraintWeight(string constraintId);
```
Returns the actual final weight `[0, 1]` applied to the constraint component in the current frame.

#### IsConstraintActive
```csharp
public bool IsConstraintActive(string constraintId);
```
Returns true if the constraint is actively being driven by any playing animation layer.

#### GetConstraint
```csharp
public IRigConstraint GetConstraint(string constraintId);
```
Retrieves the underlying Unity `IRigConstraint` interface matching the slot ID (useful for low-level custom modifications).

#### GetRegisteredConstraintCount
```csharp
public int GetRegisteredConstraintCount();
```
Returns the total number of constraint slots currently registered on this rig controller.

---

## Procedural Aiming C# Example

This script Aim-Targets a character's head at a look-at object using a Registered constraint:

```csharp
using UnityEngine;
using MaharajaStudio.MSMotion.Runtime;

public class CharacterAimer : MonoBehaviour
{
    [SerializeField] private MSMotionRigController _rigController;
    [SerializeField] private string _aimConstraintId = "HeadLookAt";
    [SerializeField] private Transform _targetTransform;
    [SerializeField] private float _aimDistanceThreshold = 15f;

    private void Update()
    {
        if (_targetTransform == null) return;

        float distance = Vector3.Distance(transform.position, _targetTransform.position);

        if (distance <= _aimDistanceThreshold)
        {
            // Point the head look-at rig to the target transform
            _rigController.SetTarget(_aimConstraintId, _targetTransform);
        }
        else
        {
            // Outside range, clear targeting so the head returns to animation pose
            _rigController.ClearTarget(_aimConstraintId);
        }
    }
}
```

> **Next Guide**: Learn how to utilize keyframe scale curves and configure Level-of-Detail (LOD) in [Stretch & Scale System](stretch-and-scale-system.md).
