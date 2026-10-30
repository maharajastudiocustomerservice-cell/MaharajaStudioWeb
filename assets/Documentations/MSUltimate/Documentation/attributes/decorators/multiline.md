# [Multiline]

> Renders string fields as multi-line text input areas with custom visible line counts and box styling.

---

## 1. Overview & Value Proposition

**What it does:**
Expands a string field into a comfortable multi-line text editor with customizable visible line counts, background colors, and border styling.

**The Problem:**
Unity's built-in `[Multiline]` and `[TextArea]` attributes only provide fixed, unstyled text boxes. They cannot be custom-styled with theme borders, colored text, or custom backgrounds, and don't support collection cascading when editing lists of text lines.

**The Solution:**
Add `[Multiline]` to any string field:
- **Configurable Visible Lines:** Set exact line count (default `3`) to fit dialogues, descriptions, or patch notes.
- **Rich Card Styling:** Customize background colors, border colors, corner radius, and text colors.
- **Collection Cascading:** Automatically styles string elements inside `List<string>` and string arrays.
- **Smooth Word-Wrap:** Handles text wrapping smoothly across varying inspector column widths.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NPCData : MonoBehaviour
{
    [Multiline(4)]
    public string greetingDialogue = "Welcome traveler!\nWhat brings you to our village?";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string`, `List<string>`, `string[]` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public MultilineAttribute(int lines = 3)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `lines` | `int` | `3` | Number of text lines displayed by the input box. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Lines` | `int` | `3` | Number of visible text lines in the editor area. |
| `TextColor` | `string` | `null` | Hex text color string. |
| `BackgroundColor` | `string` | `null` | Hex background color behind the text area. |
| `BorderColor` | `string` | `null` | Hex border outline color. |
| `BorderWidth` | `float` | `0f` | Border outline line thickness in pixels. |
| `BorderRadius` | `float` | `0f` | Corner rounding radius in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class QuestLogData : MonoBehaviour
{
    [Header("Quest Briefing")]
    [Multiline(lines: 5, BackgroundColor = "#1a1a24", BorderColor = "#3d3d52", BorderWidth = 1f, BorderRadius = 4f)]
    public string questStoryLog;

    [Header("Objective Journal Steps")]
    [Multiline(lines: 2)]
    public List<string> journalCheckpoints = new List<string>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[HideLabel]` | Recommended | Pairs together so the multi-line editor spans edge-to-edge. |
| `[BoxGroup]` | Supported | Integrates cleanly inside grouped cards and tabs. |
| `[ReadOnly]` | Supported | Converts into a clean, selectable, non-editable text display block. |
