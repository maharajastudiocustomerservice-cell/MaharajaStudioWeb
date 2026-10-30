# Scene Debug & Handles Attributes

> In-scene interactive 3D gizmos, manipulation handles, sliders, buttons, and collision bounds rendered directly inside Unity SceneView.

---

## Attribute Directory (17 Attributes)
| Attribute | Target | Description | Status |
| :--- | :--- | :--- | :---: |
| `[InteractiveSceneDebug]` | `Class, Field` | Master controller enabling interactive SceneView debugging overlay. | ⏳ Planned |
| [**`[SceneArrow]`**](scene-arrow.md) | `Field \| Property` | Directional 3D arrow gizmo with interactive tip dragging. | ✅ Complete |
| [**`[SceneBounds]`**](scene-bounds.md) | `Field \| Property` | Visual wireframe/solid bounding box gizmo for bounds and colliders. | ✅ Complete |
| `[SceneBoxHandle]` | `Field` | Interactive 6-handle box scale tool in SceneView. | ⏳ Planned |
| [**`[SceneButton]`**](scene-button.md) | `Method \| Field \| Property` | In-Scene 3D clickable button triggering target method or reset. | ✅ Complete |
| `[SceneDebug]` | `Field` | Overlays live floating label and gizmo marker in SceneView. | ⏳ Planned |
| `[SceneDebugMesh]` | `Field` | Visualizes mesh topology and normals directly in scene. | ⏳ Planned |
| `[SceneDiscHandle]` | `Field` | Interactive angular rotation disc in SceneView. | ⏳ Planned |
| [**`[SceneGrid]`**](scene-grid.md) | `Field \| Property` | Reference coordinate grid on XZ, XY, or YZ planes. | ✅ Complete |
| [**`[SceneLabel]`**](scene-label.md) | `Field \| Property` | World-space floating text label and telemetry readout. | ✅ Complete |
| [**`[SceneLine]`**](scene-line.md) | `Field \| Property` | Connected line segments and interactive waypoint path handles. | ✅ Complete |
| [**`[ScenePositionHandle]`**](scene-position-handle.md) | `Field \| Property` | Standard 3-axis position handle mapped directly to Vector3 field. | ✅ Complete |
| [**`[SceneRadius]`**](scene-radius.md) | `Field \| Property` | Spherical, circular, or hemispherical radius visualization with resize handles. | ✅ Complete |
| [**`[SceneRotationHandle]`**](scene-rotation-handle.md) | `Field \| Property` | 3-axis rotation handle mapped to Quaternion or Euler Vector3. | ✅ Complete |
| [**`[SceneScaleHandle]`**](scene-scale-handle.md) | `Field \| Property` | 3-axis scale handle in SceneView for direct scale adjustments. | ✅ Complete |
| [**`[SceneSlider]`**](scene-slider.md) | `Field \| Property` | In-scene linear slider handle along custom directional vector. | ✅ Complete |
| [**`[ShowInScene]`**](show-in-scene.md) | `Field \| Property` | 3D waypoint marker shape and text label with interactive translation handles. | ✅ Complete |
