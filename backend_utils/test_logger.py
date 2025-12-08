import logging

from backend_utils.logger import get_logger

logger = get_logger()

logger.debug("Debug log test")
logger.info("Info log test")
logging.warning("Warning log test")
logging.error("Error log test")
logging.critical("Critical log test")