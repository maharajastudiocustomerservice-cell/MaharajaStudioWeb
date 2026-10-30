# [OnFieldBlur]

> Invokes a C# callback method when a serialized field or property loses UI focus (blurs) in the Inspector.

---

## 1. Overview & Value Proposition

**What it does:**
Runs a method as soon as you click away or finish editing a specific field in the Inspector.

**The Problem:**
In standard Unity, `OnValidate()` fires on every single keystroke. When typing a URL, math formula, or long dialogue line, firing validation on every letter keystroke causes console errors, frame hiccups, and premature checks while the developer is still typing.

**The Solution:**
Add `[OnFieldBlur]` next to any serialized field or method:
- **Fires Only When Finished:** Waits until the developer finishes typing and clicks or tabs away.
- **Batched Processing:** Ideal for compiling heavy math, parsing JSON, or validating web links only once after input is complete.
- **Clean Field Verification:** Verify capitalization, trim whitespace, or calculate hashes without interrupting typing.
- **UI Toolkit Native:** Integrates directly with UI Toolkit's native `BlurEvent` lifecycle.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerAccount : MonoBehaviour
{
    [OnFieldBlur(nameof(ValidatePlayerTag))]
    public string playerTag;

    private void ValidatePlayerTag()
    {
        playerTag = playerTag.Trim().ToUpperInvariant();
        Debug.Log($"Player tag standardized: {playerTag}");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property | AttributeTargets.Method` |
| **Supported Types** | Any serializable field type; target method must be parameterless |
| **Allow Multiple** | `true` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public OnFieldBlurAttribute(string methodNameOrFieldName)
```
- **`methodNameOrFieldName`**: Name of callback method (when placed on field) or target field (when placed on method).

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MethodName` | `string` | *(Constructor)* | Name of the method to call when focus is lost. |
| `TargetFieldName` | `string` | *(Constructor)* | Target field name to listen for blur events. |
| `Order` | `int` | `0` | Execution priority relative to other attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkServerConfig : MonoBehaviour
{
    [Header("Server Connection")]
    [OnFieldBlur(nameof(NormalizeIpAddress))]
    public string ipAddress = "127.0.0.1";

    public int port = 7777;

    [ReadOnly]
    public string connectionEndpoint;

    private void NormalizeIpAddress()
    {
        ipAddress = ipAddress.Trim();
        connectionEndpoint = $"{ipAddress}:{port}";
        Debug.Log($"[NetworkConfig] Updated endpoint on blur: {connectionEndpoint}");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Pairing with `[OnFieldFocus]`:** Pair together to manage enter/exit focus state transitions (e.g. show guide on focus, validate on blur).
- **Text & Input Fields:** Works with all standard Unity inputs and custom field drawers.
- **Layouts:** Fully functional inside `[BoxGroup]`, `[TabGroup]`, and vertical stacks.
