# [TargetLockOnReticle]

> Surrounds target coordinates, references, or combat targets with rotating sci-fi tracking brackets and a center crosshair dot.

`Package: MSUltimate-AnimatedAttributes` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (GPU Painter2D + MeshGenerationContext)`

---

## 1. Overview & Value Proposition

**What it does:**
`[TargetLockOnReticle]` equips inspector fields with an active targeting system. It embeds a rotating reticle instrument (`ReticleSize`, defaulting to 28px) to the left of the property field. Using UI Toolkit's 2D vector painter, it draws 4 rotating corner arc brackets at 90-degree intervals (`painter.Arc`) and a stationary center targeting dot (`painter.Arc(center, 2f, 0, 360)`) in a high-visibility tactical hue (`ReticleColor`, defaulting to `#EF4444` red). The brackets spin continuously according to `SpinSpeed` (revolutions per second).

**The Problem:**
Selecting combat targets, missile lock-on coordinates, homing beacon waypoints, or sniper aim points in the Unity Inspector feels passive when displayed as ordinary `Transform` references or raw `Vector3` coordinate fields.

**The Solution:**
Decorating targeting parameters with `[TargetLockOnReticle]`:
- **Rotating Tactical Brackets:** 4-corner arc brackets continuously spin around the target center, delivering immediate visual lock-on confirmation.
- **Center Targeting Crosshair Dot:** Fixed 2px center point anchors the reticle to the target origin.
- **Collection Row Cascading:** Implements `ICollectionElementAttribute` to surround each waypoint or missile target in arrays and lists with its own spinning bracket reticle.
- **Configurable Size & Speed:** Adjust outer diameter (`ReticleSize`) and rotation rate (`SpinSpeed`) from deliberate tracking sweeps to rapid lock-on alerts.
- **Clean Inline Layout:** Positioned seamlessly alongside the serialized input field without distorting Inspector indentation.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class MissileGuidance : MonoBehaviour
{
    [TargetLockOnReticle(reticleColor: "#EF4444", spinSpeed: 1.5f)]
    public Transform activeCombatTarget;
}
```

---

## 3. Constructors & Parameters

```csharp
public TargetLockOnReticleAttribute(string reticleColor = "#EF4444", float spinSpeed = 1.0f)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `reticleColor` | `string` | `"#EF4444"` | Hex color string for the rotating targeting brackets and center dot. |
| `spinSpeed` | `float` | `1.0f` | Bracket rotation speed in revolutions per second. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ReticleColor` | `string` | `"#EF4444"` | Hex color string for the targeting reticle (defaults to Red). |
| `SpinSpeed` | `float` | `1.0f` | Rotational speed in revolutions per second. |
| `ReticleSize` | `float` | `28f` | Outer diameter dimensions in pixels of the reticle widget. |
| `Order` | `int` | `0` | Execution order relative to other modular inspector drawers. |

---

## 5. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

namespace MaharajaStudio.MSUltimate.AnimatedAttributes.Sample
{
    public class TargetLockOnReticleExample : ModularMonoBehaviour
    {
        [Title("TargetLockOnReticle Attribute Showcase", "Rotating targeting bracket reticles with HUD tracking graphics")]
        [InfoBox("TargetLockOnReticle surrounds inspector fields with animated rotating corner brackets, crosshairs, and tracking reticles.", InspectorMessageType.Info)]

        [BoxGroup("1. Standalone Target Brackets")]
        [TargetLockOnReticle(reticleColor: "#EF4444", spinSpeed: 1.0f, ReticleSize = 32f)]
        public string primaryTargetDesignation = "MIG-35-FLANKER-CONTACT";

        [TargetLockOnReticle(reticleColor: "#F59E0B", spinSpeed: 1.5f, ReticleSize = 28f)]
        public Vector3 orbitalStrikeTarget = new Vector3(840.5f, 0.0f, -1250.2f);

        [BoxGroup("2. Inside Class Demonstration")]
        public FireControlPod activePod = new FireControlPod();

        [BoxGroup("3. Active Target Tracking Queue Manifest")]
        [InfoBox("TargetLockOnReticle cascades to collections of coordinates and objects, surrounding each waypoint row with rotating brackets.", InspectorMessageType.Info)]
        [TargetLockOnReticle(reticleColor: "#EF4444", spinSpeed: 1.2f)]
        public Vector3[] tacticalWaypoints = new Vector3[]
        {
            new Vector3(100f, 0f, 50f),
            new Vector3(250f, 15f, -120f),
            new Vector3(-80f, 5f, 300f)
        };

        public List<FireControlPod> weaponsQueue = new List<FireControlPod>
        {
            new FireControlPod { pylonSerial = "VENTRAL-BAY-BAYONET-01" },
            new FireControlPod { pylonSerial = "WING-PYLON-RIGHT-02" }
        };

        [Serializable]
        public class FireControlPod
        {
            public string pylonSerial = "WING-PYLON-LEFT-01";

            [TargetLockOnReticle(reticleColor: "#10B981", spinSpeed: 1.2f)]
            public GameObject laserDesignatedTarget;
        }

        [BoxGroup("4. Fire Control HUD Controls")]
        [Button("Acquire Full Tone Lock (Tone Confirmed)", BackgroundColor = "#EF4444", TextColor = "#FEF2F2")]
        public void AcquireTargetLock()
        {
            Debug.LogWarning($"<color=#EF4444>[TargetLockOnReticle]</color> TARGET LOCK CONFIRMED on {primaryTargetDesignation}!");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Integrates neatly beside target fields inside weapon configuration panels. |
| `[WarningStrobe]` | Stacking | Combines spinning reticle brackets with emergency hazard warning stripes. |
| Object References (`Transform`, `GameObject`) | Supported | Perfect companion for combat targets, waypoints, and homing origins. |
| `[ShowIf]` / `[HideIf]` | Supported | Disables reticle animation when conditional visibility is false. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`Vector3[]`, `Transform[]`, `GameObject[]`, `List<T>`), embedding reticles beside each item. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Target Collections** | Supported | Renders interactive spinning reticle graphics beside every waypoint coordinate or target object in collections. |
| **Nested Serializable Classes** | Supported | Fully functions inside child classes and structs declared within lists. |
| **Custom Serializers** | Supported | Compatible with `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
