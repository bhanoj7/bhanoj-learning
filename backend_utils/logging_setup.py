from backend_utils.config import get_log_level
import logging

level_name = get_log_level()
level = getattr(logging, level_name)