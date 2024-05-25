import pytest
from unittest.mock import MagicMock

from ostray.logger import Logger
from ostray.lead import LeadProcessor, Lead
from ostray.workflow import WorkflowManager, Workflow, Trigger, Persona, Channel


@pytest.fixture
def logger():
    return Logger("dummy_log.log")

@pytest.fixture
def workflow_manager():
    return WorkflowManager()

@pytest.fixture
def lead_processor(workflow_manager, logger):
    return LeadProcessor(workflow_manager, logger)

@pytest.fixture
def sample_workflow():
    return Workflow(Trigger("Salesforce"), Persona("GPT-3", "AI Sales Agent"), Channel("WhatsApp"))

def test_process_lead_with_matching_workflow(
    lead_processor: LeadProcessor, 
    workflow_manager: WorkflowManager, 
    sample_workflow: Workflow
):
    workflow_manager.add_workflow(sample_workflow)
    lead = Lead("Salesforce Lead", "Salesforce")
    lead_processor.route_lead = MagicMock()
    lead_processor.process_lead(lead)
    lead_processor.route_lead.assert_called_once_with(lead, sample_workflow)

def test_process_lead_without_matching_workflow(lead_processor: LeadProcessor):
    lead = Lead("Salesforce Lead", "UnknownSource")
    lead_processor.route_lead = MagicMock()
    lead_processor.process_lead(lead)
    lead_processor.route_lead.assert_not_called()
