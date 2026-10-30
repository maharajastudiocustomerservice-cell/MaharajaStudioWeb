# [GrabFromChild]

> Intercepts drag-and-drop operations on object reference and collection fields, allowing developers to drop any ancestor or parent GameObject to automatically resolve, extract, and assign nested child components.

---

## 1. Overview & Value Proposition

**What it does:**  
`[GrabFromChild]` solves one of the most frustrating bottlenecks in Unity game development: assigning references to components or bones buried 10–20 levels deep in a GameObject hierarchy. Instead of forcing you to expand endless hierarchy folds to find a nested child, you can drop any visible parent or root GameObject directly onto the field—`[GrabFromChild]` searches the hierarchy, extracts the matching component, and assigns it instantly.

**The Problem:**
- Standard Unity `ObjectField` is strictly type-bound: if your field is `Hitbox`, dragging `Character_Root` is immediately rejected with a "not allowed" cursor.
- Manually expanding skeletal armatures (`Root/Pelvis/Spine/Chest/Shoulder/Arm/Hand/WeaponSocket`) is tedious, slow, and collapses if the Inspector accidentally loses focus.
- Populating collections (e.g. `List<Collider>` or `List<ParticleSystem>`) requires dragging dozens of child objects one-by-one.

**The Solution:**
- **Zero Hierarchy Diving:** Drop `Character_Root` directly into `headBone`, `weaponSocket`, or `characterHitboxes`.
- **Search Modes & Depth:** Choose between `Recursive` (all descendants), `DirectChildren` (immediate only), `SelfThenRecursive`, or `SelfThenDirect`.
- **Name & Wildcard Filtering:** Scope searches using patterns like `"Head"`, `"*Socket*"`, or `"Muzzle*"`.
- **Disambiguation Modes:** Automatically picks the `FirstMatch`, `LastMatch`, or opens an interactive `PromptIfMultiple` popup menu if several matches exist.
- **Bulk Collection Auto-Fill:** Drop a parent into a `List<T>` or `T[]` to populate all matching child components in a single click (`Replace` or `Append`).
- **Clean Field Integration:** Retains 100% of standard Unity inspector styling with zero UI clutter or extra buttons.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterRigBindings : MonoBehaviour
{
    // Drop Character_Root here -> automatically finds the child bone containing "Head"
    [GrabFromChild("Head")]
    public Transform headBone;

    // Drop Weapon_Prefab here -> automatically finds and assigns the audio source
    [GrabFromChild]
    public AudioSource weaponAudio;

    // Drop Character_Root here -> fills all child colliders into the list in bulk
    [GrabFromChild]
    public List<BoxCollider> hitboxes = new List<BoxCollider>();
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Category** | Fields (FieldModifier) |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any `Component` (e.g., `Transform`, `Collider`, `AudioSource`) or `GameObject`, plus collections (`List<T>`, `T[]`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes (`Inherited = true`) |
| **UI Toolkit Compatible** | Yes (Native UI Toolkit hybrid) |
| **Collection Interception** | Yes (Implements `ICollectionInterceptorAttribute` & `ICollectionElementAttribute`) |

---

## 4. Constructors & Signatures

```csharp
public GrabFromChildAttribute()

public GrabFromChildAttribute(bool enabled)

public GrabFromChildAttribute(
    string nameFilter, 
    GrabSearchMode searchMode = GrabSearchMode.Recursive, 
    bool enabled = true)

public GrabFromChildAttribute(
    GrabSearchMode searchMode, 
    bool enabled = true)

public GrabFromChildAttribute(
    GrabSearchMode searchMode, 
    CollectionDropMode collectionMode, 
    bool enabled = true)

public GrabFromChildAttribute(
    CollectionDropMode collectionMode, 
    GrabSearchMode searchMode = GrabSearchMode.Recursive, 
    bool enabled = true)

public GrabFromChildAttribute(
    GrabSearchMode searchMode, 
    GrabResolutionMode resolutionMode, 
    string nameFilter = "", 
    bool enabled = true)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `nameFilter` | `string` | `""` | Optional name or wildcard filter pattern (e.g. `*Socket*`, `Head`). |
| `searchMode` | `GrabSearchMode` | `Recursive` | Traversal scope (`Recursive`, `DirectChildren`, `SelfThenRecursive`, `SelfThenDirect`). |
| `resolutionMode` | `GrabResolutionMode` | `FirstMatch` | How to resolve multiple matches (`FirstMatch`, `LastMatch`, `PromptIfMultiple`). |
| `collectionMode` | `CollectionDropMode` | `Replace` | How dropped parents populate collections (`Replace`, `Append`). |
| `enabled` | `bool` | `true` | Controls whether child-grabbing drag interception is active. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Enabled` | `bool` | `true` | Enables or disables child-grabbing drag interception. |
| `NameFilter` | `string` | `""` | Pattern to match against child GameObject names. |
| `ExactName` | `bool` | `false` | If `true`, requires an exact name match; if `false`, supports substring/wildcards. |
| `CaseSensitive` | `bool` | `false` | If `true`, name matching is case-sensitive. |
| `SearchMode` | `GrabSearchMode` | `Recursive` | Hierarchy search traversal depth and order. |
| `ResolutionMode` | `GrabResolutionMode` | `FirstMatch` | Disambiguation behavior when multiple matching components are found. |
| `CollectionMode` | `CollectionDropMode` | `Replace` | Whether dropping onto a collection replaces or appends items. |
| `IncludeInactive` | `bool` | `true` | Whether to include inactive child GameObjects during search. |
| `ShowFeedback` | `bool` | `true` | Renders a green success badge and border flash on successful grab. |
| `AllowSelfGrabButton` | `bool` | `false` | Optional inline quick-grab button next to the field. |
| `AllowHierarchyBrowse` | `bool` | `false` | Optional hierarchy browser context menu for child components. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using Header = MaharajaStudio.MSUltimate.Runtime.HeaderAttribute;

public class CombatMechRig : ModularMonoBehaviour
{
    [Title("Combat Mech Rigging Subsystem", "Drag root mech chassis or weapon hardpoints to auto-wire bones")]
    
    [Header("Core Skeletal Sockets")]
    [Tooltip("Drag the Mech Root GameObject here to resolve the head cockpit bone.")]
    [GrabFromChild(nameFilter: "Cockpit*", searchMode: GrabSearchMode.Recursive)]
    public Transform cockpitPivot;

    [Tooltip("Finds the primary weapon mounting socket across descendants.")]
    [GrabFromChild(nameFilter: "*WeaponMount_R*", searchMode: GrabSearchMode.Recursive)]
    public Transform rightWeaponMount;

    [Tooltip("Searches only direct children of the dropped object for an audio emitter.")]
    [GrabFromChild(GrabSearchMode.DirectChildren)]
    public AudioSource engineAudio;

    [Header("Modular Armor Subsystem")]
    [Tooltip("Nested serializable armor slot with auto-grab capabilities.")]
    public ArmorSlot torsoArmor = new ArmorSlot();

    [Header("Damage Colliders (Populated in Bulk)")]
    [Tooltip("Drop the Mech Root here to extract all child BoxColliders into this list at once.")]
    [GrabFromChild(collectionMode: CollectionDropMode.Replace)]
    public List<BoxCollider> armorHitboxes = new List<BoxCollider>();

    [Serializable]
    public class ArmorSlot
    {
        public string armorPlateID = "CHASSIS_PLATING_01";

        [GrabFromChild(nameFilter: "*Plate_Mesh*")]
        public MeshRenderer plateRenderer;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Operational Behavior |
| :--- | :---: | :--- |
| **`[BoxGroup]` / `[TabGroup]`** | ✅ Compatible | Renders seamlessly inside any MSUltimate layout group without overflow. |
| **`[ShowIf]` / `[HideIf]`** | ✅ Compatible | Respects conditional visibility; drag interception is disabled when hidden. |
| **`[ReadOnly]`** | ✅ Compatible | When combined with `[ReadOnly]`, drag-and-drop assignment is prevented. |
| **`[AdvancedList]`** | ✅ Compatible | Intercepts drag-and-drop operations on AdvancedList via `ICollectionDropInterceptorDrawer` while AdvancedList renders its native frame, pagination, search, and animations completely intact. |
| **`[HighlightIfNull]`** | ✅ Compatible | Renders null warning border until a valid parent is dropped to grab the component. |
| **Collections (`List<T>`, `T[]`)** | ✅ Compatible | Native support via `ICollectionElementAttribute` and collection bulk drop engine. |
