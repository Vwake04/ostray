from typing import List
from abc import ABC, abstractmethod

from .persona import Persona, IPersona
from .trigger import Trigger, ITrigger
from .channel import Channel, IChannel


class Workflow:
    def __init__(self, trigger: ITrigger, persona: IPersona, output_channel: IChannel):
        self.trigger = trigger
        self.persona = persona
        self.output_channel = output_channel

    def __repr__(self):
        return f"Workflow(trigger={self.trigger}, persona={self.persona}, output_channel={self.output_channel})"


class IWorkflowManager(ABC):
    @abstractmethod
    def load_workflows(self, config_file: str):
        pass

    @abstractmethod
    def add_workflow(self, workflow: 'Workflow'):
        pass

    @abstractmethod
    def list_workflows(self) -> List['Workflow']:
        pass

    @abstractmethod
    def get_workflow(self, lead_source: str) -> List['Workflow']:
        pass

    @abstractmethod
    def remove_workflow(self, lead_source: str):
        pass


class WorkflowManager(IWorkflowManager):
    def __init__(self):
        self.workflows: List[Workflow] = []

    def load_workflows(self, workflows: dict):
        """Load workflows from a JSON configuration file."""
        for workflow in workflows:
            trigger = Trigger(workflow['lead_source'])
            persona = Persona(workflow['persona']['name'], workflow['persona']['description'])
            output_channel = Channel(workflow['output_channel'])
            self.add_workflow(Workflow(trigger, persona, output_channel))
    
    def add_workflow(self, workflow: Workflow):
        self.workflows.append(workflow)

    def list_workflows(self) -> List[Workflow]:
        return self.workflows

    def get_workflow(self, lead_source: str) -> List[Workflow]:
        return [workflow for workflow in self.workflows if workflow.trigger.get_lead_source() == lead_source]

    def remove_workflow(self, lead_source: str):
        self.workflows = [workflow for workflow in self.workflows if workflow.trigger.get_lead_source() != lead_source]