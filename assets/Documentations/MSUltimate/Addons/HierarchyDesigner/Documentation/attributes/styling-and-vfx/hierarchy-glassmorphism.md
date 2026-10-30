# [HierarchyGlassmorphism]

> Renders a frosted glass translucent background with a specular rim highlight across the hierarchy row.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyGlassmorphism]` styles the hierarchy row with modern frosted glass aesthetics (glassmorphism). Driven by `HierarchyGlassmorphismRenderer`, it utilizes `HierarchyDrawUtilities.DrawGlassmorphism` to paint a smooth translucent background card tint (`BlurColor = "#1E2A38"`), an ultra-fine specular rim highlight line across the top edge (`SpecularOpacity = 0.5f`), and a subtle translucent border outline (`BorderAlpha = 0.2f`).

**The Problem:**
Standard hierarchy rows in Unity use flat gray backgrounds. Customizing rows with harsh solid color blocks can feel jarring and visually overwhelming. Developers want a premium, modern AAA look that makes key entities stand out without overpowering surrounding text or icons.

**The Solution:**
Decorating components with `[HierarchyGlassmorphism]`:
- **Frosted Glass Panel Aesthetics:** Applies a sleek, translucent modern card styling directly over the hierarchy row.
- **Top Specular Rim Light:** A subtle 1px white highlight line gives the impression of refractive glass.
- **Custom Blur Tint & Alpha:** Fine-tune background hue, specular brightness, and border alpha.
- **Non-Intrusive Contrast:** Hierarchy text, badges, and icons remain crisp and legible against the frosted panel.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyGlassmorphism]
public class MainPlayerRig : MonoBehaviour
{
    public float movementSpeed = 6.5f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyGlassmorphismRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyGlassmorphismAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BlurColor` | `string` | `"#1E2A38"` | Hex background tint color for the frosted glass effect. |
| `SpecularOpacity` | `float` | `0.5f` | Opacity of the specular top rim highlight line (0.0 to 1.0). |
| `BorderAlpha` | `float` | `0.2f` | Alpha transparency of the subtle surrounding border outline (0.0 to 1.0). |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the frosted glass styling remains visible during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyGlassmorphism(
    BlurColor = "#0F172A", 
    SpecularOpacity = 0.65f, 
    BorderAlpha = 0.3f)]
public class GameManagerSingleton : MonoBehaviour
{
    [Header("Game State")]
    public int currentScore = 0;
    public bool isGamePaused = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyGlow]`** | High | Combine glass panels with subtle ambient glow halos for premium hero entity presentation. |
| **`[HierarchyIcon]`** | High | Custom and native icons contrast beautifully against frosted glass backgrounds. |
| **`[HierarchyBadge]`** | High | Colored pill badges sit cleanly atop the glass container without visual clutter. |
| **Selection Highlight** | High | Renders during repaint; Unity's native selection blue tint overlays seamlessly when clicked. |
