# [ComponentPresetManager]

> Injects a preset management toolbar into the component header to save, load, and snapshot field configurations as JSON assets.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentPresetManager]` equips any component inspector with a built-in preset storage system. Positioned in `ComponentSlot.BeforeContent`, it renders a preset selection toolbar with interactive controls to snapshot current serialized field states to disk (`AllowSaveLoad = true`), select from saved preset files in a designated directory (`PresetFolder = "Presets"`), and quickly restore configurations without re-entering values manually.

**The Problem:**
Balancing character stats, camera shake profiles, physics tunings, weapon spreads, and AI behaviors requires constantly testing multiple parameter sets. Developers frequently lose tuned values when switching game scenes, or must manually create cumbersome ScriptableObject wrappers just to save a few variable configurations.

**The Solution:**
Equipping tunable components with `[ComponentPresetManager]`:
- **One-Click State Snapshotting:** Save the current component configuration into a clean JSON file stored inside your project assets.
- **Instant Preset Swapping:** Switch between presets via a header dropdown to instantly see how parameter variations affect gameplay.
- **Configurable Storage Directories:** Group presets logically by subfolder (e.g. `"Presets/Weapons"`, `"Presets/Cameras"`).
- **Zero Runtime Dependencies:** Operates seamlessly during editor time and serializes standard Unity fields without modifying your runtime architecture.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentPresetManager("Presets/Vehicles", allowSaveLoad: true)]
public class SportsCarTuningProfile : MonoBehaviour
{
    public float horsepower = 450f;
    public float steeringSensitivity = 1.35f;
    public float suspensionStiffness = 3500f;
    public float brakeBiasFrontPercent = 0.62f;
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
| **Component Slot** | `BeforeContent` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentPresetManagerAttribute(string presetFolder = "Presets", bool allowSaveLoad = true)
```

- `presetFolder`: Relative project path where JSON preset assets for this component will be stored.
- `allowSaveLoad`: Flag enabling or disabling the save and load interface buttons in the toolbar.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PresetFolder` | `string` | `"Presets"` | Target project subfolder path where preset files are located and created. |
| `AllowSaveLoad` | `bool` | `true` | When true, displays interactive Save and Load buttons alongside the preset dropdown. |
| `Label` | `string` | `"Preset"` | Display prefix label shown on the preset toolbar header. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#059669", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#062016", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("ORBITAL CAMERA RIG", Subtitle = "Cinematic & Gameplay Tracking Profile", BackgroundColor = "#0B3827", TitleColor = "#A7F3D0")]
[ComponentPresetManager("Presets/CinematicCameras", AllowSaveLoad = true, Label = "Camera Preset")]
public class OrbitalCameraRigController : MonoBehaviour
{
    [Header("Field of View & Distance")]
    public float fieldOfViewDegrees = 65f;
    public float targetDistanceMeters = 8.5f;
    public Vector3 cameraOffset = new Vector3(0f, 2.2f, -5f);

    [Header("Damping & Inertia")]
    public float positionDampingLag = 0.15f;
    public float rotationSlerpSpeed = 12f;
    public bool isCollisionAvoidanceActive = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Places the preset selection bar directly underneath the primary title banner. |
| **`[ComponentHeaderButton]`** | High | Works alongside custom header buttons without layout overlaps. |
| **Undo/Redo System** | High | Loading presets registers with Unity's Undo stack so changes can be reverted instantly with `Ctrl+Z`. |
| **Inspector Controls** | High | Automatically repaints all serialized property elements when a new preset is selected. |
