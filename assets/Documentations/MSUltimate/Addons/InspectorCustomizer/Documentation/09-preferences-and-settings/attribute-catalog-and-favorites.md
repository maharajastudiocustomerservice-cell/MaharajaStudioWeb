# Attribute Catalog & Favorites Manager

> **Module:** MSUltimate Inspector Customizer — Preferences & Settings  
> **Topic:** The Full Attribute Registry, Favorites, Custom Tags, and Target Scopes

---

## 1. The Attribute Catalog Browser

The **Catalog** tab in `InspectorCustomizerSettingsWindow` lists the complete reflection registry of all 454+ concrete MSUltimate attributes (463 total attribute classes) installed across Core and Addons:

```
┌────────────────────────────────────────────────────────────────────────┐
│  ATTRIBUTE CATALOG EXPLORER                                            │
│  🔍 Search catalog... (454+ Attributes Registered across Core & Addons)│
├──────────────────────┬─────────────────────────────────────────────────┤
│  MODULES             │  ProgressBar                                    │
│  • MSUltimate Core   │  Namespace: MaharajaStudio.MSUltimate.Runtime   │
│  • AnimatedAttributes│  Target Scopes: Field                           │
│  • ComponentDesigner │  AllowMultiple: False   Inherited: True         │
│  • HierarchyDesigner │  Parameters: min (float), max (float), color    │
│  • ValidationModule  │  [ ★ Favorite ]   [ View Documentation ]        │
│  • ToolBox-Vol1      │  ─────────────────────────────────────────────  │
│                      │  MinMaxSlider                                   │
│                      │  Namespace: MaharajaStudio.MSUltimate.Runtime   │
│                      │  Target Scopes: Field (Vector2 only)            │
└──────────────────────┴─────────────────────────────────────────────────┘
```

---

## 2. Managing Favorites, Recents & Usage Statistics

The attribute management pipeline is powered by `AttributeFavoritesManager` and persisted in developer `EditorPrefs`:

- **Starring Favorites (`★`):** Click the star icon next to any attribute in the catalog or in `AttributePickerWindow`. Starred attributes automatically populate the **Favorites** section at the top of the picker for instant 1-click addition (`EditorPrefs` key: `MSUltimate_Customizer_Favorites`).
- **Recent Attributes Tracking:** Automatically tracks the last 25 attributes selected or applied across any component, placing them into the **Recent** drawer for fast re-use (`EditorPrefs` key: `MSUltimate_Customizer_Recent`).
- **Usage Frequency Telemetry:** Tracks invocation counts for every attribute, surfacing your team's most frequently used attributes in the **Most Used** drawer (`EditorPrefs` key: `MSUltimate_Customizer_UsageCounts`).
- **Custom User Groups:** Organize attributes into studio-specific custom groups (e.g. "Combat HUD", "Vehicle Telemetry", "Level Design") stored under `MSUltimate_Customizer_Groups`.

---

## 3. Supported Member Scopes & Validation

The catalog displays the strict attribute contract for each entry:
- **`Target Scope`:** Displays whether the attribute is valid on `Field`, `Property`, `Method`, or `Class`.
- **`Type Constraints`:** Identifies any data type constraints (e.g. `[MinMaxSlider]` requires `Vector2`, `[AudioPreview]` requires `AudioClip`).
- **`Multiple Allowed`:** Indicates whether stacking multiple instances of the attribute on the same member is legal.
