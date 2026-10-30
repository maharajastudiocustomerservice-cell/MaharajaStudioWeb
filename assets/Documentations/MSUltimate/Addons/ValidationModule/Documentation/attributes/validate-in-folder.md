# [ValidateInFolder]

> Validates that an assigned project asset is stored within an expected directory path in the project asset hierarchy.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateInFolder]` inspects assigned project asset references (`UnityEngine.Object`, `ScriptableObject`, `AudioClip`, `Material`, `Prefab`, etc.). It interrogates the asset's project database path (`AssetDatabase.GetAssetPath`) and asserts that the asset resides inside an expected folder or directory path (`RequiredFolder`). When `ExactMatch = true`, it requires the asset to reside directly in that directory rather than in nested subdirectories.

**The Problem:**
In large multi-team Unity projects, asset organization is governed by strict folder hierarchies (e.g., all player skins must reside in `Assets/Art/Characters/Skins/`, or all sound effects must live in `Assets/Audio/SFX/`). Without enforcement, team members drag assets from staging folders, sandbox directories, third-party plugin folders, or temporary download folders into core gameplay references, leading to broken bundle builds and missing dependencies when assets are moved or deleted.

**The Solution:**
Decorating asset fields with `[ValidateInFolder]`:
- **Directory Placement Enforcement:** Restricts valid asset assignments strictly to designated studio project directories (e.g. `"Assets/GameData/Weapons"`).
- **Subdirectory Control:** Toggle `ExactMatch = true` to disallow deep subdirectory nesting if a flat folder structure is required.
- **Prevents Asset Reference Pollution:** Guards core game configs from referencing temporary artist sandbox files.
- **Clear Error Guidance:** Informs developers exactly where the assigned asset should be located.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class CharacterCustomizer : MonoBehaviour
{
    [ValidateInFolder("Assets/Art/Characters/Skins", 
        message: "Character skin prefab must be located inside 'Assets/Art/Characters/Skins'.")]
    public GameObject skinPrefab;
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
public ValidateInFolderAttribute(string requiredFolder, string message = null)
```

- **`requiredFolder`** (`string`): The project-relative folder path required (e.g. `"Assets/Configs/Balancing"`).
- **`message`** (`string`, optional): Custom error message displayed upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RequiredFolder` | `string` | Assigned in constructor | Required parent directory path. |
| `ExactMatch` | `bool` | `false` | When true, asset must reside directly in `RequiredFolder` without subdirectories. |
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
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Audio
{
    public class BGMController : MonoBehaviour
    {
        [Header("Licensed Music Track")]
        [ValidateInFolder("Assets/Audio/Music/Production", 
            ExactMatch = false,
            message: "Soundtrack clip must reside inside 'Assets/Audio/Music/Production' or a designated subfolder.",
            MessageType = InspectorMessageType.Error)]
        public AudioClip backgroundMusicClip;

        [Header("Stinger SFX")]
        [ValidateInFolder("Assets/Audio/SFX/Stingers", ExactMatch = true)]
        public AudioClip victoryStingerClip;

        [Header("Direct Collection Cascading")]
        [ValidateInFolder("Assets/MSUltimate/Materials")]
        [Tooltip("Cascades folder requirement to each Material element in the array.")]
        public Material[] environmentMaterials;

        [ValidateInFolder("Assets/Audio/SFX", ExactMatch = false)]
        [Tooltip("Cascades folder path validation to each AudioClip in the list.")]
        public List<AudioClip> soundEffectClips = new List<AudioClip>();
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### 7.1 Layout & Conditional Stacking

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateAssetExtension]`** | High | Guarantee both folder location and expected file extension format. |
| **`[ValidateIsPrefab]`** | High | Verify prefab status while asserting placement within project prefab directories. |
| **`[Required]` / `[NotNull]`** | High | Ensure reference is assigned before evaluating folder containment. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans via `ValidateInFolderRule`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Supported | Implements `ICollectionElementAttribute`; validates every asset reference individually with dedicated error banners. |
| **Generic Lists (`List<T>`)** | Supported | Full support for dynamic lists; elements outside the target folder display inline alert banners. |
| **Custom `[Serializable]` Classes** | Supported | Operates seamlessly on nested class fields when rendered inline or within collections. |
| **Validation Engine Iteration** | Supported | `ValidateInFolderRule` iterates `IEnumerable` collections during static project validation audits. |
