# Metadata Manager

The **Metadata Manager** is a project utility that allows you to scan, hide, show, or permanently delete embedded **IK Stretch & Joint Scale Metadata** sub-assets across all Animation Clips in your Unity project.

---

## What is MSMotion Metadata?

When you bake animations that utilize procedural IK or scaling modifications (such as limb stretching, parent scale compensation, or volume preservation), MSMotion embeds specialized **Clip Metadata** sub-assets directly into the generated `.anim` files. 

These sub-assets contain scale calibration matrices and joint-length proportions. While these assets are required for correct runtime playback and solver adjustments:
*   They are normally hidden sub-assets inside the `.anim` files.
*   Retiring old rigs or deleting compositions can leave orphaned metadata files inside the project database.
*   Unused metadata sub-assets can accumulate over time, increasing file sizes and cluttering search structures.

---

## Accessing the Metadata Manager

To open the utility window, choose **Tools > Maharaja Studio > MsMotion > Metadata Manager** from the Unity editor menu bar.

---

## Scanning the Project

When the window opens, the database list is empty:
1.  Click **Scan Project** in the toolbar.
2.  A progress bar will display while the utility scans the Unity Asset Database for all `.anim` assets.
3.  Upon completion, the list displays all Animation Clips containing embedded MSMotion metadata.

---

## List Controls

Each detected clip card displays the following information:

*   **Clip Icon & Title**: Pings the parent Animation Clip.
*   **Asset Folder Path**: The location of the clip in your project directory.
*   **Visibility State**:
    *   **VISIBLE**: The metadata sub-asset is exposed in the Project window hierarchy.
    *   **HIDDEN**: The metadata sub-asset is hidden from the Project window hierarchy (recommended to prevent clutter).
*   **Show / Hide Button**: Instantly toggles the hierarchy visibility state for that specific clip's metadata sub-asset.
*   **Delete**: Permanently removes the metadata sub-asset from the parent `.anim` file.
    > [!CAUTION]
    > Deleting a clip's metadata permanently removes its cached IK stretch and joint scale proportions. The clip will lose stretch calculations during solver playbacks.

---

## Global Toolbar Operations

The toolbar at the top of the window provides bulk operations:

*   **Hide All**: Sets the visibility state of all detected metadata sub-assets to hidden, keeping your project files panel organized.
*   **Show All**: Exposes all metadata sub-assets within their parent `.anim` files in the Project window.
*   **Delete All**: Deletes all embedded metadata from all scanned clips in the project.
    > [!CAUTION]
    > This operation permanently deletes all IK/scale proportions from all clips. This action is irreversible.
*   **Search Bar**: Type a clip name to filter the list instantly.

---

## Related Guides

*   **IK Rig Settings**: Learn how scale overrides are calculated in [IK Rig Configuration](ik-rig-configuration.md).
*   **Baking Clips**: Bake animations with [Export Options](export-options.md).
*   **Troubleshooting**: Find cleanup recommendations in [Troubleshooting](troubleshooting.md).
