# Ultimate Quick Inspector

**A powerful Unity Editor extension for pinning and organizing your most-used assets and scene objects for instant access.**

---

## Table of Contents

- [Features](#features)
- [How to Use](#how-to-use)
  - [Opening the Window](#opening-the-window)
  - [Adding Objects](#adding-objects)
  - [Managing Objects](#managing-objects)
  - [Organizing with Pages](#organizing-with-pages)
  - [Searching and Filtering](#searching-and-filtering)
- [Components Explained](#components-explained)
  - [GuidComponent](#guidcomponent)
- [Data Storage](#data-storage)
- [Troubleshooting & Best Practices](#troubleshooting--best-practices)

---

## Features

*   **Pin Anything:** Keep references to any object in your project, whether it's a prefab, a script, a material, or a specific object in your scene.
*   **Multi-Page Organization:** Group your pinned objects into customizable pages. Keep your work organized by context, such as "Player Objects," "UI Elements," or "Level Design."
*   **Drag-and-Drop:** Easily add objects by dragging them into the window.
*   **Search and Filter:** Quickly find the object you're looking for with a simple search bar.
*   **Persistent Data:** Your pinned objects and pages are saved and will be available the next time you open Unity.
*   **Scene Object Tracking:** The tool uses a robust system to track objects in your scene, even if you rename them or they are inactive.

---

## How to Use

### Opening the Window

To open the Ultimate Quick Inspector, go to the Unity Editor's main menu and select **Window > Ultimate Quick Inspector**.

### Adding Objects

There are two ways to add objects to the Quick Inspector:

1.  **Drag and Drop:** Simply drag any object from your Project window or Scene Hierarchy and drop it into the "Drag and Drop Objects Here" area in the Quick Inspector.
2.  **Object Field:** Use the object field at the top right of the window to select an object to add.

### Managing Objects

*   **Remove:** To remove an object from the list, click the "Remove" button next to it.
*   **Remove All:** Use the "Remove All" button in the toolbar to clear all objects from the current page.

### Organizing with Pages

*   **Add Page:** Click the `+` button in the page navigation bar to create a new page.
*   **Remove Page:** Click the `-` button to remove the currently selected page and all objects on it.
*   **Rename Page:** Click the settings icon (gear) to open the page settings, where you can rename the current page.

### Searching and Filtering

Use the search bar at the top of the window to filter the objects on the current page by name.

---

## Components Explained

### GuidComponent

When you add a scene object to the Quick Inspector, a `GuidComponent` is automatically added to it. This component assigns a unique, persistent ID to the GameObject.

**Why is this important?**

Unity's internal instance IDs can change when you close and reopen a scene. The `GuidComponent` ensures that the Quick Inspector can always find the correct object, even after reloading the scene or restarting Unity. This component is lightweight and has no performance impact.

---

## Data Storage

The Ultimate Quick Inspector stores all its data (the list of pinned objects and your page configurations) in a `ScriptableObject` file named `QuickInspectorData.asset`. This file is located in the same directory as the main tool script (`UltimateQuickInspector/Editor/`).

You don't need to manually edit this file, but it's good to know where it is. If you're using version control, make sure to include this file to share your pinned objects with your team.

---

## Troubleshooting & Best Practices

*   **"Object not found in scene" warning:** This means that the object is in a diffrent scene.
*   **"Missing Refrence:"** This means the scene object you pinned has been deleted. You can safely remove it from the Quick Inspector.
*   **Best Practice:** Use pages to keep your workspace organized. For example, you could have a page for each major feature of your game, or for different types of assets.
*   **Resetting the tool:** If you ever want to start from scratch, you can use the "Reset" button (refresh icon) in the toolbar. This will clear all objects and pages.

---


## Contact

If you have any questions, suggestions, or run into any issues, please feel free to contact me at:

*   **Email:** maharajastudiocustomerservice@gmail.com
  
---

## Thank You

Thank you for purchasing the Ultimate Quick Inspector! I hope it helps you streamline your workflow and be more productive in Unity. If you find this tool useful, please consider leaving a review on the Unity Asset Store.
