# Validation Attributes (Core)

> Core data integrity guards alerting developers to null references, broken assets, interface compliance, and invalid numeric thresholds directly in the Inspector.

---

## Attribute Directory (8 Attributes)
| Attribute | Target | Description | Status |
| :--- | :--- | :--- | :---: |
| [**`[ClampWarning]`**](clamp-warning.md) | `Field \| Property` | Non-intrusive warning box when numeric value falls outside soft range. | ✅ Complete |
| [**`[CompareWith]`**](compare-with.md) | `Field \| Property` | Compares numeric field against another field with relational badges. | ✅ Complete |
| [**`[ConfirmationDialog]`**](confirmation-dialog.md) | `Method \| Field \| Property` | Modal confirmation prompt dialog before executing destructive actions. | ✅ Complete |
| [**`[HighlightIfNull]`**](highlight-if-null.md) | `Field \| Property` | High-visibility colored border outline when object reference is null. | ✅ Complete |
| [**`[Required]`**](required.md) | `Field \| Property` | Mandatory reference guard with styled error callout if null or empty. | ✅ Complete |
| [**`[RequireInterface]`**](require-interface.md) | `Field \| Property` | Restricts Object field to components/assets implementing specific interface. | ✅ Complete |
| [**`[ValidateInput]`**](validate-input.md) | `Field \| Property` | Custom C# boolean method validation callback with configurable severity. | ✅ Complete |
| [**`[Validation]`**](validation.md) | `Class` | Foundational base class and pipeline assigner for all validation attributes. | ✅ Complete |

> **Note:** For deep scene-wide scanning, regex, layer masks, and automatic batch repair, see the [MSUltimate Validation Module Addon](../../../Addons/MSUltimate-ValidationModule/Documentation/index.md).
