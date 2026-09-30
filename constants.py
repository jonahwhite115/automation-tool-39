"""Centralized constants for gaming automation tool."""

from enum import Enum, auto
from typing import Final, NamedTuple

# Timing and Delays (in seconds)
DEFAULT_TICK_RATE: Final[float] = 0.05
MAX_RETRY_TIMEOUT: Final[float] = 10.0
HUMAN_INPUT_JITTER: Final[tuple[float, float]] = (0.02, 0.08)

# Screen and Detection Thresholds
DEFAULT_SCREEN_RESOLUTION: Final[tuple[int, int]] = (1920, 1080)
IMAGE_MATCH_THRESHOLD: Final[float] = 0.85
COLOR_TOLERANCE: Final[int] = 12


class GameState(Enum):
    """Supported internal automation states."""
    UNKNOWN = auto()
    MAIN_MENU = auto()
    IN_GAME = auto()
    IN_COMBAT = auto()
    LOADING = auto()
    PAUSED = auto()
    INVENTORY_OPEN = auto()


class KeyBind(NamedTuple):
    """Structure for mapping key combinations."""
    primary_key: str
    modifier: str | None = None


# Default Hotkeys Configuration
DEFAULT_HOTKEYS: Final[dict[str, KeyBind]] = {
    "HEALTH_POTION": KeyBind(primary_key="1"),
    "MANA_POTION": KeyBind(primary_key="2"),
    "OPEN_INVENTORY": KeyBind(primary_key="i"),
    "TOGGLE_PAUSE": KeyBind(primary_key="p", modifier="ctrl"),
    "ESCAPE_MENU": KeyBind(primary_key="esc"),
}


def get_hotkey(action_name: str) -> KeyBind | None:
    """Retrieve hotkey configuration for a specific action."""
    return DEFAULT_HOTKEYS.get(action_name.upper())
