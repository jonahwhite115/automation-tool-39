"""
Game automation constants and configuration structures.
Reorganized to group keybindings, screen region defaults, and color thresholds.
"""

from enum import Enum
from typing import NamedTuple, Tuple


class GameState(Enum):
    UNKNOWN = 0
    LOBBY = 1
    MATCH_SEARCHING = 2
    IN_GAME = 3
    VICTORY_SCREEN = 4
    DEFEAT_SCREEN = 5


class ScreenRegion(NamedTuple):
    x: int
    y: int
    width: int
    height: int


class KeyBinding(Enum):
    PRIMARY_ATTACK = "z"
    SECONDARY_ATTACK = "x"
    HEAL_ITEM = "1"
    MANA_POTION = "2"
    OPEN_INVENTORY = "i"
    CONFIRM_DIALOG = "space"
    CANCEL_DIALOG = "escape"


# Window and graphics constants
GAME_TITLE: str = "Realm Legend Online v1.4"
DEFAULT_WINDOW_SIZE: Tuple[int, int] = (1920, 1080)
TARGET_FPS: int = 60

# Detection & Matching Thresholds
MATCH_CONFIDENCE_THRESHOLD: float = 0.85
COLOR_TOLERANCE_RGB: Tuple[int, int, int] = (15, 15, 15)

# Standard timing delays (in seconds)
ACTION_DELAY_SHORT: float = 0.15
ACTION_DELAY_LONG: float = 0.80
POLL_INTERVAL_FPS: float = 0.05

# Region coordinates relative to standard 1080p window
HEALTH_BAR_REGION = ScreenRegion(50, 40, 300, 25)
MANA_BAR_REGION = ScreenRegion(50, 70, 300, 25)
MINIMAP_REGION = ScreenRegion(1620, 40, 250, 250)
ACTION_BAR_REGION = ScreenRegion(660, 980, 600, 80)
