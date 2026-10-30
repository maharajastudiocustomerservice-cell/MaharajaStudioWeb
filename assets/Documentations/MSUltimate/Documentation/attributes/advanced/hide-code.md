# [HideCode]

> Conceals automatic source code extraction and decompilation display from inspectable methods, classes, and structs.

---

## 1. Overview & Value Proposition

**What it does:**
Hides source code blocks from the Inspector so sensitive algorithms or messy internal methods remain concealed.

**The Problem:**
When you use features like `[ShowCode]` to show designers how a method works, or when building tools for other teams, some methods contain complex math, proprietary formulas, or messy boilerplate that you don't want displayed in the Inspector.

**The Solution:**
Add `[HideCode]` above any method, class, struct, or interface:
- **Clean Inspector View:** Keeps the button or field visible while hiding the source code viewer.
- **Protects Secret Logic:** Prevents proprietary math or security keys from being shown on screen.
- **Class-Level Control:** Place it at the top of a class to hide code across all methods at once.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SecurityManager : MonoBehaviour
{
    [Button("Generate Encryption Key")]
    [HideCode]
    public void GenerateKey()
    {
        // Internal cryptographic logic is hidden from inspector view
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Class | AttributeTargets.Struct | AttributeTargets.Interface | AttributeTargets.Method` |
| **Allow Multiple** | `false` |
| **Inherited** | `false` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public HideCodeAttribute()
```

---

## 5. Properties & Customization Options

*This attribute is a marker directive and does not expose additional configuration properties.*

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameAnalyticsService : MonoBehaviour
{
    [ShowCode(Title = "Public Event Dispatcher")]
    public void TrackPublicEvent(string eventName)
    {
        Debug.Log($"[Analytics] Dispatching: {eventName}");
    }

    [Button("Process Secure Telemetry")]
    [HideCode]
    public void ProcessSecurePayload()
    {
        // Confidential hashing & auth handshake hidden from inspector view
    }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Pairing with `[Button]`:** Safely keeps the interactive button visible while ensuring source decompilation is omitted.
- **Counterpart:** Serves as the direct suppression counterpart to `[ShowCode]`.
- **Targeting:** Can be applied directly at the `Class` level to blanket-hide code display across all member methods in that class.
