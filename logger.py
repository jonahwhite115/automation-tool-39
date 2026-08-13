import logging
from logging.handlers import RotatingFileHandler

# Logger setup function

def setup_logger(log_file='game_log.log', max_bytes=10*1024*1024, backup_count=5):
    """Sets up a rotating logger."""
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

# Example of how to use the logger
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logging has started.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
