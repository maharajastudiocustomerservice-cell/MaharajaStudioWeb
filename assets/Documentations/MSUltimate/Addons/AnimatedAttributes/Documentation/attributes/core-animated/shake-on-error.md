# [ShakeOnError]

> Shakes an inspector field horizontally and flashes an error tint whenever validation fails or required values are missing.

---

## 1. Overview & Value Proposition

**What it does:**
`[ShakeOnError]` provides tactile, physics-inspired error feedback directly inside the Unity Inspector. When an input fails validation—either because an object/string is left empty or a custom validation callback evaluates to false—the field executes a rapid horizontal camera-shake vibration accompanied by a red error flash (`ErrorColor`).

**The Problem:**
Static validation messages or tiny warning icons can easily be ignored in busy inspectors, causing developers to run play mode with missing assets or invalid numeric ranges and trigger avoidable crashes.

**The Solution:**
Applying `[ShakeOnError]` to input fields:
- **Instant Visceral Feedback:** The horizontal rumble directly tells the user that their entered value is invalid.
- **Custom Validation Logic:** Link a custom C# boolean method via `ValidationMethod` or rely on built-in non-empty checks via `ValidateNotEmpty`.
- **Configurable Vibration Dynamics:** Fine-tune `ShakeIntensity` (pixels), `ShakeSpeed` (Hz), and `Duration` (ms) to match your UI feel.
- **Visual Alert Tinting:** Emphasizes invalid state with an accent background flash (`ErrorColor`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class ProfileSetup : MonoBehaviour
{
    [ShakeOnError(ValidateNotEmpty = true, ShakeIntensity = 6f)]
    public string playerName;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-AnimatedAttributes Addon |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or collection element (`T[]`, `List<T>`, etc.) |
| **Interface Implemented** | `ICollectionElementAttribute` (Cascades directly to collection element rows) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ShakeOnErrorAttribute()
```

*Initializes error vibration with 5px amplitude, 25Hz oscillation, and 400ms duration. Set validation rules and parameters via object initializers.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ValidationMethod` | `string` | `""` | Name of an instance method returning a `bool` (`false` triggers error shake). |
| `ValidateNotEmpty` | `bool` | `true` | When true, automatically shakes if an object reference is null or string is empty. |
| `ShakeIntensity` | `float` | `5f` | Maximum horizontal displacement offset in pixels during the shake. |
| `ShakeSpeed` | `float` | `25f` | Oscillation frequency of the horizontal vibration in cycles per second. |
| `Duration` | `float` | `400f` | Total duration of the shake vibration in milliseconds before settling. |
| `ErrorColor` | `string` | `"#ff444433"` | Hex color string for the background error flash tint. |
| `Order` | `int` | `0` | Execution sorting priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class NetworkRoomConfig : MonoBehaviour
{
    [Header("Mandatory Credentials")]
    [ShakeOnError(ValidateNotEmpty = true, ShakeIntensity = 8f, Duration = 500f)]
    public string serverEndpoint = "https://api.game.com";

    [Header("Port Validation")]
    [ShakeOnError(
        ValidationMethod = nameof(ValidatePort), 
        ShakeIntensity = 4f, 
        ErrorColor = "#e74c3c44"
    )]
    public int networkPort = 7777;

    private bool ValidatePort()
    {
        return networkPort >= 1024 && networkPort <= 65535;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :--- | :--- |
| `[Validate]` | Supported | Pairs seamlessly with validation attributes; adds dynamic physical feedback to warnings. |
| `[BoxGroup]` | Supported | The horizontal shake applies locally to the field without displacing parent containers. |
| `[ShowIf]` | Supported | Only evaluates and triggers shake events when the field is visible. |
| `Collections (Arrays & Lists)` | **Supported (`ICollectionElementAttribute`)** | Directly decorates arrays or lists (`string[]`, `int[]`, `GameObject[]`, `List<T>`) to trigger horizontal error shakes specifically on invalid/empty rows. |
| `SerializableDictionary<K, V>` | **Supported (`ICollectionElementAttribute`)** | Evaluates and vibrates individual invalid dictionary values. |

