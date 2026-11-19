from typing import Final

# Gaming automation profile configurations
DEFAULT_FRAME_RATE: Final[int] = 60
DEFAULT_RESOLUTION: Final[tuple[int, int]] = (1920, 1080)

# Network timeout settings in seconds
CONNECTION_TIMEOUT: Final[float] = 30.5
RETRY_ATTEMPTS: Final[int] = 3

# File paths for assets
ASSET_DIRECTORY: Final[str] = "./assets"
LOG_FILE_PATH: Final[str] = "./logs/automation.log"

# User-agent identification for scraping
USER_AGENT: Final[str] = "AutomationTool-39/1.0.0"

def get_app_version() -> str:
    """
    Return current automation tool version.

    Returns:
        str: The semantic versioning string.
    """
    return "1.0.0"

class GameState:
    """Container for shared game status constants."""
    RUNNING: Final[str] = "RUNNING"
    PAUSED: Final[str] = "PAUSED"
    LOADING: Final[str] = "LOADING"
    DISCONNECTED: Final[str] = "DISCONNECTED"