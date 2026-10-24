import logging
import sys
from datetime import datetime

def get_logger(name: str) -> logging.Logger:
    """Configures a standardized logger for automation-tool-39."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def log_execution_start(task_name: str):
    """Utility to mark the beginning of a game automation task."""
    logger = get_logger('automation')
    logger.info(f'Starting execution of task: {task_name}')

def log_error(task_name: str, error: Exception):
    """Utility to report exceptions with context."""
    logger = get_logger('automation')
    logger.error(f'Task {task_name} failed: {str(error)}')

def log_performance(duration: float):
    """Logs execution duration for performance monitoring."""
    logger = get_logger('automation')
    logger.info(f'Task completed in {duration:.2f} seconds')
