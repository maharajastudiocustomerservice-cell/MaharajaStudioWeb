# BinaryStreamText

> `[BinaryStreamText]` · Target: `Field | Property` · Category: `Typography` · Assembly: `MSUltimate-AnimatedAttributes`

---

## 1. Overview & Value Proposition

In sci-fi, cyberpunk, or modern terminal interfaces, static field labels feel rigid and unresponsive. Standard Unity inspector labels cannot communicate real-time digital computation, network handshakes, or cryptographic ciphers.

`[BinaryStreamText]` transforms any field label into a live digital stream. Individual characters intermittently flicker into raw bits (`'0'`, `'1'`) or hexadecimal bytes (`'0'`–`'F'`) before resolving back into readable text. Hovering or clicking the field triggers an interactive sequential sweep wave across all characters, delivering immediate visual tactility to technical gameplay parameters.

---

## 2. Quick-Start Snippet

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class SecurityTerminal : MonoBehaviour
{
    [BinaryStreamText(25f, 0.2f, "#10B981")]
    public string UplinkCipher = "SEC_ALPHA_NODE_99";
}
```

---

## 3. Constructors & Signatures

```csharp
// Default constructor (25 Hz flicker, 15% flicker probability, emerald stream color)
public BinaryStreamTextAttribute();

// Parameterized constructor with custom speed, probability, and stream color
public BinaryStreamTextAttribute(float flickerSpeed, float flickerChance = 0.15f, string streamColor = "#10B981");
```

---

## 4. Properties & Customization Table

| Property | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `FlickerSpeed` | `float` | `25f` | Flickering update frequency in hertz. |
| `FlickerChance` | `float` | `0.15f` | Probability (0.0 to 1.0) that any character flickers to a bit or byte. |
| `StreamColor` | `string` | `"#10B981"` | Highlight color for digital glyphs during flickering (hex code). |
| `UseHexDigits` | `bool` | `false` | When true, includes hex characters (`0`–`F`); otherwise pure binary (`0`, `1`). |
| `HoverWave` | `bool` | `true` | Whether mouse hover triggers a sequential decode sweep. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class CyberpunkHackingRig : ModularMonoBehaviour
{
    [Title("Security Telemetry", "Live encryption channel telemetry", BackgroundColor = "#022c22", TextColor = "#34D399")]

    [BoxGroup("Core Channels")]
    [BinaryStreamText(30f, 0.25f, "#10B981")]
    public string PrimaryCipherKey = "SEC-QUANTUM-NODE-404";

    [BoxGroup("Core Channels")]
    [BinaryStreamText(40f, 0.35f, "#38BDF8", UseHexDigits = true)]
    public string MemoryBusPointer = "0x7FFE_A10B_44F2";

    [BoxGroup("Gateway Manifest")]
    public List<GatewaySlot> ConnectedGateways = new List<GatewaySlot>
    {
        new GatewaySlot("GATEWAY_NORTH_RELAY", 443),
        new GatewaySlot("PERIMETER_SAT_UPLINK", 8080)
    };

    [Serializable]
    public class GatewaySlot
    {
        [BinaryStreamText(20f, 0.15f, "#EC4899")]
        public string Hostname;

        public int Port;

        public GatewaySlot(string host, int port)
        {
            Hostname = host;
            Port = port;
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Domain | Compatibility | Notes |
| :--- | :---: | :--- |
| **`[BoxGroup]` & `[TabGroup]`** | Compatible | Safely measures container widths and aligns cleanly inside nested cards. |
| **`[ShowIf]` & `[EnableIf]`** | Compatible | Halts scheduled animation timer when element is hidden or disabled. |
| **`[AdvancedClass]`** | Compatible | Operates seamlessly inside custom serializable classes and structs. |
| **Lists (`List<TClass>`)** | Compatible | Re-attaches safely during virtualized list row recycling without DOM leaks. |
| **Raw String Arrays (`string[]`)** | Intentional Wrapper | Excluded from direct primitive collections to prevent visual clutter; wrap in class. |

---

## 7. Performance & Architecture

- **UI Toolkit Native:** Replaces target labels with safe sibling container layouts, preventing Unity 6 UIR `DepthFirstOnVisualsChanged` assertion crashes.
- **Garbage Free:** Pre-allocated lookup pools for binary and hexadecimal character buffers.
- **Zero Update Loop Overhead:** Uses UI Toolkit scheduled items running at 30 fps without polling in MonoBehaviour `Update`.

