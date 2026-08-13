DEFAULT_CONFIG = {
    'fullscreen': False,
    'resolution': (1920, 1080),
    'volume': 0.5,
    'controls': {
        'move_up': 'W',
        'move_down': 'S',
        'move_left': 'A',
        'move_right': 'D',
        'shoot': 'SPACE',
    },
}

import json
import os

class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG
        self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
            self.config = {**DEFAULT_CONFIG, **user_config}

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
# config_loader = ConfigLoader('user_config.json')
# fullscreen_setting = config_loader.get('fullscreen')
