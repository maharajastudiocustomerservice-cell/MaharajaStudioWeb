# Curve & Keyframe Editing

The Animation Editor provides detailed control over curves and individual keyframe coordinates. This guide explains how to isolate animated properties, modify key values, adjust tangents, and edit object reference tracks.

---

## The Curves Panel

The **Curves** panel lists all animated properties contained within the clip. It allows you to isolate and operate on specific parts of your model:

* **Filter Search**: Type search terms (e.g., `shoulder` or `rotation`) into the search bar at the top of the panel to filter the list of curves.
* **Operate on Selected Curves Only**: When this toggle is enabled, range operations (such as Delete Range, Scale Range, or Snap Keys) affect *only* the curves you have highlighted in the list. Unselected curves remain untouched.
* **Select All** / **Clear Selection**: Quick buttons to highlight all visible curves or clear selection.
* **Delete Selected**: Removes the selected property curves entirely from the animation clip.
* **Clear Scene Bones**: Rather than manually searching for curves, you can highlight bones directly in the Scene view and click **Clear Scene Bones**:
  * **Clear Selected Bones Only**: Deletes animated curves for the selected bones.
  * **Clear Selected Bones & Children**: Deletes animated curves for the selected bones and their entire hierarchy (e.g., clearing an entire arm from the shoulder down). This tool automatically maps humanoid muscle properties and generic transform paths.

---

## Single-Key Editor

When you select **exactly one curve** in the Curves list, the **Key Editor** panel activates, listing every keyframe on that curve.

### Selecting Keyframes
* **Scroller List**: Select a keyframe from the scrollable list. Each entry displays its index, frame number, time in seconds, and value.
* **Timeline Clicks**: Click a keyframe marker directly in the timeline tracks.
* **Select Nearest**: Click the **Nearest** button to automatically highlight the keyframe closest to the playhead time.

### Editing Keyframe Coordinates
To edit a keyframe:
1. Select a keyframe. Its coordinates will populate the editable fields.
2. Modify any of the following parameters:
   * **Time**: Change the keyframe's position in seconds.
   * **Frame**: Change the keyframe's frame position.
   * **Value**: Set the numerical value (for float curves like translation, rotation, or scale).
   * **Tangents (Incoming / Outgoing)**: Adjust the numerical slope of the curve entering and leaving the keyframe to control acceleration.
3. Click **Apply Key** to save the changes.

### Key Editing Toolbar Actions
* **Add Key**: Creates a new keyframe on the active curve at the time and value entered in the fields.
* **Delete Key**: Removes the selected keyframe.
* **Nudge Buttons (-1 Frame / +1 Frame)**: Shifts the selected keyframe backward or forward in time by exactly one frame.
* **Key Current**: Samples the preview character's current pose and writes a keyframe onto all selected curves at the playhead time.
* **Delete Current**: Deletes any keyframes that sit on the current frame for all selected curves.

---

## Working with Object Reference Curves

Some animation tracks drive object changes (such as swapping sprites, activating audio clips, or replacing materials) rather than numeric values:

* **Visual Indicators**: Object reference keyframes appear on the timeline tracks as **orange diamond markers** (instead of standard blue float markers).
* **Object Picker**: The **Value** field in the Key Editor converts into an **Object Value** field. Clicking this opens a selection popup displaying all assets in your project of that object type. Choose an asset to bind it to that keyframe.
* **No Tangents**: Because object changes are instantaneous swaps rather than gradients, tangent controls and the curve graph are automatically disabled when editing an object reference curve.
