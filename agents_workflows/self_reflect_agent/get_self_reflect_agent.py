import os

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.tool_context import ToolContext
from agents_workflows.self_reflect_agent.prompt.get_self_reflect_prompt import  get_self_reflect_prompt
from dotenv import load_dotenv

from global_tools.exit_loop_tool import exit_loop_tool
load_dotenv()



def get_self_reflect_agent():
    return LlmAgent(
        name="self_reflect_agent",
        model=os.getenv("MODEL") or "gemini-2-flash",
        instruction=get_self_reflect_prompt(),
        description="A looping agent workflow where 2 agents act as one with self reflection.",
        tools=[exit_loop_tool],

        output_key="last_reflect",
    )
