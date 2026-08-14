import os

class Config:
    """Configuration management for the application."""
    def __init__(self):
        self.env = os.getenv('ENVIRONMENT', 'development')
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///:memory:')
        self.logging_level = os.getenv('LOGGING_LEVEL', 'INFO')

    def display_config(self):
        """Prints the current configuration values."""
        print(f'Environment: {self.env}')
        print(f'Database URL: {self.database_url}')
        print(f'Logging Level: {self.logging_level}')  

# Example usage
if __name__ == '__main__':
    config = Config()
    config.display_config()