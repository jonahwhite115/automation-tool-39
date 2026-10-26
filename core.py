import time
import logging

# Gaming automation loop core

def validate_user_input(command: str) -> bool:
    """Ensures command strings meet game protocol."""
    valid_commands = {'move', 'attack', 'loot', 'rest'}
    return command.strip().lower() in valid_commands

def process_automation():
    """Main execution loop for task automation."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('automation-tool-39')
    
    logger.info("Starting automation sequence...")
    
    # Mock input stream
    commands = ['move', 'invalid_cmd', 'attack', 'loot']
    
    for cmd in commands:
        if not validate_user_input(cmd):
            logger.warning(f"Discarding malformed input: {cmd}")
            continue
            
        try:
            logger.info(f"Executing action: {cmd}")
            time.sleep(0.5)
        except Exception as e:
            logger.error(f"Unexpected loop interruption: {e}")
            break

if __name__ == '__main__':
    process_automation()