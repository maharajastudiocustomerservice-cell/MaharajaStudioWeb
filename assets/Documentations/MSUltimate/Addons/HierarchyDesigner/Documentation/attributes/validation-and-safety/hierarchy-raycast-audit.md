# [HierarchyRaycastAudit]

> Audits UI graphics for wasted raycast calculations and provides an instant one-click optimization fix directly in the hierarchy.

---

## 1. Overview & Value Proposition

**What it does:**
`[HierarchyRaycastAudit]` inspects Unity UI components (`Graphic`, `Image`, `Text`, `TextMeshProUGUI`) on the GameObject. If non-interactive graphics have `raycastTarget = true` enabled (such as background plates, static icons, or decorative borders that never receive clicks), it displays an alert badge in the Hierarchy window. When `EnableOneClickFix = true`, clicking the badge in the Hierarchy immediately sets `raycastTarget = false` and marks the scene dirty.

**The Problem:**
In standard Unity UI (uGUI), newly created `Image` and `Text` components enable `Raycast Target` by default. As UI scenes expand, hundreds of non-interactive elements are tested every frame during `EventSystem` raycasting. This produces substantial CPU overhead, canvas rebuild penalties, and input latency—especially on mobile and VR devices. Manually hunting down and unchecking every redundant raycast target across dozens of nested prefabs is tedious and error-prone.

**The Solution:**
Decorating UI components with `[HierarchyRaycastAudit]`:
- **Automated Raycast Auditing:** Instantly identifies decorative UI elements wasting raycasts (`ShowOnlyIfWastingRaycasts = true`).
- **One-Click Instant Fix:** Simply click the hierarchy warning badge to automatically disable `raycastTarget` on all redundant graphics on that object.
- **Safe State Indicators:** When `ShowOnlyIfWastingRaycasts = false`, renders an unobtrusive green badge (`SafeColor`) confirming the object is optimized.
- **Measurable Mobile Performance:** Dramatically slashes CPU time inside `GraphicRaycaster.Raycast` during heavy touch/click interactions.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

[HierarchyRaycastAudit]
public class InventorySlotUI : MonoBehaviour
{
    public int slotIndex;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-HierarchyDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Window Surface** | Unity Hierarchy Window |
| **Render Engine** | `HierarchyRaycastAuditRenderer (IMGUI)` |

---

## 4. Constructors & Parameters

```csharp
public HierarchyRaycastAuditAttribute()
```

- Parameterless constructor with one-click repair enabled and alert filtering focused strictly on wasted raycasts.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ShowOnlyIfWastingRaycasts` | `bool` | `true` | When true, only displays the badge when decorative non-interactive graphics have raycasts enabled. |
| `WarningColor` | `string` | `"#C0392B"` | Hex color string for the warning badge when redundant raycast targets are detected. |
| `SafeColor` | `string` | `"#27AE60"` | Hex color string for the badge when all attached graphics are properly optimized. |
| `EnableOneClickFix` | `bool` | `true` | When true, clicking the hierarchy badge immediately disables `raycastTarget` on redundant elements. |
| `XOffset` | `float` | `4f` | Horizontal offset in pixels from the right margin of the hierarchy row. |
| `IsActiveInPlayMode` | `bool` | `true` | Whether raycast auditing indicators remain active during Play Mode. |
| `Order` | `int` | `0` | Drawing execution priority relative to other hierarchy row renderers. |

---

## 6. Real-World Production Example

```csharp
using UnityEngine;
using UnityEngine.UI;
using MaharajaStudio.MSUltimate.HierarchyDesigner;

namespace ProjectZero.UI
{
    // Health bar HUD with decorative borders and text audited for wasted raycasts
    [HierarchyRaycastAudit(
        ShowOnlyIfWastingRaycasts = true,
        WarningColor = "#E74C3C",
        EnableOneClickFix = true,
        XOffset = 6f)]
    public class PlayerHealthBarHUD : MonoBehaviour
    {
        [Header("UI References")]
        public Image healthFillImage;       // Fill bar - should not be a raycast target
        public Image frameBorderImage;      // Decorative frame - should not be a raycast target
        public Button useHealthPotionButton;// Interactive button - raycast target SHOULD remain true

        public void UpdateHealth(float current, float max)
        {
            if (healthFillImage != null)
                healthFillImage.fillAmount = current / max;
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[HierarchyRaycastTargetCounter]`** | High | Pair single-object raycast auditing with branch-wide cumulative raycast counters. |
| **`[HierarchyBatchingAlert]`** | High | Monitor both raycast waste and canvas draw call batching on UI hierarchies. |
| **`[HierarchyTooltip]`** | High | Hover tooltip explains why certain UI elements require interaction while others do not. |
| **`[HierarchyMissingScriptDetector]`** | High | Simultaneously guard against broken UI scripts and redundant raycasts. |
