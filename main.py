import asyncio
import uuid
from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.runners import Runner
from agents.cpu_agent.get_cpu_agent import get_cpu_agent
from utils.llm.call_agent_async import call_agent_async
from agents.task_planner_agent.get_task_planner_agent import get_task_planner_agent
from agents_workflows.self_reflect_agent_workflow import get_self_reflect_agent_workflow

load_dotenv()




async def main():
    print('in main')
    
    APP_NAME="cpu-agent"
    SESSION_ID = str(uuid.uuid4())
    USER_ID = "user-1"

    state = {
        "user_request": "",
        "task_for_powershell_script_writer": "",
        "last_response" : "",
        "last_reflect" : ""
    }
    # Initialize session service
    # InMemorySessionService is used for demonstration purposes; replace with your session management solution.
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, session_id=SESSION_ID, user_id=USER_ID, state=state)
    root_agent = SequentialAgent(
        name="team_manager_agent",
        description="a manager that act as a pipe flow for agents team.",
        sub_agents=[get_task_planner_agent(),  get_self_reflect_agent_workflow(get_cpu_agent())],
    )
    runner = Runner(app_name=APP_NAME, agent=root_agent, session_service=session_service)
    while True:
        # Small matrix effect before each prompt (very brief)
        # matrix_effect(0.3)
        is_session_debug = False
        if is_session_debug:
            # Print session state for debugging
            print("--- Session State for User ID:", USER_ID, "Session ID:", SESSION_ID, "---")
            print("user_request:", session.state["user_request"])
            print("task_for_powershell_script_writer:", session.state["task_for_powershell_script_writer"])
        user_input = input("Say something: ")
        session.state["user_request"] = user_input
        if user_input.lower() == "exit":
            # Exit sequence
            break
        else:
            # Process the message
            response = await call_agent_async(
                runner=runner,
                user_id=USER_ID, 
                session_id=SESSION_ID, 
                message=user_input
            )

        # ✨ pull the updated state AFTER the run
        session = await session_service.get_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID,
        )
          
if __name__ == "__main__":
    asyncio.run(main())