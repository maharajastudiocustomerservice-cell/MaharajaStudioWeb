# [CreateAsset]

> Adds a quick "Create" button next to a ScriptableObject reference field, allowing rapid instantiation and saving of new assets.

---

## 1. Overview & Value Proposition

**What it does:**
Injects an inline "Create New" button directly beside a ScriptableObject field that instantiates and saves a new asset file in one click.

**The Problem:**
Creating a new ScriptableObject configuration asset requires right-clicking in the Project window, navigating multi-level `Create -> Game -> Data -> ...` menus, naming the file, and then dragging it into the inspector field. Repeating this hundreds of times slows down workflow.

**The Solution:**
Add `[CreateAsset]` to any ScriptableObject field:
- **One-Click Instantiation:** Click the create button to instantly generate a new asset and auto-assign it.
- **Configurable Default Name:** Suggests context-aware default file names (e.g. `New Item Data`).
- **Button Styling & Icons:** Customize button colors, icons, fonts, padding, and alignments.
- **Collection Elements:** Functions seamlessly on ScriptableObject elements within lists and arrays.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LootChest : MonoBehaviour
{
    [CreateAsset(DefaultFileName = "ChestLootTable")]
    public LootTableData dropTable;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any `ScriptableObject` reference type |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public CreateAssetAttribute()
```

*This attribute is configured using public object initializer properties.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DefaultFileName` | `string` | `"New Asset"` | Suggested default file name in the OS save dialog. |
| `ButtonText` | `string` | `""` | Optional text label for the create button. |
| `Icon` | `string` | `"d_CreateAddNew"` | Built-in Unity icon name for the button. |
| `ButtonColor` | `string` | `""` | Hex background color for the button. |
| `TextColor` | `string` | `""` | Hex font color for the button text. |
| `BorderColor` | `string` | `""` | Hex border outline color. |
| `BorderWidth` | `float` | `1f` | Border line thickness in pixels. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius in pixels. |
| `Padding` | `float` | `3f` | Internal button padding in pixels. |
| `Height` | `float` | `22f` | Button height in pixels. |
| `Alignment` | `UiAlignment` | `UiAlignment.Right` | Button alignment within row (`Right`, `Left`). |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class DialogueTrigger : MonoBehaviour
{
    [Header("Primary Conversation")]
    [CreateAsset(DefaultFileName = "NewDialogueNode", ButtonText = "New Node", ButtonColor = "#27ae60", TextColor = "#ffffff")]
    public DialogueNodeData primaryConversation;

    [Header("Branching Dialogue Graph")]
    [CreateAsset(DefaultFileName = "DialogueChoice")]
    public List<DialogueChoiceData> conversationBranches = new List<DialogueChoiceData>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[InlineEditor]` | Recommended | Create the new asset in one click, then immediately edit its properties inline! |
| `[BoxGroup]` | Supported | Functions normally inside group containers. |
| `[AssetOnly]` | Compatible | Created asset is saved directly to the Project folder as an asset. |
