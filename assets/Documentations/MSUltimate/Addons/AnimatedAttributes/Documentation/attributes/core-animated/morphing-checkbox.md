# [MorphingCheckbox]

> Renders boolean fields with a vector-drawn icon that smoothly morphs vector paths between checkmark and cross states with spring animation.

---

## 1. Overview & Value Proposition

**What it does:**
Replaces the standard binary checkbox with a vector path visual that smoothly interpolates and morphs its geometry: morphing from a red "✕" when false into a crisp green "✓" when true. Powered by vector stroke interpolation with customizable colors, line thickness, and transition duration.

**The Problem:**
Standard Unity checkboxes swap sprites abruptly without any intermediate animation, feeling mechanical and uninspired.

**The Solution:**
Add `[MorphingCheckbox]` to any boolean field:
- **Smooth Vector Path Morphing:** The stroke smoothly bends and animates from a cross into a checkmark.
- **Color Transitions:** Interpolates smoothly between `UncheckedColor` (red) and `CheckedColor` (green).
- **Line Weight Control:** Configure stroke width (`LineThickness = 3px`) for delicate or bold vector graphics.
- **Collection Elements:** Renders morphing icons for boolean items inside lists and arrays (`ICollectionElementAttribute`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class QuestObjective : MonoBehaviour
{
    [MorphingCheckbox(CheckedColor = "#2ecc71", UncheckedColor = "#e74c3c", MorphDuration = 250f)]
    public bool isObjectiveComplete = false;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `bool` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public MorphingCheckboxAttribute()
```

*Attribute initializes with standard green checkmark and red cross morphing; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CheckedColor` | `string` | `"#4CAF50"` | Hex color string for the checkmark when `true`. |
| `UncheckedColor` | `string` | `"#F44336"` | Hex color string for the cross icon when `false`. |
| `LineThickness` | `float` | `3f` | Stroke thickness in pixels for the morphing vector lines. |
| `MorphDuration` | `float` | `300f` | Morph transition duration in milliseconds. |
| `IsEditable` | `bool` | `true` | Whether the morphing checkbox is interactively clickable. |
| `Interactive` | `bool` | `true` | Alias for `IsEditable`. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ChecklistManager : MonoBehaviour
{
    [Header("Level Readiness Checks")]
    [MorphingCheckbox(CheckedColor = "#00FF88", UncheckedColor = "#FF3366", LineThickness = 4f)]
    public bool hasNavMeshBaked = true;

    [MorphingCheckbox(CheckedColor = "#00FF88", UncheckedColor = "#FF3366", LineThickness = 4f)]
    public bool hasLightingBaked = false;

    [Header("Item Completion Checklist")]
    [MorphingCheckbox]
    public List<bool> taskStatusList = new List<bool>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Morphing vector icons sit cleanly inside group cards. |
| `ICollectionElement` | Supported | Morphs individual checkboxes inside boolean collections. |
| Category | PrimaryDrawer | Acts as an animated primary field drawer for boolean fields. |
