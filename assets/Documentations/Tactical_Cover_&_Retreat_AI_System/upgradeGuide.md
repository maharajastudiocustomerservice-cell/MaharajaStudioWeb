# 🛡️ Tactical Cover & Retreat AI – Version 2.0 Upgrade Guide

## 👋 Welcome to 2.0!

Formerly known as **"Hiding System,"** version 2.0 represents a massive evolution in the asset's capabilities. Because the system now handles **Ambushing, Flanking, Squad Tactics, and Pincer Movements**, the old name no longer fit.

We have rebranded to **Tactical Cover & Retreat AI (TCRAI)** to reflect this power.

### ⚠️ Important: Read Before Importing

This update includes **renamed classes and namespaces**.

* **Good News:** We have used Unity's `[MovedFrom]` and `[FormerlySerializedAs]` attributes. This means your **Prefabs and Inspector settings will be preserved automatically.** You will not lose your tuned values.
* **Action Required:** If you have written **custom C# scripts** that reference `EnemyHider` or `MaharajaStudio.HidingSystem`, you will need to perform a simple Find & Replace update.

---

## 🛠️ Step-by-Step Upgrade Process

### 1. Backup Your Project

Before performing any major asset update, always backup your project or commit your current state to Version Control (Git/PlasticSCM).

### 2. Remove the Old Version

**Do not** simply import 2.0 over the old 1.x folder. This can cause duplicate file errors.

1. Open your project.
2. Delete the folder: `Assets/MaharajaStudio/HidingSystem`.
3. (Optional) If you have moved the folder elsewhere, delete the `HidingSystem` root folder.

### 3. Import Version 2.0

1. Import the new `Tactical Cover & Retreat AI` package.
2. Unity might trigger an "API Update" dialog. If it does, click **"I Made a Backup, Go Ahead!"**

### 4. Update Your Custom Scripts

Your console will likely show errors like `The type or namespace name 'HidingSystem' could not be found`. This is normal. You need to update your references to the new names.

**Use "Find and Replace" (Ctrl+Shift+F) in your IDE to swap these terms:**

| Old Term | New Term | Notes |
| --- | --- | --- |
| `MaharajaStudio.HidingSystem` | `MaharajaStudio.TacticalAI` | **Namespace Update (Required)** |
| `EnemyHider` | `TacticalAgent` | The main component script |
| `HidingSettingsSO` | `TacticalProfileSO` | The settings profile asset |
| `HideSpotScorerSO` | `TacticalScorerSO` | Base class for custom scorers |
| `HideSpotProviderSO` | `TacticalProviderSO` | Base class for custom providers |

#### Example of Code Migration:

**Old Code (v1.x):**

```csharp
using MaharajaStudio.HidingSystem; // Error!

public class MyAIController : MonoBehaviour
{
    private EnemyHider _hider; // Error!
    
    void Start() {
        _hider = GetComponent<EnemyHider>();
        _hider.RetreatToHide();
    }
}

```

**New Code (v2.0):**

```csharp
using MaharajaStudio.TacticalAI; // Fixed!

public class MyAIController : MonoBehaviour
{
    private TacticalAgent _agent; // Fixed!
    
    void Start() {
        _agent = GetComponent<TacticalAgent>();
        
        // "RetreatToHide" still works, but we recommend using the new API:
        _agent.FindTacticalPosition(); 
    }
}

```

---

## 📋 Cheat Sheet: What Changed?

### 1. The Main Component

* **Old:** `EnemyHider`
* **New:** `TacticalAgent`
* **Location:** Now found in the Add Component menu under `Tactical AI > Tactical Agent`.

### 2. The Settings

* **Old:** `HidingSettingsSO`
* **New:** `TacticalProfileSO`
* **Note:** Your existing settings assets have been automatically upgraded. You do not need to recreate them.

### 3. Scorers & Providers

* **Old:** `AmbushScorerSO` (in `HidingSystem.AllScorer`)
* **New:** `AmbushScorerSO` (in `TacticalAI.Scorers`)
* **Action:** If you wrote custom scorers, change them to inherit from `TacticalScorerSO`.

---

## ❓ Troubleshooting / FAQ

**Q: I see "Missing Script" on my Enemy GameObjects!**
**A:** This happens if the `[MovedFrom]` data hasn't refreshed.

1. Close the scene and reopen it.
2. If that fails, restart Unity.
3. As a last resort, ensure you didn't accidentally delete the `.meta` files associated with your scripts if you manually moved files around.

**Q: My custom Scorer says "The type name 'HidingContext' could not be found".**
**A:** `HidingContext` is one of the few classes we kept named similar for compatibility, but it is now in the `MaharajaStudio.TacticalAI` namespace. Simply add `using MaharajaStudio.TacticalAI;` to the top of your file.

**Q: Where did the "Hiding System" folder go?**
**A:** The default install path is now `Assets/MaharajaStudio/TacticalAI`.

---

## 🚀 What's New in 2.0?

Now that you've upgraded, check out the new features available in your `TacticalProfileSO`:

* **Ambush Logic:** Agents can now lie in wait for a target.
* **Pincer Formations:** Automatically coordinate agents to surround the player.
* **Dynamic Flanking:** Agents actively seek the player's blind spots.
* **Light Probes:** Use `ShadowProvider` and `LightProbeScorer` to make your AI hide in the dark!

If you have any issues upgrading, please contact support at [Email/Discord].