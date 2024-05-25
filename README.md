# Ostray

Ostray is a dynamic workflow management system for handling leads, featuring modules for workflow definition, lead simulation, processing, and logging.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Vwake04/ostray.git
    cd ostray
    ```

2. Install dependencies:
    ```bash
    pip install -e .
    ```

## Running Tests

1. Install `pytest` if not already installed:
    ```bash
    pip install pytest
    ```

2. Run the tests:
    ```bash
    pytest
    ```

## Usage

1. **Define Workflows**: Create a `workflows_config.json` file with your workflow configurations. Example:
    ```json
    {
      "workflows": [
        {
          "lead_source": "Salesforce",
          "persona": {
            "name": "GPT-3",
            "description": "AI Sales Agent"
          },
          "output_channel": "WhatsApp"
        }
      ]
    }
    ```

2. **Run the Application**: Use the following script to start the application:
    ```python
    from ostray.config_loader import JSONConfigLoader
    from ostray.workflow import WorkflowManager
    from ostray.lead_processor import LeadProcessor
    from ostray.logger import Logger
    from ostray.lead import Lead

    # Load workflows from configuration
    config_loader = JSONConfigLoader('workflows_config.json')
    workflows = config_loader.load_config()
    workflow_manager = WorkflowManager()
    workflow_manager.load_workflows(workflows)

    # Process a lead
    logger = Logger('lead_processing.log')
    lead_processor = LeadProcessor(workflow_manager, logger)
    lead = Lead('Salesforce Lead', 'Salesforce')
    lead_processor.process_lead(lead)
    ```

## Run the Simulator
   ```bash
   python simulate.py
   ```


## Project Structure
```
ostray/
├── ostray/
│ ├── init.py
│ ├── channel.py
│ ├── config_loader.py
│ ├── lead.py
│ ├── logger.py
│ ├── persona.py
│ ├── trigger.py
│ ├── workflow.py
├── tests/
│ ├── init.py
│ ├── test_config_loader.py
│ ├── test_integration.py
│ ├── test_lead_processor.py
│ ├── test_workflow_config_loader.py
│ ├── test_workflow_manager.py
├── README.md
├── .gitignore
├── simulate.py
└── pyproject.toml
```
