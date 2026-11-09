import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(
    logger_name: str = "bot_logger",
    log_dir: str = "logs",
    log_filename: str = "automation.log",
    max_bytes: int = 5 * 1024 * 1024,  # 5 MB
    backup_count: int = 5,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures and returns a logger with rotating file and console handlers."""
    logger = logging.getLogger(logger_name)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    logger.setLevel(level)

    # Ensure target directory exists for log files
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    file_path = log_path / log_filename

    # Define unified formatting for gaming event logs
    formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Primary rotating file handler to prevent runaway log sizes
    file_handler = RotatingFileHandler(
        file_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    # Stream handler for live stdout monitor
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    return logger


def get_game_logger(component_name: str) -> logging.Logger:
    """Utility helper to retrieve scoped child loggers for sub-modules."""
    base_logger = setup_logger()
    return base_logger.getChild(component_name)
