# Global Component Defaults Manager

> **Module:** MSUltimate Inspector Customizer — Component Defaults  
> **Topic:** Project-Wide Automatic Component Styling, Master Safety Controls, and Global Themes

---

## 1. What Are Global Component Defaults?

In large projects with hundreds of components, manually styling every single script with headers and cards is impractical.

The **Component Defaults & Rules** window (`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Component Defaults & Rules`) allows developers to configure **Global Default Attributes** that automatically style *every* MonoBehaviour or ScriptableObject across your entire project:

```
┌────────────────────────────────────────────────────────────────────────┐
│  Component Defaults & Rules                                            │
│  🎯 Active Defaults: 2   🛡️ Active Ignore Rules: 7   ● System Active    │
├────────────────────────────────────────────────────────────────────────┤
│  CARD 1: ⚡ MASTER ACTIVATION & SCOPE                                   │
│  [✓] Enable Default Component Attributes (Master Switch)               │
│  Scope: [✓] Apply to MonoBehaviours   [✓] Apply to ScriptableObjects   │
│  SAFETY GUARDS & PRECAUTIONS:                                          │
│  [✓] Ignore Unity Built-Ins (UnityEngine.*, UnityEditor.*)             │
│  [✓] Ignore UPM Package Assemblies (Unity.*)                           │
│  [✓] Ignore Abstract Base Classes                                      │
│  ℹ Classes with [NoDefaultAttributes] are automatically excluded.       │
├────────────────────────────────────────────────────────────────────────┤
│  CARD 2: GLOBAL DEFAULT ATTRIBUTES DECK                                │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │ ☰ [ComponentHeader("{Name}", "Auto-Styled Component", "#2A2A3E")] │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │ ☰ [ComponentBorder(Color = "#3388FF", Radius = 6f)]               │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│  [ + Add Default Attribute ]                                           │
├────────────────────────────────────────────────────────────────────────┤
│  CARD 3: GRANULAR IGNORE RULES ENGINE (7 Active Rules)                 │
│  [ + Add New Ignore Rule ]                                             │
├────────────────────────────────────────────────────────────────────────┤
│  CARD 4: LIVE COMPONENT RULE TESTER                                    │
│  Test Slot: [ Drag any GameObject or Component here ]                  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Master Controls & Safety Guards

To protect engine internals, third-party packages, and developer tooling, the Master Activation & Scope card provides granular safety controls:

| Master Setting / Safety Guard | Field in Settings | Purpose & Default Behavior |
| :--- | :--- | :--- |
| **`Enable Default Component Attributes`** | `EnableDefaultComponentAttributes` | Master project-wide switch for automatic default styling. Default: `true`. |
| **`Apply to MonoBehaviours`** | `DefaultApplyToMonoBehaviours` | Applies active default attributes to scene and prefab `MonoBehaviour` instances. Default: `true`. |
| **`Apply to ScriptableObjects`** | `DefaultApplyToScriptableObjects` | Applies active default attributes to `ScriptableObject` data assets. Default: `true`. |
| **`Ignore Unity Built-Ins`** | `DefaultIgnoreUnityBuiltIns` | Safely excludes `Transform`, `Camera`, `Rigidbody`, and all engine classes under `UnityEngine.*` and `UnityEditor.*`. Default: `true`. |
| **`Ignore UPM Package Assemblies`** | `DefaultIgnorePackageAssemblies` | Excludes official Unity packages and third-party UPM packages in `PackageCache` matching `Unity.*`. Default: `true`. |
| **`Ignore Abstract Base Classes`** | `DefaultIgnoreAbstractClasses` | Prevents injecting default attributes onto abstract base classes. Default: `true`. |
| **`[NoDefaultAttributes] Opt-Out`**| Contract Attribute | Any class decorated with `[NoDefaultAttributes]` in code is permanently bypassed by the default engine. |

---

## 3. Configuring Default Attributes

You can attach any class-level styling attribute from `MSUltimate-ComponentDesigner` or `MSUltimate Core`:

1. Click **`+ Add Default Attribute`**.
2. Select an attribute (e.g. `ComponentHeader`, `ComponentBorder`, `ComponentColorStrip`, or `ComponentBackground`).
3. Set your parameters (e.g. `Color = "#3388FF"`, `Radius = 6`).
4. Parameter strings support dynamic tokens like `{Name}` to automatically display the class name in the header.
5. **Result:** Every component inspected in your project instantly displays a unified, beautiful AAA card header and frame!
