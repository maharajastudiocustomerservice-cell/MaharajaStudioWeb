# [ValidateRegex]

> Validates that a string field conforms to a regular expression pattern (e.g. semantic versions, GUIDs, identifiers).

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateRegex]` validates string serialized fields against a regular expression pattern (`Pattern`). It executes real-time regex matching as text is typed into the Inspector, rendering an immediate validation error banner if the string value violates the regex structure.

**The Problem:**
In production game architectures, many critical string configurations follow strict syntactic formats: item IDs (e.g. `ITEM_[A-Z]{3}_\d{4}`), localization keys (`UI_MENUS_[A-Z_]+`), hex color codes (`^#([A-Fa-f0-9]{6})$`), or semantic versioning strings (`^\d+\.\d+\.\d+$`). When team members enter strings with typos, illegal characters, or missing segments, backend databases, asset bundles, or API calls fail at runtime.

**The Solution:**
Decorating string fields with `[ValidateRegex]`:
- **Pattern Matching Power:** Leverage full .NET regular expressions to enforce exact syntax and character standards.
- **Immediate Input Feedback:** Validates strings in real time as designers type in the Inspector.
- **Customizable Error Banners:** Provide helpful error messages explaining the expected format or regular expression syntax.
- **Automated Pipeline Audits:** Discovered and validated project-wide via the Validation Engine scan window.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class GameBuildInfo : MonoBehaviour
{
    [ValidateRegex(@"^\d+\.\d+\.\d+$", "Version string must follow semantic versioning format (e.g. 1.0.4).")]
    public string semanticVersion = "1.0.0";
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
public ValidateRegexAttribute(string pattern, string message = null)
```

- **`pattern`** (`string`): Regular expression string pattern that the field value must match.
- **`message`** (`string`, optional): Custom error message displayed upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Pattern` | `string` | Assigned in constructor | Regular expression pattern evaluated against the string value. |
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

namespace ProjectZero.Inventory
{
    public class ItemDefinition : ScriptableObject
    {
        [Header("Item Identifiers")]
        [ValidateRegex(@"^ITM_[A-Z]{3,5}_\d{3}$", 
            message: "Item ID must match format 'ITM_TYPE_001' (e.g. ITM_SWD_001, ITM_POT_042).",
            MessageType = InspectorMessageType.Error)]
        public string uniqueItemId = "ITM_SWD_001";

        [Header("Color Tint Override")]
        [ValidateRegex(@"^#(?:[0-9a-fA-F]{3}){1,2}$", 
            message: "Hex code must be a valid 3 or 6 digit hex color (e.g. #FFF or #FF5500).",
            MessageType = InspectorMessageType.Warning)]
        public string customHexTint = "#FFFFFF";
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateStringLength]`** | High | Enforce minimum/maximum character length alongside regex patterns. |
| **`[ValidateNotNull]`** | High | Ensure string is not null or empty before regex pattern matching. |
| **`[ValidateIf]`** | High | Conditionally apply regex validation rules based on selected input type. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |

### Collection Cascading & Serializer Matrix

| Collection / Container Type | Supported | Behavior |
| :--- | :---: | :--- |
| **`List<string>`** | Yes | Cascades to validate every string element independently. |
| **`string[]`** | Yes | Cascades to validate each array item against the regex pattern. |
| **`AdvancedList<string>`** | Yes | Full element-level validation support with dynamic item reordering. |
| **`SerializableDictionary<K, V>`** | Yes | Validates when applied to string key or value element targets. |
| **`SerializableNullable<string>`** | Yes | Validates the wrapped string when populated. |
| **`SerializableTuple<...>`** | Yes | Validates string fields within tuple members. |
