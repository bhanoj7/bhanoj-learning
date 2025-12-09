from backend_utils.config import get_log_level, get_db_url, get_env

print("ENV", get_env("ENV"))
print("Log Level:", get_log_level())
print("DB URL :", get_db_url())