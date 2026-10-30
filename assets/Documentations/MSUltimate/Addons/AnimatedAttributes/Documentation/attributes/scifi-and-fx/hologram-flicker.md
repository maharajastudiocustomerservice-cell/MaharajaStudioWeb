# [HologramFlicker]

> Applies holographic transmission interference with periodic micro-flickering, chromatic shifts, and subtle opacity jitter.

---

## 1. Overview & Value Proposition

**What it does:**
`[HologramFlicker]` gives inspector fields an unstable, ethereal holographic projection aesthetic. Powered by UI Toolkit's scheduling system, it monitors the target property and periodically introduces probabilistic micro-flickering (`FlickerIntensity`). When a flicker event triggers, the element momentarily jitters its opacity (`Random.Range(0.75f, 1.0f)`) and tints the text in a futuristic holographic hue (`HoloTint`), settling back to standard rendering between flicker cycles.

**The Problem:**
Holographic comms arrays, glitchy transmissions, AI avatar dialogues, or damaged telemetry consoles often look too crisp, stable, and solid in the editor. Without subtle transmission instability, they fail to feel like projected light beams traveling across lightyears.

**The Solution:**
Decorating holographic, transmission, or AI properties with `[HologramFlicker]`:
- **Unstable Projection Jitter:** Probabilistically flickers opacity and color based on `FlickerIntensity`, simulating photon decay.
- **Futuristic Holographic Tint:** Applies signature sci-fi projection hues (`HoloTint`, defaulting to `#00F0FF` cyan) during micro-flicker events.
- **Zero Distraction Tuning:** Designed with subtle ranges (`FlickerIntensity = 0.15f`) to deliver mood without impeding data entry or causing eye fatigue.
- **Direct Element Modulation:** Seamlessly binds to the parent element hierarchy via `AnimationTargetHelper`, requiring zero extra wrapper containers.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class HologramCommArray : MonoBehaviour
{
    [HologramFlicker(holoTint: "#00F0FF", flickerIntensity: 0.15f)]
    public string incomingTransmissionLog = "RECEIVING ENCRYPTED BEACON...";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public HologramFlickerAttribute(string holoTint = "#00F0FF", float flickerIntensity = 0.15f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `holoTint` | `string` | `"#00F0FF"` | Hex tint color applied during holographic micro-flicker shifts. |
| `flickerIntensity` | `float` | `0.15f` | Probability (from `0f` to `1f`) that a flicker event triggers per tick. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HoloTint` | `string` | `"#00F0FF"` | Hex tint color of the holographic glow (defaults to Electric Cyan). |
| `FlickerIntensity` | `float` | `0.15f` | Probability amplitude controlling flicker frequency. |
| `ScanlineAlpha` | `float` | `0.18f` | Opacity alpha value of overlay scanlines. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ShipAIInterface : MonoBehaviour
{
    [Header("AI Persona Signal")]
    [HologramFlicker(
        holoTint: "#38BDF8", 
        flickerIntensity: 0.22f, 
        ScanlineAlpha = 0.25f
    )]
    public string aiPersonaStatus = "AURA_V3: SUBROUTINE_ONLINE";

    [Header("Degraded Holo-Projector")]
    [HologramFlicker(holoTint: "#A855F7", flickerIntensity: 0.35f)]
    public float projectorSignalDegradation = 42.8f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Applies holographic flicker to fields enclosed in card and box groupings. |
| `[CRTScanlineOverlay]` | Stacking | Combines vertical scanlines with holographic opacity flicker for vintage terminals. |
| `[ReadOnly]` | Supported | Accentuates incoming transmission logs and AI dialogue readouts. |
