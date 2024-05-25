from abc import ABC, abstractmethod


class IPersona(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class Persona(IPersona):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def __repr__(self):
        return f"Persona(name={self.name}, description={self.description})"
