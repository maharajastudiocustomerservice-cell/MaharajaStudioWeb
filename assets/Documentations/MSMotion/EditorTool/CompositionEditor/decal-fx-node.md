# Decal FX Node

The **Decal FX Node** projects visual decals (such as blood splatters, footstep dirt, scorch marks, magic runes, or bullet impacts) directly onto scene geometry at a designated timestamp during animation playback.

Decals are projected via directional raycasts originating from a skeletal bone or socket, automatically conforming to terrain, floors, walls, and dynamic scene obstacles.

---

## Inspector Parameter Reference

Configure decal projection, materials, dimensions, and pooling in the node details panel:

### Decal Source

Select how the decal graphic is defined:

| Source Mode | Description |
|:---|:---|
| **Prefab** | Instantiates a custom GameObject prefab containing a projection component (such as a URP Decal Projector or custom decal mesh). Supports multiple prefabs for randomized picking. |
| **Material** | Applies an assigned Material asset directly to an automatically generated projector. Supports a list of materials for randomized visual variation. |

*   **Decal Prefab / Prefabs**: Assign one or more prefab assets. When multiple prefabs are provided, the system randomly selects one per trigger.
*   **Decal Material / Materials**: Assign one or more material assets for direct projection.

---

### Surface Raycasting

Controls the raycast query that detects surfaces to receive the decal:

*   **Raycast Direction**: The local or world direction along which the surface detection ray is cast (e.g., `(0, -1, 0)` to project downward onto the floor).
*   **Max Ray Distance**: The maximum search distance (in meters) from the socket origin to look for receiving geometry.
*   **Surface Normal Acceptance Angle**: The maximum allowed slope angle between the ray direction and the hit surface normal (default: `75°`). Surfaces steeper than this threshold reject the decal, preventing unnatural stretching on vertical cliffs or walls.
*   **Layer Mask**: Specifies which physics layers are eligible to receive projected decals (e.g. `Default`, `Ground`, `Environment`).

---

### Size & Dimensions

Fine-tune the projected decal's scale and footprint:

*   **Decal Size (m)**: Base footprint dimension in meters.
*   **Scale Multiplier**: A uniform scale factor applied on top of the base decal size.
*   **Non-Uniform Scale**: Toggle to independently control the width (**X**) and length (**Y**) of the decal on the surface plane. Ideal for directional skid marks, slash stains, angled weapon impacts, and blood drips.

---

### Attachment & Lifetime

*   **Attach to Hit Object**: When checked, parents the spawned decal to the hit surface GameObject. This ensures decals stay planted on moving platforms, elevators, or dynamic vehicles.
*   **Fade In**: Smoothly ramps the decal opacity/alpha from 0 to full on spawn.
*   **Fade Out**: Smoothly fades the decal out at the end of its duration before removal.
*   **Max Active Decals**: Sets the maximum number of concurrent decals permitted for this event slot. When the limit is reached, the oldest decal is automatically recycled (0 = unlimited).
*   **Use Pool**: Recycles decal GameObjects using the internal object pool instead of instantiating and destroying them. Always keep this enabled for high-frequency events (such as sprint footsteps or rapid projectile impacts) to maintain zero runtime garbage collection.

---

### URP Decal Projector Settings

When using Universal Render Pipeline (URP) Decal Projector components:

*   **Normal Blend**: A slider from `0.0` (flat decal projection) to `1.0` (full surface normal interaction), controlling how the decal interacts with underlying surface normal maps and lighting.

---

### Scene View Gizmos

*   **Show Decal Gizmos**: Displays an interactive projection cone, surface detection ray, and hit boundary circle in the Scene View for visual alignment.
*   **Gizmo Color / Ray Color / Normal Color**: Customizable viewport colors for the projection bounds, ray path, and surface normal indicator.
