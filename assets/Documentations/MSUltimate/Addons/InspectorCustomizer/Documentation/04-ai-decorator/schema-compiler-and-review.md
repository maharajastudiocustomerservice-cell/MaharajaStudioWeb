# Schema Extraction & Layout Compilation

> **Module:** MSUltimate Inspector Customizer — AI Decorator  
> **Topic:** AST Schema Serialization, Token Budgeting, JSON Layout Compilation, and Verification

---

## 1. How AST Schema Extraction Works

Large Language Models perform poorly when fed raw, unformatted C# source files filled with thousands of lines of math formulas, update loops, and private algorithms.

To maximize accuracy and minimize token costs, `AISchemaExtractor` transforms the target component into a compact, token-efficient JSON schema representation:

```json
{
  "targetClass": "HeroController",
  "namespace": "Game.Characters",
  "baseType": "MonoBehaviour",
  "members": [
    {
      "name": "currentHealth",
      "type": "float",
      "scope": "field",
      "defaultValue": "100.0",
      "siblingCompanion": "maxHealth",
      "docSummary": "Current player hit points"
    },
    {
      "name": "RespawnPlayer",
      "type": "void",
      "scope": "method",
      "parameterCount": 0,
      "docSummary": "Resets health and moves player to spawn point"
    }
  ]
}
```

### Benefits of Schema Extraction
- **90% Token Reduction:** A 1,500-line C# file that would cost 6,000 tokens is condensed into a 250-token schema.
- **Privacy Enforcement:** Internal gameplay formulas are never parsed or sent.
- **Accurate Model Attention:** The model focuses purely on variables, data types, and companion relationships.

---

## 2. Layout Compilation (`AILayoutCompiler`)

Once the AI generates its response, `AILayoutCompiler` parses and verifies the JSON output:

```json
{
  "classOverrides": [
    {
      "attribute": "ComponentHeader",
      "parameters": { "title": "WARRIOR HERO", "color": "#FF3344" }
    }
  ],
  "memberOverrides": [
    {
      "memberName": "currentHealth",
      "attribute": "ProgressBar",
      "parameters": { "min": 0, "maxMember": "maxHealth", "color": "#33CC66" }
    },
    {
      "memberName": "RespawnPlayer",
      "attribute": "Button",
      "parameters": { "text": "Respawn", "height": "Medium" }
    }
  ]
}
```

### Compiler Verification Steps
1. **Type Safety Check:** Verifies that every recommended attribute actually exists in the MSUltimate assembly.
2. **Member Existency Check:** Ensures the AI did not hallucinate fields that do not exist on the target class.
3. **Type Compatibility Check:** Ensures attributes are valid for their target types (e.g. `[MinMaxSlider]` is only applied to `Vector2`).
4. **Parameter Parsing:** Converts raw string numbers and hex colors into validated `SerializedKVP` pairs.

---

## 3. Reviewing Payloads Before Execution

Inside `AIDecoratorModalWindow`, switch to the **Raw Payload & Schema** tab:
- **System Prompt:** View the exact system prompt being dispatched.
- **User Payload:** Review the extracted AST schema and user directives.
- **Token Estimate:** Check the estimated prompt and response token costs.
- You have complete transparency over what is sent across the network.
