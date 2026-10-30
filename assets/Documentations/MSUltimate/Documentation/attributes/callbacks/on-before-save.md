# [OnBeforeSave]

> Automatically executes a C# callback method right before a scene or asset is serialized and saved to disk.

---

## 1. Overview & Value Proposition

**What it does:**
Runs a method immediately before you save an asset or scene, letting you sanitize or prepare data.

**The Problem:**
In standard Unity, if a developer forgets to calculate derived stats, format metadata, or strip temporary runtime test objects before saving, bad data gets committed to version control. Unity offers no simple MonoBehaviour hook right before serialization happens.

**The Solution:**
Add `[OnBeforeSave]` above any method, field, or property in your component:
- **Pre-Save Sanitization:** Clean up null items, recalculate hashes, and format data before it touches disk.
- **Enforce Invariants:** Automatically validate that references and numeric ranges meet project standards before writing.
- **Strip Temporary Data:** Remove scratch runtime arrays, test spawn caches, or preview meshes cleanly.
- **Zero Runtime Overhead:** Only runs in the Editor; completely stripped from standalone game builds.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LevelConfig : MonoBehaviour
{
    public int enemyCount;
    public string checksum;

    [OnBeforeSave]
    private void PrepareForSave()
    {
        checksum = $"LEVEL_CNT_{enemyCount}_{System.DateTime.UtcNow.Ticks}";
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
public OnBeforeSaveAttribute()
public OnBeforeSaveAttribute(string methodName)
```
- **`methodName`**: Optional method name to invoke when placing the attribute on a field or property.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MethodName` | `string` | `null` | Optional method name to invoke when applied at the field/property level. |
| `Order` | `int` | `0` | Execution order priority among multiple lifecycle callbacks. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class QuestDatabase : MonoBehaviour
{
    [System.Serializable]
    public struct QuestEntry
    {
        public string questId;
        public int rewardExp;
    }

    public List<QuestEntry> quests = new List<QuestEntry>();
    public int totalQuestsCached;

    [OnBeforeSave]
    private void SanitizeQuestList()
    {
        // Remove empty or unconfigured entries before saving
        quests.RemoveAll(q => string.IsNullOrWhiteSpace(q.questId));
        totalQuestsCached = quests.Count;
        Debug.Log($"[QuestDatabase] Sanitized quest data: {totalQuestsCached} active quests saved.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Pairing with `[OnAfterSave]`:** Pair together for full before-and-after save workflows.
- **Pairing with `[ReadOnly]`:** Pair with read-only summary fields calculated right before save.
- **Layouts:** Functions normally inside `[BoxGroup]`, `[TabGroup]`, and custom layouts.
