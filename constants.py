import os

# Gaming automation constants
DEFAULT_SCREEN_RESOLUTION = (1920, 1080)
RETRY_ATTEMPTS = 3
TIMEOUT_SECONDS = 15

# Paths and directory configurations
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(BASE_DIR, "assets")
LOGS_PATH = os.path.join(BASE_DIR, "logs")

# Detection sensitivity settings
MATCHING_THRESHOLD = 0.85
FRAME_RATE_LIMIT = 60

# User-agent and network headers
DEFAULT_HEADERS = {
    "User-Agent": "automation-tool-39/1.0.0",
    "Accept": "application/json"
}

# State machine definitions
STATE_IDLE = 0
STATE_ACTIVE = 1
STATE_PAUSED = 2
STATE_ERROR = 3

def get_asset_path(filename: str) -> str:
    """Return full path for game assets."""
    return os.path.join(ASSETS_PATH, filename)

def format_log_path(name: str) -> str:
    """Format log file names with standard extension."""
    return os.path.join(LOGS_PATH, f"{name}.log")