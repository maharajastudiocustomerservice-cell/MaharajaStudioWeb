# [ValidateAssetPath]

> Validates that a string path refers to an existing asset in the Unity project, with optional asset type assignment verification.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateAssetPath]` validates string fields representing project-relative paths (e.g. `"Assets/Configs/WeaponData.asset"` or `Resources` / `Addressable` path keys). It verifies that an asset physically exists at the specified project path via `AssetDatabase.LoadAssetAtPath`, and optionally confirms that the asset is assignable to an expected type (`ExpectedType`).

**The Problem:**
String-based asset loading (such as `Resources.Load`, `AssetDatabase.LoadAssetAtPath`, or custom procedural asset loaders) is vulnerable to typos, broken file renames, and moved folders. Because strings cannot be verified at compile time, broken paths go unnoticed until runtime loading fails, throwing null references during critical gameplay or initialization sequences.

**The Solution:**
Decorating string path fields with `[ValidateAssetPath]`:
- **Real-Time Path Existence Verification:** Confirms that the target asset actually exists in the project asset database.
- **Type Compatibility Enforcement:** When `ExpectedType` is provided (e.g. `ExpectedType = typeof(ScriptableObject)`), verifies that the loaded asset matches the required type.
- **Immediate Visual Error:** Displays an inspector error banner as soon as a path string is mistyped or points to a non-existent location.
- **Configurable Severity:** Toggle between `Error` and `Warning` states to suit development vs. production build stages.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class ConfigLoader : MonoBehaviour
{
    [ValidateAssetPath("Asset path must point to a valid project file.")]
    public string configAssetPath = "Assets/GameData/MasterConfig.asset";
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
public ValidateAssetPathAttribute(string message = "Asset path is invalid or does not exist.")
```

- **`message`** (`string`, optional): Custom error message displayed if the target asset path is invalid or missing.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ExpectedType` | `Type` | `null` | When set, also verifies that the asset loaded from the path is assignable to this type. |
| `Message` | `string` | `"Asset path is invalid..."` | Custom failure explanation displayed in the error banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error message. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background banner color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Data
{
    public class MasterLevelRegistry : MonoBehaviour
    {
        [Header("Registry Path Configuration")]
        [ValidateAssetPath(
            "Target path must point to an existing ScriptableObject asset.",
            ExpectedType = typeof(ScriptableObject),
            MessageType = InspectorMessageType.Error)]
        public string levelRegistryAssetPath = "Assets/ProjectZero/Data/LevelRegistry.asset";

        [ValidateAssetPath(
            "Default fallback material path is invalid or missing.",
            ExpectedType = typeof(Material))]
        public string defaultMaterialPath = "Assets/ProjectZero/Art/Materials/M_Fallback.mat";
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[FilePath]`** | High | Pair path picker drawer UI with automatic path validity validation. |
| **`[ValidateAssetExtension]`** | High | Guarantee both path existence and required file extension format. |
| **`[ValidateFolder]`** | High | Simultaneously validate root folder paths and nested asset paths. |
| **Validation Engine** | Native | Audited globally via the project-wide Validation Engine scan window. |
