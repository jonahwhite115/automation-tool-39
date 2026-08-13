import logging

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('game_log.log')
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_debug(self, message):
        try:
            self.logger.debug(message)
        except Exception as e:
            self.logger.error(f'Failed to log debug message: {e}')

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f'Failed to log info message: {e}')

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.logger.error(f'Failed to log warning message: {e}')

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.logger.error(f'Failed to log error message: {e}')

    def log_critical(self, message):
        try:
            self.logger.critical(message)
        except Exception as e:
            self.logger.error(f'Failed to log critical message: {e}')
