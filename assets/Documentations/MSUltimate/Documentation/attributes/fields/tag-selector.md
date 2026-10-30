# [TagSelector]

> Displays string fields as an interactive dropdown menu populated directly with Unity project Tags, with 1-click Project Settings access.

---

## 1. Overview & Value Proposition

**What it does:**
Converts standard `string` fields into an ergonomic dropdown menu populated in real time with all defined Unity tags (`"Player"`, `"Enemy"`, `"Untagged"`, and custom user tags). Includes a 1-click shortcut button to open Project Settings $\rightarrow$ Tags & Layers.

**The Problem:**
In standard Unity, string fields intended to hold tags (such as `public string targetTag = "Enemy";`) are displayed as plain text input fields. Developers must manually type the tag string without auto-completion. A single spelling or casing typo (such as `"enemy"` instead of `"Enemy"`) causes `CompareTag()` checks to fail silently at runtime.

**The Solution:**
Add `[TagSelector]` to any string field:
- **No More Typos:** Select tags directly from a clean dropdown populated with all current project tags.
- **Dynamic Updates:** Automatically reflects newly added or renamed tags from Project Settings.
- **1-Click Tags & Layers Access:** An inline gear button jumps directly to Project Settings to add new tags without leaving the Inspector.
- **Collection Support:** Full support for `List<string>` and `string[]` via `ICollectionElementAttribute`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class ProximityDetector : MonoBehaviour
{
    [TagSelector]
    public string targetTag = "Player";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | `string` |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public TagSelectorAttribute(string customLabel = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `customLabel` | `string` | `null` | Optional display label override for the inspector row. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CustomLabel` | `string` | `null` | Custom field display name override. |
| `ShowManagerButton` | `bool` | `true` | If `true`, shows a button to open Project Settings $\rightarrow$ Tags & Layers. |
| `TextColor` | `string` | `null` | Hex text color override for the dropdown. |
| `BackgroundColor` | `string` | `null` | Hex background color for the dropdown field. |
| `LabelWidth` | `float` | `0f` | Explicit width for the field label in pixels. |
| `Order` | `int` | `0` | Drawing execution order in the inspector pipeline. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class CombatDamageZone : MonoBehaviour
{
    [Header("Primary Target Tag")]
    [TagSelector("Afflicted Target Tag", ShowManagerButton = true)]
    public string primaryTargetTag = "Enemy";

    [Header("Immune Tags (Collection of Tags)")]
    [TagSelector]
    public List<string> immuneTags = new List<string>
    {
        "Player",
        "Companion"
    };

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag(primaryTargetTag))
        {
            ApplyDamage(other.gameObject);
        }
    }

    private void ApplyDamage(GameObject target)
    {
        Debug.Log($"Damage applied to {target.name}");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Sits comfortably inside detection and trigger cards. |
| `[ShowIf]` | Supported | Conditionally hides or displays tag targeting options. |
| `[ReadOnly]` | Supported | Locks tag selection while preserving display state. |
| `ICollectionElement` | Supported | Renders dropdowns inside `List<string>` and `string[]` rows. |
