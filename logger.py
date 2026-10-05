import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "automation.log") -> logging.Logger:
    """Configures a standardized logger for automation-tool-39."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    log_path = Path(log_file)
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def get_module_logger(name: str) -> logging.Logger:
    """Factory function to retrieve existing module logger."""
    return logging.getLogger(name)