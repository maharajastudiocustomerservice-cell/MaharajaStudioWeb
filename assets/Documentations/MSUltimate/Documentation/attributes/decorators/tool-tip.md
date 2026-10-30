# [ToolTip]

> Displays an informative hover tooltip over the property label or button in the Inspector.

`Package: MSUltimate Core` `Targets: Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: Zero Runtime Cost (Editor Visual Only)`

---

## 1. Overview & Value Proposition

**What it does:**
Attaches helpful mouse hover description tooltips to fields, properties, and buttons so designers can read documentation on demand without cluttering the UI.

**The Problem:**
Unity's built-in `[Tooltip]` attribute works only on serialized fields and cannot be attached to method buttons or properties. It also suffers from inconsistent rendering bugs across custom drawer wrappers, and duplicating tooltips unconditionally across every list row creates immense visual fatigue.

**The Solution:**
Add `[ToolTip]` to any member:
- **Broad Target Support:** Works reliably on fields, properties, and method buttons.
- **Clean Inspector Interface:** Keeps the inspector layout clean by showing detailed instructions only when hovered.
- **Opt-In Collection Cascading:** Stay at the collection container level by default, or opt-in to per-element tooltips via `ApplyToElements = true`.
- **Zero Build Cost:** Pure editor-time metadata with zero performance overhead at runtime.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TurretAim : MonoBehaviour
{
    [ToolTip("Speed in degrees per second at which the turret barrel tracks targets.")]
    public float rotationSpeed = 90f;

    [ToolTip("Maximum distance in meters before target acquisition fails.")]
    public float targetLockRange = 120f;
}
```

---

## 3. Constructors & Parameters

```csharp
public ToolTipAttribute(string text)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `text` | `string` | *(Required)* | Tooltip text displayed on mouse hover. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Text` | `string` | *(Required)* | Hover tooltip text description string. |
| `ApplyToElements` | `bool` | `false` | When `true`, cascades hover tooltips to individual collection element rows. |
| `Order` | `int` | `1` | Early decorator pipeline processing order. |

---

## 5. Production-Grade Example

```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using Header = MaharajaStudio.MSUltimate.Runtime.HeaderAttribute;
using ToolTip = MaharajaStudio.MSUltimate.Runtime.ToolTipAttribute;

namespace MaharajaStudio.MSUltimate.Example
{
    public class ToolTipExample : ModularMonoBehaviour
    {
        [Title("Combat Defense Matrix", "Informative hover tooltips providing instant documentation for designers")]
        [InfoBox("Hover the mouse over any property label below to view contextual help and formula details without cluttering the UI.", InspectorMessageType.Info)]

        [Header("Vital Statistics")]
        [@ToolTip("Base vital hit points. When this drops to zero, the character enters an incapacitated state.")]
        [Range(100, 5000)]
        public int vitalHealthPoints = 1250;

        [@ToolTip("Flat damage reduction deducted directly from incoming physical and kinetic projectile strikes.")]
        [Range(0f, 150f)]
        public float armorRating = 45f;

        [@ToolTip("Percentage mitigation (0% - 75%) applied against fire, frost, and shock magic damage.")]
        [Range(0f, 75f)]
        public float elementalResistancePercent = 35f;

        [Title("Nested Class Showcase")]
        [@ToolTip("Demonstrates [ToolTip] applied inside child serializable shield models.")]
        public ShieldGeneratorSlot activeShield = new ShieldGeneratorSlot
        {
            shieldModel = "Aegis Kinetic Barrier Mk3",
            barrierCapacity = 450f,
            rechargeRate = 25f
        };

        [Header("Defense Perk Tags Collection")]
        [@ToolTip("Active defense perk modifier keyword slot. Cascades to elements via ApplyToElements = true.", ApplyToElements = true)]
        public string[] defensePerkTags = new string[]
        {
            "PERK_FORTIFIED_STANCE",
            "PERK_DEFLECTIVE_PLATING",
            "PERK_RESILIENT_WILL"
        };

        [Serializable]
        public class ShieldGeneratorSlot
        {
            [@ToolTip("Proprietary manufacturer model name for this energy shield.")]
            public string shieldModel;

            [@ToolTip("Maximum absorption energy pool before barrier fails.")]
            public float barrierCapacity;

            [@ToolTip("Shield points recovered per second after a 3-second delay.")]
            public float rechargeRate;
        }

        [Title("Interactive Simulation")]
        [Button("Print Combat Defense Readout", BackgroundColor = "#10B981", TextColor = "#FFFFFF")]
        private void PrintReadout()
        {
            Debug.Log($"<color=#10B981>[ToolTipExample]</color> <b>Health:</b> {vitalHealthPoints} | <b>Armor:</b> {armorRating} | <b>Resist:</b> {elementalResistancePercent}% | <b>Shield:</b> {activeShield.shieldModel} ({activeShield.barrierCapacity} HP)");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[LabelText]` | Supported | Tooltip attaches cleanly to the customized label text. |
| `[BoxGroup]` | Supported | Functions normally inside group layouts. |
| `[Button]` | Supported | Provides hover documentation for custom inspector buttons. |
| `[ShowIf]` / `[HideIf]` | Supported | Only active when the parent property is displayed. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Header Tooltip** | Supported | Default mode (`ApplyToElements = false`). Attaches tooltip solely to the root foldout label to describe overall collection purpose. |
| **Element-Level Cascading** | Supported (Opt-In) | Setting `ApplyToElements = true` implements `ICollectionElementAttribute` and attaches tooltips to every child element row. |
| **Nested Serializable Classes** | Supported | Fields inside child classes declared within collections support individual, distinct tooltips. |
| **Custom Serializers** | Supported | Compatible with `AdvancedList<T>`, `SerializableDictionary<K, V>`, `SerializableTuple<...>`, and `SerializableNullable<T>`. |
