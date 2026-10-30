# [AccordionUnfold]

> Animates foldout groups and fields with smooth accordion height expansion and cross-fade opacity transitions.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit Transitions)`

---

## 1. Overview & Value Proposition

**What it does:**
`[AccordionUnfold]` replaces abrupt, jarring inspector visibility pop-ins with a fluid, natural accordion unfolding animation. When the decorated group, property, or collection element row attaches to the visual tree, the drawer measures the natural resolved height of the element, initializes `maxHeight = 0` and `opacity = 0`, and smoothly expands downward over a configurable duration (`UnfoldDuration`, defaulting to 300ms) using a graceful Cubic Ease-Out curve ($1 - (1 - t)^3$). It also supports optional cross-fade opacity transitions (`FadeOpacity = true`).

**The Problem:**
Standard foldouts, conditional toggles (`[ShowIf]`), and collection item expansions in Unity snap open and shut instantaneously. This abrupt layout shifting jolts developer focus and feels archaic compared to modern fluid GUI frameworks.

**The Solution:**
Decorating collapsible groups, conditional fields, or collection elements with `[AccordionUnfold]`:
- **Cubic Ease-Out Expansion:** Interpolates height smoothly from zero to full natural resolved height with a deceleration curve.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so expanding collapsible collection element rows or arrays triggers smooth accordion unfolding.
- **Synchronized Opacity Fade:** Cross-fades element opacity simultaneously (`FadeOpacity = true`) to prevent content clipping visually.
- **Automatic Layout Settlement:** Upon reaching 100% progress, automatically resets `maxHeight`, `opacity`, and `overflow` to `StyleKeyword.Null` so dynamic child resizes remain unrestricted.
- **Zero Overhead When Resting:** The schedule item terminates automatically upon completion, leaving 0% CPU consumption during steady-state inspection.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CharacterCustomization : MonoBehaviour
{
    [AccordionUnfold(unfoldDuration: 350f)]
    public string advancedFacialMorphData = "Default_Preset_A";
}
```

---

## 3. Constructors & Parameters

```csharp
public AccordionUnfoldAttribute(float unfoldDuration = 300f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `unfoldDuration` | `float` | `300f` | Expansion and collapse transition duration in milliseconds. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `UnfoldDuration` | `float` | `300f` | Total duration of the accordion height expansion in milliseconds. |
| `FadeOpacity` | `bool` | `true` | Whether to cross-fade content opacity from 0 to 1 during the unfolding transition. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

namespace MaharajaStudio.MSUltimate.AnimatedAttributes.Sample
{
    public class AccordionUnfoldExample : ModularMonoBehaviour
    {
        [Title("AccordionUnfold Attribute Showcase", "Smooth vertical accordion unfolding")]
        [InfoBox("AccordionUnfold removes abrupt snap-opens when toggling foldouts and nested inspectable panels.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Accordion Sections")]
        [AccordionUnfold(unfoldDuration: 300f, FadeOpacity = true)]
        public string graphicsBackend = "DirectX 12 (Ultimate DXR Raytracing)";

        [AccordionUnfold(unfoldDuration: 250f, FadeOpacity = true)]
        public float atmosphericDensity = 0.035f;

        [BoxGroup("2. Inside Class Demonstration")]
        public AudioSettingsNode audioSubsystem = new AudioSettingsNode();

        [BoxGroup("3. Configuration Category Manifest")]
        [InfoBox("AccordionUnfold cascades down to collections, smoothly animating accordion height unfolds across individual collection rows.", InspectorMessageType.Info)]
        [Title("Resolution Presets (Accordion Unfold Cascading)")]
        [AccordionUnfold(unfoldDuration: 280f, FadeOpacity = true)]
        public string[] displayResolutionPresets = new string[]
        {
            "1920x1080 (FHD 60FPS)",
            "2560x1440 (QHD 144FPS)",
            "3840x2160 (4K UHD HDR)"
        };

        public List<AudioSettingsNode> systemCategories = new List<AudioSettingsNode>
        {
            new AudioSettingsNode { subsystemName = "Ambience & Reverb Bus", dspBufferSamples = 512 },
            new AudioSettingsNode { subsystemName = "Voice Chat Codec Stream", dspBufferSamples = 256 }
        };

        [Serializable]
        public class AudioSettingsNode
        {
            public string subsystemName = "Spatial 3D Audio Engine";

            [AccordionUnfold(unfoldDuration: 350f, FadeOpacity = true)]
            public int dspBufferSamples = 1024;
        }

        [BoxGroup("4. Accordion Panel Controls")]
        [Button("Toggle Cinematic Graphics Preset", BackgroundColor = "#3B82F6", TextColor = "#EFF6FF")]
        public void ToggleCinematicPreset()
        {
            atmosphericDensity = 0.085f;
            audioSubsystem.dspBufferSamples = 2048;
            Debug.Log("<color=#60A5FA>[AccordionUnfold]</color> Cinematic preset applied: Volumetric fog and DSP buffers elevated.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[FoldoutGroup]` | Supported | Pairs with foldout groups to provide fluid height accordion unfolding. |
| `[ShowIf]` | Supported | Animates smoothly into view when conditional display prerequisites are satisfied. |
| `[BoxGroup]` | Supported | Expands gracefully within boxed grouping containers without layout jitter. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`string[]`, `List<T>`), smoothly unfolding row heights with cubic ease-out motion. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Collections** | Supported | Operates on direct string arrays (`string[]`), numeric arrays, and custom item lists. |
| **Nested Serializable Classes** | Supported | Fully animates fields inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions in `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
