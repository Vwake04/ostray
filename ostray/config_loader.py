import json
from typing import List, Dict
from abc import ABC, abstractmethod


class IConfigLoader(ABC):
    @abstractmethod
    def load_config(self) -> List[Dict]:
        pass


class JSONConfigLoader(IConfigLoader):
    def __init__(self, config_file: str):
        self.config_file = config_file

    def load_config(self) -> List[Dict]:
        with open(self.config_file, 'r') as file:
            data: dict = json.load(file)
        return data.get("workflows", [])