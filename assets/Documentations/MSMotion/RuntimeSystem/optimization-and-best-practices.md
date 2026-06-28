# Optimization & Best Practices

MSMotion's runtime framework is designed from the ground up for high-performance execution, targeting 60+ FPS on console and mobile hardware. This guide details the architectural optimizations under the hood and outlines best practices for structuring your character systems.

---

## Garbage Collection Mitigation

Garbage Collection (GC) spikes cause micro-stutters that ruin fluid action games. MSMotion eliminates runtime allocations using several techniques:

### 1. Pre-Warmed Object Pooling (`MSMotionFXPool`)
*   When `MSMotionFXPlayer` starts, it pre-allocates pools of `AudioSource` and `ParticleSystem` game objects based on your Inspector settings (**Pool Sizes**).
*   During gameplay, spawning footstep dust, hit sparks, or voice lines calls a fast reference swap in the pool instead of `Instantiate()` or `Destroy()`.
*   If pool capacities are exceeded, the pool grows dynamically. To avoid mid-combat allocations, profile your game and set the initial pool size to cover your maximum concurrent visual/sound effects.

### 2. Allocation-Free Spline Evaluation
*   Spline trajectories used by particles and visual effects evaluate dynamically via the `FXTrajectoryEvaluator`.
*   The evaluator operates using struct-based math arrays rather than heap allocations, keeping the tick loop completely free of GC allocations.

### 3. Cached Data Structures
*   **Bone Lookups**: The FX Player cache bones dynamically (`_boneCache`). The first time a bone is requested (e.g., `"LeftHand"`), the player traverses the skeleton hierarchy and stores the reference. Subsequent ticks resolve instantly. If you re-parent the skeleton or swap rigs, call `RebindBones()` to safely clear the cache.
*   **Avatar Mask Calculations**: Evaluating whether a bone is masked out by a layer's `AvatarMask` is cached in a per-layer dictionary (`AvatarMaskCache`). This ensures bones are only resolved against the mask structure once, rather than traversing the skeleton on every frame.

---

## Thread Safety & Asynchronous Playback

The runtime framework combines Unity's main thread API with asynchronous task management:

### 1. PlayableGraph Evaluation
*   Unity evaluates the `PlayableGraph` internally on worker threads using its native C++ job system.
*   Custom logic modifications (such as calling `Play()`, `CrossFade()`, or setting IK targets) must be called from the **Main Thread**. Do not attempt to modify layer structures from secondary worker threads.

### 2. Async Fade and Transition Tasks
*   Weight blending, IK fades, and transition intervals are driven by C# `Awaitable` tasks.
*   To prevent memory leaks or abandoned tasks when an animation is interrupted (for example, getting hit while executing a heavy attack), every layer has an active `CancellationTokenSource`.
*   When a new play request comes in, the animator automatically cancels the active task, discards the token, and begins the new blend safely.

---

## Level-of-Detail (LOD) & Culling Strategies

When rendering crowds of characters, procedural systems can become a bottleneck. Implement these culling strategies to maintain high frame rates:

*   **Distance Culling**: Always add `MSMotionStretchApplicator` to characters using scale features. Set the `farDistance` threshold to a reasonable range (e.g. 30–50 meters). Once characters cross this threshold, bone scaling evaluation drops to `0` and bones are restored to their standard local scale, freeing up CPU cycles.
*   **Update Skipping**: Configure `_midLODInterval` on the applicator to skip frames for mid-distance characters. An interval of `2` or `3` cuts evaluation overhead by 50–66% with negligible visual impact at a distance.
*   **Disable Off-Screen Applicators**: The `MSMotionStretchApplicator` utilizes Unity's `OnBecameVisible()` and `OnBecameInvisible()` callbacks to suspend curve evaluations entirely when a character is off-screen. Ensure your character meshes have properly configured render bounds.

---

## Best Practices for Combat & Locomotion Setups

To get the most out of MSMotion's multi-layer blending, structure your character and animation configurations using these guidelines:

### 1. Standard Layer Layout
Maintain a consistent layer scheme across all character configurations in your project:

| Layer Index | Name | Blending Mode | Purpose |
| :--- | :--- | :--- | :--- |
| **Layer 0** | Base / Locomotion | Override | Standard movement (runs Animator Controller or fallback idle). |
| **Layer 1** | Upper-Body Action | Override (with Mask) | Weapon swings, item interactions, spell casting. |
| **Layer 2** | Full-Body Override | Override | Dodge rolls, hit reactions, deaths, knockbacks. |
| **Layer 3** | Impact Overlays | Additive | Flinches, breathing heavy overlays, physics shakes. |

### 2. Isolate Bones with Avatar Masks
*   Always assign an `AvatarMask` to upper-body action clips (Layer 1) to exclude the hips and legs. This allows your character to move, run, and jump on Layer 0 while naturally executing attack swings on Layer 1.
*   Leave full-body overrides (Layer 2) mask-less (or `null`) so the action takes absolute precedence over the skeletal pose.

### 3. Additive Blending for Overlays
*   Use additive layers for small impact reaction clips. An additive hit-flinch animation can play on Layer 3 without interrupting an attack on Layer 1 or locomotion on Layer 0, blending on top of whatever pose the character is currently in.
