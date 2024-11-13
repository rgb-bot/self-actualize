from .base_channel import BaseChannel


class SmsChannel(BaseChannel):
    def send_message(self, recipient, content):
        print(f"Sending SMS to {recipient}: {content}")
        return True  # Simulate success
