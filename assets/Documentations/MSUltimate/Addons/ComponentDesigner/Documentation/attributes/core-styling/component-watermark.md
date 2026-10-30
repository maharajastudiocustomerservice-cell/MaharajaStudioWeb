# [ComponentWatermark]

> Adds a subtle, rotated typographic watermark overlay across the background of the component card for studio branding, classification, or security markings.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentWatermark]` imprints a large, semi-transparent typographic watermark across the center of the component card canvas. Injected into `ComponentSlot.ContentOverlay`, it renders behind all serialized properties. It displays angled display text (`Text`, `FontSize = 48`, `FontStyle = BoldAndItalic`), rotated at a customizable diagonal angle (`Rotation = -15f`). Featuring low ambient opacity (`Opacity = 0.04f`), custom color tinting (`Color`), and alignment anchors (`Alignment`, `VerticalAlignment`), it gives component cards an official studio branding mark or security classification without reducing field readability.

**The Problem:**
Confidential builds, proprietary studio tools, architecture layers, and framework modules lack persistent identity when viewed in the inspector. Watermarking scripts with comments is easily ignored, and static banner cards can occupy valuable vertical screen space.

**The Solution:**
Decorating proprietary systems with `[ComponentWatermark]`:
- **Large Typographic Branding:** Projects prominent 48pt angled text (e.g. `"CONFIDENTIAL"`, `"CORE"`, `"MAHARAJA"`) directly into the background.
- **Ultra-Subtle Default Opacity:** Defaults to `0.04f` opacity, ensuring foreground fields, buttons, and sliders remain 100% sharp and readable.
- **Customizable Angle & Scale:** Adjust diagonal rotation (`Rotation = -15f`) and typography size to fit any component card.
- **Zero Input Interference:** Positioned in `ContentOverlay` with `PickingMode.Ignore`, preserving complete click-through interaction.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentWatermark("PROPRIETARY", Color = "#EF4444", Opacity = 0.05f, Rotation = -12f)]
public class ProprietaryPhysicsSolver : MonoBehaviour
{
    public float solverSubStepCount = 8f;
    public bool enableCustomClothSimulation = true;
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
public ComponentWatermarkAttribute(string text)
```

- `text`: Primary watermark string displayed diagonally in the background (e.g. `"CONFIDENTIAL"`).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | *(Constructor)* | Primary watermark string displayed in the background. |
| `Color` | `string` | `"#FFFFFF"` | Hex color string for watermark typography. |
| `Opacity` | `float` | `0.04f` | Transparency alpha of the watermark text (0.0 to 1.0). |
| `FontSize` | `int` | `48` | Font size in points for watermark text. |
| `FontStyle` | `FontStyle` | `FontStyle.BoldAndItalic`| Font styling (`Normal`, `Bold`, `Italic`, `BoldAndItalic`). |
| `Rotation` | `float` | `-15f` | Diagonal tilt angle in degrees. |
| `Alignment` | `UiAlignment` | `UiAlignment.Center` | Horizontal alignment (`Left`, `Center`, `Right`). |
| `VerticalAlignment` | `ComponentVerticalAlignment` | `ComponentVerticalAlignment.Center` | Vertical alignment (`Top`, `Center`, `Bottom`). |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#4F46E5", Width = 1.5f, Radius = 8f)]
[ComponentBackground("#0D0E24", BorderRadius = 8f, Padding = 10f)]
[ComponentHeader("ANTI-CHEAT ENGINE HOOK", Subtitle = "Kernel Memory Integrity Sentinel", BackgroundColor = "#16183B", TitleColor = "#E0E7FF")]
[ComponentWatermark("SECURITY CORE", Color = "#818CF8", Opacity = 0.06f, FontSize = 44, Rotation = -10f)]
public class AntiCheatEngineHook : MonoBehaviour
{
    [Header("Memory Verification")]
    public float integrityScanFrequencySeconds = 10f;
    public int checksumHashBucketSize = 1024;
    public bool enableDllSignatureValidation = true;

    [Header("Heartbeat")]
    public string backendSentinelEndpoint = "https://guard.studio.internal";
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Renders on top of solid background fills in `ContentOverlay` with clean contrast. |
| **`[ComponentBorder]`** | High | The large watermark text is clipped cleanly within the bordered container bounds. |
| **Inspector Controls** | High | `PickingMode.Ignore` ensures complete click-through transparency for all inspector controls. |
