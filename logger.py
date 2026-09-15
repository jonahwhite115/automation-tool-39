import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "automation.log", level: int = logging.INFO) -> logging.Logger:
    """Configures a standard logger for automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # File output for persistent logs
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Stream output for console debugging
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

def log_performance(func):
    """Decorator to measure execution time of gaming routines."""
    import time
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        logging.getLogger("performance").info(f"{func.__name__} took {duration:.4f}s")
        return result
    return wrapper