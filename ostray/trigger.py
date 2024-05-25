from abc import ABC, abstractmethod


class ITrigger(ABC):
    @abstractmethod
    def get_lead_source(self) -> str:
        pass


class Trigger(ITrigger):
    def __init__(self, lead_source: str):
        self.lead_source = lead_source

    def get_lead_source(self) -> str:
        return self.lead_source

    def __repr__(self):
        return f"Trigger(lead_source={self.lead_source})"
