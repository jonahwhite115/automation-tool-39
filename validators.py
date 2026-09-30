import re

class InputValidator:
    """
    handles validation for gaming automation inputs
    """
    @staticmethod
    def validate_coordinates(x, y):
        if not (isinstance(x, int) and isinstance(y, int)):
            return False
        return 0 <= x <= 1920 and 0 <= y <= 1080

    @staticmethod
    def validate_action_delay(delay):
        try:
            value = float(delay)
            return 0.1 <= value <= 60.0
        except (ValueError, TypeError):
            return False

    @staticmethod
    def validate_command(command):
        allowed_patterns = [r'^click_\d+x\d+$', r'^press_[a-z0-9]+$', r'^wait_\d+$']
        return any(re.match(p, command) for p in allowed_patterns)

def run_validation_cycle(data):
    """
    main loop validation check for incoming packets
    """
    results = {
        "coords": InputValidator.validate_coordinates(data.get('x'), data.get('y')),
        "delay": InputValidator.validate_action_delay(data.get('delay')),
        "command": InputValidator.validate_command(data.get('cmd', ''))
    }
    
    if not all(results.values()):
        return False, f"validation failure: {results}"
    
    return True, "success"