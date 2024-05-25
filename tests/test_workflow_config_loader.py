import json
import pytest
from typing import List

from ostray.workflow import WorkflowManager, Workflow
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


def test_load_workflows(config):
    json_config = JSONConfigLoader(config)
    workflows = json_config.load_config()
    workflow_manager = WorkflowManager()
    workflow_manager.load_workflows(workflows)
    workflows = workflow_manager.list_workflows()

    assert len(workflow_manager.workflows) == 1
    assert workflows[0].trigger.get_lead_source() == "Salesforce"
    assert workflows[0].persona.get_name() == "GPT-3"
    assert workflows[0].output_channel.get_channel_type() == "WhatsApp"
