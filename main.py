import asyncio
import uuid
from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from agents.cpu_agent.get_cpu_agent import get_cpu_agent
from utils.llm.call_agent_async import call_agent_async

load_dotenv()




async def main():
    print('in main')
    
    APP_NAME="cpu-agent"
    SESSION_ID = str(uuid.uuid4())
    USER_ID = "user-1"

    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, session_id=SESSION_ID, user_id=USER_ID)
    
    runner = Runner(app_name=APP_NAME, agent=get_cpu_agent(), session_service=session_service)
    while True:
        # Small matrix effect before each prompt (very brief)
        # matrix_effect(0.3)
        
        # Get user input with Matrix-style prompt
        user_input = input("Say something: ")
        
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
          
if __name__ == "__main__":
    asyncio.run(main())