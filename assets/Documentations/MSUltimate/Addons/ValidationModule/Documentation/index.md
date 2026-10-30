# MSUltimate - Validation Module Documentation

> **Enterprise Project Sanity, Asset Integrity, and Automated 1-Click Fix Architecture.**
> Standalone Addon for Unity 6 (6000.x)+.

---

## Overview
MSUltimate Validation Module is a comprehensive QA and asset validation framework. Combining 39 specialized validation attributes with a project-wide batch scanning window and custom rule compiler, it catches errors before they reach QA or player builds.

## Systems & Sections
| Section | Type | Description | Index Link |
| :--- | :--- | :--- | :--- |
| **Validation Attributes** | C# Attributes | 39 attributes enforcing regex, file paths, layer masks, audio specs, texture formats, and dependencies. | [Browse 39 Attributes](attributes/index.md) |
| **Validation Engine Window**| Editor Window | Project-wide asset & scene scanner with 1-click batch autofix tools. | [Open Window Manual](tools/validation-engine/index.md) |
| **Custom Rule Pipeline** | C# Extensibility | Guide to creating custom validation rules and automated repair handlers. | [Open Developer Guide](custom-rules/index.md) |
