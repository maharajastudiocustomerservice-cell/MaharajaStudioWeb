# Getting Started

Follow this guide to install the MSMotion Animation Editor and perform your first animation editing pass.

---

## System Requirements

* **Unity Version**: Unity 2022.3 LTS or newer.
* **UI Toolkit**: Compatible with projects using Unity's modern UI Toolkit styling.
* **Dependencies**: Requires a character GameObject with an **Animator** component in the scene to enable active Scene view previews and IK solvers.

---

## Installation

The Animation Editor is distributed as a Unity Package Manager (UPM) package. Add it to your project using one of the following methods:

### Method A: Install via Git URL (Recommended)
1. In Unity, open **Window > Package Manager**.
2. Click the **+** button in the top-left corner of the Package Manager window.
3. Select **Add package from git URL...** from the dropdown menu.
4. Enter the package URL provided with your repository access or purchase:
   ```
   https://github.com/maharajastudio/com.maharajastudio.animation-editor.git
   ```
5. Click **Add**. Unity will download and import the package.

### Method B: Install via Local Tarball
1. Download the package tarball file (`.tgz`) to your computer.
2. Open **Window > Package Manager**.
3. Click the **+** button in the top-left corner and select **Add package from tarball...**
4. Browse to and select the downloaded `.tgz` file.
5. Click **Open** to import.

---

## Quick Start Tutorial: Your First Edit

Follow these steps to load a character model and modify an existing walk animation clip:

### 1. Open the Animation Editor
Open the editor window from the main Unity menu:
Go to **Tools > Maharaja Studio > MsMotion > Animation Editor**.

### 2. Set Up the Preview Character
1. Open or set up a Unity scene containing your character model.
2. Ensure the character GameObject has an **Animator** component.
3. In the Animation Editor's top toolbar, click the object picker next to **Preview Root** (or drag the character GameObject from the **Hierarchy** directly into the **Preview Root** field).

### 3. Load an Animation Clip
1. In the Project window, find a walk or idle Animation Clip asset (`.anim`).
2. Drag and drop the Animation Clip asset directly into the **Animation Clip** field in the sidebar's **Clip** panel.
3. Alternatively, select the character in the Hierarchy, make sure it has an Animator playing a clip, and click **Load Selection** in the editor sidebar to automatically populate the root and clip fields.

### 4. Play and Scrub
* Click **► Play** in the toolbar to preview the animation running in edit mode.
* Drag the red **Scrubber** line horizontally across the timeline to inspect the pose frame-by-frame.
* Adjust the **Loop** and **Reset Root** toggles to control how the character loops.

### 5. Modify a Bone Pose (Auto-Key)
1. Turn on the **Auto-Key** toggle in the toolbar.
2. Move the timeline scrubber to the frame you want to edit (e.g. Frame 15).
3. In the Scene view, select one of the character's arm bones (e.g., shoulder or elbow).
4. Use Unity's standard rotation handle to rotate the arm.
5. Release the mouse. The timeline will register a red marker on that frame for the modified bone, saving your pose change directly into the animation clip.
6. Press **Ctrl + Z** to undo the change if needed.

> [!WARNING]
> If you load an imported FBX model's animation clip, it will be marked as read-only. You must extract an editable copy before you can write keyframes. See the [Clip Asset Management](clip-asset-management.md) guide for details.
