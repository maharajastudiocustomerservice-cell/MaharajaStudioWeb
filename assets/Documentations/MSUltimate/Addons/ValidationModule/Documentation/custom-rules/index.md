# Custom Validation Rules Guide

> Guide to authoring custom validation rules, validators, and automated auto-fix scripts in C#.

---

## Authoring Custom Rules
- **Implementing `IValidationRule` / `IDeepValidationRule`:** Defining field-level attribute rules (`IValidationRule`) or project/GameObject-wide deep scan rules (`IDeepValidationRule`), error messages, and severity.
- **Registering Auto-Fix Actions:** Supplying 1-click repair delegates via `ValidationResult.FixAction`.
- **Integrating with CI / Command Line:** Running validation headless during automated builds via `ValidationCLI`.
