# [ValidateChildTag]

> Validates that direct children of a referenced GameObject carry a specific Unity tag (with Any, All, or None match modes).

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateChildTag]` inspects direct children of an assigned `GameObject` or `Component` reference. It audits child transforms to ensure they carry a specified Unity tag (`RequiredTag`), evaluated according to a designated match mode (`MatchMode`: `Any`, `All`, or `None`). If the child tag condition is violated, an error banner is displayed in the Inspector.

**The Problem:**
Many gameplay and physics architectures use Unity tags for collision filtering, team affiliation, or damage routing (e.g. `tag == "PlayerHitbox"`, `tag == "EnemySpawnPoint"`). When artists build new characters, prefabs, or environment props, forgetting to set the tag on a child hitbox or collider causes weapons to pass through without dealing damage, or causes enemy AI to ignore player colliders.

**The Solution:**
Decorating reference fields with `[ValidateChildTag]`:
- **Tag Integrity Guard:** Ensures child objects carry designated tags required by game mechanics.
- **Match Mode Support:** Configure whether `Any` child must have the tag, `All` children must share the tag, or `None` may have it (blacklisting tags).
- **Supports Multiple Tag Rules:** Stack multiple attributes (`AllowMultiple = true`) to enforce distinct tag requirements across complex structures.
- **Inactive Child Awareness:** Include or exclude disabled children via `IncludeInactive`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class CombatEntity : MonoBehaviour
{
    [ValidateChildTag("Hitbox", 
        MatchMode = ChildTagMatchMode.All, 
        message: "All children of hitbox container must be tagged 'Hitbox'.")]
    public GameObject hitboxContainer;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ValidationModule Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Window Surface** | Unity Inspector & Validation Engine Window |
| **Validation Interface** | `IValidationAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateChildTagAttribute(string requiredTag, string message = null)
```

- **`requiredTag`** (`string`): The Unity tag required to exist on the child GameObjects.
- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RequiredTag` | `string` | Assigned in constructor | The Unity tag required on child GameObjects. |
| `MatchMode` | `ChildTagMatchMode` | `ChildTagMatchMode.Any` | Match rule: `Any`, `All`, or `None`. |
| `IncludeInactive` | `bool` | `true` | When true, includes inactive child GameObjects in the tag audit. |
| `Message` | `string` | Auto-generated | Failure explanation displayed in the validation message box. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error message. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background banner color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

### `ChildTagMatchMode` Enum Values
- **`Any`**: At least one direct child must have the specified tag.
- **`All`**: Every direct child must have the specified tag.
- **`None`**: No direct child may carry the specified tag.

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Combat
{
    public class BossEncounterArena : MonoBehaviour
    {
        [Header("Spawn Markers")]
        [ValidateChildTag("EnemySpawn", 
            MatchMode = ChildTagMatchMode.All, 
            Message = "All children in the wave spawn root must carry the 'EnemySpawn' tag.",
            MessageType = InspectorMessageType.Error)]
        public GameObject waveSpawnPoints;

        [Header("Hazard Triggers")]
        [ValidateChildTag("Hazard", 
            MatchMode = ChildTagMatchMode.Any, 
            Message = "Arena hazards root must contain at least one child tagged 'Hazard'.")]
        public GameObject hazardVolumes;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateChildCount]`** | High | Enforce both total child count limits and tag consistency. |
| **`[ValidateChildHasComponent]`** | High | Guarantee children possess both the required tag and required functional components (e.g. `Collider`). |
| **`[ValidateChildName]`** | High | Combine naming pattern rules with tag verification on children. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
