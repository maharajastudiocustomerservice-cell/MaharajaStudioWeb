# [ComponentHeaderMenu]

> Injects a compact dropdown action menu into the component header to invoke target methods without cluttering header space.

---

## 1. Overview & Value Proposition

**What it does:**
`[ComponentHeaderMenu]` condenses multiple utility commands into an elegant dropdown context menu embedded right inside the component header. Injected into `ComponentSlot.BeforeContent`, it displays a sleek menu button (`ButtonIcon = "⚙️"`, `"☰"`, or `"⋮"`). Clicking the button opens a popup list of actions (`MenuItems`) mapped one-to-one with corresponding MonoBehaviour methods (`MethodNames`), providing a rich suite of tools in minimal screen real estate.

**The Problem:**
Complex managers, simulation controllers, and procedural generators often require 5 to 10 distinct debug routines (e.g., "Reset Defaults", "Export JSON", "Clear Cache", "Dump Telemetry"). Rendering each one as a distinct button overcrowds the inspector header and pushes vital fields out of view.

**The Solution:**
Organizing component operations with `[ComponentHeaderMenu]`:
- **Space-Efficient Action Hub:** Consolidates unlimited administrative and debugging methods into a single compact header button.
- **Contextual Dropdown Navigation:** Uses native Unity popup menu workflows familiar to all game developers.
- **Customizable Menu Icons:** Configure gear wheels (`⚙️`), hamburger bars (`☰`), vertical ellipses (`⋮`), or wrench icons (`🔧`) to match interface conventions.
- **Reflection-Safe Method Binding:** Cleanly routes selected menu items directly to target instance methods without boilerplate editor scripts.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentHeaderMenu("⚙️", 
    new string[] { "Regenerate Grid", "Clear Terrain", "Export Heightmap" }, 
    new string[] { "RegenerateGrid", "ClearTerrain", "ExportHeightmap" })]
public class TerrainChunkGenerator : MonoBehaviour
{
    public int chunkSize = 64;
    public float heightScale = 25f;

    public void RegenerateGrid() => Debug.Log("Regenerating terrain chunk grid...");
    public void ClearTerrain() => Debug.Log("Clearing terrain data...");
    public void ExportHeightmap() => Debug.Log("Exporting heightmap texture...");
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate-ComponentDesigner Addon |
| **Attribute Target** | `Class` |
| **Inherited** | Yes |
| **Allow Multiple** | No (`AllowMultiple = false`) |
| **Component Slot** | `BeforeContent` |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public ComponentHeaderMenuAttribute()
public ComponentHeaderMenuAttribute(string buttonIcon, string[] menuItems, string[] methodNames)
```

- `buttonIcon`: Unicode glyph or emoji displayed on the menu button (e.g. `"⚙️"`, `"⋮"`, `"🛠️"`).
- `menuItems`: Array of human-readable labels displayed inside the dropdown menu list.
- `methodNames`: Array of method names on the target class matching each menu entry by index.

---

## 5. Properties & Customization Options

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ButtonIcon` | `string` | `"⚙️"` | Icon glyph or emoji representing the dropdown trigger button. |
| `MenuItems` | `string[]` | `new string[0]` | Array of human-readable labels shown in the dropdown menu. |
| `MethodNames` | `string[]` | `new string[0]` | Array of method names invoked when corresponding menu items are selected. |
| `Order` | `int` | `0` | Execution priority order used by the modular attribute framework. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.ComponentDesigner;

[ComponentBorder(Color = "#4F46E5", Width = 1.5f, Radius = 6f)]
[ComponentBackground("#0D1117", BorderRadius = 6f, Padding = 10f)]
[ComponentHeader("WORLD SAVE STATE CONTROLLER", Subtitle = "Persistence & Cloud Serialization Hub", BackgroundColor = "#161B22", TitleColor = "#E6EDF3")]
[ComponentHeaderMenu("⋮",
    new string[] { "Save Local Slot", "Load From Cloud", "Validate Integrity", "Wipe Save Data" },
    new string[] { "SaveLocalSlot", "LoadFromCloud", "ValidateIntegrity", "WipeSaveData" })]
public class WorldSaveStateController : MonoBehaviour
{
    [Header("Profile & Persistence")]
    public string activeProfileName = "Hero_Slot_01";
    public int totalPlaytimeSeconds = 84520;
    public bool isCloudSyncEnabled = true;

    public void SaveLocalSlot() => Debug.Log($"[SAVE] Local slot '{activeProfileName}' committed to disk.");
    public void LoadFromCloud() => Debug.Log($"[CLOUD] Fetching latest snapshot for '{activeProfileName}'...");
    public void ValidateIntegrity() => Debug.Log("[VERIFY] SHA-256 checksum verified successfully!");
    public void WipeSaveData() => Debug.LogWarning($"[WIPE] Save data for '{activeProfileName}' destroyed.");
}
```

---

## 7. Stacking & Compatibility Matrix

| Attribute System | Compatibility | Notes & Best Practices |
| :--- | :---: | :--- |
| **`[ComponentHeader]`** | High | Positions the dropdown trigger flush against the top-right header corner. |
| **`[ComponentHeaderButton]`** | High | Place high-frequency actions as direct buttons and rare/administrative actions inside the menu. |
| **`[ComponentPresetManager]`** | High | Complements preset managers by providing dedicated administrative submenus. |
| **Inspector Controls** | High | Dropdown menu selection does not cause inspector recreation or lose active field focus. |
