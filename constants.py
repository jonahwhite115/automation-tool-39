from typing import Final, Dict, List

# Configuration constants for automation-tool-39 gaming sessions

# Supported game resolution modes
RESOLUTION_MODES: Final[Dict[str, tuple]] = {
    "1080p": (1920, 1080),
    "1440p": (2560, 1440),
    "4k": (3840, 2160),
}

# Default interval settings for polling automation
POLLING_INTERVALS: Final[Dict[str, float]] = {
    "fast": 0.1,
    "normal": 0.5,
    "slow": 1.0,
}

# API endpoints for game server interactions
API_ENDPOINTS: Final[Dict[str, str]] = {
    "status": "https://api.gaming-server.local/v1/status",
    "telemetry": "https://api.gaming-server.local/v1/telemetry",
    "action": "https://api.gaming-server.local/v1/input",
}

# Maximum retry attempts for network operations
MAX_RETRIES: Final[int] = 5

# Supported character classes within the game environment
CHARACTER_CLASSES: Final[List[str]] = [
    "warrior",
    "mage",
    "rogue",
    "paladin",
    "ranger"
]

# Global timeout duration for blocking operations in seconds
CONNECTION_TIMEOUT: Final[float] = 30.0

def get_resolution_aspect_ratio(mode: str) -> float:
    """Calculates aspect ratio for a specific resolution mode."""
    width, height = RESOLUTION_MODES.get(mode, (1920, 1080))
    return width / height