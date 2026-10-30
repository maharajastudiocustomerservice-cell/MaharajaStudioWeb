# [ShowCode]

> Extracts and renders the C# source code of methods or classes directly in the Inspector with syntax highlighting, line numbers, and dark-mode styling.

---

## 1. Overview & Value Proposition

**What it does:**
Displays the actual C# code of a method right inside the Inspector, complete with syntax highlighting and line numbers.

**The Problem:**
When designers or teammates are configuring components and click an inspector button, they often don't know what that method actually does under the hood. Opening Visual Studio or Rider just to read a 10-line calculation method breaks workflow and wastes time.

**The Solution:**
Add `[ShowCode]` above any method, class, struct, or interface:
- **Instant Code Snippet:** Reads the method directly from your script and displays it in a clean, syntax-highlighted box.
- **Line Numbers & Dark Theme:** Looks just like a code editor with colored keywords, strings, comments, and numbers.
- **Scrollable Box:** Large methods stay neat and tidy inside a max-height scrollable window.
- **Pair with Buttons:** Place it above a `[Button]` so team members can inspect the logic before hitting the trigger.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class DamageCalculator : MonoBehaviour
{
    [ShowCode("Formula Implementation")]
    public float CalculateCriticalHit(float baseDamage, float multiplier)
    {
        return baseDamage * multiplier + Random.Range(1f, 5f);
    }
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Class | AttributeTargets.Struct | AttributeTargets.Interface | AttributeTargets.Method` |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public ShowCodeAttribute()
public ShowCodeAttribute(string title)
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Title` | `string` | `null` | Header label displayed above the code block. Defaults to method name if null. |
| `TitleColor` | `string` | `"#cccccc"` | Hex color for the title text. |
| `ShowLineNumbers` | `bool` | `true` | Renders a left-hand line numbering gutter. |
| `LineNumberColor` | `string` | `"#858585"` | Hex color for line numbers. |
| `MaxHeight` | `float` | `300f` | Maximum container pixel height before enabling vertical scrolling. |
| `FontSize` | `float` | `12f` | Typography font size for the monospace code viewer. |
| `BackgroundColor` | `string` | `"#1e1e1e"` | VS Code style dark editor background hex color. |
| `KeywordColor` | `string` | `"#569cd6"` | C# language keywords syntax highlight color. |
| `StringColor` | `string` | `"#ce9178"` | String literals syntax highlight color. |
| `CommentColor` | `string` | `"#6a9955"` | Code comments syntax highlight color. |
| `NumberColor` | `string` | `"#b5cea8"` | Numeric constants syntax highlight color. |
| `MethodColor` | `string` | `"#dcdcaa"` | Method calls highlight color. |
| `RegularTextColor`| `string` | `"#d4d4d4"` | Standard code text color. |
| `BorderRadius` | `float` | `5f` | Corner rounding radius of the code block. |
| `BorderWidth` | `float` | `1f` | Border outline stroke thickness in pixels. |
| `BorderColor` | `string` | `"#333333"` | Hex color for the border outline. |
| `Padding` | `float` | `10f` | Internal padding in pixels. |
| `MarginTop` | `float` | `10f` | Spacing above code block in pixels. |
| `MarginBottom` | `float` | `10f` | Spacing below code block in pixels. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class EnemyBehaviorTree : MonoBehaviour
{
    [BoxGroup("AI Decision Logic", Box = true)]
    [ShowCode(
        title: "Aggro Distance Evaluation",
        MaxHeight = 220f,
        ShowLineNumbers = true
    )]
    [Button("Audition Aggro Check")]
    public bool CheckPlayerInRange(float distanceToTarget)
    {
        // 1. Evaluate line of sight
        if (distanceToTarget < 15f)
        {
            return true; // Target is in visual perimeter
        }
        return false;
    }
}
```

---

## 7. Stacking & Compatibility Matrix

- **Pairing with `[Button]`:** Renders the source snippet directly adjacent to or above the button trigger, allowing designers to review logic before executing it.
- **Suppression:** Can be overridden or suppressed at the member level using `[HideCode]`.
- **Performance:** Caches source extraction in editor memory so reflection is only performed once during asset compilation.
