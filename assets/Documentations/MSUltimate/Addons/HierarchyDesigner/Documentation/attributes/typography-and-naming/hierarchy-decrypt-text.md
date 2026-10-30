# [HierarchyDecryptText]

> Scrambles hierarchy label characters through cyber glyphs before resolving into the real GameObject name.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyDecryptText]` executes a sci-fi matrix cypher decryption sequence across the GameObject hierarchy label. At regular intervals (`Interval = 4.0f`), characters scramble through randomized alphanumeric symbols in `DecryptColor` before locking one-by-one into their resolved name in `TextColor`.

**The Problem:**
In futuristic, cyberpunk, or hacking-themed projects, standard hierarchy trees lack immersive flavor. Developers and designers working on AI directors, terminal consoles, security grids, or encryption puzzles often want these systems to visually stand out in the hierarchy with a distinctive hacker aesthetic.

**The Solution:**
Decorating components with `[HierarchyDecryptText]`:
- **Procedural Cypher Scrambling:** Replaces characters with rapidly alternating matrix glyphs that resolve left-to-right over a configured duration (`GlitchDuration = 1.2f`).
- **Dual Hue Design:** Configures distinct colors for unresolved scrambling glyphs (`DecryptColor = "#00FFAA"`) versus locked characters (`TextColor = "#2ECC71"`).
- **Periodic Cycling:** Automatically repeats the decryption cycle at user-defined intervals (`Interval = 4.0f`).
- **Bold Styling:** Ensures glyphs remain sharp and legible across all Editor scale factors.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyDecryptText(TextColor = "#2ECC71", DecryptColor = "#00FFAA", GlitchDuration = 1.0f, Interval = 5.0f)]
public class CyberTerminalConsole : MonoBehaviour
{
    public int securityAccessLevel = 4;
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
| **Render Engine** | `HierarchyDecryptTextRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyDecryptTextAttribute()
```

- Standard parameterless constructor. Decryption timings and color profiles are set via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TextColor` | `string` | `"#2ECC71"` | Hex color applied to resolved, finalized text characters. |
| `DecryptColor` | `string` | `"#00FFAA"` | Hex color applied to scrambling cypher characters during decryption. |
| `GlitchDuration` | `float` | `1.2f` | Time in seconds taken to resolve all characters from left to right. |
| `Interval` | `float` | `4.0f` | Repeat interval duration in seconds between consecutive decryption runs. |
| `Bold` | `bool` | `true` | Whether to render the glyph characters with bold font weight. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the cypher animation continues running during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row decorations. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyDecryptText(
    TextColor = "#10B981", 
    DecryptColor = "#34D399", 
    GlitchDuration = 1.5f, 
    Interval = 6.0f, 
    Bold = true)]
public class SecurityFirewallNode : MonoBehaviour
{
    [Header("Network Security")]
    public string encryptionProtocol = "AES-256-GCM";
    public bool isBreached = false;
    public float integrityPercentage = 100f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyMonospaceCodeText]`** | High Alternative | Use `[HierarchyDecryptText]` for dynamic cyber animations and `[HierarchyMonospaceCodeText]` for static terminal styling. |
| **`[HierarchyTooltip]`** | High | Display node network addresses, IP configurations, or security credentials on hover. |
| **`[HierarchyGlow]`** | High | Pair with matrix green ambient glow for maximum futuristic visual impact. |
| **`[HierarchyTextColor]`** | Incompatible | Do not stack with static color attributes as decrypt text dynamically drives label color. |
