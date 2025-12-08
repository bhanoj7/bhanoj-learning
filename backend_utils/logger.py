import logging
from backend_utils.log_config import get_log_level, get_handlers

def get_logger():
    logger = logging.getLogger("app Logger")
    logger.setLevel(get_log_level())
    if not logger.handlers:
        for h in get_handlers():
            logger.addHandler(h)
    return logger