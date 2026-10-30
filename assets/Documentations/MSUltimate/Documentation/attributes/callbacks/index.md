# Lifecycle & Callback Attributes

> Event triggers executed during Inspector initialization, field mutation, asset saving, undo/redo, or playmode transitions.

---

## Attribute Directory
| Attribute | Target | Description | Status | Doc Link |
| :--- | :--- | :--- | :---: | :--- |
| `[OnAfterSave]` | `Method` | Invoked immediately after an asset or scene is saved to disk. | ✅ Complete | [Read Docs](on-after-save.md) |
| `[OnBeforeSave]` | `Method` | Pre-save hook for validation or data sanitization. | ✅ Complete | [Read Docs](on-before-save.md) |
| `[OnFieldBlur]` | `Field, Property` | Dispatches callback when focus leaves the field element. | ✅ Complete | [Read Docs](on-field-blur.md) |
| `[OnFieldFocus]` | `Field, Property` | Dispatches callback when user clicks or focuses the element. | ✅ Complete | [Read Docs](on-field-focus.md) |
| `[OnInspectorDispose]` | `Method` | Cleanup callback invoked when inspector window closes or selection changes. | ✅ Complete | [Read Docs](on-inspector-dispose.md) |
| `[OnInspectorInit]` | `Method` | Invoked on first layout pass when object is selected in inspector. | ✅ Complete | [Read Docs](on-inspector-init.md) |
| `[OnPlayModeStateChanged]`| `Method` | Dispatched during editor-to-playmode and playmode-to-editor transitions. | ✅ Complete | [Read Docs](on-play-mode-state-changed.md) |
| `[OnSceneGUI]` | `Method` | Dispatches an OnSceneGUI callback for custom in-scene handles. | ✅ Complete | [Read Docs](on-scene-gui.md) |
| `[OnStateUpdate]` | `Method` | Dispatched periodically during inspector update ticks. | ✅ Complete | [Read Docs](on-state-update.md) |
| `[OnUndoRedo]` | `Method` | Invoked when an undo or redo operation modifies target object. | ✅ Complete | [Read Docs](on-undo-redo.md) |
| `[OnValueChanged]` | `Field, Property` | Dispatches callback whenever value changes in inspector. | ✅ Complete | [Read Docs](on-value-changed.md) |
