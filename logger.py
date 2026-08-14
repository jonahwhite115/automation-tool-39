import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f'Failed to log info: {e}')

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.logger.error(f'Failed to log warning: {e}')

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.logger.error(f'Failed to log error: {e}')

    def log_debug(self, message):
        try:
            self.logger.debug(message)
        except Exception as e:
            self.logger.error(f'Failed to log debug: {e}')

# Example of using the CustomLogger
if __name__ == '__main__':
    custom_logger = CustomLogger(__name__)
    custom_logger.log_info('This is an info message.')
    custom_logger.log_warning('This is a warning message.')
    custom_logger.log_error('This is an error message.')
    custom_logger.log_debug('This is a debug message.')