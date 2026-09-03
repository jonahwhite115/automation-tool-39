import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 60,
    "action_delay_ms": 100,
    "hotkeys": {
        "start": "f10",
        "stop": "f11",
        "pause": "f12"
    },
    "game_window_title": "GameWindow",
    "debug_mode": False,
    "capture_region": [0, 0, 1920, 1080]
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file and merges it with default gaming settings.

    Args:
        config_path: Path to the configuration file.

    Returns:
        A dictionary containing the merged configuration.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        try:
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=4)
        except IOError:
            pass
        return config

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
            # Deep merge nested hotkeys dictionary
            if "hotkeys" in user_config and isinstance(user_config["hotkeys"], dict):
                config["hotkeys"].update(user_config["hotkeys"])
                del user_config["hotkeys"]

            config.update(user_config)
    except (json.JSONDecodeError, KeyError, IOError):
        # Fallback to default values if loading fails
        pass

    return config
