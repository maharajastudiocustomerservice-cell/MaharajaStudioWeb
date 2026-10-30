# [EndSplitPane]

> Terminates an active dual-pane split layout scope started by [BeginSplitPane], restoring subsequent members to default layout flow.

---

## 1. Overview & Value Proposition

**What it does:**
Closes the active dual-pane container scope opened by `[BeginSplitPane]`. All subsequent fields, properties, and methods declared after `[EndSplitPane]` are rendered outside the split container in standard full-width vertical layout flow.

**The Problem:**
Without an explicit closing boundary, all fields declared below a split container would continue to be captured inside Pane 2, making it impossible to add full-width inspector sections (like global settings or master action buttons) below the split pane.

**The Solution:**
Place `[EndSplitPane]` on the final member intended for Pane 2:
- **Clean Container Termination:** Explicitly finishes the resizable split pane view after rendering the decorated member.
- **Post-Split Alignment:** Subsequent members span the full width of the inspector window.
- **Robust Error Handling:** Defensively recovers if nested incorrectly without throwing GUI exceptions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class InventoryInspector : MonoBehaviour
{
    // Pane 1: Category Selection
    [BeginSplitPane("InventorySplit")]
    public string categoryFilter = "Weapons";

    // Pane 2: Properties
    [BeginSplitPane("InventorySplit")] // Transitions to Pane 2
    [EndSplitPane] // Ends Pane 2 and closes the split pane container
    public int maxCarryWeight = 100;

    // Renders full-width below the split pane
    public bool enableEncumbrance = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any member closing a split container scope |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | Handled natively by MSUltimate Inspector layout engine |

---

## 4. Constructors & Parameters

```csharp
public EndSplitPaneAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `AttributeCategory`| `LayoutGroup` | Category tag identifying this attribute as a layout scope terminator. |
| `Order` | `int` | `0` | Drawing order priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterCustomizer : MonoBehaviour
{
    // Pane 1: Preset Slots
    [BeginSplitPane("CustomizerSplit", 
        InitialSplitterPosition = 200f, 
        Pane1Title = "Preset Slots", 
        Pane2Title = "Mesh Configuration"
    )]
    public string activePresetName = "Warrior_Default";
    public Color hairColor = Color.black;

    // Pane 2: 3D Mesh Assignments
    [BeginSplitPane("CustomizerSplit")] // Switches to Pane 2
    public Mesh headMesh;
    [EndSplitPane] // Closes the split pane after drawing bodyArmorMesh
    public Mesh bodyArmorMesh;

    [Header("Global Equipment Overrides (Full Width)")]
    public bool enableCapePhysics = true;
    public float globalScaleModifier = 1.0f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BeginSplitPane]` | Mandatory Pair | Must pair with preceding `[BeginSplitPane]` attributes defining Pane 1 and Pane 2. |
| `[Button]` | Supported | Can decorate a method button to close Pane 2 and trigger an action simultaneously. |
| `[BoxGroup]` | Supported | Full-width members after `[EndSplitPane]` can begin new box groups freely. |
