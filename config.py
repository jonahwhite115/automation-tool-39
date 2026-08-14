import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_configuration()

    def load_configuration(self):
        default_config = self.load_json(self.default_config_path)
        user_config = self.load_json(self.user_config_path)
        return self.merge_configs(default_config, user_config)

    def load_json(self, path):
        if os.path.exists(path):
            with open(path, 'r') as file:
                return json.load(file)
        return {}

    def merge_configs(self, default, user):
        merged = default.copy()
        merged.update(user)
        return merged

# Example usage (uncomment to use):
# config_loader = ConfigLoader('default_config.json', 'user_config.json')
# config = config_loader.config
# print(config)