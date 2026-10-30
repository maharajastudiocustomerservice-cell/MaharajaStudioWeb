# [ComponentNotification]

> Adds an interactive, dismissible toast notification banner above the component body with semantic status color palettes, icons, and close buttons.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentNotification]` introduces interactive status banners to Unity component cards. Injected into `ComponentSlot.BeforeBody`, it renders a styled notification strip above serialized inspector fields. It supports four semantic notification types (`NotificationType` $\to$ `Info`, `Success`, `Warning`, `Error`), built-in or custom icons (`Icon`), full background and text color overrides (`BackgroundColor`, `TextColor`), rounded corners (`BorderRadius`), and an interactive dismissal button (`Dismissible = true`). When clicked, the dismissal button smoothly hides the banner for the duration of the current editor session.

**The Problem:**
Developers often need to communicate runtime prerequisites, pending migrations, asset warnings, or success confirmations across complex MonoBehaviours. Static warning labels can clutter inspector layouts permanently, even after the developer has read and acknowledged them.

**The Solution:**
Decorating components with `[ComponentNotification]`:
- **Interactive Session Dismissal:** The integrated close button (`✕`) lets developers acknowledge and dismiss the notice without altering script code.
- **Four Semantic Status Modes:** Instant color and icon styling for `Info` (blue), `Success` (green), `Warning` (amber), and `Error` (red).
- **Multiple Allowed:** `AllowMultiple = true` allows stacking multiple status alerts concurrently.
- **Custom Theming & Icons:** Override default colors and icons to match custom studio design standards.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentNotification("Migration to Input System Package completed successfully.", Type = NotificationType.Success)]
public class PlayerInputRouter : MonoBehaviour
{
    public float movementDeadzone = 0.15f;
    public bool enableHapticFeedback = true;
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Component Slot** | `BeforeBody` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentNotificationAttribute(string message)
```

- `message`: Informational or alert text string displayed in the notification banner.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | *(Constructor)* | Primary notification message string. |
| `Type` | `NotificationType` | `NotificationType.Info` | Semantic notification mode (`Info`, `Success`, `Warning`, `Error`). |
| `Dismissible` | `bool` | `true` | When true, renders an interactive close button (`✕`) to hide the banner. |
| `Icon` | `string` | `""` | Unity built-in editor icon name override. If empty, uses preset icon for the type. |
| `BackgroundColor` | `string` | `""` | Hex background color override string. If empty, uses preset color. |
| `TextColor` | `string` | `""` | Hex text color override string. If empty, uses preset color. |
| `BorderRadius` | `float` | `4f` | Corner rounding radius in pixels. |
| `MarginBottom` | `float` | `4f` | Vertical margin spacing in pixels below the banner. |
| `Order` | `int` | `0` | Execution and rendering priority order relative to other stacked modular attributes. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#3B82F6", Width = 1.5f, Radius = 6f)]
[ComponentHeader("SAVE STATE SYNCHRONIZER", Subtitle = "Local SQLite & Cloud Steam Sync", BackgroundColor = "#111827", TitleColor = "#E5E7EB")]
[ComponentNotification("Cloud save schema upgraded to v3. Verify all player profiles before deploying.", Type = NotificationType.Warning, Dismissible = true)]
[ComponentNotification("Local SQLite cache verified: 100% integrity.", Type = NotificationType.Success, Dismissible = true)]
public class SaveStateSynchronizer : MonoBehaviour
{
    [Header("Sync Timing")]
    public float autoSaveIntervalSeconds = 300f;
    public int maxBackupSnapshots = 5;
    public bool compressSaveFilesWithZstd = true;

    [Header("Network Authentication")]
    public string cloudApiEndpoint = "https://save.studio.net/api/v3";
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Banners render neatly in `BeforeBody`, docking directly underneath the header card. |
| **`[ComponentHelpBox]`** | High | Use notifications for dismissible operational status and help boxes for permanent instructions. |
| **Multiple Instances** | High | Stacking multiple notifications organizes complex statuses into a clean list of dismissible banners. |
