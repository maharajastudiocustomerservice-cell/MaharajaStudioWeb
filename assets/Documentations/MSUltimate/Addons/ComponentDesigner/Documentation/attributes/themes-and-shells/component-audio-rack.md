# [ComponentAudioRack]

> Restyles the component inspector as an authentic studio rack-mount audio unit with brushed metal faceplates, corner mounting screws, and glowing LED meters.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentAudioRack]` transforms component inspectors into hardware audio processing units inspired by 19-inch studio gear. Operating in `ComponentSlot.BodyWrapper`, it encases the component inside a brushed aluminum or dark anodized steel chassis. The shell is complete with realistic corner hex mounting screws (`ShowScrews = true`), a stylized unit model plate (`UnitName = "DSP MASTER RACK"`), configurable rack unit height standards (`RackUnits = 1` or `2`), and glowing LED indicators (`LedColor = "#10B981"`).

**The Problem:**
Audio equalizers, reverb processors, dynamic compressors, synthesizer oscillators, and sound effect routers look plain and generic in Unity's standard gray inspector. Sound designers miss the tactile feel of physical outboard hardware racks when balancing studio-grade acoustic parameters.

**The Solution:**
Decorating audio processing and DSP components with `[ComponentAudioRack]`:
- **Physical Studio Hardware Aesthetic:** Replicates the industrial look and feel of high-end analog mastering racks.
- **Configurable Form Factors:** Choose between standard 1U compact and 2U expanded rack heights to suit parameter complexity.
- **Vibrant LED Indicators:** Add hardware flair with illuminated emerald green, amber, or ruby signal lights.
- **Corner Mounting Screws:** Precision-rendered hex rack bolts anchor the chassis into a virtual studio rack stack.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentAudioRack("DYNAMIC MASTER COMPRESSOR", ledColor: "#10B981", rackUnits: 1)]
public class DynamicMasterCompressor : MonoBehaviour
{
    public float thresholdDb = -18f;
    public float compressionRatio = 4.0f;
    public float attackTimeMs = 15f;
    public float releaseTimeMs = 240f;
    public float makeupGainDb = 3.5f;
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
| **Component Slot** | `BodyWrapper` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentAudioRackAttribute()
public ComponentAudioRackAttribute(string unitName, string ledColor = "#10B981", int rackUnits = 1)
```

- `unitName`: Text displayed on the front panel metal badge (e.g. `"DSP 7-BAND PARAMETRIC EQ"`).
- `ledColor`: Hex color string for illuminated LED indicator lights and VU meters.
- `rackUnits`: Standard rack height tier (`1` for 1U standard, `2` for 2U double-height).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `UnitName` | `string` | `"DSP MASTER RACK"` | Nameplate text stamped onto the faceplate of the audio unit. |
| `RackUnits` | `int` | `1` | Form-factor rack height in standard unit increments (1U or 2U). |
| `LedColor` | `string` | `"#10B981"` | Hex color string for the power and signal LED lamps. |
| `ShowScrews` | `bool` | `true` | Whether to render industrial corner mounting screws in the outer flanges. |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentAudioRack(UnitName = "VINTAGE TUBE TAPE SATURATOR", LedColor = "#F59E0B", RackUnits = 2, ShowScrews = true)]
public class VintageTubeTapeSaturator : MonoBehaviour
{
    [Header("Input Drive & Tube Bias")]
    [Range(0f, 24f)] public float inputDriveDb = 8.5f;
    [Range(0f, 100f)] public float tubeWarmthPercentage = 68f;
    public bool isTriodeModeEngaged = true;

    [Header("Tape Flutter & Wow")]
    [Range(0f, 1f)] public float tapeWowRateHz = 0.35f;
    [Range(0f, 1f)] public float tapeFlutterDepth = 0.12f;
    public float tapeHissVolumeDb = -62f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeaderButton]`** | High | Buttons integrate neatly onto the faceplate to simulate physical bypass or test buttons. |
| **`[ComponentSound]`** | High | Pairs naturally with tactile switch clicks and rotary knob audio cues. |
| **Audio Sliders & Knobs** | High | Dial knobs and frequency sliders look right at home inside the hardware rack chassis. |
| **Inspector Controls** | High | Encases controls cleanly in `BodyWrapper` without disrupting input handling or undo tracking. |
