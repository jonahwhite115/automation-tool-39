import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures a logger instance for automation-tool-39 components.

    Args:
        name: The name of the logger instance.
        level: The logging severity level.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

def log_game_event(logger: logging.Logger, event: str, metadata: Optional[dict] = None) -> None:
    """
    Records specific gaming automation events with optional metadata.

    Args:
        logger: The logger instance to use.
        event: A description of the event.
        metadata: Optional dictionary containing event details.
    """
    msg = f"EVENT: {event}"
    if metadata:
        msg += f" | DATA: {metadata}"
    logger.info(msg)