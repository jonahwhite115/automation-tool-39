import os

# Screen coordinate ratios for resolution independence
SCREEN_CENTER = (0.5, 0.5)
DEFAULT_TOLERANCE = 0.05

# Gaming automation constants
DEFAULT_FRAME_RATE = 60
RETRY_ATTEMPTS = 3
TIMEOUT_SECONDS = 10.0

# Directory structures for automation-tool-39
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(BASE_DIR, 'assets')
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# User agent and API keys
DEFAULT_HEADERS = {
    'User-Agent': 'AutomationTool39-Bot/1.0',
    'Accept': 'application/json'
}

# Supported game state codes
STATE_IDLE = 0
STATE_INGAME = 1
STATE_MENU = 2
STATE_ERROR = -1

# Thresholds for visual recognition
CONFIDENCE_THRESHOLD = 0.85
COLOR_MATCH_EPSILON = 10