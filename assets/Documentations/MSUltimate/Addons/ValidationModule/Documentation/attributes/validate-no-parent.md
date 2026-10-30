# [ValidateNoParent]

> Validates that a referenced GameObject is a root-level object in the hierarchy with no parent transform (transform.parent == null).

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateNoParent]` inspects assigned `GameObject` or `Component` fields. It asserts that the referenced object resides at the root level of the active scene hierarchy (`transform.parent == null`). If the assigned object is parented under any container or other GameObject, an immediate error banner is displayed.

**The Problem:**
Singleton managers, scene directors, global audio controllers, and `DontDestroyOnLoad` managers must typically remain root-level GameObjects. If a level designer accidentally parents a master manager under a moving vehicle or a localized level sector container, the manager gets inadvertently scaled, moved, disabled, or destroyed when the parent container is unloaded or deleted.

**The Solution:**
Decorating root manager fields with `[ValidateNoParent]`:
- **Root-Level Enforcement:** Guarantees that referenced objects have no parent in the hierarchy (`transform.parent == null`).
- **Protects Global Managers:** Prevents global singletons and `DontDestroyOnLoad` systems from being parented under ephemeral sector containers.
- **Immediate Hierarchy Feedback:** Warns developers immediately if an object is mistakenly dragged into a folder or group container.
- **Pairs with `[ValidateRequiresParent]`:** Perfect counterpart to `[ValidateRequiresParent]`.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class GameInitializer : MonoBehaviour
{
    [ValidateNoParent("Master Audio Manager must remain a root-level GameObject.")]
    public GameObject masterAudioManager;
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
public ValidateNoParentAttribute(
    string message = "GameObject must be a root-level object (no parent).")
```

- **`message`** (`string`, optional): Custom error message to display upon validation failure.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | `"GameObject must be a root-level..."` | Failure explanation displayed in the validation message banner. |
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

namespace ProjectZero.Core
{
    public class SceneLifecycleSupervisor : MonoBehaviour
    {
        [Header("Global Persistent Systems")]
        [ValidateNoParent("Network session manager must not be parented under any scene hierarchy container.",
            MessageType = InspectorMessageType.Error)]
        public GameObject networkSessionManager;

        [ValidateNoParent("Global event broker must remain an unparented root object.")]
        public GameObject globalEventBroker;

        private void Awake()
        {
            if (networkSessionManager != null && networkSessionManager.transform.parent == null)
            {
                DontDestroyOnLoad(networkSessionManager);
            }
        }
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateHierarchyDepth]`** | High | Equivalent to setting `minDepth = 0, maxDepth = 0`. |
| **`[ValidateRequiresParent]`** | Inverse | Exact complement: use `[ValidateRequiresParent]` when an object must have a parent. |
| **`[Required]` / `[NotNull]`** | High | Ensure reference is non-null before validating parent hierarchy status. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
