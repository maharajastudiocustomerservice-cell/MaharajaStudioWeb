# Setting Up MT Providers

Scriptable Studio Pro's Machine Translation system supports multiple translation services. This guide explains how to configure profiles for each supported provider.

To start, you must create an MT Profile:
1. In your **Project** window, right-click inside a folder.
2. Select **Create > Scriptable Studio Pro > MT > Translation Profile**.
3. Select the newly created asset and open **Settings > MT Services** to edit it.

## DeepL

DeepL provides highly accurate translations and offers both a Free API and a Pro API tier.

1. **Provider**: Select `DeepL`.
2. **Apply Defaults**: Click the **Apply Defaults** button. This will automatically fill the correct Base URL.
3. **API Key**: Enter your DeepL Authentication Key. You can find this in your DeepL account dashboard under the "API Keys" section.
4. **DeepL Free Api**: If you are using the free tier (`DeepL API Free`), leave this toggle **enabled**. If you are paying for DeepL Pro, disable this toggle so the system targets the Pro endpoint.
5. **Batching**: DeepL supports batching. You can safely leave **Batch Requests** enabled.

## Google Cloud Translation (V2)

Google Cloud offers a robust translation API that supports over 100 languages.

1. **Provider**: Select `GoogleCloudV2`.
2. **Apply Defaults**: Click the **Apply Defaults** button to set the Google APIs endpoint.
3. **API Key**: Enter your Google Cloud API Key. 
   - You must generate this key in the Google Cloud Console. Ensure that the **Cloud Translation API** is enabled for your project and your API key has access to it.
4. **Batching**: Google Cloud V2 does not natively support large JSON batch arrays in the same way Azure does, but the tool will format requests appropriately if batching is enabled.

## Azure Translator (Cognitive Services)

Azure Translator is highly scalable and supports multiple translation text nodes in a single request.

1. **Provider**: Select `AzureTranslator`.
2. **Apply Defaults**: Click the **Apply Defaults** button.
3. **API Key**: Enter your Azure Ocp-Apim-Subscription-Key.
4. **Azure Region**: Azure requires you to specify the region where your resource was created (e.g., `eastus`, `westeurope`). Enter the region code exactly as it appears in your Azure Portal.
5. **Batching**: Azure is highly optimized for batch requests. Keep **Batch Requests** enabled for the best performance.

## LibreTranslate

LibreTranslate is an open-source, self-hostable translation API. It is completely free if you host it yourself, making it perfect for unlimited offline translations without API costs.

### Hosting Locally with Docker (Recommended)

To run LibreTranslate locally on your machine for free, you can use Docker. To make it extremely easy to start your local server, you can create a simple batch script anywhere on your computer (e.g., `C:\CustomAI\LibreTranslate\start.bat`).

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and ensure it is running.
2. Create a new text file and rename it to `start.bat`.
3. Paste the following code into the file and save:

```bat
@echo off
title LibreTranslate Local Server
echo Starting LibreTranslate Local Server via Docker...

docker ps | findstr libretranslate_server >nul
if %errorlevel%==0 (
    echo [OK] LibreTranslate is already running on port 5000.
) else (
    docker start libretranslate_server >nul 2>&1
    if %errorlevel% neq 0 (
        echo [INFO] Downloading and creating new container (this may take a while)...
        docker run -d --name libretranslate_server -p 5000:5000 libretranslate/libretranslate
    ) else (
        echo [OK] Started existing LibreTranslate container.
    )
)
echo.
echo Server running at: http://localhost:5000/translate
pause
```

4. Double-click `start.bat` to run the server. (The initial download might take a few minutes).

### Configuring the Profile

1. **Provider**: Select `LibreTranslate`.
2. **Base URL**: Enter the URL where your LibreTranslate instance is hosted (e.g., `http://localhost:5000/translate`).
3. **API Key**: If your hosted instance does not require an API key, you can leave this blank. If you are using the official `libretranslate.com` API, enter the key you purchased from them.
4. **Batching**: LibreTranslate does **not** support batch arrays natively. The tool will automatically loop requests if you try to batch, but for the best stability, you may want to disable **Batch Requests** or keep the **Max Batch Size** low.

---

### Troubleshooting Providers

- **Timeout Errors**: If you are translating hundreds of strings and your provider is timing out, increase the **Request Timeout Seconds** in your profile.
- **Language Not Supported**: Ensure your **Source Language** and **Default Target** use valid BCP-47 codes (e.g., `en`, `fr`). If you are unsure, check your provider's documentation for their list of supported language codes.
- **Auto-Detect Failing**: Not all providers support automatic language detection flawlessly. If you are getting errors, disable **Detect Source Language Automatically** and manually set the **Source Language** code.
