from .email_channel import EmailChannel
from .sms_channel import SmsChannel

class ChannelFactory:
    channels = {
        "email": EmailChannel,
        "sms": SmsChannel,
    }

    @classmethod
    def get_channel(cls, type):
        channel_class = cls.channels.get(type.lower())
        if not channel_class:
            raise ValueError(f"Unsupported channel type: {type}")
        return channel_class()