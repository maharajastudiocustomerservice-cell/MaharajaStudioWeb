# [EnumToggleButtons]

> Displays enum fields as an interactive segmented button bar or pill toggles instead of a dropdown menu.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms standard enum dropdown menus into a sleek, horizontal segmented button bar or modern rounded pill toggles.

**The Problem:**
Standard enum dropdown menus require two clicks to change an option (one to open the menu, one to pick). For common 2-to-5 choice states (like game modes, weapon types, or difficulty settings), constantly clicking in and out of dropdown menus slows down testing.

**The Solution:**
Add `[EnumToggleButtons]` to any enum field:
- **1-Click Option Selection:** All enum choices are visible at once; switch modes instantly with a single click.
- **[Flags] Multi-Select Bitmasks:** Automatically supports multi-selection when applied to enum types marked with `[Flags]`.
- **Segmented Bar or Pill Styles:** Switch between sleek segmented bars and isolated rounded pill buttons.
- **Theme Customization:** Customize selected and unselected background and text colors to match your studio's UI.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public enum DifficultyLevel { Easy, Normal, Hard, Nightmare }

public class GameConfig : MonoBehaviour
{
    [EnumToggleButtons]
    public DifficultyLevel gameDifficulty = DifficultyLevel.Normal;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any `enum` type (single choice or `[Flags]` bitmask) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public EnumToggleButtonsAttribute(string customLabel = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `customLabel` | `string` | `null` | Custom display label override for the inspector row. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CustomLabel` | `string` | `null` | Custom field label override text. |
| `ShowLabel` | `bool` | `true` | Whether to display the property label before buttons. |
| `UsePillStyle` | `bool` | `false` | Renders buttons as isolated rounded pills instead of a segmented bar. |
| `SelectedColor` | `string` | `"#5973A6"` | Hex background color for selected button(s). |
| `UnselectedColor` | `string` | `"#2D2D2D"` | Hex background color for unselected buttons. |
| `SelectedTextColor` | `string` | `"#FFFFFF"` | Hex font color for active choice text. |
| `UnselectedTextColor` | `string` | `"#D3D3D3"` | Hex font color for inactive choices. |
| `LabelColor` | `string` | `null` | Custom hex color for the property label. |
| `Height` | `float` | `25f` | Height of the toggle buttons in pixels. |
| `LabelWidth` | `float` | `150f` | Width allocated to the field label. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public enum MovementMode { Walk, Run, Sprint, Fly }

[Flags]
public enum DamageElements { None = 0, Fire = 1, Ice = 2, Lightning = 4, Poison = 8 }

public class PlayerCombatSetup : MonoBehaviour
{
    [Header("Locomotion State")]
    [EnumToggleButtons(SelectedColor = "#3498db")]
    public MovementMode defaultLocomotion = MovementMode.Run;

    [Header("Active Enchantments (Flags Bitmask)")]
    [EnumToggleButtons(UsePillStyle = true, SelectedColor = "#e67e22")]
    public DamageElements activeEnchantments = DamageElements.Fire | DamageElements.Lightning;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Adapts cleanly within group containers and tabs. |
| `[ShowIf]` | Supported | Functions as an ideal driver for conditional visibility rules. |
| `[ReadOnly]` | Supported | Renders current choice in active state while disabling clicks. |
