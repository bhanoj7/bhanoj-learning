import os
import logging

def get_log_level():
    env = os.getenv("ENV", "development")
    if env == "production":
        return logging.INFO
    return logging.DEBUG

def get_handlers():
    env = os.getenv("ENV","development")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    file_handler = logging.FileHandler("app.log")
    file_handler.setFormatter(formatter)
    if env == "production":
        return [stream_handler, file_handler]
    return [stream_handler]

