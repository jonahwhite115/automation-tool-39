import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "automation.log") -> logging.Logger:
    """Initializes a standard logger for automation-tool-39."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Console output for real-time monitoring
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File output for long-term audit
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def log_performance(func):
    """Decorator for tracking function execution time."""
    import time
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        logging.getLogger("performance").debug(f"{func.__name__} took {duration:.4f}s")
        return result
    return wrapper