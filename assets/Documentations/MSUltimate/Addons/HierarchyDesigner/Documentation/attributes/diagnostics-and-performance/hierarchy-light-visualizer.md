# [HierarchyLightVisualizer]

> Displays a light color preview swatch and intensity badge directly on the hierarchy row for Light components.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyLightVisualizer]` embeds real-time lighting telemetry directly onto the hierarchy row for GameObjects equipped with a Unity `Light` component. Driven by `HierarchyLightVisualizerRenderer`, it renders a live solid color swatch representing the exact color of the light (`ShowColorSwatch = true`) and a miniature numerical intensity badge (e.g., `"1.5lx"`, `ShowIntensity = true`).

**The Problem:**
Lighting artists and environment designers frequently deal with dozens of point lights, spotlights, and area fills. Checking light colors or comparing intensities requires selecting each light in the hierarchy, inspecting its color picker and intensity values in the Inspector, and repeating the process, making lighting balance checks slow and disjointed.

**The Solution:**
Decorating light controllers or entities with `[HierarchyLightVisualizer]`:
- **Live Color Swatch Preview:** View the exact emitted light color right in the hierarchy row.
- **Instant Intensity Telemetry:** Compare light brightness levels across scene fixtures at a glance.
- **Clean Background Capsule:** Renders inside a sleek dark container capsule (`#1F242E`) with rounded corners.
- **Automatic Light Binding:** Automatically pulls color and intensity from `go.GetComponent<Light>()`; gracefully hides if no Light is attached.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[RequireComponent(typeof(Light))]
[HierarchyLightVisualizer]
public class StreetLampFixture : MonoBehaviour
{
    public float flickerSpeed = 1.2f;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyLightVisualizerRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyLightVisualizerAttribute()
```

- Standard parameterless constructor. Customizations are configured via object initializer properties.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowIntensity` | `bool` | `true` | Whether to display the numerical light intensity badge (e.g. `2.5lx`). |
| `ShowColorSwatch` | `bool` | `true` | Whether to display a preview swatch of the light's current color. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether the lighting visualizer remains visible and updates during Play Mode. |
| `Order` | `int` | `0` | Drawing order priority relative to other hierarchy row items. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[RequireComponent(typeof(Light))]
[HierarchyLightVisualizer(ShowIntensity = true, ShowColorSwatch = true, XOffset = 6f)]
public class DynamicCampfireLight : MonoBehaviour
{
    private Light _light;

    [Header("Flicker Configuration")]
    public float baseIntensity = 3.0f;
    public float flickerRange = 0.8f;

    private void Awake()
    {
        _light = GetComponent<Light>();
    }

    private void Update()
    {
        if (_light != null)
        {
            _light.intensity = baseIntensity + Mathf.Sin(Time.time * 8f) * flickerRange;
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`Light` Component** | Required | Queries `go.GetComponent<Light>()`; gracefully hides if no `Light` component is present. |
| **`[HierarchyToggle]`** | High | Combine with boolean toggles to enable or disable shadow casting or volumetric modes. |
| **`[HierarchyActiveButton]`** | High | Toggle the light GameObject on/off with single-click power buttons while watching the color swatch. |
| **Play Mode Lighting** | High | Reflects real-time light mutations (e.g. animated fire flicker, alarm strobes) live in the hierarchy row. |
