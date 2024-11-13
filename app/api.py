import logging
from flask import Flask, request, jsonify
from app.api_validations.validate_all import validate_and_get_response
from app.models import Messages, db
from app.config import SQLALCHEMY_DATABASE_URI

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
        # If all validations pass, proceed with the business logic
        logger.info(f"Validated data: {data}")

        message_type = data.get('type')
        recipient = data.get('recipient')
        content = data.get('content')
        # Log message status
        log = Messages(type=message_type, recipient=recipient,
                       content=content, status="success")
        db.session.add(log)
        logger.info(f"Adding message: {log}")
        db.session.commit()
        return jsonify({"message": "Message Sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
