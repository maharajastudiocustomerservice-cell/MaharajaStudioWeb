# [HierarchyFolder]

> Transforms an empty GameObject into an organizational folder header with folder styling and collapse indicators.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyFolder]` converts empty organizational GameObjects into clean, stylized virtual folders directly within the Unity Hierarchy window. Driven by `HierarchyFolderRenderer`, it paints a full-width background header row (`HeaderColor = "#1E272E"`), an accent stripe along the left edge (`FolderColor = "#F39C12"`), a bold folder icon (`"📁 "`), and customized title text. It supports an optional build-time optimization (`FlattenOnBuild = true`) to unparent and flatten child objects during player builds, preventing unnecessary transform hierarchy overhead in shipping games.

**The Problem:**
Unity does not provide native folders for the Hierarchy window. Developers create empty dummy GameObjects as pseudo-folders (e.g. `[CAMERAS]`, `_LIGHTS_`, `--- ENVIRONMENT ---`). These dummy objects look messy, lack folder iconography, and introduce deep transform hierarchy matrices at runtime that can negatively affect performance if left unmanaged.

**The Solution:**
Decorating organizational GameObjects with `[HierarchyFolder]`:
- **Native-Feeling Folder Headers:** Displays full-width colored folder rows with distinct folder icons (`📁`).
- **Clean Visual Chapters:** Visually divides scenes into logical chapters (e.g., Audio, Lighting, Spawners, UI).
- **Optional Flatten-On-Build:** Unparents children during standalone build compilation to optimize runtime transform depth.
- **Custom Folder & Header Colors:** Assign distinct theme colors to different folder types (amber for lights, blue for UI, purple for VFX).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyFolder(FolderName = "STATIC ENVIRONMENT", FolderColor = "#10B981")]
public class EnvironmentFolder : MonoBehaviour
{
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyFolderRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyFolderAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `FolderName` | `string` | `""` | Custom display name for the folder header. If empty, uses the GameObject's name in uppercase. |
| `FolderColor` | `string` | `"#F39C12"` | Hex accent color of the left vertical accent stripe. |
| `HeaderColor` | `string` | `"#1E272E"` | Hex background color spanning the full folder header row. |
| `TextColor` | `string` | `"#F5F6FA"` | Hex text color of the folder title label. |
| `FlattenOnBuild` | `bool` | `false` | Whether to unparent and flatten child objects during build player execution. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the folder header styling remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyFolder(
    FolderName = "POST PROCESSING & LIGHTING", 
    FolderColor = "#F59E0B", 
    HeaderColor = "#0F172A", 
    TextColor = "#F8FAFC", 
    FlattenOnBuild = false)]
public class LightingFolderHeader : MonoBehaviour
{
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyChildCounter]`** | High | Place child counters on folders to display the count of child entities organized within. |
| **`[HierarchyLock]`** | High | Lock folder header GameObjects to prevent accidental dragging or editing of the container itself. |
| **`[HierarchyBookmark]`** | High | Bookmark top-level folders for instant one-click navigation between major scene sections. |
| **Empty GameObjects** | Best Practice | Best used on empty GameObjects serving strictly as organizational group containers. |
