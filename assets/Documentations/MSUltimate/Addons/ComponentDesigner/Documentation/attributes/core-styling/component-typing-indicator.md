# [ComponentTypingIndicator]

> Renders a sequentially pulsing 3-dot typing indicator at any corner of the component card to signal active dialogue, asynchronous processing, or pending AI response states.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentTypingIndicator]` brings modern messaging app motion aesthetics to Unity component cards. Injected into `ComponentSlot.BodyOverlay`, it renders three horizontally aligned dots (`Size = 5f`, `Spacing = 4f`) anchored at any specified corner (`Position = TypingIndicatorPosition.BottomRight`, `TopRight`, etc.). The dots pulse sequentially in brightness and vertical displacement at a configurable cycle tempo (`Speed = 1.5f`). It supports custom dot hues (`Color`), providing immediate visual cues for dialogue trees, NPC conversational AI, network message queues, or async background routines.

**The Problem:**
Dialogue engines, branching narrative scripts, NPC chatter managers, and chatbot AI controllers look inert in traditional inspector panels. Developers configuring conversation state machines cannot tell at a glance whether a component handles communicative dialogue logic.

**The Solution:**
Decorating conversational and async components with `[ComponentTypingIndicator]`:
- **Sequential 3-Dot Wave Motion:** Animates a recognizable chat typing wave across three dots.
- **Corner Anchoring Options:** Mount the indicator at `BottomRight`, `TopRight`, `BottomLeft`, or `TopLeft` via `TypingIndicatorPosition`.
- **Customizable Sizing & Tempo:** Adjust dot diameter (`Size`), dot gap (`Spacing`), and pulse frequency (`Speed`).
- **Full Mouse Click-Through:** Placed in `BodyOverlay` with `PickingMode.Ignore`, preserving responsiveness for all serialized fields.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentTypingIndicator(Color = "#38BDF8", Size = 6f, Speed = 1.6f, Position = TypingIndicatorPosition.BottomRight)]
public class NpcDialogueTreeRunner : MonoBehaviour
{
    public string activeSpeakerId = "NPC_ELDER_MERCHANT";
    public int currentDialogueNodeIndex = 14;
    public bool isWaitingForPlayerChoice = true;
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
| **Component Slot** | `BodyOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentTypingIndicatorAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Color` | `string` | `"#AAAAAA"` | Hex color string for the pulsing dots. |
| `Size` | `float` | `5f` | Diameter in pixels for each individual dot. |
| `Spacing` | `float` | `4f` | Horizontal gap in pixels between adjacent dots. |
| `Speed` | `float` | `1.5f` | Sequential wave pulsation speed multiplier. |
| `Position` | `TypingIndicatorPosition` | `TypingIndicatorPosition.BottomRight` | Corner placement (`TopLeft`, `TopRight`, `BottomLeft`, `BottomRight`). |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#0284C7", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#081824", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("AI COMPANION CHATTER", Subtitle = "Conversational LLM Context Streamer", BackgroundColor = "#0C2E42", TitleColor = "#E0F2FE")]
[ComponentTypingIndicator(Color = "#38BDF8", Size = 5.5f, Spacing = 4f, Speed = 1.8f, Position = TypingIndicatorPosition.TopRight)]
public class AiCompanionChatter : MonoBehaviour
{
    [Header("Chat State")]
    public string companionName = "A.R.I.A.";
    public int contextWindowTokens = 4096;
    public float temperatureCreativity = 0.7f;

    [Header("Voice Synthesis")]
    public bool isStreamingTtsAudio = true;
    public float speechRateMultiplier = 1.05f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Docking to `TopRight` places the typing dots directly inside the header bar. |
| **`[ComponentFooter]`** | High | Docking to `BottomRight` tucks the indicator neatly next to footer metadata. |
| **Inspector Controls** | High | Runs with `PickingMode.Ignore`, ensuring all standard Unity input controls remain completely responsive. |
