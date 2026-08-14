import logging

# Configure the logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def critical(self, msg):
        self.logger.critical(msg)

# Example usage
if __name__ == '__main__':
    log = Logger('game_logger')
    log.info('Game started')
    log.warning('Low health warning')
    log.error('Error loading level')