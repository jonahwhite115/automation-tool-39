import json
import os

class ConfigLoader:
    def __init__(self, default_config_path: str, user_config_path: str):
        self.default_config = self.load_json(default_config_path)
        self.user_config = self.load_json(user_config_path) if os.path.exists(user_config_path) else {}
        self.final_config = self.merge_configs()

    def load_json(self, path: str) -> dict:
        """Load JSON configuration from a file."""
        with open(path, 'r') as file:
            return json.load(file)

    def merge_configs(self) -> dict:
        """Merge user config with default config."""
        config = self.default_config.copy()
        config.update(self.user_config)
        return config

    def get(self, key: str, default=None):
        """Get a configuration value, return default if not found."""
        return self.final_config.get(key, default)

# Example usage
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json', 'user_config.json')
    print(loader.get('some_setting', 'default_value'))