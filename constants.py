from typing import Final, Dict

# Configuration constants for automation-tool-39 gaming engine

POLLING_INTERVAL: Final[float] = 0.5
MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[int] = 30

# Map of platform-specific keycodes
INPUT_MAPPING: Final[Dict[str, int]] = {
    "ACTION_JUMP": 0x20,
    "ACTION_FIRE": 0x01,
    "ACTION_RELOAD": 0x52
}

SCREEN_RESOLUTION: Final[tuple[int, int]] = (1920, 1080)
LOG_FILE_PATH: Final[str] = "logs/automation.log"

def get_timeout_buffer() -> float:
    """Returns the padded timeout duration for network operations."""
    return float(TIMEOUT_SECONDS + 5.0)

def get_retry_limit() -> int:
    """Returns the maximum allowed retry count for engine tasks."""
    return MAX_RETRIES