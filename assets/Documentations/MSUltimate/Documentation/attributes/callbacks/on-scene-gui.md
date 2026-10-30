# [OnSceneGUI]

> Executes custom 3D scene handle and GUI drawing logic directly from your MonoBehaviour without writing a custom Editor script.

---

## 1. Overview & Value Proposition

**What it does:**
Lets you draw interactive 3D handles, curves, and scene overlays directly inside your script without creating a separate Editor class.

**The Problem:**
In standard Unity, drawing interactive handles (like custom movement discs, spline control points, or bounding box manipulators) requires creating a dedicated `Editor` script in an `Editor` folder, inheriting from `Editor`, and overriding `OnSceneGUI()`. This creates 2x more files and fractures your component code.

**The Solution:**
Add `[OnSceneGUI]` directly above a method in your MonoBehaviour:
- **No Custom Editor Needed:** Draw `UnityEditor.Handles` directly from your component file.
- **Interactive In-Scene Handles:** Adjust patrol points, attack ranges, and spawn arcs directly with mouse handles in the Scene View.
- **Selection Filtering:** Optionally run only when the object is actively selected (`RequireSelected = true`).
- **Clean Editor Separation:** Automatically stripped from game builds so runtime performance is 100% untouched.

---

## 2. Quick Start

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
#if UNITY_EDITOR
using UnityEditor;
#endif

public class PatrolPath : MonoBehaviour
{
    public Vector3 targetOffset = new Vector3(5, 0, 0);

#if UNITY_EDITOR
    [OnSceneGUI]
    private void DrawSceneHandles()
    {
        Vector3 worldTarget = transform.position + targetOffset;
        Handles.color = Color.green;
        Handles.DrawLine(transform.position, worldTarget);
        targetOffset = Handles.PositionHandle(worldTarget, Quaternion.identity) - transform.position;
    }
#endif
}
```

---

## 3. Compatibility & Specification

| Specification | Value |
| :--- | :--- |
| **Package** | MSUltimate Core |
| **Attribute Target** | `Method | Field | Property` |
| **Supported Types** | Parameterless methods, or methods accepting `SceneView` |
| **Allow Multiple** | Yes (`AllowMultiple = true`) |
| **Inherited** | Yes |
| **UI Toolkit Compatible** | Yes |

---

## 4. Constructors & Parameters

```csharp
public OnSceneGUIAttribute()
public OnSceneGUIAttribute(string methodName)
public OnSceneGUIAttribute(string methodName, bool requireSelected)
```

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `methodName` | `string` | `null` | Optional method name when placing the attribute on a field instead of directly on the method. |
| `requireSelected` | `bool` | `true` | When true, handles are drawn only when this GameObject is actively selected in the Hierarchy. |

---

## 5. Properties & Customization Table

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `RequireSelected` | `bool` | `true` | Restricts drawing to when the object is selected in the Editor. |
| `MethodName` | `string` | `null` | Target method name invoked when attribute decorates a field or property. |
| `Order` | `int` | `0` | Drawing priority relative to other scene callbacks. |

---

## 6. Production-Grade Example

```csharp
using UnityEngine;
using MaharajaStudio.MSUltimate.Runtime;
#if UNITY_EDITOR
using UnityEditor;
#endif

public class LaunchCannon : MonoBehaviour
{
    [Header("Aiming Trajectory")]
    public float firingPower = 20f;
    public float firingAngleDegrees = 45f;

#if UNITY_EDITOR
    [OnSceneGUI(RequireSelected = true)]
    private void DrawTrajectoryArc()
    {
        Vector3 startPos = transform.position;
        Vector3 dir = Quaternion.Euler(-firingAngleDegrees, transform.eulerAngles.y, 0) * Vector3.forward;

        Handles.color = new Color(1f, 0.5f, 0f, 0.8f);
        Handles.DrawDottedLine(startPos, startPos + dir * (firingPower * 0.5f), 4f);
        Handles.Label(startPos + dir * (firingPower * 0.5f), $"Power: {firingPower:F1} | Angle: {firingAngleDegrees:F0}°");
    }
#endif
}
```

---

## 7. Stacking & Compatibility Matrix

| Feature / Attribute | Compatibility | Notes |
| :--- | :---: | :--- |
| `[ScenePositionHandle]` | Supported | Pair with MSUltimate Scene Debug attributes for declarative scene gizmos. |
| `[Range]` | Supported | Use range sliders in the Inspector while interacting with in-scene handles. |
| `[BoxGroup]` | Supported | Fully functional inside layout containers. |
