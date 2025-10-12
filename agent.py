import uuid

from langgraph.prebuilt import create_react_agent
from utils.model import model
from utils.state import CustomState
from utils.tools import addition


system_prompt = """This is a generic agent template using Langgraph's prebuilt agent.

"""

workflow = create_react_agent(
    name="react-agent-template",
    model=model,
    state_schema=CustomState,
    prompt=system_prompt,
    tools=[addition],
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