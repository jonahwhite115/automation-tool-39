import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'automation.log', level: int = logging.INFO):
    """
    Configures a rotating file logger for game automation tasks.
    Max file size: 5MB, keep 3 backup files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotating file handler: 5MB per file, max 3 files
        handler = RotatingFileHandler(
            log_file, maxBytes=5*1024*1024, backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Stream handler for console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Example usage for the automation tool
if __name__ == '__main__':
    game_logger = setup_logger('automation-tool-39')
    game_logger.info('Logger initialized successfully for gaming session')