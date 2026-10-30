# [Foldout]

> Encloses a single field or property inside an independent, collapsible foldout card with persistent expand/collapse state.

---

## 1. Overview & Value Proposition

**What it does:**
Wraps a single serialized field or complex property (like a nested struct, class, or lengthy array) inside its own dedicated collapsible foldout container. The expanded/collapsed state is persistently cached across inspector selections and domain reloads.

**The Problem:**
Standard Unity foldouts only exist automatically for arrays, lists, or serialized classes without customization. Single large fields or individual nested settings cannot be collapsed independently without declaring an entire group or writing custom editors.

**The Solution:**
Add `[Foldout("Custom Label")]` to any field:
- **Zero Boilerplate:** Collapsible foldout wrapping without needing group IDs or ending tags.
- **Persistent State:** Remembers whether you left it open or closed when switching GameObjects.
- **Custom Header Styling:** Supports custom title labels, icons, bold text, and header background colors.
- **Card Framing:** Optional borders, corner radii, and body padding.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class BossTelemetry : MonoBehaviour
{
    [Foldout("Advanced AI Settings", StartOpen = false)]
    public float decisionTickRate = 0.1f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | `FoldoutDrawer` (registered in `DrawerDatabase`) |

---

## 4. Constructors & Parameters

```csharp
public FoldoutAttribute(string label = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `string` | `null` | Custom label displayed on the foldout header (uses property name if null). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Label` | `string` | *(Set in constructor)* | Custom foldout header title. |
| `StartOpen` | `bool` | `true` | Whether the foldout begins expanded by default. |
| `HeaderColor` | `string` | `null` | Hex text color for the foldout title. |
| `HeaderBackgroundColor`| `string`| `null`| Hex fill color for the foldout header row. |
| `Bold` | `bool` | `true` | Renders the foldout title in bold text. |
| `FontSize` | `int` | `0` | Header font size in pixels (`0` = default). |
| `Icon` | `string` | `null` | Built-in Unity icon name displayed before the title. |
| `BorderColor` | `string` | `null` | Hex outline border color. |
| `BorderWidth` | `float` | `1f` | Border outline thickness in pixels. |
| `BorderRadius` | `float` | `4f` | Corner radius for the foldout card. |
| `IndentContent` | `bool` | `true` | Indents inner content to distinguish from parent level. |
| `Padding` | `float` | `5f` | Internal padding around content within the foldout. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[Serializable]
public class PhysicsSubsystemConfig
{
    public float gravityScale = 1.0f;
    public float airResistance = 0.05f;
    public PhysicMaterial groundPhysicMaterial;
}

public class VehicleController : MonoBehaviour
{
    [Header("Primary Controls")]
    public float forwardAcceleration = 50f;

    [Foldout("Physics Simulation Overrides", 
        StartOpen = false, 
        Icon = "d_SettingsIcon", 
        HeaderBackgroundColor = "#2c3e50", 
        BorderColor = "#34495e", 
        BorderRadius = 6f
    )]
    public PhysicsSubsystemConfig physicsOverrides;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ShowIf]` | Supported | Evaluates conditional visibility cleanly on the foldout container. |
| `[ReadOnly]` | Supported | Locks child properties while keeping foldout expansion interactive. |
| `[BoxGroup]` | Supported | Can be nested inside outer box groups without clipping. |
