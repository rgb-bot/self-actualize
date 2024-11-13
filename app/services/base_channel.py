class BaseChannel:
    def send_message(self, recipient, content):
        raise NotImplementedError(
            "Send message must be implemented by subclasses.")
