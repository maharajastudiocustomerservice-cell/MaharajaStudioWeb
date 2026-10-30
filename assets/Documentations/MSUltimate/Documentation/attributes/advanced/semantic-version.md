# [SemanticVersion]

> Formats string fields into a compliant SemVer 2.0 controller with Major, Minor, and Patch stepper buttons, pre-release tags, and metadata support.

---

## 1. Overview & Value Proposition

**What it does:**
Turns a normal string field into a smart Semantic Versioning (SemVer 2.0) control with 1-click Major, Minor, and Patch increment buttons.

**The Problem:**
Typing game version numbers like `1.4.2-beta` into raw text boxes is messy and error-prone. Team members often type inconsistent formats (like `v1.2`, `1.2.0.1`, or `1.2-alpha`), which breaks automated build pipelines, save-game migrations, and server compatibility checks.

**The Solution:**
Add `[SemanticVersion]` above any version string field:
- **1-Click Version Bumping:** Click `+` on Major, Minor, or Patch to increment version numbers without typing.
- **Pre-Release Channels:** Choose tags like `-alpha`, `-beta`, or `-rc.1` from a clean dropdown.
- **Enforces SemVer 2.0:** Automatically guarantees that your version numbers follow proper industry standards.
- **Build Metadata:** Supports optional build numbers (e.g. `+build.42`) for production release tracking.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

public class GameBuildInfo : MonoBehaviour
{
    [SemanticVersion]
    public string clientVersion = "1.0.0";
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `AttributeTargets.Field | AttributeTargets.Property` |
| **Supported Types** | `string` |
| **Allow Multiple** | `false` |
| **Inherited** | `true` |
| **Interfaces** | `ICollectionElementAttribute` |
| **Build Overhead** | Editor-only (Zero runtime build overhead / stripped in builds) |
| **Minimum Unity** | Unity 6 (6000.x)+ |

---

## 4. Constructors & Signatures

```csharp
public SemanticVersionAttribute()
public SemanticVersionAttribute(bool allowPreRelease)
public SemanticVersionAttribute(bool allowPreRelease, string colorHex)
```

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `AllowPreRelease` | `bool` | `true` | Enables suffix tag selection (e.g. `-alpha`, `-beta`, `-rc.1`). |
| `AllowBuildMetadata`| `bool` | `false` | Enables build metadata tag support (`+build.204`). |
| `ShowDecrementButtons`| `bool` | `false` | Shows `-` decrement buttons alongside `+` increment steppers. |
| `ColorHex` | `string` | `null` | Custom accent hex color for stepper buttons and version badges. |
| `CustomLabel` | `string` | `null` | Overrides the field display label. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;

[CreateAssetMenu(fileName = "AppReleaseManifest", menuName = "Game/Release/App Manifest")]
public class AppReleaseManifest : ScriptableObject
{
    [BoxGroup("Release Metadata", Box = true)]
    [SemanticVersion(
        allowPreRelease: true, 
        colorHex: "#3498DB"
    )]
    [Tooltip("SemVer release identifier dispatched to matchmaking servers.")]
    public string clientAppVersion = "2.1.0-rc.1";

    [BoxGroup("Release Metadata")]
    public int internalBuildNumber = 1420;

    [BoxGroup("Release Metadata")]
    public bool forceClientUpdate = false;
}
```

---

## 7. Stacking & Compatibility Matrix

- **Grouping:** Pairs cleanly inside `[BoxGroup]` and `[VerticalGroup]`.
- **Validation:** Automatically validates string inputs against standard Semantic Versioning 2.0 specifications (`MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]`).
- **Persistence:** Serializes cleanly as a standard UTF-8 string, ensuring 100% compatibility with JSON serializers and remote config endpoints.
