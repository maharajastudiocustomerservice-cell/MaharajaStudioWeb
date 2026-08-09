# Changelog

All notable changes to the MSMotion Animation Editor will be documented in this file.

## [4.6] - 2026-08-05

### Fixed
- Fixed an issue where extra bones and finger bones could not be edited correctly during animation authoring.

## [4.5] - 2026-07-26

### Added
- **Time Warper (Advanced Tool)**: Introduced an advanced retiming system for non-linear time warping.
  - Custom Warp Curve authoring (Input Time vs. Output Time).
  - Includes presets: Linear, Ease In, Ease Out, Snappy, and Anticipate.
  - Support for Per-Bone Overrides, allowing individual bones to have different timings.
  - Intelligent Humanoid Bone Grouping: Automatically consolidates hundreds of directional muscle curves into logical bone names (e.g. *Left Arm*, *Spine*).
  - Configurable baking FPS to ensure curve fidelity after warping.
  - Options to Apply destructively (with Undo support) or Export as a new `.anim` file.
- **Remove Root Motion (Advanced Tool)**: Added dedicated tooling to strip existing root motion from animations.
  - Separate toggles for Position and Rotation removal.
  - Option to "Flatten to First Frame" to lock the character at its starting offset instead of snapping to zero.

### Fixed
- Fixed an issue where the "Add Bone Override" generic menu would show "No animated bones found" for Humanoid clips due to empty path filtering.
- Fixed a UI Toolkit `ArgumentException` in the bone list by correctly managing callback registration and element `userData`.
- Fixed UI layout overlap issues in advanced tool foldouts (e.g., Toggles overlapping labels in the Remove Root Motion panel).
