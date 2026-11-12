# Member Scoping & Target Declarations

> **Module:** MSUltimate Inspector Customizer — Editor Windows  
> **Topic:** Styling Class Declarations, Serialized & Private Fields, Computed Properties, and Action Methods

---

## 1. Member Target Scopes Overview

Inspector Customizer supports decorating all four major C# member targets:

```
[Target Type]
   ├── 1. Class / Component Level   ──► [ComponentHeader], [ComponentBorder], [ComponentBackground]
   ├── 2. Fields                     ──► [ProgressBar], [Range], [MinMaxSlider], [ReadOnly]
   ├── 3. Properties                 ──► [ShowInInspector], [ComputedProperty]
   └── 4. Methods                    ──► [Button], [ButtonGroup], [IconButton]
```

---

## 2. Class & Component Level Declarations

Selecting **Component** at the top of the member list targets the `MonoBehaviour` or `ScriptableObject` class declaration itself (`AttributeTargets.Class`). This allows you to construct an authentic AAA component card frame without touching C# code:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  CLASS-LEVEL DECORATION PREVIEW                                                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ 🛡️ COMBAT SYSTEM                        [ Alpha 0.9 ]                            │  │
│  │ Advanced Weaponry & Ballistics Subsystem                                         │  │
│  ├──────────────────────────────────────────────────────────────────────────────────┤  │
│  │ (Component Body with Border Frame, Color Strip & Background Pattern)             │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Supported Component Designer Attributes
| Attribute | Primary Parameters | Visual Effect on Inspector |
| :--- | :--- | :--- |
| **`[ComponentHeader]`** | `Title`, `Subtitle`, `BackgroundColor` | Renders a styled top banner with title typography, description subtitle, and optional icon. |
| **`[ComponentBorder]`** | `Color`, `Width`, `Radius`, `Glow` | Wraps the entire inspector inside a styled border frame with rounded corners and optional glow. |
| **`[ComponentBadge]`** | `Label`, `BadgeColor`, `Alignment` | Displays a pill badge in the top-right corner (e.g. `"WIP"`, `"v1.2"`, `"Core Rig"`). |
| **`[ComponentColorStrip]`** | `Color`, `Edge`, `Thickness` | Adds a colored accent stripe along the left, top, right, or bottom edge of the component. |
| **`[ComponentBackground]`** | `Color`, `BorderRadius`, `Padding` | Applies a styled card background color and corner radius behind component fields. |

---

## 3. Fields: Serialized, Private Backing, and Inherited Fields

The **Fields** tab indexes all fields on the target type.

### 3.1 Public & `[SerializeField]` Fields
- Fields serialized by Unity appear immediately in the list.
- Can be decorated with any field-level presenter: `[ProgressBar]`, `[Range]`, `[MinMaxSlider]`, `[ColorWheel]`, `[EnumToggleButtons]`, `[FilePath]`, `[ReadOnly]`, or layout wrappers like `[BoxGroup]`.

### 3.2 Private Fields & Compiler Backing Fields
- By default, private fields without `[SerializeField]` are invisible in Unity's Inspector.
- In `InspectorCustomizerWindow`, click **`Scope ▼ > Fields > Private Fields`** or **`Compiler Backing Fields`**.
- Private fields and auto-property backing fields (e.g. `<MaxSpeed>k__BackingField`) appear in the list.
- Adding `[ShowInInspector]` and `[ReadOnly]` exposes them safely in the Inspector for edit-time telemetry and debugging without exposing them as public in code.

### 3.3 Inherited Fields from Base Classes
- Click **`Scope ▼ > Inheritance & Statics > Inherited Members`**.
- Fields declared on parent classes (e.g. `CharacterBase`, `VehicleCore`, `Entity`) appear in the member list with a subtle inherited pill badge.
- You can apply specialized attributes to inherited fields per derived class (e.g. styling `moveSpeed` differently on `TankHero` vs `ScoutHero`).

---

## 4. C# Properties (Getters & Setters)

Standard Unity Inspectors cannot display C# properties because Unity's serializer only serializes fields.

Inspector Customizer surfaces properties under the **Properties** tab:

```csharp
// Example Target Script
public class VehicleRig : MonoBehaviour
{
    private Rigidbody _rb;

    // Computed Read-Only Property
    public float CurrentSpeedKmh => _rb != null ? _rb.velocity.magnitude * 3.6f : 0f;

    // Auto-Property
    public int ActiveGear { get; set; } = 1;
}
```

### Visual Styling Workflow for Properties
1. Open `InspectorCustomizerWindow` and select the **Properties** tab.
2. Select `CurrentSpeedKmh`.
3. Add `[ShowInInspector]`.
4. Add `[ProgressBar(0f, 250f, SliderColor = "#FF8800")]`.
5. Add `[ReadOnly]`.
6. **Result in Unity Inspector:** `CurrentSpeedKmh` renders as a live, dynamic speed gauge that updates smoothly in Play Mode as the vehicle accelerates!

---

## 5. Methods & Interactive Debug Buttons

Parameterless `public` and `private` methods can be surfaced directly in the Inspector as interactive buttons:

```csharp
// Example Target Script
public class CombatDirector : MonoBehaviour
{
    public void ResetAllCooldowns() { /* ... */ }
    public void SpawnTestEnemy()     { /* ... */ }
    public void TriggerSuperNova()   { /* ... */ }
}
```

### 5.1 Single Buttons (`[Button]`)
- Select any method in the **Methods** tab.
- Add `[Button("Reset Cooldowns", ButtonHeight.Medium, ButtonColor = "#00CC66")]`.
- In the Unity Inspector, clicking this button invokes the method immediately in Edit Mode or Play Mode!

### 5.2 Button Groups (`[ButtonGroup]`)
To arrange multiple related action buttons horizontally side-by-side:
- Apply `[ButtonGroup("Combat Actions")]` to `ResetAllCooldowns()`.
- Apply `[ButtonGroup("Combat Actions")]` to `SpawnTestEnemy()`.
- Apply `[ButtonGroup("Combat Actions")]` to `TriggerSuperNova()`.
- **Result:** All three buttons arrange into a sleek, horizontal action toolbar at the bottom of the component!
