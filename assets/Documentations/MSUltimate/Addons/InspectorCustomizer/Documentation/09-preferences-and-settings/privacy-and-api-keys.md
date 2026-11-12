# Privacy Settings & API Key Isolation

> **Module:** MSUltimate Inspector Customizer — Preferences & Settings  
> **Topic:** Studio Privacy Shield, Local Key Isolation, Network Security, and Code Scrubbing

---

## 1. Studio Privacy Philosophy

Maharaja Studio designs tools for enterprise AAA and indie game studios alike. We believe that **developer privacy and code confidentiality must never be compromised** for AI tooling.

The **Privacy** tab inside `InspectorCustomizerSettingsWindow` manages the **Studio Privacy Shield**:

```
┌────────────────────────────────────────────────────────────────────────┐
│  PRIVACY & NETWORK SECURITY                                            │
│  🛡️ Studio Privacy Shield: ACTIVE                                      │
├────────────────────────────────────────────────────────────────────────┤
│  Key Storage Architecture:                                             │
│  [✓] Store Key in Local EditorPrefs (Machine-Specific, Never in Git)   │
│      Key Prefs: MSUltimate_AI_Key_{ProviderType}                       │
│                                                                        │
│  Metadata Extraction Safeguards:                                       │
│  [✓] Zero Source Code: Method bodies and algorithms are never read     │
│  [✓] Include Field Names & Types only                                  │
│  [✓] Exclusion Wildcards (m_*, _internal*, *BackingField)              │
│  [✓] Safety Member Cap (MaxMembersLimit: 120)                          │
│  [✓] Transparent Raw Payload Review before dispatch                    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Key Isolation & Storage Architecture

Developers can control how API keys are handled using the `Store Key in EditorPrefs` setting on each provider:

1. **Local EditorPrefs (`StoreKeyInEditorPrefs = true`, Default & Recommended):**
   - Keys are stored strictly in the local developer machine's operating system preferences via Unity `EditorPrefs` (`MSUltimate_AI_Key_{ProviderType}`).
   - The serialized `_apiKey` string inside the `AIProfile` asset on disk remains completely empty (`string.Empty`).
   - Pushing project changes or sharing branches across Git, GitHub, GitLab, or Perforce will **never** leak corporate or personal API keys.
2. **Serialized in AIProfile Asset (`StoreKeyInEditorPrefs = false`):**
   - The key is saved directly inside the `AIProfile.asset` file.
   - Intended exclusively for shared internal development environments where team members deliberately share a dedicated studio development API key without configuring it on each machine.

---

## 3. Data Transmission Safeguards

- **Zero Implementation Transmission:** The AI Decorator strictly never parses or transmits method bodies, physics loops, shaders, private mathematics, or gameplay algorithms. Only variable names, data types, and doc comments are extracted.
- **Granular Member Filters:** Inside the **Privacy** settings tab, developers can toggle exactly which member categories are allowed for extraction (Public Fields, Serialized Private Fields, Action Methods, Existing Attributes, Doc Comments).
- **Wildcard Ignored Patterns:** Exclude internal or compiler-generated variables using comma-separated patterns (e.g. `m_*, _internal*, *BackingField`).
- **Safety Max Members Cap:** Enforces a hard limit on total members extracted per component (default: `120`), guarding against runaway token consumption on monolithic classes.
- **Transparent JSON Review:** The **Raw Payload & Schema** tab in `AIDecoratorModalWindow` lets developers review the exact payload and prompt strings before dispatching any network request.
