from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
import os


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError(
        "API key not found! Please set OPENAI_API_KEY environment variable."
    )


basic_model = ChatOpenAI(
    model="gpt-5-mini",
    api_key=openai_api_key
)
advanced_model = ChatOpenAI(
    model="gpt-5",
    api_key=openai_api_key
)

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        model = advanced_model
    else:
        model = basic_model

    return handler(request.override(model=model))