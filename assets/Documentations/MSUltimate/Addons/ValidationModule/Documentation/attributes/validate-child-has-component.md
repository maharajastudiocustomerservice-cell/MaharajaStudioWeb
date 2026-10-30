# [ValidateChildHasComponent]

> Validates that direct children of a referenced GameObject possess an attached component of the specified type.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateChildHasComponent]` inspects children of an assigned `GameObject` or `Component` reference. It audits child transforms for the presence of a required component type (`RequiredComponentType`). The evaluation scope is controlled via `MatchMode`:
- **`Any`**: At least one direct child must have the component.
- **`All`**: Every direct child must have the component.
- **`Exact`**: An exact number of children (`ExpectedCount`) must have the component.

**The Problem:**
In multi-node game objects (such as weapon mounts, audio emitter clusters, or patrol waypoint loops), systems expect children to hold specific functional components (e.g. `Collider`, `AudioSource`, `WaypointNode`). If an artist adds an empty `GameObject` as a child without attaching the required component, runtime logic iterating over children throws null reference exceptions or fails silently.

**The Solution:**
Decorating reference fields with `[ValidateChildHasComponent]`:
- **Flexible Match Modes:** Configure whether `Any`, `All`, or an `Exact` count of child objects must carry the component.
- **Multiple Attributes Supported:** Supports multiple stacked attributes (`AllowMultiple = true`) to enforce multiple distinct child components.
- **Inactive Child Awareness:** Includes or excludes inactive children via `IncludeInactive`.
- **Immediate Diagnostic Feedback:** Displays a detailed failure notice highlighting the missing component requirement.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class TurretMount : MonoBehaviour
{
    [ValidateChildHasComponent(typeof(Collider), 
        MatchMode = ChildComponentMatchMode.All, 
        message: "Every child barrel must have a Collider attached.")]
    public GameObject barrelsRoot;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ValidationModule Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Window Surface** | Unity Inspector & Validation Engine Window |
| **Validation Interface** | `IValidationAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateChildHasComponentAttribute(Type requiredComponentType, string message = null)
```

- **`requiredComponentType`** (`Type`): The `System.Type` of the component required to exist on the child GameObjects.
- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RequiredComponentType` | `Type` | Assigned in constructor | The component type required to be present on children. |
| `MatchMode` | `ChildComponentMatchMode` | `ChildComponentMatchMode.Any` | Match rule: `Any`, `All`, or `Exact`. |
| `ExpectedCount` | `int` | `1` | Number of children that must own the component when `MatchMode == Exact`. |
| `IncludeInactive` | `bool` | `true` | When true, includes inactive children in the component audit. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message box. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error message. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background banner color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

### `ChildComponentMatchMode` Enum
- **`Any`**: At least one direct child must have the component.
- **`All`**: Every direct child must have the component.
- **`Exact`**: Exactly `ExpectedCount` children must have the component.

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Gameplay
{
    public class AudioClusterEmitter : MonoBehaviour
    {
        [Header("Audio Nodes")]
        [ValidateChildHasComponent(typeof(AudioSource), 
            MatchMode = ChildComponentMatchMode.All,
            IncludeInactive = true,
            Message = "All child sound nodes must have an AudioSource component attached.",
            MessageType = InspectorMessageType.Error)]
        public GameObject speakerContainer;

        [Header("Ambient Lights")]
        [ValidateChildHasComponent(typeof(Light), 
            MatchMode = ChildComponentMatchMode.Exact, 
            ExpectedCount = 3,
            Message = "Lighting container must have exactly 3 child Light components.")]
        public GameObject spotlightPillars;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateChildCount]`** | High | Combine total child count limits with child component existence rules. |
| **`[ValidateChildTag]`** | High | Require both specific tags and attached components on child GameObjects. |
| **`[ValidateChildName]`** | High | Validate naming patterns alongside component presence on children. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
