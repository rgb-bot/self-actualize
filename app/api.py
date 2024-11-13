import logging
from flask import Flask, request, jsonify
from app.api_validations.validate_all import validate_and_get_response
from app.models import db
from app.config import SQLALCHEMY_DATABASE_URI
from app.services import commit_log
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # This sets the log level to DEBUG
logger = logging.getLogger(__name__)


@app.route('/sendMessage', methods=['POST'])
def send_message():
    logger.info("sendMessage route was hit")  # Log the route hit

    data = request.json
    logger.debug(f"Received data: {data}")  # Log the data received

    error_msg = validate_and_get_response(data)

    if error_msg is not False:
        return error_msg

    try:
        log = commit_log(data, logger)
        logger.debug(f"Commited message to db: {log}")
        return jsonify({"message": "Message Sent"}), 200
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500
    except ValueError as e:
        logger.error(f"Value error: {str(e)}")
        return jsonify({"error": "Invalid data format"}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
