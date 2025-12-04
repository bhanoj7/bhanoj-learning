from backend_utils.logging_setup import get_logger
from backend_utils.errors import AppError, ValidationError, DatabaseError


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

