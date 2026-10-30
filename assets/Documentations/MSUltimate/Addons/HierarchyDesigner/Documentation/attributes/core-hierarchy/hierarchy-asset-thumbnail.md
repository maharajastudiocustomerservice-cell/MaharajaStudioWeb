# [HierarchyAssetThumbnail]

> Renders an interactive asset preview thumbnail directly in the hierarchy row with hover zoom popouts and single-click asset pinging.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyAssetThumbnail]` brings asset previews out of the Project and Inspector windows and directly into the Scene Hierarchy. Applied to an asset reference field (such as `Sprite`, `Texture2D`, `Mesh`, `Material`, or `AudioClip`), it renders an interactive preview badge (`ThumbnailSize = 16f`, `CornerRadius = 3f`) on the object's hierarchy row. If the asset is missing, it draws a warning border (`MissingBorderColor = "#552222"`). Hovering the cursor displays a magnified preview popout (`ShowHoverPopout = true`, `PopoutSize = 64f`), and clicking the thumbnail immediately pings and highlights the asset in the Project window (`AllowPingOnClick = true`).

**The Problem:**
Verifying whether UI icons, character sprites, audio stingers, or material variants are assigned across dozens of hierarchy entities requires selecting each GameObject and scouring the Inspector. Missing asset references frequently go unnoticed until runtime rendering failures occur.

**The Solution:**
Decorating serialized asset fields with `[HierarchyAssetThumbnail]`:
- **At-a-Glance Asset Auditing:** Scan through the entire scene hierarchy to confirm that sprites, models, and materials are assigned correctly.
- **Single-Click Project Ping:** Click the thumbnail badge to immediately highlight and locate the referenced source asset in your Project directory.
- **Magnified Hover Popout:** Hover over the miniature icon to view high-resolution 64px asset previews without opening secondary windows.
- **Instant Missing-Reference Alerts:** Null fields display distinct dark-red warning borders, catching unassigned references instantly.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class InventoryItemSlotUI : MonoBehaviour
{
    [HierarchyAssetThumbnail(ThumbnailSize = 16f, ShowHoverPopout = true)]
    public Sprite itemIcon;

    public string itemName = "Health Potion";
    public int stackCount = 5;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyAssetThumbnailRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyAssetThumbnailAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ThumbnailSize` | `float` | `16f` | Dimension in pixels (width and height) of the hierarchy thumbnail icon. |
| `CornerRadius` | `float` | `3f` | Corner rounding radius in pixels for the thumbnail border frame. |
| `BorderColor` | `string` | `"#445577"` | Hex color of the thumbnail frame when a valid asset is assigned. |
| `MissingBorderColor`| `string` | `"#552222"` | Hex border color displayed when the target field is null or unassigned. |
| `BackgroundColor` | `string` | `"#1A1A22"` | Hex background color behind transparent textures and sprites. |
| `ShowHoverPopout` | `bool` | `true` | Whether hovering over the badge reveals a magnified preview popout box. |
| `PopoutSize` | `float` | `64f` | Width and height in pixels of the magnified hover popout box. |
| `AllowPingOnClick` | `bool` | `true` | When true, clicking the thumbnail pings the asset in the Project window. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the thumbnail badge remains visible in Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

public class EnvironmentPropAnchor : MonoBehaviour
{
    [Header("Visual Meshes")]
    [Tooltip("Primary 3D mesh model rendered on this prop.")]
    [HierarchyAssetThumbnail(ThumbnailSize = 18f, ShowHoverPopout = true, PopoutSize = 80f, BorderColor = "#3B82F6")]
    public Mesh propModel;

    [Tooltip("Primary surface material.")]
    [HierarchyAssetThumbnail(ThumbnailSize = 18f, XOffset = 24f)]
    public Material propMaterial;

    [Header("Prop Metadata")]
    public bool isDestructible = true;
    public float healthPoints = 100f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **Multiple Field Thumbnails** | High | Offset multiple thumbnails horizontally using `XOffset` (e.g. `4f`, `24f`) to display models and materials side-by-side. |
| **`[HierarchyBadge]`** | High | Pairs cleanly with text badges indicating item rarity or category. |
| **Project Window Integration**| High | Seamlessly invokes `EditorGUIUtility.PingObject` without clearing Scene selection. |
| **Supported Types** | High | Compatible with `Sprite`, `Texture2D`, `Material`, `Mesh`, `AudioClip`, and `GameObject` prefabs. |
