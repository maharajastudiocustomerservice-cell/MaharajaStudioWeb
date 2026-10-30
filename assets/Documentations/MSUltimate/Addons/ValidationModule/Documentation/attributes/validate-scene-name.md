# [ValidateSceneName]

> Validates that a string field matches the name of an enabled scene in the Unity Build Settings list.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateSceneName]` validates string serialized fields representing scene names (such as level load destinations, portal transition targets, or main menu scene identifiers). It interrogates `EditorBuildSettings.scenes` to verify that the string exactly matches an existing, enabled scene registered in Unity's Build Settings. If the string is mistyped, refers to a deleted scene, or matches a scene that is disabled in the build list, an immediate error banner is displayed.

**The Problem:**
In gameplay scripting, developers load scenes using string parameters: `SceneManager.LoadScene("Level_02")`. If a level designer renames `"Level_02"` to `"Level_02_Forest"` or disables it in Build Settings without updating the trigger script, the game crashes or freezes with a black screen at runtime when the scene fails to load.

**The Solution:**
Decorating scene name strings with `[ValidateSceneName]`:
- **Build Settings Verification:** Guarantees that any scene name typed into the inspector is registered and enabled in `File > Build Settings`.
- **Typo Protection:** Catches typos and naming discrepancies instantly at edit time.
- **Pairs with `[ValidateSceneReference]`:** Use `[ValidateSceneName]` for string identifiers, or `[ValidateSceneReference]` for scene asset references.
- **Clear Error Reporting:** Informs designers that the specified scene is missing from Build Settings.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class LevelPortal : MonoBehaviour
{
    [ValidateSceneName("Target scene name must exist and be enabled in Build Settings.")]
    public string targetSceneName = "Level_02_Forest";
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
public ValidateSceneNameAttribute(
    string message = "String does not match an enabled Scene in the Build Settings.")
```

- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | `"String does not match..."` | Failure explanation displayed in the validation message banner. |
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
using UnityEngine.SceneManagement;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.World
{
    public class SceneTransitionTrigger : MonoBehaviour
    {
        [Header("Target Scene Configuration")]
        [ValidateSceneName("Next level scene is not configured in Build Settings.", 
            MessageType = InspectorMessageType.Error)]
        public string nextLevelScene = "Sector_02_Citadel";

        [ValidateSceneName("Fallback respawn scene is missing or disabled in Build Settings.")]
        public string respawnFallbackScene = "Hub_Sanctuary";

        public void LoadNextLevel()
        {
            if (!string.IsNullOrEmpty(nextLevelScene))
            {
                SceneManager.LoadScene(nextLevelScene);
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[Scene]`** | High | Pair standard visual scene picker dropdown drawers with validation verification. |
| **`[ValidateNotNull]`** | High | Guarantee the scene name string is not empty before validating against Build Settings. |
| **`[ValidateIf]`** | High | Conditionally validate scene names based on active game mode or destination type. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
