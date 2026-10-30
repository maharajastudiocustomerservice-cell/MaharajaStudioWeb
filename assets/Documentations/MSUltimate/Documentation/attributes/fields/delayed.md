# [Delayed]

> Defers updating the serialized property until the user presses Enter or the input field loses focus.

---

## 1. Overview & Value Proposition

**What it does:**
Prevents immediate property value updates on every single keystroke, committing the value only when you press Enter or click away.

**The Problem:**
In standard Unity, typing a number or string updates the serialized property on every typed character. If a setter or `OnValidate` method re-generates meshes, recalculates pathfinding, or triggers web requests, typing `"1000"` will run expensive rebuilds 4 times (`1`, `10`, `100`, `1000`), freezing the editor.

**The Solution:**
Add `[Delayed]` to any text or numeric field:
- **Batch Expensive Rebuilds:** Commit changes only when the user finishes typing and presses Enter or un-focuses the field.
- **Prevents Intermediate Invalids:** Avoids temporary zero or single-digit values from triggering validation errors while typing.
- **Broad Data Type Support:** Supported on `float`, `int`, `string`, `double`, and `long`.
- **Zero Runtime Overhead:** Operates strictly within the UI Toolkit field change event pipeline.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TerrainBakeSettings : MonoBehaviour
{
    [Delayed]
    public int voxelResolution = 512;

    [Delayed]
    public string remoteApiEndpoint = "https://api.game.internal/v1/config";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `float`, `int`, `string`, `double`, `long`, `short`, `byte`, `uint`, `ulong` |
| **Collection Cascading** | Supported (`List<T>`, `T[]`, `AdvancedList<T>`, `SerializableDictionary<K, V>` via `ICollectionElementAttribute`) |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public DelayedAttribute()
```

*This attribute is configured using public object initializer properties.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TextColor` | `string` | `null` | Optional hex text color override. |
| `BackgroundColor` | `string` | `null` | Optional hex background color override. |
| `LabelColor` | `string` | `null` | Optional hex label color override. |
| `LabelWidth` | `float` | `0f` | Optional fixed label width in pixels. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using Delayed = MaharajaStudio.MSUltimate.Runtime.DelayedAttribute;

namespace MaharajaStudio.MSUltimate.Example
{
    [AddComponentMenu("Maharaja Studio/MSUltimate/Samples/Fields/Delayed Example")]
    public class DelayedExample : ModularMonoBehaviour
    {
        // ─── 1. Standalone Usage: Deferred Input Commits ─────────────────────────
        [Title("1. Deferred Input Commits", "Prevents continuous updates while typing", TitleColor = "#38BDF8")]
        [InfoBox("The [Delayed] attribute defers property value commits until Enter is pressed or focus is lost.")]

        [Delayed]
        public float renderScale = 1.0f;

        [Delayed]
        public int maxParticleBudget = 10000;

        [Delayed]
        public string apiEndpointUrl = "https://api.game.internal/v2/config";

        // ─── 2. Inside Class Demonstration ───────────────────────────────────────
        [Title("2. Inside Class Demonstration", "Encapsulated deferred inputs", TitleColor = "#A855F7")]
        public ServerConnection primaryServer = new ServerConnection();

        [Serializable]
        public class ServerConnection
        {
            [Delayed] public string serverHost = "10.0.0.1";
            [Delayed] public int listenPort = 8080;
            [Delayed] public float timeoutSeconds = 30f;
        }

        // ─── 3. Direct Collections Cascading ─────────────────────────────────────
        [Title("3. Direct Collections Cascading", "Direct collection cascading on float[] and List<string>", TitleColor = "#10B981")]
        [InfoBox("[Delayed] implements ICollectionElementAttribute to cascade delayed commit input fields down into raw arrays and lists automatically.", InspectorMessageType.Info)]

        [Delayed]
        public float[] physicsSubstepScales = new float[] { 0.016f, 0.008f, 0.004f };

        [Delayed]
        public List<string> clusterRemoteEndpoints = new List<string>
        {
            "https://node-1.region.gameserver.io",
            "https://node-2.region.gameserver.io"
        };

        // ─── 4. Interactive Playground ───────────────────────────────────────────
        [Title("4. Interactive Playground", "Inspect current committed values in console", TitleColor = "#F59E0B")]
        [ButtonGroup("DelayedActions")]
        [Button("Print Committed Server Config", BackgroundColor = "#0284C7", TextColor = "#FFFFFF")]
        private void PrintServerConfig()
        {
            Debug.Log($"[Delayed] Primary: {primaryServer.serverHost}:{primaryServer.listenPort} | Scale: {renderScale}");
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

### Attribute Stacking

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[OnValueChanged]` | Recommended | Pairs together to ensure callbacks only trigger once editing is committed. |
| `[SuffixLabel]` | Supported | Suffix measurement unit remains docked cleanly on the right. |
| `[BoxGroup]` | Supported | Functions normally inside group containers. |

### Collection Cascading Matrix

| Collection Type | Element Type | Supported | Notes |
| :--- | :--- | :---: | :--- |
| `T[]` (Array) | `float[]`, `int[]`, `string[]`, `double[]` | Yes | Each array element renders with a delayed commit field. |
| `List<T>` | `List<float>`, `List<string>`, `List<int>` | Yes | Cascades down to individual elements automatically. |
| `AdvancedList<T>` | Numeric and text types | Yes | Supported in reorderable list items. |
| `SerializableDictionary<K, V>` | Key or Value elements | Yes | Elements receive delayed inputs for deferred dictionary mutation. |
| `[Serializable] class/struct` | Nested properties | Yes | Fully supported on nested fields inside serializable classes. |

