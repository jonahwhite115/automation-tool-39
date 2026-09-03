from typing import Final

# Network and connection constants
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Game interaction settings
CLICK_DELAY: Final[float] = 0.5
FRAME_RATE_LIMIT: Final[int] = 60

# Asset directories and paths
ASSET_DIR: Final[str] = "./assets"
LOG_DIR: Final[str] = "./logs"
CONFIG_FILE: Final[str] = "settings.yaml"

# Supported game states
STATE_IDLE: Final[str] = "idle"
STATE_RUNNING: Final[str] = "running"
STATE_ERROR: Final[str] = "error"

def get_timeout_multiplier(base_delay: float) -> float:
    """Calculates timeout based on provided base delay multiplier."""
    return float(base_delay * DEFAULT_TIMEOUT)

# Valid screen resolutions
SCREEN_RESOLUTIONS: Final[list[tuple[int, int]]] = [
    (1920, 1080),
    (2560, 1440),
    (3840, 2160)
]