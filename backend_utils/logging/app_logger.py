import logging
from backend_utils.config.settings import LOG_LEVEL, APP_ENV

def get_app_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(LOG_LEVEL)

    # Stream Handler → prints logs to console
    handler = logging.StreamHandler()

    # Format → include env, log level, message
    formatter = logging.Formatter(
        f"%(asctime)s - {APP_ENV.upper()} - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add only once
    if not logger.handlers:
        logger.addHandler(handler)

    return logger


# Example usage
if __name__ == "__main__":
    logger = get_app_logger()
    logger.info("Application started")
    logger.debug("This is a debug message")
    logger.error("An error occurred")
