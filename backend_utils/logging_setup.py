import logging
from logging.handlers import RotatingFileHandler

def get_logger(name: str):
    logger = logging.getLogger(name)
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


# Run this file directly to test
if __name__ == "__main__":
    logger = get_logger("")
    for i in range(200):
        logger.info(f"Log entry {i}")
