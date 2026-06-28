# Batch Export Queue

The **Batch Export Queue** is a pipeline optimization tool that allows you to queue multiple animation composition bakes and process them sequentially in a single batch. This prevents the editor from locking up repeatedly during iterative bakes.

---

## Accessing the Batch Queue

There are two primary ways to open the Batch Export Queue window:
1.  **Menu Bar**: Choose **Window > MSMotion > Batch Export Queue** from the Unity editor menu.
2.  **Export Window**: Click the **View Queue** button in the footer of the [Export Options](export-options.md) window.

---

## Adding Jobs to the Queue

Rather than exporting a composition immediately, you can queue it:
1.  Open your composition in the editor and click **Export (💾 Icon)** on the top toolbar.
2.  Configure your settings (Exporter, Custom Range, Root Motion, and Output parameters).
3.  Click **Add to Queue** in the bottom footer of the window. 
4.  The Export Options window will close, and the job will be added to the background queue. The "View Queue" button will update its counter to reflect the new job count.

---

## Managing Queued Jobs

Inside the **Batch Export Queue** window, all pending exports are listed as cards showing the following details:

*   **Job Index**: The position of the job in the baking queue.
*   **Asset Output Name**: The name of the file that will be generated (e.g. `Run_InPlace`).
*   **Source Composition**: The source composition asset being baked.
*   **Range Description**: Displays whether the job bakes the *Full Duration* or a *Custom Time Range*.
*   **Baking Exporter**: The selected exporter mode (e.g. `Humanoid Pose Snapshot` or `Generic Transform Snapshot`).
*   **Output Path**: The target folder path in the project where the generated animation asset will be created.

### Removing Jobs
*   **Remove Single Job (✕)**: Click the red cross button on the right side of any job card to remove that specific bake from the queue.
*   **Clear Queue**: Click the button in the bottom-left corner to empty the entire queue list.

---

## Processing the Batch

Once you have added all desired compositions to the queue:
1.  Open the Batch Export Queue window.
2.  Click **Process All Jobs** in the bottom-right corner.
3.  The editor will sequentially load, solve, and bake each composition asset into its corresponding Animation Clip or FBX file.
4.  A progress tracker will display the current active job being processed. When finished, the queue list will automatically clear, and the status bar will display `All jobs processed successfully`.

---

## Related Guides

*   **Export Options**: Learn about parameters and tabs in [Export Options](export-options.md).
*   **Main Workspace**: Review basic editor features in the [Composition Editor Index](index.md).
