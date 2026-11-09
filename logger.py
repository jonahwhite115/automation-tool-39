import logging
import sys
import os

def setup_logger(name: str, log_file: str = 'automation.log'):
    """Configures a robust logger for gaming tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        try:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            
            # File handler with fallback if disk is full or path restricted
            try:
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
            except (IOError, OSError) as e:
                sys.stderr.write(f"Logging fallback to stderr: {e}\n")
                
            # Console stream handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
            
        except Exception as e:
            # Final safety check for logging system critical failure
            sys.stderr.write(f"Fatal logging setup failure: {e}\n")
    
    return logger

# Global logger instance for the automation tool
log = setup_logger('automation-tool-39')