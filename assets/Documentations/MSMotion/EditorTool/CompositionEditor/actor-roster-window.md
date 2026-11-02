# Actor Roster & Dynamic Alignment Window

The **Actor Roster & Alignment Window** is the central management hub for multi-character animations, choreography duets, summons, and procedural motion warping in MSMotion.

Open the window from the **Composition Editor** top toolbar by clicking either:
*   **👥 Actors**: Opens the **Character Roster** tab.
*   **⚡ Alignment**: Opens the **Dynamic Alignment** tab.

---

## Tab 1: Character Roster

The **Character Roster** tab configures all participants involved in the composition — from primary heroes and dance partners to combat adversaries and temporary summons.

### Managing Participant Characters

*   **+ Add Participant Character**: Appends a new character definition to the composition roster.
*   **Search & Filter**: Quickly locate participants by display name, role, or skeletal rig type.
*   **Expand All / Collapse All**: Toggles the display state of all actor cards for convenient inspection.

### Participant Properties

Each character card exposes the following settings:

| Property | Description |
|:---|:---|
| **Display Name** | The user-friendly name displayed on timeline slots and badges (e.g. `Hero`, `Partner`, `Boss`). |
| **Actor Role** | Logical role identifier used by export and runtime systems (e.g. `Lead`, `Follower`, `Target`). |
| **Accent Color** | Color swatch used to tint this character's timeline clips, slot badges, and scene view gizmos. |
| **Rig Type** | Choose between **Humanoid** and **Generic**. Generic rigs allow non-humanoid skeletons (creatures, quadrupeds, mechanical robots, animated props) to participate in synchronized sequences. |
| **Preview GameObject** | The scene GameObject bound to this actor during edit-mode playback and scrubbing. |
| **Actor Type** | Choose between **Scene Character** (persistent character present in the scene) and **Dynamic** (temporary entity spawned during the interaction). |

---

### Dynamic / Temporary Actors (Summons & Ephemeral Entities)

When **Actor Type** is switched to **Dynamic**, the character represents an ephemeral entity — such as a summoned dragon, phantom weapon, spectral beast, or Stand avatar — that spawns, animates, and despawns automatically during the sequence:

*   **Dynamic Prefab**: The prefab asset to instantiate for this entity.
*   **Spawn Time**: Choose when the entity appears. Select from quick presets (`0.0`, `0.25`, `0.5`, `0.75`, `1.0`) or choose `Custom`.
*   **Destroy Time**: Choose when the entity despawns and recycles back to the object pool (`0.0`, `0.25`, `0.5`, `0.75`, `1.0`, or `Custom`).
*   **Attachment Mode**: Defines how the dynamic entity follows the caster:
    *   **Caster Bone Socket**: Snaps to a designated bone on the primary character (e.g. `RightHand`, `Spine`).
    *   **Caster Root Relative**: Tracks the caster's root position with an authored spatial offset.
    *   **World Sync Offset**: Spawns relative to the global interaction sync anchor.
*   **Custom Timeline Nodes**: When spawn or destroy time is set to `Custom`, click **+ Add Spawn Node** or **+ Add Destroy Node** to place precise [Spawn Actor](actor-lifecycle-nodes.md) and [Destroy Actor](actor-lifecycle-nodes.md) blocks directly on the composition timeline.

---

### Timeline Slot Routing & Visual Indicators

Once participants are configured in the roster:
1.  **Assigning Slots**: Select any timeline block (animation clip, FX node, or procedural solver). In the details panel, select the desired actor from the **Target Character** dropdown, or right-click any block and choose **Assign to Actor > [Character Name]**.
2.  **Visual Badges**: Slots assigned to secondary actors display a colored badge pill with the character's role and a matching tinted accent stripe along the top of the block.
3.  **Synchronized Scrubbing**: Moving the timeline playhead scrubs all participant characters simultaneously in the Scene View with zero frame drift.

---

## Tab 2: Dynamic Alignment (Motion Warping)

In real gameplay, characters rarely start at the exact relative positions and rotations required for a synchronized sequence. The **Dynamic Alignment** system bridges arbitrary starting distances dynamically: secondary actors travel smoothly to their sync spots, dynamically scaling their locomotion speed to match travel distance, before seamlessly crossfading into the synchronized interaction.

### Pre-Interaction Entry Phase

Dynamic Alignment functions as an **asynchronous Pre-Interaction Entry Phase** rather than eating fixed time on the composition timeline. The composition timeline itself remains strictly focused on the synchronized choreography starting at $t = 0$.

### Configuration Settings

*   **Enable Dynamic Alignment**: Master switch enabling runtime approach warping and scene view visualization.
*   **Approach Locomotion Clip**: The walking, jogging, or running animation played while characters travel toward their authored spots.
*   **Waiting / Idle Clip**: The idle animation played if a character reaches their spot early while waiting for others to arrive.
*   **Primary Actor Waiting Clip**: The idle animation played by the lead character (Actor 0) while waiting for secondary characters to approach.
*   **Min / Max Time (s)**: The minimum and maximum allowable approach duration in seconds (e.g. `0.5s` to `4.0s`).
*   **Min / Max Speed Multiplier**: Playback speed bounds (e.g. `0.5x` to `2.0x`) preventing unnatural fast-forwarding or foot sliding.
*   **Natural Stride Speed (m/s)**: The character's authentic locomotion speed. Click **Auto Stride** to automatically analyze the locomotion clip's root motion curves and calculate the exact velocity.
*   **Arrival Threshold (m)**: Distance tolerance (e.g. `0.1m`) within which a character is considered to have arrived at their spot.
*   **Adapt to Terrain**: Enables ground raycasting during the approach path to keep feet planted on slopes, steps, or uneven ground.

---

### Scene View Visualizer & Testing Tools

When Dynamic Alignment is active, the Scene View displays real-time alignment feedback:
*   **Sync Spot Discs**: Cyan boundary rings marking each actor's authored arrival point and facing direction.
*   **Lead Anchor**: A gold coordinate pivot highlighting the interaction sync origin.
*   **Trajectory Lines & Readouts**: Dotted lines connecting each character's current position to their target spot, showing live distance, travel time, and calculated playback speed.
*   **Snap to Sync Spots**: A quick-action button in the Scene HUD that snaps all preview characters to their authored interaction origins.
*   **Test Approach Offsets**: Temporarily displaces secondary characters by several meters in the viewport so you can visually test and preview approach speeds without entering Play Mode.
