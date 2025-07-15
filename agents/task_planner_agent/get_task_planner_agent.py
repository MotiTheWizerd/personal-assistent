import os
from google.adk.agents.llm_agent import LlmAgent
from agents.task_planner_agent.prompt.get_task_planner_prompt import get_task_planner_prompt

def get_task_planner_agent():
    print("get_task_planner_agent called")
    return LlmAgent(
        name="task_planner_agent",
        model=os.getenv("MODEL") or "gemini-2.0-flash",
        instruction=get_task_planner_prompt(),
        description="an agent that interprets user requests and generates actionable task plans for a system management agent on Windows 11.",
        output_key="task_for_powershell_script_writer",
    )
