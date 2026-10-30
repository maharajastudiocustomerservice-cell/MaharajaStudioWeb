# [ValidateFolder]

> Validates that a string field represents a valid, existing directory or folder path on the filesystem.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateFolder]` inspects string fields that represent folder paths (such as asset output directories, screenshot dump locations, level chunk directories, or save folder targets). It validates that the string contains legal directory syntax and, when `RequireExists = true` (default), checks whether the directory physically exists on the disk using `System.IO.Directory.Exists`.

**The Problem:**
Automated pipeline tools, asset processors, and build scripts frequently accept folder destination paths via inspector fields. If a developer enters a non-existent directory or mistypes a folder name, automated operations fail with `DirectoryNotFoundException`, or batch exports dump hundreds of files into the wrong project directory.

**The Solution:**
Decorating string folder fields with `[ValidateFolder]`:
- **Directory Existence Guard:** Confirms that the target folder exists on the operating system before file I/O operations execute.
- **Support for Planned Directories:** Set `RequireExists = false` if the script generates the directory automatically at runtime, validating only path syntax sanity.
- **Real-Time Inspector Feedback:** Displays an immediate error or warning banner if the folder path is missing or invalid.
- **Cross-Platform Compatibility:** Handles path separators seamlessly across Windows, macOS, and Linux platforms.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class AssetBatchProcessor : MonoBehaviour
{
    [ValidateFolder("Raw textures directory does not exist on disk.")]
    public string rawTexturesDirectory = "Assets/RawArt/Textures";
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
public ValidateFolderAttribute(string message = "Invalid or non-existent folder path.")
```

- **`message`** (`string`, optional): Custom error message displayed upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RequireExists` | `bool` | `true` | When true, asserts that the directory physically exists on the filesystem. |
| `Message` | `string` | `"Invalid or non-existent..."` | Failure explanation displayed in the validation message banner. |
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

namespace ProjectZero.EditorTools
{
    public class BuildAssetPipelineConfig : ScriptableObject
    {
        [Header("Source Asset Folders")]
        [ValidateFolder("Models source directory must exist.", 
            RequireExists = true, 
            MessageType = InspectorMessageType.Error)]
        public string modelsSourcePath = "RawAssets/3DModels";

        [Header("Runtime Output Folders")]
        [ValidateFolder("StreamingAssets cache folder path is invalid.", 
            RequireExists = false, 
            MessageType = InspectorMessageType.Warning)]
        public string runtimeCachePath = "Assets/StreamingAssets/Cache";
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[FolderPath]`** | High | Pair visual folder selection dialogs with automatic directory validation. |
| **`[ValidateFilePath]`** | High | Validate root directory paths alongside specific file paths. |
| **`[ValidateInFolder]`** | High | Enforce asset presence inside validated folder hierarchies. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
