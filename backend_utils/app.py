from flask import Flask, jsonify
from backend_utils.logging.app_logger import get_app_logger
from backend_utils.config.settings import APP_ENV

app = Flask(__name__)
logger = get_app_logger()

# Mock data
ITEMS = [
    {"id": 1, "name": "pen", "price": 10},
    {"id": 2, "name": "book", "price": 100},
    {"id": 3, "name": "notebook", "price": 50}
]

@app.route("/items", methods=["GET"])
def get_items():
    logger.info("GET /items accessed")
    return jsonify(ITEMS), 200

if __name__ == "__main__":
    logger.info(f"Starting Flask app in {APP_ENV.upper()} environment")
    app.run(host="127.0.0.1", port=5000, debug=True)
