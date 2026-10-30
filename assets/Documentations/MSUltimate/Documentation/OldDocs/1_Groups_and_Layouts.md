# 1. Groups and Layouts

These attributes allow you to organize fields in the Inspector, creating complex layouts using horizontal, vertical, tabbed, and split-pane groups with deep styling control.

---

## `[BoxGroup]`
Groups members into a visually distinct box with a header and customizable background.

**Parameters:**
- `GroupName`: Unique identifier for the box.
- `ShowLabel`: (bool) Show the group header. Default: `true`.
- `CenterLabel`: (bool) Center the header text. Default: `false`.

**Ultimate Control Styling:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `LabelColor` | `string` | Hex color for the header text. |
| `LabelFontSize` | `int` | Font size for the header text. |
| `LabelFontStyle` | `FontStyle` | Font style (Bold, Italic, etc.). |
| `BackgroundColor` | `string` | Hex background color for the box body. |
| `BorderColor` | `string` | Hex border color for the box. |
| `BorderWidth` | `float` | Width of the box border. |
| `BorderRadius` | `float` | Corner radius for the box. |
| `Padding` | `float` | Internal padding for the box content. |
| `MarginTop` / `Bottom` | `float` | External vertical spacing. |

---

## `[VerticalGroup]` & `[HorizontalGroup]`
These attributes are applied to fields to group them into columns or rows. Multiple fields with the same `GroupName` will be consolidated.

**VerticalGroup Features:**
- **Scrolling:** Can wrap content in a `ScrollView` if `Scrollable` is true.
- **Separators:** Optional horizontal lines between items via `ShowSeparator`.
- **Indentation:** Custom `IndentLevel` for child fields.

**HorizontalGroup Features:**
- **Alignment:** Top, Middle, Bottom, or Stretch alignment for the entire row.
- **NoWrap:** Prevents items from wrapping to a new line on overflow.

**Shared Group Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `Title` | `string` | Optional header title for the group. |
| `TitleColor` | `string` | Hex color for the group title text. |
| `Box` | `bool` | If true, applies a background box style. |
| `BackgroundColor` | `string` | Hex background color. |
| `Gap` | `float` | Pixel spacing between child elements. |
| `Collapsible` | `bool` | Enables a collapse toggle for the group. |
| `StartCollapsed`| `bool` | Initial state of the collapsible group. |

---

## `[FoldoutGroup]`
A specialized group that places items inside a toggleable foldout header.

**Features:**
- **Animated:** Smooth expansion/collapse transitions.
- **Header Styling:** Customize `HeaderColor`, `HeaderBackgroundColor`, and `HeaderIcon`.
- **Content Indent:** Optional `IndentContent` with custom `IndentAmount`.

---

## `[BeginHorizontal]` & `[EndHorizontal]`
Marker attributes to start/end a horizontal row block. Ideal for methods or mixed field/method rows.

**Ultimate Control Layout:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `Gap` | `float` | Spacing between items. Default: `5`. |
| `AlignItems` | `string` | Cross-axis alignment: `flex-start`, `center`, `flex-end`, `stretch`. |
| `JustifyContent` | `string` | Main-axis alignment: `flex-start`, `center`, `space-between`, etc. |
| `FlexGrow` | `bool` | If true, the group grows to fill horizontal space. |
| `NoWrap` | `bool` | If true, items will not wrap to the next line. |

---

## `[BeginTabGroup]` & `[EndTabGroup]`
Creates a professional tab-strip UI. Fields between these markers are grouped into a specific tab.

**Tab Strip Styling:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `TabStripAlignment`| `Enum` | `Left`, `Center`, `Right`, `Expand`. |
| `ActiveTabColor` | `string` | Hex color for the active tab background. |
| `TabIndicatorColor`| `string` | Color of the underline/indicator on the active tab. |

---

## `[BeginSplitPane]` & `[EndSplitPane]`
Divides the inspector into two resizable panes (left/right or top/bottom).

**Properties:**
- `Direction`: `Horizontal` or `Vertical`.
- `InitialSplitterPosition`: Starting position in pixels.
- `PaneMinSize`: Minimum allowed size for each pane.
- `ShowCollapseButtons`: Adds buttons to quickly collapse/expand panes.

---

## `[TableList]`
Renders a list or array as a multi-column interactive table.

**Features:**
- **Zebra Striping:** `AlternatingRowBackgroundColor` for readability.
- **Scrollable:** `MaxHeight` constraint enables internal scrolling.
- **Headers:** Toggleable `ShowHeader` with custom `HeaderBackgroundColor`.

---

## `[AdvancedList]`
An extremely powerful list drawer that adds professional management tools to any collection.

**Features:**
- **Pagination:** `ItemsPerPage` control for large collections.
- **Visuals:** Custom `HeaderBackgroundColor`, `BorderColor`, and `ListBackgroundColor`.
- **Logic:** `OnItemAdded` and `OnItemRemoved` callback hooks.
- **Search:** Built-in filtering if configured.
