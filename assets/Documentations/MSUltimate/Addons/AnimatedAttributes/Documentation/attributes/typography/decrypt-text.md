# [DecryptText]

> Animates field labels by scrambling through randomized matrix cipher characters before resolving letter-by-letter.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (Efficient UI Toolkit Text Transitions)`

---

## 1. Overview & Value Proposition

**What it does:**
`[DecryptText]` adds a sci-fi hacker or cyberpunk terminal decoding effect to inspector labels and string fields. Upon mounting or clicking the field (`TriggerOnFocus`), the text begins in a fully scrambled matrix cipher, displaying randomly cycling symbols from a designated character set (`ScrambleChars`) rendered in a phosphor green glow (`GlitchColor`, defaulting to `#00FF66`). At a rate determined by `ResolveSpeed` (defaulting to 20 characters per second), glyphs resolve sequentially from left to right into their actual names, restoring the original font styling once fully decoded.

**The Problem:**
In sci-fi, espionage, or hacking-themed projects, standard inspector panels appear flat and disconnected from the game's aesthetic. Highlighting classified game state, security clearance levels, or encrypted parameters with standard static labels fails to evoke high-tech immersion.

**The Solution:**
Decorating encrypted parameters or string collections with `[DecryptText]`:
- **Sci-Fi Matrix Decoding:** Progressively unscrambles text strings with rapid character churning.
- **Collection Element Cascading:** Implements `ICollectionElementAttribute` so array and list string elements unscramble independently when viewed or inspected.
- **Customizable Cipher Alphabet:** Swap out the default punctuation/hex string for binary (`"01"`), runes, or custom glyph sets.
- **Luminous Glitch Hue:** Scrambled characters glow in neon phosphor green (`GlitchColor`) before stabilizing.
- **Interactive Focus Trigger:** Re-triggers the decryption sequence whenever the designer clicks or modifies the target field.
- **Whitespace Preservation:** Automatically preserves spaces and whitespace formatting so word structures remain legible during the decrypt process.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SecurityTerminal : MonoBehaviour
{
    [DecryptText(resolveSpeed: 25f, glitchColor: "#00FF66")]
    public string clearanceOverrideCode = "DELTA-OMEGA-99";
}
```

---

## 3. Constructors & Parameters

```csharp
public DecryptTextAttribute()

public DecryptTextAttribute(float resolveSpeed, string glitchColor = "#00FF66")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `resolveSpeed` | `float` | `20f` | Number of characters decoded per second. |
| `glitchColor` | `string` | `"#00FF66"` | Hex color string applied to unresolved scrambling characters. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ResolveSpeed` | `float` | `20f` | Rate of character decoding in glyphs per second. |
| `ScrambleChars` | `string` | `"!@#$%^&*()_+-=[]{}|;:,.<>?/0123456789ABCDEF"` | Pool of characters randomly sampled during the scramble phase. |
| `GlitchColor` | `string` | `"#00FF66"` | Color tint applied to unresolved matrix characters. |
| `TriggerOnFocus` | `bool` | `true` | When true, replays the decrypt sequence on mouse click / field interaction. |
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
    public class DecryptTextExample : ModularMonoBehaviour
    {
        [Title("DecryptText Attribute Showcase", "Cyberpunk terminal matrix character scramble")]
        [InfoBox("DecryptText animates text strings and labels by cascading through random cyber/matrix characters before resolving sequentially.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Decryption Terminals")]
        [DecryptText(resolveSpeed: 20f, glitchColor: "#00FF66", TriggerOnFocus = true)]
        public string classifiedAgentCodename = "PROJECT-ICARUS-ZERO: AGENT NIGHTSHADE";

        [DecryptText(resolveSpeed: 30f, glitchColor: "#00F0FF", TriggerOnFocus = true)]
        public string alienSignalDecoded = "COSMIC-BEACON: GALAXY-NGC-4826-DISCOVERED";

        [BoxGroup("2. Inside Class Demonstration")]
        public ClassifiedIntelligenceDocket primaryDocket = new ClassifiedIntelligenceDocket();

        [BoxGroup("3. Intelligence Agency Wiretap Manifest")]
        [InfoBox("Demonstrates that [DecryptText] decodes cleanly on fields declared inside wrapper classes inside lists (List<MyClass>).", InspectorMessageType.Info)]
        public List<ClassifiedIntelligenceDocket> wiretapLogs = new List<ClassifiedIntelligenceDocket>
        {
            new ClassifiedIntelligenceDocket { clearanceTier = "CONFIDENTIAL", missionBriefing = "Intercepted diplomatic courier frequency encrypted." },
            new ClassifiedIntelligenceDocket { clearanceTier = "RESTRICTED", missionBriefing = "Cyber-grid firewall breached in sub-level 4." }
        };

        [Serializable]
        public class ClassifiedIntelligenceDocket
        {
            public string clearanceTier = "TOP SECRET // EYES ONLY";

            [DecryptText(resolveSpeed: 25f, glitchColor: "#C084FC")]
            public string missionBriefing = "Infiltrate orbital satellite uplink at 0200 hours.";
        }

        [BoxGroup("4. Cryptographic Terminal Controls")]
        [Button("Scramble & Decrypt New Message", BackgroundColor = "#00FF66", TextColor = "#022C22")]
        public void DecryptNewMessage()
        {
            classifiedAgentCodename = "PROJECT-ICARUS-ZERO: AGENT VIPER-STRIKE";
            Debug.Log("<color=#00FF66>[DecryptText]</color> Scramble buffer activated! Matrix characters resolving.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` / `[HorizontalGroup]` | Supported | Fits cleanly inside cyber-themed container cards and group boxes. |
| `[ShowIf]` / `[EnableIf]` | Supported | Automatically fires the decrypt sequence upon conditional reveal. |
| `[BouncingText]` / `[WavyText]` | Avoid | Multiple text mutation attributes modifying the same label will conflict; use one kinetic text effect per field. |
| Validation Attributes | Supported | Fully compatible with `[Required]`, `[NotNull]`, and string validations. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Direct Collections (`string[]`, `List<string>`)** | Not Supported | Direct string arrays and lists are intentionally not cascaded. |
| **Wrapper Classes in Lists (`List<MyClass>`)** | Supported | Fully functions inside child classes and structs declared within lists. |
| **Custom Serializers** | Supported | Seamlessly functions on fields within custom serialized wrappers. |
