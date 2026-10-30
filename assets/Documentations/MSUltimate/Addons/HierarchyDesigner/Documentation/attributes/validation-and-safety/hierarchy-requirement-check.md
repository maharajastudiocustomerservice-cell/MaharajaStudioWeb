# [HierarchyRequirementCheck]

> Validates required peer components on the same GameObject and displays an immediate alert badge if any are missing.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyRequirementCheck]` audits the GameObject's component stack against a specified list of required component types (`params Type[] requiredTypes`). If any required peer component is absent (e.g. missing `Rigidbody`, `AudioSource`, or `Collider`), it displays an unmistakable warning alert badge in the Hierarchy window displaying which components are missing.

**The Problem:**
While Unity provides the native `[RequireComponent]` attribute, it only adds missing components at the exact moment the script is first attached. If a developer or artist subsequently removes the dependent component, or creates a prefab variant without it, Unity offers no hierarchy-level warning. Missing dependencies then trigger runtime `NullReferenceExceptions` when scripts attempt to call `GetComponent<T>()`.

**The Solution:**
Decorating components with `[HierarchyRequirementCheck]`:
- **Continuous Hierarchy Validation:** Continuously checks for the presence of required component types in real-time.
- **Support for Multiple Dependencies:** Accepts any number of required component types via `params Type[]` (e.g. `typeof(Rigidbody)`, `typeof(Collider)`).
- **Non-Intrusive Workflow:** Unlike `[RequireComponent]`, it does not forcefully instantiate components that might need specialized custom setup, allowing artists to configure dependencies deliberately.
- **Custom Alert Color:** Configurable alert badge color (`AlertColor`) for rapid identification.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyRequirementCheck(typeof(Rigidbody), typeof(Collider))]
public class PhysicsDamager : MonoBehaviour
{
    public float impactForce = 100f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyRequirementCheckRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyRequirementCheckAttribute(params Type[] requiredTypes)
```

- **`requiredTypes`** (`params Type[]`): One or more `System.Type` objects representing the mandatory components that must exist on the host GameObject.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RequiredTypes` | `Type[]` | Assigned via constructor | Read-only array of required component types. |
| `AlertColor` | `string` | `"#FF4757"` | Hex color string for the missing dependency alert badge. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether requirement checking continues evaluating during active Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row renderers. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

namespace ProjectZero.Gameplay
{
    // Interactive audio vehicle requiring NavMeshAgent, AudioSource, and Rigidbody
    [HierarchyRequirementCheck(
        typeof(UnityEngine.AI.NavMeshAgent),
        typeof(AudioSource),
        typeof(Rigidbody),
        AlertColor = "#FF3838",
        XOffset = 6f)]
    public class PatrolDroneAI : MonoBehaviour
    {
        [Header("Patrol Settings")]
        public Transform[] waypoints;
        public float patrolSpeed = 3.5f;

        private UnityEngine.AI.NavMeshAgent _agent;
        private AudioSource _audio;

        private void Awake()
        {
            _agent = GetComponent<UnityEngine.AI.NavMeshAgent>();
            _audio = GetComponent<AudioSource>();
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyMissingScriptDetector]`** | High | Combines missing component requirement validation with broken script file detection. |
| **`[HierarchyTooltip]`** | High | Hover tooltip displays a full breakdown of missing and attached components. |
| **`[HierarchyComponentIcons]`** | High | Visualize attached component icons while validating mandatory requirements. |
| **`[HierarchyTransformWarning]`** | High | Audit physical components while monitoring non-uniform scale warnings. |
