# Clip & Asset Management

The Animation Editor operates directly on animation assets. This guide explains how to manage animation clips, convert read-only animations, and utilize the clip clipboard.

---

## Loading Animations

You can load animations into the editor using three methods:
1. **Drag and Drop**: Drag any Animation Clip asset from your Project window and drop it anywhere inside the Animation Editor window.
2. **Object Picker**: Click the small circle icon next to the **Animation Clip** field in the sidebar and choose a clip from the list.
3. **Load Selection**: Highlight a character in the scene hierarchy or click an Animation Clip asset in the Project view, then click the **Load Selection** button in the sidebar. The editor will automatically hook up the character and the clip.

---

## Understanding Editable vs. Read-Only Clips

Unity separates animations into two categories, and the editor displays safety warnings based on the loaded asset type:

| Asset Type | Origin | Editable? | Editor Behavior |
|:---|:---|:---|:---|
| **Standalone Clip** (`.anim`) | Created inside Unity or exported. | **Yes** | Fully editable. Keyframe changes write directly to the asset. |
| **Embedded Clip** | Embedded inside a Layout Composition. | **Yes** | Fully editable. Edits save inside the parent composition container. |
| **Imported Model Clip** | Embedded inside a 3D model file (e.g. `.fbx`, `.obj`). | **No** | **Read-Only**. The editor blocks key editing and displays a yellow warning bar. |

### Extracting Read-Only Animations
To edit an imported model animation, you must create a writeable copy. The editor provides an **Extract Editable Copy** button in the sidebar's **Clip** panel to automate this:
* **Standalone Mode**: If you are editing a clip outside a layout composition, clicking **Extract Editable Copy** opens a standard Unity save file dialog. Choose a folder in your project to save the writeable `.anim` file.
* **Composition Mode**: If the clip is loaded inside a Layout Composition, clicking **Extract Editable Copy** automatically extracts the clip and embeds it directly inside the composition asset as a sub-asset, avoiding folder clutter.

---

## Asset Panel Controls

The **Clip** panel in the sidebar contains actions to manage files and copy data:

### File Commands
* **Duplicate**: Creates a direct clone of the currently loaded Animation Clip asset. It prompts for a new filename and loads the clone.
* **Save**: Forces Unity to write all cached in-memory keyframe changes back to the physical `.anim` file on your disk.

### Clipboard Commands
The editor features a dedicated animation clipboard separate from the operating system clipboard. This allows you to transfer animations between clips:
* **Copy Clip**: Copies the entire loaded animation (all curves, keys, and events) into the clipboard buffer.
* **Replace**: Replaces the loaded animation's contents with the animation currently held in the clipboard. This is a destructive operation and supports Undo.
* **Paste New**: Extracts the animation from the clipboard buffer and saves it as a brand-new standalone `.anim` asset.
* **Cut Asset**: Copies the loaded animation to the clipboard, then prompts you to delete the source asset from the project files entirely.

---

## Safety Safeguards

To prevent accidental data loss, the editor includes several built-in safety features:
* **Status Readout Warning**: A status label at the bottom of the Clip panel turns red and displays a detailed description whenever you attempt to write keyframes to a read-only FBX file.
* **Destructive Confirmations**: Prompts are shown before deleting assets or overwriting files (e.g., when clicking **Cut Asset** or **Replace**).
* **Empty Selections**: Operations that require selections (like copying keyframes) display status prompts if nothing is highlighted, preventing silent failures.
