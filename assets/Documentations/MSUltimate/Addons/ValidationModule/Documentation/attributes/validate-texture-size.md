# [ValidateTextureSize]

> Validates that a referenced Texture2D, Texture, or Sprite satisfies maximum dimension constraints and power-of-two optimization requirements.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateTextureSize]` inspects serialized `Texture`, `Texture2D`, and `Sprite` reference fields. It measures the asset's pixel width and height against defined `MaxWidth` and `MaxHeight` limits and optionally verifies whether both dimensions are power-of-two values (`MustBePowerOfTwo = true`). If a texture exceeds maximum dimensions or violates power-of-two constraints, a validation alert banner is displayed in the Inspector and recorded in the Validation Engine window.

**The Problem:**
Texture memory is frequently the single largest contributor to VRAM overhead and build size:
- 2D artists frequently drop uncompressed 4K or 8K raw source images into UI or icon slots that only need 512×512 resolution.
- Non-Power-of-Two (NPOT) textures cannot utilize hardware block compression formats (such as ASTC, BC7, ETC2, or DXT) on many platforms or suffer from mipmap generation penalties.
- Mobile platforms experience severe memory strain and GPU fill rate bottlenecks when oversized textures are allocated on HUD canvases and world-space particle billboards.
Without automated size checks, oversized assets slip into production builds unnoticed until performance profiling uncovers severe memory pressure.

**The Solution:**
Decorating texture fields with `[ValidateTextureSize]`:
- **Dimension Caps:** Constrains width and height to maximum budget thresholds (`MaxWidth = 1024, MaxHeight = 1024`).
- **Power-of-Two (POT) Enforcement:** Guarantees texture dimensions are powers of two (e.g. 256, 512, 1024, 2048) enabling full GPU compression support.
- **Support for Sprites and Textures:** Accurately evaluates both `Texture2D` assets and sliced `Sprite` rects.
- **Budget Control in the Editor:** Catches oversized art assets right at the assignment step before committing to version control.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class SkillIconPresenter : MonoBehaviour
{
    [ValidateTextureSize("Skill icon must not exceed 512x512 pixels.", MaxWidth = 512, MaxHeight = 512)]
    public Texture2D skillIcon;

    [ValidateTextureSize("Atlas texture must be Power-of-Two for GPU compression.", MustBePowerOfTwo = true)]
    public Texture2D uiAtlas;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ValidationModule Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Inspector & Validation Engine Window |
| **Validation Interface** | `IValidationAttribute`, `ICollectionElementAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateTextureSizeAttribute(string message = "Texture size validation failed.")
```

- **`message`** (`string`, optional): Custom error message displayed upon validation failure. Default is `"Texture size validation failed."`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaxWidth` | `int` | `0` | Maximum allowable texture width in pixels (0 disables max width check). |
| `MaxHeight` | `int` | `0` | Maximum allowable texture height in pixels (0 disables max height check). |
| `MustBePowerOfTwo` | `bool` | `false` | When true, asserts both width and height are power-of-two values (e.g., 256, 512, 1024). |
| `Message` | `string` | `"Texture size validation failed."` | Failure explanation displayed in the validation message banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error banner. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Rendering
{
    public class MaterialTextureBinder : ModularMonoBehaviour
    {
        [Header("Diffuse Map (POT + Max 2048)")]
        [ValidateTextureSize("Diffuse texture must be max 2048x2048 and Power-of-Two for ASTC compression.",
            MaxWidth = 2048,
            MaxHeight = 2048,
            MustBePowerOfTwo = true,
            MessageType = InspectorMessageType.Error)]
        public Texture2D diffuseMap;

        [Header("UI Thumbnail (Max 256x256)")]
        [ValidateTextureSize("Thumbnail sprite is too large — cap at 256x256.",
            MaxWidth = 256,
            MaxHeight = 256,
            MessageType = InspectorMessageType.Warning)]
        public Sprite itemThumbnail;

        [Header("Normal Map (Strict POT)")]
        [ValidateTextureSize("Normal map must be strictly power-of-two to prevent compression artifacts.",
            MustBePowerOfTwo = true,
            ErrorColor = "#FF6666")]
        public Texture2D normalMap;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateNotNull]` / `[Required]`**| High | Guard texture field against null before checking pixel dimensions. |
| **`[ValidateAssetExtension]`** | High | Combine to enforce `.png` or `.tga` format alongside dimension restrictions. |
| **`[ValidateInFolder]`** | High | Guarantee textures are placed inside proper asset subdirectories (`Textures/UI/`). |
| **Validation Engine** | Native | Audited automatically during project-wide asset validation scans. |

### Collection Cascading & Serializer Matrix

| Collection / Container Type | Supported | Behavior |
| :--- | :---: | :--- |
| **`List<Texture2D>` / `List<Texture>`** | Yes | Cascades to validate dimension limits on each texture in the list. |
| **`Texture2D[]` / `Sprite[]`** | Yes | Cascades to validate resolution constraints across each array element. |
| **`AdvancedList<Texture2D>`** | Yes | Full element-level validation support with dynamic item reordering. |
| **`SerializableDictionary<K, Texture2D>`** | Yes | Validates texture dimensions when applied to value elements. |
| **`SerializableNullable<Texture2D>`** | Yes | Validates wrapped texture dimensions when populated. |
| **`SerializableTuple<...>`** | Yes | Validates texture fields within tuple members. |
