# Validation & Safety Attributes

> Structural sanity guards: layer collision matrices, missing script detection, naming convention enforcement, prefab override tracking, raycast audits, component requirement checks, and transform scale warnings.

---

## Attribute Directory (7 Attributes)

| Attribute | Target | Description | Status |
| :--- | :--- | :--- | :---: |
| [**`[HierarchyLayerCollisionMatrix]`**](hierarchy-layer-collision-matrix.md) | `Class` | Displays a compact hierarchy badge showing how many layers can physically collide with this object's layer. | ✅ Complete |
| [**`[HierarchyMissingScriptDetector]`**](hierarchy-missing-script-detector.md) | `Class` | Highlights GameObjects containing broken or missing MonoBehaviour scripts with a hazard warning badge. | ✅ Complete |
| [**`[HierarchyNamingConvention]`**](hierarchy-naming-convention.md) | `Class` | Enforces naming conventions (affixes, disallowed spaces) and displays an alert icon on violations. | ✅ Complete |
| [**`[HierarchyPrefabState]`**](hierarchy-prefab-state.md) | `Class` | Displays hierarchy indicators for Prefab variant depth, overridden property counts, and broken instances. | ✅ Complete |
| [**`[HierarchyRaycastAudit]`**](hierarchy-raycast-audit.md) | `Class` | Audits UI graphics for wasted raycasts and provides a one-click optimization fix directly in the hierarchy. | ✅ Complete |
| [**`[HierarchyRequirementCheck]`**](hierarchy-requirement-check.md) | `Class` | Validates required peer components on the same GameObject and displays an alert badge if missing. | ✅ Complete |
| [**`[HierarchyTransformWarning]`**](hierarchy-transform-warning.md) | `Class` | Displays an alert badge if the GameObject has non-uniform or negative scale values. | ✅ Complete |
