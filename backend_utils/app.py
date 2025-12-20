from config.settings import APP_ENV, DEBUG, DATABASE_URL
from logging_setup import get_logger

logger = get_logger(f"App Environment: {APP_ENV}")
logger.info(f"App Environment: {APP_ENV}")
logger.info(f"Debug Mode: {DEBUG}")
logger.info(f"Database URL: {DATABASE_URL}")