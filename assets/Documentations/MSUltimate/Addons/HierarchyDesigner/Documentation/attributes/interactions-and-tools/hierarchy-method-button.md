# [HierarchyMethodButton]

> Renders a clickable action button directly on the hierarchy row to invoke parameterless component methods with one click.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyMethodButton]` attaches to parameterless methods on MonoBehaviour components and embeds a clickable button directly on the right edge of the hierarchy row. Driven by `HierarchyMethodButtonRenderer`, clicking the button invokes the method via reflection, records full Unity Undo operations (`Undo.RecordObject`), and marks the component dirty. It supports custom button labels (`Text`), color themes (`ButtonColor`, `TextColor`), auto-sizing or fixed widths, and custom horizontal placement.

**The Problem:**
Triggering utility or debug actions (e.g., `ResetPosition()`, `RespawnEnemies()`, `BakeLightingProbe()`, `ClearInventory()`, `TestAttack()`) usually requires selecting the GameObject, scrolling past dozens of inspector fields to find a custom button or context menu, and clicking it. When testing frequently, this workflow is repetitive and slow.

**The Solution:**
Decorating methods with `[HierarchyMethodButton]`:
- **Single-Click In-Hierarchy Execution:** Run utility, debug, or editor actions directly from the hierarchy row.
- **Visual Button Customization:** Customize button labels, colors, and sizing for clear differentiation.
- **Full Undo Registration:** Integrates with Unity's undo manager in Edit Mode, ensuring state changes can be rolled back with `Ctrl+Z`.
- **Zero Runtime Overhead:** Buttons exist solely within the Editor GUI lifecycle and do not impact standalone builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class SpawnerController : MonoBehaviour
{
    public GameObject enemyPrefab;

    [HierarchyMethodButton(Text = "Spawn Wave", ButtonColor = "#3B82F6")]
    public void TriggerWave()
    {
        Debug.Log("Spawning new enemy wave!");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Method` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyMethodButtonRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyMethodButtonAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | `"Execute"` | Button label text to display. If left empty, defaults to the method name. |
| `IconName` | `string` | `""` | Optional built-in Unity editor icon name to display on the button. |
| `ButtonColor` | `string` | `"#3B5998"` | Hex color of the button background. |
| `TextColor` | `string` | `"#FFFFFF"` | Hex color of the button label text. |
| `Width` | `float` | `0f` | Width of the button in pixels, or `0` for auto-fitting to text width. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the button remains visible and clickable during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class LevelHazardManager : MonoBehaviour
{
    [Header("Hazard Configuration")]
    public float explosionRadius = 15f;
    public bool isArmed = true;

    [HierarchyMethodButton(
        Text = "Detonate", 
        ButtonColor = "#DC2626", 
        TextColor = "#FEF2F2", 
        Width = 65f, 
        XOffset = 6f)]
    public void DetonateAllTraps()
    {
        Debug.LogWarning("Detonating all active level traps!");
    }

    [HierarchyMethodButton(
        Text = "Reset", 
        ButtonColor = "#4B5563", 
        TextColor = "#F3F4F6", 
        Width = 50f, 
        XOffset = 75f)]
    public void ResetTraps()
    {
        isArmed = true;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyToggle]`** | High | Use toggles for boolean states and method buttons for one-shot executable actions. |
| **`[HierarchyStatusDot]`** | High | Display status dots alongside buttons to indicate whether an action is ready to execute. |
| **Method Signature** | Required | Target methods must be parameterless (`void Method()`) to be invoked via button click. |
| **Hierarchy Selection** | High | Consumes mouse click events inside the button rect to prevent unwanted GameObject selection or renaming. |
