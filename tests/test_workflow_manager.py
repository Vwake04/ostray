import pytest

from ostray.workflow import WorkflowManager, Workflow, Trigger, Persona, Channel

@pytest.fixture
def workflow_manager():
    return WorkflowManager()

@pytest.fixture
def sample_workflow():
    return Workflow(Trigger("Salesforce"), Persona("GPT-3", "AI Sales Agent"), Channel("WhatsApp"))

def test_add_workflow(workflow_manager: WorkflowManager, sample_workflow: Workflow):
    workflow_manager.add_workflow(sample_workflow)
    workflows = workflow_manager.list_workflows()
    assert len(workflows) == 1
    assert workflows[0] == sample_workflow

def test_get_workflow(workflow_manager: WorkflowManager, sample_workflow: Workflow):
    workflow_manager.add_workflow(sample_workflow)
    workflows = workflow_manager.get_workflow("Salesforce")
    assert len(workflows) == 1
    assert workflows[0] == sample_workflow

def test_remove_workflow(workflow_manager: WorkflowManager, sample_workflow: Workflow):
    workflow_manager.add_workflow(sample_workflow)
    workflow_manager.remove_workflow("Salesforce")
    workflows = workflow_manager.list_workflows()
    assert len(workflows) == 0
