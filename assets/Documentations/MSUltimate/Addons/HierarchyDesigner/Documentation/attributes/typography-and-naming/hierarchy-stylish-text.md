# [HierarchyStylishText]

> Applies text casing, decorative framing brackets, font styling, and optional background pill boxes to hierarchy labels.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyStylishText]` provides an all-in-one typography and framing suite for GameObject hierarchy labels. It combines automated text casing (`Uppercase`, `SmallCaps`, `TitleCase`, etc.), decorative unicode framing glyphs (`[ ]`, `{ }`, `» «`, `✦ ✦`, `◈ ◈`, `//`), custom font sizing, bold/italic weights, and optional background pill boxes with rounded corners (`BorderRadius`).

**The Problem:**
Creating distinct visual categories in large scene hierarchies usually requires manually typing special symbols into GameObject names (e.g. `[MANAGERS]`, `--- ENVIRONMENT ---`, `>> UI <<`). This pollutes runtime object names, creates inconsistencies across team members, and clutters asset references.

**The Solution:**
Decorating components with `[HierarchyStylishText]`:
- **Six Casing Modes:** Convert names automatically to `Uppercase`, `Lowercase`, `Spaced`, `SmallCaps`, or `TitleCase` without modifying the actual `gameObject.name`.
- **Decorative Framing Glyphs:** Surround names with framing brackets (`Brackets`, `Curly`, `Arrows`, `Stars`, `Cyber`, or `Slash`).
- **Background Pill Box:** Draw an optional rounded container box (`BackgroundColor = "#1E293B"`, `BorderRadius = 4f`) behind the label.
- **Custom Prefix & Suffix:** Prepend and append custom string tags directly in the editor display.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyStylishText(
    Casing = HierarchyTextCasing.Uppercase, 
    Frame = HierarchyTextFrame.Cyber, 
    TextColor = "#38BDF8", 
    Bold = true)]
public class CoreSystemManager : MonoBehaviour
{
    public bool isInitialized = true;
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
| **Render Engine** | `HierarchyStylishTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyStylishTextAttribute()
```

- Standard parameterless constructor. Casing, frames, colors, and background box properties are configured via object initializers.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Casing` | `HierarchyTextCasing` | `None` | Text casing transformation: `None`, `Uppercase`, `Lowercase`, `Spaced`, `SmallCaps`, `TitleCase`. |
| `Frame` | `HierarchyTextFrame` | `None` | Framing glyphs: `None`, `Brackets` (`[ ]`), `Curly` (`{ }`), `Arrows` (`» «`), `Stars` (`✦ ✦`), `Cyber` (`◈ ◈`), `Slash` (`// `). |
| `Bold` | `bool` | `true` | Whether to render the label characters with bold font weight. |
| `Italic` | `bool` | `false` | Whether to render the label characters in italics. |
| `FontSize` | `int` | `0` | Custom font size in pixels (0 uses default hierarchy size). |
| `TextColor` | `string` | `"#E0E0E0"` | Hex color string for the label text. |
| `Prefix` | `string` | `""` | Optional prefix string prepended to the name. |
| `Suffix` | `string` | `""` | Optional suffix string appended to the name. |
| `BackgroundColor` | `string` | `""` | Optional hex background color for a rounded pill box behind the text. |
| `BorderRadius` | `float` | `3f` | Corner radius in pixels of the background pill box. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether styling remains active during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyStylishText(
    Casing = HierarchyTextCasing.Uppercase, 
    Frame = HierarchyTextFrame.Stars, 
    TextColor = "#FBBF24", 
    BackgroundColor = "#1E293B", 
    BorderRadius = 4f, 
    Bold = true, 
    FontSize = 13)]
public class VIPGuestSpawner : MonoBehaviour
{
    [Header("VIP Settings")]
    public string guestTier = "ROYAL";
    public float arrivalInterval = 120.0f;
    public Transform entranceSpawnPoint;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyFolder]`** | High | Apply stylish frames and casing to organizational virtual folders. |
| **`[HierarchyTooltip]`** | High | Pair framed headers with informative developer notes on hover. |
| **`[HierarchyChildCounter]`** | High | Sits cleanly alongside child counter pills and badges. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with standard text color attributes as stylish text completely handles text rendering. |
