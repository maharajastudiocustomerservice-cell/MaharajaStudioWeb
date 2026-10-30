# [ComponentTerminal]

> Transforms the component into a retro terminal console complete with monospaced typography, bash command prompts, and blinking cursors.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentTerminal]` converts any component inspector into a high-authenticity command-line interface. Working in `ComponentSlot.BodyWrapper`, it themes the component with an obsidian terminal background (`BackgroundColor = "#0B0F14"`), phosphorescent green or amber monospaced text (`FontColor = "#33FF33"`), and a top shell header bar displaying a Unix command prompt (`HeaderText = "ROOT@MAHARAJA:~$"`) and system diagnostics string (`SystemInfo = "TTY-1 // MEM: 640K OK"`). It adds subtle CRT scanlines (`ShowScanlines = true`) and an animated blinking command cursor (`BlinkPrompt = true`).

**The Problem:**
Hacking mini-games, server backend simulators, terminal console emulators, and low-level memory managers look contradictory when presented as polished modern GUI widgets. Programmers and level designers miss the gritty hacker aesthetic that matches command-line game mechanics.

**The Solution:**
Decorating command-line and cybernetic components with `[ComponentTerminal]`:
- **Authentic Monospaced Shell:** Displays fields and labels in clean monospaced hacker typography.
- **Interactive Blinking Cursor:** Subtle terminal animation gives the interface an active, live-running mainframe feel.
- **Customizable Prompts & TTY Readouts:** Configure custom root hosts, user logins, and memory buffer readouts in the top terminal bar.
- **Complete Control Usability:** Keeps standard Unity numeric scrubbers, sliders, and string fields functional while giving them an authentic text console appearance.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentTerminal("GUEST@CYBERDYNE:~$", fontColor: "#33FF33", backgroundColor: "#0B0F14")]
public class CyberHackingDeck : MonoBehaviour
{
    public string targetHostIp = "192.168.0.254";
    public int breachAttemptsRemaining = 3;
    public float iceBreakerProgressPercent = 42.5f;
    public bool isProxyBypassEnabled = true;
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
| **Component Slot** | `BodyWrapper` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentTerminalAttribute()
public ComponentTerminalAttribute(string headerText, string fontColor = "#33FF33", string backgroundColor = "#0B0F14")
```

- `headerText`: Shell command prompt text displayed in the header title bar (e.g., `"ADMIN@APERTURE:~$"`).
- `fontColor`: Hex color string for terminal typography and line accents.
- `backgroundColor`: Hex color string for the dark console background plate.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `FontColor` | `string` | `"#33FF33"` | Hex color string for terminal typography and active cursor. |
| `BackgroundColor` | `string` | `"#0B0F14"` | Hex color string for the dark terminal console body. |
| `HeaderText` | `string` | `"ROOT@MAHARAJA:~$"` | Shell command prompt text displayed on the header bar. |
| `SystemInfo` | `string` | `"TTY-1 // MEM: 640K OK"` | Diagnostic status string displayed opposite the prompt. |
| `ShowScanlines` | `bool` | `true` | Whether to render subtle CRT raster scanlines on the terminal body. |
| `BlinkPrompt` | `bool` | `true` | Whether to animate the terminal cursor prompt with a realistic blink cycle. |
| `Order` | `int` | `0` | Sequence sorting order within the target component slot. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentTerminal(
    HeaderText = "OPERATOR@NORAD-SATCOM:~$", 
    SystemInfo = "TTY-4 // BUFFER: SYNCED", 
    FontColor = "#F59E0B", 
    BackgroundColor = "#0C0A09", 
    ShowScanlines = true, 
    BlinkPrompt = true)]
public class SatelliteUplinkTerminal : MonoBehaviour
{
    [Header("Telemetry & Transceiver")]
    public float uplinkFrequencyGhz = 14.25f;
    public int packetLatencyMs = 120;
    public string encryptionCipher = "AES-GCM-256";

    [Header("Orbital State")]
    public float satelliteAltitudeKm = 35786f;
    public bool isGeostationaryLockAcquired = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeaderButton]`** | High | Buttons look like physical terminal keys or command triggers on the prompt bar. |
| **`[ComponentCRTMonitor]`** | High | Combine with CRT curvature to turn the terminal into a full spherical television screen. |
| **`[ComponentSound]`** | High | Pair with mechanical keyboard clatter audio feedback on clicks. |
| **Inspector Controls** | High | Smoothly encases all fields in `BodyWrapper` without disrupting input handling or drag events. |
