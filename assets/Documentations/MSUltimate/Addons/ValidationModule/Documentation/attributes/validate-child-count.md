# [ValidateChildCount]

> Validates that a referenced GameObject's direct child count falls within specified minimum and maximum bounds.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateChildCount]` inspects referenced `GameObject` or `Component` fields. It counts the target object's direct child transforms (`transform.childCount`) and asserts that the count satisfies required minimum (`MinChildren`) and maximum (`MaxChildren`) bounds. It supports including or excluding inactive child GameObjects via `IncludeInactive`.

**The Problem:**
In modular game architecture, many gameplay entities rely on strict child hierarchy structures. For instance, a 4-player spawn container must have exactly 4 spawn nodes; a weapon socket must have at least 1 muzzle transform; or an inventory UI row must not exceed 8 slot items. When level designers accidentally add too few or too many child nodes, systems break silently or crash with `IndexOutOfRangeException` at runtime.

**The Solution:**
Decorating reference fields with `[ValidateChildCount]`:
- **Hierarchy Boundary Enforcement:** Enforces strict min/max limits on child transform counts directly in the Inspector.
- **Support for Inactive Children:** Toggle `IncludeInactive = false` to evaluate only actively enabled child GameObjects.
- **Informative Error Messages:** Displays an immediate, formatted alert banner whenever the child count falls outside valid parameters.
- **Prevents Structural Defects:** Protects procedural spawner rigs, vehicle wheel hierarchies, and UI container layouts from structural corruption.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class SpawnGridManager : MonoBehaviour
{
    [ValidateChildCount(4, 4, "Spawn container must have exactly 4 child spawn points.")]
    public GameObject spawnPointsContainer;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ValidationModule Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Inspector & Validation Engine Window |
| **Validation Interface** | `IValidationAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateChildCountAttribute(int minChildren, int maxChildren, string message = null)
```

- **`minChildren`** (`int`): Minimum acceptable direct child count.
- **`maxChildren`** (`int`): Maximum acceptable direct child count.
- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinChildren` | `int` | `0` | Minimum acceptable direct child count. |
| `MaxChildren` | `int` | `int.MaxValue` | Maximum acceptable direct child count. |
| `IncludeInactive` | `bool` | `true` | When true, includes inactive child GameObjects in the total count. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message box. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error message. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background banner color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Vehicles
{
    public class QuadBikeRig : MonoBehaviour
    {
        [Header("Wheel Hierarchies")]
        [ValidateChildCount(4, 4, "Wheel container must have exactly 4 child wheel sockets.",
            IncludeInactive = true,
            MessageType = InspectorMessageType.Error)]
        public Transform wheelSocketContainer;

        [Header("Passenger Seats")]
        [ValidateChildCount(1, 2, "Vehicle must support 1 to 2 passenger seat mount transforms.")]
        public GameObject seatContainer;

        public void InitializeVehicle()
        {
            // Guaranteed safe child iteration
            for (int i = 0; i < wheelSocketContainer.childCount; i++)
            {
                Transform wheel = wheelSocketContainer.GetChild(i);
                // Setup wheel physics
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateChildHasComponent]`** | High | Combine child count bounds with required component presence on those children. |
| **`[ValidateChildTag]`** | High | Ensure children not only match count constraints, but also carry the required tag. |
| **`[Required]` / `[NotNull]`** | High | Guarantee the container reference is assigned before counting its children. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
