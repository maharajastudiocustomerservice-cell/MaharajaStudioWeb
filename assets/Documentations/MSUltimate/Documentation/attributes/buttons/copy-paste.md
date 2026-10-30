# [CopyPaste]

> Attaches compact "Copy" and "Paste" action buttons adjacent to serialized fields and complex structs for instant data transfer.

---

## 1. Overview & Value Proposition

**What it does:**
Adds dedicated "Copy" and "Paste" buttons next to any field or struct for instant data transfer.

**The Problem:**
Copying complex settings (like character stats, animation curves, color palettes, or arrays) between GameObjects in standard Unity is tedious. You either have to copy the whole component and overwrite everything else, or manually re-type every number one by one.

**The Solution:**
Add `[CopyPaste]` above any field, struct, or class:
- **1-Click Clipboard:** Click "Copy" to save data to the system clipboard, and "Paste" to apply it to any matching field.
- **Works on Complex Structs:** Copies entire classes, nested data structures, arrays, and lists seamlessly.
- **Cross-Scene & Prefab Transfer:** Easily transfer data across different GameObjects, prefabs, or even across different scenes.
- **Full Undo Support:** Every paste operation registers with Unity's Undo system (`Ctrl+Z`), so your work is always safe.

---

## 2. Quick Start

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CharacterPreset : MonoBehaviour
{
    [Serializable]
    public struct CombatStats
    {
        public float baseAttack;
        public float defense;
        public float criticalChance;
    }

    [CopyPaste]
    public CombatStats stats;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | Serialized classes, structs, arrays, primitive types, vectors, colors |
| **Collection Cascading** | Supported (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>` via `ICollectionElementAttribute`) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public CopyPasteAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CopyButtonText` | `string` | `"📄"` | Text or emoji displayed on the copy button. |
| `PasteButtonText`| `string` | `"📋"` | Text or emoji displayed on the paste button. |
| `CopyIcon` | `string` | `""` | Unity Editor icon name for the Copy button (e.g. `"TreeEditor.Duplicate"`). |
| `PasteIcon` | `string` | `""` | Unity Editor icon name for the Paste button (e.g. `"Clipboard"`). |
| `ShowLabel` | `bool` | `true` | Whether to display the field's standard label. |
| `ButtonWidth` | `float` | `24f` | Width of the copy/paste icon buttons in pixels. |
| `Height` | `float` | `20f` | Height of the copy/paste icon buttons in pixels. |
| `Spacing` | `float` | `2f` | Spacing gap between the copy and paste buttons. |
| `Alignment` | `UiAlignment` | `UiAlignment.Right`| Placement alignment of the button group. |
| `ButtonColor` | `string` | `""` | Hex background color for the copy and paste buttons. |
| `TextColor` | `string` | `""` | Hex text color for button labels. |
| `BorderColor` | `string` | `""` | Hex border color for the buttons. |
| `BorderWidth` | `float` | `1f` | Border line thickness in pixels. |
| `BorderRadius` | `float` | `3f` | Corner rounding radius of the button frames. |
| `Padding` | `float` | `3f` | Inner padding in pixels inside buttons. |
| `MarginLeft` | `float` | `0f` | Left margin spacing in pixels. |
| `MarginRight` | `float` | `0f` | Right margin spacing in pixels. |
| `MarginTop` | `float` | `0f` | Top margin spacing in pixels. |
| `MarginBottom` | `float` | `0f` | Bottom margin spacing in pixels. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

namespace MaharajaStudio.MSUltimate.Example
{
    [AddComponentMenu("Maharaja Studio/MSUltimate/Samples/Buttons/Copy Paste Example")]
    public class CopyPasteExample : ModularMonoBehaviour
    {
        [Serializable]
        public struct AudioBusProfile
        {
            public string busName;
            [CustomRange(-24f, 12f)] public float lowBandGain;
            [CustomRange(-24f, 12f)] public float midBandGain;
            [CustomRange(-24f, 12f)] public float highBandGain;
            [CustomRange(0.1f, 5f)] public float reverbDecay;
            [CustomRange(0f, 1f)] public float masterVolume;
        }

        [Title("Copy Paste Attribute Showcase", "1-click serialized data clipboard copying and pasting",
            Alignment = UiAlignment.Center, BackgroundColor = "#1E293B", TextColor = "#38BDF8")]
        [InfoBox("[CopyPaste] attaches compact Copy (📄) and Paste (📋) buttons directly adjacent to inspector properties. Transfer complex structs, vectors, colors, or configurations between slots instantly.", InspectorMessageType.Info)]

        // ─── Pillar 1 & 2: Standalone & Nested Struct Usage ────────────────────────
        [BoxGroup("1. Audio Equalizer Profiles", BackgroundColor = "#0F172A", BorderColor = "#334155", BorderRadius = 6, MarginBottom = 8)]
        [CopyPaste(ButtonColor = "#1E293B", BorderColor = "#3B82F6", BorderRadius = 4f, Spacing = 4f, ButtonWidth = 26f, Height = 22f)]
        public AudioBusProfile dialogueBus = new AudioBusProfile
        {
            busName = "Dialogue_Master",
            lowBandGain = -2f,
            midBandGain = 4.5f,
            highBandGain = 1.2f,
            reverbDecay = 0.8f,
            masterVolume = 0.95f
        };

        [CopyPaste(ButtonColor = "#1E293B", BorderColor = "#10B981", BorderRadius = 4f, Spacing = 4f, ButtonWidth = 26f, Height = 22f)]
        public AudioBusProfile sfxBus = new AudioBusProfile
        {
            busName = "SFX_Master",
            lowBandGain = 3.5f,
            midBandGain = -1.0f,
            highBandGain = 5.0f,
            reverbDecay = 1.6f,
            masterVolume = 0.85f
        };

        // ─── Pillar 3: Direct Collections Cascading ───────────────────────────────
        [BoxGroup("2. Direct Collections (Cascading Showcase)", BackgroundColor = "#0F172A", BorderColor = "#10B981", BorderRadius = 6, MarginBottom = 8)]
        [InfoBox("Direct collection cascading: [CopyPaste] implements ICollectionElementAttribute to automatically add individual Copy and Paste buttons to each row in arrays and lists.", InspectorMessageType.Info)]

        [Title("Preset Color Palette Swatches (Array)")]
        [CopyPaste(ButtonColor = "#1E293B", BorderColor = "#10B981", ButtonWidth = 24f, Height = 20f)]
        public Color[] themePaletteColors = new Color[]
        {
            new Color(0.2f, 0.6f, 1.0f, 1.0f),
            new Color(0.1f, 0.8f, 0.4f, 1.0f),
            new Color(0.9f, 0.3f, 0.3f, 1.0f)
        };

        [Title("Spatial Telemetry Coordinate Waypoints (List)")]
        [CopyPaste(ButtonColor = "#1E293B", BorderColor = "#3B82F6", ButtonWidth = 24f, Height = 20f)]
        public List<Vector3> patrolWaypoints = new List<Vector3>
        {
            new Vector3(0, 0, 0),
            new Vector3(15, 2, -5),
            new Vector3(30, 0, 10)
        };

        // ─── Pillar 4: Interactive Playground ─────────────────────────────────────
        [BoxGroup("3. Interactive Playground", BackgroundColor = "#0F172A", BorderColor = "#EAB308", BorderRadius = 6)]
        [Button("Compare Profile A vs Profile B", BackgroundColor = "#2563EB", TextColor = "#FFFFFF")]
        public void CompareProfiles()
        {
            Debug.Log($"[CopyPaste] Dialogue: Vol={dialogueBus.masterVolume:P0} | SFX: Vol={sfxBus.masterVolume:P0}");
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### Attribute Stacking

| Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Integrates cleanly inside box groups and compact inspector panels. |
| `[ShowIf]` / `[HideIf]` | Supported | Dynamic visibility controls show or hide the property alongside its copy/paste buttons. |
| `[ReadOnly]` | Supported | In read-only mode, the Copy button remains functional while Paste is disabled. |

### Collection Cascading Matrix

| Collection Type | Element Type | Supported | Notes |
| :--- | :--- | :---: | :--- |
| `T[]` (Array) | `Color[]`, `Vector3[]`, `string[]` | Yes | Individual Copy & Paste buttons render on every element row. |
| `List<T>` | `List<AudioBusProfile>`, `List<Vector3>` | Yes | Cascades down to individual elements automatically. |
| `AdvancedList<T>` | Any serializable type | Yes | Fully supported in reorderable list items. |
| `SerializableDictionary<K, V>` | Key or Value elements | Yes | Elements receive dedicated clipboard controls. |
| `[Serializable] class/struct` | Nested properties | Yes | Entire struct or inner members can be copied and pasted. |
| **Undo Support** | `Undo.RecordObject` | Yes | Every paste operation is registered with Unity's Undo stack (`Ctrl+Z`). |

