# [ValidateCollection]

> Validates collection sizes, checks for null elements, and enforces uniqueness across array and list items.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateCollection]` audits array and `List<T>` serialized collections. It asserts that collection lengths stay within defined minimum (`MinSize`) and maximum (`MaxSize`) boundaries, guarantees that elements are not null (`DisallowNullElements = true`), and optionally asserts that all elements in the collection are unique without duplicate references (`RequireUniqueElements = true`).

**The Problem:**
Collections in Unity inspectors are prone to accidental editor oversights: developers forget to populate an array slot (leaving a `None (Game Object)` null element), leave an empty list that causes a runtime `IndexOutOfRangeException`, or accidentally assign the same ScriptableObject or item prefab twice. Standard Unity provides no built-in collection size clamping or element uniqueness validation.

**The Solution:**
Decorating collections with `[ValidateCollection]`:
- **Capacity Bounds:** Enforces strict min/max element count boundaries (e.g. `minSize: 1, maxSize: 8`).
- **Null Element Guarding:** Immediately detects null array slots (`DisallowNullElements = true`) and displays a clear error banner.
- **Uniqueness Enforcement:** Prevents duplicate entries (`RequireUniqueElements = true`), critical for inventory slots, ability loadouts, and audio clip pools.
- **Project-Wide Scanning:** Integrates with the Validation Engine scan window for automated batch validation.

---

## 2. Quick Start

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class AbilityLoadout : MonoBehaviour
{
    [ValidateCollection(minSize: 1, maxSize: 4, disallowNullElements: true, requireUniqueElements: true,
        message: "Equipped abilities must contain 1 to 4 unique, non-null ability assets.")]
    public List<ScriptableObject> equippedAbilities = new List<ScriptableObject>();
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
| **Validation Interface** | `IValidationAttribute`, `ICollectionBatchAttribute` |
| **Batch Action Button** | `🧹` (Cleans null and unassigned elements with one click) |

---

## 4. Constructors & Parameters

```csharp
public ValidateCollectionAttribute(string message = "Collection validation failed.")
public ValidateCollectionAttribute(
    int minSize, 
    int maxSize = -1, 
    bool disallowNullElements = true, 
    bool requireUniqueElements = false, 
    string message = null)
```

- **`minSize`** (`int`): Minimum acceptable collection element count (-1 skips check).
- **`maxSize`** (`int`, optional): Maximum acceptable collection element count (-1 skips check).
- **`disallowNullElements`** (`bool`, optional): When true, flags an error if any entry is null or empty.
- **`requireUniqueElements`** (`bool`, optional): When true, flags an error if duplicate items exist.
- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinSize` | `int` | `-1` | Minimum required element count (-1 disables lower bound check). |
| `MaxSize` | `int` | `-1` | Maximum allowed element count (-1 disables upper bound check). |
| `DisallowNullElements` | `bool` | `true` | When true, fails validation if any array or list slot contains null. |
| `RequireUniqueElements` | `bool` | `false` | When true, fails validation if any element appears more than once. |
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
    public class FootstepSoundBank : MonoBehaviour
    {
        [Header("Surface Footsteps")]
        [ValidateCollection(minSize: 3, maxSize: 12, disallowNullElements: true, requireUniqueElements: true,
            message: "Grass footsteps bank must provide between 3 and 12 distinct audio clips.",
            MessageType = InspectorMessageType.Error)]
        public AudioClip[] grassClips;

        [ValidateCollection(minSize: 1, disallowNullElements: true,
            message: "Must provide at least one stone step sound effect.")]
        public List<AudioClip> stoneClips = new List<AudioClip>();

        [Header("Direct Collection Batch Operations")]
        [ValidateCollection(minSize: 2, maxSize: 6, disallowNullElements: true)]
        [Tooltip("Features the 🧹 header batch action button to purge null references automatically.")]
        public Transform[] raidPartyMembers;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### 7.1 Layout & Conditional Stacking

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[DrawCollection]`** | High | Pairs seamlessly with enhanced collection drawing UI while enforcing size/null constraints. |
| **`[BoxGroup]`** | High | Nests cleanly within layout groups and inspector tab cards. |
| **`[ValidateIf]`** | High | Conditionally validate collection contents based on active game mode or toggle. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans via `ValidateCollectionRule`. |

### 7.2 Collection Cascading & Serializer Behavior Matrix

| Target Context | Support Status | Architecture Notes |
| :--- | :---: | :--- |
| **Direct Arrays (`T[]`)** | Supported | Implements `ICollectionBatchAttribute`; validates the array container bounds and displays the `🧹` batch action button. |
| **Generic Lists (`List<T>`)** | Supported | Full dynamic list support; provides real-time size validation and one-click purging of null elements via `ICollectionBatchDrawer.ExecuteBatch`. |
| **AdvancedList (`AdvancedList<T>`)** | Supported | Seamlessly mounts atop MSUltimate's advanced list header bar with visual validation badges. |
| **Validation Engine Auditing** | Supported | `ValidateCollectionRule` inspects collection bounds and null entries during global project validation. |
