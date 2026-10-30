# [ValidateEmail]

> Validates that a string field conforms to a valid email address format (e.g. user@domain.com).

---

## 1. Overview & Value Proposition

**What it does:**
`[ValidateEmail]` inspects string fields representing email addresses (such as crash report destinations, developer contact fields, or feedback endpoints). It validates the input string against standard RFC-compliant email address structure (`local-part@domain.tld`). If the string does not represent a validly formatted email address, an immediate validation error banner is displayed.

**The Problem:**
In developer tooling, analytics configurations, telemetry reporting, and customer support integrations, developers configure feedback recipients or crash alert emails in ScriptableObject configs. A mistyped address (e.g. missing `@` symbol, missing domain, or illegal whitespace) causes crash reports and feedback webhooks to fail silently at runtime.

**The Solution:**
Decorating string fields with `[ValidateEmail]`:
- **Format Verification:** Guarantees that any entered email conforms to valid email syntax (`user@domain.com`).
- **Real-Time Input Auditing:** Validates characters as they are typed in the Inspector, catching typos immediately.
- **Support for Empty Strings:** Pair with `[ValidateNotNull]` or `[Required]` if the field is mandatory; empty values can be optional fallback routes.
- **Customizable Error Text:** Provide clear error messages directing team members to provide the proper corporate or department address.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ValidationModule;

public class SupportFeedbackConfig : ScriptableObject
{
    [ValidateEmail("Please provide a valid support email address (e.g. support@studio.com).")]
    public string feedbackRecipient = "support@maharajastudio.com";
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
public ValidateEmailAttribute(string message = "Invalid email format.")
```

- **`message`** (`string`, optional): Custom error message displayed if the email format is invalid.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Message` | `string` | `"Invalid email format."` | Failure explanation displayed in the validation message banner. |
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

namespace ProjectZero.Telemetry
{
    [CreateAssetMenu(fileName = "CrashReportingConfig", menuName = "ProjectZero/Config/Crash Reporting")]
    public class CrashReportingConfig : ScriptableObject
    {
        [Header("Alert Dispatch")]
        [ValidateEmail("Critical QA alert email must be properly formatted (e.g. qa-leads@studio.com).",
            MessageType = InspectorMessageType.Error)]
        public string qaLeadEmail = "qa-leads@projectzero.com";

        [ValidateEmail("Engineering notification email is invalid.")]
        public string engineeringNotificationEmail = "bugs@projectzero.com";
    }
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ValidateNotNull]`** | High | Combine email format verification with non-empty string enforcement. |
| **`[ValidateStringLength]`** | High | Enforce minimum/maximum length constraints on email fields. |
| **`[BoxGroup]`** | High | Visualizes cleanly inside grouped network or settings cards. |
| **Validation Engine** | Native | Audited automatically during project-wide validation scans. |
