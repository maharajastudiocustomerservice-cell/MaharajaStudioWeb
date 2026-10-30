# [ComponentSmokeMist]

> Renders an animated rolling smoke and fog mist effect drifting with fluid turbulence across the component background.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentSmokeMist]` envelops the component inspector in a rolling blanket of atmospheric vapor and fog. Rendered via UI Toolkit vector painters in `ComponentSlot.ContentOverlay`, it simulates organic volumetric smoke puffs (`Density = 12`) drifting laterally (`DriftSpeed = 0.6f`) with curling aerodynamic turbulence (`Turbulence = 0.8f`). The mist puffs drift in soft slate, charcoal, or ghostly hues (`SmokeColor = "#64748B33"`), establishing a palpable sense of mystery, gloom, or industrial exhaust.

**The Problem:**
Haunted mansions, necromantic graveyards, stealth smoke canisters, industrial exhaust chimneys, and misty swamps feel clinical and plain in standard Unity inspectors. Developers miss the ominous tactile presence of creeping fog while authoring supernatural or atmospheric game systems.

**The Solution:**
Decorating fog, stealth, and supernatural components with `[ComponentSmokeMist]`:
- **Organic Fluid Turbulence:** Multi-scale noise creates rolling, tumbling smoke puffs with realistic billowing behavior.
- **Configurable Particle Density:** Scale density to simulate anything from a delicate morning mountain mist to thick industrial chimney smog.
- **Ghostly Color Customization:** Supports translucent hex strings with 8-character alpha for spectral green ectoplasm, toxic sulfur yellow, or shadowy slate mist.
- **Zero Input Disruption:** Runs in `ContentOverlay` with `PickingMode.Ignore`, preserving crisp interaction across all inspector controls.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentSmokeMist(smokeColor: "#64748B33", driftSpeed: 0.6f, turbulence: 0.8f)]
public class GraveyardFogVolume : MonoBehaviour
{
    public float fogDensity = 0.045f;
    public float visibilityDistanceMeters = 15f;
    public Color ambientScatteringColor = new Color(0.2f, 0.25f, 0.3f);
    public bool isHauntedAuraActive = true;
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
| **Component Slot** | `ContentOverlay` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentSmokeMistAttribute()
public ComponentSmokeMistAttribute(string smokeColor = "#64748B33", float driftSpeed = 0.6f, float turbulence = 0.8f)
```

- `smokeColor`: Hex color string with alpha channel defining smoke tint and density.
- `driftSpeed`: Horizontal movement velocity multiplier of the drifting mist cloud.
- `turbulence`: Aerodynamic curling and swirling intensity of the smoke puffs.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `SmokeColor` | `string` | `"#64748B33"` | Hex color string (with alpha) for the smoke puff clouds. |
| `DriftSpeed` | `float` | `0.6f` | Lateral drifting velocity multiplier of the fog volume. |
| `Turbulence` | `float` | `0.8f` | Swirling turbulence and eddy intensity for the cloud bodies. |
| `Density` | `int` | `12` | Number of animated smoke puff particles rendered across the card. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#475569", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#0F172A", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("NECROMANTIC CRYPT SHADOWS", Subtitle = "Catacomb Atmospheric Mist Generator", BackgroundColor = "#1E293B", TitleColor = "#E2E8F0")]
[ComponentSmokeMist(SmokeColor = "#94A3B840", DriftSpeed = 0.5f, Turbulence = 0.9f, Density = 16)]
public class CatacombMistGenerator : MonoBehaviour
{
    [Header("Ectoplasmic Fog Settings")]
    public float ectoplasmConcentrationPpm = 320f;
    public float chillTemperatureCelsius = -4.5f;

    [Header("Spook Telemetry")]
    public int wanderingSpecterCount = 4;
    public bool isUnholyConsecrationIntact = false;
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentBackground]`** | High | Deep midnight slate or obsidian card backdrops (`#0F172A`) make rolling mist clouds feel dense and ominous. |
| **`[ComponentHeader]`** | High | Fits cemetery, stealth, dungeon, and post-apocalyptic header themes. |
| **`[ComponentSound]`** | High | Pair with howling wind or distant thunder audio cues for full multi-sensory immersion. |
| **Inspector Controls** | High | `PickingMode.Ignore` guarantees completely unhindered mouse events on all sliders, foldouts, and input fields. |
