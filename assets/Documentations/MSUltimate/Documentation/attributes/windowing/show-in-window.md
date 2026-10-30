# [ShowInWindow]

> Adds a pop-out button beside any field, property, or method to inspect the target object in a standalone floating Modular Window.

---

## 1. Overview & Value Proposition

**What it does:**
Renders an inline action button (e.g. `"Inspect ↗"`) beside an object reference, nested class, or method. Clicking the button pops out the target object (ScriptableObject, Component, or sub-asset) into a dedicated standalone floating window for focused editing.

**The Problem:**
Editing complex nested ScriptableObjects or referenced components often requires pinging them in the Project window or losing your current Inspector context to view their details.

**The Solution:**
Add `[ShowInWindow]` to any reference or method:
- **Instant Pop-Out Inspection:** Open referenced data in a dedicated floating panel with one click.
- **Side-by-Side Editing:** Keep your main component open while tweaking referenced assets alongside it.
- **Custom Dimensions:** Configure initial pop-out window width and height.
- **Custom Button Styling:** Customize button label, tooltip, and hex highlight color.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Windowing;

public class CharacterSheet : MonoBehaviour
{
    [ShowInWindow("Character Stats Config", width: 600f, height: 500f)]
    public ScriptableObject combatStatsAsset;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | `ScriptableObject`, `Component`, `GameObject`, serialized reference classes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ShowInWindowAttribute()
public ShowInWindowAttribute(string title, float width = 500f, float height = 450f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `title` | `string` | `null` | Custom window title (defaults to property name if omitted). |
| `width` | `float` | `500f` | Initial width of the pop-out window in pixels. |
| `height` | `float` | `450f` | Initial height of the pop-out window in pixels. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | *(Constructor)* | Title text displayed in the pop-out window tab. |
| `Width` | `float` | `500f` | Initial width of the pop-out window in pixels. |
| `Height` | `float` | `450f` | Initial height of the pop-out window in pixels. |
| `IsUtility` | `bool` | `true` | Whether the window opens as a floating utility window (always on top). |
| `ButtonLabel` | `string` | `"Inspect ↗"` | Label text displayed on the inspect action button. |
| `ButtonTooltip` | `string` | `"Open in a standalone Modular Window"` | Tooltip text displayed on hover. |
| `ButtonColorHex` | `string` | `null` | Hex color string for the inspect button text / icon. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime.Windowing;

public class LevelSpawner : MonoBehaviour
{
    [Header("Enemy Encounter Definition")]
    [ShowInWindow(
        title: "Wave Configuration", 
        width: 700f, 
        height: 550f, 
        ButtonLabel = "Open Editor ↗", 
        ButtonColorHex = "#3498db"
    )]
    public ScriptableObject waveConfigAsset;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Inspect button aligns cleanly inside group cards. |
| `[ShowIf]` | Supported | Inspect button hides dynamically when field is hidden. |
| Category | PostDecorator | Operates in the PostDecorator execution phase beside the field control. |
