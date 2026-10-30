# [ShowInInspector]

> Surfaces non-serialized C# fields, private variables, and auto-properties directly in the Unity Inspector with live polling and read-only options.

---

## 1. Overview & Value Proposition

**What it does:**
Makes private variables and C# `{ get; set; }` properties visible in the Inspector without needing `[SerializeField]`.

**The Problem:**
In standard Unity, you can only see fields in the Inspector if they are `public` or marked with `[SerializeField]`. That means calculated properties (like `HealthPercentage => currentHp / maxHp`), private runtime counters, and dictionary counts are completely invisible while testing.

**The Solution:**
Add `[ShowInInspector]` above any private variable or C# property:
- **Inspect Live C# Properties:** View computed getter values in real time as your game runs.
- **Zero Serialization Overhead:** Keeps your code architecture clean without forcing you to make variables public or serialize data you don't want saved.
- **Live Auto-Refresh:** Updates periodically (configurable `UpdateInterval`) so you can monitor values during gameplay without writing GUI code.
- **Optional Read-Only Mode:** Mark properties as read-only to prevent accidental edits while testing.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerHealth : MonoBehaviour
{
    private float currentHealth = 100f;
    private float maxHealth = 100f;

    [ShowInInspector]
    public float HealthPercentage => (currentHealth / maxHealth) * 100f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | Any inspectable C# type, getters, private members |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public ShowInInspectorAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IsReadOnly` | `bool` | `false` | When `true`, disables editing and displays member as read-only telemetry. |
| `Label` | `string` | `null` | Overrides the field label displayed in the inspector. |
| `UpdateInterval` | `int` | `200` | Polling frequency in milliseconds during active editor updates. |
| `LabelColor` | `string` | `null` | Custom hex color string for the property label. |
| `LabelWidth` | `float` | `0f` | Fixed width for the label in pixels (`0` for auto). |
| `LabelFontSize` | `int` | `0` | Font size for the label (`0` for default). |
| `ValueColor` | `string` | `null` | Custom hex color for the displayed value text. |
| `BackgroundColor` | `string` | `null` | Card container background tint for highlighted telemetry. |
| `BorderWidth` | `float` | `0f` | Width of the border around the field in pixels. |
| `BorderColor` | `string` | `null` | Hex color for the border around the field. |
| `BorderRadius` | `float` | `0f` | Corner rounding radius if border/background styling is enabled. |
| `MarginTop` | `float` | `0f` | Spacing above the field in pixels. |
| `MarginBottom` | `float` | `0f` | Spacing below the field in pixels. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class VehiclePhysicsController : MonoBehaviour
{
    private Rigidbody rb;

    private void Awake() => rb = GetComponent<Rigidbody>();

    [BoxGroup("Live Telemetry", Box = true)]
    [ShowInInspector(
        Label = "Current Speed (km/h)",
        IsReadOnly = true,
        ValueColor = "#00FFCC",
        UpdateInterval = 100
    )]
    public float SpeedKmh => rb != null ? rb.linearVelocity.magnitude * 3.6f : 0f;

    [BoxGroup("Live Telemetry")]
    [ShowInInspector(IsReadOnly = true)]
    public bool IsGrounded { get; private set; }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Pairing with Layouts:** Works inside `[BoxGroup]`, `[TabGroup]`, and `[VerticalGroup]`.
- **Conditionals:** Compatible with `[ShowIf]` and `[HideIf]`.
- **Zero Serialization:** Values marked with `[ShowInInspector]` do NOT dirty the scene or write to `.unity` YAML files, preventing accidental Git merge conflicts during debug sessions.
