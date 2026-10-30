# [ShaderProperty]

> Renders string or int fields as a smart, searchable dropdown populated with exposed properties from a target Material or Shader.

---

## 1. Overview & Value Proposition

**What it does:**
Populates a string (property name) or integer (property ID) field with exposed parameters from a target `Material`, `Shader`, or `Renderer`. Allows designers to pick shader properties visually, complete with type badges (`[Color]`, `[Tex]`, `[Float]`), live swatch previews, and property-type filtering.

**The Problem:**
Controlling material effects via script (such as `material.SetFloat("_DissolveAmount", 0.5f)` or `material.SetColor("_EmissionColor", Color.red)`) requires hardcoding property name strings or property ID hashes. A typo in `"_DissolveAmount"` fails silently without compiler errors or warnings, wasting hours of debugging.

**The Solution:**
Add `[ShaderProperty]` to your property name field:
- **Searchable Property Dropdown:** Displays every exposed parameter directly from the assigned Material or Shader.
- **Type-Safe Filtering:** Restrict dropdown choices by type using `MSShaderPropertyType` (`Color`, `Texture`, `Float`, `Vector`, `Range`, `Keyword`).
- **Live Previews & Badges:** Shows live color swatches or current parameter values directly alongside dropdown options.
- **Auto Renderer Resolution:** Automatically finds a `Renderer` on the same GameObject if no explicit Material member is provided.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class MaterialDissolveEffect : MonoBehaviour
{
    [ShaderProperty(MSShaderPropertyType.Float)]
    public string dissolveProperty = "_DissolveAmount";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string` (property name) or `int` (property name ID hash) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ShaderPropertyAttribute()
public ShaderPropertyAttribute(MSShaderPropertyType filter)
public ShaderPropertyAttribute(string targetMaterialMember, MSShaderPropertyType filter = MSShaderPropertyType.All)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `filter` | `MSShaderPropertyType` | `MSShaderPropertyType.All` | Restricts properties to specific types (`Color`, `Texture`, `Float`, etc.). |
| `targetMaterialMember` | `string` | `""` | Name of field/property/method on the component returning a `Material`, `Shader`, or `Renderer`. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Filter` | `MSShaderPropertyType` | `All` | Property type filter (`All`, `Color`, `Vector`, `Float`, `Texture`, `Range`, `Keyword`). |
| `TargetMaterialMember` | `string` | `""` | Member returning target Material/Renderer. Defaults to local Renderer if empty. |
| `CustomShaderPath` | `string` | `""` | Explicit shader path (e.g. `"Universal Render Pipeline/Lit"`) to inspect when Material is unassigned. |
| `ShowPropertyTypeBadge` | `bool` | `true` | Displays property category pills (e.g. `[Color]`, `[Float]`) beside names. |
| `ShowPreviewValue` | `bool` | `true` | Displays current live material value or color swatch in the inspector. |
| `AllowCustomInput` | `bool` | `true` | Allows typing custom property names not present in the current shader. |
| `BackgroundColor` | `string` | `null` | Hex background color for the dropdown button. |
| `TextColor` | `string` | `null` | Hex font color for the dropdown button text. |
| `BorderColor` | `string` | `null` | Hex border color for the dropdown button. |
| `BorderRadius` | `float` | `3f` | Corner radius of the selector button. |
| `Height` | `float` | `22f` | Height of the selector button in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ShieldImpactFlash : MonoBehaviour
{
    [Header("Material Source")]
    public Material targetShieldMaterial;

    [Header("Shader Properties")]
    [ShaderProperty(nameof(targetShieldMaterial), MSShaderPropertyType.Color)]
    public string impactColorProperty = "_HitColor";

    [ShaderProperty(nameof(targetShieldMaterial), MSShaderPropertyType.Float)]
    public string flashIntensityProperty = "_FlashIntensity";

    [ShaderProperty(nameof(targetShieldMaterial), MSShaderPropertyType.Texture)]
    public string hitNormalMapProperty = "_HitRippleTex";

    private int _intensityPropId;

    private void Awake()
    {
        _intensityPropId = Shader.PropertyToID(flashIntensityProperty);
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Sits cleanly inside VFX and material configuration cards. |
| `[ShowIf]` | Supported | Conditionally displays properties based on effect toggles. |
| `[ReadOnly]` | Supported | Locks property selection while retaining visual badges and preview values. |
| `ICollectionElement` | Supported | Usable inside lists of animated shader properties (`List<string>`). |
