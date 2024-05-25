import json
import pytest

from ostray.config_loader import JSONConfigLoader


@pytest.fixture
def config():
    sample_config = {
        "workflows": [
            {
                "lead_source": "Salesforce",
                "persona": {"name": "GPT-3", "description": "AI Sales Agent"},
                "output_channel": "WhatsApp"
            }
        ]
    }

    path = "test_config.json"

    with open(path, "w") as file:
        file.write(json.dumps(sample_config))

    return path

@pytest.fixture
def empty_config():
    sample_config = {}
    path = "empty_test_config.json"
    
    with open(path, "w") as file:
        file.write(json.dumps(sample_config))

    return path


def test_load_config(config):
    config_loader = JSONConfigLoader(config)
    loaded_config = config_loader.load_config()
    assert len(loaded_config) == 1
    assert loaded_config[0]["lead_source"] == "Salesforce"


def test_load_config_empty(empty_config):
    config_loader = JSONConfigLoader(empty_config)
    config = config_loader.load_config()
    assert len(config) == 0
