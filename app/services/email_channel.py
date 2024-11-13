from .base_channel import BaseChannel

class EmailChannel(BaseChannel):
    def send_message(self, recipient, content):
        print(f"Sending email to {recipient}: {content}")
        return True  # Simulate success