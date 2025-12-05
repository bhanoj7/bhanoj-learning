import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            "level": record.levelname,
            "message": record.getMessage(),
            "timestamp": self.formatTime(record, "%Y-%m-%d %H:%M:%S")
        }
        return json.dumps(log_obj)

def get_json_logger():
    logger = logging.getLogger("json_logger")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())

    logger.addHandler(handler)
    return logger
