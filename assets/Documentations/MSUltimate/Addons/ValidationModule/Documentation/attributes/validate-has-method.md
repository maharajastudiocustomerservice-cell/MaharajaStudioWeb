# [ValidateHasMethod]

> Validates that an assigned object reference or attached component contains a public or private method with the specified name.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateHasMethod]` inspects assigned `UnityEngine.Object` or `GameObject` reference fields. It uses reflection to scan the referenced object (or all components on an assigned GameObject) to verify that a method with a designated name (`ExpectedMethodName`) exists. If no matching method is discovered, it renders an immediate validation error banner.

**The Problem:**
In event-driven architectures, reflection triggers, animation event dispatchers, or generic button triggers (such as `UnityEvent`, `SendMessage`, or custom string-based method invocations), developers specify method names as strings. If a target object is replaced with a script that does not implement the expected method, or if a method is renamed during refactoring without updating the inspector reference, events trigger silently with zero execution or log warnings.

**The Solution:**
Decorating target fields with `[ValidateHasMethod]`:
- **Reflection Target Verification:** Asserts that the referenced object implements the required callback method (e.g. `"OnDoorTriggered"`, `"OnPlayerRespawn"`).
- **Refactoring Protection:** Immediately highlights broken string-based bindings when method signatures or names are renamed in code.
- **Works on GameObjects and Components:** Recursively searches all MonoBehaviour components on an assigned GameObject to locate the target method.
- **Custom Error Reporting:** Displays clear messages identifying the missing method name.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class EventTriggerVolume : MonoBehaviour
{
    [ValidateHasMethod("OnVolumeEnter", "Assigned listener must implement 'OnVolumeEnter()'.")]
    public MonoBehaviour eventListener;
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
public ValidateHasMethodAttribute(string expectedMethodName, string message = null)
```

- **`expectedMethodName`** (`string`): The name of the method required to exist on the referenced object or its attached components.
- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ExpectedMethodName` | `string` | Assigned in constructor | Required method identifier name. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error banner. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Interaction
{
    public class InteractiveSwitch : MonoBehaviour
    {
        [Header("Target Dispatcher")]
        [ValidateHasMethod("ExecuteInteraction", 
            message: "Assigned target GameObject must have a component with an 'ExecuteInteraction' method.",
            MessageType = InspectorMessageType.Error)]
        public GameObject interactionTarget;

        [Header("Audio Feedback")]
        [ValidateHasMethod("PlayClickSound")]
        public MonoBehaviour clickAudioHandler;

        public void ActivateSwitch()
        {
            if (interactionTarget != null)
                interactionTarget.SendMessage("ExecuteInteraction", SendMessageOptions.DontRequireReceiver);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[Required]` / `[NotNull]`** | High | Guarantee the reference is assigned before checking method presence. |
| **`[ValidateComponent]`** | High | Combine component existence checks with specific method validation. |
| **`[ValidateInterface]`** | High | Prefer `[ValidateInterface]` for strongly typed contracts; use `[ValidateHasMethod]` for dynamic invocation. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
