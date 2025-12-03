import logging
logger = logging.getLogger("app_logger")

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        logger.error("Attempted to divide by 0(zero)")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
print(safe_divide(10, 0))
print(safe_divide("A", 5))

