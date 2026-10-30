# [ConfirmationDialog]

> Displays a modal confirmation prompt dialog before executing destructive button actions or committing critical property modifications.

---

## 1. Overview & Value Proposition

**What it does:**
Intercepts inspector interactions (such as button clicks or property edits) with a native Unity modal confirmation popup (`EditorUtility.DisplayDialog`). Requires the developer to explicitly confirm before the method executes or the property value updates.

**The Problem:**
Inspector utility buttons that wipe player progress, rebuild world databases, reset character stats, or overwrite saved assets can be clicked accidentally, resulting in lost work or corrupt project data.

**The Solution:**
Add `[ConfirmationDialog]` to any method or property:
- **Accident Prevention:** Guarantees destructive actions require a deliberate second click.
- **Customizable Dialog Copy:** Configure custom modal titles and explanatory prompt messages.
- **Button Labels:** Customize confirm and cancel button text (`"Proceed"`, `"Abort"`, `"Delete"`, `"Cancel"`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SaveManager : MonoBehaviour
{
    [Button("Reset All Save Data")]
    [ConfirmationDialog("Delete Save", "This will permanently wipe all local save files. Are you sure?")]
    public void WipeSaveData()
    {
        PlayerPrefs.DeleteAll();
        Debug.Log("Save data wiped successfully.");
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Method | Field | Property` |
| **Supported Types** | Any method or serializable field |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ConfirmationDialogAttribute(string title = null, string message = null)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `title` | `string` | `"Confirmation"` | Modal dialog window title header. |
| `message` | `string` | `"Are you sure you want to perform this action?"` | Body message explaining the action being confirmed. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | `"Confirmation"` | Dialog window title. |
| `Message` | `string` | `"Are you sure you want to perform this action?"` | Detailed body text explaining consequences. |
| `OkButton` | `string` | `"Yes"` | Text displayed on the primary confirmation action button. |
| `CancelButton` | `string` | `"No"` | Text displayed on the dismiss / cancel button. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LevelDatabaseManager : MonoBehaviour
{
    [Header("Destructive Administrative Actions")]
    [Button("Rebuild Level Grid Navmesh", ButtonSize.Large)]
    [ConfirmationDialog(
        Title = "Rebuild Navmesh Cache",
        Message = "Rebuilding all grid nodes may take several minutes and clears active baker caches.",
        OkButton = "Rebuild Now",
        CancelButton = "Cancel"
    )]
    public void RebuildNavmesh()
    {
        Debug.Log("Navmesh generation triggered.");
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[Button]` | Supported | Ideal combination for dangerous administrative or debug commands. |
| `[ButtonGroup]` | Supported | Functions smoothly on individual buttons inside a button row group. |
| `[ShowIf]` | Supported | Dialog only triggers when the button is active and visible. |
