import os

# Constants for game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# File paths
ASSETS_DIR = os.path.join('assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')

# Game states
MENU = 'menu'
PLAYING = 'playing'
PAUSED = 'paused'
GAME_OVER = 'game_over'

# Default settings
DEFAULT_VOLUME = 0.5
DEFAULT_DIFFICULTY = 'normal'

# Other game constant values
MAX_SCORE = 1000
PLAYER_LIVES = 3
