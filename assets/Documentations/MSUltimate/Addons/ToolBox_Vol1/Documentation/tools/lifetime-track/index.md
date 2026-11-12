# Lifetime Track Manual

> GameObject and asset lifecycle tracker identifying persistent memory leaks, post-mortem dangling C# references, scene teardown leaks, and unreleased pooling allocations.

## Access & Launch
- **Menu Path:** `Tools > Maharaja Studio > MSUltimate > ToolBox Vol 1 > Object Lifetime Tracker`
- **In-Game Runtime HUD Overlay:** Hotkey `F8` or 3-finger mobile touch gesture (Console: `lifetime.hud`).

---

## Capabilities & Workflows

### 1. Post-Mortem Dangling Reference Hunter
- **The Problem:** Calling `Destroy(gameObject)` destroys the native C++ engine object (`m_CachedPtr == 0`), but static events (`GameEvents.OnScoreChanged += HandleScore`), singletons, or living managers retaining a C# reference keep the entire managed wrapper, its fields, arrays, and textures alive in the Mono/IL2CPP heap forever.
- **The Solution:** 
  - Retains a `WeakReference<object>` on `OnDestroy()`.
  - Audits surviving references where `target != null && (UnityEngine.Object)target == null`.
  - Flags dead instances with `⚠ DANGLING` alerts in the inspector and tables.
  - One-click **"Inspect Retainers"** button scans static event delegates, collections, and living scene `MonoBehaviour` fields to pinpoint the exact leak source holding the dead object.

### 2. Scene Teardown & Transition Audit
- **The Problem:** GameObjects and pooled instances often fail to clean up during scene changes, leaking past scene unloads or PlayMode transitions.
- **The Solution:**
  - Automated hooks into `SceneManager.sceneUnloaded` and `EditorApplication.playModeStateChanged (ExitingPlayMode)`.
  - Any instance belonging to the unloaded scene that is still marked alive is automatically flagged as a teardown leak (`🚨 LEAKED`).
  - Generates formatted audit reports to console and UI:
    > *"3 instances leaked past Scene 'Level_01' unload! (2x EnemyBullet, 1x FloatingDamagePopup). Alive duration: 240s."*

### 3. Differential Snapshot Engine (Baseline Diffing A vs B)
- **The Problem:** Cumulative session counters make it difficult to isolate leaks caused by a specific gameplay action (e.g., Opening Inventory, Completing Wave 3, or Replaying a Match).
- **The Solution:**
  - **Set Baseline (Snapshot A):** Freezes all current type and global active counts as the reference state.
  - **Live Delta Tracking:** Real-time columns for $\Delta\text{Active}$, $\Delta\text{Spawn}$, $\Delta\text{Kill}$, $\text{Net Leak}$, and $\Delta\text{RAM}$.
  - Types with positive active deltas or unreleased net counts upon returning to an idle state are highlighted in bright red as verified leaks.

### 4. Interactive Timeline & Range Slicing
- Real-time rolling/sliding window painter (Last 10s, 30s, 60s, 2m, 5m, Full Session).
- Zoom with mouse wheel, pan with Middle/Right/Alt drag, and click-and-drag to slice time windows for targeted anomaly inspection.

---

## Quick-Action Console Commands

| Command | Category | Description |
| :--- | :---: | :--- |
| `lifetime.hud` | Lifetime | Toggles the in-game runtime HUD overlay. |
| `lifetime.stats` | Lifetime | Prints active, spawned, destroyed, peak, and dangling reference telemetry. |
| `lifetime.audit` | Lifetime | Triggers full GC and audits all destroyed objects for post-mortem dangling references. |
| `lifetime.baseline` | Lifetime | Establishes a baseline snapshot (`lifetime.baseline clear` to reset). |
| `lifetime.clear` | Lifetime | Clears the current lifetime tracking session and resets event buffers. |
