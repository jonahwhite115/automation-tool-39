import os

# screen coordinate ranges for game engine interactions
GAME_SCREEN_WIDTH = 1920
GAME_SCREEN_HEIGHT = 1080

# paths for automation assets and cache
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, 'assets')
CACHE_DIR = os.path.join(BASE_DIR, '.cache')

# retry configuration for network requests and input hooks
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 1.5

# color profiles for image processing
COLOR_THRESHOLD = 0.85
UI_HIGHLIGHT_COLOR = (255, 215, 0)

# input timing constants in milliseconds
CLICK_HOLD_DURATION = 150
INPUT_COOLDOWN = 500

# logging configuration
LOG_FILE = 'automation-tool.log'
LOG_LEVEL = 'INFO'

# environment validation keys
REQUIRED_ENV_VARS = ['GAME_PATH', 'API_KEY']