# [SceneReference]

> Binds string or int fields to SceneAsset objects with build index badges, 1-click scene opening in Editor, and Build Settings validation.

---

## 1. Overview & Value Proposition

**What it does:**
Allows developers to serialize scene names (as `string`) or scene build indices (as `int`) by dragging and dropping actual `SceneAsset` objects into the Inspector. It displays the scene's current build index badge, verifies inclusion in Build Settings, and provides an instant "Open" button to load the scene in the Editor.

**The Problem:**
Unity's `SceneAsset` cannot be serialized into standalone player builds. Developers end up using raw strings or integer indices, sacrificing drag-and-drop workflow and breaking asset rename tracking. If a designer renames a scene in the Project, string references break silently.

**The Solution:**
Add `[SceneReference]` to `string` or `int` fields:
- **SceneAsset Drag-and-Drop:** Drag `.unity` assets directly into the field; MSUltimate automatically syncs the string name or integer build index.
- **Build Index Badge:** Displays a pill badge showing the scene's assigned build index (`[Build: 3]`) or alerts if unassigned.
- **1-Click Scene Open:** Includes an inline button to open the scene directly in the Unity Editor during level design.
- **Build Settings Enforcement:** Warns if the scene has not yet been registered in Build Settings (`RequireInBuildSettings = true`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameManager : MonoBehaviour
{
    [SceneReference]
    public string mainMenuScene = "MainMenu";

    [SceneReference]
    public int splashScreenIndex = 0;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string` (scene name) or `int` (build index) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SceneReferenceAttribute(string customLabel = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `customLabel` | `string` | `null` | Optional label override for the inspector field row. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CustomLabel` | `string` | `null` | Custom field display name override. |
| `RequireInBuildSettings` | `bool` | `true` | Displays a warning if the assigned scene is not registered in Build Settings. |
| `ShowOpenSceneButton` | `bool` | `true` | Renders an inline button to immediately open the scene in the Editor. |
| `ShowBuildIndexBadge` | `bool` | `true` | Displays a visual status badge showing the scene's current Build Index. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using MaharajaStudio.MSUltimate.Runtime;

public class CampaignMissionSelector : MonoBehaviour
{
    [Header("Campaign Intro Scene")]
    [SceneReference("Prologue Scene", RequireInBuildSettings = true, ShowOpenSceneButton = true)]
    public string prologueScene = "Prologue_Cinematic";

    [Header("Campaign Chapter Levels (List of Scenes)")]
    [SceneReference]
    public List<string> chapterSceneList = new List<string>
    {
        "Chapter_01_Castle",
        "Chapter_02_Swamp",
        "Chapter_03_Volcano"
    };

    public void LaunchPrologue()
    {
        SceneManager.LoadScene(prologueScene);
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Object field, open button, and build badge fit comfortably inside card layouts. |
| `[ShowIf]` | Supported | Seamlessly toggles visibility based on campaign mode or game edition. |
| `[ReadOnly]` | Supported | Locks the scene from being replaced while keeping open button functional. |
| `ICollectionElement` | Supported | Full support for `List<string>`, `List<int>`, and array collections. |
