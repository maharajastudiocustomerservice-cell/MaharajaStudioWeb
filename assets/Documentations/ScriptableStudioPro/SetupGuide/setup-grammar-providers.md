# Setting Up Grammar Providers

Scriptable Studio Pro's Grammar checking system supports **LanguageTool**. You can either use their cloud API or host it yourself locally for free using Docker.

To start, you must create a Grammar Profile:
1. In your **Project** window, right-click inside a folder.
2. Select **Create > Scriptable Studio Pro > Grammar > Grammar Profile**.
3. Select the newly created asset to configure it in the Inspector.
4. Finally, set it as your default profile in **Tools > Maharaja Studio > Scriptable Studio Pro > Settings** under the **Grammar Services** tab.

## Local Docker (Free, Offline, Unlimited)

LanguageTool is open-source, which means you can run the server on your own computer. This is the recommended approach as it ensures no data leaves your machine and you have no rate limits.

### Step 1: Install Docker Desktop
1. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for Windows/Mac.
2. Ensure Docker Desktop is running (you should see the whale icon in your system tray).

### Step 2: Create a Startup Script (Windows)
To make it extremely easy to start your local server, you can create a simple batch script anywhere on your computer (e.g., `C:\CustomAI\LanguageTool\start.bat`).

1. Create a new text file and rename it to `start.bat`.
2. Right-click and open it in a text editor like Notepad.
3. Paste the following code and save:

```bat
@echo off
title LanguageTool Local Server
echo Starting LanguageTool Local Server via Docker...

docker ps | findstr languagetool_server >nul
if %errorlevel%==0 (
    echo [OK] LanguageTool is already running on port 8010.
) else (
    docker start languagetool_server >nul 2>&1
    if %errorlevel% neq 0 (
        echo [INFO] Downloading and creating new container...
        docker run -d --name languagetool_server -p 8010:8010 erikvl87/languagetool
    ) else (
        echo [OK] Started existing LanguageTool container.
    )
)
echo.
echo Server running at: http://localhost:8010/v2/check
pause
```

4. Double-click `start.bat` to run the server. Docker will download the required files automatically on the first run.

### Step 3: Configure the Profile
1. **Provider**: Select `LocalDocker`.
2. **Base URL**: Set to `http://localhost:8010/v2/check`.
3. Leave **API Key** and **Username** empty.

## LanguageTool Cloud

If you do not want to use Docker, you can use LanguageTool's cloud API. Note that their free tier has strict rate limits, and you may need a Premium account for heavy usage.

1. **Provider**: Select `LanguageToolCloud`.
2. **Base URL**: Set to `https://api.languagetool.org/v2/check`.
3. **API Key**: If you have a Premium account, enter your API key here.
4. **Username**: If using Premium, enter the email address associated with your LanguageTool account.

---

## Configuration Options

- **Language**: The BCP-47 language code to check against (e.g., `en-US`, `de-DE`). You can also use `auto` to let LanguageTool attempt to detect the language automatically.
- **Disabled Rule IDs**: A comma-separated list of LanguageTool rule IDs that you want to ignore. This is incredibly useful for ignoring game-specific terminology, character names, or fantasy lore that the grammar checker flags as incorrect. (Example: `MORFOLOGIK_RULE_EN_US,UPPERCASE_SENTENCE_START`)
- **Enabled Categories**: A comma-separated list of category IDs to exclusively check. If you only care about typos, you could put `TYPOS` here. Leave empty to check all categories.
- **Request Timeout Seconds**: If you are checking massive amounts of text in a single request and the server times out, increase this value.
