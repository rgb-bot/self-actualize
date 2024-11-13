import re

# Define the regular expression pattern for a U.S. phone number
PHONE_PATTERN = r"^(\+1|1)?\s*\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"


def validate_phone_number(phone_number):
    # Use re.match to check if the input matches the pattern
    return re.match(PHONE_PATTERN, phone_number) is not None
