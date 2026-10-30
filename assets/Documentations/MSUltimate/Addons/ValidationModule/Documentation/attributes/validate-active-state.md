# [ValidateActiveState]

> Validates that a referenced GameObject or Component matches an expected active or inactive state in the scene.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateActiveState]` inspects referenced scene `GameObject` or `Component` fields. It verifies whether the target object is actively enabled or disabled in the scene at editor evaluation time. It can evaluate either the local active state (`activeSelf`, default) or the global ancestor chain (`activeInHierarchy`, via `CheckHierarchy = true`). If the state fails validation, a customizable validation banner is rendered directly in the Inspector.

**The Problem:**
Complex scenes often contain managers, spawners, or triggers that must start inactive (waiting for scripted activation) or must start active (such as audio listeners or camera rigs). Developers frequently commit scenes where critical managers were accidentally disabled during isolated testing, or where hidden template objects were left active, creating silent initialization bugs and broken level transitions.

**The Solution:**
Decorating fields with `[ValidateActiveState]`:
- **Active / Inactive Verification:** Enforce that target references must be active (`mustBeActive = true`) or explicitly inactive (`mustBeActive = false`).
- **Hierarchy-Aware Evaluation:** Toggle `CheckHierarchy = true` to verify that no parent or ancestor in the transform branch has deactivated the object.
- **Customizable Warning Messages:** Provide clear, domain-specific alerts (`"Boss spawner must start inactive!"`) with configurable warning/error severity (`MessageType`).
- **Visual Styling Tokens:** Style error badges with custom colors (`ErrorColor`, `ErrorBackgroundColor`), fonts, and margins.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class MissionManager : MonoBehaviour
{
    [ValidateActiveState(true, "Main Camera must be active in the scene.")]
    public Camera sceneCamera;

    [ValidateActiveState(false, "Cinematic trigger volume must start inactive.")]
    public GameObject endSequenceTrigger;
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
public ValidateActiveStateAttribute(bool mustBeActive = true, string message = null)
```

- **`mustBeActive`** (`bool`, default `true`): The required active state. When `true`, object must be active; when `false`, object must be inactive.
- **`message`** (`string`, optional): Custom error message displayed upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MustBeActive` | `bool` | `true` | The expected active state configured via the constructor. |
| `CheckHierarchy` | `bool` | `false` | When true, evaluates `activeInHierarchy`; when false, checks `activeSelf`. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message box. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Warning` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation warning message. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background banner color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Quests
{
    public class CutsceneTriggerVolume : MonoBehaviour
    {
        [Header("Cinematic Stage References")]
        [ValidateActiveState(true, "Cinematic camera rig must be active.", 
            CheckHierarchy = true, 
            MessageType = InspectorMessageType.Error)]
        public Camera cinematicCamera;

        [ValidateActiveState(false, "Dialogue canvas must remain inactive until cutscene activates.", 
            MessageType = InspectorMessageType.Warning)]
        public GameObject dialogueOverlayUI;

        public void TriggerCutscene()
        {
            if (dialogueOverlayUI != null)
                dialogueOverlayUI.SetActive(true);
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateIf]`** | High | Gate active state validation so it only executes when specific stage conditions are met. |
| **`[ValidateComponent]`** | High | Combine component existence checks with scene activation state verification. |
| **`[Required]` / `[NotNull]`** | High | Ensure reference is non-null before checking its active state in the hierarchy. |
| **Validation Engine** | Native | Audited globally via the project-wide Validation Engine scan window. |
