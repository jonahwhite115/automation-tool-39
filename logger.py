import logging
import sys
from pathlib import Path

# Configure centralized logging for automation-tool-39
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("automation_tool")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Console handler
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)

# File handler
file_handler = logging.FileHandler(LOG_DIR / "runtime.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_logger(name: str) -> logging.Logger:
    """Returns a child logger for module specific context."""
    return logger.getChild(name)

def log_performance(func):
    """Decorator for tracking execution timing."""
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logger.debug(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper