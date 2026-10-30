# [Asset3DPreview]

> Renders an interactive, real-time 3D viewport directly in the Unity Inspector for 3D Meshes, Prefabs, Particle Systems, and Materials with orbit, zoom, pan, lighting, wireframe, animation controls, snapshot export, and collection showcase grid support.

---

## 1. Overview & Value Proposition

**What it does:**
Adds an interactive 3D preview viewport right inside the Inspector, allowing you to preview, inspect, rotate, zoom, and test animations on models, prefabs, and materials without switching windows or dropping them into the scene hierarchy.

**The Problem:**
In standard Unity, checking how a 3D model looks requires either dragging it into the active scene hierarchy, moving the scene camera around, or squinting at the tiny preview thumbnail at the bottom of the Project window. This breaks flow when tuning weapon drops, cosmetic skins, or modular environment props.

**The Solution:**
Add `[Asset3DPreview]` above any `GameObject`, `Mesh`, `Material`, or collection of 3D assets. You instantly get an interactive 3D viewport:
- **Orbit, Zoom & Pan:** Rotate with left-click drag, zoom with the scroll wheel, and pan with middle-click.
- **Lighting, Fog & Wireframe:** Adjust key, fill, and ambient lighting, toggle wireframe view, configure distance fog, and toggle ground grid lines.
- **Turntable & Animation:** Automatically rotate the model and scrub/playback animations directly in the Inspector.
- **Screenshot Capture:** Capture high-resolution PNG snapshots (up to 4K, solid/scene/transparent backgrounds) with one click.
- **Collection Showcase Grid:** When applied to `List<GameObject>` or `Mesh[]`, renders an interactive multi-item 3D asset showcase grid.
- **Zero Runtime Cost:** Editor-only execution stripped completely from player builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PropSpawner : MonoBehaviour
{
    [Asset3DPreview(PreviewHeight = 220f, AutoRotate = true)]
    public GameObject propPrefab;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `GameObject`, `Prefab`, `Mesh`, `Material`, `Component`, `List<T>`, `T[]` (where `T` is 3D asset) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Interfaces** | `ICollectionElementAttribute`, `ICollectionPresentationAttribute` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public Asset3DPreviewAttribute()
```

---

## 5. Properties & Customization Options

### Viewport & Layout
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PreviewHeight` | `float` | `200f` | Height of the 3D viewport canvas in pixels. |
| `PreviewWidth` | `float` | `0f` | Fixed width in pixels (`0` auto-fits the inspector width). |
| `FullWidth` | `bool` | `false` | When `true`, expands across the entire inspector width ignoring default margins. |
| `AboveGroup` | `bool` | `false` | Positions the preview above its parent layout group instead of inside it. |
| `BorderColor` | `string` | `"#333344"` | Hex color string for the viewport frame border. |
| `BorderWidth` | `float` | `1f` | Border thickness in pixels. |
| `BorderRadius` | `float` | `6f` | Corner rounding radius of the viewport container. |
| `MarginTop` | `float` | `6f` | Top margin spacing in pixels. |
| `MarginBottom` | `float` | `6f` | Bottom margin spacing in pixels. |
| `Grid` | `bool` | `true` | When decorating collections, renders an interactive multi-item showcase grid. |

### Camera & Navigation
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CameraDistance` | `float` | `5f` | Initial distance of the preview camera from the asset center. |
| `CameraFOV` | `float` | `30f` | Field of view angle for the preview camera in degrees. |
| `DefaultRotationX` | `float` | `-20f` | Initial pitch angle in degrees. |
| `DefaultRotationY` | `float` | `135f` | Initial yaw angle in degrees. |
| `AllowOrbit` | `bool` | `true` | Enables left-click drag camera orbiting. |
| `AllowZoom` | `bool` | `true` | Enables scroll-wheel camera zooming. |
| `AllowPan` | `bool` | `true` | Enables middle-mouse drag camera panning. |
| `ZoomSensitivity` | `float` | `0.5f` | Scroll-wheel zoom speed multiplier. |
| `MinZoom` | `float` | `0.5f` | Minimum allowable camera zoom distance. |
| `MaxZoom` | `float` | `30f` | Maximum allowable camera zoom distance. |
| `AutoRotate` | `bool` | `false` | Automatically spins the 3D asset continuously. |
| `AutoRotateSpeed` | `float` | `30f` | Turntable rotation speed in degrees per second. |
| `ShowCameraPresets` | `bool` | `true` | Displays quick camera preset buttons (Front, Back, Top, Isometric). |

### Lighting, Fog & Background
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `LightColor` | `string` | `"#FFF4E0"` | Main directional key light hex color. |
| `LightIntensity` | `float` | `1f` | Main directional key light intensity multiplier. |
| `LightAngleX` | `float` | `50f` | Main light Euler pitch angle. |
| `LightAngleY` | `float` | `-30f` | Main light Euler yaw angle. |
| `AmbientColor` | `string` | `"#404040"` | Spherical ambient light hex color. |
| `AmbientIntensity` | `float` | `0.5f` | Spherical ambient light intensity multiplier. |
| `EnableFillLight` | `bool` | `true` | Enables a secondary directional fill light from the opposite angle. |
| `FillLightColor` | `string` | `"#8090B0"` | Secondary fill light hex color. |
| `FillLightIntensity` | `float` | `0.4f` | Secondary fill light intensity multiplier. |
| `BackgroundColor` | `string` | `"#1E1E2E"` | Solid viewport background hex color when gradients are disabled. |
| `ShowGradient` | `bool` | `true` | Enables a vertical gradient background behind the 3D model. |
| `GradientTopColor` | `string` | `"#2A2A3D"` | Top hex color of the background gradient. |
| `GradientBottomColor` | `string` | `"#0D0D15"` | Bottom hex color of the background gradient. |
| `EnableFog` | `bool` | `false` | Enables distance fog inside the preview scene. |
| `FogColor` | `string` | `"#1A1A2E"` | Preview fog hex color. |
| `FogDensity` | `float` | `0.05f` | Density for exponential fog. |
| `FogMode` | `UnityEngine.FogMode` | `FogMode.Exponential` | Fog calculation mode (`Linear` or `Exponential`). |

### Overlays, Overlays & Snapshots
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowGrid` | `bool` | `true` | Draws a perspective reference ground grid plane below the asset. |
| `GridColor` | `string` | `"#FFFFFF30"` | Ground grid line hex color. |
| `GridLines` | `int` | `20` | Number of subdivision lines across the ground plane. |
| `ShowWireframe` | `bool` | `false` | Renders asset geometry with wireframe overlay lines. |
| `ShowMeshInfo` | `bool` | `true` | Displays vertex count, triangle count, and submesh count HUD overlay. |
| `ShowToolbar` | `bool` | `true` | Displays the floating control bar (Reset, Wireframe, Turntable, Snapshot). |
| `ToolbarColor` | `string` | `"#1A1A2A"` | Hex background color of the preview toolbar. |
| `ShowAnimationControls`| `bool` | `true` | Displays animation playback and scrubber controls when clips are present. |
| `AnimationSpeed` | `float` | `1f` | Animation playback speed multiplier. |
| `ScreenshotWidth` | `int` | `1024` | Width in pixels of saved snapshot captures. |
| `ScreenshotHeight` | `int` | `1024` | Height in pixels of saved snapshot captures. |
| `ScreenshotBgMode` | `Asset3DScreenshotBgMode` | `Scene` | Snapshot background mode (`Scene`, `SolidColor`, `Transparent`). |
| `ScreenshotBgColor`| `string` | `"#000000"` | Hex color used when snapshot background mode is `SolidColor`. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using System.Collections.Generic;
using MaharajaStudio.MSUltimate.Runtime;

[CreateAssetMenu(fileName = "CharacterSkinData", menuName = "Game/Cosmetics/Character Skin")]
public class CharacterSkinData : ScriptableObject
{
    [BoxGroup("Featured Model", Box = true)]
    [Asset3DPreview(
        PreviewHeight = 260f,
        AutoRotate = true,
        AutoRotateSpeed = 25f,
        CameraDistance = 4.2f,
        ShowGrid = true,
        ShowMeshInfo = true,
        ShowAnimationControls = true,
        LightColor = "#FFFFFF",
        BackgroundColor = "#181824"
    )]
    [Tooltip("Target skeletal mesh model for this skin.")]
    public GameObject characterModel;

    [BoxGroup("Featured Model")]
    public string skinDisplayName = "Cyber Warrior";

    [BoxGroup("Armor Variations", Box = true)]
    [Asset3DPreview(PreviewHeight = 140f, Grid = true)]
    [Tooltip("Showcase grid displaying modular armor piece prefabs.")]
    public List<GameObject> armorVariants = new List<GameObject>();
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Pairs seamlessly inside `[BoxGroup]`, `[TabGroup]`, and `[CardGroup]`. Set `FullWidth = true` when nested in wide cards.
- **Conditionals:** Fully reactive with `[ShowIf]` and `[HideIf]`—the internal preview render texture and preview scene are disposed when the field is hidden.
- **Validation:** Combine with `[NotNull]` or `[Required]` to highlight empty slots while displaying the interactive frame when assigned.
- **Defensive Fallback:** If assigned an incompatible object (e.g. an Audio clip or TextAsset), safely displays a non-destructive fallback message without throwing GUI exceptions.
