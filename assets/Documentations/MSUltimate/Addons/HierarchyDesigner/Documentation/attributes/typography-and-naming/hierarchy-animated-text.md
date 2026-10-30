# [HierarchyAnimatedText]

> Animates the GameObject hierarchy label with real-time typography effects such as wavy motion, rainbow hue shifts, glitching, typewriter reveal, pulse, or neon flicker.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyAnimatedText]` applies procedural real-time typography animations to the GameObject's label directly within the Unity Hierarchy window. Supporting six distinct animation styles (`Wavy`, `Rainbow`, `Glitch`, `Typewriter`, `Pulse`, `NeonFlicker`), it transforms static hierarchy rows into lively visual landmarks.

**The Problem:**
In expansive projects with hundreds of actors, spawners, and active subsystems, critical GameObjects (such as boss entities during active combat, streaming managers, or network beacons) easily get lost in the sea of monotone hierarchy labels. Standard Unity provides no built-in mechanism to highlight active or important objects dynamically.

**The Solution:**
Applying `[HierarchyAnimatedText]`:
- **Six Procedural Animation Styles:** Switch seamlessly between smooth sine-wave undulations (`Wavy`), chromatic cycling (`Rainbow`), digital distortion (`Glitch`), character-by-character reveal (`Typewriter`), rhythmic breathing (`Pulse`), and electric shimmer (`NeonFlicker`).
- **Granular Motion Parameters:** Adjust oscillation amplitude, wave frequency, playback speed, and per-character phase delays.
- **Full Typography Control:** Specify custom base colors (`BaseColor = "#00FFAA"`), bold/italic styling, and pixel font sizing.
- **Continuous Repaint Engine:** Driven by an optimized hierarchy repaint lifecycle (`Continuous = true`) for buttery-smooth 60fps editor animations without runtime overhead.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyAnimatedText(
    AnimationMode = HierarchyTextAnimMode.Wavy, 
    Speed = 3.0f, 
    Amplitude = 3.0f, 
    BaseColor = "#00FFAA", 
    Bold = true)]
public class BossEncounterManager : MonoBehaviour
{
    public bool isEncounterActive = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` \| `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyAnimatedTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyAnimatedTextAttribute()
```

- Standard parameterless constructor. Animation modes and typographic parameters are configured via named object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `AnimationMode` | `HierarchyTextAnimMode` | `Wavy` | Animation mode: `Wavy`, `Rainbow`, `Glitch`, `Typewriter`, `Pulse`, `NeonFlicker`. |
| `Speed` | `float` | `2.0f` | Playback speed multiplier of the text animation. |
| `Amplitude` | `float` | `2.5f` | Displacement amplitude in pixels for wavy and bouncing motions. |
| `Frequency` | `float` | `2.0f` | Wave oscillation frequency across the text span. |
| `CharacterPhaseShift` | `float` | `0.4f` | Time phase delay between consecutive characters in wavy/sequential modes. |
| `BaseColor` | `string` | `"#00FFAA"` | Hex base color of the animated label text. |
| `Bold` | `bool` | `false` | Whether to render the label characters with bold font weight. |
| `Italic` | `bool` | `false` | Whether to render the label characters in italics. |
| `FontSize` | `int` | `0` | Custom font size in pixels (0 uses default hierarchy size). |
| `Continuous` | `bool` | `true` | Whether to continuously request hierarchy repaints for fluid animation. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether animations continue running while in Unity Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyAnimatedText(
    AnimationMode = HierarchyTextAnimMode.NeonFlicker,
    Speed = 4.0f,
    BaseColor = "#38BDF8",
    Bold = true,
    FontSize = 13)]
public class CyberpunkRadioBeacon : MonoBehaviour
{
    [Header("Broadcast Settings")]
    public float transmissionFrequency = 104.5f;
    public float signalRadius = 250f;
    public bool isBroadcasting = true;

    [ContextMenu("Toggle Broadcast")]
    public void ToggleBroadcast()
    {
        isBroadcasting = !isBroadcasting;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyGlow]`** | High | Combines animated text with ambient background halos for futuristic cyberpunk aesthetics. |
| **`[HierarchyTooltip]`** | High | Pair animated labels with informative hover tooltips detailing GameObject status. |
| **`[HierarchyBookmark]`** | High | Retains bookmark ribbon functionality while animating the central GameObject name. |
| **`[HierarchyStateColorText]`** | Mutually Exclusive | Avoid stacking with other text coloring/replacing attributes to prevent visual draw fights. |
