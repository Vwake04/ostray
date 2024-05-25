import json
import pytest
from unittest.mock import patch, mock_open, MagicMock

from ostray.logger import Logger
from ostray.lead import LeadProcessor, Lead
from ostray.workflow import WorkflowManager
from ostray.config_loader import JSONConfigLoader


@pytest.fixture
def config():
    sample_config = {
        "workflows": [
            {
                "lead_source": "Salesforce",
                "persona": {"name": "GPT-3", "description": "AI Sales Agent"},
                "output_channel": "WhatsApp",
            }
        ]
    }

    path = "test_config.json"

    with open(path, "w") as file:
        file.write(json.dumps(sample_config))

    return path


@pytest.fixture
def mock_config_loader(config):
    return JSONConfigLoader(config)


@pytest.fixture
def workflow_manager():
    return WorkflowManager()

@pytest.fixture
def lead_processor(workflow_manager):
    logger = Logger("dummy_log.log")
    return LeadProcessor(workflow_manager, logger)

def test_integration(
    mock_config_loader: JSONConfigLoader,
    workflow_manager: WorkflowManager,
    lead_processor: LeadProcessor,
):
    # Load workflows from the configuration
    workflows = mock_config_loader.load_config()
    workflow_manager.load_workflows(workflows)

    # Simulate processing a lead
    lead = Lead("Salesforce Lead", "Salesforce")

    # Mock the route_lead method to just log the routing for verification
    processed_lead = lead_processor.process_lead(lead)

    # Verify that the lead was processed with the correct workflow
    assert processed_lead[0].output_channel.get_channel_type() == "WhatsApp"
