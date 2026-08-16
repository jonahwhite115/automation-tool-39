import json
import os

DEFAULT_CONFIG = {
    'screen_resolution': '1920x1080',
    'volume': 75,
    'controls': {
        'jump': 'space',
        'move_left': 'a',
        'move_right': 'd'
    },
    'language': 'English'
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()  # Start with defaults
        self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self.update_config(user_config)

    def update_config(self, user_config):
        self.config.update(user_config)

    def get_config(self):
        return self.config

# Example usage
if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.get_config())