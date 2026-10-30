# [MSIgnore]

> Opts out a field or property from MSUltimate's enhanced inspector pipeline, reverting it to standard native Unity drawing.

---

## 1. Overview & Value Proposition

**What it does:**
Tells MSUltimate's inspector engine to bypass custom drawer processing, styling, and animations for the decorated field or property, forcing Unity to render the property using its default native editor GUI.

**The Problem:**
In projects using third-party packages or complex legacy custom PropertyDrawers (e.g. specialized shader graph nodes, custom timeline tracks, or third-party serializable dictionaries), MSUltimate's enhanced UI Toolkit rendering pipeline might conflict with existing legacy IMGUI property drawer implementations.

**The Solution:**
Add `[MSIgnore]` to any field or property:
- **Instant Fallback:** Reverts the specific member to standard Unity rendering without modifying global settings.
- **Third-Party Compatibility:** Ensures 100% interoperability with custom legacy property drawers from other Asset Store packages.
- **Granular Control:** Apply only to problematic properties while letting the rest of your MonoBehaviour enjoy full MSUltimate styling.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LegacyInteropConfig : MonoBehaviour
{
    [BoxGroup("Enhanced Section")]
    public float movementSpeed = 10f;

    // Bypasses MSUltimate custom drawing and uses native Unity drawer
    [MSIgnore]
    public LayerMask legacyCustomLayerMask;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serialized field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes (Delegates directly to native Unity drawer) |
| **Drawer Resolution** | Reverts to native Unity property drawing (`DrawerDatabase` returns `null`) |

---

## 4. Constructors & Parameters

```csharp
public MSIgnoreAttribute()
```

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Category` | `AttributeCategory`| `Behavioral` | Categorizes this attribute in the behavioral execution phase. |
| `Order` | `int` | `0` | Drawing execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ThirdPartyAssetBridge : MonoBehaviour
{
    [Header("MSUltimate Managed Gameplay Settings")]
    [MinMaxSlider(0f, 100f)]
    public Vector2 spawnBounds = new Vector2(10f, 50f);

    [EnumToggleButtons]
    public LightType lightSourceType = LightType.Spot;

    [Header("Legacy IMGUI Third-Party Field")]
    [MSIgnore]
    [Tooltip("Rendered strictly via legacy native drawer to preserve third-party plugin compatibility")]
    public AnimationCurve legacyThirdPartySplineCurve;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| Native Unity Attributes | Recommended | Works seamlessly with `[Range]`, `[Header]`, and `[Tooltip]`. |
| Custom PropertyDrawers | Recommended | Preserves specialized third-party drawers without interference. |
| `[BoxGroup]` | Supported | Sits inside groups while rendering with native Unity control styling. |
