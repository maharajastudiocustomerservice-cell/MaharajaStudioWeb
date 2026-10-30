# [GUIColor]

> Tints the background and interactive elements of a field, property, button, or entire class using a unified hex color.

---

## 1. Overview & Value Proposition

**What it does:**
Colors the background and controls of inspector fields, action buttons, or whole components using clean hex color codes (like `#FF4444` or `#3498DB`).

**The Problem:**
Inspectors with dozens of numeric inputs and buttons look uniformly grey and monolithic. Critical danger buttons (like "Wipe Player Data" or "Drop Database") look identical to benign helper buttons, leading to accidental clicks and mistakes during live development.

**The Solution:**
Add `[GUIColor]` to any field, method, or class:
- **Immediate Visual Hierarchy:** Highlight critical parameters, network values, or health bars with distinct color highlights.
- **Color-Coded Buttons:** Make destructive action buttons vibrant red, save buttons green, and debug toggles yellow.
- **Class-Level Tinting:** Apply to a class to give the entire custom component inspector a distinctive theme accent.
- **Standard Hex Codes:** Use standard 6 or 8 character hex strings (`#RRGGBB` or `#RRGGBBAA`) for pixel-perfect brand consistency.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerShield : MonoBehaviour
{
    [GUIColor("#3498db")]
    public float maxShield = 100f;

    [GUIColor("#e74c3c")]
    [Button]
    public void OverloadShield()
    {
        maxShield = 0;
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method | Class` |
| **Supported Types** | Any field, property, or method button |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **Interfaces** | `ICollectionElementAttribute` |
| **UI Toolkit Compatible** | Yes |

### Collection Cascading Behavior

| Target Placement | Cascades to Elements? | Behavior / Notes |
| :--- | :---: | :--- |
| `List<T>`, `T[]` (Default) | No | Tints the collection foldout / header container without overriding element colors. |
| `List<T>`, `T[]` (`ApplyToElements = true`) | **Yes** | Cascades the color tint down to every individual row and control inside the collection. |
| `SerializableDictionary<K, V>` | Opt-In | Can cascade to key/value rows when `ApplyToElements = true`. |

---

## 4. Constructors & Parameters

```csharp
public GUIColorAttribute()
public GUIColorAttribute(string colorHex)
public GUIColorAttribute(string colorHex, bool applyToElements)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorHex` | `string` | `null` | Hex color string (e.g. `"#FF4444"`, `"#2ECC71"`, `"#3498DB"`). |
| `applyToElements` | `bool` | `false` | When `true`, cascades color tinting to individual collection element rows. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorHex` | `string` | `null` | Unified hex color applied to the element's background and interactive controls. |
| `ApplyToElements` | `bool` | `false` | When `true`, cascades color tinting down to individual collection element rows. |
| `Order` | `int` | `0` | Execution priority relative to other field modifiers. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[GUIColor("#2c3e50")]
public class NuclearReactorController : MonoBehaviour
{
    [Header("Core Status")]
    [GUIColor("#2ecc71")]
    public float coolantFlowRate = 98.5f;

    [GUIColor("#f39c12")]
    public float coreTemperature = 850f;

    [Header("Coolant Reservoir Nodes")]
    [GUIColor("#38BDF8", applyToElements: true)]
    public List<float> coolantNodePressures = new List<float> { 45.2f, 48.0f, 44.9f };

    [Header("Emergency Controls")]
    [GUIColor("#e74c3c")]
    [Button("SCRAM - Emergency Shutdown", ButtonHeight = 36)]
    public void EmergencyShutdown()
    {
        Debug.LogWarning("Reactor emergency shutdown triggered!");
    }

    [GUIColor("#1abc9c")]
    [Button("Flush Coolant Loop")]
    public void FlushCoolant()
    {
        coolantFlowRate = 100f;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Tints the button background and highlight borders. |
| `[BoxGroup]` | Supported | Tints individual fields inside the group without breaking group styling. |
| `[ReadOnly]` | Supported | Color tint remains visible even when the field is disabled or read-only. |
| `[FieldTag]` | Supported | Pair together with field tags for multi-layered visual categorization. |
| Collections (`List<T>`, `T[]`) | Supported | Tints container foldout by default; opt-in element cascading via `ApplyToElements = true`. |

