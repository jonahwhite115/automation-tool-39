import logging
import sys
from pathlib import Path

# Configure global logging for automation-tool-39
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    """Initializes and returns a configured logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Console output for real-time monitoring
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File output for persistent audit logs
        file_handler = logging.FileHandler(LOG_DIR / "app.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger