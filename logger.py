import logging
import os
from datetime import datetime

class AutomationLogger:
    """Handles application logging with edge case safety."""

    def __init__(self, log_dir: str = "logs"):
        self.log_dir = log_dir
        self._ensure_log_directory()
        self.logger = logging.getLogger("automation-tool-39")
        self._configure_logger()

    def _ensure_log_directory(self) -> None:
        """Create directory if missing, handle permission edge cases."""
        try:
            if not os.path.exists(self.log_dir):
                os.makedirs(self.log_dir, exist_ok=True)
        except OSError as e:
            print(f"Critical: Failed to create log directory: {e}")

    def _configure_logger(self) -> None:
        """Standard file logging setup with basic formatting."""
        self.logger.setLevel(logging.INFO)
        log_path = os.path.join(self.log_dir, f"run_{datetime.now().strftime('%Y%m%d')}.log")
        
        try:
            handler = logging.FileHandler(log_path)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        except (PermissionError, IOError) as e:
            print(f"Warning: Logger file inaccessible: {e}")

    def log_error(self, message: str, exc: Exception = None) -> None:
        """Safe logging of errors with exception detail."""
        if exc:
            self.logger.error(f"{message}: {str(exc)}", exc_info=True)
        else:
            self.logger.error(message)

    def log_info(self, message: str) -> None:
        """General info logging for operational transparency."""
        if message:
            self.logger.info(message)