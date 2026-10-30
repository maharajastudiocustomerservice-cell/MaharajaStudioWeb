# [OnPlayModeStateChanged]

> Automatically executes a C# callback method when Unity transitions into or out of Play Mode.

---

## 1. Overview & Value Proposition

**What it does:**
Triggers a method automatically whenever you enter, pause, or exit Unity's Play Mode.

**The Problem:**
In standard Unity, running setup or cleanup code during Play Mode transitions requires subscribing to `EditorApplication.playModeStateChanged` inside a static Editor class. This scatters your game logic across different files and leads to memory leaks if event handlers are not properly unregistered.

**The Solution:**
Add `[OnPlayModeStateChanged]` directly inside your MonoBehaviour:
- **Targeted State Transitions:** Trigger specifically on `EnteredPlayMode`, `ExitingPlayMode`, `EnteredEditMode`, `ExitingEditMode`, or `Any`.
- **Zero Static Listeners:** No manual event subscription or unsubscription boilerplate needed.
- **State Restoration:** Perfect for resetting debug camera positions, restoring initial spawn coordinates, or wiping test counters.
- **Safe Execution:** Executes cleanly without stalling domain reload or Play Mode startup time.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameTestRig : MonoBehaviour
{
    [OnPlayModeStateChanged(PlayModeStateTarget.EnteredPlayMode)]
    private void OnStartGame()
    {
        Debug.Log("Entered Play Mode: Initializing automated gameplay tests!");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Method | Field | Property` |
| **Supported Types** | Parameterless methods, or methods accepting `PlayModeStateTarget` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public OnPlayModeStateChangedAttribute()
public OnPlayModeStateChangedAttribute(PlayModeStateTarget targetState)
public OnPlayModeStateChangedAttribute(string methodName, PlayModeStateTarget targetState = PlayModeStateTarget.Any)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `targetState` | `PlayModeStateTarget` | `PlayModeStateTarget.Any` | Specific transition event to listen for (`EnteredPlayMode`, `ExitingPlayMode`, `EnteredEditMode`, `ExitingEditMode`, `Any`). |
| `methodName` | `string` | `null` | Optional method name when placing the attribute on a field or property instead of directly on the method. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TargetState` | `PlayModeStateTarget` | `PlayModeStateTarget.Any` | The specific Play Mode transition trigger. |
| `MethodName` | `string` | `null` | Target method name invoked when attribute decorates a field or property. |
| `Order` | `int` | `0` | Execution priority relative to other callbacks. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerSpawnManager : MonoBehaviour
{
    [Header("Spawn Position Cache")]
    public Vector3 editorDesignPosition;
    public bool resetOnExitPlayMode = true;

    [OnPlayModeStateChanged(PlayModeStateTarget.EnteredPlayMode)]
    private void CacheEditorState()
    {
        editorDesignPosition = transform.position;
        Debug.Log($"[SpawnManager] Cached editor design position: {editorDesignPosition}");
    }

    [OnPlayModeStateChanged(PlayModeStateTarget.EnteredEditMode)]
    private void RestoreEditorState()
    {
        if (resetOnExitPlayMode)
        {
            transform.position = editorDesignPosition;
            Debug.Log("[SpawnManager] Restored original editor design position after exiting Play Mode.");
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Pairs well with interactive debug test harnesses. |
| `[ReadOnly]` | Supported | Useful for displaying editor-cached coordinates or state flags. |
| `[BoxGroup]` | Supported | Fully functional inside layout containers. |
