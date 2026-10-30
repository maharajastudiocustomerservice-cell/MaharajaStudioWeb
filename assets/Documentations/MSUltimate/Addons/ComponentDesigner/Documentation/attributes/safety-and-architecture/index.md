# Safety & Architecture Attributes

> Developer governance tools: deprecation banners, inspector locks, and scene singleton validators.

---

## Attribute Directory (3 Attributes)
| Attribute | Target | Description | Status |
| :--- | :--- | :--- | :---: |
| [**`[ComponentDeprecated]`**](component-deprecated.md) | `Class` | Obsolete warning or error banner above the inspector indicating replacement types. | ✅ Complete |
| [**`[ComponentLock]`**](component-lock.md) | `Class` | Header padlock toggle that locks all inspector fields into read-only mode. | ✅ Complete |
| [**`[ComponentSingleton]`**](component-singleton.md) | `Class` | Validates that only one instance exists in the active scene and warns of duplicates. | ✅ Complete |
