# [ValidateNotNull]

> Validates that a reference or string is not null, with optional empty string and zero-length collection detection.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateNotNull]` is an advanced null-safety validation attribute. It inspects object references (`UnityEngine.Object`, components, assets), strings, and collections. Beyond simple null pointer checks, it features `FailOnEmpty = true` (default), which additionally flags empty strings (`string.IsNullOrEmpty`) and zero-length arrays or lists (`collection.Count == 0`) as invalid.

**The Problem:**
Null reference exceptions are the single most common cause of runtime bugs in Unity games. Standard Unity attributes like `[SerializeField]` perform zero verification when a reference slot is left unassigned. Furthermore, native `[RequireComponent]` only works on attached components, not project assets, ScriptableObjects, strings, or child objects. Standard null checks also ignore empty string configs (`""`) that lead to broken URLs, empty resource paths, or missing IDs.

**The Solution:**
Decorating fields with `[ValidateNotNull]`:
- **Comprehensive Null & Empty Guard:** Validates object references, strings, and collections in one unified attribute.
- **Empty String & List Detection:** Setting `FailOnEmpty = true` prevents unpopulated string keys or empty array loadouts from passing QA.
- **Superset of `[Required]`:** Designed as the primary runtime validation counterpart to `[Required]`, fully discoverable by the Validation Engine.
- **Customizable Error Banners:** Displays high-contrast alert boxes directly below unassigned fields with custom messages and styling tokens.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class PlayerInventory : MonoBehaviour
{
    [ValidateNotNull("Item database asset must be assigned.")]
    public ScriptableObject itemDatabase;

    [ValidateNotNull("Character display name cannot be null or empty.", FailOnEmpty = true)]
    public string characterName = "Hero";
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
public ValidateNotNullAttribute(string message = "This field must not be null or empty.")
```

- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `FailOnEmpty` | `bool` | `true` | When true, also flags empty strings (`""`) and zero-length collections as validation failures. |
| `Message` | `string` | `"This field must not be null..."` | Failure explanation displayed in the validation message banner. |
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
    public class CombatAudioDirector : MonoBehaviour
    {
        [Header("Mandatory Sound Assets")]
        [ValidateNotNull("Combat theme music clip must be assigned before level start.", 
            MessageType = InspectorMessageType.Error)]
        public AudioClip combatThemeBgm;

        [Header("Mandatory SFX Bank")]
        [ValidateNotNull("Explosion audio clip reference must not be null.")]
        public AudioClip explosionSfxClip;

        [Header("Audio Mixer Group")]
        [ValidateNotNull(FailOnEmpty = false)]
        public UnityEngine.Audio.AudioMixerGroup targetMixerGroup;

        [Header("Direct Collection Cascading")]
        [ValidateNotNull("All sound bank audio clip slots must be assigned.")]
        [Tooltip("Cascades null validation to each AudioClip in the array.")]
        public AudioClip[] soundBankClips = new AudioClip[2];

        [ValidateNotNull("Mission waypoint transforms cannot be null.", MessageType = InspectorMessageType.Warning)]
        [Tooltip("Cascades null validation to each Transform entry in the list.")]
        public List<Transform> missionWaypoints = new List<Transform>();
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### 7.1 Layout & Conditional Stacking

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateIf]`** | High | Conditionally enforce non-null requirements only when relevant features are enabled. |
| **`[BoxGroup]`** | High | Renders alert banners neatly inside layout cards below unassigned fields. |
| **`[ValidateCollection]`** | High | Use `[ValidateNotNull]` for single reference fields or element cascading; use `[ValidateCollection]` for overall list boundary validation. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans via `NotNullValidationRule`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Supported | Implements `ICollectionElementAttribute`; cascades null checking directly to every array element slot with error banners. |
| **Generic Lists (`List<T>`)** | Supported | Full support for dynamic lists; checks every element and displays inline error banners for any null reference slots. |
| **Custom `[Serializable]` Classes** | Supported | Operates seamlessly on nested class fields when rendered inline or within collections. |
| **Validation Engine Iteration** | Supported | `NotNullValidationRule` iterates `IEnumerable` collections during static project validation audits. |
