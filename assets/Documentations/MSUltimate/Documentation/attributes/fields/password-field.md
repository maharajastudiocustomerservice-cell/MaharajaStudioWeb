# [PasswordField]

> Visually masks sensitive string fields with custom bullet characters and provides a 1-click eye button to reveal or conceal secrets.

---

## 1. Overview & Value Proposition

**What it does:**
Renders string fields as obfuscated password inputs in the Inspector. Replaces visible text with masking characters (default `•` or custom characters like `*`) and includes an interactive eye toggle button to reveal or hide the secret value on demand.

**The Problem:**
Game projects often contain API keys, backend server secrets, database access tokens, or live-service credentials inside serialized settings components or ScriptableObjects. When streaming on Discord, presenting at conferences, or recording tutorials, having these credentials displayed as plain text creates severe security risks.

**The Solution:**
Add `[PasswordField]` to any sensitive string field:
- **Automatic Character Masking:** Obfuscates text by default so shoulder-surfers or screen recordings cannot capture secrets.
- **Eye Reveal Toggle:** Click the inline eye icon to temporarily inspect or edit the raw string without navigating away.
- **Custom Mask Characters:** Supports custom masking symbols such as `*`, `#`, or standard bullets `•`.
- **Collection Compatible:** Implements `ICollectionElementAttribute` to protect lists and dictionaries of authentication keys.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class BackendConfig : MonoBehaviour
{
    [PasswordField]
    public string apiSecretKey = "sk_live_9384792384729384";
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
public PasswordFieldAttribute()
public PasswordFieldAttribute(char maskCharacter)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `maskCharacter` | `char` | `'•'` | The character displayed in place of actual string characters. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MaskCharacter` | `char` | `'•'` | Masking character used to hide the text. |
| `AllowReveal` | `bool` | `true` | If `true`, renders the eye toggle button allowing users to reveal the text. |
| `Height` | `float` | `22f` | Height of the password input field in pixels. |
| `BorderRadius` | `float` | `4f` | Corner radius of the input field border. |
| `BackgroundColor` | `string` | `""` | Custom hex background color for the text input box. |
| `TextColor` | `string` | `""` | Custom hex text color for the input field. |
| `Order` | `int` | `0` | Execution priority relative to other drawer attributes. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class LiveServiceCredentials : MonoBehaviour
{
    [Header("Server Gateway Authentication")]
    [PasswordField]
    public string primaryMasterKey = "prod_secret_8492048590";

    [Header("Strict Password (No Reveal Allowed)")]
    [PasswordField('*', AllowReveal = false)]
    public string databaseAdminPassword = "SuperSecurePassword123!";

    [Header("Credential Vault (Collection Elements)")]
    [PasswordField]
    public List<string> thirdPartyClientSecrets = new List<string>
    {
        "apple_auth_9482759",
        "google_play_0284759"
    };
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[BoxGroup]` | Supported | Functions cleanly inside credentials cards or security sections. |
| `[ShowIf]` | Supported | Conditionally reveals the password field based on login mode or environment toggles. |
| `[ReadOnly]` | Supported | Prevents editing while still allowing masking and optional eye toggle inspection. |
| `ICollectionElement` | Supported | Directly masks elements inside `List<string>` and `string[]`. |
