# [ComponentImageBackground]

> Displays a custom project texture asset or built-in Unity icon as a subtle background image behind all component fields with scale modes, tinting, and opacity control.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentImageBackground]` transforms plain inspector cards by projecting a custom texture or Unity editor icon directly across the component background. Injected into `ComponentSlot.ContentOverlay`, it renders seamlessly behind serialized properties. It supports relative project asset paths (e.g. `"Assets/Textures/UI/FactionCrest.png"`) or built-in Unity editor icons, configurable image scaling modes (`ScaleMode` $\to$ `ScaleAndCrop`, `StretchToFill`, `ScaleToFit`), customizable tinting (`TintColor`), fine-grained transparency (`Opacity`, defaulting to a subtle `0.1f`), and corner clipping (`BorderRadius`).

**The Problem:**
Signature studio assets, faction crests, character portraits, and biome concept art remain locked inside Project folders while inspector editors look generic. Without visual brand immersion, complex configuration components feel detached from the game's actual art direction.

**The Solution:**
Decorating components with `[ComponentImageBackground]`:
- **Asset & Built-in Icon Flexibility:** Loads textures directly from `Assets/` or retrieves built-in editor icons via `EditorGUIUtility`.
- **Subtle Ambient Opacity:** Default low opacity (`0.1f`) guarantees that text, sliders, and input fields remain razor-sharp and effortlessly readable.
- **Three Texture Scaling Modes:** Choose between `ScaleAndCrop` for immersive edge-to-edge coverage, `ScaleToFit` for unclipped logos, or `StretchToFill`.
- **Non-Interfering Interaction:** Absolute positioning with `PickingMode.Ignore` ensures controls receive full mouse click and drag events.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentImageBackground("Assets/Art/UI/CyberpunkDragonEmblem.png", Opacity = 0.12f, ScaleMode = ImageScaleMode.ScaleAndCrop)]
public class CyberpunkFactionHandler : MonoBehaviour
{
    public string factionName = "Neon Syndicates";
    public float territoryControlPercentage = 68.4f;
    public int activeMercenaries = 120;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `ContentOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentImageBackgroundAttribute(string imagePath)
```

- `imagePath`: Relative path to a project texture asset starting from `Assets/` or a Unity built-in icon identifier (e.g. `"d_UnityLogo"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ImagePath` | `string` | *(Constructor)* | Path to texture asset (e.g. `"Assets/Textures/Logo.png"`) or built-in icon name. |
| `Opacity` | `float` | `0.1f` | Transparency alpha of the background image (0.0 to 1.0). |
| `ScaleMode` | `ImageScaleMode` | `ImageScaleMode.ScaleAndCrop` | Texture fitting mode (`ScaleAndCrop`, `StretchToFill`, `ScaleToFit`). |
| `TintColor` | `string` | `""` | Hex tint color string applied to the texture. If empty, uses original colors. |
| `BorderRadius` | `float` | `0f` | Corner clipping radius in pixels to prevent texture overflowing rounded card borders. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#D97706", Width = 2f, Radius = 8f)]
[ComponentBackground("#1A1207", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("ANCIENT RELIC CONTROLLER", Subtitle = "Mythic Artifact Powers & Attunement", BackgroundColor = "#2E1C0A", TitleColor = "#FEF3C7")]
[ComponentImageBackground("Assets/Art/Textures/RelicCarvingPattern.png", Opacity = 0.15f, ScaleMode = ImageScaleMode.ScaleAndCrop, TintColor = "#F59E0B", BorderRadius = 8f)]
public class AncientRelicController : MonoBehaviour
{
    [Header("Relic State")]
    public string relicDesignation = "Eye of Ra'Kesh";
    public int attunementLevel = 4;
    public float currentAetherMana = 350f;

    [Header("Passive Bonuses")]
    public float elementalResistance = 0.25f;
    public bool isCurseCleansed = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Renders on top of the solid background color in `ContentOverlay` for textured card finishes. |
| **`[ComponentBorder]`** | High | Set `BorderRadius` to match the border radius for clean clipped image corners. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures complete click-through transparency for all inspector controls. |
