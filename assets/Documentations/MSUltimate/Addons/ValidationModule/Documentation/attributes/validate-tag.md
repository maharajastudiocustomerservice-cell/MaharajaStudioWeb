# [ValidateTag]

> Validates that a string field contains a tag name that is officially defined and registered in the Unity project's Tag Manager.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateTag]` inspects serialized `string` fields intended to store Unity tags. In the editor, it queries `UnityEditorInternal.InternalEditorUtility.tags` to verify that the assigned string matches a tag currently defined in the project's Tag Manager (such as `"Player"`, `"MainCamera"`, `"Enemy"`, or `"Respawn"`). If the string is empty or does not exist in the project tags registry, a validation error banner is displayed.

**The Problem:**
Unity's tagging system relies on magic string literals. Typical pitfalls include:
- A developer mistypes a tag (e.g. typing `"Playr"` or `"Enemies"` instead of `"Player"` or `"Enemy"`).
- A tag is renamed or deleted from the project's Tag Manager, but string fields referencing the old name across hundreds of prefabs silently retain the dead tag string.
- At runtime, calls like `gameObject.CompareTag(targetTag)` or `GameObject.FindWithTag(targetTag)` fail silently or throw runtime exceptions, leading to critical gameplay bugs that are tricky to trace.

**The Solution:**
Decorating tag strings with `[ValidateTag]`:
- **Tags Database Verification:** Checks string values directly against `InternalEditorUtility.tags` in real time.
- **Catches Typographical Errors:** Instantly flags misspelled tag strings as soon as they are typed into the Inspector.
- **Dead Tag Detection:** Alerts teams whenever a tag has been removed from Project Settings while still referenced in prefabs.
- **Eliminates Magic String Runtime Failures:** Ensures runtime tag queries (`CompareTag`, `FindGameObjectsWithTag`) never fail due to invalid tag identifiers.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class TargetDetector : MonoBehaviour
{
    [ValidateTag("Target tag must be registered in the project Tag Manager.")]
    public string targetTag = "Player";
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
| **Validation Interface** | `IValidationAttribute`, `ICollectionElementAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateTagAttribute(string message = "Invalid Unity Tag.")
```

- **`message`** (`string`, optional): Custom error message displayed when the tag does not exist in the project. Default is `"Invalid Unity Tag."`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | `"Invalid Unity Tag."` | Failure explanation displayed in the validation message banner. |
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

namespace ProjectZero.Combat
{
    public class ProximitySensor : ModularMonoBehaviour
    {
        [Header("Targeting Filters")]
        [ValidateTag("Primary target tag must exist in project Tag Manager.", 
            MessageType = InspectorMessageType.Error)]
        public string primaryTargetTag = "Player";

        [ValidateTag("Hostile tag is required for faction threat detection.", 
            MessageType = InspectorMessageType.Warning)]
        public string hostileFactionTag = "Enemy";

        [Header("Exclusion Filter")]
        [ValidateTag("Neutral bypass tag must be valid if specified.")]
        public string neutralBypassTag = "Untagged";

        private void OnTriggerEnter(Collider other)
        {
            if (other.CompareTag(primaryTargetTag))
            {
                // Engage target logic
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateLayer]`** | High | Pair together on actor detectors to enforce both valid layers and valid tags. |
| **`[ValidateChildTag]`** | High | Use `[ValidateTag]` for string variables; use `[ValidateChildTag]` to check child GameObject tags directly. |
| **`[ValidateIf]` / `[ValidateUnless]`** | High | Conditionally validate tag fields based on detection mode or feature switches. |
| **Validation Engine** | Native | Audited automatically during scene-wide and prefab validation batch runs. |

### Collection Cascading & Serializer Matrix

| Collection / Container Type | Supported | Behavior |
| :--- | :---: | :--- |
| **`List<string>`** | Yes | Cascades to validate every tag string in the list against TagManager. |
| **`string[]`** | Yes | Cascades to validate each array item exists in project tags. |
| **`AdvancedList<string>`** | Yes | Full element-level validation support with dynamic item reordering. |
| **`SerializableDictionary<K, string>`** | Yes | Validates tag strings when applied to value elements. |
| **`SerializableNullable<string>`** | Yes | Validates wrapped tag string when populated. |
| **`SerializableTuple<...>`** | Yes | Validates tag string fields within tuple members. |
