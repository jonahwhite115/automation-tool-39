import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_window": "GameTitle",
    "fps_limit": 60,
    "hotkeys": {
        "start_macro": "f9",
        "stop_macro": "f10",
        "emergency_exit": "f12",
    },
    "auto_save_interval": 300,
    "debug_mode": False,
    "ocr_confidence_threshold": 0.85,
}


def merge_dicts(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge override dictionary into base dictionary."""
    result = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads JSON configuration file and merges it with default gaming settings."""
    if not os.path.exists(config_path):
        save_config(DEFAULT_CONFIG, config_path)
        return DEFAULT_CONFIG.copy()

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
        return merge_dicts(DEFAULT_CONFIG, user_config)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Failed to load {config_path} ({e}). Using defaults.")
        return DEFAULT_CONFIG.copy()


def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """Saves current configuration dictionary to a JSON file."""
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
