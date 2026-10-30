# [AutoRename]

> Automatically renames referenced scene GameObjects or components to match clean naming patterns, eliminating generic Unity default names (`GameObject (1)`, `(Clone)`) in the hierarchy with automatic and button-controlled manual modes.

---

## 1. Overview & Value Proposition

**What it does:**
Automatically renames referenced GameObjects or Components assigned in the Inspector to match a clean, customizable naming pattern (e.g. `{FieldName}`, `{Host}_{FieldName}`, or `{FieldName}_{Index:00}`). Includes an inline 🏷️ button for on-demand manual renaming, supports automatic `(Clone)` suffix stripping, and handles sibling collision deduplication.

**The Problem:**
In standard Unity development, creating new game objects or instantiating prefabs results in generic default names like `GameObject (1)`, `GameObject (2)`, or `EnemyVariantA(Clone)`. When these objects are assigned to fields on other components, it is difficult to determine which object is referenced without clicking each field to ping the hierarchy. Over time, scene hierarchies become messy and confusing.

**The Solution:**
Add `[AutoRename]` above any object reference field or collection:
- **Clean Hierarchy Hygiene:** Automatically converts generic names into descriptive, context-aware names matching their field role.
- **Both Auto and Manual Modes:** Choose between automatic renaming on assignment (`AutoRenameMode.Auto`) or intentional button-driven renaming (`AutoRenameMode.Manual`).
- **Inline 🏷️ Action Button:** Render an ergonomic button beside the field control (styled like `[SetRandomValue]`) to trigger or re-run renaming at any time.
- **Dynamic Token Formatting:** Construct names using tokens like `{FieldName}`, `{Host}`, `{Component}`, `{Type}`, `{Original}`, and `{Index:00}`.
- **Designer Name Protection:** With `RenameCondition.OnlyIfDefault` (the default), existing custom-named objects are preserved and never overwritten by accident.
- **Prefab Asset Safety:** By default, restricts renaming strictly to scene instances (`SceneObjectsOnly = true`), preventing accidental modification of project prefab files on disk.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerCombatRig : MonoBehaviour
{
    // Dragging "GameObject (1)" automatically renames it to "MuzzlePoint"
    [AutoRename]
    public Transform muzzlePoint;

    // Names using host context: "Player_CombatRig_CameraPivot"
    [AutoRename("{Host}_{FieldName}")]
    public Transform cameraPivot;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `GameObject`, `Component` (`Transform`, `Collider`, etc.), Collections (`List<T>`, `T[]`) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **UI Toolkit Compatible** | Yes |
| **Undo Supported** | Yes (`Undo.RecordObject` + Scene Dirtying) |

---

## 4. Constructors & Parameters

```csharp
public AutoRenameAttribute()
public AutoRenameAttribute(string pattern)
public AutoRenameAttribute(AutoRenameMode mode)
public AutoRenameAttribute(string pattern, AutoRenameMode mode)
public AutoRenameAttribute(string pattern, RenameCondition condition)
public AutoRenameAttribute(string pattern, AutoRenameMode mode, RenameCondition condition)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `pattern` | `string` | `"{FieldName}"` | Naming template with dynamic tokens (`{FieldName}`, `{Host}`, `{Type}`, `{Original}`, `{Index}`). |
| `mode` | `AutoRenameMode` | `AutoRenameMode.Auto` | Execution mode: `Auto` (on assignment/change) or `Manual` (via button click only). |
| `condition` | `RenameCondition` | `RenameCondition.OnlyIfDefault` | Overwrite rule: `OnlyIfDefault` (protects custom names) or `Always` (overwrites unconditionally). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Pattern` | `string` | `"{FieldName}"` | Naming template supporting tokens (`{FieldName}`, `{Host}`, `{Component}`, `{Type}`, `{Original}`, `{Index}`). |
| `Mode` | `AutoRenameMode` | `AutoRenameMode.Auto` | Trigger mode: `Auto` (automatic on assignment) or `Manual` (button click only). |
| `Condition` | `RenameCondition` | `RenameCondition.OnlyIfDefault` | When to rename: `OnlyIfDefault` (Unity generic names) or `Always` (force overwrite). |
| `Target` | `RenameTarget` | `RenameTarget.ReferencedObject` | Renaming target: `ReferencedObject` (assigned object) or `HostGameObject` (current component holder). |
| `Casing` | `NamingCasing` | `NamingCasing.PascalCase` | Output casing: `PascalCase`, `CamelCase`, `SnakeCase`, `UpperSnakeCase`, `Nicified`, `LowerCase`, `UpperCase`. |
| `StripCloneSuffix` | `bool` | `true` | Automatically strips `(Clone)` suffixes from instantiated prefabs before renaming. |
| `SceneObjectsOnly` | `bool` | `true` | Defensive guard: only renames scene hierarchy objects; ignores Project folder assets. |
| `ResolveCollisions`| `bool` | `true` | Appends a numeric counter (`_01`, `_02`) if a sibling under the same parent shares the name. |
| `Prefix` | `string` | `""` | Optional string prepended before the resolved name. |
| `Suffix` | `string` | `""` | Optional string appended after the resolved name. |
| `ShowButton` | `bool` | `true` | Whether to render the inline rename button beside the field control. |
| `ButtonText` | `string` | `"🏷️"` | Label text or emoji displayed on the inline button. |
| `ButtonTooltip` | `string` | `"Rename object to match pattern"` | Tooltip displayed on hover over the rename button. |
| `ForceOnManualClick` | `bool` | `true` | If true, clicking the manual button renames even if `Condition` is `OnlyIfDefault` and it has a custom name. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TurretMountSystem : ModularMonoBehaviour
{
    [Title("Turret Rigging", "Automatic and manual object naming")]

    [AutoRename]
    [Tooltip("Dragging an empty child GameObject renames it to 'RotationPivot'")]
    public Transform rotationPivot;

    [AutoRename("{Host}_{FieldName}")]
    [Tooltip("Names using host name: 'Turret_Base_MuzzleTip'")]
    public Transform muzzleTip;

    [Title("Manual & Audio Controls", "Explicit button activation")]

    [AutoRename("SFX_{FieldName}", AutoRenameMode.Manual, ButtonText = "✏️")]
    [Tooltip("Click the inline ✏️ button to apply the format")]
    public AudioSource firingAudio;

    [Title("VFX & Prefabs", "Automatic (Clone) stripping")]

    [AutoRename("VFX_{Original}", StripCloneSuffix = true)]
    [Tooltip("Dragging 'MuzzleFlash(Clone)' automatically renames it to 'VFX_MuzzleFlash'")]
    public ParticleSystem muzzleFlash;

    [Title("Waypoint Network", "List item indexing")]

    [AutoRename("{FieldName}_{Index:00}")]
    [Tooltip("Elements automatically numbered 'PatrolNodes_00', 'PatrolNodes_01', etc.")]
    public List<Transform> patrolNodes = new List<Transform>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[AdvancedList]` | Supported | Fully compatible with paginated lists and batch drag-and-drop. Renames all items across all pages immediately without needing to open them, and adds a collection header rename button. |
| `[BoxGroup]` | Supported | Inline rename button sits smoothly within group rows. |
| `[ReadOnly]` | Supported | Locks field reference input while keeping the manual 🏷️ button clickable. |
| `[ShowIf]` | Supported | Respects dynamic visibility logic; hides button when field is hidden. |
| `ICollectionElement` | Supported | Automatically cascades to child elements of `List<T>` and `T[]` with `{Index}` resolution. |
| Unity Undo System | Supported | Every rename registers with `Undo.RecordObject` for full `Ctrl+Z` support. |
