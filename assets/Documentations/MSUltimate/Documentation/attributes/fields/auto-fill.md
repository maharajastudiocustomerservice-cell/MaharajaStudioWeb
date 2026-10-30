# [AutoFill]

> Automatically searches and assigns matching Component references in the Inspector across Self, Children, Parent, or Scene scopes.

---

## 1. Overview & Value Proposition

**What it does:**
Auto-detects and connects missing Component references (like `Rigidbody`, `AudioSource`, or `Collider`) the moment an object is inspected or initialized.

**The Problem:**
Connecting boilerplate component references by dragging and dropping them into serialized fields on every GameObject is tedious and error-prone. Forgetting to drag a `Rigidbody` or `Animator` causes frustrating `NullReferenceException` crashes when running play mode.

**The Solution:**
Add `[AutoFill]` to any Component field:
- **Flexible Search Scopes:** Search `Self`, `Children`, `Parent`, or the active `Scene` automatically.
- **Tag Filtering:** Scope scene-wide searches to objects with specific tags (e.g. `"Player"` or `"GameController"`).
- **Auto-Filled Badge:** Renders a clean pill badge indicating that the component was automatically resolved.
- **Overwrite Protection:** By default, preserves manually assigned references unless `Overwrite = true` is set.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerController : MonoBehaviour
{
    [AutoFill(SearchScope.Self)]
    public Rigidbody characterRigidbody;

    [AutoFill(SearchScope.Children)]
    public Animator characterAnimator;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any `Component` or `GameObject` type, or collections (`Component[]`, `List<Component>`) |
| **Collection Batching** | Supported via `ICollectionBatchAttribute` with `⚡` header action button |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AutoFillAttribute(
    SearchScope scope = SearchScope.Self, 
    string tag = "", 
    bool overwrite = false, 
    bool showBadge = true)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `scope` | `SearchScope` | `SearchScope.Self` | Hierarchy scope to search (`Self`, `Children`, `Parent`, `Scene`). |
| `tag` | `string` | `""` | Tag filter when searching across `Scene` scope. |
| `overwrite` | `bool` | `false` | If `true`, overwrites existing non-null assignments. |
| `showBadge` | `bool` | `true` | Shows an "Auto-Filled" badge next to the field. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Scope` | `SearchScope` | `Self` | Search scope in hierarchy (`Self`, `Children`, `Parent`, `Scene`). |
| `Tag` | `string` | `""` | Tag string filter. |
| `Overwrite` | `bool` | `false` | Whether to overwrite non-null values. |
| `ShowBadge` | `bool` | `true` | Toggles visual "Auto-Filled" status badge. |
| `BatchTriggers` | `CollectionBatchTriggers` | `InitialLoad` | Lifecycle triggers that run batch population on collections. |
| `ShowHeaderButton`| `bool` | `true` | Renders a `⚡` batch population action button in collection headers. |
| `HeaderButtonText`| `string` | `"⚡"` | Action button icon/text in the collection header. |
| `HeaderButtonTooltip`| `string` | `"Auto-fill all elements from scene/hierarchy"` | Tooltip displayed when hovering over header button. |
| `Order` | `int` | `0` | Execution priority relative to other decorator attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TurretAI : MonoBehaviour
{
    [Header("Local Components")]
    [AutoFill(SearchScope.Self)]
    public AudioSource turretAudio;

    [AutoFill(SearchScope.Children)]
    public Transform barrelExitPoint;

    [Header("Hierarchy Targets")]
    [AutoFill(SearchScope.Parent)]
    public TurretBasePlatform basePlatform;

    [AutoFill(SearchScope.Scene, tag: "Player")]
    public Transform currentTargetPlayer;

    [Header("Batch Populated Collections")]
    [AutoFill(SearchScope.Children)]
    [Tooltip("Populates all Colliders found in child GameObjects with a '⚡' header action button.")]
    public Collider[] childHitboxColliders;

    [AutoFill(SearchScope.Scene)]
    [Tooltip("Populates all Lights found across the active scene.")]
    public List<Light> targetSceneLights;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ReadOnly]` | Supported | Lock the field from manual dragging while letting `[AutoFill]` populate it automatically. |
| `[Required]` | Recommended | Pairs together to ensure the reference is populated and throw errors if missing. |
| `[BoxGroup]` | Supported | Functions normally inside group cards. |
| Collections (`T[]`, `List<T>`) | Supported | Implements `ICollectionBatchAttribute` to auto-populate all matching items in batch with a header `⚡` button. |
