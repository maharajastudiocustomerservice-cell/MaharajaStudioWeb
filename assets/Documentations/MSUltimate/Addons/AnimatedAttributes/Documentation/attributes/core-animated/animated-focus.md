# [AnimatedFocus]

> Smoothly animates border, background, and text styling when a field gains or loses keyboard/cursor focus.

---

## 1. Overview & Value Proposition

**What it does:**
Applies smooth animated visual feedback whenever the user clicks into or focuses a field. Transitions border highlight color, border width, corner rounding, and background tint using hardware-accelerated UI Toolkit transitions.

**The Problem:**
Standard Unity inspector fields provide minimal focus feedback, making it easy to lose track of which field is currently active when navigating large data forms or editing dense spreadsheets.

**The Solution:**
Add `[AnimatedFocus]` to any field:
- **Instant Active State Feedback:** A sleek glowing border highlights the active input element.
- **Configurable Theming:** Customize border color (`FocusBorderColor`), background tint, and text color.
- **Corner & Border Control:** Adjust `BorderRadius` and `BorderWidth` to match your project aesthetic.
- **Smooth Easing:** Configurable transition speed (`TransitionDuration = 200ms`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class UserProfile : MonoBehaviour
{
    [AnimatedFocus(FocusBorderColor = "#00FF88", BorderWidth = 2.5f, TransitionDuration = 150f)]
    public string username = "Player1";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public AnimatedFocusAttribute()
```

*Attribute initializes with standard focus styling; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `FocusBorderColor` | `string` | `"#589DF6"` | Hex color string for border when field is focused. |
| `BackgroundColorOnFocus` | `string` | `""` | Hex color string for background when focused (empty leaves unchanged). |
| `TextColorOnFocus` | `string` | `""` | Hex color string for text when focused (empty leaves unchanged). |
| `BorderWidth` | `float` | `2f` | Border width in pixels when focused. |
| `BorderRadius` | `float` | `3f` | Corner radius in pixels when focused. |
| `TransitionDuration` | `float` | `200f` | Transition duration in milliseconds. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ServerConnectionForm : MonoBehaviour
{
    [Header("Network Host Configuration")]
    [AnimatedFocus(
        FocusBorderColor = "#3498db", 
        BackgroundColorOnFocus = "#1a252f", 
        BorderWidth = 2f, 
        BorderRadius = 4f
    )]
    public string serverHostName = "127.0.0.1";

    [AnimatedFocus(FocusBorderColor = "#2ecc71")]
    public int serverPort = 7777;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[AnimatedHover]` | Supported | Composes seamlessly; hover state yields to focus state when active. |
| `[BoxGroup]` | Supported | Border transitions fit cleanly inside layout cards. |
| Primary Drawers | Supported | Enhances text fields, sliders, and integer inputs. |
