# Machine Translation (MT)

The Machine Translation feature in Scriptable Studio Pro allows you to rapidly translate your ScriptableObject string fields and Unity Localization `LocalizedString` fields directly within the editor using powerful cloud translation providers (like DeepL, Google Cloud, Azure) or self-hosted open-source options (like LibreTranslate). 

This tool is optimized for batch-translating large quantities of text quickly and seamlessly integrating it into your existing Unity Localization tables.

## Quick Overview

1. **Create an MT Profile**: Create a profile from the **Project** window (`Create > Scriptable Studio Pro > MT > Translation Profile`) and set up your provider details.
2. **Assign the Profile**: Go to **Tools > Maharaja Studio > Scriptable Studio Pro > Settings**, navigate to **MT Services**, and select your newly created profile.
3. **Open the MT Translate Window**: Select your ScriptableObjects, right-click, and choose **Scriptable Studio Pro > Translate (MT)**.
4. **Translate**: Select your target language and click **Translate Now**.

---

## MT Translate Window

This window is your main interface for running translations on your selected assets. 

### Target Language

- **Target**: A text field with a dropdown menu to select the language you want to translate your normal strings into. You can type a BCP-47 language code (e.g., `es`, `ja`, `de`) manually or pick from the dropdown list of common locales. 
  - *Note: If you are translating `LocalizedString` fields, the translation will automatically apply to all locales defined in your global Localization settings.*

### String Table Override

*(Visible only if the Unity Localization package is installed.)*

- **Target Table**: A dropdown that allows you to override the default String Table Collection for the current translation session. If you want to dump translations into a different table, select it here. By default, it will use the collection defined in your global Settings.

### Scope

- **Apply To**: Choose whether to translate only the **Selected Items** in the left panel or **All Items** across the entire batch.

### Options

- **Skip Empty Strings**: Enabled by default. Ignores any fields that are empty or null, saving you unnecessary API calls and time.
- **Dry Run (Preview in Console)**: When enabled, the tool will fetch translations from the provider but **will not write them** to your assets or String Tables. Instead, it prints every fetched translation to the Unity Console so you can verify the output before committing.
- **Overwrite Existing Table Keys**: When translating `LocalizedString` fields, this decides if the MT tool should overwrite existing translations in the String Table or only fill in the blanks.
- **Key Naming Pattern**: Defines how new keys are named when added to the String Table. You can use dynamic placeholders:
  - `{TypeName}` - The name of the ScriptableObject type.
  - `{FieldName}` - The name of the field being translated.
  - `{AssetName}` - The name of the specific ScriptableObject asset.
  - `{#}` - A unique randomized string.

---

## Global Localization Settings

You can configure master rules for localization across the entire tool inside **Settings > Localization**.

- **Auto-Create Missing Keys**: If a translation is generated but no key exists in the target String Table, the tool will automatically create a new key.
- **Overwrite Existing Keys**: Master toggle to allow overriding existing translations in the tables.
- **Target Locales**: Define which locales your `LocalizedString` fields should automatically translate into. For example, if you add French and German here, one click will translate your fields into both languages simultaneously.
- **Target String Table**: The default Unity String Table Collection where all translations will be stored.

---

## Performance & Batching

Scriptable Studio Pro optimizes your translation requests behind the scenes. When you select multiple assets and hit translate, the tool bundles the text into optimized batches (up to the limit defined in your MT Profile). This drastically reduces the number of API calls made, making translations lightning-fast and keeping you well within your provider's rate limits.
