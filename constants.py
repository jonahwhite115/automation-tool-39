from typing import Final, Dict

# Configuration limits for automation-tool-39
MAX_RETRIES: Final[int] = 3
REQUEST_TIMEOUT: Final[float] = 30.0

# Gaming platform status codes
STATUS_SUCCESS: Final[int] = 200
STATUS_RATE_LIMITED: Final[int] = 429
STATUS_SERVER_ERROR: Final[int] = 500

# Data handling constants
DEFAULT_ENCODING: Final[str] = 'utf-8'
SUPPORTED_PLATFORMS: Final[list[str]] = ['steam', 'epic', 'xbox', 'playstation']

def get_platform_timeout(platform: str) -> float:
    """Returns specific request timeout for gaming platform."""
    timeouts: Dict[str, float] = {
        'steam': 15.0,
        'epic': 20.0,
        'xbox': 25.0,
        'playstation': 25.0
    }
    return timeouts.get(platform, REQUEST_TIMEOUT)

# Formatting defaults
DATE_FORMAT: Final[str] = '%Y-%m-%d %H:%M:%S'
LOG_FILE_PATH: Final[str] = 'logs/automation_tool.log'
MAX_LOG_SIZE_MB: Final[int] = 5