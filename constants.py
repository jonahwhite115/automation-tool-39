import enum

# Gaming data configuration constants

class GamePlatform(enum.Enum):
    STEAM = "steam"
    EPIC = "epic_games"
    GOG = "gog"
    XBOX = "xbox_pc"

# Standardized status codes for automation tasks
class TaskStatus(enum.IntEnum):
    PENDING = 0
    RUNNING = 1
    COMPLETED = 2
    FAILED = 3

# Data directory paths for automation-tool-39
DEFAULT_DATA_DIR = "data/logs"
BACKUP_DIR = "data/backups"

# Throttle limits for API requests to prevent bans
MAX_REQUESTS_PER_MINUTE = 30
REQUEST_TIMEOUT_SECONDS = 15

# Supported save file extensions
SAVE_FILE_EXTENSIONS = {".sav", ".dat", ".json", ".xml"}

# Schema validation thresholds
REQUIRED_FIELDS = {"user_id", "timestamp", "game_id", "action"}

def is_supported_file(filename: str) -> bool:
    """Checks if a file extension is supported for processing."""
    return any(filename.endswith(ext) for ext in SAVE_FILE_EXTENSIONS)

# Error logging templates
ERROR_MESSAGES = {
    "AUTH_FAIL": "Authentication token expired or invalid",
    "PARSE_FAIL": "Failed to parse game save data",
    "NETWORK_ERR": "Connection interrupted while syncing data"
}