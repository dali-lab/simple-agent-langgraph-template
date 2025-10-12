from langchain_ollama import ChatOllama

model = ChatOllama(
    model="gpt-oss:20b",
    temperature=0
)