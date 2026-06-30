# IK Rig Configuration

The **Rig Config** window allows you to define and adjust **Inverse Kinematics (IK) Chains** and constraints for your preview character. The editor uses these rig definitions to solve limb targets, handle ground grounding, and calculate physical modifications in real time.

To open the Rig Config window, click the **Rig Config (🦴 Icon)** on the composition top toolbar.

---

## Window Layout

The editor features a split panel workspace for editing the character rig:

```
+------------------------+-----------------------------------------+
|      Left Pane         |               Right Pane                |
| (Chains List & Presets)|    (Global settings & Chain details)    |
+------------------------+-----------------------------------------+
```

---

## 1. Rig Global Settings
When no specific chain is selected in the left list, the right pane displays global settings for the character rig:

*   **Enable Full-Body IK (Root Pull)**: Toggles full-body IK solver reactions. When enabled, pulling hand or foot targets beyond the character's natural limb length will drag the hips and body towards the target instead of letting the limb hyper-extend.
*   **FBIK Weight**: A slider (`0.0` to `1.0`) controlling the influence of the full-body root pulling effect.
*   **FBIK Root Bone**: The character joint (usually the hips or pelvis) from which the full-body pull originates.

---

## 2. Left Pane: Chains & Presets
Manage joint chains in the list using the top toolbar buttons:

*   **+ Custom**: Adds a blank, unassigned IK chain to the list.
*   **+ Preset**: Opens a dropdown menu to instantiate template chains:
    *   *Left Arm* / *Right Arm*
    *   *Left Leg* / *Right Leg*
    *   *Spine*
    *   *Tail*
*   **Auto-Detect**: Scans the preview character to construct chains automatically:
    *   *Humanoid Rig*: Queries the Animator components and binds the Left Arm, Right Arm, Left Leg, and Right Leg chains using standard humanoid bones.
    *   *Generic Heuristics*: Scans non-humanoid hierarchies to guess logical limb joints based on bone lengths and layout.

---

## 3. Right Pane: Chain Configuration
Selecting a chain in the left list displays its properties in the details pane:

*   **Chain Label**: The user-facing name of the IK chain.
*   **Solver Type**: The mathematical algorithm used to resolve joints:
    *   **Two Bone Analytic**: Highly optimized solver restricted to exactly three joints (Root, Mid, Tip) like shoulder-elbow-wrist or hip-knee-ankle. Ideal for standard biped limbs.
    *   **FABRIK**: (Forward And Backward Reaching Inverse Kinematics). A heuristic solver that supports chains of any bone count (such as multi-joint tails, spines, tentacles, or neck chains).
*   **Soft IK Ratio**: A slider (`0.0` to `0.5`) that prevents limbs from aggressively popping or shaking when extending straight. As the target nears maximum limb length, the solver softens bone angles.
*   **Use Pole Vector**: Toggles custom pole target alignment to direct joint hinge bends (e.g., pointing elbows backward or knees forward).

### Squash & Stretch
Enables procedural bone stretching under tension:
*   **Allow Stretch**: Toggles bone lengthening when targets are pulled beyond the natural limb span.
*   **Max Stretch Multiplier**: The maximum length scale factor allowed (must be `>= 1.0`).
*   **Stretch Axis**: The local alignment axis along which the bone scales.
*   **Preserve Volume**: When stretched, squashes the bone's perpendicular scale to maintain volume.
*   **Compensate Parent Scale**: Ignores parental scale changes to prevent scaling errors.

### Twist Distribution (Roll Solvers)
Prevents "candy wrapper" twisting artifacts on character limbs (such as forearms and upper arms) by distributing the source bone's twist rotation across multiple twist target bones.
*   **Enable Twist Distribution**: Toggles the roll solver for this chain.
*   **Twist Source Bone**: The bone whose twist is measured (usually the wrist/hand).
*   **Twist Axis (Local)**: The local axis vector around which the source bone naturally twists (usually `1,0,0` for the X-axis).
*   **Twist Target Bones**: A dynamic list of bones that will receive a fraction of the twist. Add bones (e.g. `ForearmTwist_L`) and adjust their **Weight** sliders (e.g., `0.5` for 50% twist distribution).

### Bone Paths
Defines the joints included in the solver:
*   *Two-Bone Analytic*: Specify the **Root** (shoulder/hip), **Mid** (elbow/knee), and **Tip** (hand/foot) transforms.
*   *FABRIK*: Specify the **Root** and the **Tip** transforms. The solver automatically extracts all bone segments in between and displays them in a hierarchy checklist.
*   **Recalculate Rest Pose Proportions**: Clears cached scale dimensions and measures default limb spans using the character's current Scene View coordinates.

### Per-Joint Scale Overrides
Displays a list of joint scales. Adjust these vectors to manually compress or extend specific bones inside the chain during animation playback.

---

## 4. FABRIK Joint Limits
When using the **FABRIK** solver type, you can assign physical limits to individual joints (excluding the final tip target) to restrict bending:

*   **Stiffness (FK Bias)**: A slider (`0.0` to `1.0`) defining joint resistance. Higher values bias the joint to retain its original rest pose shape, while lower values comply with IK target pulls.
*   **Constraint Type**:
    *   **None**: Free rotation.
    *   **Hinge**: Restricts rotation to a single local axis.
        *   *Hinge Axis (Local)*: Direction vector of the hinge.
        *   *Min Angle* / *Max Angle*: Rotation limits in degrees.
    *   **Cone**: Restricts rotation to a conical range.
        *   *Cone Center (Local)*: Vector defining the center direction of the cone.
        *   *Cone Angle Limit*: Maximum angular deviation from the center line.

### Scene View Visualization
When a FABRIK chain is selected, active constraints display interactive overlays in the Scene View:
*   **Hinge Overlays**: Render as semi-transparent green arcs showing the allowed angular slice.
*   **Cone Overlays**: Render as semi-transparent orange wire cones and solid discs representing the allowable limits.
*   **Viewport Dragging**: Adjust limit angles and axis directions directly using handles in the Scene View.

---

## Related Guides

*   **Main Workspace**: Get an overview of the editor in the [Composition Editor Index](index.md).
*   **Baking Clips**: Bake animations with [Export Options](export-options.md).
*   **Global Options**: Customize workspace defaults in [Editor Settings](editor-settings.md).
