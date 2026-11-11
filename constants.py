import os

# Gaming automation configuration defaults
POLL_RATE = 0.5
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Supported game client processes
SUPPORTED_CLIENTS = {
    "VALORANT": "VALORANT-Win64-Shipping.exe",
    "LEAGUE": "League of Legends.exe",
    "DOTA2": "dota2.exe"
}

# Directories for resource storage
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

# Coordinate defaults for screen capture
DEFAULT_RESOLUTION = (1920, 1080)
CAPTURE_REGION = (0, 0, 1920, 1080)

# Logging levels and formats
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"

# Exit signals and status codes
STATUS_SUCCESS = 0
STATUS_ERROR = 1
SHUTDOWN_SIGNAL = "SIGINT"