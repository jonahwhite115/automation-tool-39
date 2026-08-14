import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name, log_file, level=logging.INFO):
    # Create a logger with the given name
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)
    
    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger('GameLogger', 'game_log.log')
    log.info('Logger setup complete.')
    log.warning('This is a warning message.')
    log.error('This is an error message.')