import logging
from flask import jsonify
from .validate_phone import validate_phone_number
from .validate_email import validate_email

logger = logging.getLogger(__name__)

# Returns False (no response needed) if no errors detected


def validate_and_get_response(data):
    if not data:
        logger.error("No data provided in the request")
        return jsonify({"error": "No data provided"}), 400

    # Validate that all required fields are in the request
    required_fields = ['type', 'recipient', 'content']
    for field in required_fields:
        if field not in data:
            logger.error("Missing required field: %s", field)
            return jsonify({"error": f"Missing required field: {field}"}), 400

    for field in required_fields:
        # Validate that each field is a non-empty string
        if not isinstance(data[field], str) or not data[field]:
            logger.error("%s must be a non-empty string", field)
            return jsonify({"error": f"{field} must be a non-empty string"}), 400

    if data['type'] not in ["SMS", "email"]:
        return jsonify({"error": "type must be one of: SMS, email"}), 400

    if data['type'] == "email":
        if not validate_email(data['recipient']):
            return jsonify({"error": "Email is could not be validated"}), 400
    else:
        if not validate_phone_number(data['recipient']):
            return jsonify({"error": "Phone number could not be validated"}), 400

    return False
