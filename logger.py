import logging
import os
from datetime import datetime

# Configure logging for automation-tool-39 gaming data processing
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DIR = 'logs'

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Initializes a standard logger instance for gaming telemetry."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.now().strftime('%Y-%m-%d')
    log_file = os.path.join(LOG_DIR, f"game_data_{timestamp}.log")

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

def log_performance_metrics(logger: logging.Logger, data: dict):
    """Formats and logs internal telemetry data dictionary."""
    metric_string = " | ".join([f"{k}: {v}" for k, v in data.items()])
    logger.info(f"METRIC_UPDATE: {metric_string}")