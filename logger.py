import logging
from logging.handlers import RotatingFileHandler

# Logger setup function

def setup_logger(log_file='app.log', max_bytes=10*1024*1024, backup_count=5):
    # Create a logger
    logger = logging.getLogger('GameAutomationLogger')
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Create a handler that writes log messages to a file with rotation
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage of the logger
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger initialized successfully')
    log.warning('This is a warning message')
    log.error('This is an error message')