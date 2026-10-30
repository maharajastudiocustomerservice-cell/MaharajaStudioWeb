# [IconButton]

> Injects a compact, inline icon button directly beside a serialized field to trigger utility actions with confirmation dialogs and tooltip hints.

---

## 1. Overview & Value Proposition

**What it does:**
Places a compact, inline icon button right next to any field to trigger helper actions without taking up vertical space.

**The Problem:**
Standard buttons take up a full row in the Inspector. When an action is directly tied to a specific field (like "Ping Asset", "Reset to Default", or "Focus Camera on Target"), a full-width button wastes valuable screen space and clutters the UI.

**The Solution:**
Add `[IconButton]` next to any field:
- **Zero Vertical Waste:** Docks neatly at the end of the field's row, keeping your Inspector compact.
- **Unity Built-in Icons:** Supports any built-in Unity Editor icon name (e.g. `d_ViewToolOrbit`, `Refresh`, `d_Search Icon`).
- **Hover Tooltips:** Shows helpful tooltip hints when designers hover over the icon.
- **Safe Execution:** Optional confirmation prompt before triggering sensitive method calls.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TargetLocator : MonoBehaviour
{
    [IconButton("d_ViewToolOrbit", nameof(FocusTarget), tooltip: "Frame target in SceneView")]
    public Transform targetTransform;

    private void FocusTarget()
    {
        if (targetTransform != null)
            Debug.Log($"Focusing on {targetTransform.name}");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | Any serializable field, property, struct, or collection element |
| **Collection Cascading** | Supported (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>` via `ICollectionElementAttribute`) |
| **Allow Multiple** | `true` (Multiple icon buttons can be docked beside the same field or collection row) |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public IconButtonAttribute(string iconName, string methodName, string tooltip = "", float buttonSize = 20f, bool showAtRight = true)
public IconButtonAttribute(string iconName, string methodName, string tooltip, string buttonColor)
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IconName` | `string` | `null` | Unity built-in editor icon name (e.g. `"d_Refresh"`, `"d_Search"`). |
| `MethodName` | `string` | `null` | Name of the method invoked upon button click. |
| `Tooltip` | `string` | `""` | Tooltip hint displayed when mouse hovers over the button. |
| `ButtonSize` | `float` | `20f` | Square width and height of the button in pixels. |
| `ShowAtRight` | `bool` | `true` | When `true`, docks at the right edge; when `false`, docks at the left. |
| `ButtonColor` | `string` | `null` | Hex background tint color for the button. |
| `Confirm` | `bool` | `false` | When `true`, prompts user with an `EditorUtility.DisplayDialog` confirmation alert. |
| `ConfirmMessage`| `string` | `"Are you sure you want to perform this action?"`| Custom message body displayed in the confirmation dialog. |
| `Condition` | `string` | `null` | Name of boolean field/method controlling whether button is enabled. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

namespace MaharajaStudio.MSUltimate.Example
{
    [AddComponentMenu("Maharaja Studio/MSUltimate/Samples/Buttons/Icon Button Example")]
    public class IconButtonExample : ModularMonoBehaviour
    {
        // ─── 1. Standalone Fields ────────────────────────────────────────────────
        [BoxGroup("1. Standalone Action Controls", BackgroundColor = "#0F172A", BorderColor = "#334155", BorderRadius = 6, MarginBottom = 8)]
        [IconButton("d_Refresh", nameof(RandomizePosition), "Click to randomize spawn coordinates", ButtonColor = "#059669")]
        public Vector3 spawnPosition = new Vector3(0, 0, 0);

        [IconButton("d_TreeEditor.Trash", nameof(ResetAllData), "Reset all settings to default",
            ButtonColor = "#DC2626", Confirm = true, ConfirmMessage = "Reset player profile data to factory defaults?")]
        public string playerProfile = "ProGamer_Elite_2026";

        // ─── 2. Inside Custom Class Showcase ─────────────────────────────────────
        [BoxGroup("2. Inside Custom Class Showcase", BackgroundColor = "#0F172A", BorderColor = "#2563EB", BorderRadius = 6, MarginBottom = 8)]
        public PatrolWaypointNode activeWaypoint = new PatrolWaypointNode();

        [Serializable]
        public class PatrolWaypointNode
        {
            public string waypointName = "Alpha_Point";

            [IconButton("d_MoveTool", nameof(SnapToTerrain), "Snap waypoint to terrain surface height", ButtonColor = "#3B82F6")]
            public Vector3 worldPosition = new Vector3(0, 0, 0);

            public void SnapToTerrain()
            {
                worldPosition.y = 0f;
            }
        }

        // ─── 3. Direct Collections Cascading Showcase ────────────────────────────
        [BoxGroup("3. Direct Collections Cascading", BackgroundColor = "#0F172A", BorderColor = "#10B981", BorderRadius = 6, MarginBottom = 8)]
        [InfoBox("[IconButton] implements ICollectionElementAttribute to automatically add compact icon buttons to individual rows in arrays and lists without wrapper classes.", InspectorMessageType.Info)]

        [IconButton("d_MoveTool", nameof(SnapWaypointIndex), "Snap this waypoint to ground elevation", ButtonColor = "#3B82F6")]
        public Vector3[] perimeterPatrolPoints = new Vector3[]
        {
            new Vector3(0, 4.5f, 0),
            new Vector3(15, 2.8f, -10),
            new Vector3(30, 8.1f, 15)
        };

        [IconButton("d_Refresh", nameof(PingEndpoint), "Ping and re-validate this server cluster node", ButtonColor = "#10B981")]
        public List<string> clusterEndpoints = new List<string>
        {
            "https://cluster-us-east.net",
            "https://cluster-eu-central.net"
        };

        // ─── 4. Interactive Playground Actions ───────────────────────────────────
        [BoxGroup("4. Interactive Playground", BackgroundColor = "#0F172A", BorderColor = "#EAB308", BorderRadius = 6)]
        [Button("Simulate Patrol Route Execution", BackgroundColor = "#10B981", TextColor = "#FFFFFF")]
        public void SimulatePatrolExecution()
        {
            Debug.Log($"[IconButton] Patrol route initialized with {perimeterPatrolPoints.Length} waypoints.");
        }

        private void RandomizePosition() => spawnPosition = UnityEngine.Random.insideUnitSphere * 10f;
        private void ResetAllData() => playerProfile = "Default_Player";
        private void SnapWaypointIndex() { for (int i = 0; i < perimeterPatrolPoints.Length; i++) perimeterPatrolPoints[i].y = 0f; }
        private void PingEndpoint() => Debug.Log("[IconButton] Pinged cluster nodes.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### Attribute Stacking

| Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[IconButton]` (Stacked) | Supported | `AllowMultiple = true`. Stack multiple icon buttons on the same field to create an action toolbar. |
| `[BoxGroup]` | Supported | Integrates cleanly inside groups and cards without layout overflows. |
| `[Condition]` | Supported | Dynamic boolean conditions enable or disable the button interactively. |

### Collection Cascading Matrix

| Collection Type | Element Type | Supported | Notes |
| :--- | :--- | :---: | :--- |
| `T[]` (Array) | `Vector3[]`, `string[]`, any element | Yes | Attaches compact inline action icon buttons to every element row. |
| `List<T>` | `List<string>`, `List<Vector3>`, `List<T>` | Yes | Cascades down to individual elements automatically. |
| `AdvancedList<T>` | Any element type | Yes | Fully supported in reorderable list rows. |
| `SerializableDictionary<K, V>` | Key or Value elements | Yes | Elements receive dedicated action buttons. |
| `[Serializable] class/struct` | Nested properties | Yes | Methods can be declared on the nested class or fallback to the root component. |

