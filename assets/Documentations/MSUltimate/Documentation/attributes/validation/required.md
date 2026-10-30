# [Required]

> Validates that an object reference or string field is assigned, displaying a high-priority error message box if null or empty.

---

## 1. Overview & Value Proposition

**What it does:**
Checks that an object reference, component, asset, or string field contains a valid value. If the reference is null or string is empty, it renders a prominent error box directly beneath the field with customizable message text, font sizing, padding, and alert coloring.

**The Problem:**
Missing references are the #1 cause of runtime crashes (`NullReferenceException`) in Unity projects. Standard inspectors offer no warning when essential references are left unassigned.

**The Solution:**
Add `[Required]` to any reference or string field:
- **Immediate Warning:** Prominently alerts developers inside the Inspector before entering Play Mode.
- **Custom Explanations:** Explain exactly why the field is required and where to find the needed asset.
- **Visual Customization:** Customize text color, error background, padding, and font size.
- **Collection Elements:** Validates items in lists and arrays with individual callouts.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerCameraRig : MonoBehaviour
{
    [Required("Target camera transform must be assigned for tracking!")]
    public Camera mainCamera;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `UnityEngine.Object`, `string`, interfaces, classes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public RequiredAttribute(string message = "This field is required and cannot be null.")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `message` | `string` | `"This field is required and cannot be null."` | Error message text displayed when unassigned. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | *(Constructor)* | Custom error message displayed when unassigned. |
| `ErrorColor` | `string` | `null` | Hex color code for the error message text. |
| `ErrorBackgroundColor` | `string` | `null` | Hex color code for the error box background plate. |
| `FontSize` | `int` | `0` | Font size for the error text (`0` = system default). |
| `Padding` | `float` | `0f` | Internal padding inside the error callout. |
| `Margin` | `float` | `5f` | Margin spacing around the error callout. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AudioBgmManager : MonoBehaviour
{
    [Header("Mandatory Audio Track")]
    [Required("Main background music clip is missing!", 
        ErrorColor = "#FFFFFF", 
        ErrorBackgroundColor = "#c0392b", 
        FontSize = 11,
        Padding = 6f
    )]
    public AudioClip backgroundMusic;

    [Header("Player Target Tag")]
    [Required("Player identification tag cannot be empty!")]
    public string playerTag = "Player";
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Error banners render neatly inside layout cards. |
| `[ShowIf]` | Supported | Error message is automatically suppressed if field is hidden. |
| `ICollectionElement` | Supported | Validates each entry in arrays or lists of object references. |
