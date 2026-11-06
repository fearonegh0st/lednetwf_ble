"""Built-in scenes for hc3 "carrier wave symphony" IOTBT devices (0xE1 0x21).

Product 197 (0x00C5, IOTBT* name, e.g. the Aurelux Christmas tree) has no
scene_data_v3 function, so the 0xE0 0x02 effect command is ignored. Its
vendor app (Zengge Magic Home 2 white-label "Aurelux") plays scenes by
sending a full scene description with the voice_control_ii custom-mode
command, built by app_common_command_lib/voice_control_ii/builder.dart
::buildCustomModeHEXCommand. Layout, recovered from the app's compiled code:

    E1 21 preview brightness type otherMode direction density speed rotate
          bg[hs_hi hs_lo v cct cctV]
          count  count x [hs_hi hs_lo v cct cctV]

- preview: 0 = apply, 1 = preview
- brightness, density, speed: 0-100 (app sends 100 when the scene disables
  density/speed; direction defaults to 1, rotate to 1)
- hs_hi/hs_lo: (hue << 7) | saturation, hue 0-359, saturation 0-100
  (the same packing as the 0x3B / v3 colour commands)
- v: colour value 0-100, cct: 0-100, cctV: white level 0-100
- bg: background colour; the app uses black when a scene has none
- at most 8 colours

The scene table is the app's built-in "cycle" preset list
(biz_control_page/.../voice_control_ii_cycle_default_data.dart), with the
Chinese preset names translated to English.
"""
from __future__ import annotations

from typing import NamedTuple

HC3_SCENE_PRODUCT_IDS = frozenset({197})


class HC3Scene(NamedTuple):
    """One built-in scene: (h, s, v, cct, cctV) colours."""

    type: int
    speed: int
    density: int
    direction: int
    other_mode: int
    rotate: int
    colors: tuple[tuple[int, int, int, int, int], ...]


