"""Game constants and configuration parameters for automation-tool-39."""

from enum import Enum
from typing import Dict, Final, Tuple


class GameState(Enum):
    """Enumeration of recognized in-game state screens."""

    UNKNOWN: int = 0
    MAIN_MENU: int = 1
    IN_GAME: int = 2
    INVENTORY_OPEN: int = 3
    LOADING: int = 4


# Target rendering resolution for template matching
TARGET_RESOLUTION: Final[Tuple[int, int]] = (1920, 1080)

# Main loop execution speed parameters
TARGET_FPS: Final[int] = 60
FRAME_DELAY: Final[float] = 1.0 / TARGET_FPS

# RGB color targets for UI detection
HEALTH_BAR_COLOR: Final[Tuple[int, int, int]] = (220, 40, 40)
MANA_BAR_COLOR: Final[Tuple[int, int, int]] = (40, 100, 220)

# Default keybindings for standard macro controls
DEFAULT_KEYMAP: Final[Dict[str, str]] = {
    "move_forward": "w",
    "move_backward": "s",
    "strafe_left": "a",
    "strafe_right": "d",
    "use_potion": "1",
    "open_inventory": "i",
    "primary_skill": "space",
}

# Inventory grid specification (rows, columns)
INVENTORY_SLOTS: Final[Tuple[int, int]] = (5, 8)

# Detection threshold tolerances
COLOR_MATCH_TOLERANCE: Final[float] = 0.85
ACTION_TIMEOUT_SECONDS: Final[float] = 10.0
