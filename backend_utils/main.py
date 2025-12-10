from backend_utils.config.settings import settings

print("Running in:",settings["APP_ENV"])
print("Database URL:", settings["DATABASE_URL"])