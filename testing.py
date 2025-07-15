import asyncio
import uuid
from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from agents_workflows.self_reflect_agent_workflow import get_self_reflect_agent_workflow
from google.adk.runners import Runner
from utils.llm.call_agent_async import call_agent_async


load_dotenv()




async def main():
    print('in main')
    
    APP_NAME="test-project"
    SESSION_ID = str(uuid.uuid4())
    USER_ID = "user-1"

    state = {
        "goal": "",
        "last_response": "",
        "last_reflect": "",
    }
    # Initialize session service
    # InMemorySessionService is used for demonstration purposes; replace with your session management solution.
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, session_id=SESSION_ID, user_id=USER_ID, state=state)
    
    story_agent_clone = LlmAgent(
        name="story_agent",
        model="gemini-2.0-flash",
        instruction="Generate a short story based on the user's input.",
        description="An agent that generates creative stories.",
        output_key="last_response",
    )
   
    self_reflect_workflow = get_self_reflect_agent_workflow(story_agent_clone)

   
    runner = Runner(app_name=APP_NAME, agent=self_reflect_workflow, session_service=session_service)
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
        session.state["goal"] = user_input
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