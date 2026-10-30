# [DetailedInfoBox]

> Renders an informative banner card with a distinct icon, bold title, and descriptive body message.

---

## 1. Overview & Value Proposition

**What it does:**
Adds an expandable tutorial or documentation card (with title, message, and icon) above a field to guide designers on how to use it.

**The Problem:**
Unity's built-in `[HelpBox]` is plain, single-level, and cannot be collapsed. Long documentation notes permanently consume vertical screen space, pushing critical gameplay variables down the page.

**The Solution:**
Add `[DetailedInfoBox]` above any member:
- **Collapsible Content:** Keeps the Inspector compact while making deep documentation accessible with a single click.
- **Title & Message Split:** Separate bold headline from detailed instructional text.
- **Message Severity Themes:** Support `Info`, `Warning`, `Error`, and `None` styling with matching icons.
- **Dynamic Visibility:** Conditionally show instructions only when specific settings or states are active (`VisibleIf`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SpawnerGuide : MonoBehaviour
{
    [DetailedInfoBox("Wave Spawning Rules", "Ensure spawn points have valid NavMesh surfaces before enabling endless mode.", InspectorMessageType.Info)]
    public bool enableEndlessMode;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any inspectable member |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public DetailedInfoBoxAttribute(string title, string message, InspectorMessageType type = InspectorMessageType.Info)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `title` | `string` | *(Required)* | Header title text displayed prominently at the top of the box. |
| `message` | `string` | *(Required)* | Detailed body text explaining guidelines, usage instructions, or warnings. |
| `type` | `InspectorMessageType` | `InspectorMessageType.Info` | Message icon and border theme (`None`, `Info`, `Warning`, `Error`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | *(Required)* | Bold title header text. |
| `Message` | `string` | *(Required)* | Body message text. |
| `Type` | `InspectorMessageType` | `InspectorMessageType.Info` | Severity icon style (`None`, `Info`, `Warning`, `Error`). |
| `VisibleIf` | `string` | `null` | Optional member condition controlling when the info box is drawn. |
| `TitleColor` | `string` | `null` | Hex color code for the title header text. |
| `MessageColor` | `string` | `null` | Hex color code for the body description text. |
| `BackgroundColor` | `string` | `null` | Background container hex color. |
| `BorderColor` | `string` | `null` | Border stroke hex color. |
| `BorderRadius` | `float` | `3f` | Box corner rounding radius in pixels. |
| `BorderWidth` | `float` | `1f` | Border stroke thickness in pixels. |
| `FullWidth` | `bool` | `false` | Stretches banner across full width of the inspector window. |
| `AboveGroup` | `bool` | `false` | Renders the banner outside and above parent group containers. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ShaderWarmupController : MonoBehaviour
{
    [DetailedInfoBox(
        "Performance Notice",
        "Pre-warming complex compute shaders on mobile devices may cause initial hitching. Limit pre-warming to loading screens.",
        InspectorMessageType.Warning,
        BorderRadius = 6f,
        BackgroundColor = "#2C2010"
    )]
    public bool prewarmOnStartup = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[InfoBox]` | Alternative | Use `[InfoBox]` for compact one-liners; use `[DetailedInfoBox]` for titled cards with body text. |
| `[BoxGroup]` | Supported | Nests cleanly inside box containers. |
| `[ShowIf]` | Supported | Automatically aligns with visibility rules. |
