import os
from pathlib import Path
from typing import Optional


def get_env(key: str, default: Optional[str] = None) -> str:
    """
    Read environment variables safely.
    """
    return os.getenv(key, default)


def get_log_level() -> str:
    """
    Decide log level based on ENV variable.
    ENV can be: development, production, testing
    """
    env = get_env("ENV", "development").lower()

    if env == "production":
        return "INFO"
    elif env == "testing":
        return "WARNING"
    return "DEBUG"   # default for development


def get_db_url() -> str:
    """
    Example function: Reads database URL from env.
    """
    return get_env("DB_URL", "postgresql://localhost:5432/learning_db")