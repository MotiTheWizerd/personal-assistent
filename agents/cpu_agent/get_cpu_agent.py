from google.adk.agents.llm_agent import LlmAgent
from agents.cpu_agent.prompt.get_cpu_agent_prompt import get_cpu_agent_prompt
from agents.cpu_agent.tools.execute_command_tool import execute_command
from agents.cpu_agent.tools.execute_powershell import execute_powershell
def get_cpu_agent():
    return LlmAgent(
        name="cpu_agent",
        model="gemini-2.0-flash", 
        instruction=get_cpu_agent_prompt(),
        description="an agent the assist main the windows 11",
        tools=[
            execute_command,
            execute_powershell
        ]
    )
