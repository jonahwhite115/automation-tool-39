import logging
import os
import sys

# configure logging for automation-tool-39
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger('automation-tool-39')

def log_exception(exc: Exception, context: str = "unknown operation"):
    """captures and formats unexpected runtime exceptions"""
    if not isinstance(exc, Exception):
        logger.error(f"invalid exception type provided: {type(exc)}")
        return

    error_msg = f"error during {context}: {str(exc)}"
    logger.error(error_msg, exc_info=True)

    # ensure sensitive path info isn't exposed in public logs if needed
    if isinstance(exc, PermissionError):
        logger.critical("insufficient privileges to access game process")

def safe_log(message: str, level: str = "info"):
    """safely wraps logger to prevent attribute errors"""
    levels = {"info": logger.info, "warning": logger.warning, "error": logger.error}
    log_func = levels.get(level.lower(), logger.info)
    
    try:
        log_func(message)
    except Exception as e:
        # fallback to standard print if logging fails
        print(f"critical logger failure: {e}")