# [ValidateInput]

> Validates a field's value in real time using a custom C# callback method and displays informative, warning, or error messages when validation fails.

---

## 1. Overview & Value Proposition

**What it does:**
Executes a custom validation callback method on the MonoBehaviour or ScriptableObject whenever a field is edited. If the method returns `false`, it renders a styled feedback message box beneath the field with customizable severity (`Info`, `Warning`, `Error`).

**The Problem:**
Complex game logic often requires multi-variable validation checks that cannot be captured by simple numeric ranges or null checks—such as checking that a string is a valid regex, verifying that weapon damage is not negative, or ensuring an inventory count matches maximum slots.

**The Solution:**
Add `[ValidateInput]` to any field:
- **Arbitrary C# Validation:** Run any C# boolean method receiving the field value as a parameter or checking instance state.
- **Message Severity Levels:** Choose between `Info`, `Warning`, or blocking `Error` callouts.
- **Styling Customization:** Customize message colors, padding, background plates, and font sizes.
- **Collection Elements:** Can validate each element in collections (`ICollectionElementAttribute`).

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class PlayerAccount : MonoBehaviour
{
    [ValidateInput(nameof(ValidatePlayerName), "Player name must be between 3 and 16 characters!")]
    public string playerName = "Hero";

    private bool ValidatePlayerName(string name)
    {
        return !string.IsNullOrEmpty(name) && name.Length >= 3 && name.Length <= 16;
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Field | Property` |
| **Supported Types** | Any serializable field type |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ValidateInputAttribute(string conditionMethod, string message = "Invalid input")
public ValidateInputAttribute(string conditionMethod, string message, InspectorMessageType messageType)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `conditionMethod` | `string` | *(Required)* | Name of the validation method returning `bool`. |
| `message` | `string` | `"Invalid input"` | Validation message text displayed when callback returns `false`. |
| `messageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Severity type (`Info`, `Warning`, `Error`). |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ConditionMethod` | `string` | *(Constructor)* | Name of the callback method invoked on the target object. |
| `Message` | `string` | *(Constructor)* | Validation failure message text. |
| `MessageType` | `InspectorMessageType` | `InspectorMessageType.Error` | Message severity category. |
| `ErrorColor` | `string` | `null` | Hex color code for message text. |
| `ErrorBackgroundColor` | `string` | `null` | Hex color code for message callout background plate. |
| `FontSize` | `int` | `0` | Font size for validation message (`0` = system default). |
| `Padding` | `float` | `0f` | Internal padding inside the message box. |
| `Margin` | `float` | `5f` | Margin spacing around the message box. |
| `Order` | `int` | `0` | Execution priority relative to other attributes on the same member. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkServerConfig : MonoBehaviour
{
    [Header("Port Number Validation")]
    [ValidateInput(nameof(IsValidPort), "Port number must be between 1024 and 65535!", InspectorMessageType.Error)]
    public int serverPort = 7777;

    [Header("Connection Timeout Warning")]
    [ValidateInput(nameof(CheckTimeout), "Timeouts under 5 seconds may cause frequent disconnections.", InspectorMessageType.Warning)]
    public float timeoutSeconds = 15f;

    private bool IsValidPort(int port) => port >= 1024 && port <= 65535;
    private bool CheckTimeout(float timeout) => timeout >= 5f;
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Message boxes render cleanly inside container groups. |
| Multiple Allowed | Supported | Stack multiple `[ValidateInput]` rules on a single field to check multiple conditions. |
| `ICollectionElement` | Supported | Validates each individual item in arrays or lists. |
