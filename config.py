import json
import os

class ConfigError(Exception):
    pass

def load_config(filepath):
    if not os.path.isfile(filepath):
        raise ConfigError(f'Config file {filepath} does not exist.')

    try:
        with open(filepath, 'r') as file:
            config = json.load(file)
    except json.JSONDecodeError:
        raise ConfigError(f'Config file {filepath} is not a valid JSON.')
    except Exception as e:
        raise ConfigError(f'An error occurred while reading the config file: {str(e)}')
    
    required_keys = ['game_name', 'version', 'settings']
    for key in required_keys:
        if key not in config:
            raise ConfigError(f'Missing required config key: {key}')
    
    return config

# Example usage if needed:
# if __name__ == '__main__':
#     try:
#         config = load_config('config.json')
#         print(config)
#     except ConfigError as e:
#         print(e)
