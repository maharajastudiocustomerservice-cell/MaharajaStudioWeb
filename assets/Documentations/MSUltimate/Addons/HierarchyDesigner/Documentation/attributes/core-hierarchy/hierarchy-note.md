# [HierarchyNote]

> Attaches a documentary note and indicator icon to the hierarchy row with hover tooltip and inline text preview.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyNote]` allows developers and technical designers to anchor production reminders, architectural instructions, and warning notes directly to GameObjects in the Hierarchy window. Driven by `HierarchyNoteRenderer`, it renders a styled indicator icon (`IconName = "d_UnityEditor.InspectorWindow"`, `IconColor = "#FFDD88"`) on the hierarchy row. Hovering over the icon displays the full message as an editor tooltip, and an optional truncated inline snippet can be rendered directly beside the icon (`ShowInlinePreview = true`).

**The Problem:**
In multi-developer teams, scenes quickly fill with complex prefab rigs, lighting rigs, and cutscene triggers that require context (e.g. "Do not disable this collider," "Baked lighting probe anchor," "WIP - Waiting for art pass"). Without inline documentation, teams rely on external wikis or sticky comments inside C# code that level designers rarely read.

**The Solution:**
Decorating components with `[HierarchyNote]`:
- **Contextual Scene Documentation:** Embed production notes directly where developers interact with objects daily.
- **Rich Hover Tooltips:** Read complete multi-line instructions without opening the Inspector or checking source code.
- **Optional Inline Text Snippet:** Show the first 24+ characters inline to identify key notes at a glance.
- **Custom Iconography & Tints:** Choose distinct Unity icons (e.g., warning icons, info tags, bookmark symbols) and colors.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyNote("Main spawn point. Do not modify transform without checking NavMesh bounds!")]
public class PlayerSpawnAnchor : MonoBehaviour
{
    public int teamId = 1;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyNoteRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyNoteAttribute(string text)
```

- `text`: Primary note content shown in full on hover tooltip and in the inline preview.

```csharp
public HierarchyNoteAttribute()
```

- Parameterless constructor for property-based configuration.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | `""` | Note text displayed in full on the hover tooltip. |
| `IconName` | `string` | `"d_UnityEditor.InspectorWindow"` | Built-in Unity icon name for the note indicator. |
| `IconColor` | `string` | `"#FFDD88"` | Hex color tint applied to the note icon. |
| `IconSize` | `float` | `13f` | Size of the note icon in pixels. |
| `ShowInlinePreview` | `bool` | `false` | Whether to display a truncated text snippet beside the icon. |
| `PreviewLength` | `int` | `24` | Maximum character count shown in the inline preview before adding `"..."`. |
| `PreviewColor` | `string` | `"#887766"` | Hex color of the inline preview text. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the note indicator remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyNote(
    "Cinematic trigger zone: Triggers act 2 cutscene. Requires AudioListener on Player camera.", 
    IconName = "console.warnicon.sml", 
    IconColor = "#F59E0B", 
    ShowInlinePreview = true, 
    PreviewLength = 28, 
    PreviewColor = "#D97706", 
    XOffset = 6f)]
public class StoryTriggerZone : MonoBehaviour
{
    public string cutsceneSequenceId = "ACT2_INTRO";
    public bool triggerOnce = true;
    public float triggerDelay = 0.5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchySeparator]`** | High | Use separators for high-level scene layout and notes for specific component instructions. |
| **`[HierarchyLock]`** | High | Pair notes with lock attributes to explain why an object has been locked against editing. |
| **`[HierarchyIcon]`** | High | `HierarchyNote` places its icon on the far right, avoiding overlap with type icons on the left. |
| **Team Workflow** | High | Notes persist in scene metadata without modifying serialized gameplay fields or adding runtime overhead. |
