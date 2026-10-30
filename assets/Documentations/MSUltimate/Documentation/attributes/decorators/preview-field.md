# [PreviewField]

> Displays a live visual thumbnail of assigned assets, replacing or inlining the standard ObjectField with square preview sizing.

---

## 1. Overview & Value Proposition

**What it does:**
Replaces or enhances the standard Unity object field with a square visual thumbnail card featuring drag-and-drop asset loading, pinging, and modal zoom.

**The Problem:**
Standard Unity object fields only show tiny 16x16 icons next to file names. When selecting textures, sprites, meshes, or material assets, designers cannot see what the asset actually looks like without hunting for it in the Project window.

**The Solution:**
Add `[PreviewField]` to any object reference field:
- **Square Visual Card:** Renders a clean square thumbnail (e.g. 64x64, 80x80) displaying the asset preview directly.
- **Drag & Drop Support:** Drop assets straight from the Project window into the preview box.
- **Interactive Lightbox Zoom:** Click to inspect textures and sprites at high resolution.
- **Flexible Placement:** Align inline with the property row or stacked above/below with custom flex alignment.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class InventoryItem : MonoBehaviour
{
    [PreviewField(64)]
    public Sprite itemIcon;

    [PreviewField(80, PreviewPosition.Below)]
    public Texture2D characterPortrait;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `Sprite`, `Texture2D`, `Material`, `GameObject`, `Mesh`, `AudioClip` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public PreviewFieldAttribute()
public PreviewFieldAttribute(float height)
public PreviewFieldAttribute(float height, FlexAlign align)
public PreviewFieldAttribute(float height, PreviewPosition position)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `height` | `float` | `64f` | Square width and height dimension in pixels. |
| `align` | `FlexAlign` | `FlexAlign.Auto` | Flex alignment within the inspector row (`Auto`, `FlexStart`, `Center`, `FlexEnd`). |
| `position` | `PreviewPosition` | `PreviewPosition.Inline` | Position of preview relative to field (`Inline`, `Below`, `ReplaceField`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Width` | `float` | `64f` | Thumbnail width in pixels. |
| `Height` | `float` | `64f` | Thumbnail height in pixels. |
| `Position` | `PreviewPosition` | `Inline` | Placement mode (`Inline`, `Below`, `ReplaceField`). |
| `ScaleToFit` | `bool` | `true` | Preserves aspect ratio within the preview frame. |
| `EnableLightbox` | `bool` | `true` | Enables high-res zoom modal popup on click. |
| `ShowTransparencyGrid` | `bool` | `true` | Renders checkerboard background behind transparent sprites. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterCustomizer : MonoBehaviour
{
    [Header("Hero Appearance")]
    [PreviewField(72, FlexAlign.Center)]
    public Sprite heroAvatar;

    [Header("Armor Texture")]
    [PreviewField(96, PreviewPosition.Below)]
    public Texture2D diffuseAlbedoMap;

    [Header("Model Mesh")]
    [PreviewField(64)]
    public GameObject heroPrefab;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[AssetPreview]` | Alternative | Use `[PreviewField]` for compact square fields; use `[AssetPreview]` for full-featured multi-asset grids. |
| `[BoxGroup]` | Supported | Adapts cleanly within grouped layouts. |
| `[AssetOnly]` | Recommended | Pairs together to ensure only project assets are assigned to the preview. |
