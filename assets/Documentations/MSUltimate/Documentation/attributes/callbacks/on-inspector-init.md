# [OnInspectorInit]

> Automatically executes a C# method the very first time the object's custom Inspector is drawn in the editor.

---

## 1. Overview & Value Proposition

**What it does:**
Runs a C# method once when an object is first selected and shown in the Unity Inspector.

**The Problem:**
Unity developers often use `OnValidate()` or `Reset()` to auto-find components or set default values. But `OnValidate()` runs constantly—every time you change any property, recompile scripts, or save scenes—causing lag, performance drops, and unwanted console spam.

**The Solution:**
Add `[OnInspectorInit]` above any setup method or field:
- **Runs Exactly Once:** Triggers only when you select the GameObject in the Hierarchy and open its Inspector.
- **No Lag Spikes:** Avoids heavy domain reload slowdowns and keeps your Editor snappy.
- **Ideal for Auto-Setup:** Perfect for caching `GetComponent<T>()` references, loading default config assets, or validating missing links.
- **Zero Build Footprint:** Runs purely inside the Editor and is completely stripped out of your final game build.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class EnemySetup : MonoBehaviour
{
    public Animator cachedAnimator;

    [OnInspectorInit]
    private void InitializeEditor()
    {
        if (cachedAnimator == null)
            cachedAnimator = GetComponentInChildren<Animator>();
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Method | AttributeTargets.Field | AttributeTargets.Property` |
| **Method Signature** | Parameterless method (`void MethodName()`) |
| **Allow Multiple** | `true` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public OnInspectorInitAttribute()
public OnInspectorInitAttribute(string methodName)
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MethodName` | `string` | `null` | Name of the callback method to invoke (when applied to a field or property). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LevelZoneManager : MonoBehaviour
{
    [BoxGroup("Zone References", Box = true)]
    public Collider zoneTrigger;
    [BoxGroup("Zone References")]
    public Light zoneKeyLight;

    [OnInspectorInit]
    private void AutoDiscoverZoneComponents()
    {
        if (zoneTrigger == null)
            zoneTrigger = GetComponent<Collider>();

        if (zoneKeyLight == null)
            zoneKeyLight = GetComponentInChildren<Light>();

        Debug.Log($"[LevelZoneManager] Initialized inspector references for '{gameObject.name}'.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Pairing with Fields:** Can be placed directly on a method, OR on a serialized field pointing to a method name via `[OnInspectorInit(nameof(InitMethod))]`.
- **Counterpart:** Works as the initialization counterpart to `[OnInspectorDispose]`, which handles teardown when the object is deselected.
- **Defensive Execution:** Wrapped in internal try-catch safety guards so errors in custom user initialization logic will not crash or break Unity Inspector rendering.
