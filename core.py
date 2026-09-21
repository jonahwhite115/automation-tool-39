import logging

logger = logging.getLogger('automation-tool-39')

class GameSession:
    def __init__(self, session_id):
        self.session_id = session_id
        self.is_active = True

    def execute_command(self, cmd_data: dict):
        """Process command with bounds and type validation."""
        try:
            if not isinstance(cmd_data, dict):
                raise ValueError("invalid command format")
            
            action = cmd_data.get('action')
            value = cmd_data.get('value', 0)
            
            if not action:
                raise KeyError("missing command action")
            
            if not (0 <= value <= 100):
                raise ValueError("value out of range")
                
            # Simulate command execution
            return f"executed {action} at {value}"
            
        except (ValueError, KeyError) as e:
            logger.error(f"session {self.session_id} error: {e}")
            return None
        except Exception as e:
            logger.critical(f"unexpected system fault: {e}")
            self.is_active = False
            return None

    def shutdown(self):
        self.is_active = False
        logger.info(f"session {self.session_id} terminated gracefully")