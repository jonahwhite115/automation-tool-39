from typing import Dict, Tuple

# Game state definitions for automation state machine
STATE_UNKNOWN = "unknown"
STATE_MAIN_MENU = "main_menu"
STATE_LOBBY = "lobby"
STATE_LOADING = "loading"
STATE_IN_GAME = "in_game"
STATE_MATCH_END = "match_end"

# Color definitions (RGB) for pixel-detection automation (UI scanning)
COLOR_HEALTH_BAR_RED: Tuple[int, int, int] = (220, 20, 60)
COLOR_SHIELD_BAR_BLUE: Tuple[int, int, int] = (0, 191, 255)
COLOR_ACTIVE_BUTTON_GOLD: Tuple[int, int, int] = (255, 215, 0)
COLOR_TEXT_WHITE: Tuple[int, int, int] = (255, 255, 255)

# Standard scanning resolutions and aspect ratios
TARGET_RESOLUTION: Tuple[int, int] = (1920, 1080)
COLOR_MATCH_TOLERANCE: int = 15  # Acceptable color delta for screen matching

# Item rarity scoring system (useful for sorting inventory data)
RARITY_TIERS: Dict[str, int] = {
    "COMMON": 1,
    "UNCOMMON": 2,
    "RARE": 3,
    "EPIC": 4,
    "LEGENDARY": 5,
    "MYTHIC": 6
}

# Automation delay settings (seconds) to prevent anti-cheat triggers
DELAY_SHORT: float = 0.15
DELAY_MEDIUM: float = 0.5
DELAY_LONG: float = 1.5
DELAY_SAFETY_BUFFER: float = 0.05
