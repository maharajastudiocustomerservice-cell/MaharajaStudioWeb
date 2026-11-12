# AI Provider Setup & Studio Privacy Shield

> **Module:** MSUltimate Inspector Customizer — AI Decorator  
> **Topic:** Provider Setup (OpenAI, Claude, Gemini, Ollama, Groq, Mistral), Key Security, and Privacy Architecture

---

## 1. Supported AI Service Providers

Inspector Customizer includes native API connectors for 8 AI backends defined in `AIProviderType`:

```csharp
namespace MaharajaStudio.MSUltimate.InspectorCustomizer.Editor.AI
{
    public enum AIProviderType
    {
        OpenAI,        // GPT-4o, o1, o3-mini
        Anthropic,     // Claude 3.5 Sonnet, Claude 3 Opus
        Gemini,        // Gemini 1.5 Pro, 2.0 Flash
        Groq,          // Llama 3.3 70B (Ultra-low latency)
        Mistral,       // Mistral Large
        Ollama,        // Zero-cost offline local models (llama3.1, qwen2.5-coder)
        OpenRouter,    // Multi-provider proxy router
        Custom         // Enterprise self-hosted OpenAI-compatible endpoints
    }
}
```

---

## 2. Configuration Guide by Provider

To configure providers, open:  
**`Tools > Maharaja Studio > MSUltimate > Inspector Customizer > Inspector Customizer Settings`** $\rightarrow$ select **AI Profiles**.

### 2.1 OpenAI
- **Supported Models:** `gpt-4o` (Recommended), `gpt-4o-mini`, `o1`, `o3-mini`, `gpt-4-turbo`.
- **API Key Format:** `sk-proj-...`
- **Default Base URL:** `https://api.openai.com/v1`
- **Recommended Settings:** Temperature: `0.2`, Max Tokens: `4096`.

### 2.2 Anthropic (Claude)
- **Supported Models:** `claude-3-5-sonnet-20241022` (Recommended for complex layouts), `claude-3-5-haiku-20241022`, `claude-3-opus-20240229`.
- **API Key Format:** `sk-ant-api03-...`
- **Default Base URL:** `https://api.anthropic.com/v1`
- **Recommended Settings:** Temperature: `0.1`, Max Tokens: `4096`. Excellent understanding of visual hierarchy and color harmony.

### 2.3 Google Gemini
- **Supported Models:** `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-1.5-flash-8b`, `gemini-1.5-pro` (Recommended), `gemini-2.5-flash`.
- **API Key Format:** `AIzaSy...`
- **Default Base URL:** `https://generativelanguage.googleapis.com/v1beta`
- **Recommended Settings:** Temperature: `0.2`, Max Tokens: `8192`. High context window allowing large reference scripts and image mockups.

### 2.4 Groq (Ultra-Fast Inference)
- **Supported Models:** `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `mixtral-8x7b-32768`.
- **API Key Format:** `gsk_...`
- **Default Base URL:** `https://api.groq.com/openai/v1`
- **Speed:** Delivers complete inspector layouts in under 400 milliseconds.

### 2.5 Mistral AI
- **Supported Models:** `mistral-large-latest`, `mistral-small-latest`, `codestral-latest`.
- **API Key Format:** Bearer token string.
- **Default Base URL:** `https://api.mistral.ai/v1`

### 2.6 OpenRouter (Multi-Model Gateway)
- **Supported Models:** `anthropic/claude-3.5-sonnet`, `openai/gpt-4o-mini`, `meta-llama/llama-3.3-70b-instruct`, `google/gemini-2.0-flash-exp:free`.
- **API Key Format:** `sk-or-v1-...`
- **Default Base URL:** `https://openrouter.ai/api/v1`

### 2.7 Offline & Local LLMs (Ollama)
For confidential projects where game code cannot leave the local workstation:
1. Download and run [Ollama](https://ollama.ai).
2. Pull a coding model via terminal:
   ```bash
   ollama pull qwen2.5-coder
   # or
   ollama pull llama3.2
   ```
3. In Unity's **AI Profiles** tab:
   - Select Provider: **`Ollama`**.
   - Base URL: `http://localhost:11434/v1`.
   - Model Name: `qwen2.5-coder` or `llama3.2`.
   - API Key: *(Leave blank; Ollama runs locally without authentication).*
4. Click **Test Connection**. A green checkmark confirms offline communication.

### 2.8 Custom OpenAI-Compatible Endpoints
- **Supported Servers:** LM Studio, vLLM, LocalAI, Azure OpenAI proxy, or enterprise internal inference clusters.
- **Default Base URL:** `http://localhost:1234/v1`

---

## 3. The Studio Privacy Shield

Game studios operating under strict Non-Disclosure Agreements (NDAs) require guarantees that their proprietary game mechanics, algorithms, and intellectual property remain safe.

Inspector Customizer includes the multi-tier **Studio Privacy Shield**:

```
[Target C# Component]
         │
         ├───► Tier 1: Local Reflection Filtering
         │     • Method bodies, math formulas, update loops, and private
         │       algorithms are completely discarded.
         │     • Only member names, data types, and doc comments are parsed.
         │
         ├───► Tier 2: AST Schema Sanitization & Caps
         │     • Exclusion wildcards (m_*, _internal*, *BackingField).
         │     • Max members limit cap to prevent token explosion.
         │     • Optional parameter doc stripping to minimize payload size.
         │
         └───► Tier 3: Local Key Storage Isolation (Zero Git Leak Risk)
               • StoreKeyInEditorPrefs enabled by default.
               • API keys are stored in machine-specific EditorPrefs:
                 MSUltimate_AI_Key_{ProviderType}.
               • Key fields inside AIProfile assets on disk remain strictly empty!
```

### Privacy & Security Guarantees
1. **Zero Git Leak Risk:** When `StoreKeyInEditorPrefs` is enabled (the default), API keys are stored in your machine's local user `EditorPrefs` under `MSUltimate_AI_Key_{ProviderType}`. The serialized `_apiKey` field in the `AIProfile` asset on disk remains completely empty, ensuring you never commit secrets to GitHub, GitLab, or Perforce.
2. **Transparent Payload Review:** The **Raw Payload & Schema** tab in `AIDecoratorModalWindow` lets you inspect the exact JSON text being sent before any request is dispatched.
3. **No Training On Your Code:** Standard API endpoints (OpenAI, Anthropic, Gemini, Groq) with developer keys do not use API data to train public models. Local Ollama execution keeps 100% of data on your physical hardware.
