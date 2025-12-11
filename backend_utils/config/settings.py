import os
from dotenv import load_dotenv
from .constants import (
    ENV_DEVELOPMENT,
    ENV_PRODUCTION,
    ENV_TESTING,
    DEFAULT_LOG_LEVEL
)

# WHAT? Loads key-value pairs from .env file into environment variables.
# WHY? Prevents hard-coding secrets in code.
load_dotenv()

# WHAT? Reads env variable OR fallback default.
# WHY? Ensures app does not crash if variable missing.
def get_env(key: str, default: str = None):
    return os.getenv(key, default)


# WHAT? Determine which environment app is running.
# WHY? Different settings for DEV, PROD, TEST.
APP_ENV = get_env("APP_ENV", ENV_DEVELOPMENT)


# WHAT? DEBUG flag.
# WHY? Enable debug only in local environment, not in production.
DEBUG = get_env("DEBUG", "False").lower() == "true"


# WHAT? Database connection string.
# WHY? Never store DB credentials in code.
DATABASE_URL = get_env("DATABASE_URL")


# WHAT? Logging level.
# WHY? Debug logs only in DEV, not in PROD.
LOG_LEVEL = get_env("LOG_LEVEL", DEFAULT_LOG_LEVEL)


# WHAT? Sensitive API keys.
# WHY? Must NEVER be hard-coded → security risk.
API_KEY = get_env("API_KEY")


# WHY? Environment-specific overrides.
# WHAT? Different configs based on environment.
if APP_ENV == ENV_PRODUCTION:
    DEBUG = False
    LOG_LEVEL = "WARNING"        # Reduce log noise in PRODUCTION

elif APP_ENV == ENV_TESTING:
    DEBUG = False
    LOG_LEVEL = "ERROR"          # Only errors during automated tests