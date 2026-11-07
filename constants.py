import os

# Configuration paths for gaming automation
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Default application settings
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
POLLING_INTERVAL = 0.5

# Gaming specific constants
SCREEN_RESOLUTION = (1920, 1080)
CAPTURE_REGION = (0, 0, 1920, 1080)
PIXEL_TOLERANCE = 5

# Supported input mechanisms
INPUT_METHODS = ['keyboard', 'mouse', 'direct_input']

# Resource cleanup settings
TEMP_FILE_PREFIX = 'auto_'
CLEANUP_EXTENSIONS = ['.tmp', '.log.old']

def get_resource_path(filename: str) -> str:
    """Constructs full path for internal game resources."""
    return os.path.join(DATA_DIR, filename)

# Exit codes for the automation engine
STATUS_SUCCESS = 0
STATUS_ERROR_INIT = 1
STATUS_ERROR_EXECUTION = 2
STATUS_ERROR_CLEANUP = 3