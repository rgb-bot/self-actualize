import pytest
from app.api_validations.validate_email import validate_email
from app.api_validations.validate_phone import validate_phone_number


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
        "+1 (123) 456-7890",
        "1 123 456 7890",
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "1234567890",
        "11234567890",
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
