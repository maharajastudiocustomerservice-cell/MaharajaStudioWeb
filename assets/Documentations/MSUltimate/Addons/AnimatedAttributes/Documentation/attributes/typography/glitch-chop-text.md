# [GlitchChopText]

> Applies a horizontal glitch jitter slice displacement to field labels whenever values are modified.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Hardware-Accelerated UI Toolkit Transforms)`

---

## 1. Overview & Value Proposition

**What it does:**
`[GlitchChopText]` delivers high-impact cybernetic feedback by momentarily chopping and jittering field labels horizontally when values change. Hooked directly into property modification telemetry (`TrackPropertyValue`), any modification to the field value or collection element row triggers an instantaneous glitch burst. Over `Duration` (defaulting to 250ms), the primary label shakes horizontally within `[-ChopIntensity, +ChopIntensity]` pixels (defaulting to ±4px) before snapping cleanly back to rest at $(0, 0)$.

**The Problem:**
When tweaking critical combat thresholds, overclocking multipliers, or volatility variables, standard inspectors provide silent updates without giving tactile or visceral cues that a disruptive value has been committed.

**The Solution:**
Decorating volatile parameters or collection items with `[GlitchChopText]`:
- **Immediate Value-Change Response:** Triggers exclusively upon actual data edits, providing instant visual feedback.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so modifying a specific element row in `string[]` or `List<T>` glitches only that targeted row.
- **Micro-Jitter Displacement:** Randomly shifts horizontal translation via hardware UI Toolkit transforms without causing layout reflow.
- **Configurable Intensity:** Fine-tune jitter from subtle 1.5px screen tremors up to violent 8px digital tear displacement.
- **Snappy Auto-Reset:** Automatically resets translation to exact origin coordinates upon completion of the burst duration.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ReactorCore : MonoBehaviour
{
    [GlitchChopText(chopIntensity: 5.0f, Duration = 200f)]
    public float coreTemperature = 3500f;
}
```

---

## 3. Constructors & Parameters

```csharp
public GlitchChopTextAttribute(float chopIntensity = 4.0f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `chopIntensity` | `float` | `4.0f` | Maximum horizontal pixel displacement applied during the glitch jitter. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ChopIntensity` | `float` | `4.0f` | Maximum horizontal pixel offset in either direction (`-ChopIntensity` to `+ChopIntensity`). |
| `Duration` | `float` | `250f` | Duration of the glitch shake burst in milliseconds. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

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
    public class GlitchChopTextExample : ModularMonoBehaviour
    {
        [Title("GlitchChopText Attribute Showcase", "Horizontal text slicing and chromatic displacement glitch")]
        [InfoBox("GlitchChopText imparts authentic cyberpunk video distortion onto text strings whenever edited.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Glitch Slicing Fields")]
        [GlitchChopText(chopIntensity: 4.0f, Duration = 250f)]
        public string memorySectorLog = "CORRUPT_SECTOR_0x7F: NEURAL_OVERFLOW_DETECTED";

        [GlitchChopText(chopIntensity: 6.0f, Duration = 350f)]
        public string radiationWarningPrompt = "CRITICAL: REACTOR CORE SHUTDOWN IMMINENT";

        [BoxGroup("2. Inside Class Demonstration")]
        public CorruptedTelemetryRecord primaryError = new CorruptedTelemetryRecord();

        [BoxGroup("3. Cyberware Malfunction Audit Manifest")]
        [InfoBox("Demonstrates that [GlitchChopText] operates cleanly on fields declared inside wrapper classes inside lists (List<MyClass>).", InspectorMessageType.Info)]
        public List<CorruptedTelemetryRecord> diagnosticHistory = new List<CorruptedTelemetryRecord>
        {
            new CorruptedTelemetryRecord { faultCode = "ERR_MEMORY_LEAK_01", errorStackTrace = "Heap overflow in optical targeting buffer." },
            new CorruptedTelemetryRecord { faultCode = "ERR_VOLTAGE_SPIKE_02", errorStackTrace = "Thermal throttle engaged on neural coprocessor." }
        };

        [Serializable]
        public class CorruptedTelemetryRecord
        {
            public string faultCode = "ERR_STACK_DISPLACEMENT_99";

            [GlitchChopText(chopIntensity: 5.0f, Duration = 300f)]
            public string errorStackTrace = "SYNAPSE_FAULT at address 0xFEEDC0DE in core 3";
        }

        [BoxGroup("4. Cybernetic Fault Injection Controls")]
        [Button("Inject Digital Glitch Noise", BackgroundColor = "#C026D3", TextColor = "#FDF4FF")]
        public void InjectGlitch()
        {
            memorySectorLog = $"CORRUPT_SECTOR_0x{UnityEngine.Random.Range(0x1000, 0xFFFF):X}: NEURAL_DESYNC";
            Debug.LogWarning("<color=#F472B6>[GlitchChopText]</color> Digital glitch noise injected!");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` / `[HorizontalGroup]` | Supported | Contained cleanly within group cards without clipping borders. |
| `[DiffHighlightFlash]` | Stacking | Pairs excellently: `DiffHighlightFlash` highlights the border while `GlitchChopText` jitters the label upon value changes. |
| `[ShowIf]` / `[EnableIf]` | Supported | Triggers only upon true value edits, ignoring visibility toggles. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[Range]`, and `[NotNull]`. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Direct Collections (`string[]`, `List<T>`)** | Not Supported | Direct collections are intentionally not cascaded. |
| **Wrapper Classes in Lists (`List<MyClass>`)** | Supported | Fully animates fields inside child items and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions on fields within custom serialized wrappers. |
