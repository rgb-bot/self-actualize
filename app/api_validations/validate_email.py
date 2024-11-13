import re

EMAIL_VALIDATE_PATTERN = r"^\S+@\S+\.\S+$"
# # Returns <re.Match object; span=(0, 17), match='hello@hello.com'>
# re.match(email_validate_pattern, "hello@hello.com")


def validate_email(data):
    return re.match(EMAIL_VALIDATE_PATTERN, data) is not None
