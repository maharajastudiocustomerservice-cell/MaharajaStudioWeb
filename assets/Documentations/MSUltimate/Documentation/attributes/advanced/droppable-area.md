# [DroppableArea]

> Creates a prominent, styled drag-and-drop landing target in the Inspector with type validation, custom highlights, placement options, and drop callbacks.

---

## 1. Overview & Value Proposition

**What it does:**
Creates a large, clear drag-and-drop landing box in the Inspector so you can easily drop single assets or bulk collections into your fields.

**The Problem:**
In standard Unity, dragging audio clips, textures, or prefabs into tiny 16-pixel object fields is frustrating. You have to aim carefully with your mouse, and if you are filling an array with 10+ assets, you often miss the field or drag things into the wrong slot.

**The Solution:**
Add `[DroppableArea]` above any object reference or collection. You get a spacious, easy-to-hit drop zone right in your component:
- **Big Landing Target:** Never miss a drop again with a clearly marked, styled drop zone.
- **Bulk Drops for Lists:** Drag 20 audio clips or prefabs at once from your Project window and drop them directly onto the box to auto-populate the list.
- **Visual Hover Feedback:** The box lights up in green or blue when your mouse hovers over it with valid assets.
- **Automatic Type Checking:** Rejects incompatible asset types automatically so invalid objects can't be assigned by mistake.
- **Custom Placement:** Place the drop zone `Top`, `Bottom`, `Left`, or `Right` relative to the property field.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioPlaylist : MonoBehaviour
{
    [DroppableArea("Drop AudioClips Here", "Accepts .wav, .mp3, .ogg", 70f)]
    public AudioClip[] backgroundTracks;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `UnityEngine.Object`, Components, Prefabs, Collections (`List<T>`, `T[]`) |
| **Collection Interception** | Supported (`ICollectionInterceptorAttribute`) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public DroppableAreaAttribute()
public DroppableAreaAttribute(string text)
public DroppableAreaAttribute(string text, string subtext, float height = 60f)
public DroppableAreaAttribute(params Type[] acceptedTypes)
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `EnableCollectionInterception` | `bool` | `true` | Whether drag-and-drop interception on collection fields is enabled. |
| `ReplaceCollectionOnDrop` | `bool` | `false` | If true, dropping objects into a collection replaces all existing items instead of appending. |
| `Text` | `string` | `"Drop Items Here"` | Primary heading instruction displayed inside the drop zone. |
| `Subtext` | `string` | `""` | Subtitle description providing format or type hints. |
| `Height` | `float` | `60f` | Total pixel height of the landing drop zone box. |
| `Width` | `float` | `-1f` | Total width in pixels (`-1` auto-fits and stretches to available width). |
| `NormalColorHex` | `string` | `"#2c3e5066"` | Idle background color of the zone in hex with alpha. |
| `HighlightColorHex` | `string` | `"#3498db66"` | Highlight color when valid objects are dragged over the box. |
| `BorderColorHex` | `string` | `"#7f8c8d"` | Border color outline around the drop target. |
| `BorderWidth` | `float` | `1f` | Border outline stroke thickness in pixels. |
| `BorderRadius` | `float` | `4f` | Corner rounding radius of the drop target. |
| `AcceptedTypes` | `Type[]` | `null` | Explicit allowed types. When `null` or empty, allows all types compatible with the field. |
| `AllowSceneObjects` | `bool` | `true` | Whether GameObjects/Components from the active scene hierarchy can be dropped. |
| `OnDropCallback` | `string` | `""` | Name of method invoked on target object upon successful asset drop. |
| `Icon` | `string` | `"d_Project"` | Unity editor icon name rendered inside the drop zone. |
| `Alignment` | `UiAlignment` | `UiAlignment.Stretch` | Horizontal alignment of the dropzone (`Left`, `Center`, `Right`, `Stretch`). |
| `Placement` | `DropAreaPlacement` | `DropAreaPlacement.Top` | Placement relative to field control (`Top`, `Bottom`, `Left`, `Right`). |
| `FullWidth` | `bool` | `false` | Expands the dropzone across the full width of the inspector. |
| `AboveGroup` | `bool` | `false` | Renders the dropzone above the parent layout group if applicable. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LootTableConfig : MonoBehaviour
{
    [BoxGroup("Loot Drops", Box = true)]
    [DroppableArea(
        "Drop Loot Prefabs Here", 
        "Accepts Weapon & Armor GameObjects", 
        80f,
        HighlightColorHex = "#27ae6088",
        Icon = "d_Prefab Icon",
        OnDropCallback = nameof(OnLootAssetsDropped)
    )]
    [Tooltip("Collection of prefabs eligible for random drops.")]
    public List<GameObject> droppableItemPrefabs = new List<GameObject>();

    private void OnLootAssetsDropped()
    {
        Debug.Log($"[LootTableConfig] Registered {droppableItemPrefabs.Count} items.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Works cleanly inside `[BoxGroup]` and `[VerticalGroup]`.
- **Collection Handling:** When placed above an array or `List<T>`, dropping multiple files appends all dropped items into the collection automatically.
- **Callbacks:** The optional `OnDropCallback` executes immediately after serialized properties are updated and dirty flags are marked.
