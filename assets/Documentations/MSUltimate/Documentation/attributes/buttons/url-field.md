# [UrlField]

> Enhances string URL fields with a 1-click external browser launch button and URL validation.

---

## 1. Overview & Value Proposition

**What it does:**
Adds a 1-click "Open Link" button next to web URLs to open them directly in your default browser.

**The Problem:**
When storing web links in string fields (like documentation links, API URLs, bug tracker pages, or Discord server links), opening them in standard Unity requires manually selecting the text, copying it, opening your browser, and pasting the URL. If the link has a typo, you won't know until someone manually tests it.

**The Solution:**
Add `[UrlField]` above any `string` containing a website link:
- **1-Click Web Launch:** Click the button beside the field to launch the web page immediately.
- **Custom Button Labels & Colors:** Style the button text (e.g. "Read Wiki", "Join Discord"), background colors, hover highlights, and borders.
- **Link Validation:** Automatically verifies the URL format and warns you if the link is malformed or invalid.
- **Clean Inline Layout:** Keeps the text field and the launch button neatly aligned on the same row.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class SupportLinks : MonoBehaviour
{
    [UrlField(ButtonText = "Open Docs", ButtonColor = "#3498DB")]
    public string apiDocumentationUrl = "https://docs.maharajastudio.com";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `string`, `string[]`, `List<string>`, `SerializableDictionary<K, string>`, `SerializableNullable<string>` |
| **Collection Interface** | `ICollectionElementAttribute` (Automatic Element Cascading) |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public UrlFieldAttribute()
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ButtonText` | `string` | `"Open URL"` | Label text rendered on the browser launch button. |
| `Icon` | `string` | `""` | Built-in Unity icon name to display on the button. |
| `IconAlignment` | `IconAlignment`| `IconAlignment.Left`| Placement of icon relative to button text (`Left`, `Right`). |
| `ValidateUrl` | `bool` | `true` | Checks if string is a validly formatted URL before enabling. |
| `ButtonColor` | `string` | `""` | Hex background tint color for the button. |
| `HoverColor` | `string` | `""` | Hex color for button when hovered. |
| `TextColor` | `string` | `""` | Hex color for button text. |
| `ButtonWidth` | `float` | `80f` | Width in pixels of the launch button. |
| `ButtonHeight`| `float` | `20f` | Height in pixels of the launch button. |
| `BorderRadius`| `float` | `3f` | Corner rounding radius of the button frame in pixels. |
| `BorderWidth` | `float` | `0f` | Width of button border stroke in pixels. |
| `BorderColor` | `string` | `""` | Hex color for button border. |
| `HoverBorderColor` | `string` | `""` | Hex color for button border when hovered. |
| `MarginLeft` | `float` | `4f` | Spacing to the left of the button in pixels. |
| `MarginRight` | `float` | `0f` | Spacing to the right of the button in pixels. |
| `Tooltip` | `string` | `"Open URL in default browser"`| Tooltip text on button hover. |
| `ShowTextField`| `bool` | `true` | Whether the editable string text input is shown beside the button. |

---

## 6. Production-Grade Example

```csharp
using System.Collections.Generic;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class NetworkServerConfig : MonoBehaviour
{
    [BoxGroup("Cloud Services", Box = true)]
    [UrlField(
        ButtonText = "Live Dashboard",
        ButtonColor = "#2ECC71",
        ButtonWidth = 110f,
        ButtonHeight = 22f
    )]
    [Tooltip("Web URL linking directly to live cloud server telemetry.")]
    public string serverDashboardUrl = "https://analytics.gamecloud.com/live";

    [BoxGroup("Cloud Services")]
    [InfoBox("Direct collection cascading: [UrlField] cascades to each entry in string collections.")]
    [UrlField(ButtonText = "Open Endpoint", ButtonWidth = 100f, ButtonHeight = 20f, ButtonColor = "#0284C7")]
    public string[] publicApiGateways = new string[]
    {
        "https://api.gamecloud.com/v1",
        "https://auth.gamecloud.com/oauth"
    };

    [BoxGroup("Cloud Services")]
    [UrlField(ButtonText = "Read Docs", ButtonWidth = 85f, ButtonHeight = 20f, ButtonColor = "#4F46E5")]
    public List<string> developerResources = new List<string>
    {
        "https://docs.gamecloud.com/guides",
        "https://status.gamecloud.com"
    };
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Pairs seamlessly inside `[BoxGroup]` and `[VerticalGroup]`.
- **Validation:** Automatically checks URL protocols (`http://`, `https://`) and prefixes secure HTTPS protocol if omitted.
- **Safety:** Prompts standard OS security protocols before launching external system browsers.

### Collection Cascading Matrix

| Collection / Container Type | Cascading Support | Render Target | Notes |
| :--- | :---: | :--- | :--- |
| `string[]` | ✅ Yes | Individual array items | Each string element renders an "Open URL" button beside its input field. |
| `List<string>` | ✅ Yes | Individual list items | Renders dedicated URL launch buttons for all entries in the list. |
| `AdvancedList<string>` | ✅ Yes | Individual list items | Fully compatible with reordering and item manipulation. |
| `SerializableDictionary<K, string>` | ✅ Yes | Dictionary value column | Value column string displays open URL button. |
| `SerializableNullable<string>` | ✅ Yes | Inner string value | Active string value features URL launch button. |
| `SerializableTuple<..., string>` | ✅ Yes | Tuple string member | Renders button within tuple cell. |

