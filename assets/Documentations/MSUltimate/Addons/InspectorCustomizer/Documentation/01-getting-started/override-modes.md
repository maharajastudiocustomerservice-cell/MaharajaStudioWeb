# Override Modes & Precedence Resolution

> **Module:** MSUltimate Inspector Customizer — Getting Started  
> **Topic:** The Three Override Modes, Conflict Handling, and Inheritance Rules

---

## 1. Overview of the Three Modes

Every component entry inside an `InspectorProfile` can operate in one of three distinct modes defined by `InspectorOverrideMode`:

```csharp
namespace MaharajaStudio.MSUltimate.InspectorCustomizer
{
    public enum InspectorOverrideMode
    {
        EditorOverride,
        CodeOnly,
        Both
    }
}
```

You can toggle the mode at any time using the mode dropdown in the top toolbar of `InspectorCustomizerWindow` or `BakeCodePreviewWindow`.

---

## 2. Detailed Behavior of Each Mode

| Mode | Source Code Attributes | Profile Virtual Overrides | Conflict Winner | Best Used For |
| :--- | :---: | :---: | :---: | :--- |
| **`Both`** *(Default)* | ✅ Active | ✅ Active | **Profile Wins** | Production teams where developers author basic attributes in code, and designers polish visual styles and grouping in Customizer. |
| **`EditorOverride`** | ❌ Ignored | ✅ Active | **Profile Only** | Total inspector redesigns where legacy or third-party code attributes must be completely suppressed without altering packages. |
| **`CodeOnly`** | ✅ Active | ❌ Bypassed | **Code Only** | Debugging or testing the pure raw C# inspector without deleting your profile data. |

---

## 3. Precedence & Conflict Resolution Rules

When running in **`Both`** mode, multiple sources can declare attributes on the same member. MSUltimate resolves conflicts using a deterministic 4-tier precedence hierarchy:

```
[Highest Priority]
       ▲
       │  1. Profile Override (Specific Member & Value)
       │  2. Profile Grouping Override (Wrap in BoxGroup / Foldout)
       │  3. Code-Declared Modular Attribute ([ProgressBar], [Range])
       │  4. Unity Built-in Decorator ([Header], [Space], [Tooltip])
       │
[Lowest Priority]
```

### Conflict Scenarios

#### Scenario 1: Same Attribute Type on the Same Field
- **Code declares:** `[Range(0f, 10f)] public float speed;`
- **Profile declares:** `Range(0f, 100f)`
- **Resolution:** The profile value takes precedence (`0f to 100f`). The code attribute is suppressed.

#### Scenario 2: Complementary Attributes on the Same Field
- **Code declares:** `[ReadOnly] public int score;`
- **Profile declares:** `[ProgressBar(0, 1000, "#00FF00")]`
- **Resolution:** Both attributes stack! The member is drawn as a read-only progress bar.

#### Scenario 3: Class-Level Header Conflicts
- **Code declares:** `[ComponentHeader("Old Title")]`
- **Profile declares:** `[ComponentHeader("Enhanced HUD", "#FF5500")]`
- **Resolution:** The profile `[ComponentHeader]` replaces the code header entirely.

---

## 4. Switching Modes Dynamically

You can switch modes without data loss:
- Switching from `Both` to `CodeOnly` temporarily deactivates profile styling in the Inspector while preserving all your configured cards in the profile asset.
- Switching to `EditorOverride` allows you to test clean-room visual redesigns of complex legacy components.
