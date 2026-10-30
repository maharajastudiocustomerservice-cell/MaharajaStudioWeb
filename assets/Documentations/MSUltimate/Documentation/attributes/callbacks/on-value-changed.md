# [OnValueChanged]

> Automatically executes a C# callback method whenever a serialized field's value is modified in the Inspector.

---

## 1. Overview & Value Proposition

**What it does:**
Runs a method immediately whenever you change a field or slider in the Inspector.

**The Problem:**
In standard Unity, reacting to field edits requires using `OnValidate()`. But `OnValidate()` executes globally for the entire component on every single domain reload, scene open, and property modification, making it hard to know *which* specific field changed without tedious before-and-after cache checks.

**The Solution:**
Add `[OnValueChanged]` directly onto the target field:
- **Field-Specific Triggering:** Executes strictly when *this specific field* is modified by the user.
- **Optional Parameter Passing:** Your callback method can optionally accept the new value as an argument.
- **Immediate Visual Feedback:** Update material colors, regenerate procedural meshes, or update child transforms in real time.
- **Clean Configuration Flags:** Configure whether to fire on load (`InvokeOnLoad`) or on inspector rebuild (`InvokeOnRebuild`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LightAdjuster : MonoBehaviour
{
    [OnValueChanged(nameof(UpdateLightColor))]
    public Color lightColor = Color.white;

    public Light targetLight;

    private void UpdateLightColor()
    {
        if (targetLight != null)
            targetLight.color = lightColor;
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field type; method can be parameterless or accept matching value |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public OnValueChangedAttribute(string methodName)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `methodName` | `string` | *(Required)* | The name of the callback method to invoke when the field value changes. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MethodName` | `string` | *(Required)* | Name of the callback method to execute. |
| `InvokeOnLoad` | `bool` | `false` | When true, executes the callback when the component or ScriptableObject is loaded. |
| `InvokeOnRebuild` | `bool` | `false` | When true, executes the callback whenever the Inspector UI hierarchy rebuilds. |
| `Order` | `int` | `0` | Execution priority relative to other value-change handlers. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[ExecuteAlways]
public class CharacterAuraConfig : MonoBehaviour
{
    [Header("Aura Configuration")]
    [OnValueChanged(nameof(OnIntensityChanged))]
    [Range(0f, 10f)]
    public float auraIntensity = 2.5f;

    [OnValueChanged(nameof(OnColorChanged))]
    public Color auraColor = Color.cyan;

    [SerializeField]
    private ParticleSystem auraParticles;

    private void OnIntensityChanged(float newIntensity)
    {
        if (auraParticles != null)
        {
            var main = auraParticles.main;
            main.startSpeed = newIntensity * 1.5f;
            Debug.Log($"[Aura] Intensity adjusted to {newIntensity}");
        }
    }

    private void OnColorChanged()
    {
        if (auraParticles != null)
        {
            var main = auraParticles.main;
            main.startColor = auraColor;
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Range]`, `[MinMaxSlider]` | Supported | Fires smoothly as the user drags sliders in real time. |
| `[ColorPalette]`, `[ColorWheel]` | Supported | Triggers immediately upon selecting color swatches. |
| `[OnUndoRedo]` | Supported | Recommended to stack together to handle both user edits and `Ctrl+Z` operations. |
| `[BoxGroup]` | Supported | Fully functional inside layout containers. |
