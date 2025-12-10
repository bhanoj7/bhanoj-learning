import os
from dotenv import load_dotenv

load_dotenv()

def get_env(key: str, default = None):
    return os.getenv(key, default)
settings = {
    "APP_ENV": get_env("APP_ENV","development"),
    "DEBUG": get_env("DEBUG","True"),
    "DATABASE_URL": get_env("DATABASE_URL","sqlite:///local.db"),
    "API_KEY": get_env("API_KEY","default_api_key"), # do not hard code real keys
}
