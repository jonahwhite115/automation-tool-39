import logging
import sys
from pathlib import Path

# automation-tool-39 game log configuration
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Initializes a standard console and file logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    # Console output
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    # File output
    file_handler = logging.FileHandler(LOG_DIR / f"{name}.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def log_game_action(logger: logging.Logger, action: str, details: str = ""):
    """Helper for standardized game event logging."""
    logger.info(f"ACTION: {action} | DETAILS: {details}")

if __name__ == "__main__":
    game_logger = setup_logger("automation-tool-39")
    log_game_action(game_logger, "INITIALIZE", "system boot sequence initiated")