import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

# Example usage
if __name__ == '__main__':
    app_logger = Logger('MyGameApp')
    app_logger.info('Game started')
    app_logger.warning('Low health warning')
    app_logger.error('An error occurred')
    app_logger.debug('Debugging the starting process')