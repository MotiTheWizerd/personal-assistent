from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.loop_agent import LoopAgent
from agents_workflows.self_reflect_agent.get_self_reflect_agent import get_self_reflect_agent
load_dotenv()


def get_self_reflect_agent_workflow(agent : LlmAgent):
    """
    Returns a self-reflecting agent workflow that loops between two agents that acts as one thinking machinisim.
    """
    self_reflect_workflow = LoopAgent(
        name="self_reflect_agent_workflow",
        sub_agents=[agent, get_self_reflect_agent()],
        max_iterations=2
       
    )
    return self_reflect_workflow
