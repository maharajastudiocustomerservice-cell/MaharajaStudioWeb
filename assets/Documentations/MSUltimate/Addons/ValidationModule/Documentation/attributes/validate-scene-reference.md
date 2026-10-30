# [ValidateSceneReference]

> Validates that an assigned SceneAsset object reference or path matches an enabled entry in Unity's Build Settings list.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateSceneReference]` inspects assigned `SceneAsset` object reference fields (or wrapper classes encapsulating scene assets). It verifies against `EditorBuildSettings.scenes` that the assigned scene asset is formally added to the project's Build Settings and marked as enabled. If an un-registered scene asset is assigned, an immediate error banner is displayed.

**The Problem:**
In modern Unity development, teams often prefer assigning strongly-typed `SceneAsset` objects rather than raw string names to preserve drag-and-drop workflow and reference tracking. However, assigning a scene asset does not automatically add it to `File > Build Settings`. When the game is compiled into a standalone player, un-registered scenes are excluded from the build, causing runtime level loading to fail completely.

**The Solution:**
Decorating `SceneAsset` fields with `[ValidateSceneReference]`:
- **Build Settings Inclusion Guard:** Confirms that the assigned scene asset is registered in Build Settings before testing or building.
- **Prevents Missing Scene Build Crashes:** Eliminates player crashes where scenes work in the Editor but fail in standalone builds.
- **Works with SceneAsset & Wrappers:** Handles native `UnityEditor.SceneAsset` objects as well as custom serialized scene wrapper structs.
- **Immediate Visual Error:** Prompts developers to add the scene to Build Settings right inside the Inspector.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;
#if UNITY_EDITOR
using UnityEditor;
#endif

public class MainMenuController : MonoBehaviour
{
#if UNITY_EDITOR
    [ValidateSceneReference("Campaign start scene must be added to Build Settings.")]
    public SceneAsset startCampaignScene;
#endif
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
public ValidateSceneReferenceAttribute(string message = "Scene is not in Build Settings.")
```

- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | `"Scene is not in Build Settings."` | Failure explanation displayed in the validation message banner. |
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
#if UNITY_EDITOR
using UnityEditor;
#endif

namespace ProjectZero.World
{
    public class LevelLoaderButton : MonoBehaviour
    {
#if UNITY_EDITOR
        [Header("Scene Asset Binding")]
        [ValidateSceneReference("Target level asset is missing from Build Settings! Add it via File > Build Settings.",
            MessageType = InspectorMessageType.Error)]
        public SceneAsset targetLevelAsset;

        [ValidateSceneReference("Intro cinematic scene is not configured in Build Settings.")]
        public SceneAsset introCinematicAsset;
#endif
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[Scene]`** | High | Pair standard visual scene picker drawers with Build Settings validation. |
| **`[ValidateSceneName]`** | Alternative | Use `[ValidateSceneReference]` for asset references; use `[ValidateSceneName]` for string keys. |
| **`[Required]` / `[NotNull]`** | High | Guarantee the scene asset slot is assigned before validating build settings inclusion. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
