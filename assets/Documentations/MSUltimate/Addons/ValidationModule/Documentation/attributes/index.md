# Validation Module Attributes

> 39 specialized validation attributes safeguarding asset configurations, component dependencies, file existence, and numerical thresholds.

---

## Attribute Directory (39 Attributes)

| Attribute | Target | Description | Status |
| :--- | :--- | :--- | :---: |
| [**`[ValidateActiveState]`**](validate-active-state.md) | `Field` | Validates that a referenced GameObject or Component is active or inactive in the scene. | ✅ Complete |
| [**`[ValidateAnimatorParameter]`**](validate-animator-parameter.md) | `Field` | Validates that an assigned Animator contains a specific parameter name and type. | ✅ Complete |
| [**`[ValidateAssetExtension]`**](validate-asset-extension.md) | `Field` | Validates that a referenced asset matches a specific file extension (e.g. .png, .wav). | ✅ Complete |
| [**`[ValidateAssetPath]`**](validate-asset-path.md) | `Field` | Validates relative or absolute asset path exists in project database. | ✅ Complete |
| [**`[ValidateChildCount]`**](validate-child-count.md) | `Field` | Enforces minimum/maximum direct child count constraints on referenced GameObject. | ✅ Complete |
| [**`[ValidateChildHasComponent]`**](validate-child-has-component.md) | `Field` | Validates that children possess an attached component of the specified type. | ✅ Complete |
| [**`[ValidateChildName]`**](validate-child-name.md) | `Field` | Validates that child names conform to a pattern match condition (contains, prefix, regex). | ✅ Complete |
| [**`[ValidateChildTag]`**](validate-child-tag.md) | `Field` | Enforces that direct children carry a required Unity tag. | ✅ Complete |
| [**`[ValidateCollection]`**](validate-collection.md) | `Field` | Validates every element inside an array or list. | ✅ Complete |
| [**`[ValidateCompare]`**](validate-compare.md) | `Field` | Validates field value against another serialized field. | ✅ Complete |
| [**`[ValidateComponent]`**](validate-component.md) | `Field` | Verifies component presence and validity on target object. | ✅ Complete |
| [**`[ValidateCustom]`**](validate-custom.md) | `Field` | Validates a field using a custom boolean callback method. | ✅ Complete |
| [**`[ValidateEmail]`**](validate-email.md) | `Field` | Validates that a string is a properly formatted email address. | ✅ Complete |
| [**`[ValidateFilePath]`**](validate-file-path.md) | `Field` | Checks file path format and existence on OS filesystem. | ✅ Complete |
| [**`[ValidateFolder]`**](validate-folder.md) | `Field` | Validates that a string represents a valid, existing folder path. | ✅ Complete |
| [**`[ValidateHasMethod]`**](validate-has-method.md) | `Field` | Validates that a referenced object contains a method with the specified name. | ✅ Complete |
| [**`[ValidateHierarchyDepth]`**](validate-hierarchy-depth.md) | `Field` | Validates that hierarchy nesting depth falls within specified bounds. | ✅ Complete |
| [**`[ValidateIf]`**](validate-if.md) | `Field` | Conditionally evaluates validation rule only when predicate matches. | ✅ Complete |
| [**`[ValidateInFolder]`**](validate-in-folder.md) | `Field` | Enforces that target asset is located inside a designated project folder. | ✅ Complete |
| [**`[ValidateInterface]`**](validate-interface.md) | `Field` | Validates that a referenced object implements a specified interface. | ✅ Complete |
| [**`[ValidateIsPrefab]`**](validate-is-prefab.md) | `Field` | Validates that a referenced object is a project Prefab asset. | ✅ Complete |
| [**`[ValidateIsSceneObject]`**](validate-is-scene-object.md) | `Field` | Validates that a referenced object is a scene instance rather than a Prefab asset. | ✅ Complete |
| [**`[ValidateLayer]`**](validate-layer.md) | `Field` | Validates GameObject or layer mask against allowed layers. | ✅ Complete |
| [**`[ValidateNoParent]`**](validate-no-parent.md) | `Field` | Validates that a referenced GameObject is a root-level hierarchy object. | ✅ Complete |
| [**`[ValidateNotNull]`**](validate-not-null.md) | `Field` | Validates that a field is not null or empty. | ✅ Complete |
| [**`[ValidateParentName]`**](validate-parent-name.md) | `Field` | Validates that parent (or ancestor) GameObject name matches a specified pattern. | ✅ Complete |
| [**`[ValidateRange]`**](validate-range.md) | `Field` | Strict min/max range invariant guard with visual warning. | ✅ Complete |
| [**`[ValidateRegex]`**](validate-regex.md) | `Field` | Validates string structure against regex pattern. | ✅ Complete |
| [**`[ValidateRequiresParent]`**](validate-requires-parent.md) | `Field` | Enforces that object has a qualifying parent matching tag, name, or component. | ✅ Complete |
| [**`[ValidateSceneName]`**](validate-scene-name.md) | `Field` | Validates that a string matches an enabled scene in Build Settings. | ✅ Complete |
| [**`[ValidateSceneReference]`**](validate-scene-reference.md) | `Field` | Validates that a scene reference matches an entry in Build Settings. | ✅ Complete |
| [**`[ValidateSiblingCount]`**](validate-sibling-count.md) | `Field` | Validates that the number of siblings falls within specified bounds. | ✅ Complete |
| [**`[ValidateSiblingIndex]`**](validate-sibling-index.md) | `Field` | Validates that a referenced GameObject is at a specific sibling index. | ✅ Complete |
| [**`[ValidateStringLength]`**](validate-string-length.md) | `Field` | Enforces minimum and maximum string character length. | ✅ Complete |
| [**`[ValidateTag]`**](validate-tag.md) | `Field` | Validates that a string value represents a defined Unity tag. | ✅ Complete |
| [**`[ValidateTextureSize]`**](validate-texture-size.md) | `Field` | Validates texture dimensions and power-of-two constraints. | ✅ Complete |
| [**`[ValidateTransformReset]`**](validate-transform-reset.md) | `Field` | Validates that local position, rotation, and scale match identity values. | ✅ Complete |
| [**`[ValidateUniqueInHierarchy]`**](validate-unique-in-hierarchy.md) | `Field` | Validates that GameObject name is unique among its siblings. | ✅ Complete |
| [**`[ValidateUnless]`**](validate-unless.md) | `Field` | Bypasses validation rule when condition is met. | ✅ Complete |

