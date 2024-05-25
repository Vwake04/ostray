from abc import ABC, abstractmethod

from .logger import Logger
from .workflow import IWorkflowManager, Workflow




class ILeadProcessor(ABC):
    @abstractmethod
    def process_lead(self, lead: 'Lead'):
        pass


class Lead:
    def __init__(self, name: str, lead_source: str):
        self.name = name
        self.lead_source = lead_source

    def __repr__(self):
        return f"Lead(name={self.name}, lead_source={self.lead_source})"


class LeadProcessor(ILeadProcessor):
    def __init__(self, workflow_manager: IWorkflowManager, logger: Logger):
        self.workflow_manager = workflow_manager
        self.logger = logger

    def process_lead(self, lead: Lead):
        """Process an incoming lead by routing it to the appropriate workflow."""
        workflows = self.workflow_manager.get_workflow(lead.lead_source)
        if not workflows:
            self.logger.log(f"No workflows found for lead source: {lead.lead_source}")
            return

        for workflow in workflows:
            self.route_lead(lead, workflow)
        
        return workflows

    def route_lead(self, lead: Lead, workflow: Workflow):
        """Route the lead to the designated persona via the specified output channel."""
        self.logger.log(f"Routing lead {lead} to {workflow.persona.get_name()} via {workflow.output_channel.get_channel_type()}")
        return workflow.output_channel
