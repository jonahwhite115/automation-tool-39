import logging
import os
from datetime import datetime

class AutomationLogger:
    """Handles application logging with edge case safety"""

    def __init__(self, log_dir='logs', log_file='automation.log'):
        self.log_dir = log_dir
        self.log_path = os.path.join(log_dir, log_file)
        self._ensure_log_directory()
        
        self.logger = logging.getLogger('automation_tool_39')
        self.logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(self.log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def _ensure_log_directory(self):
        """Creates log directory if access or existence fails"""
        try:
            if not os.path.exists(self.log_dir):
                os.makedirs(self.log_dir, exist_ok=True)
        except (OSError, PermissionError) as e:
            print(f"Critical: Failed to create log directory: {e}")

    def log_event(self, message: str, level: str = 'info'):
        """Safe logging wrapper for game event tracking"""
        try:
            if level.lower() == 'error':
                self.logger.error(message)
            else:
                self.logger.info(message)
        except Exception as e:
            # Fallback output if file system becomes unavailable
            print(f"[{datetime.now()}] Logging failure: {e} | Msg: {message}")