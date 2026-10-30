# 4. Field Drawers & Utilities

These attributes significantly change how individual primitive values or custom class fields are rendered.

### `[CustomSlider(float min, float max)]`
Provides a more aesthetic, configurable slider than Unity's default `[Range]`, offering step-snapping and color themes.

### `[MinMaxSlider(float minLimit, float maxLimit)]`
Renders a dual-handle slider on Vector2 fields or minimum-maximum ranges, ensuring `x` is always less than `y`. 
Optional attribute to force MinMax sliders on numeric `SerializableRange` structures as well.

### `[Searchable]`
Enables a live search bar in the Unity Inspector for a `MonoBehaviour` or `ScriptableObject` field. Apply this to any serialized field to instantly add a filterable search experience above its children, hiding nested properties that don't match the search term.

### `[SerializeReferenceUI]`
Enhances Unity's built in `[SerializeReference]` by providing a type-selector dropdown UI. This allows developers to instantiate any non-abstract derived class of the field's polymorphic base type.

### `[AdvancedClass]`
Applies advanced, beautiful, commercial-grade structural styling to any custom serialized class or struct. Draws the class with deep custom padding, rounded borders, an optional foldout header, and customizable backdrops to clearly distinguish complex structured objects in the layout!

### `[ProgressBar(float min, float max, string color)]`
Renders float or int fields as interactive progress bars. Commonly used for health, energy, or loading metrics.

### `[ValueDropdown(string methodName)]`
Replaces the field's standard text field with a dropdown constraint. The values for the dropdown are generated dynamically by calling the string-specified method or property from within the script!

### `[EnumToggleButtons]`
Flattens Enums into a segmented button toggle control bar so users can quickly tap their choice instead of opening a dropdown menu.

### `[FilePath]`, `[FolderPath]`
Renders string fields with a 'Browse...' button next to them, opening the native OS file explorer and auto-assigning the returned string path relative to the project.

### `[TagSelector]`, `[LayerSelector]`
Converts raw string or int fields into a dropdown constraint based natively on Unity's generated Tag Manager strings or Layer IDs.

### `[Multiline(int lines)]`
Allocates more vertical text space for string fields natively within MSUltimate custom styling configurations.

### `[PasswordField(char maskChar, bool allowReveal)]`
Transforms a string field into a secure, masked password input within the Inspector (e.g., `••••••••`). Includes an optional 👁 toggle button to safely reveal the concealed text when needed. Perfect for API keys, server passwords, and encryption seeds.

### `[ColorWheel(float wheelSize, bool showAlpha, bool showHex)]`
Transforms a standard `Color` field into a massively interactive, inline HSV visual color wheel. By rendering the Hue/Saturation spectrum natively in the inspector and providing dedicated slider toggles for Brightness and Alpha, designers no longer need to click into separate popup windows to adjust color grades!

### `[KeyPad]`
Transforms a string, integer, or float field into an interactive, visually stunning on-screen keyboard right within the Unity Inspector.

**Key Features:**
- **Layouts:** `Numpad` (default), `Calculator`, `Qwerty`, `Phone`, and `Custom` (define your own rows and keys separated by `|` and `,`).
- **Themes:** `Default`, `Dark`, `Light`, `Neumorphism` (elegant 3D popping buttons), and `Hacker` (retro terminal style).
- **Pro Styling Options:** Full control over `ButtonHeight`, `Spacing`, `BorderRadius`, `BackgroundColor`, `ButtonColor`, `TextColor`, and `AccentColor` (for special keys like `AC`, `<`).
- **Shift & Caps Lock (Qwerty):** The Qwerty layout includes a Shift key for one-shot uppercase and a Caps Lock key for persistent uppercase. Shift auto-releases after one character.
- **Special Characters (Qwerty):** Press `?#` to switch to a full symbols layer (`!@#$%^&*()` etc.). Press `ABC` to return to letters.
- **Display Screen:** Optionally enable `ShowDisplayScreen` to show a digital LCD-like readout above the keys.

**Example Usage:**
```csharp
[KeyPad(Layout = KeyPadLayout.Calculator, Theme = KeyPadTheme.Neumorphism, ShowDisplayScreen = true)]
public float calculatorValue;

[KeyPad(Layout = KeyPadLayout.Qwerty, Theme = KeyPadTheme.Hacker, ButtonHeight = 25f)]
public string terminalInput;

[KeyPad(Layout = KeyPadLayout.Custom, CustomKeys = "A,B,C|D,E,F|1,2,3|<", AccentColor = "#ff5555")]
public string customInput;
```

