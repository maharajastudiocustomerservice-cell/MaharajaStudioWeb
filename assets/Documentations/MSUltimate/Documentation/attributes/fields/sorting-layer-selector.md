# [SortingLayerSelector]

> Displays integer (Layer ID) or string (Layer Name) fields as a native Unity 2D Sorting Layer dropdown with 1-click Project Settings access.

---

## 1. Overview & Value Proposition

**What it does:**
Transforms standard `int` (Sorting Layer ID) or `string` (Sorting Layer Name) fields into an interactive dropdown menu populated directly with the project's 2D Sorting Layers. Includes an inline gear button to jump straight to Unity's Tags & Layers project settings.

**The Problem:**
In 2D projects, custom components (like custom mesh generators, VFX emitters, or custom sprite controllers) often need to specify a sorting layer. Without a drawer, developers must remember exact string names (e.g. `"Foreground"`, `"Characters"`) or raw integer IDs, leading to typos and layer ordering bugs that render sprites behind the background.

**The Solution:**
Add `[SortingLayerSelector]` to `int`, `uint`, or `string` fields:
- **Automatic Layer Discovery:** Fetches the exact sorting layers configured in the project in real time.
- **Dual Representation Support:** Works seamlessly with `string` fields (serializing layer names like `"Default"`) or `int` fields (serializing unique layer IDs).
- **1-Click Tags & Layers Shortcut:** Click the gear icon to immediately open Project Settings $\rightarrow$ Tags & Layers.
- **Visual Customization:** Supports custom label overrides, text colors, and background styling.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ParallaxLayer : MonoBehaviour
{
    [SortingLayerSelector]
    public string sortingLayerName = "Background";

    [SortingLayerSelector]
    public int sortingLayerId = 0;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `int`, `uint`, `string` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public SortingLayerSelectorAttribute(string customLabel = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `customLabel` | `string` | `null` | Optional display label override for the inspector row. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CustomLabel` | `string` | `null` | Custom field display name override. |
| `ShowManagerButton` | `bool` | `true` | If `true`, shows a button to open Project Settings $\rightarrow$ Tags & Layers. |
| `TextColor` | `string` | `null` | Hex text color override for the dropdown. |
| `BackgroundColor` | `string` | `null` | Hex background color for the dropdown field. |
| `LabelWidth` | `float` | `0f` | Explicit width for the field label in pixels. |
| `Order` | `int` | `0` | Drawing execution order in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[RequireComponent(typeof(ParticleSystem))]
public class ParticleSortingController : MonoBehaviour
{
    [Header("Render Order Configuration")]
    [SortingLayerSelector("Visual Sorting Layer", ShowManagerButton = true)]
    public string targetSortingLayer = "Foreground_VFX";

    public int orderInLayer = 10;

    private void Start()
    {
        var renderer = GetComponent<ParticleSystemRenderer>();
        if (renderer != null)
        {
            renderer.sortingLayerName = targetSortingLayer;
            renderer.sortingOrder = orderInLayer;
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Dropdown and project settings icon align cleanly inside group boxes. |
| `[ShowIf]` | Supported | Conditionally reveals sorting configuration when 2D rendering mode is active. |
| `[ReadOnly]` | Supported | Displays the assigned sorting layer while preventing modifications. |
| `ICollectionElement` | Supported | Compatible with arrays and lists of sorting layer assignments. |
