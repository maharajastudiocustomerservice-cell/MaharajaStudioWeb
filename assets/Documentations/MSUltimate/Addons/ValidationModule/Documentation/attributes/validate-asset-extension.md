# [ValidateAssetExtension]

> Validates that a referenced project asset matches a required file extension (e.g. `.png`, `.fbx`, `.json`, `.wav`).

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateAssetExtension]` inspects assigned project asset references (`UnityEngine.Object`, `DefaultAsset`, `TextAsset`, `AudioClip`, etc.) and string file paths. It interrogates the asset's project database path (`AssetDatabase.GetAssetPath`) and validates that its file extension matches the expected extension format (`ExpectedExtension`). If the assigned file has an incorrect extension (such as assigning a `.mp3` where `.wav` is required, or assigning `.txt` instead of `.json`), it displays a clear validation error.

**The Problem:**
Generic Unity asset slots like `DefaultAsset`, `TextAsset`, or `Object` accept any file type from the Project window. In data-driven pipelines, developers expecting `.json` config files can accidentally drag in `.xml` or `.csv` files. Similarly, audio pipelines requiring uncompressed `.wav` assets can receive compressed `.mp3` files, causing runtime parse failures or unexpected compression artifacts.

**The Solution:**
Decorating asset fields with `[ValidateAssetExtension]`:
- **Format Enforcement:** Guarantees that only assets matching the designated extension (e.g. `".json"`, `".fbx"`, `".png"`) can be assigned.
- **Automatic Extension Normalization:** Accepts extensions with or without leading periods (`"json"` or `".json"`), formatting them consistently.
- **Early Pipeline Guard:** Catches wrong asset types at the moment of assignment rather than during runtime asset loading or build execution.
- **Custom Error Messages:** Supply clear studio instructions to guide artists and designers to the correct source assets.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class LocalizationDataLoader : MonoBehaviour
{
    [ValidateAssetExtension(".json", "Localization database must be a .json file.")]
    public TextAsset localizationFile;
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
public ValidateAssetExtensionAttribute(string expectedExtension, string message = null)
```

- **`expectedExtension`** (`string`): The required file extension (e.g. `".json"`, `".wav"`, `".fbx"`). Leading periods are automatically added if omitted.
- **`message`** (`string`, optional): Custom failure message to display upon validation error.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ExpectedExtension` | `string` | Assigned in constructor | Normalized file extension required for the assigned asset. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message box. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error banner. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background banner color override for the alert box. |
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
    public class SoundEffectTrigger : MonoBehaviour
    {
        [Header("Audio Asset Binding")]
        [ValidateAssetExtension(".wav", "High-fidelity SFX triggers require uncompressed .wav source files.",
            MessageType = InspectorMessageType.Error)]
        public AudioClip impactSfxClip;

        [Header("Config Binding")]
        [ValidateAssetExtension(".json")]
        public TextAsset audioRoutingConfig;

        [Header("Direct Collection Cascading")]
        [ValidateAssetExtension(".wav")]
        [Tooltip("Cascades .wav extension requirement to every entry in the array.")]
        public AudioClip[] combatAudioTracks;

        [ValidateAssetExtension(".json")]
        [Tooltip("Cascades .json extension validation to every scenario text asset.")]
        public List<TextAsset> scenarioDefinitions = new List<TextAsset>();

        public void PlaySfx()
        {
            if (impactSfxClip != null)
                AudioSource.PlayClipAtPoint(impactSfxClip, transform.position);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### 7.1 Layout & Conditional Stacking

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateAssetPath]`** | High | Combine file extension checks with project folder location validation. |
| **`[Required]` / `[NotNull]`** | High | Ensure asset reference is not null before checking extension. |
| **`[ValidateIsPrefab]`** | High | Guarantee that prefab assets possess the required `.prefab` extension. |
| **Validation Engine** | Native | Audited globally via the project-wide Validation Engine scan window via `ValidateAssetExtensionRule`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Supported | Implements `ICollectionElementAttribute`; cascades extension verification to each asset entry in arrays. |
| **Generic Lists (`List<T>`)** | Supported | Validates dynamic list entries individually; shows targeted error banners on invalid file extensions. |
| **Custom `[Serializable]` Classes** | Supported | Operates seamlessly on nested class fields when rendered inline or within collections. |
| **Validation Engine Iteration** | Supported | `ValidateAssetExtensionRule` iterates `IEnumerable` collections during static project validation audits. |
