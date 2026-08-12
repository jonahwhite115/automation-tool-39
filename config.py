import json
import os

class ConfigLoader:
    def __init__(self, default_file='default_config.json', user_file='user_config.json'):
        self.default_file = default_file
        self.user_file = user_file
        self.config = self.load_config()

    def load_config(self):
        defaults = self.load_json(self.default_file)
        user_config = self.load_json(self.user_file) or {}
        return {**defaults, **user_config}

    def load_json(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                return json.load(file)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.get('game_mode', 'casual'))