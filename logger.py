import logging
import sys
from typing import Optional

def setup_logger(name: str = "automation", log_file: str = "bot.log", level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a custom logger for gaming automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler for realtime feedback
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler for persistent session logs
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def log_action(logger: logging.Logger, action: str, status: str = "SUCCESS", details: Optional[str] = None) -> None:
    """Helper to record structured gaming bot actions."""
    message = f"Action: {action} | Status: {status}"
    if details:
        message += f" | Details: {details}"

    status_upper = status.upper()
    if status_upper == "SUCCESS":
        logger.info(message)
    elif status_upper in ("WARNING", "WARN"):
        logger.warning(message)
    else:
        logger.error(message)
