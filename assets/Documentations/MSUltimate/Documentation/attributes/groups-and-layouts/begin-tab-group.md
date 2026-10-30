# [BeginTabGroup]

> Organizes inspector members into an interactive multi-tab navigation bar with custom tab icons, active indicator bars, and theme styling.

---

## 1. Overview & Value Proposition

**What it does:**
Initializes an interactive tabbed navigation layout. Subsequent serialized members are grouped under the specified tab button until closed by an `[EndTabGroup]` or transitioned to another tab in the same group. Multiple declarations sharing the same `GroupName` automatically fuse into a unified tab strip.

**The Problem:**
Complex gameplay components—such as player controllers, AI behavior trees, or vehicle physics—often contain dozens of fields. Stacking all fields vertically creates endless inspector scrollbars and overwhelms designers trying to locate specific features.

**The Solution:**
Add `[BeginTabGroup("TabName")]` across your class:
- **Clean Tab Switching:** Switch seamlessly between tabs like "General", "Movement", "Combat", and "VFX".
- **Tab Icons & Visual Indicators:** Decorate tabs with built-in Unity icons (`TabIcon`) and colored bottom/top indicator lines (`ShowTabIndicator = true`).
- **Shared Group Identification:** Tabs sharing the same `GroupName` coalesce into a single unified tab container.
- **Collapsible Tab Sets:** Make the entire tab container collapsible with `Collapsible = true`.
- **Exhaustive Styling Engine:** Customize colors, borders, fonts, paddings, and hover effects for both the tab strip and the content body.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerController : MonoBehaviour
{
    // Tab 1: Locomotion
    [BeginTabGroup("Locomotion", GroupName = "PlayerTabs")]
    public float walkSpeed = 5f;
    public float sprintSpeed = 10f;

    // Tab 2: Combat
    [BeginTabGroup("Combat", GroupName = "PlayerTabs")]
    public int maxHealth = 100;
    [EndTabGroup] // Placed on the final field of the tab group to close it
    public float attackPower = 25f;

    // Renders full-width below the tab container
    public bool isPlayerActive = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property | Method` |
| **Supported Types** | Any member declared within tab layout scopes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |
| **Drawer Resolution** | Handled natively by MSUltimate Inspector layout engine |

---

## 4. Constructors & Parameters

```csharp
public BeginTabGroupAttribute(string tabName)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `tabName` | `string` | *(Required)* | Display name on the individual tab button. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TabName` | `string` | *(Set in constructor)* | Title displayed on this specific tab button. |
| `GroupName` | `string` | `"DefaultGroup"` | Shared group identifier uniting individual tabs. |
| `MarginTop` | `float` | `5f` | Spacing above the tab group container in pixels. |
| `MarginBottom` | `float` | `5f` | Spacing below the tab group container in pixels. |
| `MarginLeft` | `float` | `0f` | Spacing to the left of the tab group container in pixels. |
| `MarginRight` | `float` | `0f` | Spacing to the right of the tab group container in pixels. |
| `Height` | `float` | `0f` | Fixed height for the tab group container (`0` = auto). |
| `MinHeight` | `float` | `0f` | Minimum height for the tab group container in pixels. |
| `MaxHeight` | `float` | `0f` | Maximum height for the tab group container in pixels. |
| `BackgroundColor` | `string` | `null` | Hex fill color for the overall tab container. |
| `BorderColor` | `string` | `null` | Hex outline border color for the overall container. |
| `BorderWidth` | `float` | `0f` | Border outline width for the overall container. |
| `BorderRadius` | `float` | `0f` | Corner radius for the overall container. |
| `Title` | `string` | `null` | Optional master title header text rendered above the tab strip. |
| `TitleColor` | `string` | `null` | Hex color code for the group title text. |
| `TitleFontSize` | `int` | `0` | Font size for the group title (`0` = default). |
| `TitleBold` | `bool` | `true` | Whether the group title text is bold. |
| `TitleAlignment` | `UiAlignment` | `UiAlignment.Left` | Alignment of the group title. |
| `TitleBackgroundColor` | `string` | `null` | Hex background color for the title header bar. |
| `TitleIcon` | `string` | `null` | Built-in Unity icon name displayed in the group title header. |
| `TitleBorderColor` | `string` | `null` | Hex border color for the title header area. |
| `TitleBorderWidth` | `float` | `0f` | Border width of the title header area. |
| `Collapsible` | `bool` | `false` | Allows collapsing the entire tab content area below the title. |
| `StartCollapsed` | `bool` | `false` | Whether the tab group starts in a collapsed state. |
| `CollapseButtonColor` | `string` | `null` | Hex color code for the collapse/expand button. |
| `TabStripBackgroundColor`| `string` | `null` | Hex background color for the bar containing tab buttons. |
| `TabStripBorderColor` | `string` | `null` | Hex border color for the tab strip bar. |
| `TabStripBorderWidth` | `float` | `0f` | Border width of the tab strip bar. |
| `TabStripPadding` | `float` | `0f` | Internal padding inside the tab strip bar. |
| `TabStripAlignment` | `UiAlignment` | `UiAlignment.Left` | Alignment of the tabs within the strip (`Left`, `Center`, `Right`). |
| `TabStripGap` | `float` | `2f` | Spacing in pixels between adjacent tab buttons. |
| `TabStripScrollable` | `bool` | `false` | If true, enables horizontal scrolling if tabs exceed container width. |
| `TabColor` | `string` | `null` | Default hex background color for tab buttons. |
| `ActiveTabColor` | `string` | `null` | Hex background color for the currently active/selected tab. |
| `InactiveTabColor` | `string` | `null` | Hex background color for inactive/unselected tabs. |
| `TabTextColor` | `string` | `null` | Default hex text color for tab buttons. |
| `ActiveTabTextColor` | `string` | `null` | Hex text color for the currently active tab. |
| `InactiveTabTextColor` | `string` | `null` | Hex text color for inactive tabs. |
| `TabFontSize` | `int` | `0` | Font size for the tab button text (`0` = default). |
| `TabPadding` | `float` | `10f` | Horizontal padding inside each tab button in pixels. |
| `TabPaddingVertical` | `float` | `6f` | Vertical padding inside each tab button in pixels. |
| `TabMargin` | `float` | `0f` | Margin between tab buttons. |
| `TabBorderRadius` | `float` | `0f` | Corner radius for the tab buttons. |
| `TabBorderWidth` | `float` | `0f` | Border outline width for tab buttons. |
| `TabBorderColor` | `string` | `null` | Default hex border color for tab buttons. |
| `ActiveTabBorderColor` | `string` | `null` | Hex border color for the active tab button. |
| `TabHeight` | `float` | `0f` | Fixed height for tab buttons (`0` = auto). |
| `TabMinWidth` | `float` | `0f` | Minimum pixel width for each tab button. |
| `TabExpandToFill` | `bool` | `false` | If true, every tab button expands to fill available strip space equally. |
| `TabFontStyle` | `FontStyle` | `FontStyle.Normal` | Default font style for tab button text. |
| `ActiveTabFontStyle` | `FontStyle` | `FontStyle.Bold` | Font style for the currently active tab button text. |
| `TabIcon` | `string` | `null` | Built-in Unity icon name displayed on this specific tab button. |
| `TabHoverColor` | `string` | `null` | Hex background color when hovering over a tab button. |
| `TabHoverTextColor` | `string` | `null` | Hex text color when hovering over a tab button. |
| `ShowTabIndicator` | `bool` | `false` | Displays a colored indicator bar on the active tab. |
| `TabIndicatorColor` | `string` | `null` | Hex color code for the active tab indicator line. |
| `TabIndicatorHeight` | `float` | `3f` | Thickness/height of the active indicator line in pixels. |
| `TabIndicatorPosition` | `TabIndicatorPos` | `TabIndicatorPos.Bottom` | Placement of the indicator line (`Bottom` or `Top`). |
| `ContentBackgroundColor`| `string` | `null` | Hex fill color for the tab body content area. |
| `ContentPadding` | `float` | `8f` | Internal padding inside the tab content area. |
| `ContentBorderColor` | `string` | `null` | Hex border color for the content area. |
| `ContentBorderWidth` | `float` | `0f` | Border width of the content area. |
| `ContentBorderRadius` | `float` | `0f` | Corner radius of the content area. |
| `ContentMargin` | `float` | `0f` | Spacing around the content area. |
| `ContentMinHeight` | `float` | `0f` | Minimum pixel height for the content area. |
| `Order` | `int` | `0` | Execution priority in the inspector pipeline (inherited from `ModularAttribute`). |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class AdvancedVehicleRig : MonoBehaviour
{
    // Tab 1: Engine & Power
    [BeginTabGroup("Engine & Power", GroupName = "VehicleRig", TabIcon = "d_SettingsIcon", ShowTabIndicator = true, TabIndicatorColor = "#e67e22")]
    public float horsepower = 450f;
    public float maxRpm = 7500f;
    public AnimationCurve torqueCurve;

    // Tab 2: Handling & Steering
    [BeginTabGroup("Handling & Steering", GroupName = "VehicleRig", TabIcon = "d_MoveTool", ShowTabIndicator = true, TabIndicatorColor = "#3498db")]
    public float maxSteeringAngle = 35f;
    public float gripMultiplier = 1.2f;
    public float downforceScalar = 2.5f;

    // Tab 3: Audio & VFX
    [BeginTabGroup("Audio & VFX", GroupName = "VehicleRig", TabIcon = "d_AudioSource Icon", ShowTabIndicator = true, TabIndicatorColor = "#2ecc71")]
    public AudioClip engineIdleClip;
    public AudioClip exhaustBackfireClip;
    [EndTabGroup] // Closes the VehicleRig tab container
    public ParticleSystem tireSmokeVfx;

    // Renders full-width below the tab container
    [Header("Telemetry Readout (Full Width)")]
    [ReadOnly]
    public bool isVehicleGrounded = true;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[EndTabGroup]` | Required | Closes the tab scope; decorate the last member of the final tab. |
| `[BoxGroup]` | Supported | Nests cleanly inside individual tab panels. |
| `[Button]` | Supported | Methods marked with `[Button]` can reside directly inside specific tabs. |
| `[ShowIf]` | Supported | Individual fields or entire tabs can be shown or hidden conditionally. |
