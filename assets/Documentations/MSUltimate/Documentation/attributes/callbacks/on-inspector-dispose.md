# [OnInspectorDispose]

> Automatically executes a C# cleanup method when the object's custom Inspector is closed, deselected, or disposed.

---

## 1. Overview & Value Proposition

**What it does:**
Runs a cleanup method when you deselect the object or close its Inspector window.

**The Problem:**
In standard Unity, if your editor workflow generates temporary preview textures, native memory arrays, async polling tasks, or scene handle listeners, they keep leaking in the background when the user selects a different object unless you write custom `Editor.OnDisable()` script boilerplate.

**The Solution:**
Add `[OnInspectorDispose]` above your cleanup method or field:
- **Clean Deselection Cleanup:** Automatically triggers when the user clicks a different GameObject or closes the Inspector.
- **Prevent Memory Leaks:** Dispose native collections, release `RenderTexture` previews, and cancel cancellation tokens safely.
- **Counterpart to `[OnInspectorInit]`:** Pair initialization and teardown logic directly inside the MonoBehaviour.
- **Zero Runtime Overhead:** Only exists inside the Editor; completely excluded from final player builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class TextureGenerator : MonoBehaviour
{
    private Texture2D _previewTexture;

    [OnInspectorDispose]
    private void CleanupEditorTextures()
    {
        if (_previewTexture != null)
        {
            DestroyImmediate(_previewTexture);
            _previewTexture = null;
            Debug.Log("Released temporary editor textures.");
        }
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Method | AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | Parameterless methods |
| **Allow Multiple** | `true` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public OnInspectorDisposeAttribute()
public OnInspectorDisposeAttribute(string methodName)
```
- **`methodName`**: Optional method name when placing the attribute on a field or property instead of directly on the method.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MethodName` | `string` | `null` | Optional method name to invoke when applied at the field/property level. |
| `Order` | `int` | `0` | Execution priority relative to other dispose callbacks. |

---

## 6. Production-Grade Example

```csharp
using System.Threading;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LiveAudioStreamer : MonoBehaviour
{
    private CancellationTokenSource _cts;

    [OnInspectorInit]
    private void StartEditorPreview()
    {
        _cts = new CancellationTokenSource();
        Debug.Log("[LiveAudio] Started background audio telemetry stream.");
    }

    [OnInspectorDispose]
    private void StopEditorPreview()
    {
        if (_cts != null)
        {
            _cts.Cancel();
            _cts.Dispose();
            _cts = null;
            Debug.Log("[LiveAudio] Successfully stopped background audio stream on inspector dispose.");
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Pairing with `[OnInspectorInit]`:** Pair together for complete lifecycle management (Init + Dispose).
- **Pairing with `[OnStateUpdate]`:** Clean up polling loops or timers started during state updates.
- **Layouts:** Fully functional inside `[BoxGroup]`, `[TabGroup]`, and vertical stacks.
