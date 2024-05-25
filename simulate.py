import time

from ostray.logger import Logger
from ostray.lead import LeadProcessor
from ostray.simulator import Simulator
from ostray.workflow import WorkflowManager
from ostray.config_loader import JSONConfigLoader

# Setup configuration
config_loader = JSONConfigLoader('workflows_config.json')
workflows = config_loader.load_config()
workflow_manager = WorkflowManager()
workflow_manager.load_workflows(workflows)

# Setup logger and lead processor
logger = Logger('lead_processing.log')
lead_processor = LeadProcessor(workflow_manager, logger)

# Start lead simulator
simulator = Simulator(lead_processor)
simulator.start()

# Run the simulator for a while then stop
try:
    time.sleep(30)  # Simulate for 30 seconds
finally:
    simulator.stop()