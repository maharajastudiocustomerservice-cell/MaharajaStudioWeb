# [ValidateStringLength]

> Validates that a string's character length falls within specified minimum and maximum bounds.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateStringLength]` inspects serialized `string` fields and evaluates `string.Length`. It checks whether the string length falls strictly within the inclusive range defined by `MinLength` and `MaxLength`. If the string is shorter than `MinLength` or exceeds `MaxLength`, an informative validation alert banner is rendered directly beneath the field in the Inspector and logged in the Validation Engine report.

**The Problem:**
Strings configured in the Unity Inspector often have strict runtime and backend limits:
- Player handles, character names, and clan tags must satisfy database length schemas (e.g. 3 to 16 characters).
- UI dialogue boxes, item descriptions, and quest tooltips have fixed layout bounds; oversized strings cause ugly text clipping, ellipse overflows, or font scale degradation.
- Serialized identifiers, server keys, or hex color strings require exact or bounded character counts.
Standard Unity provides no native attribute to restrict string lengths, forcing teams to rely on runtime assertion errors or costly bug reports during QA.

**The Solution:**
Decorating string fields with `[ValidateStringLength]`:
- **Dual Bounds Enforcement:** Guarantees strings satisfy both lower and upper length thresholds (`minLength` and `maxLength`).
- **Prevents UI Text Overflows:** Catch oversized dialogue lines or item titles before they break UI canvas boundaries.
- **Backend Schema Compliance:** Ensure configuration data strictly matches database constraints and network packet sizes.
- **Configurable Severity:** Set severity to `Warning` for soft guidelines or `Error` for mandatory constraints.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class UserProfileConfig : MonoBehaviour
{
    [ValidateStringLength(3, 16, "Username must be between 3 and 16 characters long.")]
    public string username = "Player1";

    [ValidateStringLength(0, 140, "Bio text cannot exceed standard 140 characters.")]
    public string bioDescription = "Ready for adventure!";
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
public ValidateStringLengthAttribute(int minLength, int maxLength, string message = null)
```

- **`minLength`** (`int`): Minimum acceptable string length (inclusive).
- **`maxLength`** (`int`): Maximum acceptable string length (inclusive).
- **`message`** (`string`, optional): Custom error message displayed upon failure. When omitted, defaults to `$"String length must be between {minLength} and {maxLength} characters."`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinLength` | `int` | Assigned in constructor | Minimum acceptable character count. |
| `MaxLength` | `int` | Assigned in constructor | Maximum acceptable character count. |
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

namespace ProjectZero.Account
{
    public class NetworkAccountSettings : ModularMonoBehaviour
    {
        [Header("Authentication Credentials")]
        [ValidateStringLength(4, 20, 
            Message = "Account display handle must be between 4 and 20 alphanumeric characters.",
            MessageType = InspectorMessageType.Error)]
        public string accountHandle = "Specter99";

        [Header("Security Token")]
        [ValidateStringLength(8, 32, 
            Message = "Encryption secret key must be between 8 and 32 characters in length.",
            MessageType = InspectorMessageType.Warning)]
        public string encryptionToken = "secret_auth_token_8820";

        [Header("Localization Note")]
        [ValidateStringLength(0, 80, 
            Message = "Dialogue subtitle exceeds standard single-line display limit of 80 characters.",
            MessageType = InspectorMessageType.Info)]
        public string dialogueSubtitle = "Welcome to the grand bazaar, traveler.";
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateRegex]`** | High | Combine with regex patterns to validate both string length and allowed character sets. |
| **`[ValidateIf]` / `[ValidateUnless]`** | High | Conditionally enforce string lengths based on platform or account tier flags. |
| **`[ValidateNotNull]`** | High | Guard against null strings before checking length thresholds. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |

### Collection Cascading & Serializer Matrix

| Collection / Container Type | Supported | Behavior |
| :--- | :---: | :--- |
| **`List<string>`** | Yes | Cascades to validate character count limits on each string element. |
| **`string[]`** | Yes | Cascades to validate character bounds across each array entry. |
| **`AdvancedList<string>`** | Yes | Full element-level validation support with dynamic item reordering. |
| **`SerializableDictionary<K, string>`** | Yes | Validates string lengths when applied to value string elements. |
| **`SerializableNullable<string>`** | Yes | Validates wrapped string length when populated. |
| **`SerializableTuple<...>`** | Yes | Validates string fields within tuple members. |
