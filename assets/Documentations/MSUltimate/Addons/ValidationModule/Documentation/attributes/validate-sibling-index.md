# [ValidateSiblingIndex]

> Validates that a referenced GameObject or Component occupies a specific sibling index or falls within a required sibling index range within its parent transform.

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateSiblingIndex]` inspects assigned `GameObject` or `Component` reference fields (such as `Transform` or `RectTransform`). It checks the referenced object's position in its parent transform hierarchy (`transform.GetSiblingIndex()`) against required bounds (`MinIndex`, `MaxIndex`) or a precise target position (`ExactIndex`). If the object is not nested under a parent or violates the index constraint, an informative validation alert is displayed in the Inspector and registered in the Validation Engine window.

**The Problem:**
In Unity UI (uGUI), sibling order directly controls the visual draw call layering and canvas render sorting:
- Background panels must always reside at index `0` so they never occlude foreground interactive buttons.
- Tooltips, modal dialogue overlays, and toast notifications must sit at high sibling indices so they render in front of all panels.
- Level design containers and mission marker hierarchies rely on ordered index slots for predictable sequential processing.
Without automated sibling index validation, artists and developers easily drag objects into incorrect hierarchy positions, causing rendering bugs, buried UI panels, or incorrect visual overlaps that are subtle to diagnose.

**The Solution:**
Decorating reference fields with `[ValidateSiblingIndex]`:
- **Exact Index Locking:** Pin objects to precise positions (`ExactIndex = 0` for backgrounds, `ExactIndex = 10` for top-level tooltips).
- **Index Range Clamping:** Enforce flexible sibling bands (`MinIndex = 2, MaxIndex = 5`) for grouped interactive widgets.
- **Minimum Index Thresholds:** Require overlay HUD elements to sit above standard widgets (`MinIndex = 5, MaxIndex = int.MaxValue`).
- **Real-Time Inspector Feedback:** Displays immediate warning or error banners when hierarchy reordering breaks UI layout contracts.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class UILayerManager : MonoBehaviour
{
    [ValidateSiblingIndex("Background panel must be at sibling index 0 to render behind other UI layers.", ExactIndex = 0)]
    public GameObject backgroundPanel;

    [ValidateSiblingIndex("Modal overlay must be at index 5 or higher to appear in front of standard widgets.", MinIndex = 5)]
    public RectTransform modalOverlay;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ValidationModule Addon |
| **Attribute Target** | `Field` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Inspector & Validation Engine Window |
| **Validation Interface** | `IValidationAttribute` |

---

## 4. Constructors & Parameters

```csharp
public ValidateSiblingIndexAttribute(string message = "GameObject is not at the required sibling index.")
```

- **`message`** (`string`, optional): Custom error message displayed upon validation failure. Default is `"GameObject is not at the required sibling index."`.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MinIndex` | `int` | `0` | Minimum acceptable sibling index (inclusive). |
| `MaxIndex` | `int` | `int.MaxValue` | Maximum acceptable sibling index (inclusive). |
| `ExactIndex` | `int` | `-1` | When set to `>= 0`, overrides `MinIndex`/`MaxIndex` and requires the object to be at this exact sibling index. |
| `Message` | `string` | `"GameObject is not at the required sibling index."` | Failure explanation displayed in the validation message banner. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Visual severity badge (`None`, `Info`, `Warning`, `Error`). |
| `ErrorColor` | `string` | `null` | Hex text color override for the validation error banner. |
| `ErrorBackgroundColor` | `string` | `null` | Hex background color override for the alert box. |
| `FontSize` | `int` | `0` | Font size override in pixels (0 uses default inspector font size). |
| `Padding` | `float` | `0f` | Internal padding around the validation banner. |
| `Margin` | `float` | `5f` | Outer margin spacing separating the banner from neighboring controls. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
using MaharajaStudio.MSUltimate.ValidationModule;

namespace ProjectZero.UI
{
    public class CanvasHierarchyManager : ModularMonoBehaviour
    {
        [Header("Backdrop Configuration")]
        [ValidateSiblingIndex("Backdrop must occupy sibling index 0 to stay behind canvas contents.",
            ExactIndex = 0,
            MessageType = InspectorMessageType.Error)]
        public GameObject backdropPanel;

        [Header("Gameplay Markers")]
        [ValidateSiblingIndex("Objective markers must be located between sibling indices 2 and 4.",
            MinIndex = 2,
            MaxIndex = 4,
            MessageType = InspectorMessageType.Warning)]
        public RectTransform objectiveMarkerGroup;

        [Header("Topmost Overlay")]
        [ValidateSiblingIndex("Notification toast must be at sibling index >= 8 to render topmost.",
            MinIndex = 8,
            MaxIndex = int.MaxValue,
            ErrorColor = "#FF5555")]
        public RectTransform notificationToast;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateSiblingCount]`** | High | Combine to guarantee both the total sibling count and exact position ordering. |
| **`[ValidateUniqueInHierarchy]`** | High | Enforce unique names among siblings while also maintaining index placement. |
| **`[ValidateRequiresParent]`** | High | Guarantee the reference has a valid parent transform before checking sibling index. |
| **Validation Engine** | Native | Audited automatically during scene-wide and prefab validation batch runs. |
