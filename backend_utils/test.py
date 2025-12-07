import logging.config
from backend_utils.log_config import LOG_CONFIG
from backend_utils.logging_setup import get_logger
from backend_utils.errors import AppError, ValidationError, DatabaseError
from backend_utils.json_logging import JsonFormatter, get_json_logger
from backend_utils.app_logger import log_startup, log_request, log_error

logger = get_logger()

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

# Example error handling
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        logger.error(f"Error occurred: {e}")

divide(10, 0)

try:
    raise ValidationError("Invalid input format.")
except ValidationError as e:
    logger.error(f"Validation failed: {e}")

logger = get_json_logger()
logger.info("JSON logging working!")

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger()
logger.info("Config-based logging works!")
#Day 23 Practice Test
log_startup()
log_request("/home")
log_error("Failed to load data")