### `[AdvancedCurve]`
A professional AnimationCurve editor with support for custom viewport ranges and color themes.

**Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `CurveColor` | `string` | Hex color for the curve line. |
| `UseCustomRect`| `bool` | If true, uses the `RectRange` for the graph viewport. |
| `RectRange` | `Rect` | The min/max X and Y values for the curve editor view. |

---

### `[SmartEnum]`
Enhances the standard Enum dropdown with a search bar, colored border, and a customizable header.

**Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `ShowSearch` | `bool` | Enables a live filter search bar at the top of the dropdown. |
| `BorderColor` | `string` | Hex color for the dropdown border. |
| `BorderWidth` | `float` | Thickness of the dropdown border. |
| `BackgroundColor`| `string` | Hex background for the search area. |

---

### `[UrlField]`
Displays a string field as a clickable URL link with an optional "Open" button and validation icons.

**Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `ButtonLabel` | `string` | Label for the "Open Link" button. Default: `Open`. |
| `ShowIcon` | `bool` | Shows a globe icon next to the URL. |
| `ButtonColor` | `string` | Hex color for the button. |
| `ValidateUrl` | `bool` | Checks if the string starts with `http://` or `https://`. |

---

### `[ShaderProperty]`
Renders a string or integer (Property ID) field as a smart, searchable dropdown populated with exposed shader properties from a target Material or Shader. Supports deep type filtering (`Color`, `Texture`, `Float`, `Vector`, `Range`, `Keyword`), live color swatch/texture preview, and optional manual custom input.

**Key Features:**
- **Type Filtering:** Filter to only show relevant property types (e.g. only Color properties for a tint picker, or only Texture slots for a normal map picker).
- **Auto-Detection:** Automatically discovers attached `Renderer` components on the same GameObject if no explicit material field is provided.
- **Live Preview:** Displays color swatches and texture thumbnails directly in the dropdown button.
- **Material Keywords:** Also supports inspecting multi-compile shader keywords.

**Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `Filter` | `MSShaderPropertyType` | Filter properties: `All`, `Color`, `Vector`, `Float`, `Texture`, `Range`, `Keyword`. |
| `TargetMaterialMember` | `string` | Optional field/property/method on the component returning a `Material`, `Shader`, or `Renderer`. |
| `CustomShaderPath` | `string` | Optional explicit shader name (e.g. `"Universal Render Pipeline/Lit"`) to inspect without a material instance. |
| `ShowPropertyTypeBadge` | `bool` | Displays type badges like `[Color]`, `[Tex]`, `[Float]` next to names. Default: `true`. |
| `ShowPreviewValue` | `bool` | Displays a live color swatch or texture preview in the inspector. Default: `true`. |
| `AllowCustomInput` | `bool` | Enables a toggle button to type arbitrary custom property names. Default: `true`. |

**Example Usage:**
```csharp
public class MaterialController : ModularMonoBehaviour
{
    public Material targetMaterial;

    [ShaderProperty(TargetMaterialMember = "targetMaterial", Filter = MSShaderPropertyType.Color)]
    public string tintProperty = "_BaseColor";

    [ShaderProperty(TargetMaterialMember = "targetMaterial", Filter = MSShaderPropertyType.Texture)]
    public string albedoMapProperty = "_BaseMap";

    [ShaderProperty(TargetMaterialMember = "targetMaterial", Filter = MSShaderPropertyType.Float)]
    public string metallicProperty = "_Metallic";
}
```

---

### `[AngleGauge]`
Renders a numeric angle or 2D/3D rotation field as an interactive 2D radial dial and compass widget directly in the Unity Inspector.

**Key Features:**
- **Vector Dial Canvas:** Hardware-accelerated UI Toolkit 2D vector dial with tick marks, glowing active angle arc, and a precision needle indicator.
- **Interactive Dragging:** Click and drag anywhere on the circular dial to rotate and set the angle smoothly.
- **Snapping & Presets:** Supports angular snapping (e.g. 15°, 45°, 90°) and 1-click preset buttons (`0° (N)`, `90° (E)`, `180° (S)`, `270° (W)`, `+45°`, `-45°`).
- **Compass Markings:** Displays cardinal direction labels (`N`, `E`, `S`, `W`, `NE`, `SE`, `SW`, `NW`).
- **Radian & Vector Support:** Supports `float`, `int`, `Vector2` (converts between direction and angle), and `Vector3` (Euler rotation).

**Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `Min` / `Max` | `float` | Angular boundaries in degrees. Default: `0` to `360`. |
| `SnapAngle` | `float` | Snap angle interval when dragging (e.g. `15f`, `45f`). `0` for continuous. |
| `ShowCompassDirections` | `bool` | Displays cardinal compass markings. Default: `true`. |
| `ShowQuickButtons` | `bool` | Shows 1-click snap preset buttons (`0°`, `90°`, `180°`, `270°`). Default: `true`. |
| `Radians` | `bool` | If true, stores and formats values in radians instead of degrees. |
| `GaugeSize` | `float` | Diameter of the radial dial in pixels. Default: `84`. |
| `Clockwise` | `bool` | If true, angles increase clockwise (compass). Default: `true`. |
| `NeedleColor` / `ArcColor` | `string` | Custom hex colors for the indicator needle and active arc. |

**Example Usage:**
```csharp
public class WindController : ModularMonoBehaviour
{
    [AngleGauge(Min = 0f, Max = 360f, SnapAngle = 15f, GaugeSize = 90f)]
    public float windDirection = 45f;

    [AngleGauge(Min = -90f, Max = 90f, SnapAngle = 5f, NeedleColor = "#FFA502")]
    public float turretElevation = 0f;

    [AngleGauge(SnapAngle = 45f)]
    public Vector2 launchDirection = Vector2.right;
}
```

---

### `[DecibelVolume]`
Transforms a numeric float or int volume field into a professional, logarithmic Audio Decibel (dB) slider with a dynamic LED/VU level meter, dual dB/linear percentage readouts, a 1-click mute toggle, and quick volume presets.

**Key Features:**
- **Logarithmic Audio Scaling:** Converts linear volume (`0.0` to `1.0`) to true perceptual decibels (`-80 dB` to `+6 dB`), eliminating unintuitive linear volume behavior.
- **Dual Serialization Modes:** Can serialize standard linear `0.0` to `1.0` (for `AudioSource.volume`) OR store raw decibels directly (for `AudioMixer.SetFloat`).
- **Dynamic VU Meter:** Color-graded audio level bar showing green (safe nominal range), yellow (loud / unity gain), and red (clipping / amplified boost).
- **Mute Toggle & Presets:** Quick 1-click mute button (`🔇`) with volume restoration memory and preset buttons (`Mute`, `-20dB`, `-12dB`, `-6dB`, `0dB`, `+3dB`, `+6dB`).

**Properties:**
| Property | Type | Description |
| :--- | :--- | :--- |
| `MinDb` | `float` | Minimum decibel value (representing silence). Default: `-80 dB`. |
| `MaxDb` | `float` | Maximum decibel value (boost limit). Default: `+6 dB`. |
| `StoreAsDecibels` | `bool` | If `true`, serializes raw dB; if `false`, serializes linear `0.0-1.0`. Default: `false`. |
| `ShowVuMeter` | `bool` | Whether to display the visual VU meter bar. Default: `true`. |
| `ShowLinearPercentage` | `bool` | Displays the linear percentage equivalent (e.g. `50.1%`) next to dB. Default: `true`. |
| `ShowPresets` | `bool` | Enables quick preset snap buttons. Default: `true`. |
| `ShowMuteToggle` | `bool` | Enables the 1-click Mute/Unmute speaker button. Default: `true`. |

**Example Usage:**
```csharp
public class AudioManager : ModularMonoBehaviour
{
    // Linear 0.0 - 1.0 serialization with dB inspector control
    [DecibelVolume(MinDb = -80f, MaxDb = 6f)]
    public float masterVolume = 1.0f;

    [DecibelVolume(MinDb = -40f, MaxDb = 0f)]
    public float soundEffectsVolume = 0.8f;

    // Direct AudioMixer raw dB parameter
    [DecibelVolume(StoreAsDecibels = true, MinDb = -80f, MaxDb = 12f)]
    public float mixerMasterDb = 0f;
}
```

---

### `[Hide]`
Completely hides a serialized field from the inspector. This is a cleaner alternative to Unity's `[HideInInspector]` when working within the Modular Editor Attributes ecosystem, ensuring the element is omitted strictly during the UI Toolkit generation phase without interfering with native serialization rules.

### `[MSIgnore]`
Instructs the Modular Editor system to completely bypass all custom decorators and drawers for the applied field. If `[MSIgnore]` is present, any other layout constraints or styling attributes (like `[LabelText]`, `[GUIColor]`, or `[BoxGroup]`) will be ignored, and the field will be drawn using the default native Unity `PropertyField`.


