# [Hide]

> Completely hides a serialized field or property from being drawn in the Inspector.

---

## 1. Overview & Value Proposition

**What it does:**
Conceals a public or `[SerializeField]` variable entirely from the Inspector without breaking its serialization or network replication.

**The Problem:**
Variables often need to be `public` (for other scripts to access) or serialized (so Unity saves their values in scenes, prefabs, or network packets). However, displaying internal cache IDs or runtime-managed data in the Inspector confuses designers and risks accidental manual tampering.

**The Solution:**
Add `[Hide]` to any serialized field:
- **Preserves Full Serialization:** Unity continues to serialize and save the field value without rendering it.
- **Leaves Public APIs Intact:** Keep fields public for high-performance direct script access without Inspector exposure.
- **Replaces `[HideInInspector]`:** Fully integrated into MSUltimate's UI Toolkit layout and grouping pipeline.
- **Zero Overhead:** Completely skipped during VisualElement generation passes.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkEntity : MonoBehaviour
{
    [Hide]
    public int internalNetworkSyncTick;

    public string entityDisplayName = "Hero";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field or property |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public HideAttribute()
```

*This attribute has no constructor parameters.*

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Order` | `int` | `0` | Modifier pipeline execution order. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SaveGameManager : MonoBehaviour
{
    [Header("Visible Save Settings")]
    public string saveSlotName = "Slot_01";
    public bool enableAutoSave = true;

    [Hide] // Serialized and saved into disk payload, but hidden from inspector
    public string cachedChecksumHash;

    [Hide]
    public long lastSaveTimestampUtc;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[HideIf]` | Alternative | Use `[Hide]` for permanent concealment; use `[HideIf]` for conditional hiding based on logic. |
| `[BoxGroup]` | Supported | Safely ignored; will not draw empty rows inside groups. |
| `[SerializeField]` | Compatible | Retains complete serialization while suppressing editor rendering. |
