# Reconciliation Engine & Safety Guarantees

> **Module:** MSUltimate Inspector Customizer — Code Baking  
> **Topic:** Safe AST Injection, Namespace Resolution, Git Preservation, and Undo Redo

---

## 1. Safe AST-Driven Source Injection

Rewriting source code files automatically carries the risk of damaging formatting, corrupting comments, or breaking existing code syntax.

`AttributeCodeBaker` utilizes an AST-inspired token scanner rather than blind text replacement:

- **Comment Preservation:** Doc comments (`/// <summary>`), inline comments (`//`), and block comments (`/* ... */`) are 100% preserved in their exact locations.
- **Indentation & Formatting Awareness:** Injected attributes automatically inherit the indentation level (tabs or spaces) of the declaring member.
- **Access Modifier Safety:** Attributes are strictly placed immediately above the target member declaration, below any existing preprocessor directives (`#if UNITY_EDITOR`).

---

## 2. Namespace & `using` Directive Auto-Import

MSUltimate attributes reside across several runtime namespaces:
- `MaharajaStudio.MSUltimate.Runtime` (Core attributes)
- `MaharajaStudio.MSUltimate.AnimatedAttributes` (Animated attributes)
- `MaharajaStudio.MSUltimate.ComponentDesigner` (Class stylers)
- `MaharajaStudio.MSUltimate.Validation` (Validation rules)

When baking code:
1. `AttributeCodeBaker` inspects the attribute types being injected.
2. It scans the top of the C# script for existing `using` directives.
3. If a required namespace is missing, it automatically inserts the clean `using` statement at the top of the file without creating duplicates.

---

## 3. Four-Tier Attribute Reconciliation

During the baking pass, every attribute undergoes a reconciliation evaluation defined by `AttributeBakeAction`:

```csharp
namespace MaharajaStudio.MSUltimate.InspectorCustomizer.Editor
{
    public enum AttributeBakeAction
    {
        Added,     // New attribute injected from profile
        Updated,   // Existing attribute updated with new parameter values
        Preserved, // Existing code attribute preserved without change
        Removed    // Attribute stripped in EditorOverride mode
    }
}
```

- **Non-MSUltimate Attributes:** Standard Unity attributes (`[SerializeField]`, `[HideInInspector]`, `[System.NonSerialized]`) are **always preserved** and never modified or stripped.
- **Third-Party Attributes:** Attributes from other packages (Odin, Photon, Mirror, etc.) are left completely intact unless explicitly targeted by an `AttributeReplacer` rule.

---

## 4. Git & Backup Safety

- **Atomic File Writing:** Modified files are written via temporary buffer streams. If a disk write error occurs, the original script is unaffected.
- **Unity Undo Support:** The file modification is recorded in Unity's `Undo` buffer (`Undo.RegisterCompleteObjectUndo`), allowing you to revert with `Ctrl+Z` before domain reload completes.
- **Clean Git Diffs:** Because whitespace and comments are preserved, Git diffs display only the clean single-line attribute injections, preventing merge conflicts across team branches.
