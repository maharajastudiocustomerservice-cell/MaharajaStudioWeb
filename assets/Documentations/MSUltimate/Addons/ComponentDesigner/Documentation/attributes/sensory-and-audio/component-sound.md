# [ComponentSound]

> Injects audible UX feedback into the inspector interface, playing customizable audio clips on hover and click events.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentSound]` enriches the developer user experience by adding tactile acoustic feedback to Unity inspector interactions. Handled via `ComponentSoundDecorator`, it attaches event listeners for UI Toolkit pointer events (`MouseEnterEvent` and `ClickEvent`) across the component's visual elements. It triggers custom audio sound effects on hover (`HoverSound`) and on click (`ClickSound`), supporting volume attenuation (`Volume = 1.0f`) and an optional filter to trigger sounds exclusively on clickable buttons rather than all element fields (`OnlyOnButtons = true`).

**The Problem:**
Complex editor tools, custom workflow buttons, and critical operations (such as "Bake NavMesh", "Deploy Build", or "Clear Cache") lack tactile and acoustic confirmation in standard Unity editors. Developers often second-guess whether a button press was registered or miss subtle UI feedback.

**The Solution:**
Decorating components with `[ComponentSound]`:
- **Audible Interaction Feedback:** Plays distinct acoustic cues on cursor hover and mouse click events to confirm UI actions.
- **Button-Only Filtering:** Set `OnlyOnButtons = true` to restrict audio playback strictly to interactive buttons.
- **Custom Sound Naming:** Provide custom audio clip resource names or use built-in editor acoustic cues (`"Hover"`, `"ButtonClick"`).
- **Graceful Fallback Pipeline:** Leverages editor audio reflection hooks, falling back safely to system beeps without crashing if audio utilities are unavailable.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentSound("Hover", "ButtonClick", Volume = 0.8f, OnlyOnButtons = true)]
public class BuildDeploymentTrigger : MonoBehaviour
{
    public string targetServerEnvironment = "Staging-US-East";
    public bool isAutomatedBakeRequired = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class, Struct` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | Decorator Lifecycle (Attached to Root Element) |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentSoundAttribute()
public ComponentSoundAttribute(string hoverSound, string clickSound)
```

- `hoverSound`: Name or resource identifier of the sound clip played when hovering over elements.
- `clickSound`: Name or resource identifier of the sound clip played when clicking elements.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HoverSound` | `string` | `"Hover"` | Sound effect identifier played on mouse hover (`MouseEnterEvent`). |
| `ClickSound` | `string` | `"ButtonClick"` | Sound effect identifier played on mouse click (`ClickEvent`). |
| `Volume` | `float` | `1f` | Audio playback volume multiplier (0.0 to 1.0). |
| `OnlyOnButtons` | `bool` | `false` | When true, audio triggers exclusively on `Button` elements rather than all fields. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#E11D48", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#1A0B10", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("SERVER SHUTDOWN OVERDRIVE", Subtitle = "Master World Instance Evacuation", BackgroundColor = "#2A0E18", TitleColor = "#FFE4E6")]
[ComponentSound("ConsoleHover", "HeavySwitchClick", Volume = 0.75f, OnlyOnButtons = true)]
public class ServerShutdownOverdrive : MonoBehaviour
{
    [Header("Evacuation Protocol")]
    public float evacuationCountdownSeconds = 30f;
    public string broadcastWarningMessage = "SERVER REBOOTING IN 30 SECONDS";
    public bool forceDisconnectActivePlayers = false;

    [Header("Snapshot Persistence")]
    public bool saveAllPlayerStatesBeforeKill = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Header buttons and action icons inherit acoustic click feedback automatically. |
| **`[ComponentPill]`** | High | Pill tab switching buttons play audio clicks on each category switch. |
| **Inspector Controls** | High | Operates via non-blocking UI Toolkit event listeners without interfering with field edits. |
