# [FilePath]

> Renders a file path picker with browse dialog, drag-and-drop asset support, and quick ping in the Project window.

---

## 1. Overview & Value Proposition

**What it does:**
Turns a plain string into an interactive file selector with a browse button, asset pinging, and drag-and-drop asset handling.

**The Problem:**
In standard Unity, string fields meant to hold file paths require developers to manually copy and paste file paths or open Explorer. Mistyped file paths, missing extensions, and broken relative paths cause silent asset loading errors at runtime.

**The Solution:**
Add `[FilePath]` to any string field:
- **Interactive File Dialog:** Click browse to open the native OS file picker filtered to your desired file extensions (e.g. `.json`, `.csv`, `.bytes`).
- **Drag & Drop Support:** Drag any project asset directly into the string field to auto-populate its path.
- **One-Click Asset Ping:** Jump directly to the file in Unity's Project window or reveal it in OS Explorer.
- **Relative or Absolute:** Automatically formats paths relative to the project `Assets/` directory or stores full absolute filesystem paths for external tools.
- **Collection Support:** Fully compatible with `List<string>` and string array elements.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ConfigLoader : MonoBehaviour
{
    [FilePath("json")]
    public string configurationFilePath = "Assets/Data/game_config.json";

    [FilePath("csv", absolutePath: false)]
    public string localizationTable;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string`, `List<string>`, `string[]` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public FilePathAttribute(string extension = "", bool absolutePath = false)
public FilePathAttribute(string extension, string customLabel)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `extension` | `string` | `""` | File extension filter without leading dot (e.g. `"json"`, `"png"`, `"txt"`). |
| `absolutePath` | `bool` | `false` | If `true`, saves full disk path (e.g. `C:/Projects/...`); otherwise saves relative to `Assets/`. |
| `customLabel` | `string` | `null` | Custom display label override for the inspector row. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Extension` | `string` | `""` | Extension filter string for file browsing. |
| `AbsolutePath` | `bool` | `false` | Toggles project-relative vs. full OS absolute file paths. |
| `CustomLabel` | `string` | `null` | Custom label string for the property field. |
| `ShowPingButton` | `bool` | `true` | Displays the target ping icon to highlight the file in Project hierarchy. |
| `ButtonColor` | `string` | `null` | Hex background color for the browse button. |
| `ButtonTextColor` | `string` | `null` | Hex text color for the browse button label. |
| `LabelWidth` | `float` | `0f` | Custom width in pixels for the row label (`0f` uses default inspector split). |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ModManager : MonoBehaviour
{
    [Header("Core Mod Configuration")]
    [FilePath("zip", ShowPingButton = true, ButtonColor = "#3498db")]
    public string modPackageFile;

    [Header("Server Export Output")]
    [FilePath("log", absolutePath: true, CustomLabel = "Diagnostic Log Path")]
    public string externalCrashDumpPath = "C:/GameServer/logs/crash.log";

    [Header("Batch Data Tables")]
    [FilePath("csv")]
    public List<string> importedDataSheets = new List<string>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[FolderPath]` | Complementary | Use `[FilePath]` for individual files and `[FolderPath]` for directory targets. |
| `[BoxGroup]` | Supported | Adapts cleanly within nested groups and tabs. |
| `[ReadOnly]` | Supported | Browse button remains clickable to locate the path while text field remains non-editable if desired. |
| `[ValidateInput]` | Supported | Pair with validation to verify the file exists on disk. |
