# AI Asset Architect

Scriptable Studio Pro includes a powerful **AI Asset Architect** that generates production-ready ScriptableObjects directly from text prompts. It is **context-aware**, meaning it generates data specific to the C# class you consistently work with.

## Overview

The AI system is built to handle the tedious part of data entry. It can:
- **Generate New Assets**: Create dozens of items, characters, or abilities from scratch.
- **Refine Existing Data**: Bulk-edit selected assets using natural language (e.g., "Nerf all fire weapons by 10%").
- **Understand Context**: It knows your game's name, theme, and global lore.
- **Self-Heal**: Automatically repairs invalid JSON responses from LLMs.

---

## 🚀 Getting Started

1. **Open Scriptable Studio Pro**: Go to `Asset > Scriptable Studio Pro` or `Tools > Maharaja Studio > Scriptable Studio Pro > Open Window`.
2. **Select a Type**: click on a ScriptableObject type in the left sidebar (e.g., `ItemData`).
3. **Launch AI**: Click the **AI Icon** in the main toolbar (usually next to the Duplicate button).
4. **Configure**: Select use the default profile or create a new one.
5. **Prompt**: Type a prompt (or leave it empty) and click **Generate Assets**.

---

## ⚙️ Configuration

### 1. Global Context
These settings apply to *all* generations across the project, helping the AI maintain consistency.
- **Game Name**: The name of your project.
- **Theme**: The genre or visual style (e.g., "Dark Fantasy", "Sci-Fi Horror").
- **Global Lore**: High-level rules or backstory.

### 2. AI Profiles
Profiles allow you to switch between different AI providers or configurations.

**To create a profile:**
Right-click in Project View and go to:
- `Create > Scriptable Studio Pro > AI > OpenAI > Standard Template`
- `Create > Scriptable Studio Pro > AI > Google Gemini > Standard Template`
- `Create > Scriptable Studio Pro > AI > Custom > Blank Template`
*(And other supported providers)*

**Profile Settings:**
- **Provider**: The AI service (OpenAI, Gemini, DeepSeek, etc.).
- **Model**: Specific model selection (e.g., GPT-4o, Gemini3 Pro).
- **System Prompt**: The "persona" of the AI.
- **Temperature**: 0.0 for strict data, 1.0 for creative variety.

---

## 🧠 Supported Providers

| Provider | Description | Best For |
| :--- | :--- | :--- |
| **OpenAI** | Industry standard (GPT-4o, GPT-3.5). | General purpose, high quality. |
| **Google Gemini** | Google's latest models (Gemini3 Pro/Flash). | Large context, creative writing. |
| **DeepSeek** | Powerful open weights models. | Logic and code-heavy data. |
| **Local LLM** | Connects to `localhost:1234` (LM Studio). | Privacy, free generation. |
| **Ollama** | Connects to `localhost:11434`. | Privacy, free generation. |
| **OpenRouter** | Access to Claude, Llama 3, etc. | flexible model choice. |

---

## 🛠️ Features & Workflow

### 1. Style Reference (Few-Shot Learning)
The AI Window includes a **Style Reference** section.
- **Drag & Drop**: Drag existing ScriptableObjects here to teach the AI your naming conventions and balance style.
- **Use Previous Outputs**: Toggle this to feed the last generated items back into the context, ensuring the next batch matches the previous one.

### 2. Refine Mode (Edit)
Instead of generating from scratch, you can **modify** existing assets.
1. **Select** specific rows in the Main Grid (or choose "All Instances" in the Refine Window).
2. Right-click or use the Toolbar to open **Refine Assets**.
3. **Lock Fields**: in the Refine Window, toggle "Lock" on fields you want to preserve (e.g., keep `Prefab` and `ID` unchanged).
4. **Prompt**: "Rename these to sound more Elvish" or "Double the prices".

### 3. Attribute Metadata
Control the AI directly from your C# code:

```csharp
[Header("Combat Stats")]
public int Health;

// 1. Give the AI a hint
[AIDescription("The amount of gold this monster drops. Bosses should drop 500+")]
public int GoldReward;

// 2. Hide a field from the AI interpretation entirely
[AIExclude] 
public string InternalGUID;
```

---

## 🔍 How It Works (Architecture)

1.  **Schema Generation**: The tool uses Reflection to build a JSON schema representing your C# class, including support for complex types like `AnimationCurve`, `Gradient`, `LayerMask`, and nested classes.
2.  **Context Injection**: It combines your Schema, Field Notes, Game Settings, and Style References into a single System Prompt.
3.  **Self-Healing**: If the AI returns invalid JSON, the tool catches the error and automatically sends a "repair request" back to the model.

---

## Troubleshooting

-   **"JSON Parse Error"**: The AI failed to follow the schema. Try lowering the **Temperature** or adding **Examples** to guide it.
-   **"Network Error"**: Check your API Key. For Local LLM/Ollama, ensure the server is running on the correct port.
-   **"Field Not Populated"**: Ensure the field is `public` or `[SerializeField]`.
