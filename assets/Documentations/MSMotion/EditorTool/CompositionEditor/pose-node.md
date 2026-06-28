# Pose Node

A **Pose Node** is a specialized timeline block that grabs a single, frozen frame from a source Animation Clip and holds that static pose across the node's entire duration. 

Unlike standard animation clips that play over time, the Pose Node is entirely static, acting as a pose hold.

---

## Workflows and Common Uses

Pose Nodes are highly versatile tools for designers and animators. Common use cases include:

* **Hit-Stop / Impact Freezes**: Temporarily pausing a character in an impact pose when a weapon strikes an enemy, before smoothly transitioning back to the attack follow-through.
* **Idle Stance Adjustments**: Freezing a frame from a dynamic movement to serve as a custom, static standing stance on an upper layer.
* **Transition Bridging**: Smoothly blending a moving character into a static frozen pose to bridge two incompatible animations.

---

## Inspector Parameter Reference

When you select a Pose Node, the following parameters are available in the Inspector/Details panel:

* **Clip**: The source Animation Clip asset from which the pose is extracted.
* **Is Embedded**: A checkbox indicating whether the clip asset is physically saved inside this Composition asset (embedded PSD style) or referenced as an external standalone file.
* **Pose Time**: The exact timestamp (in seconds) of the frame you want to extract from the source clip.
  * *For example:* Setting **Pose Time** to `0.5` means the character will freeze at the animation's state exactly 0.5 seconds into the clip.
  * *UI Slider:* Drag the slider to scrub through the clip length and select the target pose visually.
* **Transition In Duration**: Eases the transition from lower layers into the frozen pose.
* **Transition Out Duration**: Eases the transition out of the frozen pose, releasing control back to lower layers.
* **Transition Curve**: Selects the mathematical interpolation shape (**Linear**, **EaseIn**, **EaseOut**, **EaseInOut**, or **Smooth**) used to blend the pose in and out.
