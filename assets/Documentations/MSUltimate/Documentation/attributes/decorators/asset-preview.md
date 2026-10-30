# [AssetPreview]

> Renders a live, high-resolution thumbnail preview of assigned textures, sprites, materials, meshes, and prefabs directly beside or below the field.

---

## 1. Overview & Value Proposition

**What it does:**
Shows an instant image thumbnail of assigned textures, sprites, materials, and prefabs right in the Inspector.

**The Problem:**
In standard Unity, assigning an asset field only shows a tiny grey object slot with the asset's name. You can't see what sprite or texture is selected without squinting at the tiny preview at the bottom of the Project window or double-clicking the asset to open it.

**The Solution:**
Add `[AssetPreview]` above any `UnityEngine.Object` field:
- **Instant Visual Thumbnails:** Displays a high-resolution preview directly below or beside the field.
- **Interactive Lightbox Zoom:** Click the thumbnail to open a high-res full-size inspection modal.
- **Drag-and-Drop Landing:** Drag textures or sprites directly onto the preview card from anywhere.
- **Gallery Grid Mode:** Automatically formats lists of assets into clean, compact thumbnail galleries.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterPortrait : MonoBehaviour
{
    [AssetPreview(80f, 80f)]
    public Sprite avatarSprite;
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
public AssetPreviewAttribute()
public AssetPreviewAttribute(float size)
public AssetPreviewAttribute(float width, float height)
public AssetPreviewAttribute(float size, PreviewPosition position)
public AssetPreviewAttribute(float width, float height, PreviewPosition position)
public AssetPreviewAttribute(PreviewPosition position)
public AssetPreviewAttribute(string customPreviewMember)
public AssetPreviewAttribute(float size, string customPreviewMember)
public AssetPreviewAttribute(string customPreviewMember, float size)
public AssetPreviewAttribute(string customPreviewMember, float width, float height)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `size` | `float` | `64f` | Uniform width and height size in pixels. |
| `width` | `float` | `64f` | Preview box pixel width. |
| `height` | `float` | `64f` | Preview box pixel height. |
| `position` | `PreviewPosition` | `PreviewPosition.Below` | Placement location (`Below`, `ReplaceField`, `Inline`). |
| `customPreviewMember` | `string` | `null` | Method, property, or field name returning a custom preview object or texture. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Width` | `float` | `64f` | Pixel width of the preview card. |
| `Height` | `float` | `64f` | Pixel height of the preview card. |
| `Position` | `PreviewPosition` | `PreviewPosition.Below` | Position relative to the field (`Below`, `ReplaceField`, `Inline`). |
| `ScaleToFit` | `bool` | `true` | Preserves asset aspect ratio without stretching. |
| `ShowAssetInfo` | `bool` | `false` | Displays resolution and format metadata below the image. |
| `Interactive` | `bool` | `true` | Single-click pings asset; double-click opens asset. |
| `EnableDragAndDrop` | `bool` | `true` | Enables dragging assets in and out of the preview slot. |
| `ShowDropZone` | `bool` | `true` | Displays inviting dashed drop slot when reference is null. |
| `ShowQuickActions` | `bool` | `true` | Shows hover micro-toolbar with Clear, Ping, Open, and Lightbox actions. |
| `EnableLightbox` | `bool` | `true` | Enables 1-click full-screen zoom preview popup. |
| `ShowTransparencyGrid` | `bool` | `true` | Renders a checkered background behind transparent PNG sprites. |
| `Grid` | `bool` | `true` | Formats arrays/lists of assets as a compact thumbnail gallery. |
| `BorderRadius` | `float` | `-1f` | Corner rounding radius in pixels (-1 uses default 6px). |
| `BorderWidth` | `float` | `-1f` | Border thickness in pixels (-1 uses default 1px, 0 removes border). |
| `BorderColor` | `string` | `null` | Border stroke hex color. |
| `BackgroundColor` | `string` | `null` | Card background hex color. |
| `CustomPreviewMember` | `string` | `null` | Method/property providing dynamic preview texture or asset. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ItemPickup : MonoBehaviour
{
    [Header("Item Visuals")]
    [AssetPreview(96f, PreviewPosition.Inline, ShowAssetInfo = true, EnableLightbox = true)]
    public Texture2D itemIcon;

    [AssetPreview(120f, 80f, PreviewPosition.Below)]
    public Material holographicMaterial;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[PreviewField]` | Alternative | Replaces the object field entirely; use `[AssetPreview]` to keep the field row. |
| `[BoxGroup]` | Supported | Fully functional inside box layouts and tab containers. |
| `[ShowIf]` | Supported | Conditionally reveals preview thumbnails based on gameplay flags. |
| `[DrawCollection]` | Supported | Renders asset lists as a visual gallery grid. |
