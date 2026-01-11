import uuid

from langchain.agents import create_agent
from utils.model import dynamic_model_selection, basic_model
from utils.tools import tools


system_prompt = """This is a generic agent template using Langgraph's prebuilt agent.

"""

workflow = create_agent(
    basic_model, 
    tools=tools,
    middleware=[dynamic_model_selection]
)

async def chat():
    thread_id = str(uuid.uuid4())
    while True:
        user_input = input("User: ").strip()

        if user_input.lower() in ['quit', 'exit']:
            print("Ending chat session.")
            break

        if not user_input:
            continue

        try:
            response = workflow.invoke(
                {"messages": [{"role": "user", "content": user_input}]},
                config={"configurable": {"thread_id": thread_id}}
            )

            # Extract and print the agent's response
            if response and "messages" in response:
                last_message = response["messages"][-1]
                print(f"\nAgent: {last_message.content}\n")
            else:
                print("\nAgent: (No response)\n")

        except Exception as e:
            print(f"\nError: {e}\n")