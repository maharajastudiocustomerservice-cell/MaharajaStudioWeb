# [LayerSelector]

> Displays an int (layer index) or string (layer name) field as a dropdown menu populated with Unity project layers.

---

## 1. Overview & Value Proposition

**What it does:**
Turns an integer layer index or string variable into a clean dropdown menu containing all named layers defined in Unity Project Settings.

**The Problem:**
In standard Unity, `int` fields storing layer indices (like `gameObject.layer`) are drawn as plain integer numbers (`0`, `8`, `31`). Developers must memorize which number corresponds to which layer or risk entering invalid layer indices.

**The Solution:**
Add `[LayerSelector]` to any integer or string field:
- **Layer Name Dropdown:** Select layers by name (e.g. `Default`, `Water`, `Enemies`) instead of typing raw index numbers.
- **Int & String Support:** Works with integer indices (`int`, `uint`) and string layer names seamlessly.
- **Quick Settings Access:** Includes an optional button (`ShowManagerButton`) to jump directly to `Project Settings -> Tags and Layers`.
- **Collection Elements:** Functions smoothly on layer elements inside lists and arrays.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SpawnLayerAssigner : MonoBehaviour
{
    [LayerSelector]
    public int spawnPhysicsLayer = 8;

    [LayerSelector]
    public string targetLayerName = "Enemies";
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
public LayerSelectorAttribute(string customLabel = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `customLabel` | `string` | `null` | Custom display label override for the inspector row. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CustomLabel` | `string` | `null` | Custom field label override text. |
| `ShowManagerButton` | `bool` | `true` | Shows quick button to open Project Settings -> Tags & Layers. |
| `TextColor` | `string` | `null` | Optional hex text color override. |
| `BackgroundColor` | `string` | `null` | Optional hex background color override. |
| `LabelWidth` | `float` | `0f` | Width allocated to the field label (`0f` uses default). |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class DebrisPhysicsEmitter : MonoBehaviour
{
    [Header("Collision Filtering")]
    [LayerSelector(customLabel: "Debris Particle Layer", ShowManagerButton = true)]
    public int particleCollisionLayer = 2;

    [Header("Exempt Layers")]
    [LayerSelector]
    public List<int> ignoredLayerIndices = new List<int>();
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[LayerMaskToggles]` | Alternative | Use `[LayerSelector]` for single layers; use `[LayerMaskToggles]` for multi-layer bitmasks. |
| `[TagSelector]` | Complementary | Pair together for full tag and layer assignment workflows. |
| `[BoxGroup]` | Supported | Functions normally inside group containers. |
