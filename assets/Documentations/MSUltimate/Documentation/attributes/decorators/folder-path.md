# [FolderPath]

> Renders a folder path selector with OS directory browser, folder drag-and-drop, and project folder ping.

---

## 1. Overview & Value Proposition

**What it does:**
Converts a string variable into an intuitive directory selector featuring a folder browser dialog and quick project ping.

**The Problem:**
Specifying output directories, asset export folders, or build destinations in Unity requires typing path strings by hand. Spelling a folder name wrong or missing a slash leads to build pipeline crashes or exported files ending up in unexpected directories.

**The Solution:**
Add `[FolderPath]` to any string field:
- **Native Folder Browser:** Click to open the native operating system directory selection picker.
- **Drag & Drop Directories:** Drag any folder from the Unity Project tab directly into the field to populate its path.
- **One-Click Folder Ping:** Jump straight to the target folder in Unity's Project tab or reveal it in File Explorer / Finder.
- **Project Relative or Absolute:** Pick whether to store clean `Assets/...` relative paths for version control or absolute system paths for local build caches.
- **Collections Compatible:** Works on single strings, arrays, and lists of folder paths.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AssetPipelineSettings : ScriptableObject
{
    [FolderPath]
    public string texturesFolder = "Assets/Game/Textures";

    [FolderPath(absolutePath: true)]
    public string localBuildDirectory = "C:/Builds/Client";
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
public FolderPathAttribute(bool absolutePath = false)
public FolderPathAttribute(string customLabel, bool absolutePath = false)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `absolutePath` | `bool` | `false` | If `true`, saves full disk path; otherwise formats relative to `Assets/`. |
| `customLabel` | `string` | `null` | Custom label display override for the inspector field. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `AbsolutePath` | `bool` | `false` | Toggles project-relative vs. full OS absolute paths. |
| `CustomLabel` | `string` | `null` | Custom label text override. |
| `ShowPingButton` | `bool` | `true` | Displays ping icon to locate the folder in Project tab. |
| `ButtonColor` | `string` | `null` | Hex background color for the folder select button. |
| `ButtonTextColor` | `string` | `null` | Hex text color for the button label. |
| `LabelWidth` | `float` | `0f` | Custom width in pixels for the row label (`0f` uses default inspector split). |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class BuildExporter : MonoBehaviour
{
    [Header("Export Settings")]
    [FolderPath(customLabel: "Staging Root", absolutePath: false, ButtonColor = "#27ae60")]
    public string stagingAssetFolder = "Assets/Exports/Staging";

    [FolderPath(absolutePath: true, ShowPingButton = true)]
    public string externalBackupDrive = "D:/Backups/ProjectZero";

    [Header("Ignored Folders")]
    [FolderPath]
    public List<string> excludedDirectories = new List<string>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[FilePath]` | Complementary | Use `[FolderPath]` for directory targets and `[FilePath]` for individual files. |
| `[BoxGroup]` | Supported | Integrates cleanly inside visual box groups and tab views. |
| `[ShowIf]` | Supported | Dynamically display output directories only when export modes are active. |
