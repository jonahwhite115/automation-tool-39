import logging
import os
from logging.handlers import RotatingFileHandler

# Create a logger object
logger = logging.getLogger('GameLogger')
logger.setLevel(logging.DEBUG)

# Define log file path
log_file_path = os.path.join(os.getcwd(), 'game.log')

# Create a rotating file handler
handler = RotatingFileHandler(log_file_path, maxBytes=5*1024*1024, backupCount=3)
handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Logging example
logger.info('Logger setup complete. Ready to log events.')