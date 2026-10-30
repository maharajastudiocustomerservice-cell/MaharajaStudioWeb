# [ValidateFilePath]

> Validates that a string field represents a valid OS filesystem path with optional existence check and file extension filter.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateFilePath]` validates string fields representing file paths on the local operating system (such as external export directories, localized asset dumps, build log destinations, or external audio banks). It verifies that the path string contains valid filesystem characters, optionally asserts that the file physically exists on disk (`RequireExists = true`), and optionally asserts that the file concludes with a required file extension (`Extension = ".csv"`).

**The Problem:**
Editor tooling and data-pipeline components frequently take external file paths as strings (e.g. `"C:/GameData/Dialogue.csv"` or `"Exports/Levels/Zone01.json"`). When developers or artists enter invalid paths containing illegal OS characters, point to deleted files, or omit required extensions, file I/O operations crash with `FileNotFoundException` or `DirectoryNotFoundException` during build export or data parsing.

**The Solution:**
Decorating string fields with `[ValidateFilePath]`:
- **Filesystem Existence Validation:** When `RequireExists = true`, checks `System.IO.File.Exists(path)` before scripts attempt to open streams.
- **Extension Filtering:** Enforce specific file extensions (`Extension = ".json"`, `Extension = ".csv"`, etc.).
- **Immediate Path Feedback:** Displays an error banner in the Inspector the moment a path breaks or points to a non-existent file.
- **OS Path Normalization:** Handles forward and backward slashes gracefully across Windows, macOS, and Linux.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class LevelExporter : MonoBehaviour
{
    [ValidateFilePath("Level data output path is invalid.", Extension = ".json", RequireExists = false)]
    public string exportFilePath = "Builds/Data/LevelExport.json";
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
public ValidateFilePathAttribute(string message = "Invalid file path.")
```

- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Extension` | `string` | `null` | Expected file extension (e.g. `".csv"`, `".xml"`). |
| `RequireExists` | `bool` | `true` | When true, asserts that the file physically exists on the filesystem. |
| `Message` | `string` | `"Invalid file path."` | Failure explanation displayed in the validation message banner. |
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

namespace ProjectZero.Data
{
    public class DialogueTableImporter : MonoBehaviour
    {
        [Header("Dialogue Source File")]
        [ValidateFilePath("Dialogue CSV file does not exist on disk.", 
            Extension = ".csv", 
            RequireExists = true, 
            MessageType = InspectorMessageType.Error)]
        public string sourceCsvPath = "RawData/Dialogue/Encounter_NPCs.csv";

        [Header("Output Binaries")]
        [ValidateFilePath(Extension = ".bytes", RequireExists = false)]
        public string compiledBinaryPath = "Assets/GameData/Dialogue_Compiled.bytes";
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[FilePath]`** | High | Pair standard visual file picker dialog buttons with automatic path validation. |
| **`[ValidateFolder]`** | High | Validate root folder paths alongside specific output file paths. |
| **`[ValidateNotNull]`** | High | Ensure path string is not null or empty before performing file checks. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |

### Collection Cascading & Serializer Matrix

| Collection / Container Type | Supported | Behavior |
| :--- | :---: | :--- |
| **`List<string>`** | Yes | Cascades to validate every file path string in the list. |
| **`string[]`** | Yes | Cascades to validate each array item against path and extension rules. |
| **`AdvancedList<string>`** | Yes | Full element-level validation support with dynamic item reordering. |
| **`SerializableDictionary<K, string>`** | Yes | Validates file paths when applied to value string elements. |
| **`SerializableNullable<string>`** | Yes | Validates wrapped path string when populated. |
| **`SerializableTuple<...>`** | Yes | Validates file path strings within tuple members. |
