# [HoldToConfirmButton]

> Converts an inspector action button or method into a press-and-hold confirmation control with radial/linear progress fill and warning rumbles.

`Package: MSUltimate-AnimatedAttributes` `Targets: Method | Field | Property` `AllowMultiple: False` `Inherited: True` `Performance: High (UI Toolkit Pointer Events & Transitions)`

---

## 1. Overview & Value Proposition

**What it does:**
`[HoldToConfirmButton]` safeguards dangerous or irreversible operations by requiring the user to click and continuously hold down the mouse button for a designated timeframe (`HoldDurationSeconds`). During the hold gesture, an animated progress fill advances (`FillColor`). If released before reaching 100%, the action aborts and the progress quickly rewinds. Approaching completion triggers an escalating visual rumble pulse (`RumbleOnApproach`).

**The Problem:**
Destructive buttons in custom inspectors—such as "Delete All Save Data", "Reset Player Profile", "Reformat Level Geometry", or "Purge Texture Atlas"—can easily be triggered by accidental misclicks. Confirmation popup dialogs (`EditorUtility.DisplayDialog`) disrupt developer flow and quickly become reflexively dismissed.

**The Solution:**
Decorating critical action methods or fields with `[HoldToConfirmButton]`:
- **Physical Hold Confirmation:** Requires conscious deliberate action by holding the mouse down for a set interval (e.g. 1.5 seconds).
- **Smooth Dynamic Progress Fill:** Renders an animated progress fill (`FillColor`) that winds down instantly if released early.
- **Collection Row Cascading:** Implements `ICollectionElementAttribute` to safeguard destructive item deletion or reset actions across array and list rows.
- **Tension-Building Rumble FX:** Shakes and pulses gently as the hold approaches 100% completion (`RumbleOnApproach = true`).
- **Flexible Button Typography:** Customize button label text (`ButtonText`) to convey action purpose directly.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.AnimatedAttributes;

public class GameDataMaintenance : MonoBehaviour
{
    [HoldToConfirmButton(holdSeconds: 2.0f, buttonText: "Purge All Cloud Saves")]
    public void DeleteAllCloudSaves()
    {
        Debug.Log("Cloud saves permanently removed!");
    }
}
```

---

## 3. Constructors & Parameters

```csharp
public HoldToConfirmButtonAttribute(float holdSeconds = 1.5f, string buttonText = "Hold to Confirm")
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `holdSeconds` | `float` | `1.5f` | Required continuous press duration in seconds to trigger the action. |
| `buttonText` | `string` | `"Hold to Confirm"` | Label string rendered on the button. |

---

## 4. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HoldDurationSeconds` | `float` | `1.5f` | Required press duration in seconds to complete confirmation. |
| `ButtonText` | `string` | `"Hold to Confirm"` | Label text displayed on the button surface. |
| `FillColor` | `string` | `"#EF4444"` | Hex color string for the active progress fill. |
| `RumbleOnApproach` | `bool` | `true` | Whether to shake or pulse as hold progress nears 100%. |
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
    public class HoldToConfirmButtonExample : ModularMonoBehaviour
    {
        [Title("HoldToConfirmButton Attribute Showcase", "Continuous press duration gate with progress fill")]
        [InfoBox("HoldToConfirmButton safeguards catastrophic actions by demanding a sustained mouse hold.", InspectorMessageType.Info)]

        [BoxGroup("1. Critical Safeguarded Actions")]
        [HoldToConfirmButton(holdSeconds: 2.0f, buttonText: "Hold to Format Cloud Save", FillColor = "#EF4444", RumbleOnApproach = true)]
        public void FormatCloudSave()
        {
            saveProfileIntegrity = 0;
            Debug.LogWarning("<color=#EF4444>[HoldToConfirmButton]</color> CONFIRMED: Cloud save formatted to factory state!");
        }

        [BoxGroup("2. Inside Class Demonstration")]
        public TerminalSecuritySlot commandTerminal = new TerminalSecuritySlot();

        [BoxGroup("3. Security Station Manifest")]
        [InfoBox("HoldToConfirmButton cascades to collection slots, requiring hold-press confirmation before toggling guarded switches.", InspectorMessageType.Info)]
        [HoldToConfirmButton(holdSeconds: 1.0f, buttonText: "Hold to Arm Silo", FillColor = "#EF4444")]
        public bool[] siloArmingSwitches = new bool[] { false, false, true };

        public List<TerminalSecuritySlot> activeSilos = new List<TerminalSecuritySlot>
        {
            new TerminalSecuritySlot { terminalId = "ALPHA-SILO-01", clearanceLevel = 4, isArmingKeyInserted = false },
            new TerminalSecuritySlot { terminalId = "BRAVO-SILO-02", clearanceLevel = 5, isArmingKeyInserted = true }
        };

        [Serializable]
        public class TerminalSecuritySlot
        {
            public string terminalId = "OMEGA-SILO-09";
            public int clearanceLevel = 5;
            public bool isArmingKeyInserted = true;
        }

        [BoxGroup("4. Interactive System Controls")]
        public int saveProfileIntegrity = 100;

        [Button("Simulate Save Data Recovery", BackgroundColor = "#10B981", TextColor = "#022C22")]
        public void RestoreSaveData()
        {
            saveProfileIntegrity = 100;
            Debug.Log("<color=#10B981>[HoldToConfirmButton]</color> Save profile integrity restored to 100%.");
        }
    }
}
```

---

## 6. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Integrates cleanly inside group card layouts and headers. |
| `[ShowIf]` / `[HideIf]` | Supported | Only accessible when conditional prerequisites are fulfilled. |
| `[DisableIf]` | Supported | Visual button and pointer callbacks are cleanly disabled when inactive. |
| `[ValidateNotNull]` | Supported | Functions in tandem with object validation on the same component. |

---

## 7. Collection Cascading & Custom Serializer Discipline

| Context / Architecture | Support | Behavior & Guidelines |
| :--- | :---: | :--- |
| **Collection Element Cascading** | Supported (`ICollectionElementAttribute`) | Cascades down to individual collection rows (`bool[]`, `List<T>`) to require hold confirmation before mutating element data. |
| **Target Element Roles** | Supported | `CollectionElementRole.Element`, `Value`, `NullableValue`, `TupleItem`. |
| **Direct Boolean Collections** | Supported | Decorating `bool[]` or `List<bool>` binds hold confirmation before toggling each boolean slot. |
| **Nested Serializable Classes** | Supported | Fully functions inside child classes and structs declared within lists. |
| **Custom Serializers** | Supported | Compatible with `AdvancedList<T>`, `SerializableDictionary<K, V>`, and `SerializableTuple<...>`. |
