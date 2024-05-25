from abc import ABC, abstractmethod


class IChannel(ABC):
    @abstractmethod
    def get_channel_type(self) -> str:
        pass

    @abstractmethod
    def publish(self, message: str):
        pass


class Channel(IChannel):
    def __init__(self, channel_type: str):
        self.channel_type = channel_type

    def get_channel_type(self) -> str:
        return self.channel_type
    
    def publish(self, message: str):
        print(f"{self.channel_type}: {message}")

    def __repr__(self):
        return f"Channel(channel_type={self.channel_type})"