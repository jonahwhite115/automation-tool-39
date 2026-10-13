import logging
import sys
from typing import Optional

class AutomationLogger:
    """Custom logger for automation-tool-39 game events."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log informational game status updates."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        """Log critical failures during execution."""
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message: str) -> None:
        """Log verbose data for troubleshooting."""
        self.logger.debug(message)

def get_logger(name: str) -> AutomationLogger:
    """Factory function to instantiate tool loggers."""
    return AutomationLogger(name)