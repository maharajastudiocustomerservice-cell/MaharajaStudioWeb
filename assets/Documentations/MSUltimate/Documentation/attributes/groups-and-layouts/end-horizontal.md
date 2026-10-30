# [EndHorizontal]

> Terminates an active imperative horizontal layout row started by [BeginHorizontal], restoring subsequent members to vertical stacking.

---

## 1. Overview & Value Proposition

**What it does:**
Acts as the closing scope delimiter for imperative horizontal layout rows initiated by `[BeginHorizontal]`. All members declared between `[BeginHorizontal]` and the ending boundary are rendered side-by-side in a horizontal row; subsequent members return to standard vertical layout flow.

**The Problem:**
Imperative layout systems require unambiguous boundary markers. Without an explicit closing tag, an open horizontal row would swallow all following properties in the class, squishing them indefinitely into an unreadable horizontal line.

**The Solution:**
Add `[EndHorizontal]` to terminate the row:
- **`IncludeInGroup = true`:** Decorate the final member of the row; it will be included in the horizontal group before the scope closes.
- **`IncludeInGroup = false` (default):** Decorate the first member outside the row; the horizontal scope closes immediately before this member is rendered, placing it cleanly below.
- **Nesting Support:** Supports nested horizontal blocks inside outer cards, tab groups, or vertical stacks.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CoordinatesSetup : MonoBehaviour
{
    [BeginHorizontal]
    public float minX = 0f;

    // IncludeInGroup = true includes maxX in the horizontal row and then closes it
    [EndHorizontal(IncludeInGroup = true)]
    public float maxX = 100f;

    // Stacks normally in standard vertical layout below the row
    public float depthZ = 50f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any member closing or succeeding a horizontal row scope |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | Handled natively by MSUltimate Inspector layout engine |

---

## 4. Constructors & Parameters

```csharp
public EndHorizontalAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IncludeInGroup` | `bool` | `false` | When `true`, includes the decorated member inside the horizontal row before closing. When `false`, closes the row prior to drawing the member. |
| `Visible` | `bool` | `false` | Whether this ending marker element itself has a visual representation in the visual tree. |
| `Category` | `AttributeCategory`| `LayoutGroup` | Categorizes this attribute as a layout scope delimiter. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerCameraRig : MonoBehaviour
{
    [Header("Horizontal Field Row")]
    [BeginHorizontal(Gap = 12f, Box = true, Padding = 6f)]
    public float fovNormal = 60f;

    [EndHorizontal(IncludeInGroup = true)]
    public float fovZoomed = 35f;

    [Header("Subsequent Vertically Stacked Fields")]
    public float transitionSpeed = 5.0f;
    public bool enableCameraShake = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BeginHorizontal]` | Mandatory Pair | Must always follow an earlier `[BeginHorizontal]` declaration. |
| `[Button]` | Supported | Can decorate a method button with `IncludeInGroup = true` to close a horizontal button bar. |
| `[BoxGroup]` | Supported | Functions cleanly inside surrounding box groups. |
