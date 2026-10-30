# [HierarchyKerningText]

> Adjusts character tracking, letter spacing, and casing for the hierarchy label.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyKerningText]` gives editorial typographic control over the GameObject label by adjusting character tracking (letter spacing) in pixels (`LetterSpacing = 3.0f`) and applying text casing transformations (`Uppercase`, `Lowercase`, `TitleCase`, `SmallCaps`, `Spaced`).

**The Problem:**
Unity's built-in Hierarchy window renders GameObject names with standard font metrics and default variable tracking. For UI section headers, architectural parent folders, or AAA cinematics root objects, default text often looks crowded and lacks modern editorial hierarchy.

**The Solution:**
Decorating classes with `[HierarchyKerningText]`:
- **Custom Letter Spacing / Kerning:** Expands or tightens horizontal spacing between adjacent glyphs (`LetterSpacing = 3.0f`) for clean luxury tracking.
- **Automated Text Casing:** Instantly enforces casing standards (e.g. `HierarchyTextCasing.Uppercase` for major category headers) without having to manually rename scene GameObjects.
- **Crisp Custom Tinting:** Applies custom hex color palette styling (`TextColor = "#E0E0E0"`).
- **Bold Typography:** Enhances visual gravity and hierarchy readability.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyKerningText(LetterSpacing = 4.0f, Casing = HierarchyTextCasing.Uppercase, TextColor = "#F8FAFC")]
public class CinematicsRootDirector : MonoBehaviour
{
    public float sceneDuration = 45f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` \| `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyKerningTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyKerningTextAttribute()
```

- Standard parameterless constructor. Kerning distance, casing mode, and font settings are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `LetterSpacing` | `float` | `3.0f` | Horizontal spacing in pixels between adjacent characters. |
| `Casing` | `HierarchyTextCasing` | `Uppercase` | Text casing mode: `None`, `Uppercase`, `Lowercase`, `Spaced`, `SmallCaps`, `TitleCase`. |
| `TextColor` | `string` | `"#E0E0E0"` | Hex color string for the rendered characters. |
| `Bold` | `bool` | `true` | Whether to render characters with bold font weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether custom kerning remains active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyKerningText(
    LetterSpacing = 5.0f, 
    Casing = HierarchyTextCasing.Uppercase, 
    TextColor = "#E2E8F0", 
    Bold = true)]
public class WorldAudioZoneManager : MonoBehaviour
{
    [Header("Audio Settings")]
    public AudioReverbZone reverbZone;
    public float ambientVolume = 0.8f;
    public bool enableSpatialAudio = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyFolder]`** | High | Excellent pairing for virtual folders to give organizational headers a spacious, modern editorial look. |
| **`[HierarchyTextShadow]`** | High | Complements wide letter spacing with crisp drop shadows for elevated contrast. |
| **`[HierarchyChildCounter]`** | High | Displays neatly alongside child counter badges and tree branches. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with other text coloring attributes as kerning renders characters via custom spacing passes. |
