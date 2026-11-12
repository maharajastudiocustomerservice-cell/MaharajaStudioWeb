# Component Exclusion & Ignore Rules

> **Module:** MSUltimate Inspector Customizer — Component Defaults  
> **Topic:** The Ignore Rules Engine, Filtering Criteria, Out-of-the-Box Rules, and Live Verification

---

## 1. Why Ignore Rules Are Essential

Applying global component defaults project-wide (such as wrapping components in a branded card or adding a stylized header) is powerful for creating visual cohesion. However, **you must never apply custom card styling to engine internals or third-party packages**:
- Unity built-in components (`Transform`, `MeshRenderer`, `Camera`, `AudioSource`, `Rigidbody`).
- Engine GUI & UI Toolkit classes (`VisualElement`, `EditorWindow`, `ScriptableWizard`).
- Third-party packages (TextMeshPro, Cinemachine, Addressables, Photon, Mirror, FMOD).
- Unit test mocks and test runners (`*Test*`, `*Benchmark*`).

The **Component Ignore Rules Engine** provides a multi-condition gate that evaluates every inspected component and safely bypasses global styling if any active ignore rule matches.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  CARD 3: COMPONENT IGNORE RULES ENGINE                                                 │
│  Active Rules: 7 Enabled / 0 Disabled                                                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────────────────────────────┐ │
│  │ [✓] Rule 1: Ignore TextMeshPro package components                                 │ │
│  │     Type: Namespace | Match: StartsWith | Pattern: 'TMPro'                        │ │
│  └───────────────────────────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐ │
│  │ [✓] Rule 2: Built-in Unity engine classes                                         │ │
│  │     Type: Namespace | Match: StartsWith | Pattern: 'UnityEngine'                  │ │
│  └───────────────────────────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐ │
│  │ [✓] Rule 3: Unity Editor internal classes                                         │ │
│  │     Type: Namespace | Match: StartsWith | Pattern: 'UnityEditor'                    │ │
│  └───────────────────────────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐ │
│  │ [✓] Rule 4: System standard library classes                                       │ │
│  │     Type: Namespace | Match: StartsWith | Pattern: 'System'                         │ │
│  └───────────────────────────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐ │
│  │ [✓] Rule 5: Explicit developer opt-out attribute                                  │ │
│  │     Type: AttributePresent | Match: Exact | Pattern: 'NoDefaultAttributes'         │ │
│  └───────────────────────────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐ │
│  │ [✓] Rule 6: Unity package assemblies                                              │ │
│  │     Type: AssemblyName | Match: StartsWith | Pattern: 'Unity.'                    │ │
│  └───────────────────────────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐ │
│  │ [✓] Rule 7: Core runtime library                                                  │ │
│  │     Type: AssemblyName | Match: StartsWith | Pattern: 'mscorlib'                  │ │
│  └───────────────────────────────────────────────────────────────────────────────────┘ │
│  [ + Add New Ignore Rule ]                                                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  CARD 4: LIVE COMPONENT RULE VERIFIER                                                  │
│  Test Slot: [ Drag any GameObject or Component here ]                                  │
│  Result: 🛡️ IGNORED (Matches Rule 2: Built-in Unity engine classes)                     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Supported Ignore Rule Criteria

Each rule evaluates components against criteria defined by `ComponentIgnoreRuleType` paired with `RuleMatchMode` and `ComponentTargetScope`:

### Rule Types (`ComponentIgnoreRuleType`)
| Filter Type | Matching Mechanism | Practical Example in Game Development |
| :--- | :--- | :--- |
| **`Namespace`** | Evaluates the declaring namespace of the component type. | Prefix `TMPro`, `Cinemachine`, `UnityEngine` skips external/package classes. |
| **`AssemblyName`** | Evaluates the compiling assembly definition name (.asmdef). | Assembly prefix `Unity.` or `mscorlib` skips engine packages. |
| **`BaseType`** | Checks whether target type directly inherits from a specific base type. | Type `EditorWindow` or `ScriptableWizard` skips all developer editor windows. |
| **`DerivedFromClass`**| Checks whether target type derives anywhere down an inheritance tree. | Base `NetworkBehaviour` or `EntityComponent` targets specialized trees. |
| **`SpecificType`** | Exact match on a fully qualified class name. | Excludes a single specialized class like `GameBootstrapDirector`. |
| **`AttributePresent`** | Skips if the class is decorated with a specific attribute. | Attribute `NoDefaultAttributes` provides an explicit 1-line opt-out. |
| **`ScriptPath`** | Checks file path of the underlying `.cs` MonoScript asset. | Path containing `/ThirdParty/` or `/Plugins/` bypasses imported assets. |
| **`HasAnyMSUltimateAttribute`**| Checks if class already has explicit MSUltimate attributes in code. | Prevents overriding scripts developers have already styled by hand. |

### Match Modes (`RuleMatchMode`)
- **`StartsWith`:** Matches if identifier starts with pattern (e.g. `TMPro`).
- **`Exact`:** Strict full string comparison.
- **`Contains`:** Matches if pattern appears anywhere in identifier.
- **`Wildcard`:** Supports asterisks (e.g. `*Test*` or `*Director`).

### Target Scopes (`ComponentTargetScope`)
- **`Both`:** Evaluates MonoBehaviours and ScriptableObjects.
- **`MonoBehavioursOnly`:** Evaluates only scene and prefab MonoBehaviour components.
- **`ScriptableObjectsOnly`:** Evaluates only ScriptableObject data assets.

---

## 3. Pre-Configured Out-of-the-Box Ignore Rules

When Inspector Customizer is first loaded, `InspectorCustomizerSettings.SetupDefaultIgnoreRules()` initializes with 7 protective ignore rules:

1. **TextMeshPro Package:** `Namespace StartsWith "TMPro"` — Prevents UI components from receiving game card styling.
2. **Unity Engine Internals:** `Namespace StartsWith "UnityEngine"` — Excludes `Transform`, `Camera`, `Collider`, `MeshRenderer`, etc.
3. **Unity Editor Internals:** `Namespace StartsWith "UnityEditor"` — Excludes editor inspectors, drawers, and windows.
4. **System Library:** `Namespace StartsWith "System"` — Excludes .NET framework and standard library classes.
5. **Developer Opt-Out Attribute:** `AttributePresent Exact "NoDefaultAttributes"` — Bypasses any class carrying `[NoDefaultAttributes]`.
6. **Unity Package Assemblies:** `AssemblyName StartsWith "Unity."` — Excludes official UPM packages in `PackageCache`.
7. **Core Runtime Library:** `AssemblyName StartsWith "mscorlib"` — Excludes base runtime primitives.

---

## 4. The Live Component Rule Verifier

Testing rule regular expressions or inheritance hierarchies manually can be error-prone. The **Live Component Rule Verifier** at the bottom of the window provides real-time verification:

### Testing Scenario 1: Native Engine Component
1. Drag the `Main Camera` GameObject into the Test Slot.
2. The verifier instantly displays:
   - **Status Badge:** `🛡️ IGNORED` (Red).
   - **Matched Rule:** `Rule 1: Unity Core Internals (Matched Namespace: 'UnityEngine.Camera')`.
   - **Reason:** Camera is safely excluded; default card headers will not draw.

### Testing Scenario 2: Gameplay Script
1. Drag your `PlayerMotor` script into the Test Slot.
2. The verifier instantly displays:
   - **Status Badge:** `✅ ALLOWED` (Green).
   - **Matched Rule:** `None (No active ignore rules matched)`.
   - **Reason:** `PlayerMotor` will receive all configured global default attributes automatically.
