import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(
    name: str = "automation_tool",
    log_file: str = "logs/automation.log",
    max_bytes: int = 5 * 1024 * 1024,  # 5 MB limit per log file
    backup_count: int = 5,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures and returns a rotating file logger for long-running bot sessions."""
    # Ensure the target directory for logs exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if the logger is imported multiple times
    if not logger.handlers:
        # Detailed format string for precise tracking of gaming bot actions
        formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Rotating File Handler to prevent disk exhaustion during unattended runs
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

        # Standard Output stream handler for real-time terminal feedback
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)

    return logger


# Export standard package logger instance
game_logger = setup_logger()
