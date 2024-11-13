import pytest
import json
from app.api_validations.validate_email import validate_email
from app.api_validations.validate_phone import validate_phone_number
from app.api_validations.validate_all import validate_and_get_response
from app.api import app


@pytest.fixture
def app_context():
    # Set up the application context
    with app.app_context():
        yield


def test_email_validity():
    test_emails = [
        "hello@hello.com",
        "hello",
        "hello.",
        "@hello.com",
    ]

    expected_validities = [
        True,
        False,
        False,
        False,
    ]
    for email, expected in zip(test_emails, expected_validities):
        print(f"Testing email: {email} with expected result: {expected}")
        is_valid = validate_email(email)
        error_msg = f'Expected {expected} but got {is_valid}'
        print(f"{email}: {'TEST PASSED' if is_valid == expected else error_msg}")
        assert is_valid == expected


def test_phone_numbers():
    test_numbers = [
        # Valid
        "+1 (123) 456-7890",
        "1 123 456 7890",
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "1234567890",
        "11234567890",
        # Invalid
        "4",
        "(123)",
        "()",
        "--3243"

    ]
    expected_validities2 = [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False
    ]

    for number, expected in zip(test_numbers, expected_validities2):
        is_valid = validate_phone_number(number)
        print(f"{number}: {'TEST PASSED' if is_valid == expected else 'Invalid'}")
        assert is_valid == expected


def test_validate_all(app_context):
    payloads = [
        [{
            "type": "email",
            "recipient": "example@example.com",
            "content": "Hello World"
        }, False],
        [{
            "type": "email",
            "content": "Hello World"
        }, "Missing required field: recipient"],
        [{
            "type": "lol",
            "recipient": "example@example.com",
            "content": "Hello World"
        }, "type must be one of: SMS, email"],
        [{
            "type": "SMS",
            "recipient": "def not a phone number",
            "content": "Hello World"
        }, "Phone number could not be validated"],

    ]

    for payload, expected in payloads:
        output = None
        # try:
        output = validate_and_get_response(payload)

        if expected is False:
            assert output is False
        else:
            assert output[0].json["error"] == expected
