import os

# Gaming automation configuration settings
VERSION = "1.2.0"
APP_NAME = "automation-tool-39"

# Resource thresholds and constraints
MAX_RETRIES = 5
TIMEOUT_SECONDS = 30
POLL_INTERVAL_MS = 500

# Game-specific memory offsets and key mappings
BASE_MEMORY_OFFSET = 0x400000
KEY_ATTACK = "f1"
KEY_INTERACT = "e"
KEY_INVENTORY = "i"

# Directory structure and file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
DATA_DIR = os.path.join(BASE_DIR, "data")
SCREENSHOT_PATH = os.path.join(DATA_DIR, "screenshots")

# User agent and API headers for game services
HEADERS = {
    "User-Agent": f"{APP_NAME}/{VERSION}",
    "Content-Type": "application/json"
}

# Recognized game process identifiers
SUPPORTED_PROCESSES = {
    "game_client": "game_x64.exe",
    "launcher": "game_launcher.exe"
}

def get_abs_path(filename: str) -> str:
    """Utility to resolve file paths within the tool."""
    return os.path.join(DATA_DIR, filename)