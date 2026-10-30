# [ComponentAnimatedBorder]

> Wraps the entire component inspector in an animated border that smoothly pulses between two alternating colors.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentAnimatedBorder]` wraps the entire component inspector inside a kinetic border frame that pulses continuously between two designated colors (`ColorA` and `ColorB`). Driven by `EditorApplication.update`, it calculates a sinusoidal interpolation ($t = \frac{\sin(\text{time} \cdot 2\pi / \text{Speed}) + 1}{2}$) to transition border colors without frame stuttering. With customizable stroke thickness (`Width`), corner rounding (`Radius`), inner padding (`Padding`), and cycle period (`Speed`), it commands immediate visual attention for critical gameplay managers, warning states, or live network nodes.

**The Problem:**
In large projects containing hundreds of components, critical managers—such as active network servers, game directors, or uncommitted database managers—blend indistinguishably into standard inspector panels. Static borders can help, but they fail to convey real-time priority or active operational states.

**The Solution:**
Decorating critical classes with `[ComponentAnimatedBorder]`:
- **Continuous Color Ping-Pong:** Smoothly blends between two signature hues (e.g. warning yellow to alert red, or neon cyan to purple).
- **BodyWrapper Slot Injection:** Transparently encapsulates the component's internal controls (`ComponentSlot.BodyWrapper`) without disrupting field layouts.
- **Hardware-Accelerated UI Toolkit Rendering:** Directly animates border color styles without redrawing the internal element hierarchy.
- **Clean Event Lifecycle:** Automatically attaches to `EditorApplication.update` only while the inspector window is mounted and visible, unhooking on detach to eliminate editor CPU drain.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentAnimatedBorder("#00BCD4", "#E040FB", Width = 2.5f, Radius = 8f, Speed = 2.0f)]
public class NetworkSyncManager : MonoBehaviour
{
    public string serverAddress = "127.0.0.1";
    public int port = 7777;
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
| **Component Slot** | `BodyWrapper` (`Order = 5`) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentAnimatedBorderAttribute(string colorA, string colorB)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `colorA` | `string` | *Required* | Starting primary color hex code for the pulse cycle. |
| `colorB` | `string` | *Required* | Alternating target color hex code for the pulse cycle. |

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ColorA` | `string` | *Set via constructor* | First alternating border color hex string. |
| `ColorB` | `string` | *Set via constructor* | Second alternating border color hex string. |
| `Width` | `float` | `2f` | Stroke width of the pulsing border in pixels. |
| `Radius` | `float` | `6f` | Corner radius in pixels for rounded container framing. |
| `Speed` | `float` | `2f` | Duration in seconds for a full complete ping-pong color cycle. |
| `Padding` | `float` | `4f` | Internal padding space between the border and child fields. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentAnimatedBorder("#F43F5E", "#E11D48", Width = 3f, Radius = 10f, Speed = 1.2f, Padding = 6f)]
public class BossFightDirector : MonoBehaviour
{
    [Header("Encounter State")]
    public string bossName = "Infernal Behemoth";
    public float currentEnragePhase = 1.0f;
    public bool isPhaseTwoActive = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Pairs seamlessly; `[ComponentBackground]` provides the inner card fill while `[ComponentAnimatedBorder]` wraps the outer perimeter. |
| **`[ComponentHeader]`** | High | The animated border encloses both the header card and all serialized fields into a unified visual unit. |
| **`[ComponentBorder]`** | Avoid | Both act as `BodyWrapper` borders; choose either static `[ComponentBorder]` or animated `[ComponentAnimatedBorder]`. |
| **`[ComponentColorCycleBorder]`** | Avoid | Conflicting border wrappers; choose two-color ping-pong (`[ComponentAnimatedBorder]`) or full HSL rainbow cycle (`[ComponentColorCycleBorder]`). |
