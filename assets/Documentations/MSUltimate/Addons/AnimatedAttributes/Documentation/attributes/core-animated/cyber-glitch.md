# [CyberGlitch]

> Applies randomized cyberpunk glitch offset, scale jitter, and chromatic displacement bursts at randomized time intervals.

---

## 1. Overview & Value Proposition

**What it does:**
Injects an authentic sci-fi/cyberpunk aesthetic into inspector fields by triggering randomized glitch bursts. At randomized intervals between `MinInterval` and `MaxInterval`, the field briefly jitters horizontally and vertically (`GlitchIntensity`) for a split second (`GlitchDuration`) before snapping back to stability.

**The Problem:**
Styling sci-fi weapons, corrupted AI modules, hacker toolkits, or alien artifacts in the Inspector usually relies on static dark gray skins that lack genre immersion.

**The Solution:**
Add `[CyberGlitch]` to any field:
- **Atmospheric Genre Immersion:** Creates a realistic digital malfunction effect.
- **Randomized Timing:** Jitters unpredictably within min/max second windows to mimic authentic electronic interference.
- **Intensity Tuning:** Control displacement jitter distance in pixels (`GlitchIntensity`).
- **Zero Input Disruption:** Purely visual effect; fields remain 100% interactable during glitching.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CorruptedAI : MonoBehaviour
{
    [CyberGlitch(GlitchIntensity = 6f, MinInterval = 2f, MaxInterval = 4f)]
    public string rogueSubroutine = "SYS_OVERRIDE_0x88";
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
public CyberGlitchAttribute()
```

*Attribute initializes with standard cyberpunk jitter settings; customize properties via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GlitchIntensity` | `float` | `5f` | Maximum pixel displacement jitter during glitch bursts. |
| `MinInterval` | `float` | `1f` | Minimum delay in seconds between glitch bursts. |
| `MaxInterval` | `float` | `5f` | Maximum delay in seconds between glitch bursts. |
| `GlitchDuration` | `float` | `0.15f` | Duration of each glitch burst in seconds. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CyberpunkWeapon : MonoBehaviour
{
    [Header("Overclocked Plasma Core (Corrupted Mod)")]
    [CyberGlitch(GlitchIntensity = 8f, MinInterval = 1.5f, MaxInterval = 3.5f, GlitchDuration = 0.2f)]
    public float overclockInstability = 45.2f;

    [CyberGlitch(GlitchIntensity = 4f)]
    public string neuralFirmwareHash = "SHA256:0xDEADC0DE";
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Glitch displacement is contained cleanly inside layout groups. |
| `[AnimatedGradientBackground]` | Supported | Stacks with neon gradients for total cyberpunk presentation. |
| Primary Drawers | Supported | Operates strictly via transform offsets without disrupting field inputs. |
