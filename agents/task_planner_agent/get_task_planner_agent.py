from google.adk.agents.llm_agent import LlmAgent
from agents.task_planner_agent.prompt.get_task_planner_prompt import get_task_planner_prompt
from agents.cpu_agent.tools.execute_command_tool import execute_command
from agents.cpu_agent.tools.execute_powershell import execute_powershell
def get_task_planner_agent():
    return LlmAgent(
        name="task_planner_agent",
        model="gemini-2.0-flash", 
        instruction=get_task_planner_prompt(),
        description="an agent the assist main the windows 11",
        output_key="task_for_powershell_script_writer",
    )
