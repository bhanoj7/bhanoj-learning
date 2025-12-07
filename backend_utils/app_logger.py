import logging
import logging.config
from backend_utils.log_config import LOG_CONFIG

#logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger("app")

def log_startup():
    logger.info("Application started!")
def log_request(path):
    logger.debug(f"Request recieved at {path}")
def log_error(error):
    logger.error(f"ERROR: {error}")