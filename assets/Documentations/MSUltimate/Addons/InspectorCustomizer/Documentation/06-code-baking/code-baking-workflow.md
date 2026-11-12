# Code Baking Workflow & Permanent Injection

> **Module:** MSUltimate Inspector Customizer — Code Baking  
> **Topic:** Transitioning from Virtual Overrides to Version-Controlled C# Source Code

---

## 1. Why Bake to Code?

While virtual profiles (`InspectorProfile`) are ideal for rapid visual iteration without triggering script recompilation, production workflows frequently require inspector styling to be permanent in C# source code:

1. **Source Control Tracking (Git / Perforce / PlasticSCM):** Visual diffs of attributes are visible directly in pull requests alongside gameplay changes.
2. **Zero-Dependency Package Exports:** Exportable as standalone `.unitypackage` or UPM packages that can be used by third-party buyers or other teams who do not have `MSUltimate-InspectorCustomizer` installed.
3. **IDE Code Navigation:** Attributes are visible directly in Visual Studio, Rider, and VS Code for code-completion and refactoring.

**Code Baking** bridges this gap by permanently writing your virtual attribute configurations into your C# script source files using AST-inspired token replacement.

---

## 2. Before & After Code Baking Walkthrough

Here is a concrete real-world comparison of a gameplay script before and after executing **Bake to Code**:

### 2.1 Before Baking: Plain C# Script
```csharp
using System;
using UnityEngine;

namespace Game.Characters
{
    /// <summary>
    /// Controls player combat stats and death logic.
    /// </summary>
    public class HeroController : MonoBehaviour
    {
        public float currentHealth = 100f;
        public float maxHealth = 100f;
        public float moveSpeed = 6.5f;

        [SerializeField] private bool _hasShield = true;
        [SerializeField] private float _shieldCapacity = 50f;

        public void RespawnPlayer()
        {
            currentHealth = maxHealth;
            Debug.Log("Player respawned!");
        }
    }
}
```

### 2.2 After Baking: Fully Decorated C# Script
```csharp
using System;
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;          // Auto-injected namespace
using MaharajaStudio.MSUltimate.ComponentDesigner;// Auto-injected namespace

namespace Game.Characters
{
    /// <summary>
    /// Controls player combat stats and death logic.
    /// </summary>
    [ComponentHeader("WARRIOR HERO", Subtitle = "Player Combat & Health System", BackgroundColor = "#FF3344")]
    [ComponentBorder(Color = "#4FC3F7", Radius = 8f, Glow = true)]
    public class HeroController : MonoBehaviour
    {
        [BoxGroup("Vitality Telemetry")]
        [ProgressBar(0f, 100f, ColorHex = "#33CC66", DynamicMaxValueMember = "maxHealth")]
        [Tooltip("Current hit points of the character")]
        public float currentHealth = 100f;

        [BoxGroup("Vitality Telemetry")]
        [ReadOnly]
        public float maxHealth = 100f;

        [BoxGroup("Locomotion")]
        [Range(0f, 20f)]
        public float moveSpeed = 6.5f;

        [BoxGroup("Defensive Shield")]
        [SerializeField] private bool _hasShield = true;

        [BoxGroup("Defensive Shield")]
        [ShowIf("_hasShield")]
        [ProgressBar(0f, 100f, ColorHex = "#00AAFF")]
        [SerializeField] private float _shieldCapacity = 50f;

        [Button("Respawn Player", BackgroundColor = "#00CC66", Height = 30)]
        public void RespawnPlayer()
        {
            currentHealth = maxHealth;
            Debug.Log("Player respawned!");
        }
    }
}
```

---

## 3. The 3-Step Baking Execution Pipeline

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Developer
    participant Win as InspectorCustomizerWindow
    participant Baker as AttributeCodeBaker
    participant Preview as BakeCodePreviewWindow
    participant Disk as Local FileSystem
    participant Unity as Unity AssetDatabase

    Dev->>Win: Click 'Bake to Code'
    Win->>Baker: Generate BakeAnalysisReport(TargetType, ProfileEntry)
    Baker->>Baker: Parse C# AST, reconcile attributes (Added, Updated, Preserved)
    Baker-->>Preview: Pass Reconciled Report & Syntax Tree
    Preview-->>Dev: Display Interactive Code Diff & Line Numbers
    Dev->>Preview: Confirm Baking & Select Override Mode (Both / Override)
    Preview->>Disk: Atomically write modified file with proper indentation
    Preview->>Unity: AssetDatabase.ImportAsset() & Trigger Compilation
    Unity-->>Dev: Compilation complete; inspector now driven natively by C#!
```

---

## 4. Preservation & Safety Standards

`AttributeCodeBaker` enforces strict code safety rules:
- **Comments Preserved:** XML doc comments (`/// <summary>`), inline comments (`//`), and block comments (`/* ... */`) are never altered or shifted.
- **Indentation Matched:** Automatically detects whether your project uses tabs or 4 spaces and indents all injected attributes identically to their target members.
- **Existing Attributes Respected:** Standard Unity attributes (`[SerializeField]`, `[HideInInspector]`) and third-party attributes (Odin, Photon, etc.) are **always preserved**.
- **Undo Integration:** The file write operation is recorded in Unity's `Undo` system (`Ctrl+Z`), allowing developers to reverse changes before script compilation finishes.
