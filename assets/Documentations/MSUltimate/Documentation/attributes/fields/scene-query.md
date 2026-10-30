# [SceneQuery]

> Renders string scene path/name fields as a searchable dropdown populated from project scenes with 1-click ping and Build Settings validation.

---

## 1. Overview & Value Proposition

**What it does:**
Populates a string field with an interactive dropdown list of scenes from the active Unity Project or Build Settings. Includes automatic detection of missing build scenes, an inline "Ping" button to highlight the Scene asset in the Project browser, and path filtering.

**The Problem:**
Loading scenes in Unity using strings (like `SceneManager.LoadScene("Level_02")`) is error-prone. A typo in the level name causes fatal loading failures in standalone builds. Additionally, if a level has not been added to Build Settings, developers are only alerted when the build fails or throws exceptions at runtime.

**The Solution:**
Add `[SceneQuery]` to any string field:
- **Drop-Down Scene Picker:** Choose scenes directly from a clean dropdown instead of manually typing scene names.
- **Build Settings Validation:** Warns immediately in the Inspector if the selected scene is missing from Unity's Build Settings (`DisplayWarningIfMissing = true`).
- **Ping Asset Button:** Instantly locate and ping the `.unity` scene asset in the Project view with a single click.
- **Path & Filtering Options:** Filter scenes by name patterns, toggle between simple scene names or full asset paths, and query either Build scenes or all project scenes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LevelTeleporter : MonoBehaviour
{
    [SceneQuery]
    public string targetSceneName = "Level_01_Forest";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string`, `int`, `string[]`, `List<string>`, `int[]`, `List<int>` |
| **Interface Implemented** | `ICollectionElementAttribute` (Cascades to collection elements) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SceneQueryAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IncludeAllScenes` | `bool` | `false` | If `true`, scans all project scenes rather than only scenes registered in Build Settings. |
| `ShowFullPath` | `bool` | `false` | Displays full asset paths (e.g. `Assets/Scenes/...`) in the dropdown list. |
| `StoreFullPath` | `bool` | `false` | Serializes the complete asset path instead of just the scene name. |
| `DisplayWarningIfMissing`| `bool` | `true` | Shows an infobox warning if the scene is omitted from Build Settings. |
| `MissingSceneWarning` | `string` | `"Scene not found in Build Settings."` | Warning text displayed when a scene is missing from build list. |
| `Filter` | `string` | `""` | Search substring filter to isolate matching scenes (e.g. `"Boss_"` or `"Dungeon"`). |
| `ShowPingButton` | `bool` | `true` | Renders a button to ping and reveal the scene asset in the Project view. |
| `PingButtonText` | `string` | `"Ping"` | Label text displayed on the ping button. |
| `Height` | `float` | `20f` | Height of the scene picker dropdown in pixels. |
| `PingButtonWidth` | `float` | `40f` | Width allocated to the ping button. |
| `Icon` | `string` | `"d_SceneAsset Icon"` | Icon identifier displayed in the dropdown header. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using UnityEngine.SceneManagement;
using MaharajaStudio.MSUltimate.Runtime;

public class DungeonExitPortal : MonoBehaviour
{
    [Header("Destination Scene (Build Settings Verified)")]
    [SceneQuery(DisplayWarningIfMissing = true, ShowPingButton = true)]
    public string nextDestinationScene = "Dungeon_Floor_02";

    [Header("Secret Dev Room (Any Project Scene)")]
    [SceneQuery(IncludeAllScenes = true, Filter = "Dev_", StoreFullPath = true)]
    public string debugSandboxScene = "Assets/Dev/Scenes/Dev_TestSandbox.unity";

    public void TriggerTransition()
    {
        if (!string.IsNullOrEmpty(nextDestinationScene))
        {
            SceneManager.LoadScene(nextDestinationScene);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :--- | :--- |
| `[BoxGroup]` | Supported | Dropdown and ping button align neatly inside layout groups. |
| `[ShowIf]` | Supported | Conditionally reveals scene loading targets based on game state flags. |
| `[ReadOnly]` | Supported | Displays the selected scene and allows pinging while locking dropdown selection. |
| `Collections (Arrays & Lists)` | **Supported (`ICollectionElementAttribute`)** | Directly decorates `string[]` or `List<string>` to render scene dropdown pickers and ping buttons per element. |
| `SerializableDictionary<K, string>` | **Supported (`ICollectionElementAttribute`)** | Renders scene picker dropdown for dictionary values. |

