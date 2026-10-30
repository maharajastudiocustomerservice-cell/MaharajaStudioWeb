# [ValidateUnless]

> Conditionally bypasses sibling validation attributes on the same field whenever a specified predicate condition evaluates to true.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateUnless]` is the inverse counterpart of `[ValidateIf]`. It functions as an execution bypass gate for sibling validation attributes declared on the same field (such as `[ValidateNotNull]`, `[ValidateRange]`, or `[ValidateComponent]`). It monitors a condition member (`ConditionMember`: a boolean field, enum value, or property). When that condition evaluates to `true` (or matches `ExpectedValue`), the sibling validation attributes on the field are skipped. Conversely, when the condition is `false` (or does not match), the validation rules are actively enforced.

**The Problem:**
Game configurations frequently utilize default fallback modes, debug bypass toggles, or automated procedural overrides:
- An audio clip or material reference is required unless `useGlobalDefaults` is toggled on.
- A network matchmaking token is mandatory unless `offlineMode == true`.
- An AI behavior tree asset must be assigned unless `useProceduralDirector == true`.
Without `[ValidateUnless]`, developers must write inverted boolean flags (`isNotOfflineMode`, `doNotUseGlobalDefaults`) or invent convoluted condition wrappers just to avoid false positive validation alerts on optional fields.

**The Solution:**
Decorating fields with `[ValidateUnless]`:
- **Intuitive Negative Conditionals:** Eliminates confusing double-negative boolean flags by expressing "validate unless X is true".
- **Conditional Bypass Gates:** Skips validation when global defaults, mock systems, or procedural alternatives are active.
- **Enum and Primitive Matching:** Supports exact value comparisons (`expectedValue = GameMode.Creative`).
- **Clean Inspector Experience:** Keeps the Inspector free of false positive alerts when features are intentionally bypassed.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class AudioSourceConfig : MonoBehaviour
{
    public bool useGlobalMasterAudio = true;

    [ValidateUnless("useGlobalMasterAudio", true)]
    [ValidateNotNull("Custom sound clip must be provided when not using global master audio.")]
    public AudioClip customAudioClip;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ValidationModule Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Window Surface** | Unity Inspector & Validation Engine Window |
| **Validation Interface** | `IValidationAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateUnlessAttribute(string conditionMember, object expectedValue = null, string message = null)
```

- **`conditionMember`** (`string`): Name of the sibling field, property, or method returning a condition value.
- **`expectedValue`** (`object`, optional): The condition value that triggers the bypass. When omitted or `null`, evaluates boolean truthiness.
- **`message`** (`string`, optional): Optional guidance or informational note.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ConditionMember` | `string` | Assigned in constructor | Name of the condition member inspected. |
| `ExpectedValue` | `object` | `null` | Value that triggers bypass of sibling validation rules. |
| `Invert` | `bool` | `true` | Inversion flag (automatically locked to `true` in `ValidateUnlessAttribute`). |
| `Message` | `string` | `null` | Informational message displayed in the validation banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Info` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.Network
{
    public enum ConnectionMode { DedicatedServer, PeerToPeer, OfflineSandbox }

    public class NetworkEndpointSettings : ModularMonoBehaviour
    {
        [Header("Deployment Mode")]
        public ConnectionMode connectionMode = ConnectionMode.DedicatedServer;
        public bool bypassCertificateValidation = false;

        [Header("Server Host Address")]
        [ValidateUnless("connectionMode", ConnectionMode.OfflineSandbox)]
        [ValidateNotNull("Host URL is required for live network multiplayer.")]
        [ValidateStringLength(8, 64, "Host domain must be between 8 and 64 characters.")]
        public string serverEndpoint = "https://game.projectzero.io";

        [Header("Security Certificate")]
        [ValidateUnless("bypassCertificateValidation", true)]
        [ValidateNotNull("SSL Certificate asset is mandatory in production environments.")]
        public TextAsset sslCertificate;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateNotNull]` / `[Required]`**| High | Guard required assets while cleanly skipping validation when fallbacks are used. |
| **`[ValidateRange]`** | High | Bypass range validation when a property is procedurally driven or set to auto-scale. |
| **`[ValidateIf]`** | High | Use `[ValidateIf]` for positive execution gates and `[ValidateUnless]` for bypass gates. |
| **Validation Engine** | Native | Audited automatically during scene-wide and prefab validation batch runs. |
