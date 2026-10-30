# [MSSpace]

> Inserts vertical blank spacing pixels above fields, properties, or method buttons to separate sections cleanly.

---

## 1. Overview & Value Proposition

**What it does:**
Adds clean vertical breathing room (such as `10px`, `20px`, or `35px`) above an inspector field or button without needing dummy script variables.

**The Problem:**
Unity's standard `[Space]` attribute is notoriously inconsistent: on methods or custom property drawers, it is frequently ignored, collapses unexpectedly, or causes layout jitter when mixed with UI Toolkit elements.

**The Solution:**
Add `[MSSpace]` above any field, property, or method:
- **Universal Target Support:** Reliable vertical spacing above fields, properties, AND method buttons.
- **Pixel-Accurate Heights:** Pass custom height values (e.g. `[MSSpace(24)]`) for precise typographic rhythm.
- **Stackable:** Place multiple spaces or combine with headers without layout bugs.
- **Native UI Toolkit Flex:** Integrates cleanly with modern UI Toolkit flex layouts without causing layout overlapping.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SpacingDemo : MonoBehaviour
{
    public float movementSpeed = 6f;

    [MSSpace(20)]
    public float jumpForce = 12f;

    [MSSpace(30)]
    [Button("Reset Movement State")]
    public void ResetState() { }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any serializable field, property, or method |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public MSSpaceAttribute(float height = 15f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `height` | `float` | `15f` | Height of the blank vertical space in pixels. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Height` | `float` | `15f` | Vertical pixel height of the spacing divider. |
| `Order` | `int` | `0` | Decorator pipeline processing order. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameSettingsPanel : MonoBehaviour
{
    [Header("Primary Controls")]
    public float masterVolume = 1f;
    public float sfxVolume = 0.8f;

    [MSSpace(25)]
    [Header("Gameplay Toggles")]
    public bool enableVibration = true;
    public bool screenShake = true;

    [MSSpace(35)]
    [Button("Revert To Factory Settings", ButtonHeight = 32)]
    public void RevertSettings()
    {
        Debug.Log("Settings reverted!");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Fully supported directly above method buttons. |
| `[Header]` | Supported | Insert space above headers to clearly detach distinct functional areas. |
| `[BoxGroup]` | Supported | Functions correctly both inside and outside layout groups. |
