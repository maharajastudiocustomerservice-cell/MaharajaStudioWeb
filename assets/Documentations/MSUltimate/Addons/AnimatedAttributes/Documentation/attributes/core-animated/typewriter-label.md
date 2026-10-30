# [TypewriterLabel]

> Animates field labels with a retro typewriter character-by-character reveal effect and blinking terminal cursor.

---

## 1. Overview & Value Proposition

**What it does:**
`[TypewriterLabel]` replaces static inspector text labels with an animated, sequential character typing effect. As the inspector loads, label text appears letter-by-letter at a designated typing cadence (`TypingSpeed`), accompanied by an optional blinking terminal underscore cursor (`CursorChar`).

**The Problem:**
Narrative scripts, quest dialogues, cutscene triggers, and terminal interfaces feel sterile when configured in dry, standard inspector views. The tone of narrative tools should evoke the gameplay experience being authored.

**The Solution:**
Decorating dialogue or terminal fields with `[TypewriterLabel]`:
- **Narrative Atmosphere:** Delivers an evocative, retro terminal aesthetic directly inside developer tooling.
- **Configurable Cadence:** Adjust `TypingSpeed` in characters per second to simulate rapid telegraphs or deliberate storytelling.
- **Blinking Terminal Cursor:** Renders an authentic cursor (`_`, `|`, or custom character) with customizable blink intervals.
- **Staggered Delays:** Use `DelayBeforeStart` to sequence multiple typewriter labels down a conversation tree.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class TerminalLog : MonoBehaviour
{
    [TypewriterLabel(TypingSpeed = 30f, ShowCursor = true)]
    public string missionTransmission = "Commander, signal detected in Sector 4.";
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
public TypewriterLabelAttribute()
```

*Initializes a typewriter reveal effect running at 25 chars/sec with an underscore cursor blinking at 500ms intervals. Customize parameters via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TypingSpeed` | `float` | `25f` | Typing cadence in characters per second. |
| `ShowCursor` | `bool` | `true` | Whether to append and render an oscillating blinking cursor after the text. |
| `CursorChar` | `string` | `"_"` | Character string used for the terminal cursor indicator (e.g., `_`, `\|`, `■`). |
| `CursorBlinkRate` | `float` | `500f` | Blink interval and oscillation cycle of the cursor in milliseconds. |
| `DelayBeforeStart` | `float` | `0f` | Initial delay in milliseconds before the typing reveal begins. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class QuestDialogueEntry : MonoBehaviour
{
    [Header("Cipher Briefing")]
    [TypewriterLabel(TypingSpeed = 40f, CursorChar = "█", CursorBlinkRate = 350f)]
    public string agentCodename = "Operative Vesper";

    [TypewriterLabel(TypingSpeed = 20f, DelayBeforeStart = 600f, CursorChar = "_")]
    [TextArea(3, 6)]
    public string missionBriefing = "Infiltrate the bio-tech facility before midnight.";
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[TextArea]` | Supported | Compatible with multi-line text areas; typing animates the field label while leaving the body editable. |
| `[BoxGroup]` | Supported | Functions cleanly inside grouped headers or nested panels. |
| `[AnimatedRainbowText]` | Exclusive | Overrides static label drawing; do not stack with rainbow label effects. |