HC3_SCENES: dict[str, HC3Scene] = {
    "Fireworks Celebration": HC3Scene(36, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 100), (120, 100, 100, 0, 100), (240, 100, 100, 0, 100), (60, 100, 100, 0, 100), (300, 100, 100, 0, 100), (180, 100, 100, 0, 100), (0, 0, 100, 0, 100))),
    "Tech Vibe": HC3Scene(31, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Twinkling Starry Sky": HC3Scene(9, 80, 100, 1, 0, 1, ((210, 100, 100, 0, 100), (240, 100, 100, 0, 100))),
    "Advertising": HC3Scene(22, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 100), (120, 100, 100, 0, 100), (240, 100, 100, 0, 100), (60, 100, 100, 0, 100), (300, 100, 100, 0, 100), (180, 100, 100, 0, 100), (0, 0, 100, 0, 100))),
    "Rainbow Flow": HC3Scene(14, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Quality Outline": HC3Scene(11, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Courtyard": HC3Scene(2, 80, 80, 1, 0, 1, ((18, 100, 100, 0, 100), (0, 0, 100, 0, 0))),
    "Wedding Vows": HC3Scene(15, 80, 100, 5, 0, 1, ((330, 100, 100, 0, 100), (0, 0, 100, 0, 100), (330, 100, 100, 0, 100))),
    "Garden Picnic": HC3Scene(29, 80, 100, 1, 0, 1, ((180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0), (330, 100, 100, 0, 100))),
    "Children's Day": HC3Scene(22, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Trend": HC3Scene(15, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Game": HC3Scene(32, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Party": HC3Scene(34, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Gentle Candlelight": HC3Scene(2, 80, 80, 1, 0, 1, ((0, 0, 0, 0, 100),)),
    "Iceland Blue": HC3Scene(15, 80, 100, 1, 0, 1, ((240, 100, 100, 0, 0), (210, 100, 100, 0, 100), (180, 100, 100, 0, 100))),
    "Starry Ceiling": HC3Scene(13, 80, 3, 5, 0, 1, ((228, 100, 100, 0, 0), (0, 0, 100, 0, 0))),
    "Meteor Ceiling": HC3Scene(13, 80, 3, 5, 0, 1, ((0, 0, 100, 0, 0), (35, 100, 100, 0, 100))),
    "Dynamic Streamline": HC3Scene(13, 80, 3, 1, 1, 1, ((180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Midnight City": HC3Scene(35, 80, 100, 5, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Late Autumn": HC3Scene(15, 80, 100, 1, 0, 1, ((30, 100, 100, 0, 100), (11, 100, 100, 0, 100))),
    "Planet Journey": HC3Scene(37, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 100), (120, 100, 100, 0, 100), (240, 100, 100, 0, 100), (60, 100, 100, 0, 100), (300, 100, 100, 0, 100), (180, 100, 100, 0, 100), (0, 0, 100, 0, 100))),
    "Volcanic Eruption": HC3Scene(11, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 100), (60, 100, 100, 0, 100), (0, 0, 100, 0, 100))),
    "Meteor Shower": HC3Scene(11, 80, 100, 5, 0, 1, ((240, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Glacier Express": HC3Scene(15, 80, 100, 1, 0, 1, ((240, 100, 100, 0, 100), (40, 100, 100, 0, 100))),
    "Firefly Night": HC3Scene(2, 80, 80, 1, 0, 1, ((19, 100, 100, 0, 100),)),
    "Dream Fireworks": HC3Scene(10, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 0), (120, 100, 100, 0, 100), (240, 100, 100, 0, 100), (60, 100, 100, 0, 100), (300, 100, 100, 0, 100), (180, 100, 100, 0, 100), (0, 0, 100, 0, 100))),
    "Neon World": HC3Scene(4, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Moonlit Path": HC3Scene(18, 80, 80, 1, 0, 1, ((0, 0, 0, 0, 100), (0, 0, 0, 100, 100))),
    "Candlelight Dinner": HC3Scene(2, 80, 80, 1, 0, 1, ((18, 100, 100, 0, 100),)),
    "Champagne Party": HC3Scene(17, 80, 80, 1, 0, 1, ((0, 0, 100, 0, 0), (300, 100, 100, 0, 0), (0, 100, 100, 0, 0), (240, 100, 100, 0, 100), (180, 100, 100, 0, 100), (60, 100, 100, 0, 0))),
    "Movie Night": HC3Scene(25, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 100), (120, 100, 100, 0, 100), (240, 100, 100, 0, 100), (60, 100, 100, 0, 100), (300, 100, 100, 0, 100), (180, 100, 100, 0, 100), (0, 0, 100, 0, 100))),
    "Dream Meteor": HC3Scene(13, 80, 3, 1, 0, 1, ((0, 100, 100, 0, 0), (300, 100, 100, 0, 0), (240, 100, 100, 0, 0), (180, 100, 100, 0, 0), (120, 100, 100, 0, 0), (60, 100, 100, 0, 0))),
    "Dynamic Rhythm": HC3Scene(10, 80, 100, 1, 0, 1, ((0, 0, 100, 0, 0), (240, 100, 100, 0, 100), (120, 100, 100, 0, 100), (0, 100, 100, 0, 100), (180, 100, 100, 0, 0), (300, 100, 100, 0, 100), (60, 100, 100, 0, 0))),
    "Easter": HC3Scene(4, 80, 100, 1, 0, 1, ((0, 100, 100, 0, 100), (14, 100, 100, 0, 100), (0, 0, 100, 0, 0))),
    "Christmas 2": HC3Scene(29, 80, 100, 1, 0, 1, ((11, 100, 100, 0, 100), (120, 100, 100, 0, 100), (60, 100, 100, 0, 100), (0, 0, 100, 0, 100))),
    "Sunset Breeze": HC3Scene(10, 80, 100, 1, 0, 1, ((0, 0, 0, 0, 100),)),
    "Halloween 3": HC3Scene(29, 80, 80, 1, 0, 1, ((6, 100, 100, 0, 100), (271, 100, 100, 0, 100), (120, 100, 56, 0, 100), (120, 100, 100, 0, 100))),
    "Velvet Dream Time": HC3Scene(11, 80, 100, 5, 0, 1, ((0, 0, 0, 0, 100),)),
    "Warm Afterglow": HC3Scene(15, 80, 100, 1, 0, 1, ((0, 0, 0, 0, 100), (0, 0, 0, 96, 100))),
}


def _color_bytes(h: int, s: int, v: int, cct: int, cct_v: int) -> list[int]:
    packed = ((h % 360) << 7) | max(0, min(100, s))
    return [
        (packed >> 8) & 0xFF,
        packed & 0xFF,
        max(0, min(100, v)),
        max(0, min(100, cct)),
        max(0, min(100, cct_v)),
    ]


def build_hc3_scene_payload(
    scene: HC3Scene,
    brightness: int = 100,
    speed: int | None = None,
    preview: bool = False,
) -> bytearray:
    """Build the raw 0xE1 0x21 payload (without the transport header)."""
    payload = [
        0xE1,
        0x21,
        1 if preview else 0,
        max(1, min(100, brightness)),
        scene.type & 0xFF,
        scene.other_mode & 0xFF,
        scene.direction & 0xFF,
        max(0, min(100, scene.density)),
        max(0, min(100, scene.speed if speed is None else speed)),
        scene.rotate & 0xFF,
    ]
    payload += _color_bytes(0, 0, 0, 0, 0)  # background: black
    colors = scene.colors[:8]
    payload.append(len(colors))
    for color in colors:
        payload += _color_bytes(*color)
    return bytearray(payload)


# Static multi-colour palettes (the Aurelux app's Color tab palette swatches).
# Sent with the P3 static-colourful command, built by
# command_protocol_lib/wifi&ble/P3_1314_EC.dart ::buildP3StaticColorfulCmd and
# voice_control_ii_color_biz_component ::sendP3IIStaticColorful:
#
#     EC 01 00 brightness  then for every LED point: hs_hi hs_lo v cct cctV
#
# The app fills every point with the palette colours repeated in order
# (point i gets colours[i % len(colours)]). Colours are (hue, sat, value).
HC3_PALETTES: dict[str, tuple[tuple[int, int, int], ...]] = {
    "Amy's Christmas": ((0, 100, 100), (120, 100, 100), (240, 100, 100),
                        (180, 100, 100), (275, 100, 100), (60, 100, 100)),
    "Red & Green": ((0, 100, 100), (120, 100, 100)),
    "Red, White & Blue": ((0, 100, 100), (0, 0, 100), (240, 100, 100)),
    "Yellow & Red": ((60, 100, 100), (0, 100, 100)),
    "Purple & Orange": ((275, 100, 100), (30, 100, 100)),
}

HC3_DEFAULT_POINTS = 16


def build_hc3_palette_payload(
    colors: tuple[tuple[int, int, int], ...],
    brightness: int = 100,
    points: int = HC3_DEFAULT_POINTS,
) -> bytearray:
    """Build the raw 0xEC 0x01 static palette payload (no transport header)."""
    if not colors:
        raise ValueError("colors is empty")
    payload = [0xEC, 0x01, 0x00, max(1, min(100, brightness))]
    for i in range(max(1, points)):
        h, s, v = colors[i % len(colors)]
        payload += _color_bytes(h, s, v, 0, 0)
    return bytearray(payload)
