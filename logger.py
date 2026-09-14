import logging
import os
import sys

def setup_logger(name: str, log_file: str = 'automation.log'):
    """Configures a robust logger for automation-tool-39."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    try:
        # Ensure directory exists for log file
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    except (PermissionError, OSError) as e:
        # Fallback to console if file logging fails
        print(f"Critical: Failed to initialize log file at {log_file}: {e}", file=sys.stderr)
        stream_handler = logging.StreamHandler()
        logger.addHandler(stream_handler)
    
    return logger

# Global instance for tool-wide use
logger = setup_logger('automation-tool-39')

def log_error(exception: Exception, context: str = "unknown process"):
    """Standardized error logging for edge case management."""
    if not isinstance(exception, Exception):
        logger.error(f"Invalid error type received in {context}")
        return
    
    logger.error(f"Exception occurred in {context}: {str(exception)}", exc_info=True)