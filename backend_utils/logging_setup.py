import logging
from logging.handlers import RotatingFileHandler

def get_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    # Rotating File Handler
    file_handler = RotatingFileHandler("app.log",maxBytes=2000,backupCount=3)
    file_handler.setFormatter(formatter)

    # Stream Handler (console)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


